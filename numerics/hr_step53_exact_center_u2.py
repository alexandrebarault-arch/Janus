"""Exact local U2 recurrence for original spherical primary-reduced C=0.

This performs two evaluations of the genuine Step46 pLf_prime_rhs over
Q(sqrt(H2)) Laurent jets. The first determines U1 and the second U2. The
result concerns the stated rationalized benchmark only, NOT global radial
continuation, matter positivity on the continuum or Dirac time preservation.
"""
from __future__ import annotations
from fractions import Fraction as F
import os
from math import isqrt
from functools import lru_cache
import json
import sympy as sp
from .hr_step46_exact_secondary_ode import exact_f_momentum_ode

H2=None
class Q:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):self.a=F(a);self.b=F(b)
    @staticmethod
    def c(x):return x if isinstance(x,Q) else Q(x)
    def __add__(self,b):
        if isinstance(b,J):return NotImplemented
        b=Q.c(b);return Q(self.a+b.a,self.b+b.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,b):return self+-Q.c(b)
    def __rsub__(self,b):return Q.c(b)+-self
    def __mul__(self,b):
        if isinstance(b,J):return NotImplemented
        b=Q.c(b);return Q(self.a*b.a+self.b*b.b*H2,self.a*b.b+self.b*b.a)
    __rmul__=__mul__
    def inv(self):
        n=self.a*self.a-self.b*self.b*H2
        if not n:raise ZeroDivisionError('Q has zero norm')
        return Q(self.a/n,-self.b/n)
    def __truediv__(self,b):return self*Q.c(b).inv()
    def __rtruediv__(self,b):return Q.c(b)*self.inv()
    def __bool__(self):return bool(self.a or self.b)
    def __eq__(self,b):
        b=Q.c(b);return self.a==b.a and self.b==b.b
    def __pow__(self,n):
        if not isinstance(n,int):raise ValueError
        if n<0:return self.inv()**(-n)
        out=Q(1);v=self
        while n:
            if n&1:out=out*v
            n//=2
            if n:v=v*v
        return out

