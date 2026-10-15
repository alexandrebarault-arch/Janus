"""Compact-support homothetic Aoki action oracle from the exact HR potential.

This module is an audit helper. It evaluates the exact spherical Hassan-Rosen
interaction on the Aoki oscillation map, using compact support in conformal time
and radius so total-derivative boundary terms vanish before the quadratic
coefficients are fitted.

It deliberately does not contain the published Aoki K_S or c_S^2 formulas.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class CompactActionCoefficients:
    kinetic_hessian_coefficient: float
    gradient_hessian_coefficient: float
    sound_speed_squared: float
    zero_hubble_hessian: float
    fit_residual: float


def _profiles(t, r, T, R):
    x = t/T
    A = (1.0-x*x)**3
    At = (-6.0*x*(1.0-x*x)**2)/T
    Att = (-6.0+36.0*x*x-30.0*x**4)/(T*T)
    F = r*r - 3.0*r**4/R**2 + 3.0*r**6/R**4 - r**8/R**6
    Fr = 2.0*r - 12.0*r**3/R**2 + 18.0*r**5/R**4 - 8.0*r**7/R**6
    Frr = 2.0 - 36.0*r**2/R**2 + 90.0*r**4/R**4 - 56.0*r**6/R**6
    return A, At, Att, F, Fr, Frr


def _action(*, amp, hubble, beta1, beta2, beta3, K, w, mu, T, R, order):
    x_t, w_t = np.polynomial.legendre.leggauss(order)
    x_r, w_r = np.polynomial.legendre.leggauss(order)
    t = T*x_t[:, None] + np.zeros((1, order))
    r = 0.5*R*(x_r[None, :]+1.0) + np.zeros((order, 1))
    weights = (T*w_t[:, None])*(0.5*R*w_r[None, :])

    A, At, Att, F, Fr, Frr = _profiles(t, r, T, R)
    C = mu/(1.0+mu)
    M = mu*(2.0+mu)
    p = 2.0/(1.0+3.0*w)

    Hc = hubble/(1.0+hubble*t/p)
    Hcp = -0.5*(1.0+3.0*w)*Hc*Hc
    abase = (1.0+hubble*t/p)**p
    inv_a2 = abase**-2

    P = amp*At*F
    Q = amp*A*Fr
    Pt = amp*Att*F
    Pr = amp*At*Fr
    Qt = Pr
    Qr = amp*A*Frr

    deta = inv_a2*(-P + r*Hc*C*Q)
    drad = inv_a2*(Q/(1.0+mu) + r*Hc*C*P)
    inv_a2_t = -2.0*Hc*inv_a2
    deta_t = (
        inv_a2_t*(-P+r*Hc*C*Q)
        + inv_a2*(-Pt+r*C*(Hcp*Q+Hc*Qt))
    )
    deta_r = inv_a2*(-Pr+C*Hc*(Q+r*Qr))
    drad_t = (
        inv_a2_t*(Q/(1.0+mu)+r*Hc*C*P)
        + inv_a2*(Qt/(1.0+mu)+r*C*(Hcp*P+Hc*Pt))
    )
    drad_r = inv_a2*(Qr/(1.0+mu)+C*Hc*(P+r*Pr))

    eta_g = t+deta
    r_g = r+drad
    a_g = (1.0+hubble*eta_g/p)**p
    j00 = 1.0+deta_t
    j01 = deta_r
    j10 = drad_t
    j11 = 1.0+drad_r

    g00 = a_g*a_g*(-j00*j00+j10*j10)
    g01 = a_g*a_g*(-j00*j01+j10*j11)
    g11 = a_g*a_g*(-j01*j01+j11*j11)
    det_g2 = g00*g11-g01*g01
    gi00 = g11/det_g2
    gi01 = -g01/det_g2
    gi11 = g00/det_g2

    eta_f = t-0.5*Hc*r*r*M
    eta_f_t = 1.0-0.5*Hcp*r*r*M
    eta_f_r = -Hc*r*M
    r_f = (1.0+mu)*r
    a_f = (1.0+hubble*eta_f/p)**p
    fk = (K*a_f)**2
    f00 = fk*(-eta_f_t*eta_f_t)
    f01 = fk*(-eta_f_t*eta_f_r)
    f11 = fk*(-eta_f_r*eta_f_r+(1.0+mu)**2)

    A00 = gi00*f00+gi01*f01
    A01 = gi00*f01+gi01*f11
    A10 = gi01*f00+gi11*f01
    A11 = gi01*f01+gi11*f11
    det_A = A00*A11-A01*A10
    tr_A = A00+A11
    if np.any(det_A <= 0.0) or np.any(tr_A+2.0*np.sqrt(det_A) <= 0.0):
        raise ValueError("principal HR square root left the real branch")
    root_det = np.sqrt(det_A)
    tr_S = np.sqrt(tr_A+2.0*root_det)
    ell = K*a_f*r_f/(a_g*r_g)

    e1 = tr_S+2.0*ell
    e2 = root_det+2.0*ell*tr_S+ell*ell
    e3 = 2.0*ell*root_det+ell*ell*tr_S
    potential = beta1*e1+beta2*e2+beta3*e3
    det_J = j00*j11-j01*j10
    sqrt_minus_g = a_g**4*det_J*r_g*r_g
    return float(np.sum(weights*sqrt_minus_g*potential))


def _amplitude_hessian(*, hubble, amplitude_step, **kwargs):
    h = amplitude_step
    fp = _action(amp=h, hubble=hubble, **kwargs)
    f0 = _action(amp=0.0, hubble=hubble, **kwargs)
    fm = _action(amp=-h, hubble=hubble, **kwargs)
    return (fp-2.0*f0+fm)/(h*h)


def _profile_integrals(T, R, order):
    x_t, w_t = np.polynomial.legendre.leggauss(order)
    x_r, w_r = np.polynomial.legendre.leggauss(order)
    t = T*x_t
    r = 0.5*R*(x_r+1.0)
    wt = T*w_t
    wr = 0.5*R*w_r
    A, At, _, F, Fr, _ = _profiles(t[:, None], r[None, :], T, R)
    int_kin = float(np.sum((wt[:, None]*wr[None, :])*(r[None, :]**2)*(At*F)**2))
    int_grad = float(np.sum((wt[:, None]*wr[None, :])*(r[None, :]**2)*(A*Fr)**2))
    return int_kin, int_grad


def recover_homothetic_pi_coefficients(
    *, beta1, beta2, beta3, K, w, mu,
    time_scales=(0.5, 1.0, 2.0), radius=1.0,
    hubble_step=0.007, amplitude_step=0.002, quadrature_order=36,
):
    """Fit the H^2 quadratic ``pi`` action from the exact compact HR action.

    The returned coefficients are Hessian coefficients. The sound speed is
    inferred only from the independently fitted gradient/kinetic ratio.
    """
    vals = (beta1, beta2, beta3, K, w, mu, radius, hubble_step, amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all inputs must be finite")
    if K <= 0.0 or mu <= -1.0 or radius <= 0.0 or hubble_step <= 0.0 or amplitude_step <= 0.0:
        raise ValueError("invalid compact-action inputs")
    if abs(1.0+3.0*w) < 1.0e-12:
        raise ValueError("w=-1/3 requires a separate conformal-time background chart")
    if quadrature_order < 12:
        raise ValueError("quadrature_order must be at least 12")

    rows = []
    rhs = []
    zero_h = []
    common = dict(
        beta1=beta1, beta2=beta2, beta3=beta3,
        K=K, w=w, mu=mu, R=radius, order=quadrature_order,
    )
    for T in time_scales:
        T = float(T)
        if not math.isfinite(T) or T <= 0.0:
            raise ValueError("time_scales must be positive and finite")
        hp = _amplitude_hessian(hubble=hubble_step, amplitude_step=amplitude_step, T=T, **common)
        hm = _amplitude_hessian(hubble=-hubble_step, amplitude_step=amplitude_step, T=T, **common)
        h0 = _amplitude_hessian(hubble=0.0, amplitude_step=amplitude_step, T=T, **common)
        h2 = (hp+hm-2.0*h0)/(2.0*hubble_step*hubble_step)
        ik, ig = _profile_integrals(T, radius, quadrature_order)
        rows.append((ik, ig))
        rhs.append(h2)
        zero_h.append(abs(h0))

    X = np.asarray(rows, dtype=float)
    y = np.asarray(rhs, dtype=float)
    coeff, _, rank, _ = np.linalg.lstsq(X, y, rcond=None)
    if rank != 2 or abs(coeff[0]) < 1.0e-14:
        raise np.linalg.LinAlgError("compact profile fit is rank deficient")
    residual = float(np.linalg.norm(X@coeff-y)/max(1.0, np.linalg.norm(y)))
    return CompactActionCoefficients(
        kinetic_hessian_coefficient=float(coeff[0]),
        gradient_hessian_coefficient=float(coeff[1]),
        sound_speed_squared=float(-coeff[1]/coeff[0]),
        zero_hubble_hessian=float(max(zero_h)),
        fit_residual=residual,
    )
