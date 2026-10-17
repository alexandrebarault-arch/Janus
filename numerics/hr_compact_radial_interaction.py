"""Compact, *interaction-only* spherical projection of the finite-mu HR jet.

This is a spatial action/control, NOT the dynamical finite-mu scalar action.
The radial scalar metric perturbations are reconstructed from a C^3 compact
scalar potential F(r) using their Fourier normalization in the native jet:

  metric lapses/traces: F;
  radial scalar shifts (B): F'/k;
  radial/angular traceless scalar shears (E): -2(F''-F'/r)/k^2.

This imposes correct center regularity and radial parity. All four native
metric components of each sector and chart displacements T,L are amplitudes;
the two chart *rates* Tdot,Ldot are kept explicitly as independent action
arguments. The native HR oracle supplies the complete exact *local* 14x14
second variation. The 4*pi*r^2 integration is done before any Schur reduction.

Important limitations: (1) no Einstein-Hilbert/dust terms, (2) no native
f-perturbation sampling derivatives induced by deltaT, (3) fixed background
time, (4) the compact bump is a control trial function, not an eigenmode.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_native_stueckelberg_jet import native_hr_stueckelberg_jet

AMPLITUDES = (
    'Phi_g','B_g','psi_g','E_g','Phi_f','B_f','psi_f','E_f',
    'T','L','Tdot','Ldot',
)

@dataclass(frozen=True)
class CompactRadialInteraction:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    integration_volume: float
    radius: float
    quadrature_order: int
    amplitude_order: tuple[str,...] = AMPLITUDES


def compact_scalar_profile(r: float, R: float) -> tuple[float,float,float,float]:
    """Return F,F',F'',F''-F'/r; fourth-power compact bump.

    F = (1-r^2/R^2)^4 for r<R, else zero. The final value has
    well-defined regular limit zero at r=0 (no 0/0 division).
    """
    r=float(r); R=float(R)
    if not all(math.isfinite(x) for x in (r,R)) or r<0 or R<=0:
        raise ValueError('require finite R>0 and 0<=r')
    if r>=R:
        return (0.,0.,0.,0.)
    u=(r/R)**2
    q=1.-u
    F=q**4
    Fr=-8.*r/R**2*q**3
    Frr=-8./R**2*q**3+48.*r*r/R**4*q*q
    tracefree=48.*r*r/R**4*q*q
    return F,Fr,Frr,tracefree


def compact_native_profile_map(*,r:float,R:float,k:float) -> np.ndarray:
    """Map 12 smooth scalar amplitudes to 14 local HR jet coordinates.

    Metric shift profiles are radially odd. Traceless spherical shear
    vanishes at r=0, unlike a single aligned Cartesian plane wave.
    The map does not assert a physical gauge or an on-shell eigenprofile.
    """
    k=float(k)
    if not math.isfinite(k) or k<=0.:
        raise ValueError('require finite k>0 for Fourier-normalized B,E')
    F,Fr,_,tf=compact_scalar_profile(r,R)
    P=np.zeros((14,12),dtype=float)
    for i in (0,2,4,6):
        P[i,i]=F
    for i in (1,5):
        P[i,i]=Fr/k
    for i in (3,7):
        P[i,i]=-2.*tf/(k*k)
    # Native chart jets (dT,dT_t,dT_r,dR_t,dR_r,dR/r).
    P[8,8]=F
    P[9,10]=F
    P[10,8]=Fr
    P[11,11]=r*F
    P[12,9]=F+r*Fr
    P[13,9]=F
    return P


def integrate_compact_hr_interaction(*,radius:float,quadrature_order:int=24,**hr_parameters)->CompactRadialInteraction:
    """Integrate the quadratic native interaction over a compact sphere.

    hr_parameters are exactly the native_hr_stueckelberg_jet arguments
    other than r. Local radial measure is 4*pi*r^2 dr; no extra a^3/N
    factor is inserted because sqrt(-g) is already in the local potential.
    """
    radius=float(radius)
    if not math.isfinite(radius) or radius<=0:
        raise ValueError('require finite positive radius')
    if isinstance(quadrature_order,bool) or not isinstance(quadrature_order,int) or quadrature_order<8:
        raise ValueError('quadrature_order must be an integer >= 8')
    if 'r' in hr_parameters:
        raise ValueError('radius is controlled by the integral; do not pass r')
    if 'k' not in hr_parameters:
        raise ValueError('k is required')
    k=float(hr_parameters['k'])
    if k<=0. or not math.isfinite(k):
        raise ValueError('require finite k>0')
    xs,ws=np.polynomial.legendre.leggauss(quadrature_order)
    rr=.5*radius*(xs+1.)
    weights=2.*math.pi*radius*ws*rr*rr
    H=np.zeros((12,12));g=np.zeros(12);value=0.
    for r,w in zip(rr,weights):
        local=native_hr_stueckelberg_jet(r=float(r),**hr_parameters)
        P=compact_native_profile_map(r=float(r),R=radius,k=k)
        H+=w*(P.T@local.hessian@P)
        g+=w*(P.T@local.gradient)
        value+=w*local.value
    return CompactRadialInteraction(
        value=float(value),gradient=g,hessian=.5*(H+H.T),
        integration_volume=4.*math.pi*radius**3/3.,
        radius=radius,quadrature_order=quadrature_order,
    )