ORDER=int(os.environ.get("JANUS_JET_ORDER","14"))
if not 12<=ORDER<=28:raise ValueError("Jet order 12..28 required")
INF=10**9
class J:
    __slots__=('d','cutoff')
    def __init__(self,d=None,cutoff=INF):
        d=d or {}
        self.d={int(k):Q.c(v) for k,v in d.items() if v and k<=ORDER}
        self.cutoff=min(cutoff,ORDER+1) if any(v and k>ORDER for k,v in d.items()) else cutoff
    @staticmethod
    def c(x):return x if isinstance(x,J) else J({0:Q.c(x)})
    def val(self):return min(self.d) if self.d else (self.cutoff if self.cutoff!=INF else None)
    def __add__(self,b):
        b=J.c(b);d=self.d.copy()
        for k,v in b.d.items():d[k]=d.get(k,Q())+v
        return J(d,min(self.cutoff,b.cutoff))
    __radd__=__add__
    def __neg__(self):return J({k:-v for k,v in self.d.items()},self.cutoff)
    def __sub__(self,b):return self+-J.c(b)
    def __rsub__(self,b):return J.c(b)+-self
    def __mul__(self,b):
        b=J.c(b);d={};v1=self.val();v2=b.val()
        if v1 is None or v2 is None:return J()
        cutoff=min(self.cutoff+v2,b.cutoff+v1)
        for i,x in self.d.items():
            for j,y in b.d.items():
                if i+j<=ORDER:d[i+j]=d.get(i+j,Q())+x*y
                else:cutoff=min(cutoff,ORDER+1)
        return J(d,cutoff)
    __rmul__=__mul__
    def inv(self):
        if not self.d:raise ZeroDivisionError
        v=self.val()
        maximum=max(0,ORDER+v)
        a=[self.d.get(v+i,Q()) for i in range(maximum+1)]
        ans=[a[0].inv()]
        for n in range(1,maximum+1):
            summ=Q()
            for k in range(1,n+1):summ=summ+a[k]*ans[n-k]
            ans.append(-summ*ans[0])
        return J({-v+i:x for i,x in enumerate(ans) if x},min(ORDER+1,self.cutoff-2*v))
    def __truediv__(self,b):return self*J.c(b).inv()
    def __rtruediv__(self,b):return J.c(b)*self.inv()
    def __pow__(self,n):
        if n==0:return J.c(1)
        if n<0:return self.inv()**(-n)
        out=J.c(1);v=self
        while n:
            if n&1:out=out*v
            n//=2
            if n:v=v*v
        return out
    def sqrt(self):
        v=self.val()
        if v is None:return J()
        if v%2:raise ValueError('sqrt odd Laurent power')
        a=[self.d.get(v+i,Q()) for i in range(ORDER+abs(v)+5)]
        if a[0]!=Q(1):raise ValueError('non-unit sqrt leading term')
        result=[Q(1)]
        for n in range(1,ORDER-v//2+1):
            summ=Q()
            for k in range(1,n):summ=summ+result[k]*result[n-k]
            result.append((a[n]-summ)/2)
        return J({v//2+i:x for i,x in enumerate(result) if x},min(ORDER+1,self.cutoff-v//2))


def background():
    global H2
    a=F('.4');y=F('.5787707228025044');b=a*y;mg=F(1);mf=F('.10879548725')**2;m2=F('23.3348939346')
    beta=list(map(F,('0','1','-4.2383993109','13.6801214252','-38.5117901844')))
    H2=F('.9')/(3*a**3)+m2*(beta[0]+3*beta[1]*y+3*beta[2]*y*y+beta[3]*y**3)/3
    r=J({1:Q(1)});s=r*r;H=Q(0,1)
    cg=F('.0015');cf=F('-.0012');z1=F('.004');kg=F('.0012');kf=F('-.0016')
    b0,b1,b2,b3,b4=beta
    ug=1+cg*s;uf=1+cf*s;Lg=a*ug**2;Lf=b*uf**2;Sg=r*Lg;Sf=r*Lf
    Lgr=4*a*cg*r*ug;Lfr=4*b*cf*r*uf
    Sgr=a*ug*(1+5*cg*s);Sfr=b*uf*(1+5*cf*s)
    Pg=-2*a*a*H;plg=Pg*s*(1+F(5,2)*cg*s);plgr=2*r*(1+5*cg*s)*Pg
    trg=kg*r*Lg;trf=kf*r*Lf;z=z1*r;root=(1-z*z).sqrt()
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf;A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf;Af=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    K=m2*mg*Lg*Lf*At;Dg=K*z/root;Wg=m2*mg*(Lg*A0+Lf*At*root);Wf=m2*mg*(Lf*Af+Lg*At*root)
    Rg=-48*cg/(a*a*ug**5);Rf=-48*cf/(b*b*uf**5)
    fac=plg/(2*mg*Sg*Sgr);kin=Lg*plg**2/(4*mg*Sg**2);curvature=-mg*Lg*Sg*Sg*Rg/2
    numerator=kin-fac*(Dg+Lg*plgr)+curvature+z*Dg/Lg+Wg
    beta_g=(1+(trg/Lg)**2).sqrt()+fac*trg
    pg=-numerator/beta_g;psg=(Dg+Lg*plgr-pg*trg)/Sgr
    U0=mf*b*(Pg/(mg*a)-2*z1)
    fields={'Lg':Lg,'Lf':Lf,'Sg':Sg,'Sf':Sf,'pLg':plg,'pLf':s*U0,
        'pSg':psg,'pg':pg,'Lgr':Lgr,'Lfr':Lfr,'Sgr':Sgr,'Sfr':Sfr,
        'pLgr':plgr,'tgr':trg,'tfr':trf,'Mg2':mg,'Mf2':mf,'m2':m2,
        **{f'beta{i}':x for i,x in enumerate(beta)},'z':z,'zr':z1,'zrr':0,
        'Dg_original':Dg,'Wf_original':Wf,'R3f_original':Rf}
    return fields,r,s,U0

@lru_cache(None)
def physical_rhs():return exact_f_momentum_ode()['pLf_prime_rhs']

def evaluate(expr,fields):
    cache={}
    def inner(e):
        if e in cache:return cache[e]
        if e.is_Symbol:v=J.c(fields[str(e)])
        elif e.is_Rational:v=J.c(F(int(e.p),int(e.q)))
        elif e.is_Add:
            v=J()
            for a in e.args:v+=inner(a)
        elif e.is_Mul:
            v=J.c(1)
            for a in e.args:v*=inner(a)
        elif e.is_Pow:
            v=inner(e.base);x=e.exp
            if x.is_Integer:v=v**int(x)
            elif x.q==2 and x.p in (1,-1):v=v.sqrt() if x.p==1 else v.sqrt().inv()
            else:raise TypeError(f'power {x}')
        else:raise TypeError(type(e))
        cache[e]=v;return v
    ans=inner(expr)
    return ans,len(cache)


def exact_u2():
    fields,r,s,U0=background()
    expr=physical_rhs()
    first,n1=evaluate(expr,fields)
    if first.cutoff<=5:raise AssertionError('unknown first-jet remainder contaminates order 5')
    if first.d.get(1,Q())!=2*U0 or first.d.get(0,Q()) or first.d.get(2,Q()) or first.d.get(4,Q()):
        raise AssertionError('first odd parity/center coefficient inconsistent')
    U1=first.d.get(3,Q())/5
    fields['pLf']=s*(U0+U1*s)
    second,n2=evaluate(expr,fields)
    if second.cutoff<=5:raise AssertionError('unknown second-jet remainder contaminates order 5')
    if second.d.get(1,Q())!=2*U0 or second.d.get(3,Q())!=4*U1:
        raise AssertionError('exact U1 substitution does not reconstruct r^3 coefficient')
    if any(second.d.get(k,Q()) for k in (0,2,4,6)):
        raise AssertionError('odd spherical parity violated')
    U2=second.d.get(5,Q())/7
    return {'U0':U0,'U1':U1,'U2':U2,'H2':H2,'first_cutoff':first.cutoff,
            'second_cutoff':second.cutoff,'nodes_first':n1,'nodes_second':n2,
            'central_r1_correct':True,'central_r3_correct':True}


def rational_interval(q,digits=100):
    if not H2>0:raise ValueError('H2 not positive')
    grid=10**digits
    lo=F(isqrt((H2.numerator*grid*grid)//H2.denominator),grid)
    hi=lo+F(1,grid)
    assert lo*lo<=H2<=hi*hi
    low=q.a+q.b*(lo if q.b>=0 else hi)
    high=q.a+q.b*(hi if q.b>=0 else lo)
    if low>high:raise AssertionError('reversed')
    return low,high


def exact_certificate():
    vals=exact_u2()
    import mpmath as mp
    mp.mp.dps=110
    def display(q):return mp.nstr(mp.mpf(q.a.numerator)/q.a.denominator+mp.mpf(q.b.numerator)/q.b.denominator*mp.sqrt(mp.mpf(H2.numerator)/H2.denominator),65)
    lo,hi=rational_interval(vals['U2'])
    return {'step':53,'formula':'pLf(r)=r²[U0+U1*r²+U2*r⁴+O(r⁶)]',
         'U1_A':str(vals['U1'].a),'U1_B':str(vals['U1'].b),
         'U2_A':str(vals['U2'].a),'U2_B':str(vals['U2'].b),
         'H2':str(H2),'U1_decimal':display(vals['U1']),'U2_decimal':display(vals['U2']),
         'U2_lower_fraction':str(lo),'U2_upper_fraction':str(hi),
         'U2_enclosure_width_less_than_1e_minus_80':hi-lo<F(1,10**80),
         'jet_order':ORDER,'first_unknown_power':vals['first_cutoff'],
         'second_unknown_power':vals['second_cutoff'],
         'source':'exact algebraic original six-pair spherical primary-reduced C; rationalized benchmark',
         'global_radial_solution':'NOT_CERTIFIED','full_Dirac_time_preservation':'NOT_COMPUTED',
         'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(exact_certificate(),indent=2))
