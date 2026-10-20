"""Step 35: regular-center rigidity of the RESTRICTED flat spherical HR secondary.

The input bracket formula is the previously cross-checked Step33f restricted
mixed functional bracket, NOT a newly proven generic Dirac secondary.
Assumptions: flat spherical L_i=a_i, S_i=a_i*r, comoving two dusts,
pL_i=r**2 P_i, pS_i=(pL_i)', regular nonzero HR shift branch J(y).
No lapse/time evolution, curved 3-metric, or general BD rank is inferred.
"""
from dataclasses import dataclass
import math
import numpy as np
from numpy.polynomial import Polynomial as Poly

BETAS = (0., 1., -4.2383993109, 13.6801214252, -38.5117901844)
M2 = 23.3348939346
MG2 = 1.
MF2 = .10879548725**2
Y04 = .5787707228025044
CG = .9


def j_value(y, betas=BETAS):
    """Nondegenerate relative shift polynomial J=beta1+2 beta2*y+beta3*y²."""
    return betas[1] + 2*betas[2]*y + betas[3]*y*y


def j_roots(betas=BETAS):
    return np.roots([betas[3], 2*betas[2], betas[1]])


@dataclass(frozen=True)
class FlatData:
    a: float
    b: float
    Pg: Poly
    Pf: Poly
    betas: tuple = BETAS
    m2: float = M2
    mg2: float = MG2
    mf2: float = MF2

    def check(self):
        if self.a <= 0 or self.b <= 0 or self.mg2 <= 0 or self.mf2 <= 0:
            raise ValueError("positive scales and Planck masses required")
        if self.m2 <= 0 or abs(j_value(self.b/self.a,self.betas)) < 1.e-12:
            raise ValueError("degenerate mass/J; reduced shift oracle does not apply")

    def x(self):
        return self.Pg/(self.mg2*self.a) - self.Pf/(self.mf2*self.b)

    def secondary_polynomial(self):
        """C = (m² Mg² a² J/2) * derivative[r³ X(r)]."""
        self.check()
        r=Poly([0.,1.])
        return .5*self.m2*self.mg2*self.a**2*j_value(self.b/self.a,self.betas)*(r**3*self.x()).deriv()

    def dust_density_over_r2(self):
        """Both lapse constraints solved separately, never identify dust momenta."""
        self.check()
        y=self.b/self.a
        z=self.betas
        V=z[0]+3*z[1]*y+3*z[2]*y*y+z[3]*y**3
        W=z[1]+3*z[2]*y+3*z[3]*y*y+z[4]*y**3
        r=Poly([0.,1.])
        g=((3*self.Pg**2/4+r*self.Pg*self.Pg.deriv()/2) /
           (self.mg2*self.a) -self.m2*self.mg2*self.a**3*V)
        f=((3*self.Pf**2/4+r*self.Pf*self.Pf.deriv()/2) /
           (self.mf2*self.b) -self.m2*self.mg2*self.a**3*W)
        return g,f

    def primary_residuals(self, r):
        """Direct original (non-IBP) flat EH+HR lapse and momentum constraints."""
        self.check()
        if not 0 < r <= 1: raise ValueError("interior positive radius required")
        y=self.b/self.a; z=self.betas
        V=z[0]+3*z[1]*y+3*z[2]*y*y+z[3]*y**3
        W=z[1]+3*z[2]*y+3*z[3]*y*y+z[4]*y**3
        pLg=r*r*self.Pg(r); pLf=r*r*self.Pf(r)
        pSg=2*r*self.Pg(r)+r*r*self.Pg.deriv()(r)
        pSf=2*r*self.Pf(r)+r*r*self.Pf.deriv()(r)
        pg,pf=self.dust_density_over_r2()
        Hg=(pLg*pLg/(4*self.mg2*self.a*r*r)-
            pLg*pSg/(2*self.mg2*self.a*r)+r*r*pg(r)+
            self.m2*self.mg2*self.a**3*r*r*V)
        Hf=(pLf*pLf/(4*self.mf2*self.b*r*r)-
            pLf*pSf/(2*self.mf2*self.b*r)+r*r*pf(r)+
            self.m2*self.mg2*self.a**3*r*r*W)
        Dg=self.a*pSg-self.a*(2*r*self.Pg(r)+r*r*self.Pg.deriv()(r))
        Df=self.b*pSf-self.b*(2*r*self.Pf(r)+r*r*self.Pf.deriv()(r))
        return np.array([Hg,Hf,Dg,Df,Dg+Df],float)


def synchronized_candidate(eps=.08, a=.4, y=Y04):
    """Radially nonconstant regular primary+restricted-secondary witness."""
    if not math.isfinite(eps) or abs(eps) > .2:
        raise ValueError("restrict to explicit positive dust neighborhood")
    b=a*y
    vg=BETAS[0]+3*BETAS[1]*y+3*BETAS[2]*y*y+BETAS[3]*y**3
    H2=CG/(3*a**3)+M2*vg/3
    if H2<=0:raise ArithmeticError("nonpositive squared expansion")
    Pg=Poly([-2*MG2*a*a*math.sqrt(H2)]) * Poly([1., eps, .4*eps])
    Pf=Pg*(MF2*b/(MG2*a))
    out=FlatData(a,b,Pg,Pf)
    out.check()
    return out


def polynomial_interval_minimum(poly, left=0.,right=1.):
    """Exact-in-polynomial critical-point search, not a finite sampling claim."""
    if not left<right:raise ValueError("nonempty interval required")
    critical=np.roots(poly.deriv().coef[::-1]) if poly.degree()>1 else []
    xs=[left,right]+[float(x.real) for x in critical
                      if abs(x.imag)<1.e-10 and left<x.real<right]
    return min((float(poly(x)),x) for x in xs)


def regular_inverse_rhs(coefficients):
    """Solve 3 X + r X' = f(r), regular at center, on polynomial coefficients.

    If f=sum f_n r^n, X=sum f_n/(n+3) r^n. The omitted homogeneous
    C/r^3 is singular unless C=0.
    """
    return Poly([c/(n+3) for n,c in enumerate(coefficients)])


def candidate_y(a, nmin=2):
    """Same Candidate-C no-radiation quartic continuation, for J branch survey."""
    if not .025<=a<=1:raise ValueError("sampled Candidate C domain")
    c=(3*.23958426762*.5568825591873054**3)
    prev=.5568825591873054
    for aa in np.geomspace(1.,a,max(nmin,int(140*abs(math.log(a)))+2)):
        bs=BETAS
        co=[MF2*M2*bs[3]/3,MF2*M2*bs[2]-M2*bs[4]/3,
            MF2*M2*bs[1]-M2*bs[3],
            MF2*CG/(3*aa**3)-M2*bs[2],
            -c/(3*aa**3)-M2*bs[1]/3]
        roots=np.roots(co)
        positive=[z.real for z in roots if abs(z.imag)<1e-8 and z.real>0]
        if not positive:raise ArithmeticError("quartic root continuation failed")
        prev=min(positive,key=lambda v:abs(math.log(v/prev)))
    return float(prev)
