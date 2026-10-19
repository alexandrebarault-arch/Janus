"""Radial spatial-diffeomorphism Ward checks for exact spherical ADM+HR+two dust.

This is an infinitesimal field-density transformation test, NOT functional
Poisson smearing/constraint bracket closure nor the radial BD secondary.
Only compact diagonal spatial diffeomorphisms are considered. Both dust
canonical pairs remain explicit in the spherical constraints.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numpy.polynomial import Polynomial as Poly
from numerics.hr_spherical_adm_primary import (
    Geometry, coupled_primary, spatial_curvature, solve_relative_shift,
    relative_shift_constraint,
)

# Scalars carry weight 0; radial line metric L, pS and matter momentum p
# carry density weight 1. D has weight 2; H_g/H_f each have weight 1.
FIELDS=("Lg","Sg","pLg","pSg","thetag","pg",
        "Lf","Sf","pLf","pSf","thetaf","pf","z")
WEIGHTS=dict(zip(FIELDS,(1,0,0,1,0,1, 1,0,0,1,0,1, 0)))
BETAS=(.2,1.3,-.35,.4,-.17)
M2=.91
MG2=1.7
MF2=.63


@dataclass(frozen=True)
class RadialWard:
    metric_hamiltonian_residual: np.ndarray
    diagonal_momentum_residual: float
    curvature_residual: np.ndarray
    relative_shift_root_residual: float
    relative_shift_equation_residual: float


def default_fields():
    """Radial sample polynomials regular and positive for 0<r<1."""
    return {
        "Lg":Poly([1.12,.13,.04]),"Sg":Poly([0.,.88,.07]),
        "pLg":Poly([0.,0.,-.12,.031]),"pSg":Poly([0.,-.088,.022]),
        "thetag":Poly([.1,.08,-.014]),"pg":Poly([0.,0.,.17,.026]),
        "Lf":Poly([.96,.08,.035]),"Sf":Poly([0.,.73,.06]),
        "pLf":Poly([0.,0.,-.072,.02]),"pSf":Poly([0.,-.062,.012]),
        "thetaf":Poly([-.07,.052,.017]),"pf":Poly([0.,0.,.12,.016]),
        "z":Poly([.08,.035,-.01]),
    }


def spatial_generator():
    # eta=0.17*r*(1-r)^3 vanishes at r=0 and r=1.
    return .17*Poly([0,1])*Poly([1,-1])**3


def transformed(fields,eta,epsilon):
    """Infinitesimal diagonal radial diffeo: δφ=η φ'+w η' φ."""
    if not math.isfinite(epsilon):raise ValueError("finite spatial variation required")
    if set(fields)!=set(FIELDS):raise ValueError("all 13 canonical radial fields required")
    return {key:val+epsilon*(eta*val.deriv()+WEIGHTS[key]*eta.deriv()*val)
            for key,val in fields.items()}


def densities(fields,r):
    if not 0<r<1:raise ValueError("r must be interior to compact support")
    if set(fields)!=set(FIELDS):raise ValueError("incomplete canonical field map")
    g=Geometry(L=float(fields['Lg'](r)),S=float(fields['Sg'](r)),
        Lr=float(fields['Lg'].deriv()(r)),Sr=float(fields['Sg'].deriv()(r)),
        Srr=float(fields['Sg'].deriv(2)(r)),planck2=MG2)
    f=Geometry(L=float(fields['Lf'](r)),S=float(fields['Sf'](r)),
        Lr=float(fields['Lf'].deriv()(r)),Sr=float(fields['Sf'].deriv()(r)),
        Srr=float(fields['Sf'].deriv(2)(r)),planck2=MF2)
    vals=coupled_primary(g,f,
        pLg=float(fields['pLg'](r)),pSg=float(fields['pSg'](r)),
        pLrg=float(fields['pLg'].deriv()(r)),
        pLf=float(fields['pLf'](r)),pSf=float(fields['pSf'](r)),
        pLrf=float(fields['pLf'].deriv()(r)),
        pg=float(fields['pg'](r)),pf=float(fields['pf'](r)),
        thrg=float(fields['thetag'].deriv()(r)),
        thrf=float(fields['thetaf'].deriv()(r)),
        z=float(fields['z'](r)),betas=BETAS,m2=M2)
    root=solve_relative_shift(g,f,Dg=vals.Dg,betas=BETAS,m2=M2)
    return np.array([vals.Hg,vals.Hf,vals.Ddiag],float), \
            np.array([spatial_curvature(g),spatial_curvature(f)]),root, (g,f,vals)


def _derivative_density(fields,r,dr):
    a=densities(fields,r+dr);b=densities(fields,r-dr)
    return (a[0]-b[0])/(2*dr),(a[1]-b[1])/(2*dr),(a[2]-b[2])/(2*dr)


def radial_ward(*,r=.31,epsilon=1.e-5,dr=1.e-5,fields=None):
    """Finite directional derivative vs Lie transformation of densities.

    Local H_g/H_f are weight-one, D_diag is weight-two; R3 scalars.
    The lapse-independent z equation has weight two, its root weight zero.
    """
    if not (0<r-dr<r+dr<1):raise ValueError("interior radial stencil required")
    if not (math.isfinite(epsilon) and epsilon>0 and math.isfinite(dr) and dr>0):
        raise ValueError("positive finite steps required")
    base=default_fields() if fields is None else fields
    eta=spatial_generator();eta0=float(eta(r));etap=float(eta.deriv()(r))
    plus=densities(transformed(base,eta,+epsilon),r)
    minus=densities(transformed(base,eta,-epsilon),r)
    before=densities(base,r)
    dotH=(plus[0]-minus[0])/(2*epsilon)
    dotR3=(plus[1]-minus[1])/(2*epsilon)
    dotZ=(plus[2]-minus[2])/(2*epsilon)
    drH,drR3,drZ=_derivative_density(base,r,dr)
    expectH=eta0*drH+etap*np.array([before[0][0],before[0][1],2*before[0][2]])
    expectR3=eta0*drR3
    expectZ=eta0*drZ
    # The relative-shift EOM's F=Dg-K z/sqrt(1-z²) has density weight 2.
    # For transformed fields the value of z is also transported.
    def ff(fields):
        vals=densities(fields,r)
        G,Fm,cs=vals[3]
        return relative_shift_constraint(G,Fm,Dg=cs.Dg,z=float(fields['z'](r)),
                     betas=BETAS,m2=M2)
    dF=(ff(transformed(base,eta,epsilon))-ff(transformed(base,eta,-epsilon)))/(2*epsilon)
    # Evaluate its radial derivative using the same complete-field function.
    def f_at(R):
        vals=densities(base,R);G,Fm,cs=vals[3]
        return relative_shift_constraint(G,Fm,Dg=cs.Dg,z=float(base['z'](R)),
                                         betas=BETAS,m2=M2)
    expectF=eta0*(f_at(r+dr)-f_at(r-dr))/(2*dr)+2*etap*f_at(r)
    return RadialWard(dotH[:2]-expectH[:2],float(dotH[2]-expectH[2]),
                      dotR3-expectR3,float(dotZ-expectZ),
                      float(dF-expectF))


CANONICAL_PAIRS=(("Lg","pLg"),("Sg","pSg"),("thetag","pg"),
                 ("Lf","pLf"),("Sf","pSf"),("thetaf","pf"))


def smeared_momentum(fields,eta,order=64):
    """Integrated exact diagonal D[eta] with its radial IBP boundary support."""
    if not isinstance(eta,Poly):raise ValueError("polynomial compact smearing required")
    if type(order) is not int or order<10:raise ValueError("quadrature order >=10")
    nodes,w=np.polynomial.legendre.leggauss(order)
    r=(nodes+1)/2
    d=0*r
    for prefix in ('g','f'):
        d=d + (fields['pS'+prefix](r)*fields['S'+prefix].deriv()(r)
             -fields['L'+prefix](r)*fields['pL'+prefix].deriv()(r)
             +fields['p'+prefix](r)*fields['theta'+prefix].deriv()(r))
    return float(np.dot(w*.5,eta(r)*d))


def momentum_gradient(fields,eta):
    """Exact functional gradients of D[eta], after compact radial IBP.

    Gradients are returned as polynomials with respect to ALL SIX canonical
    pairs (including both independent matter pairs); no physics ansatz is
    eliminated or projected before variation.
    """
    if abs(eta(0))>1e-14 or abs(eta(1))>1e-14:
        raise ValueError("radial smearing must vanish on both boundaries")
    grad={}
    for prefix in ('g','f'):
        L,S,pL,pS,theta,p=('L'+prefix,'S'+prefix,'pL'+prefix,
                            'pS'+prefix,'theta'+prefix,'p'+prefix)
        grad[L]=-eta*fields[pL].deriv()
        grad[pL]=(eta*fields[L]).deriv()
        grad[S]=-(eta*fields[pS]).deriv()
        grad[pS]=eta*fields[S].deriv()
        grad[theta]=-(eta*fields[p]).deriv()
        grad[p]=eta*fields[theta].deriv()
    return grad


def smeared_momentum_poisson(fields,eta,xi,order=64):
    """Independently integrate {D[eta],D[xi]} from 12 functional gradients."""
    gr=momentum_gradient(fields,eta)
    gs=momentum_gradient(fields,xi)
    nodes,w=np.polynomial.legendre.leggauss(order);r=(nodes+1)/2
    bracket=np.zeros_like(r)
    for q,p in CANONICAL_PAIRS:
        bracket+=gr[q](r)*gs[p](r)-gr[p](r)*gs[q](r)
    return float(np.dot(w*.5,bracket))
