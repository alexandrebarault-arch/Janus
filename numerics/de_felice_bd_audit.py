"""Pressure-consistent audit of the De Felice BD algebraic scalar.

This module is diagnostic.  It uses the same EH, P(X), Eq. (72) transform and
auxiliary Schur structure as the baseline reducer, but obtains the HR block from
the already-quadratic Eqs. (45)-(46) backend so that a second background-time
derivative is numerically well conditioned.
"""

from __future__ import annotations

import math
import numpy as np

from numerics.bd_time_canonicalization import canonicalize_linear_zdot_time_dependent
from numerics.comelli_case_c import case_c_background_from_a
from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives
from numerics.de_felice_two_matter_action import (
    DFKessenceFluid,
    PhysicalFlatGaugeAction,
    bd_basis_transform,
)
from numerics.de_felice_two_matter_exact_quadratic import (
    eliminate_flat_gauge_auxiliaries_exact_quadratic,
)

_BETAS_BETA1 = (0.0, 1.0, 0.0, 0.0, 0.0)


def _validate_positive(*values: float) -> None:
    if not all(math.isfinite(v) and v > 0.0 for v in values):
        raise ValueError("audit inputs must be finite and positive")


def _case_c_fluids(point, *, f_cs2: float, f_pressure: float):
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
    return g, f


def _reduced_hessian(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    g_fluid: DFKessenceFluid,
    f_fluid: DFKessenceFluid,
    finite_difference_step: float,
) -> np.ndarray:
    reduced = eliminate_flat_gauge_auxiliaries_exact_quadratic(
        bg,
        bgp,
        betas=betas,
        g_fluid=g_fluid,
        f_fluid=f_fluid,
        finite_difference_step=finite_difference_step,
    )
    H0 = np.asarray(reduced.reduced_hessian, dtype=float)
    if H0.shape != (8, 8):
        raise ValueError("auxiliary-reduced Hessian must be 8x8")
    return H0


def bd_state_coefficient_decomposition(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    g_fluid: DFKessenceFluid,
    f_fluid: DFKessenceFluid,
    finite_difference_step: float = 5.0e-5,
) -> dict[str, float]:
    """Decompose the raw Eq. (72) ``Z^2`` coefficient and reconstruct C_ZZ."""
    H0 = _reduced_hessian(
        bg,
        bgp,
        betas=betas,
        g_fluid=g_fluid,
        f_fluid=f_fluid,
        finite_difference_step=finite_difference_step,
    )
    if bg.H_omega == 0.0:
        raise ValueError("H_omega must be non-zero")

    A = bg.a / bg.H_omega
    A_dot = (
        bg.H * bg.H_omega - bgp.H_omega_prime
    ) / (bg.H_omega * bg.H_omega)

    sigma, qf, sigma_dot, qf_dot = 0, 3, 4, 7
    pieces = {
        "Sigma2": H0[sigma, sigma],
        "2A_Sigma_qf": 2.0 * A * H0[sigma, qf],
        "A2_qf2": A * A * H0[qf, qf],
        "2Adot_Sigma_qfdot": 2.0 * A_dot * H0[sigma, qf_dot],
        "2AAdot_qf_qfdot": 2.0 * A * A_dot * H0[qf, qf_dot],
        "Adot2_qfdot2": A_dot * A_dot * H0[qf_dot, qf_dot],
    }
    raw_hzz = float(sum(pieces.values()))

    transform = bd_basis_transform(bg, bgp)
    transformed = transform.T @ H0 @ transform
    H = 0.5 * (transformed + transformed.T)

    z_state = np.zeros(8, dtype=float)
    z_state[sigma] = 1.0
    z_state[qf] = A
    z_state[qf_dot] = A_dot
    z_rate = np.zeros(8, dtype=float)
    z_rate[sigma_dot] = 1.0
    z_rate[qf_dot] = A
    czz = float(z_state @ H0 @ z_rate)

    return {
        **{name: float(value) for name, value in pieces.items()},
        "A": float(A),
        "A_dot": float(A_dot),
        "raw_hZZ": raw_hzz,
        "transformed_hZZ": float(H[3, 3]),
        "C_ZZ": czz,
        "transformed_C_ZZ": float(H[3, 7]),
    }


def _case_c_audit_pieces(
    a: float,
    k: float,
    *,
    f_cs2: float,
    finite_difference_step: float,
    f_pressure: float = 0.0,
):
    point = case_c_background_from_a(a, k=k)
    g, f = _case_c_fluids(point, f_cs2=f_cs2, f_pressure=f_pressure)
    pieces = bd_state_coefficient_decomposition(
        point.metric,
        point.derivatives,
        betas=_BETAS_BETA1,
        g_fluid=g,
        f_fluid=f,
        finite_difference_step=finite_difference_step,
    )
    return pieces, point


def _case_c_transformed_hessian(
    a: float,
    k: float,
    *,
    f_cs2: float,
    finite_difference_step: float,
    f_pressure: float = 0.0,
):
    point = case_c_background_from_a(a, k=k)
    g, f = _case_c_fluids(point, f_cs2=f_cs2, f_pressure=f_pressure)
    H0 = _reduced_hessian(
        point.metric,
        point.derivatives,
        betas=_BETAS_BETA1,
        g_fluid=g,
        f_fluid=f,
        finite_difference_step=finite_difference_step,
    )
    transform = bd_basis_transform(point.metric, point.derivatives)
    H = transform.T @ H0 @ transform
    return 0.5 * (H + H.T), point


