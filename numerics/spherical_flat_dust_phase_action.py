"""Pressureless phase action in a native spatially-flat spherical chart."""
from __future__ import annotations
import math
import numpy as np


def _finite(*values):
    if not all(math.isfinite(float(v)) for v in values):
        raise ValueError("all dust-phase inputs must be finite")


def flat_spherical_dust_phase_density(*, scale_factor: float, lapse: float,
                                      r: float, rho: float, Phi: float,
                                      shift: float, q: float, q_t: float,
                                      q_r: float, momentum: float,
                                      log_phidot_rate: float = 0.0) -> float:
    """Return the native dust phase density per ``sin(theta)``.

    The metric convention is ``g_tr=n a U`` with ``shift=U``. The local
    phase bracket is the real-space counterpart of the validated De Felice
    dust action,

    ``p(q_t+r_phi q-Phi) + rho Phi^2/2
       - n^2 rho (q_r+a U/n)^2/(2 a^2)``.

    The background spherical measure ``n a^3 r^2`` is included.
    """
    _finite(scale_factor,lapse,r,rho,Phi,shift,q,q_t,q_r,momentum,log_phidot_rate)
    a=float(scale_factor); n=float(lapse); rr=float(r); dens=float(rho)
    if a<=0.0 or n<=0.0 or rr<0.0 or dens<=0.0:
        raise ValueError("require positive scale factor, lapse, density and r>=0")
    p=float(momentum)
    spatial=float(q_r)+a*float(shift)/n
    local=(
        p*(float(q_t)+float(log_phidot_rate)*float(q)-float(Phi))
        +0.5*dens*float(Phi)**2
        -0.5*n*n*dens/(a*a)*spatial*spatial
    )
    return float(n*a**3*rr**2*local)


def pulled_back_flat_spherical_dust_phase_density(*, scale_factor: float,
        lapse: float, native_r: float, rho: float, Phi: float, shift: float,
        q: float, q_t_common: float, q_r_common: float, momentum: float,
        jacobian, log_phidot_rate: float = 0.0) -> float:
    """Pull a native dust sector to a common radial chart.

    ``jacobian = d(t_native,r_native)/d(t_common,r_common)``. Derivatives of
    the scalar phase coordinate transform as a covector and the radial-time
    measure contributes ``abs(det(jacobian))``.
    """
    J=np.asarray(jacobian,dtype=float)
    if J.shape!=(2,2) or not np.all(np.isfinite(J)):
        raise ValueError("jacobian must be a finite 2x2 matrix")
    det=float(np.linalg.det(J))
    if abs(det)<=1e-14:
        raise np.linalg.LinAlgError("dust pullback jacobian is singular")
    grad_native=np.linalg.solve(J.T,np.array([q_t_common,q_r_common],dtype=float))
    native=flat_spherical_dust_phase_density(
        scale_factor=scale_factor,lapse=lapse,r=native_r,rho=rho,
        Phi=Phi,shift=shift,q=q,q_t=float(grad_native[0]),
        q_r=float(grad_native[1]),momentum=momentum,
        log_phidot_rate=log_phidot_rate,
    )
    return float(abs(det)*native)
