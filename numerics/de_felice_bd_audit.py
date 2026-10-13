"""Diagnostic decomposition of the De Felice BD algebraic scalar coefficient.

This module is deliberately read-only with respect to the physical reduction.
It decomposes the transformed Z^2 coefficient into contributions inherited from
the auxiliary-reduced old variables (Sigma,S,q_g,q_f; rates).  It is used to
locate DF5e.3e without tuning any coefficient in the action reconstruction.
"""

from __future__ import annotations

import numpy as np

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
    H = 0.5 * (M.T @ H0 @ M + (M.T @ H0 @ M).T)
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