def _pressure_tangent(point, *, f_cs2: float) -> float:
    # n H_f = H_omega/a in the repository's g-cosmic convention.
    nHf = point.metric.H_omega / point.metric.a
    return float(-3.0 * nHf * f_cs2 * point.rho2)


def case_c_bd_effective_coefficient(
    *,
    a: float,
    k: float,
    f_cs2: float = 0.1,
    background_step_fraction: float = 1.0e-4,
    finite_difference_step: float = 2.0e-6,
    pressure_probe_fraction: float = 1.0e-4,
) -> dict[str, float]:
    """Return pressure-consistent ``h_ZZ^eff`` on exact Case C."""
    _validate_positive(
        a, k, f_cs2, background_step_fraction,
        finite_difference_step, pressure_probe_fraction,
    )
    if background_step_fraction >= 0.25:
        raise ValueError("background_step_fraction must be below 0.25")
    if pressure_probe_fraction >= 0.1:
        raise ValueError("pressure_probe_fraction must be below 0.1")

    da = a * background_step_fraction
    if a - da <= 0.0:
        raise ValueError("background step crosses a=0")

    center, point = _case_c_audit_pieces(
        a, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
    )
    minus, _ = _case_c_audit_pieces(
        a - da, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
    )
    plus, _ = _case_c_audit_pieces(
        a + da, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
    )
    dC_da = (plus["C_ZZ"] - minus["C_ZZ"]) / (2.0 * da)

    dP = point.rho2 * pressure_probe_fraction
    pminus, _ = _case_c_audit_pieces(
        a, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
        f_pressure=-dP,
    )
    pplus, _ = _case_c_audit_pieces(
        a, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
        f_pressure=dP,
    )
    dC_dP = (pplus["C_ZZ"] - pminus["C_ZZ"]) / (2.0 * dP)

    bg = point.metric
    a_dot = bg.H
    dot_C_background = dC_da * a_dot
    dot_P_f = _pressure_tangent(point, f_cs2=f_cs2)
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
        "dC_da": float(dC_da),
        "dC_da_frozen_pressure": float(dC_da),
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


def case_c_time_dependent_physical_action(
    *,
    a: float,
    k: float,
    f_cs2: float = 0.1,
    background_step_fraction: float = 1.0e-3,
    finite_difference_step: float = 2.0e-6,
    pressure_probe_fraction: float = 1.0e-4,
) -> PhysicalFlatGaugeAction:
    """Time-canonicalize and Schur-eliminate the BD scalar on Case C."""
    _validate_positive(
        a, k, f_cs2, background_step_fraction,
        finite_difference_step, pressure_probe_fraction,
    )
    if background_step_fraction >= 0.25:
        raise ValueError("background_step_fraction must be below 0.25")
    if pressure_probe_fraction >= 0.1:
        raise ValueError("pressure_probe_fraction must be below 0.1")

    da = a * background_step_fraction
    if a - da <= 0.0:
        raise ValueError("background step crosses a=0")

    center, point = _case_c_transformed_hessian(
        a, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
    )
    minus, _ = _case_c_transformed_hessian(
        a - da, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
    )
    plus, _ = _case_c_transformed_hessian(
        a + da, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
    )
    dc_da = (plus[:4, 7] - minus[:4, 7]) / (2.0 * da)

    dP = point.rho2 * pressure_probe_fraction
    pminus, _ = _case_c_transformed_hessian(
        a, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
        f_pressure=-dP,
    )
    pplus, _ = _case_c_transformed_hessian(
        a, k, f_cs2=f_cs2,
        finite_difference_step=finite_difference_step,
        f_pressure=dP,
    )
    dc_dP = (pplus[:4, 7] - pminus[:4, 7]) / (2.0 * dP)

    bg = point.metric
    dot_c = dc_da * bg.H + dc_dP * _pressure_tangent(point, f_cs2=f_cs2)
    mu_measure = 3.0 * bg.H / bg.a

    Kraw = center[4:8, 4:8]
    kscale = max(1.0, float(np.linalg.norm(Kraw, ord=np.inf)))
    zdot_kinetic_residual = float(max(
        np.linalg.norm(Kraw[3, :], ord=np.inf),
        np.linalg.norm(Kraw[:, 3], ord=np.inf),
    ) / kscale)

    canonical = canonicalize_linear_zdot_time_dependent(
        center,
        dot_c=dot_c,
        mu_measure=mu_measure,
    )
    keep7 = [0, 1, 2, 3, 4, 5, 6]
    H7 = canonical[np.ix_(keep7, keep7)]
    zidx = 3
    hzz = float(H7[zidx, zidx])
    if abs(hzz) <= 1.0e-14 * max(1.0, float(np.linalg.norm(H7, ord=np.inf))):
        raise np.linalg.LinAlgError("BD scalar is not algebraically invertible")

    phys = [0, 1, 2, 4, 5, 6]
    Hp = H7[np.ix_(phys, phys)]
    hpz = H7[np.ix_(phys, [zidx])]
    Hphys = Hp - hpz @ hpz.T / hzz
    Hphys = 0.5 * (Hphys + Hphys.T)
    K = 0.5 * (Hphys[3:6, 3:6] + Hphys[3:6, 3:6].T)

    return PhysicalFlatGaugeAction(
        transformed_hessian=np.asarray(center, dtype=float),
        canonical_hessian=np.asarray(canonical, dtype=float),
        physical_hessian=np.asarray(Hphys, dtype=float),
        kinetic_hessian=np.asarray(K, dtype=float),
        bd_algebraic_coefficient=hzz,
        zdot_kinetic_residual=zdot_kinetic_residual,
    )
