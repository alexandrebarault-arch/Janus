"""Diagnostic decomposition of the De Felice BD algebraic scalar coefficient.

This module is deliberately read-only with respect to the physical reduction.
It decomposes the transformed Z^2 coefficient into contributions inherited from
the auxiliary-reduced old variables (Sigma,S,q_g,q_f; rates).  It is used to
locate DF5e.3e without tuning any coefficient in the action reconstruction.
"""

from __future__ import annotations

import math
import numpy as np

from numerics.comelli_case_c import case_c_background_from_a
from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives
from numerics.de_felice_two_matter_action import (
    DFKessenceFluid,
    eliminate_flat_gauge_auxiliaries,
    bd_basis_transform,
)


def bd_state_coefficient_decomposition(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    g_fluid: DFKessenceFluid,
    f_fluid: DFKessenceFluid,
    finite_difference_step: float = 5.0e-5,
) -> dict[str, float]:
    """Decompose the raw Eq. (72) ``Z^2`` coefficient before BD elimination.

    Old reduced coordinates are
    ``(Sigma,S,q_g,q_f,Sigma_dot,S_dot,q_g_dot,q_f_dot)``.
    For a pure new-coordinate Z displacement (all new rates zero), Eq. (72)
    gives

        Sigma = Z,
        q_f = A Z,
        q_f_dot = A_dot Z,

    with ``A=a/H_omega``.  Therefore the transformed Z^2 Hessian is the sum of
    six explicitly auditable old-basis pieces listed below.

    ``C_ZZ`` is the transformed state/rate coefficient multiplying ``Z Zdot``;
    it is returned separately because its time derivative contributes to the
    effective algebraic coefficient after integration by parts.
    """
    reduced = eliminate_flat_gauge_auxiliaries(
        bg, bgp, betas=betas, g_fluid=g_fluid, f_fluid=f_fluid,
        finite_difference_step=finite_difference_step,
    )
    H0 = np.asarray(reduced.reduced_hessian, dtype=float)
    if H0.shape != (8, 8):
        raise ValueError("auxiliary-reduced Hessian must be 8x8")

    if bg.H_omega == 0.0:
        raise ValueError("H_omega must be non-zero")
    A = bg.a / bg.H_omega
    A_dot = (bg.H * bg.H_omega - bgp.H_omega_prime) / (bg.H_omega * bg.H_omega)

    sigma = 0
    qf = 3
    sigma_dot = 4
    qf_dot = 7

    pieces = {
        "Sigma2": H0[sigma, sigma],
        "2A_Sigma_qf": 2.0 * A * H0[sigma, qf],
        "A2_qf2": A * A * H0[qf, qf],
        "2Adot_Sigma_qfdot": 2.0 * A_dot * H0[sigma, qf_dot],
        "2AAdot_qf_qfdot": 2.0 * A * A_dot * H0[qf, qf_dot],
        "Adot2_qfdot2": A_dot * A_dot * H0[qf_dot, qf_dot],
    }
    raw_hzz = float(sum(pieces.values()))

    M = bd_basis_transform(bg, bgp)
    transformed = M.T @ H0 @ M
    H = 0.5 * (transformed + transformed.T)
    transformed_hzz = float(H[3, 3])
    transformed_czz = float(H[3, 7])

    # Direct old-basis reconstruction of H[Z,Zdot].  A pure Zdot displacement
    # has Sigma_dot=1 and q_f_dot=A in the old rate coordinates.
    z_state = np.zeros(8, dtype=float)
    z_state[sigma] = 1.0
    z_state[qf] = A
    z_state[qf_dot] = A_dot
    z_rate = np.zeros(8, dtype=float)
    z_rate[sigma_dot] = 1.0
    z_rate[qf_dot] = A
    czz = float(z_state @ H0 @ z_rate)

    return {
        **{k: float(v) for k, v in pieces.items()},
        "A": float(A),
        "A_dot": float(A_dot),
        "raw_hZZ": raw_hzz,
        "transformed_hZZ": transformed_hzz,
        "C_ZZ": czz,
        "transformed_C_ZZ": transformed_czz,
    }


def _case_c_audit_pieces(
    a: float,
    k: float,
    *,
    f_cs2: float,
    finite_difference_step: float,
    f_pressure: float = 0.0,
) -> tuple[dict[str, float], ScalarBackground]:
    point = case_c_background_from_a(a, k=k)
    g = DFKessenceFluid(
        rho=point.rho1,
        pressure=point.rho1 / 3.0,
        cs2=1.0 / 3.0,
    )
    f = DFKessenceFluid(
        rho=point.rho2,
        pressure=f_pressure,
        cs2=f_cs2,
    )
    pieces = bd_state_coefficient_decomposition(
        point.metric,
        point.derivatives,
        betas=(0.0, 1.0, 0.0, 0.0, 0.0),
        g_fluid=g,
        f_fluid=f,
        finite_difference_step=finite_difference_step,
    )
    return pieces, point.metric


