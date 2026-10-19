"""Exact spherical ADM Hamiltonian and Hassan–Rosen lapse-linear relative shift.

ANALYTIC structural primary-constraint interface for positive Einstein--Hilbert
sectors with two independent irrotational canonical dust pairs.  Spherical
unit-solid-angle densities; omit total radial derivatives, assume compact
boundary variations.  No full BD *secondary*, gauge fixing, constrained
scalar speed, or genuinely nonhomothetic on-shell branch is derived here.

Metric: ds²=-N²dt² + L²(dr+V dt)² + S²dOmega².
The g/f shift difference is parametrized as
    V_g-V_f=(N_g/L_g+N_f/L_f) z,  |z|<1.
At *fixed* z and common V_f, the exact HR principal-root interaction
Hamiltonian is linear in BOTH ADM lapses. Variation w.r.t. z has a factor
(N_g/L_g+N_f/L_f) times a lapse-INDEPENDENT equation. This is a
necessary bimetric primary-constraint structural identity, not a proof
that the nonlinear BD secondary removes the ghost in a perturbed theory.
"""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Geometry:
    L: float
    S: float
    Lr: float = 0.
    Sr: float = 1.
    Srr: float = 0.
    planck2: float = 1.

    def check(self):
        if not all(math.isfinite(x) for x in (self.L,self.S,self.Lr,self.Sr,self.Srr,self.planck2)):
            raise ValueError('nonfinite ADM geometry')
        if min(self.L,self.S,self.planck2)<=0:
            raise ValueError('positive radial geometry and EH Planck coefficient required')


def spatial_curvature(g: Geometry):
    """Exact 3-scalar curvature of L²dr²+S²dOmega²."""
    g.check()
    W=g.Sr/g.L
    Wr=g.Srr/g.L-g.Sr*g.Lr/g.L**2
    return 2/g.S**2*(1-W*W-2*g.S/g.L*Wr)


def eh_adm_density(g: Geometry, *,N,V,Vr,Ldot,Sdot):
    """Original nonlinear positive-sign EH+GHY ADM Lagrangian density."""
    g.check()
    if not all(math.isfinite(x) for x in (N,V,Vr,Ldot,Sdot)) or N<=0:
        raise ValueError('positive lapse and finite ADM data required')
    Kr=(Ldot-V*g.Lr-g.L*Vr)/(N*g.L)
    Kt=(Sdot-V*g.Sr)/(N*g.S)
    return .5*g.planck2*N*g.L*g.S*g.S*(spatial_curvature(g)-4*Kr*Kt-2*Kt*Kt)


def eh_canonical_momenta(g:Geometry,*,N,V,Vr,Ldot,Sdot):
    """Exact Legendre map (p_L,p_S), with first radial derivatives."""
    g.check()
    if N<=0:raise ValueError('positive lapse required')
    Kr=(Ldot-V*g.Lr-g.L*Vr)/(N*g.L)
    Kt=(Sdot-V*g.Sr)/(N*g.S)
    return -2*g.planck2*g.S*g.S*Kt, -2*g.planck2*g.L*g.S*(Kr+Kt)


def eh_hamiltonian_constraints(g:Geometry,*,pL,pS,pLr):
    """H_EH=N C+V D modulo boundary, true ADM canonical variables.

    pLr is the exact spatial derivative of pL, NOT a free physical mode.
    """
    g.check()
    if not all(math.isfinite(x) for x in (pL,pS,pLr)):
        raise ValueError('finite canonical momentum data required')
    C=(g.L*pL*pL/(4*g.planck2*g.S*g.S)
       -pL*pS/(2*g.planck2*g.S)
       -.5*g.planck2*g.L*g.S*g.S*spatial_curvature(g))
    D=pS*g.Sr-g.L*pLr
    return C,D


def dust_hamiltonian_constraints(g:Geometry,*,p,theta_r):
    """Stationary-rho reduced dust, keeping positive momentum p and theta."""
    g.check()
    if not all(math.isfinite(x) for x in (p,theta_r)) or p<=0:
        raise ValueError('positive independent dust momentum required')
    return p*math.sqrt(1+theta_r*theta_r/(g.L*g.L)),p*theta_r


def hr_beta_combinations(ell,betas):
    if not all(math.isfinite(float(v)) for v in betas) or len(betas)!=5:
        raise ValueError('five finite HR betas required')
    b0,b1,b2,b3,b4=betas
    return (b0+2*b1*ell+b2*ell*ell,
            b2+2*b3*ell+b4*ell*ell,
            b1+2*b2*ell+b3*ell*ell)


