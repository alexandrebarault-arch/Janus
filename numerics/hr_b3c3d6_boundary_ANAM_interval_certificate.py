"""Rigorous directed-rational enclosure of original Step58 A_N/A_M at four Step55 radii.

Conditional on the exact physical Step55 endpoint tubes SHA-verified below.
This is a special constrained spherical spatial branch, not a global Janus no-go.
"""
from fractions import Fraction as F
from math import isqrt
import sympy as sp
S=10**34

def ceil_div(a,b):return -((-a)//b)
class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        if self.lo>self.hi:raise ValueError('empty interval')
    @staticmethod
    def c(x):
        if isinstance(x,I):return x
        if isinstance(x,sp.Rational):x=F(int(x.p),int(x.q))
        if isinstance(x,str):x=F(x)
        if not isinstance(x,F):x=F(x)
        return I(x.numerator*S//x.denominator,ceil_div(x.numerator*S,x.denominator))
    @staticmethod
    def hull(a,b):
        a,b=F(a),F(b);return I(a.numerator*S//a.denominator,ceil_div(b.numerator*S,b.denominator))
    def __repr__(self):return f'[{self.lo/S:.12g},{self.hi/S:.12g}]'
    def __add__(self,y):
        if isinstance(y,Jet):return NotImplemented
        y=I.c(y);return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,y):
        if isinstance(y,Jet):return NotImplemented
        return self+-I.c(y)
    def __rsub__(self,y):return I.c(y)+-self
    def __mul__(self,y):
        if isinstance(y,Jet):return NotImplemented
        y=I.c(y);p=[a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return I(min(p)//S,ceil_div(max(p),S))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError(str(self))
        return I(S*S//self.hi,ceil_div(S*S,self.lo))
    def __truediv__(self,y):
        if isinstance(y,Jet):return NotImplemented
        return self*I.c(y).inv()
    def __rtruediv__(self,y):return I.c(y)*self.inv()
    def sqrt(self):
        if self.lo<0:raise ArithmeticError('negative sqrt '+str(self))
        l=isqrt(self.lo*S);h=isqrt(self.hi*S)
        return I(l,h+(h*h<self.hi*S))
    def __pow__(self,p):
        if isinstance(p,sp.Rational):p=F(int(p.p),int(p.q))
        if isinstance(p,float):p=F(str(p))
        if p==F(3,2):return self*self.sqrt()
        if p==F(-3,2):return (self*self.sqrt()).inv()
        if p==F(1,2):return self.sqrt()
        if p==F(-1,2):return self.sqrt().inv()
        if isinstance(p,F) and p.denominator==2:return (self**(p.numerator//2))*self.sqrt()
        if int(p)!=p:raise ValueError('power '+str(p))
        p=int(p)
        if p<0:return self.inv()**(-p)
        if p==0:return I.c(1)
        if p==1:return self
        if p%2==0 and self.lo<0<self.hi:
            t=max(self.lo*self.lo,self.hi*self.hi)
            return I(0,ceil_div(t,S))**(p//2)
        out=I.c(1);q=self
        while p:
            if p&1:out=out*q
            p//=2
            if p:q=q*q
        return out
    def __abs__(self):
        if self.lo>=0:return self
        if self.hi<=0:return -self
        return I(0,max(-self.lo,self.hi))
    def strictly_negative(self):return self.hi<0
    def strictly_positive(self):return self.lo>0

class Jet:
    """Third-order Taylor coefficients in local variable h=r-R."""
    __slots__=('a',)
    def __init__(self, coefficients):self.a=tuple(I.c(x) for x in coefficients);assert len(self.a)==4
    @staticmethod
    def c(x):
        if isinstance(x,Jet):return x
        return Jet((x,0,0,0))
    def __add__(self,y):
        y=Jet.c(y);return Jet([a+b for a,b in zip(self.a,y.a)])
    __radd__=__add__
    def __neg__(self):return Jet([-x for x in self.a])
    def __sub__(self,y):return self+-Jet.c(y)
    def __rsub__(self,y):return Jet.c(y)+-self
    def __mul__(self,y):
        y=Jet.c(y);return Jet([sum((self.a[k]*y.a[n-k] for k in range(n+1)),I.c(0)) for n in range(4)])
    __rmul__=__mul__
    def inv(self):
        ys=[self.a[0].inv()]
        for n in range(1,4):ys.append(-sum((self.a[k]*ys[n-k] for k in range(1,n+1)),I.c(0))*ys[0])
        return Jet(ys)
    def __truediv__(self,y):return self*Jet.c(y).inv()
    def __rtruediv__(self,y):return Jet.c(y)*self.inv()
    def sqrt(self):
        ys=[self.a[0].sqrt()]
        for n in range(1,4):
            ys.append((self.a[n]-sum((ys[k]*ys[n-k] for k in range(1,n)),I.c(0)))/(2*ys[0]))
        return Jet(ys)
    def __pow__(self,k):
        if isinstance(k,sp.Rational):k=F(int(k.p),int(k.q))
        if isinstance(k,float):k=F(str(k))
        if k==F(3,2):return self*self.sqrt()
        if k==F(-3,2):return (self*self.sqrt()).inv()
        if k==F(1,2):return self.sqrt()
        if k==F(-1,2):return self.sqrt().inv()
        if isinstance(k,F) and k.denominator==2:return (self**(k.numerator//2))*self.sqrt()
        if int(k)!=k:raise ValueError('bad jet power '+str(k))
        k=int(k)
        if k<0:return self.inv()**(-k)
        out=Jet.c(1);v=self
        while k:
            if k&1:out=out*v
            k//=2
            if k:v=v*v
        return out
    def val(self,n):return self.a[n]*(1 if n==0 else (1 if n==1 else 2 if n==2 else 6))

# Rational Step55 geometry and physical fields, with total r derivatives from Jet.
A=I.c('0.4');Y=I.c('0.5787707228025044');B=A*Y
MG=I.c(1);MF=I.c(F('0.10879548725')**2);M2=I.c('23.3348939346')
B0,B1,B2,B3,B4=(I.c(x) for x in ('0','1','-4.2383993109','13.6801214252','-38.5117901844'))
CG=I.c('0.0015');CF=I.c('-0.0012');KG=I.c('0.0012');KF=I.c('-0.0016');Z1=I.c('0.004')
H2=I.c('0.9')/(3*A**3)+M2*(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3
PG=-2*A**2*H2.sqrt()
U0=MF*B*(PG/A-2*Z1)
U1=I.hull('0.0007897451667202464909325108904961683602148118201690','0.0007897451667202464909325108904961683602148118201692')
U2=I.hull('-0.00001007385348674382817573689095286393593388364194376377344','-0.00001007385348674382817573689095286393593388364194376377342')

def physical_jet(r_value, u, us, uss):
    r=Jet((r_value,1,0,0));s=r*r;s0=I.c(r_value)**2;h=s-s0
    uc=u+us*h+uss*h*h/2
    ucp=us+uss*h
    # holonomic pLf and pLf_r used for on-shell physical field map.
    plf=s*uc;plfr=2*r*uc+2*r*s*ucp
    ug=1+CG*s;uf=1+CF*s
    Lg=A*ug**2;Lf=B*uf**2
    Sgr=A*ug*(1+5*CG*s);Sfr=B*uf*(1+5*CF*s)
    T=B1*Lg**2+2*B2*Lg*Lf+B3*Lf**2
    T0=B0*Lg**2+2*B1*Lg*Lf+B2*Lf**2
    Tf=B2*Lg**2+2*B3*Lg*Lf+B4*Lf**2
    root=(1-Z1**2*s).sqrt()
    Dbar=M2*MG*Lg*Lf*T*Z1/root
    Wgbar=M2*MG*(Lg*T0+Lf*T*root)
    Wfbar=M2*MG*(Lf*Tf+Lg*T*root)
    Rg=-48*CG/(A**2*ug**5);Rf=-48*CF/(B**2*uf**5)
    Gmom=PG*(1+I.c(F(5,2))*CG*s)
    Gprime=2*PG*(1+5*CG*s)
    fac=Gmom/(2*MG*Lg*Sgr)
    betag=(1+KG**2*s).sqrt()+s*fac*KG*Lg
    Rhog=-(Gmom**2/(4*MG*Lg)-fac*(s*Dbar+Lg*Gprime)-MG*Lg**3*Rg/2+s*Z1*Dbar/Lg+Wgbar)/betag
    Psg=(s*Dbar+Lg*Gprime-Rhog*s*KG*Lg)/Sgr
    Dg=r**3*Dbar;Wf=s*Wfbar;tfr=r*KF*Lf;z=Z1*r
    ffac=plf/(2*MF*r*Lf*Sfr)
    beta=(1+tfr**2/Lf**2).sqrt()
    kinetic=Lf*plf**2/(4*MF*(r*Lf)**2)
    curvature=-MF*Lf*(r*Lf)**2*Rf/2
    pf=-(kinetic-ffac*(-Dg+Lf*plfr)+curvature+z*Dg/Lf+Wf)/(beta+ffac*tfr)
    pSf=(-Dg+Lf*plfr-pf*tfr)/Sfr
    fields=dict(Lg=Lg,pLg=s*Gmom,Sg=r*Lg,pSg=r*Psg,tg=Jet.c(0),pg=s*Rhog,
        Lf=Lf,pLf=plf,Sf=r*Lf,pSf=pSf,tf=Jet.c(0),pf=pf)
    clocks={'tg':r*KG*Lg,'tf':r*KF*Lf}
    return fields,clocks

ARCHIVE_SHA='e74057dcf741bcdb655c7d9be48c6a9650d7ff3f'
ARCHIVE_ROWS={
    F(1,4): {
        'g': ('-104076228807029269821072203/10000000000000000000000000000','-102076838425701382920829307/10000000000000000000000000000'),
        'gs': ('38373221656832476910670573/10000000000000000000000000000','40420256921844014693305749/10000000000000000000000000000'),
        'gu': ('-4998928189051592003100216537/5000000000000000000000000000','-9996047435175684994736798723/10000000000000000000000000000'),
    },
    F(1,2): {
        'g': ('-98187618953991660998152359/10000000000000000000000000000','-96190121130234968103678743/10000000000000000000000000000'),
        'gs': ('38095244492510657368508881/10000000000000000000000000000','40154127409819940441797941/10000000000000000000000000000'),
        'gu': ('-9991127197007043106820836521/10000000000000000000000000000','-4991925520279942918235453341/5000000000000000000000000000'),
    },
    F(7,10): {
        'g': ('-90712238425015229936557581/10000000000000000000000000000','-22179325450335953301852061/2500000000000000000000000000'),
        'gs': ('18869277829506553448581743/5000000000000000000000000000','7962553151531274973700449/2000000000000000000000000000'),
        'gu': ('-623866559468158762101929391/625000000000000000000000000','-498375064261181354823145537/500000000000000000000000000'),
    },
    F(17,20): {
        'g': ('-1670739560678782324370567/200000000000000000000000000','-81544670093672108017750059/10000000000000000000000000000'),
        'gs': ('4674009208004524846989229/1250000000000000000000000000','1974065458319901039826603/500000000000000000000000000'),
        'gu': ('-9972203243542437579167143653/10000000000000000000000000000','-9950876159127644427090296099/10000000000000000000000000000'),
    },
}

def validate_archive(root):
    """Reject tampered physical input archive and reject copied-entry mismatches."""
    import json,hashlib
    data=(root/'research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json').read_bytes()
    sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if sha!=ARCHIVE_SHA:raise ValueError('physical interval archive SHA mismatch '+sha)
    rows=json.loads(data)['radii']
    if len(rows)!=4:raise ValueError('archive missing radius')
    for row in rows:
        r=F(row['r'])
        if r not in ARCHIVE_ROWS or F(row['s'])!=r*r:raise ValueError('archive radius')
        ref=ARCHIVE_ROWS[r]
        for key,old in [('G_monotone','g'),('G_s_composed','gs'),('G_U','gu')]:
            if tuple(row[key])!=tuple(ref[old]):raise ValueError('archive bound transcription mismatch '+str(r)+'/'+key)
    return True

def enclose_all(validate_archive_file=True,verbose=False):
    from pathlib import Path
    from numerics.hr_step45_exact_physical_ward import exact_physical_ward
    from numerics.hr_step58_temporal_operator import physical_operator
    from numerics.hr_b3c3d6_authentic_bn_replay import verify_blob_provenance
    verify_blob_provenance()
    if validate_archive_file:validate_archive(Path(__file__).resolve().parents[1])
    p=exact_physical_ward();op=physical_operator()
    funcs={}
    for label in ('N','M'):
        expr=op['operator'][label][0]
        syms=tuple(sorted(expr.free_symbols,key=str))
        if verbose:print('Compiling '+label, len(syms),sp.count_ops(expr),flush=True)
        funcs[label]=(syms,sp.lambdify(syms,expr,modules=[{'sqrt':lambda x:x.sqrt(),'Abs':abs},'math'],cse=True))
    output={}
    for r,archive in ARCHIVE_ROWS.items():
        si=I.c(r*r);du=I.c(F(1,10000))
        u=U0+U1*si+U2*si*si+I(-du.hi,du.hi)
        g,gs,gu=(I.hull(*archive[n]) for n in ('g','gs','gu'))
        assert gs.strictly_positive() and gu.strictly_negative() and g.strictly_negative()
        us=(g-2*u)/(2*si);uss=(gs+(gu-4)*us)/(2*si)
        f,clocks=physical_jet(r,Jet.c(u),Jet.c(us),Jet.c(uss))
        sub={}
        for name,var in zip(p['Q'],p['q']):sub[var]=f[name].val(0)
        for n,vec in [(1,op['qp']),(2,op['qpp']),(3,op['qppp'])]:
            for name,var in zip(p['Q'],vec):
                sub[var]=clocks[name].val(n-1) if name in clocks else f[name].val(n)
        sub[op['z']]=Z1*r;sub[op['zr']]=Z1;sub[op['zrr']]=I.c(0);sub[op['zrrr']]=I.c(0)
        sub.update(zip(p['parameters'][:8],(MG,MF,M2,B0,B1,B2,B3,B4)))
        vals={}
        for label,(syms,func) in funcs.items():
            vals[label]=func(*[sub[s] for s in syms]);assert isinstance(vals[label],I)
        vals['sum']=vals['N']+vals['M']
        output[str(r)]={'A_N':vals['N'],'A_M':vals['M'],'A_N_plus_A_M':vals['sum'],'U':u,'U_s':us,'U_ss':uss}
        if verbose:print('r',r,'AN',vals['N'],'AM',vals['M'],'sum',vals['sum'],flush=True)
    return output

def certified_report():
    import json
    bounds=enclose_all(validate_archive_file=True)
    result={}
    for r,row in bounds.items():
        result[r]={k:{'lower':f'{v.lo}/{S}','upper':f'{v.hi}/{S}'}
            for k,v in row.items()}
        assert row['A_N'].strictly_positive()
        assert row['A_M'].strictly_negative()
        assert row['A_N_plus_A_M'].strictly_negative()
    return {'scope':'CONDITIONAL_CERTIFIED_STEP55_PHYSICAL_BENCHMARK_FOUR_EXACT_RADII',
      'step45_step58':'EXACT_ORIGINAL_SYMBOLIC_OPERATORS_WITH_MINIMAL_STEP57_IMPORT_SHIM',
      'source_physical_interval_archive_blob':ARCHIVE_SHA,
      'lattice_denominator':str(S),'radii':result,
      'strict':{'A_N':'POSITIVE_ALL_FOUR','A_M':'NEGATIVE_ALL_FOUR',
                'A_N_plus_A_M':'NEGATIVE_ALL_FOUR'},
      'outer_equal_positive_lapses':'IMPOSSIBLE_ON_FULL_EXACT_SPATIAL_SHELL',
      'limitation':'NOT_A_GENERAL_JANUS_NO_GO_OR_FULL_TWO_LAPSE_BVP',
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    res=enclose_all(validate_archive_file=True,verbose=True)
    for r,row in res.items():
        print(r,'AN>0',row['A_N'].strictly_positive(),'AM<0',row['A_M'].strictly_negative(),'sum<0',row['A_N_plus_A_M'].strictly_negative())
