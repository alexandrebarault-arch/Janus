"""Direct rectangular scalar descriptor for JANUS-R Gate 2B.

This module keeps the full Comelli scalar system as a polynomial differential
operator instead of choosing a square ODE closure.  At a frozen background
point, D=d/dtau is represented by ``s`` and the 13 published scalar equations
act on 11 perturbation variables through

    P(s) x = (P0 + s P1 + s^2 P2) x = 0.

No variable is declared dynamical a priori.  In particular, E' is not
prescribed and the printed/derived variants of A.18 remain separate until the
constraint/descriptor structure is diagnosed.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives


STATE_ORDER = (
    "E", "Phi1", "Phi2", "B1", "B2", "F1", "F2",
    "delta_rho1", "u1", "delta_rho2", "u2",
)

ROW_ORDER = (
    "g00", "g0i", "f00", "f0i", "B_relation", "A17", "A18",
    "g_trace", "f_trace", "g_continuity", "g_euler",
    "f_continuity", "f_euler",
)


@dataclass(frozen=True)
class LocalBarotropicFluid:
    rho: float
    w: float

    def __post_init__(self):
        if self.rho == 0.0:
            raise ValueError("rho must be non-zero")
        if 1.0 + self.w == 0.0:
            raise ValueError("1+w must be non-zero")


def polynomial_residual(
    s,
    state,
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    g_fluid: LocalBarotropicFluid,
    f_fluid: LocalBarotropicFluid,
    a18_variant: str = "derived_prime",
) -> np.ndarray:
    """Evaluate the direct 13-equation scalar polynomial at derivative ``s``.

    Background coefficients and their first conformal-time derivatives are
    frozen at the evaluation point.  Derivatives of coefficient-weighted
    metric potentials are nevertheless retained exactly through ``bgp``.
    """
    if a18_variant not in ("derived_prime", "printed_unprime"):
        raise ValueError("unknown A.18 variant")
    if bg.c == 0.0 or bg.xi == 0.0 or bg.kappa == 0.0:
        raise ValueError("c, xi and kappa must be non-zero")

    x = np.asarray(state)
    if x.shape != (11,):
        raise ValueError("descriptor state must have length 11")

    E, P1, P2, B1, B2, F1, F2, dr1, u1, dr2, u2 = x
    a2 = bg.a**2
    c2 = bg.c**2
    xi2 = bg.xi**2

    K1 = a2 * bg.m2 * bg.f1
    K1_p = a2 * bg.m2 * (bgp.f1_prime + 2.0*bg.H*bg.f1)
    psi1 = K1*E - P1
    psi1_p = K1_p*E + K1*s*E - s*P1

    K2 = a2 * bg.m2 * bg.f1 / (bg.kappa*bg.c*xi2)
    K2_p = K2 * (
        2.0*bg.H
        + bgp.f1_prime/bg.f1
        - bgp.c_prime/bg.c
        - 2.0*bgp.xi_prime/bg.xi
    ) if bg.f1 != 0.0 else (
        a2*bg.m2/(bg.kappa*bg.c*xi2) * bgp.f1_prime
    )
    psi2 = -K2*E - P2
    psi2_p = -K2_p*E - K2*s*E - s*P2

    dphi = P1-P2
    a_diff = (
        (B1-s*E)
        * (bg.c*(bg.H-bg.H_omega)-bgp.c_prime)
        / c2
    )
    a_sum = (
        2.0*bg.c**3*(psi2-psi1)
        + B1*(bg.c*(bg.H_omega+bg.H)-3.0*bgp.c_prime)
        + 3.0*bgp.c_prime*s*E
        + bg.c*(2.0*s*B1-2.0*s*s*E-s*E*(bg.H_omega+bg.H))
    ) / c2
    A1 = 0.5*(a_sum-a_diff)
    A2 = 0.5*(a_sum+a_diff)

    g00 = (
        -2.0*bg.k2*P1
        + 6.0*bg.H*(psi1*bg.H-s*P1)
        + a2*bg.m2*bg.f2*(3.0*F1+bg.k2*E)
        + bg.G8pi*a2*dr1
    )
    g0i = (
        2.0*psi1*bg.H - 2.0*s*P1
        + a2*bg.m2*bg.f2*B1/(1.0+bg.c)
        + bg.G8pi*a2*(1.0+g_fluid.w)*g_fluid.rho*u1
    )
    f00 = (
        -2.0*c2*bg.k2*P2
        + 6.0*bg.H_omega*(psi2*bg.H_omega-s*P2)
        + bg.m2*a2*bg.f2*c2/(bg.kappa*xi2)*(-bg.k2*E-3.0*F2)
        + bg.G8pi/bg.kappa*a2*c2*xi2*dr2
    )
    f0i = (
        2.0*bg.c*(psi2*bg.H_omega-s*P2)
        - bg.m2*a2*bg.f2*B2/(bg.kappa*xi2*(1.0+bg.c))
        + bg.G8pi/bg.kappa*bg.c*a2*xi2
        * (1.0+f_fluid.w)*f_fluid.rho*u2
    )

    b_relation = B2-B1+(1.0-c2)*s*E
    a17 = (
        bg.H_omega*F2-bg.H*F1
        -(bg.H-bg.H_omega)*dphi
    )
    if a18_variant == "derived_prime":
        b_minus_e = B1-s*E
    else:
        b_minus_e = B1-E
    a18 = (
        c2*(F2+F1)
        - b_minus_e*(bg.H+bg.H_omega)
        + 2.0*c2*dphi
    )

    g_trace = (
        bg.m2*a2*(2.0*bg.f1*F1+bg.f2*A1)
        + 2.0*psi1*(bg.H**2+2.0*bgp.H_prime)
        - 2.0*s*s*P1
        - 2.0*bg.H*(2.0*s*P1-psi1_p)
        - bg.G8pi*a2*g_fluid.w*dr1
    )
    f_trace = (
        bg.m2*a2/(bg.kappa*xi2)*(2.0*bg.c*bg.f1*F2+bg.f2*A2)
        + 2.0*(
            bg.H_omega**2+2.0*bgp.H_omega_prime
            - 2.0*(bgp.c_prime/bg.c)*bg.H_omega
        )*psi2
        - 2.0*s*s*P2
        + 2.0*(bgp.c_prime/bg.c-2.0*bg.H_omega)*s*P2
        + 2.0*bg.H_omega*psi2_p
        - bg.G8pi/bg.kappa*a2*c2*xi2*f_fluid.w*dr2
    )

    g_cont = (
        s*dr1
        - (1.0+g_fluid.w)*(
            g_fluid.rho*(bg.k2*u1-3.0*s*P1)
            - 3.0*bg.H*dr1
        )
    )
    g_euler = (
        s*u1
        - (3.0*g_fluid.w-1.0)*bg.H*u1
        + g_fluid.w/(1.0+g_fluid.w)*dr1/g_fluid.rho
        + psi1
    )
    f_cont = (
        s*dr2
        - (1.0+f_fluid.w)*(
            f_fluid.rho*(bg.k2*u2-3.0*s*P2)
            - 3.0*bg.H_omega*dr2
        )
    )
    f_euler = (
        s*u2
        - u2*((3.0*f_fluid.w-1.0)*bg.H_omega+bgp.c_prime/bg.c)
        + c2*(f_fluid.w/(1.0+f_fluid.w)*dr2/f_fluid.rho+psi2)
    )

    return np.asarray([
        g00, g0i, f00, f0i, b_relation, a17, a18,
        g_trace, f_trace, g_cont, g_euler, f_cont, f_euler,
    ])


def polynomial_coefficients(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    g_fluid: LocalBarotropicFluid,
    f_fluid: LocalBarotropicFluid,
    a18_variant: str = "derived_prime",
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return ``(P0,P1,P2)`` for the rectangular scalar polynomial matrix."""
    p_at = []
    for s in (0.0, 1.0, -1.0):
        mat = np.empty((13, 11), dtype=float)
        for j in range(11):
            basis = np.zeros(11, dtype=float)
            basis[j] = 1.0
            mat[:, j] = polynomial_residual(
                s, basis, bg, bgp,
                g_fluid=g_fluid,
                f_fluid=f_fluid,
                a18_variant=a18_variant,
            )
        p_at.append(mat)
    p0, pp, pm = p_at
    p1 = 0.5*(pp-pm)
    p2 = 0.5*(pp+pm)-p0
    return p0, p1, p2