def hr_lagrangian(g:Geometry,f:Geometry,*,Ng,Nf,Vg,Vf,betas,m2):
    """Exact spherical HR interaction Lagrangian from 2x2 principal root."""
    g.check();f.check()
    if min(Ng,Nf)<=0 or not math.isfinite(m2) or m2<0:
        raise ValueError('positive ADM lapses and nonnegative HR mass² required')
    A0,As,At=hr_beta_combinations(f.S/g.S,betas)
    P=Ng*f.L+Nf*g.L
    Z=g.L*f.L*(Vg-Vf)
    rad=P*P-Z*Z
    if rad<=0: raise ValueError('lost real HR principal-root branch')
    return -m2*g.planck2*g.S*g.S*(Ng*g.L*A0+Nf*f.L*As+At*math.sqrt(rad))


def relative_shift(g:Geometry,f:Geometry,*,Ng,Nf,V,z):
    """Return (Vg,Vf) with a lapse-dependent HR shift redefinition."""
    g.check();f.check()
    if Ng<=0 or Nf<=0 or not math.isfinite(z) or abs(z)>=1:
        raise ValueError('positive lapses and |relative z|<1 required')
    return V+(Ng/g.L+Nf/f.L)*z,V


def hr_linear_lapse_coefficients(g:Geometry,f:Geometry,*,z,betas,m2):
    """W_g,W_f such that HR Hamiltonian=N_g W_g+N_f W_f.

    The common radial shift does not enter the HR potential. At fixed z
    and geometries, W's are independent of both ADM lapses.
    """
    g.check();f.check()
    if not math.isfinite(z) or abs(z)>=1 or not math.isfinite(m2) or m2<0:
        raise ValueError('real principal square-root and positive mass²')
    A0,As,At=hr_beta_combinations(f.S/g.S,betas)
    root=math.sqrt(1-z*z)
    factor=m2*g.planck2*g.S*g.S
    return factor*(g.L*A0+f.L*At*root),factor*(f.L*As+g.L*At*root)


def relative_shift_constraint(g:Geometry,f:Geometry,*,Dg,z,betas,m2):
    """Lapse-independent z equation F=Dg-K*z/sqrt(1-z²)=0.

    The complete dH/dz equals (Ng/Lg+Nf/Lf) * F on fixed ADM data.
    """
    g.check();f.check()
    if not math.isfinite(Dg) or abs(z)>=1:
        raise ValueError('valid radial momentum density and |z|<1 required')
    _,_,At=hr_beta_combinations(f.S/g.S,betas)
    K=m2*g.planck2*g.S*g.S*g.L*f.L*At
    return Dg-K*z/math.sqrt(1-z*z)


def solve_relative_shift(g:Geometry,f:Geometry,*,Dg,betas,m2):
    """Algebraic z solution when the HR relative-shift coefficient !=0."""
    _,_,At=hr_beta_combinations(f.S/g.S,betas)
    K=m2*g.planck2*g.S*g.S*g.L*f.L*At
    if not math.isfinite(Dg) or not math.isfinite(K) or K==0:
        raise ValueError('degenerate HR relative-shift sector requires separate constraints')
    return math.copysign(1.,K)*Dg/math.hypot(Dg,K)


@dataclass(frozen=True)
class ADMConstraints:
    Cg:float
    Cf:float
    Ddiag:float
    Dg:float
    Df:float
    Hg:float
    Hf:float


def coupled_primary(g:Geometry,f:Geometry,*,pLg,pSg,pLrg,pLf,pSf,pLrf,
                    pg,thrg,pf,thrf,z,betas,m2):
    """True spherical canonical density H=Ng Hg+Nf Hf+V Ddiag.

    After HR relative-shift redefinition, BEFORE z elimination. Includes
    independently canonical dust momenta p_g,p_f and clock gradients.
    Does NOT impose secondary BD constraint or dynamical time evolution.
    """
    cg,dg=eh_hamiltonian_constraints(g,pL=pLg,pS=pSg,pLr=pLrg)
    cf,df=eh_hamiltonian_constraints(f,pL=pLf,pS=pSf,pLr=pLrf)
    mg,rg=dust_hamiltonian_constraints(g,p=pg,theta_r=thrg)
    mf,rf=dust_hamiltonian_constraints(f,p=pf,theta_r=thrf)
    cg+=mg;cf+=mf;dg+=rg;df+=rf
    wg,wf=hr_linear_lapse_coefficients(g,f,z=z,betas=betas,m2=m2)
    return ADMConstraints(cg,cf,dg+df,dg,df,cg+z*dg/g.L+wg,cf+z*dg/f.L+wf)


def coupled_hamiltonian(constraints:ADMConstraints,*,Ng,Nf,V):
    if min(Ng,Nf)<=0 or not all(math.isfinite(v) for v in (Ng,Nf,V)):
        raise ValueError('positive lapse and finite common shift required')
    return Ng*constraints.Hg+Nf*constraints.Hf+V*constraints.Ddiag
