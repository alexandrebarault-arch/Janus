"""Convention bridge from JANUS/Comelli backgrounds to Lagos-Ferreira.

Lagos & Ferreira use g-sector cosmic time t with

    ds1^2 = -dt^2 + a^2 dx^2
    ds2^2 = -Nbar^2 dt^2 + b^2 dx^2.

JANUS/Comelli use g-sector conformal time and store conformal Hubble rates.
On the healthy branch the exact dictionary is

    r = b/a = xi,
    Nbar = c*xi,
    H_LF = calH/a,
    Hb_LF = H_omega/a,
    Z = m^2 f2/xi,
    Ztilde = m^2 f1/xi.

The last two identities follow from the massive-bigravity specialization of
Lagos-Ferreira Eqs. (3.14)-(3.15) together with f2=xi*J and f1=Gamma.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LagosBackground:
    a: float
    b: float
    Nbar: float
    r: float
    H: float
    Hb: float
    M1sq: float
    M2sq: float
    nu2: float
    Z: float
    Ztilde: float


def lagos_background_from_comelli(bg) -> LagosBackground:
    """Translate a JANUS/Comelli scalar background into Lagos notation.

    ``bg`` is intentionally duck-typed so this bridge stays independent of the
    old Comelli perturbation reduction; only background attributes are read.
    Planck units are normalized to M_g^2=1, hence M_f^2=kappa and
    nu^2=M_1^2/M_2^2=1/kappa.
    """
    if bg.a == 0.0 or bg.xi == 0.0 or bg.kappa == 0.0:
        raise ValueError("a, xi and kappa must be non-zero")

    return LagosBackground(
        a=float(bg.a),
        b=float(bg.a * bg.xi),
        Nbar=float(bg.c * bg.xi),
        r=float(bg.xi),
        H=float(bg.H / bg.a),
        Hb=float(bg.H_omega / bg.a),
        M1sq=1.0,
        M2sq=float(bg.kappa),
        nu2=float(1.0 / bg.kappa),
        Z=float(bg.m2 * bg.f2 / bg.xi),
        Ztilde=float(bg.m2 * bg.f1 / bg.xi),
    )