def case_c_bd_effective_coefficient(
    *,
    a: float,
    k: float,
    f_cs2: float = 0.1,
    background_step_fraction: float = 1.0e-4,
    finite_difference_step: float = 2.0e-6,
    pressure_probe_fraction: float = 1.0e-4,
) -> dict[str, float]:
    """Evaluate the time-corrected BD algebraic coefficient on exact Case C.

    The action reconstructed in ``de_felice_two_matter_action`` is normalized
    with an overall g-sector spatial measure ``a^3``.  For a term
    ``C_ZZ Z Zdot`` the integration-by-parts correction to the Z^2 Hessian is

        dot(C_ZZ) + 3 H_g C_ZZ.

    ``ScalarBackground.H`` is the conformal Hubble rate ``calH=a H_g``.
    With g-lapse N=1, ``dot(a)=a H_g=calH``.

    The derivative of ``C_ZZ`` must follow the local P(X) background tangent.
    Case C is dust in the f sector at the control point, but the finite-cs2
    diagnostic fluid obeys ``dot(P_f)=cs_f^2 dot(rho_f)``.  We therefore split
    the chain rule into a pressure-frozen background derivative and an
    independently conditioned pressure derivative,

        dot(C_ZZ) = (partial C_ZZ/partial a)_P * dot(a)
                    + (partial C_ZZ/partial P_f) * dot(P_f),

    with ``dot(P_f)=-3 n H_f cs_f^2 (rho_f+P_f)`` at ``P_f=0``.

    This helper remains diagnostic only and does not alter the physical
    reducer.
    """
    values = (
        a, k, f_cs2, background_step_fraction,
        finite_difference_step, pressure_probe_fraction,
    )
    if not all(math.isfinite(v) for v in values):
        raise ValueError("all audit inputs must be finite")
    if a <= 0.0 or k <= 0.0 or f_cs2 <= 0.0:
        raise ValueError("a, k and f_cs2 must be positive")
    if background_step_fraction <= 0.0 or background_step_fraction >= 0.25:
        raise ValueError("background_step_fraction must lie in (0,0.25)")
    if pressure_probe_fraction <= 0.0 or pressure_probe_fraction >= 0.1:
        raise ValueError("pressure_probe_fraction must lie in (0,0.1)")

    da = a * background_step_fraction
    if a - da <= 0.0:
        raise ValueError("background step crosses a=0")

    center, bg = _case_c_audit_pieces(
        a, k, f_cs2=f_cs2, finite_difference_step=finite_difference_step,
        f_pressure=0.0,
    )
    minus, _ = _case_c_audit_pieces(
        a - da, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
        f_pressure=0.0,
    )
    plus, _ = _case_c_audit_pieces(
        a + da, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
        f_pressure=0.0,
    )

    dC_da_frozen = (plus["C_ZZ"] - minus["C_ZZ"]) / (2.0 * da)
    a_dot = bg.H  # conformal H = a H_cosmic = da/dt for N=1.
    dot_C_background = dC_da_frozen * a_dot

    point = case_c_background_from_a(a, k=k)
    dP = point.rho2 * pressure_probe_fraction
    pminus, _ = _case_c_audit_pieces(
        a, k, f_cs2=f_cs2, finite_difference_step=finite_difference_step,
        f_pressure=-dP,
    )
    pplus, _ = _case_c_audit_pieces(
        a, k, f_cs2=f_cs2, finite_difference_step=finite_difference_step,
        f_pressure=dP,
    )
    dC_dP = (pplus["C_ZZ"] - pminus["C_ZZ"]) / (2.0 * dP)

    # n H_f = H_omega/a in the repository's g-cosmic convention.
    nHf = bg.H_omega / bg.a
    dot_P_f = -3.0 * nHf * f_cs2 * point.rho2
    dot_C_pressure = dC_dP * dot_P_f
    dot_C = dot_C_background + dot_C_pressure

    H_cosmic = bg.H / bg.a
    measure_term = 3.0 * H_cosmic * center["C_ZZ"]
    time_correction = dot_C + measure_term
    effective = center["raw_hZZ"] - time_correction

    return {
        **center,
        "a": float(a),
        "k": float(k),
        "background_da": float(da),
        # Backward-compatible name: this is the derivative at frozen P_f.
        "dC_da": float(dC_da_frozen),
        "dC_da_frozen_pressure": float(dC_da_frozen),
        "partial_C_ZZ_partial_P_f": float(dC_dP),
        "a_dot": float(a_dot),
        "conformal_H": float(bg.H),
        "H_cosmic": float(H_cosmic),
        "dot_P_f": float(dot_P_f),
        "dot_C_ZZ_background": float(dot_C_background),
        "dot_C_ZZ_pressure": float(dot_C_pressure),
        "dot_C_ZZ": float(dot_C),
        "measure_3H_C_ZZ": float(measure_term),
        "time_correction": float(time_correction),
        "effective_hZZ": float(effective),
    }
