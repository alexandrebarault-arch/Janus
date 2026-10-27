"""Independent exact-rational outward interval audit of the Step55 g-dust reconstruction
for Pg+lambda, |lambda|<=1/1000, on 0<=s<=289/400.
This does NOT run original Step45/46/55 modules and does NOT certify the f ODE.
"""
from fractions import Fraction as Q
from math import isqrt
import json

SCALE=10**34

def q(x): return Q(str(x))
def sqrt_bounds(x):
    assert x>=0
    n=x.numerator*SCALE*SCALE//x.denominator
    k=isqrt(n)
    lo=Q(k,SCALE)
    hi=Q(k+1,SCALE)
    assert lo*lo<=x<=hi*hi
    return lo,hi

class I:
    def __init__(self,lo,hi=None):
        if isinstance(lo,I): self.lo,self.hi=lo.lo,lo.hi;return
        self.lo=Q(lo);self.hi=Q(hi) if hi is not None else self.lo
        assert self.lo<=self.hi
    def __add__(self,o):
        o=I(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-I(o)
    def __rsub__(self,o):return I(o)+-self
    def __mul__(self,o):
        o=I(o);xs=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(xs),max(xs))
    __rmul__=__mul__
    def inv(self):
        assert self.lo>0 or self.hi<0,('denominator crosses zero',self)
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,o):return self*I(o).inv()
    def __rtruediv__(self,o):return I(o)*self.inv()
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n==1:return self
        if n%2==0:
            p=self**(n//2)
            if p.lo<=0<=p.hi:return I(0,max(p.lo*p.lo,p.hi*p.hi))
            return I(min(p.lo*p.lo,p.hi*p.hi),max(p.lo*p.lo,p.hi*p.hi))
        return self*(self**(n-1))
    def sqrt(self):
        assert self.lo>=0
        return I(sqrt_bounds(self.lo)[0],sqrt_bounds(self.hi)[1])
    def __repr__(self):return f'[{float(self.lo):.12g},{float(self.hi):.12g}]'

def parameters():
    a=q('.4');y=q('.5787707228025044');b=a*y
    mg=Q(1);mf=q('.10879548725')**2;m2=q('23.3348939346')
    b0,b1,b2,b3,b4=[q(v) for v in ('0','1','-4.2383993109','13.6801214252','-38.5117901844')]
    cg=q('.0015');cf=q('-.0012');kg=q('.0012');z1=q('.004')
    h2=q('.9')/(3*a**3)+m2*(b0+3*b1*y+3*b2*y*y+b3*y**3)/3
    assert h2>0
    sq=sqrt_bounds(h2)
    pg=I(-2*a*a*sq[1],-2*a*a*sq[0])
    return locals()

def evaluate(s,lam,p):
    a,b,mg,m2=p['a'],p['b'],p['mg'],p['m2']
    b0,b1,b2,b3=p['b0'],p['b1'],p['b2'],p['b3']
    cg,cf,kg,z1=p['cg'],p['cf'],p['kg'],p['z1']
    pg=p['pg']+lam
    ug=1+cg*s;uf=1+cf*s
    lg=a*ug**2;lf=b*uf**2
    sgr=a*ug*(1+5*cg*s)
    t=b1*lg**2+2*b2*lg*lf+b3*lf**2
    t0=b0*lg**2+2*b1*lg*lf+b2*lf**2
    root=(1-z1*z1*s).sqrt()
    dbar=m2*mg*lg*lf*t*z1/root
    wg=m2*mg*(lg*t0+lf*t*root)
    rg=-48*cg/(a*a*ug**5)
    gmom=pg*(1+Q(5,2)*cg*s)
    gprime=2*pg*(1+5*cg*s)
    fac=gmom/(2*mg*lg*sgr)
    beta=(1+kg*kg*s).sqrt()+s*fac*kg*lg
    rhog=-(gmom**2/(4*mg*lg)-fac*(s*dbar+lg*gprime)-mg*lg**3*rg/2+s*z1*dbar/lg+wg)/beta
    return {'rho_g':rhog,'beta_g':beta,'pg':pg,'lg':lg,'sgr':sgr,'root':root}

def certificate(cells=256,lam_bound=Q(1,1000)):
    p=parameters();lam=I(-lam_bound,lam_bound)
    minima={k:None for k in ('rho_g','beta_g','lg','sgr','root')}
    max_rho=None
    for j in range(cells):
        s=I(Q(289,400)*j/cells,Q(289,400)*(j+1)/cells)
        e=evaluate(s,lam,p)
        for key in minima:
            x=e[key].lo
            if minima[key] is None or x<minima[key]:minima[key]=x
        x=e['rho_g'].hi
        if max_rho is None or x>max_rho:max_rho=x
    assert all(v>0 for v in minima.values())
    # Strict exact rational witness lower bounds (coarser than actual enclosure).
    assert minima['rho_g']>Q(4,5), minima['rho_g']
    assert minima['beta_g']>Q(99,100), minima['beta_g']
    assert (p['pg']+lam).hi<0
    return {'step':'68ad-C2d2e5b3b2c2a','source':'independent transcription of Step55 g geometry / g-dust primary',
            'source_original_modules_reexecuted':False,'cells':cells,'s_interval':['0','289/400'],
            'lambda_interval':[str(-lam_bound),str(lam_bound)],
            'pg_interval':[str(p['pg'].lo),str(p['pg'].hi)],
            'strict_lower_bounds':{k:str(v) for k,v in minima.items()},
            'rho_g_upper_bound':str(max_rho),
            'certified':'positive g dust, positive g denominator and geometry for all s and lambda in box',
            'not_certified':'f dust, true G(s,U,Pg), sensitivity, global U continuation, boundary admissibility, Dirac rank, 4D',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(certificate(),indent=2,sort_keys=True))
