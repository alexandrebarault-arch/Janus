"""Quadratic sampling correction for f-native *perturbation fields*.

The existing 14-coordinate native HR jet samples background n(T),alpha(T)
at displaced T but treats the independent f-native metric perturbations as
point values frozen at the chart background position (T0,R0).

For the four independent f-native fields q=(Phi_f,B_f,psi_f,E_f), with
q and its native field gradients counted as first-order perturbations:

 q(T0+deltaT,R0+deltaR) = q(T0,R0) + q_T deltaT + q_R deltaR + O(3).

The previous 14-vector already contains deltaT and deltaR/r, so
 deltaR = r * (deltaR_over_r).
The ONLY new quadratic contribution to the interaction density is
 sum_{f fields i} (dL/dq_i)*(q_Ti deltaT+r q_Ri deltaR_over_r).

The q_T and q_R entries are *not* independent propagating degrees of
freedom: their coherent profile/rate relations must be imposed in the
full pre-metric action. In particular, q_R means the derivative in the
f-native radial coordinate R, not the common-chart derivative in r.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_native_stueckelberg_jet import (
    NativeHRStueckelbergJet, native_hr_stueckelberg_jet, JET_ORDER,
)

SAMPLED_ORDER = JET_ORDER + (
    'Phi_f_T','B_f_T','psi_f_T','E_f_T',
    'Phi_f_R','B_f_R','psi_f_R','E_f_R',
)

@dataclass(frozen=True)
class SampledNativeHRJet:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    variable_order: tuple[str,...] = SAMPLED_ORDER


def add_native_field_sampling(local:NativeHRStueckelbergJet, *,r:float)->SampledNativeHRJet:
    """Append 8 field-derivative coordinates with exact O(perturbation^2) terms."""
    r=float(r)
    if not math.isfinite(r) or r<0:
        raise ValueError('r must be nonnegative and finite')
    if local.hessian.shape!=(14,14) or local.gradient.shape!=(14,):
        raise ValueError('expected the original 14x14 native HR Hessian')
    H=np.zeros((22,22),dtype=float)
    H[:14,:14]=local.hessian
    g=np.zeros(22,dtype=float)
    g[:14]=local.gradient
    for j in range(4):
        coeff=local.gradient[4+j]
        H[8,14+j]=H[14+j,8]=coeff
        H[13,18+j]=H[18+j,13]=r*coeff
    return SampledNativeHRJet(
        value=local.value,gradient=g,hessian=.5*(H+H.T),
    )


def sampled_native_hr_stueckelberg_jet(*,r:float=0.,**kwargs)->SampledNativeHRJet:
    return add_native_field_sampling(native_hr_stueckelberg_jet(r=r,**kwargs),r=r)
