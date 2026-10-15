"""Adjoint reduction from coordinate Stueckelberg residuals to Aoki's scalar pi."""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class HomotheticPiMapCoefficients:
    A: float
    B: float
    C: float
    D: float
    A_t: float
    B_r: float
    C_r: float
    D_t: float


def homothetic_pi_map_coefficients(*, a: float, conformal_H: float,
                                    conformal_H_prime: float, r: float,
                                    mu: float) -> HomotheticPiMapCoefficients:
    vals=(a,conformal_H,conformal_H_prime,r,mu)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("pi-map inputs must be finite")
    if a<=0.0 or r<0.0 or mu<=-1.0:
        raise ValueError("require a>0, r>=0 and mu>-1")
    inva2=1.0/(a*a)
    c=mu/(1.0+mu)
    A=-inva2
    B=inva2*r*conformal_H*c
    C=inva2/(1.0+mu)
    D=B
    return HomotheticPiMapCoefficients(
        A=A,B=B,C=C,D=D,
        A_t=2.0*conformal_H*inva2,
        B_r=inva2*conformal_H*c,
        C_r=0.0,
        D_t=inva2*r*c*(conformal_H_prime-2.0*conformal_H*conformal_H),
    )


def pi_adjoint_residual(*, E_eta, E_r, E_eta_t, E_eta_r, E_r_t, E_r_r,
                        A, B, C, D, A_t, B_r, C_r, D_t):
    """Return the Euler residual for ``delta_eta=A pi_t+B pi_r`` and
    ``delta_r=D pi_t+C pi_r`` after integration by parts.
    """
    return -(
        A_t*E_eta + A*E_eta_t
        + D_t*E_r + D*E_r_t
        + B_r*E_eta + B*E_eta_r
        + C_r*E_r + C*E_r_r
    )
