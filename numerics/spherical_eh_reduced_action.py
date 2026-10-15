"""Spherically reduced Einstein-Hilbert density in areal gauge.

For a four-dimensional metric

    ds^2 = h_ab dx^a dx^b + R(x)^2 dOmega^2,

Einstein-Hilbert reduces, up to a total derivative and the overall angular
factor, to

    sqrt(-h) [R^2 R[h] + 2 (nabla R)^2 + 2].

This helper specializes to Aoki's native areal gauge

    h_ab dx^a dx^b = a(eta)^2[-e^{2 phi} d eta^2 + e^{2 psi} dr^2],
    R(eta,r) = a(eta) r.
"""
from __future__ import annotations

import math


def _validate(vals):
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all inputs must be finite")


def two_dimensional_ricci_scalar(
    *, a, a_prime, a_second, r,
    phi, phi_t, phi_r, phi_rr,
    psi, psi_t, psi_tt, psi_r,
):
    vals=(a,a_prime,a_second,r,phi,phi_t,phi_r,phi_rr,psi,psi_t,psi_tt,psi_r)
    _validate(vals)
    a=float(a); r=float(r)
    if a <= 0.0 or r <= 0.0:
        raise ValueError("a and r must be positive")
    ap=float(a_prime); app=float(a_second)
    Hc=ap/a
    Hcp=app/a-Hc*Hc

    # For ds_2^2 = -N^2 dt^2 + L^2 dr^2,
    # R_2 = 2/(NL)[ d_t(L_t/N) - d_r(N_r/L) ].
    exp_pm=math.exp(float(psi)-float(phi))
    exp_mp=1.0/exp_pm
    time_term=exp_pm*((float(psi_t)-float(phi_t))*(Hc+float(psi_t)) + Hcp + float(psi_tt))
    radial_term=exp_mp*(float(phi_rr) + (float(phi_r)-float(psi_r))*float(phi_r))
    N=a*math.exp(float(phi))
    L=a*math.exp(float(psi))
    return 2.0*(time_term-radial_term)/(N*L)


def reduced_eh_density(
    *, a, a_prime, a_second, r,
    phi, phi_t, phi_r, phi_rr,
    psi, psi_t, psi_tt, psi_r,
):
    vals=(a,a_prime,a_second,r,phi,phi_t,phi_r,phi_rr,psi,psi_t,psi_tt,psi_r)
    _validate(vals)
    a=float(a); r=float(r)
    if a <= 0.0 or r <= 0.0:
        raise ValueError("a and r must be positive")
    ap=float(a_prime)
    N=a*math.exp(float(phi))
    L=a*math.exp(float(psi))
    R=a*r
    Rt=ap*r
    Rr=a
    grad_R_sq=-(Rt*Rt)/(N*N) + (Rr*Rr)/(L*L)
    R2=two_dimensional_ricci_scalar(
        a=a,a_prime=a_prime,a_second=a_second,r=r,
        phi=phi,phi_t=phi_t,phi_r=phi_r,phi_rr=phi_rr,
        psi=psi,psi_t=psi_t,psi_tt=psi_tt,psi_r=psi_r,
    )
    return N*L*(R*R*R2 + 2.0*grad_R_sq + 2.0)
