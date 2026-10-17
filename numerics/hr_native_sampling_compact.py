"""Coherent compact radial pullback of f-native perturbation-field sampling.

The common-coordinate amplitudes q_f(t,r) = A_i(t) P_i(r) have
native derivatives q_T and q_R related by the *background* Jacobian:

 [q_t, q_r]^T = [[T_t, R_t],[T_r, R_r]] [q_T,q_R]^T.

The new f-native derivative slots are hence not new physical modes. This
interaction-only gate includes all 22 native-jet dimensions but does not
include EH/dust dynamics, the physical eigenprofile, or fold propagation.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_compact_radial_interaction import (AMPLITUDES, compact_native_profile_map, compact_scalar_profile)
from numerics.hr_native_stueckelberg_jet import native_hr_stueckelberg_jet
from numerics.hr_native_field_sampling import add_native_field_sampling

SAMPLED_COMPACT_ORDER = AMPLITUDES + ('Phi_f_dot','B_f_dot','psi_f_dot','E_f_dot')

@dataclass(frozen=True)
class CompactSampledHRInteraction:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    radius: float
    quadrature_order: int
    amplitude_order: tuple[str,...] = SAMPLED_COMPACT_ORDER


def compact_metric_radial_profiles(*, r:float,R:float,k:float):
    """Return the native metric radial profile and common-r derivative.

    The radial B component is odd, while the spherical scalar shear
    component is even and vanishes quadratically at the origin.
    """
    k=float(k)
    if not math.isfinite(k) or k<=0:
        raise ValueError('require finite positive k')
    F,Fr,Frr,tf=compact_scalar_profile(r,R)
    if r>=R:
        tf_r=0.
    else:
        q=1.-(r/R)**2
        tf_r=96.*r/R**4*q*q-192.*r**3/R**6*q
    profiles=np.array([F,Fr/k,F,-2.*tf/(k*k)])
    derivatives=np.array([Fr,Frr/k,Fr,-2.*tf_r/(k*k)])
    return profiles,derivatives


def sampled_compact_native_map(*, r:float,R:float,k:float,mu:float,
                               mu_dot:float,sigma_r:float,sigma_dot:float):
    """Return 22x16 profile map including full inverse-chart chain rule.

    Native f derivative input order is (Phi_f_T,...,E_f_T,Phi_f_R,...,E_f_R).
    Profile radius R and wavenumber k are fixed in common coordinates
    at this frozen background instant. Each native f field q_f's common
    derivative is q_t=A_dot*P, q_r=A*P_r.
    """
    scalars=(r,R,k,mu,mu_dot,sigma_r,sigma_dot)
    if not all(math.isfinite(float(v)) for v in scalars) or r<0 or R<=0 or k<=0 or mu<=-1:
        raise ValueError('invalid background, radius or wave number')
    t_t=1.+.5*sigma_dot*r*r
    t_r=sigma_r*r
    r_t=mu_dot*r
    r_r=1.+mu
    D=t_t*r_r-t_r*r_t
    if D<=0:raise ValueError('nonpositive native chart Jacobian')
    Q=np.zeros((22,16),dtype=float)
    Q[:14,:12]=compact_native_profile_map(r=r,R=R,k=k)
    p,dp=compact_metric_radial_profiles(r=r,R=R,k=k)
    for j in range(4):
        # q_T = (R_r q_t - R_t q_r)/det(J)
        Q[14+j,12+j]=r_r*p[j]/D
        Q[14+j,4+j]=-r_t*dp[j]/D
        # q_R = (-T_r q_t + T_t q_r)/det(J)
        Q[18+j,12+j]=-t_r*p[j]/D
        Q[18+j,4+j]=t_t*dp[j]/D
    return Q


def integrate_sampled_compact_hr_interaction(*,radius:float,quadrature_order:int=24,
                                               **hr_parameters)->CompactSampledHRInteraction:
    """Spatial 4*pi*r^2 interaction Hessian, with no EH/dust sector."""
    radius=float(radius)
    if not math.isfinite(radius) or radius<=0:raise ValueError('invalid compact radius')
    if type(quadrature_order) is not int or quadrature_order<8:
        raise ValueError('quadrature_order must be integer >= 8')
    if 'r' in hr_parameters:raise ValueError('the integration controls r')
    required=('k','mu','mu_dot','sigma_r','sigma_dot')
    if not all(x in hr_parameters for x in required):
        raise ValueError('missing native background Jacobian inputs')
    k,mu,mu_dot,sigma_r,sigma_dot=(hr_parameters[x] for x in required)
    nodes,weights=np.polynomial.legendre.leggauss(quadrature_order)
    H=np.zeros((16,16));g=np.zeros(16);value=0.
    for z,w in zip(nodes,weights):
        r=.5*radius*(z+1.)
        native=native_hr_stueckelberg_jet(r=r,**hr_parameters)
        sampled=add_native_field_sampling(native,r=r)
        Q=sampled_compact_native_map(r=r,R=radius,k=k,mu=mu,
                                     mu_dot=mu_dot,sigma_r=sigma_r,sigma_dot=sigma_dot)
        wt=2.*math.pi*radius*w*r*r
        H+=wt*(Q.T@sampled.hessian@Q)
        g+=wt*(Q.T@sampled.gradient)
        value+=wt*sampled.value
    return CompactSampledHRInteraction(
        value=float(value),gradient=g,hessian=.5*(H+H.T),
        radius=radius,quadrature_order=quadrature_order)
