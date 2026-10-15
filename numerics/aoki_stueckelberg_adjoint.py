"""Adjoint reduction from coordinate Stueckelberg residuals to Aoki's scalar pi."""
from __future__ import annotations


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
