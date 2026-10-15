"""Adjoint reduction from coordinate Stueckelberg residuals to Aoki's scalar pi."""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class HomotheticPiModeJet:
    delta_eta: complex
    delta_r: complex
    delta_eta_t: complex
    delta_eta_r: complex
    delta_r_t: complex
    delta_r_r: complex


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


def homothetic_pi_mode_jet(*, a: float, conformal_H: float, conformal_H_prime: float,
                            r: float, mu: float, omega: float, k: float,
                            pi: complex = 1.0 + 0.0j) -> HomotheticPiModeJet:
    c = homothetic_pi_map_coefficients(
        a=a, conformal_H=conformal_H, conformal_H_prime=conformal_H_prime,
        r=r, mu=mu,
    )
    pi = complex(pi)
    pt = -1j*omega*pi
    pr = 1j*k*pi
    ptt = -(omega*omega)*pi
    ptr = (omega*k)*pi
    prr = -(k*k)*pi
    B_t = c.D_t
    C_t = -2.0*conformal_H*c.C
    D_r = c.B_r
    delta_eta = c.A*pt + c.B*pr
    delta_r = c.D*pt + c.C*pr
    delta_eta_t = c.A_t*pt + c.A*ptt + B_t*pr + c.B*ptr
    delta_eta_r = c.A*ptr + c.B_r*pr + c.B*prr
    delta_r_t = c.D_t*pt + c.D*ptt + C_t*pr + c.C*ptr
    delta_r_r = D_r*pt + c.D*ptr + c.C_r*pr + c.C*prr
    return HomotheticPiModeJet(
        delta_eta=delta_eta, delta_r=delta_r,
        delta_eta_t=delta_eta_t, delta_eta_r=delta_eta_r,
        delta_r_t=delta_r_t, delta_r_r=delta_r_r,
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
