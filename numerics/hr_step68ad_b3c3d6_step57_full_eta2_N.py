"""Exact outward integer enclosure for the previously omitted Step57 eta''*N
coefficient on prescribed Step55 geometry; no Step58 or Dirac conclusion.
Sources: original Step45 66aa43841dccfe4a5d586a49be9c10af3a67a10e,
Step55 a6e7004120d0a166a3a8973c2fbe1487a8eb70fe,
Step57 bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f.
"""
from fractions import Fraction as F
from math import isqrt
import json
import sympy as sp
SCALE=10**28
class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        if self.lo>self.hi:raise ValueError('invalid interval')
    @staticmethod
    def c(v):
        if isinstance(v,I):return v
        v=F(v)
        return I(v.numerator*SCALE//v.denominator,-((-v.numerator*SCALE)//v.denominator))
    @staticmethod
    def hull(a,b):
        a,b=F(a),F(b)
        return I(a.numerator*SCALE//a.denominator,-((-b.numerator*SCALE)//b.denominator))
    def __add__(self,o):
        o=I.c(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-I.c(o)
    def __rsub__(self,o):return I.c(o)+-self
    def __mul__(self,o):
        o=I.c(o);v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(v)//SCALE,-((-max(v))//SCALE))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('cross zero')
        return I((SCALE*SCALE)//self.hi,-((-SCALE*SCALE)//self.lo))
    def __truediv__(self,o):return self*I.c(o).inv()
    def __rtruediv__(self,o):return I.c(o)*self.inv()
    def __pow__(self,k):
        if k==0:return I.c(1)
        if k<0:return self.inv()**(-k)
        a=I.c(1);b=self
        while k:
            if k&1:a=a*b
            k//=2
            if k:b=b*b
        return a
    def sqrt(self):
        if self.lo<0:raise ValueError('negative sqrt')
        lo=isqrt(self.lo*SCALE);hi=isqrt(self.hi*SCALE)
        if hi*hi<self.hi*SCALE:hi+=1
        return I(lo,hi)
    def lt(self,o):return self.hi<I.c(o).lo
    def gt(self,o):return self.lo>I.c(o).hi
    def as_fraction_pair(self):return (F(self.lo,SCALE),F(self.hi,SCALE))
    def as_float_pair(self):return (self.lo/SCALE,self.hi/SCALE)

def consts():
    A=I.c(F(2,5));Y=I.c(F('0.5787707228025044'));B=A*Y
    MG=I.c(1);M2=I.c(F('23.3348939346'))
    B0,B1,B2,B3,B4=[I.c(F(x)) for x in ('0','1','-4.2383993109','13.6801214252','-38.5117901844')]
    CG=I.c(F('0.0015'));CF=I.c(F('-0.0012'));KG=I.c(F('0.0012'));Z1=I.c(F('0.004'))
    H2=I.c(F('0.9'))/(3*A**3)+M2*(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3
    PG=-2*A**2*H2.sqrt()
    return locals()

def coefficients(s,c):
    A=c['A'];B=c['B'];MG=c['MG'];M2=c['M2'];B0=c['B0'];B1=c['B1'];B2=c['B2'];B3=c['B3'];CG=c['CG'];CF=c['CF'];KG=c['KG'];Z1=c['Z1'];PG=c['PG']
    ug=1+CG*s;uf=1+CF*s
    lg=A*ug**2;lf=B*uf**2
    sgr=A*ug*(1+5*CG*s)
    Tbar=B1*lg**2+2*B2*lg*lf+B3*lf**2
    T0=B0*lg**2+2*B1*lg*lf+B2*lf**2
    root=(1-Z1**2*s).sqrt()
    Dbar=M2*MG*lg*lf*Tbar*Z1/root
    Wgbar=M2*MG*(lg*T0+lf*Tbar*root)
    Rg=-48*CG/(A**2*ug**5)
    Gmom=PG*(1+F(5,2)*CG*s)
    Gprime=2*PG*(1+5*CG*s)
    fac=Gmom/(2*MG*lg*sgr)
    betag=(1+KG**2*s).sqrt()+s*fac*KG*lg
    Rhog=-(Gmom**2/(4*MG*lg)-fac*(s*Dbar+lg*Gprime)-MG*lg**3*Rg/2+s*Z1*Dbar/lg+Wgbar)/betag
    Psg=(s*Dbar+lg*Gprime-Rhog*s*KG*lg)/sgr
    # T_N0/r² = k_g/r² + rho_g/beta_dust - mg*(Lg-Sgr²/Lg)/r² + m2*mg*Lg*A0/r²
    # Algebraic cancellation: Sgr²/Lg-Lg = A*s*(8CG+24CG²*s).
    T_over_s=(Gmom**2/(4*MG*lg)-Gmom*Psg/(2*MG*lg)
              +Rhog/(1+KG**2*s).sqrt()
              +MG*A*(8*CG+24*CG**2*s)
              +M2*MG*lg*T0)
    cN_over_s=-(1-Z1**2*s)*T_over_s/(lg*lf)
    cM_over_s=-M2*MG*Tbar*root/lf
    cNprime_over_r=-2*MG*sgr*(1-Z1**2*s)/(lg*lf)
    return {'cN_over_s':cN_over_s,'cM_over_s':cM_over_s,
            'cNprime_over_r':cNprime_over_r,'T_N0_over_s':T_over_s,
            'Rhog':Rhog,'betag':betag,'K_over_s':M2*MG*lg*lf*Tbar}

def symbolic_residuals():
    Lg,plg,Sg,psg,pg,Sgr,tgr,z,Lf,Sf,mg,m2,b0,b1,b2,b3=sp.symbols('Lg plg Sg psg pg Sgr tgr z Lf Sf mg m2 b0 b1 b2 b3',positive=True)
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    kg=Lg*plg**2/(4*mg*Sg**2)-plg*psg/(2*mg*Sg)
    Ag=kg+pg*sp.sqrt(1+tgr**2/Lg**2)-mg*Lg-mg*Sgr**2/Lg+m2*mg*(Lg*A0+Lf*At*sp.sqrt(1-z*z))+z*(psg*Sgr+pg*tgr)/Lg
    original=Lg*sp.diff(Ag,Lg)+psg*sp.diff(Ag,psg)+pg*sp.diff(Ag,pg)
    reduced=kg+pg/sp.sqrt(1+tgr**2/Lg**2)-mg*Lg+mg*Sgr**2/Lg+m2*mg*Lg*A0
    s,CG,A=sp.symbols('s CG A',real=True)
    ug=1+CG*s; Sgr_expr=A*ug*(1+5*CG*s);Lg_expr=A*ug**2
    residuals={
       'Step45_N0_contraction':sp.simplify(original-reduced),
       'Step55_Sgr_difference':sp.factor((Sgr_expr**2/Lg_expr-Lg_expr)-A*s*(8*CG+24*CG**2*s)),
       'Step57_Bbase_Fz_shell':sp.cancel(-sp.Symbol('K')**2/(Lg*Lf*sp.Symbol('R')**2)+(1-z*z)/(Lg*Lf)).subs(sp.Symbol('K')**2,sp.Symbol('R')**2*(1-z*z)),
    }
    for k,v in residuals.items():assert sp.simplify(v)==0,(k,v)
    return len(residuals)

def certificate(cells=256):
    assert isinstance(cells,int) and cells>=64
    c=consts(); sym=symbolic_residuals()
    smax=F(289,400)
    ranges={k:[10**40,-10**40] for k in ('cN_over_s','cM_over_s','cNprime_over_r','T_N0_over_s')}
    guards=0
    for i in range(cells):
        s=I.hull(smax*i/cells,smax*(i+1)/cells)
        row=coefficients(s,c)
        assert row['Rhog'].gt(0) and row['betag'].gt(0) and row['K_over_s'].gt(0)
        assert row['cN_over_s'].gt(F(6,1)),('cN sign',i,row['cN_over_s'].as_float_pair())
        assert row['cN_over_s'].lt(F(7,1)),('cN upper',i)
        assert row['cM_over_s'].lt(-F(10,1)),('cM sign',i)
        assert row['cNprime_over_r'].lt(-F(17,2)),('cNprime sign',i)
        guards+=7
        for k in ranges:
            v=row[k];ranges[k][0]=min(ranges[k][0],v.lo);ranges[k][1]=max(ranges[k][1],v.hi)
    center=coefficients(I.c(0),c)
    rho=I.hull(F(1037,2000),F(2593,5000))
    center_residual=center['cN_over_s']+center['cM_over_s']*rho
    center_n2=-center_residual/(2*center['cNprime_over_r'])
    assert center_residual.gt(0) and center_n2.gt(F(1,25)) and center_n2.lt(F(1,20))
    guards+=3
    return {
      'conditional_step58_center_ratio_bounds':['1037/2000','2593/5000'],
      'eta2_required_N2_over_N0_bounds':['1/25','1/20'],
      'eta2_center_residual_without_N2':list(map(str,center_residual.as_fraction_pair())),
      'scope':'Step57_eta2_N_coefficient_on_prescribed_Step55_not_original_Step58',
      'radius':'0<r<=17/20', 'cells':cells,'outward_integer_scale':'1e-28',
      'symbolic_residuals':sym,'rational_cell_sign_guards':guards,
      'uniform_enclosures':{k:[str(F(a,SCALE)),str(F(b,SCALE))] for k,(a,b) in ranges.items()},
      'uniform_signs':{'cN_over_r2':'>6','cM_over_r2':'<-10','cNprime_over_r':'<-17/2'},
      'full_eta2_central_relation':'cN2*N0+cM2*M0+2*cNprime1*N2=0 (for even C2 N,M)',
      'full_eta2_N2_dependence':'NONZERO; no forced central M0/N0 from this eta2 coefficient alone',
      'original_Step58_outer_probe_executed':False,'Dirac_rank':'NOT_COMPUTED',
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'
    }
if __name__=='__main__':print(json.dumps(certificate(),indent=2))
