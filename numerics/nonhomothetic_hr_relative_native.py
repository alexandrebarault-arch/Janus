"""Exact native-chart HR density for a finite-mu relative spherical pullback.

The common chart is the g-sector cosmic FLRW chart.  The f native coordinates
are pulled back by

    t_f = t + s r^2/2 - T,
    R_f = (1+mu) r - d_r L.

Metric perturbations remain in their native charts.  This is the natural
nonlinear continuation of the pre-BD relative variables used by the linear
Candidate-C bridge.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class RelativeNativeGeometry:
    g_radial_native: np.ndarray
    f_radial_native: np.ndarray
    jacobian_f: np.ndarray
    g_angular_native: float
    f_angular_native: float
    f_time: float
    f_radius: float
    n_f: float
    alpha_f: float


def _native_hr_density(*, geometry: RelativeNativeGeometry, betas, m2: float, Mg2: float) -> float:
    beta = np.asarray(tuple(float(v) for v in betas), dtype=float)
    if beta.shape != (5,):
        raise ValueError("betas must contain five coefficients")
    gn = geometry.g_radial_native
    fn = geometry.f_radial_native
    Jf = geometry.jacobian_f
    gc = gn
    fc = Jf.T @ fn @ Jf
    det_g = float(np.linalg.det(gc))
    if det_g >= 0.0:
        raise ValueError("g radial block must remain Lorentzian")
    A = np.linalg.solve(gc, fc)
    det_A = float(np.linalg.det(A))
    tr_A = float(np.trace(A))
    if det_A <= 0.0:
        raise ValueError("g^-1 f radial determinant must be positive")
    root_det = math.sqrt(det_A)
    den = tr_A + 2.0 * root_det
    if den <= 0.0:
        raise ValueError("principal square root is not real")
    S = (A + root_det * np.eye(2)) / math.sqrt(den)
    trS = float(np.trace(S))
    detS = float(np.linalg.det(S))
    ell = math.sqrt(geometry.f_angular_native / geometry.g_angular_native)
    e = np.array([
        1.0,
        trS + 2.0 * ell,
        detS + 2.0 * ell * trS + ell * ell,
        2.0 * ell * detS + ell * ell * trS,
        ell * ell * detS,
    ])
    return float(
        float(m2) * float(Mg2)
        * math.sqrt(-det_g) * geometry.g_angular_native
        * np.dot(beta, e)
    )


def relative_native_geometry(
    *,
    a: float,
    n: float,
    alpha: float,
    r: float,
    a_dot_over_a: float = 0.0,
    a_ddot_over_a: float = 0.0,
    common_time_offset: float = 0.0,
    n_dot_over_n: float = 0.0,
    n_ddot_over_n: float = 0.0,
    alpha_dot_over_alpha: float = 0.0,
    alpha_ddot_over_alpha: float = 0.0,
    mu: float = 0.0,
    mu_dot: float = 0.0,
    s: float = 0.0,
    s_dot: float = 0.0,
    T: float = 0.0,
    T_dot: float = 0.0,
    T_r: float = 0.0,
    L_r: float = 0.0,
    L_dot_r: float = 0.0,
    L_rr: float = 0.0,
    Phi_g: float = 0.0,
    B_g_r: float = 0.0,
    Phi_f: float = 0.0,
    B_f_r: float = 0.0,
) -> RelativeNativeGeometry:
    vals = (
        a,n,alpha,r,a_dot_over_a,a_ddot_over_a,common_time_offset,
        n_dot_over_n,n_ddot_over_n,alpha_dot_over_alpha,alpha_ddot_over_alpha,
        mu,mu_dot,s,s_dot,T,T_dot,T_r,L_r,L_dot_r,L_rr,
        Phi_g,B_g_r,Phi_f,B_f_r,
    )
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all relative-geometry inputs must be finite")
    if a <= 0.0 or n <= 0.0 or alpha <= 0.0 or r <= 0.0 or mu <= -1.0:
        raise ValueError("require positive a,n,alpha,r and mu>-1")

    t = float(common_time_offset)
    a_common = a * (1.0 + a_dot_over_a*t + 0.5*a_ddot_over_a*t*t)
    mu_common = mu + mu_dot*t
    s_common = s + s_dot*t
    if a_common <= 0.0 or mu_common <= -1.0:
        raise ValueError("local Taylor jet left regular g/relative background")

    # Background jets are anchored at the central common time.  The f native
    # clock therefore samples the total offset t + delta t_f.
    f_time = t + 0.5 * s_common * r * r - T
    n_f = n * (1.0 + n_dot_over_n*f_time + 0.5*n_ddot_over_n*f_time*f_time)
    alpha_f = alpha * (
        1.0 + alpha_dot_over_alpha*f_time
        + 0.5*alpha_ddot_over_alpha*f_time*f_time
    )
    if n_f <= 0.0 or alpha_f <= 0.0:
        raise ValueError("local Taylor jet left positive f background")

    f_radius = (1.0 + mu_common) * r - L_r
    if f_radius <= 0.0:
        raise ValueError("relative radial map left positive branch")

    Jf = np.array([
        [1.0 + 0.5*s_dot*r*r - T_dot, s_common*r - T_r],
        [mu_dot*r - L_dot_r, 1.0 + mu_common - L_rr],
    ], dtype=float)

    gn = np.array([
        [-(1.0 + 2.0*Phi_g), a_common*B_g_r],
        [a_common*B_g_r, a_common*a_common],
    ], dtype=float)
    fn = np.array([
        [-n_f*n_f*(1.0 + 2.0*Phi_f), n_f*alpha_f*B_f_r],
        [n_f*alpha_f*B_f_r, alpha_f*alpha_f],
    ], dtype=float)

    return RelativeNativeGeometry(
        g_radial_native=gn,
        f_radial_native=fn,
        jacobian_f=Jf,
        g_angular_native=a_common*a_common*r*r,
        f_angular_native=alpha_f*alpha_f*f_radius*f_radius,
        f_time=float(f_time),
        f_radius=float(f_radius),
        n_f=float(n_f),
        alpha_f=float(alpha_f),
    )


def relative_native_hr_density(*, betas, m2: float = 1.0, Mg2: float = 1.0, **kwargs) -> float:
    geometry = relative_native_geometry(**kwargs)
    return _native_hr_density(geometry=geometry, betas=betas, m2=m2, Mg2=Mg2)


def relative_native_hr_correction_density(*, betas, m2: float = 1.0, Mg2: float = 1.0, **kwargs) -> float:
    """Finite-mu HR correction relative to the same native perturbation at mu=0.

    The reference keeps the same FLRW background jets and perturbative fields
    but removes the nonlinear background relative map.  Consequently the
    correction vanishes identically at mu=mu_dot=s=s_dot=0.
    """
    finite = relative_native_hr_density(betas=betas, m2=m2, Mg2=Mg2, **kwargs)
    ref = dict(kwargs)
    ref.update(mu=0.0, mu_dot=0.0, s=0.0, s_dot=0.0)
    linear = relative_native_hr_density(betas=betas, m2=m2, Mg2=Mg2, **ref)
    return float(finite - linear)
