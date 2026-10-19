"""Exact HOMOGENEOUS two-dust bimetric Poisson secondary and lapse fixing.

Derives the minisuperspace constraint bracket and its time preservation using
TWO independent canonical dust clock/momentum pairs. The result is on the
homogeneous dynamical branch and does NOT constitute the spatially dependent
Hassan--Rosen BD secondary, full 4D ghost elimination, scalar sound speed or
new nonhomothetic on-shell solution. All dimensional constants are explicit.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_spherical_adm_primary import (
    Geometry, coupled_primary, solve_relative_shift
)


@dataclass(frozen=True)
class Parameters:
    betas: tuple[float, float, float, float, float]
    m2: float
    Mg2: float
    Mf2: float

    def validate(self):
        if len(self.betas)!=5 or not all(math.isfinite(float(x)) for x in
                (*self.betas,self.m2,self.Mg2,self.Mf2)):
            raise ValueError('five finite beta values and finite couplings required')
        if self.m2<0 or min(self.Mg2,self.Mf2)<=0:
            raise ValueError('positive EH Planck masses and nonnegative HR mass²')


@dataclass(frozen=True)
class PhasePoint:
    a: float
    b: float
    pa: float
    pb: float
    theta_g: float
    theta_f: float
    pg: float
    pf: float

    def validate(self):
        if not all(math.isfinite(float(x)) for x in vars(self).values()):
            raise ValueError('finite homogeneous canonical fields required')
        if min(self.a,self.b,self.pg,self.pf)<=0:
            raise ValueError('positive scales and TWO dust momenta required')

    def canonical_vector(self):
        # Canonical pairs (a,pa), (b,pb), (theta_g,pg), (theta_f,pf).
        return np.array([self.a,self.b,self.theta_g,self.theta_f,
                         self.pa,self.pb,self.pg,self.pf],float)


def from_vector(v):
    v=np.asarray(v,float)
    if v.shape!=(8,):raise ValueError('eight homogeneous phase-space variables required')
    return PhasePoint(v[0],v[1],v[4],v[5],v[2],v[3],v[6],v[7])


def beta_functions(par:Parameters,q:PhasePoint):
    par.validate();q.validate()
    y=q.b/q.a
    b0,b1,b2,b3,b4=par.betas
    V=b0+3*b1*y+3*b2*y*y+b3*y**3
    W=b1+3*b2*y+3*b3*y*y+b4*y**3
    A=b0+2*b1*y+b2*y*y
    J=b1+2*b2*y+b3*y*y
    K=b2+2*b3*y+b4*y*y
    return V,W,A,J,K


def homogeneous_constraints(par:Parameters,q:PhasePoint):
    """Reduced mini constraints BEFORE BD secondary, dust phases still canonical."""
    V,W,*_=beta_functions(par,q)
    k=par.m2*par.Mg2
    a,b=q.a,q.b
    return (-q.pa*q.pa/(12*par.Mg2*a)+k*a**3*V+q.pg,
            -q.pb*q.pb/(12*par.Mf2*b)+k*a**3*W+q.pf)


def primary_poisson_analytic(par:Parameters,q:PhasePoint):
    """Canonical {Hg,Hf} factorization, exact for homogeneous dust clocks."""
    *_,J,_=beta_functions(par,q)
    return .5*par.m2*par.Mg2*q.a*q.a*J*secondary_chi(par,q)


def secondary_chi(par:Parameters,q:PhasePoint):
    par.validate();q.validate()
    return q.pa/(par.Mg2*q.a)-q.pb/(par.Mf2*q.b)


def secondary_preservation_brackets(par:Parameters,q:PhasePoint):
    """Exact ({chi,Hg},{chi,Hf}), including all kinetic and HR derivatives.

    The secondary chi=0 is implied by {Hg,Hf}=0 only if m²*J !=0.
    Its preservation Ng*{chi,Hg}+Nf*{chi,Hf}=0 fixes the lapse ratio
    on regular dynamical backgrounds, not an extra propagating mode.
    """
    _,_,A,J,K=beta_functions(par,q)
    a,b=q.a,q.b
    M,F,k=par.Mg2,par.Mf2,par.m2*par.Mg2
    bg=(q.pa*q.pa/(12*M*M*a**3)-3*k*a*A/M+3*k*a*a*J/(F*b))
    bf=(-q.pb*q.pb/(12*F*F*b**3)-3*k*a*J/M+3*k*a*a*K/(F*b))
    return bg,bf


def preservation_lapse_ratio(par:Parameters,q:PhasePoint,*,min_denom=1e-12,on_shell_tol=1e-8):
    if not math.isfinite(min_denom) or min_denom<=0:raise ValueError('positive regularity threshold')
    if not math.isfinite(on_shell_tol) or on_shell_tol<=0:raise ValueError('positive on-shell tolerance')
    hg,hf=homogeneous_constraints(par,q)
    if max(abs(hg),abs(hf),abs(secondary_chi(par,q)))>on_shell_tol:
        raise ValueError('cannot infer physical lapse ratio off the primary+secondary constraint surface')
    _,_,_,J,_=beta_functions(par,q)
    if abs(par.m2*J)<=min_denom:
        raise ValueError('algebraic/degenerate J=0 branch: chi not implied by primary bracket')
    bg,bf=secondary_preservation_brackets(par,q)
    if abs(bf)<=min_denom:
        raise ValueError('secondary lapse-fixing bracket degenerate')
    return -bg/bf


def canonical_bracket_fd(func,other,par:Parameters,q:PhasePoint,*,step=2e-6):
    """Independent centered finite-difference Poisson oracle, FOUR canonical pairs."""
    if not math.isfinite(step) or step<=0:raise ValueError('positive finite difference step')
    y=q.canonical_vector()
    grads=[]
    for fn in (func,other):
        g=np.zeros(8)
        for i in range(8):
            h=step*max(1.,abs(y[i]))
            plus=y.copy();minus=y.copy();plus[i]+=h;minus[i]-=h
            g[i]=(fn(par,from_vector(plus))-fn(par,from_vector(minus)))/(2*h)
        grads.append(g)
    f,g=grads
    return float(np.dot(f[:4],g[4:])-np.dot(f[4:],g[:4]))


def mini_hg(par,q):return homogeneous_constraints(par,q)[0]
def mini_hf(par,q):return homogeneous_constraints(par,q)[1]
def mini_chi(par,q):return secondary_chi(par,q)


def flat_spherical_embedding(par:Parameters,q:PhasePoint,*,radius=.2):
    """Independent check: true spherical Step33a primary divided by r² = mini Hg/Hf.

    The homogeneous spherical canonical densities are pL=(pa/3)r²,
    pS=(2pa/3)r, and pL'=(2pa/3)r, equally in each sector. These
    relations are obtained by matching the radial symplectic one-form.
    All clocks are comoving and each dust momentum density is pi*r².
    """
    par.validate();q.validate()
    if not math.isfinite(radius) or radius<=0:raise ValueError('positive radius')
    r=radius
    gg=Geometry(L=q.a,S=q.a*r,Sr=q.a,planck2=par.Mg2)
    ff=Geometry(L=q.b,S=q.b*r,Sr=q.b,planck2=par.Mf2)
    c=coupled_primary(gg,ff,pLg=q.pa*r*r/3,pSg=2*q.pa*r/3,
              pLrg=2*q.pa*r/3,pLf=q.pb*r*r/3,pSf=2*q.pb*r/3,
              pLrf=2*q.pb*r/3,pg=q.pg*r*r,thrg=0.,pf=q.pf*r*r,
              thrf=0.,z=0.,betas=par.betas,m2=par.m2)
    return c.Hg/(r*r),c.Hf/(r*r),c.Ddiag/(r*r)


CANDIDATE_BETAS=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
CANDIDATE_M2=23.3348939346
CANDIDATE_MF2=.10879548725**2
CANDIDATE_Y0=.5568825591873054


def candidate_dust_point(a):
    """Independent quartic continuation of dust-only Candidate-C (NO radiation).

    Recomputes both fixed dust charges, the quartic root and Bianchi
    Nf=y+dy/d ln a, without importing the older mini Routhian.
    """
    if not math.isfinite(a) or not .025<=a<=1.:
        raise ValueError('candidate dust-only sampling range [.025,1]')
    m2=CANDIDATE_M2;F=CANDIDATE_MF2
    b0,b1,b2,b3,b4=CANDIDATE_BETAS
    Cg=.9;Cf=3*.23958426762*CANDIDATE_Y0**3
    par=Parameters(CANDIDATE_BETAS,m2,1.,F)
    yprev=CANDIDATE_Y0
    for A in np.geomspace(1.,a,max(2,int(140*abs(math.log(a)))+2)):
        poly=np.array([F*m2*b3/3,F*m2*b2-m2*b4/3,
              F*m2*b1-m2*b3,F*Cg/(3*A**3)-m2*b2,
              -Cf/(3*A**3)-m2*b1/3])
        roots=np.roots(poly)
        pos=[v.real for v in roots if abs(v.imag)<1e-8 and v.real>0]
        if not pos:raise RuntimeError('no candidate positive quartic root')
        yprev=float(min(pos,key=lambda v:abs(math.log(v/yprev))))
    y=yprev; b=a*y
    poly=np.array([F*m2*b3/3,F*m2*b2-m2*b4/3,
              F*m2*b1-m2*b3,F*Cg/(3*a**3)-m2*b2,
              -Cf/(3*a**3)-m2*b1/3])
    py=np.polyval(np.polyder(poly),y)
    pn=(-F*Cg*y+Cf)/a**3
    if abs(py)<1e-10:raise RuntimeError('singular polynomial derivative')
    yn=-pn/py; nf=y+yn
    V=beta_functions(par,PhasePoint(a,b,0,0,0,0,Cg,Cf))[0]
    H2=Cg/(3*a**3)+m2*V/3
    if nf<=0 or H2<=0:raise ValueError('nonregular candidate dust background')
    adot=a*math.sqrt(H2)
    pa=-6*par.Mg2*a*adot
    pb=-6*par.Mf2*b*adot
    return par,PhasePoint(a,b,pa,pb,0.,0.,Cg,Cf),nf
