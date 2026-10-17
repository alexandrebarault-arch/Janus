"""Project a regular spherical scalar profile into the native HR local jets.

Kinematic control only, NOT the full physical oscillation action.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

@dataclass(frozen=True)
class ProfileProjectedHRJet:
    gradient: np.ndarray
    hessian: np.ndarray
    jacobian: np.ndarray
    radial_profile: float
    radial_profile_derivative: float

def spherical_bessel_j0_with_radial_derivative(k, r):
    k=float(k);r=float(r)
    if k<0 or r<0 or not math.isfinite(k) or not math.isfinite(r):
        raise ValueError("k and r must be nonnegative finite values")
    z=k*r
    if abs(z)<1e-3:
        v=1-z*z/6+z**4/120-z**6/5040+z**8/362880
        return v,k*(-z/3+z**3/30-z**5/840+z**7/45360)
    return math.sin(z)/z,k*(z*math.cos(z)-math.sin(z))/(z*z)

def regular_profile_to_native_jet(*,r,profile,profile_r):
    r=float(r);f=float(profile);df=float(profile_r)
    if r<0 or not all(math.isfinite(q) for q in (r,f,df)):
        raise ValueError("invalid regular spherical profile")
    P=np.zeros((14,12),dtype=float)
    P[:8,:8]=np.eye(8)
    P[8,8]=f
    P[9,10]=f
    P[10,8]=df
    P[11,11]=r*f
    P[12,9]=f+r*df
    P[13,9]=f
    return P

def project_hr_native_profile(jet,*,r,k):
    if jet.hessian.shape!=(14,14) or jet.gradient.shape!=(14,):
        raise ValueError("expected 14-dimensional HR jet")
    f,df=spherical_bessel_j0_with_radial_derivative(k,r)
    P=regular_profile_to_native_jet(r=r,profile=f,profile_r=df)
    H=P.T@jet.hessian@P
    return ProfileProjectedHRJet(
        gradient=P.T@jet.gradient,
        hessian=.5*(H+H.T),jacobian=P,
        radial_profile=f,radial_profile_derivative=df,
    )
