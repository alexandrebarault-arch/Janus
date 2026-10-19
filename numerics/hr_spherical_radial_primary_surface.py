"""A genuinely radial primary-constraint witness for spherical HR+TWO dust.

Spatial three-geometries in this restricted family are flat FLRW slices,
Lg=a, Sg=a*r, Lf=b, Sf=b*r; gravitational momenta and both *positive*
dust density momenta vary with r. All local primaries Hg=Hf=Ddiag=0 hold
pointwise, without imposing the mixed Hamiltonian (BD) secondary.

On this special submanifold, the mixed bracket local N*M coefficient is
    (m² Mg² a²/2) J(b/a) r² [3X(r)+r X'(r)],
    X=Pg(r)/(Mg²*a)-Pf(r)/(Mf²*b),
    pL_i=r² P_i(r), pS_i=pL_i'(r).
The relation is tested numerically against the FULL radial functional bracket
from Step33e; do NOT extrapolate it to arbitrary radially curved geometries,
non-comoving dust, lapse consistency or the full BD constraint algebra.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
import math
import numpy as np
from numpy.polynomial import Polynomial as Poly
from numerics.hr_spherical_local_mixed_kernel import local_mixed_kernel

CANDIDATE_BETAS=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
CANDIDATE_M2=23.3348939346
CANDIDATE_MG2=1.
CANDIDATE_MF2=.10879548725**2
CANDIDATE_Y0=.5568825591873054
CANDIDATE_CG=.9
CANDIDATE_CF=3*.23958426762*CANDIDATE_Y0**3


@lru_cache(maxsize=32)
def dust_candidate_y(a):
    """Independent dust-only quartic continuation; radiation excluded."""
    if not math.isfinite(a) or not .025<=a<=1.:
        raise ValueError('a in [.025,1] required')
    b0,b1,b2,b3,b4=CANDIDATE_BETAS
    y=CANDIDATE_Y0
    for A in np.geomspace(1.,a,max(2,int(140*abs(math.log(a)))+2)):
        c=[CANDIDATE_MF2*CANDIDATE_M2*b3/3,
           CANDIDATE_MF2*CANDIDATE_M2*b2-CANDIDATE_M2*b4/3,
           CANDIDATE_MF2*CANDIDATE_M2*b1-CANDIDATE_M2*b3,
           CANDIDATE_MF2*CANDIDATE_CG/(3*A**3)-CANDIDATE_M2*b2,
           -CANDIDATE_CF/(3*A**3)-CANDIDATE_M2*b1/3]
        roots=np.roots(c)
        positive=[x.real for x in roots if abs(x.imag)<1e-8 and x.real>0]
        if not positive:raise ArithmeticError('positive Candidate-C dust quartic branch lost')
        y=float(min(positive,key=lambda v:abs(math.log(v/y))))
    return y


@dataclass(frozen=True)
class PrimaryWitness:
    fields:dict[str,Poly]
    a:float
    b:float
    P_g:Poly
    P_f:Poly
    betas:tuple=CANDIDATE_BETAS
    m2:float=CANDIDATE_M2
    mg2:float=CANDIDATE_MG2
    mf2:float=CANDIDATE_MF2


def radial_primary_witness(*,a=.4,eps_g=.08,eps_f=-.06,
                            momentum_fraction=0.,synchronized=False):
    """Exact radially inhomogeneous Hg=Hf=Dg=Df=0 primary data.

    Parametrizes gravitational radial momenta by free polynomials Pg,Pf,
    chooses pS_i=pL_i' to enforce EACH momentum constraint, and separately
    solves Hg=0 and Hf=0 algebraically for positive dust momenta pg,pf.
    This does not impose the secondary mixed bracket or time evolution.
    """
    if not all(math.isfinite(v) for v in (eps_g,eps_f,momentum_fraction)):
        raise ValueError('finite radial momentum shape perturbations required')
    if max(abs(eps_g),abs(eps_f),abs(momentum_fraction))>.3:
        raise ValueError('test restricted to regular positive dust neighborhood')
    y=dust_candidate_y(a);b=a*y
    b0,b1,b2,b3,b4=CANDIDATE_BETAS
    vg=b0+3*b1*y+3*b2*y*y+b3*y**3
    vf=b1+3*b2*y+3*b3*y*y+b4*y**3
    H2=CANDIDATE_CG/(3*a**3)+CANDIDATE_M2*vg/3
    if H2<=0:raise ValueError('nonregular Friedmann background')
    H=math.sqrt(H2)
    pa=-6*CANDIDATE_MG2*a*a*H
    pb=-6*CANDIDATE_MF2*b*a*H
    r=Poly([0.,1.]);
    Pg=Poly([pa*(1+momentum_fraction)/3,pa*eps_g/3,pa*.4*eps_g/3])
    if synchronized:
        # Force X=0 IDENTICALLY while keeping both dust momenta positive;
        # gravitational momenta may still have independent radial gradients.
        Pf=Pg*(CANDIDATE_MF2*b/(CANDIDATE_MG2*a))
    else:
        Pf=Poly([pb/3,pb*eps_f/3,-pb*.3*eps_f/3])
    pg=r*r*((3*Pg*Pg/4+r*Pg*Pg.deriv()/2)/(CANDIDATE_MG2*a)
              -CANDIDATE_M2*CANDIDATE_MG2*a**3*vg)
    pf=r*r*((3*Pf*Pf/4+r*Pf*Pf.deriv()/2)/(CANDIDATE_MF2*b)
              -CANDIDATE_M2*CANDIDATE_MG2*a**3*vf)
    fields={
        'Lg':Poly([a]),'Sg':a*r,'pLg':r*r*Pg,'pSg':(r*r*Pg).deriv(),
        'tg':Poly([0.]),'pg':pg,
        'Lf':Poly([b]),'Sf':b*r,'pLf':r*r*Pf,'pSf':(r*r*Pf).deriv(),
        'tf':Poly([0.]),'pf':pf,
    }
    if min(min(float(pg(x)),float(pf(x))) for x in (.15,.4,.7))<=0:
        raise ValueError('negative dust test charge density')
    return PrimaryWitness(fields,a,b,Pg,Pf)


def primary_residuals(witness,r):
    """INDEPENDENT unintegrated spherical ADM primary density evaluation.

    Spatial R3=0 for the exactly flat L=a,S=a*r subfamily. The original
    non-IBP gravitational momentum scalar and full beta0..4 HR potentials
    are evaluated directly, with the two *separately* conserved dust phases.
    """
    if not math.isfinite(r) or not 0<r<1:raise ValueError('positive interior radius')
    w=witness;f=w.fields;a=w.a;b=w.b
    Pg=w.P_g(r);Pf=w.P_f(r)
    plg=f['pLg'](r);psg=f['pSg'](r)
    plf=f['pLf'](r);psf=f['pSf'](r)
    b0,b1,b2,b3,b4=w.betas;y=b/a
    V=b0+3*b1*y+3*b2*y*y+b3*y**3
    W=b1+3*b2*y+3*b3*y*y+b4*y**3
    Cg=a*plg**2/(4*w.mg2*(a*r)**2)-plg*psg/(2*w.mg2*(a*r))
    Cf=b*plf**2/(4*w.mf2*(b*r)**2)-plf*psf/(2*w.mf2*(b*r))
    Hg=Cg+f['pg'](r)+w.m2*w.mg2*a**3*r*r*V
    Hf=Cf+f['pf'](r)+w.m2*w.mg2*a**3*r*r*W
    Dg=psg*a-a*f['pLg'].deriv()(r)
    Df=psf*b-b*f['pLf'].deriv()(r)
    return np.array([Hg,Hf,Dg+Df,Dg,Df],float)


def local_secondary_candidate(witness,r):
    """Closed-form local mixed bracket coefficient on THIS primary surface.

    Derived as a diagnostic from the exact mixed functional Poisson bracket:
    K00 = (m² Mg² a² J/2) * r² * (3X+rX'), with
    X=Pg/(Mg² a)-Pf/(Mf² b). For constant Pg=pa/3,Pf=pb/3 this is
    r² times the independently known homogeneous minisuperspace bracket.
    """
    if not math.isfinite(r) or not 0<r<1:raise ValueError('interior radius required')
    w=witness
    y=w.b/w.a
    J=w.betas[1]+2*w.betas[2]*y+w.betas[3]*y*y
    X=w.P_g/(w.mg2*w.a)-w.P_f/(w.mf2*w.b)
    return .5*w.m2*w.mg2*w.a*w.a*J*r*r*(3*X(r)+r*X.deriv()(r))


def constrained_local_kernel(witness,r):
    """Direct FULL radial Poisson bracket on exact primary-satisfying data."""
    return local_mixed_kernel(witness.fields,r,betas=witness.betas,
            m2=witness.m2,mg2=witness.mg2,mf2=witness.mf2)
