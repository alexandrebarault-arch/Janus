"""Exact-quadratic g-flat scalar action with one pressureless sector per metric."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives
from numerics.de_felice_dust_phase_action import dust_phase_density
from numerics.de_felice_gravity_action import eh_scalar_quadratic_density_flat
from numerics.de_felice_two_matter_action import _cosmic_background
from numerics.hr_scalar_potential import hr_scalar_quadratic_action_density_de_felice


DUST_DYNAMIC_ORDER = ("psi_f", "E_f", "q_g", "q_f")
DUST_RATE_ORDER = ("psi_f_dot", "E_f_dot", "q_g_dot", "q_f_dot")
DUST_AUXILIARY_ORDER = ("Phi_g", "Phi_f", "B_g", "B_f", "p_g", "p_f")


@dataclass(frozen=True)
class DustFlatGaugeReducedAction:
    augmented_hessian: np.ndarray
    reduced_hessian: np.ndarray
    metric_auxiliary_hessian: np.ndarray
    metric_auxiliary_rank: int
    metric_auxiliary_condition_number: float
    metric_reconstruction_matrix: np.ndarray


def _as_vector(values, size: int, name: str) -> np.ndarray:
    arr = np.asarray(values, dtype=float)
    if arr.shape != (size,):
        raise ValueError(f"{name} must have length {size}")
    if not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} must be finite")
    return arr


def flat_gauge_two_dust_action_value(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    rho_g: float,
    rho_f: float,
    dynamic,
    rates,
    auxiliaries,
) -> float:
    """Return the common-normalized exact quadratic phase action density."""
    q = _as_vector(dynamic, 4, "dynamic")
    v = _as_vector(rates, 4, "rates")
    aux = _as_vector(auxiliaries, 6, "auxiliaries")
    vals = (rho_g, rho_f)
    if not all(math.isfinite(x) and x > 0.0 for x in vals):
        raise ValueError("dust densities must be finite and positive")

    p = _cosmic_background(bg, bgp)
    psi_f, E_f, q_g, q_f = q
    psi_f_dot, E_f_dot, q_g_dot, q_f_dot = v
    Phi_g, Phi_f, B_g, B_f, p_g, p_f = aux
    psi_g = E_g = psi_g_dot = E_g_dot = 0.0
    k = math.sqrt(bg.k2)
    a = p["a"]
    alpha = p["alpha"]
    xi = bg.xi
    n = p["n"]

    L_eh_g = 0.5 * eh_scalar_quadratic_density_flat(
        lapse=1.0, scale_factor=a, H=p["Hg"],
        Hdot_over_lapse=p["Hg_dot_over_N"], k=k,
        Phi=Phi_g, B=B_g, psi=psi_g, E=E_g,
        psi_dot=psi_g_dot, E_dot=E_g_dot,
    )
    L_eh_f = 0.5 * bg.kappa * n * xi**3 * eh_scalar_quadratic_density_flat(
        lapse=n, scale_factor=alpha, H=p["Hf"],
        Hdot_over_lapse=p["Hf_dot_over_n"], k=k,
        Phi=Phi_f, B=B_f, psi=psi_f, E=E_f,
        psi_dot=psi_f_dot, E_dot=E_f_dot,
    )

    L_m_g = (
        p_g * q_g_dot
        + dust_phase_density(
            rho=rho_g, lapse=1.0, scale_factor=a, k=k,
            Phi=Phi_g, B=B_g, psi=psi_g, E=E_g,
            q=q_g, momentum=p_g,
        )
    )

    f_prefactor = n * xi**3
    p_f_local = p_f / f_prefactor
    L_m_f = (
        p_f * q_f_dot
        + p_f * p["n_dot_over_n"] * q_f
        + f_prefactor * dust_phase_density(
            rho=rho_f, lapse=n, scale_factor=alpha, k=k,
            Phi=Phi_f, B=B_f, psi=psi_f, E=E_f,
            q=q_f, momentum=p_f_local,
        )
    )

    potential = hr_scalar_quadratic_action_density_de_felice(
        N=1.0, a=a, n=n, alpha=alpha,
        m2=bg.m2, Mg2=1.0, betas=betas, k=k,
        Phi_g=Phi_g, B_g=B_g, psi_g=psi_g, E_g=E_g,
        Phi_f=Phi_f, B_f=B_f, psi_f=psi_f, E_f=E_f,
    ) / a**3

    return float(L_eh_g + L_eh_f + L_m_g + L_m_f + potential)


def flat_gauge_two_dust_hessian(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    rho_g: float,
    rho_f: float,
) -> np.ndarray:
    """Return the 14x14 Hessian by exact quadratic polarization."""
    nvar = 14
    eye = np.eye(nvar, dtype=float)

    def L(z: np.ndarray) -> float:
        return flat_gauge_two_dust_action_value(
            bg, bgp, betas=betas, rho_g=rho_g, rho_f=rho_f,
            dynamic=z[:4], rates=z[4:8], auxiliaries=z[8:14],
        )

    # The action is exactly quadratic, but its coefficients span many powers
    # of k (up to k^6 in the scalar metric sector). Unit-vector polarization
    # subtracts O(k^6) diagonal pieces to recover much smaller mixed terms and
    # loses precision at the early/high-k benchmark. Rescale every coordinate
    # from its diagonal curvature before polarizing. This changes only the
    # numerical conditioning, not the quadratic form.
    diagonal = np.array([2.0 * L(eye[i]) for i in range(nvar)], dtype=float)
    scales = 1.0 / np.sqrt(np.maximum(np.abs(diagonal), 1.0))

    H = np.zeros((nvar, nvar), dtype=float)
    H[np.diag_indices(nvar)] = diagonal
    for i in range(nvar):
        ui = scales[i] * eye[i]
        for j in range(i + 1, nvar):
            uj = scales[j] * eye[j]
            value = (
                L(ui + uj) - L(ui - uj)
                - L(-ui + uj) + L(-ui - uj)
            ) / (4.0 * scales[i] * scales[j])
            H[i, j] = H[j, i] = value
    return 0.5 * (H + H.T)


def eliminate_flat_gauge_two_dust(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    rho_g: float,
    rho_f: float,
) -> DustFlatGaugeReducedAction:
    """Eliminate only metric lapses/shifts; retain dust canonical momenta.

    Reduced order is ``(4 states, 4 rates, p_g, p_f)``. In the exact dust
    limit the two phase momenta are canonical variables because the action
    contains ``p_g q_g_dot + p_f q_f_dot``. They must not be treated as
    ordinary Schur auxiliaries.
    """
    H = flat_gauge_two_dust_hessian(
        bg, bgp, betas=betas, rho_g=rho_g, rho_f=rho_f,
    )
    metric_idx = list(range(8, 12))
    keep = list(range(8)) + [12, 13]

    Hmm = H[np.ix_(metric_idx, metric_idx)]
    Hmk = H[np.ix_(metric_idx, keep)]
    Hkk = H[np.ix_(keep, keep)]
    rank_m = int(np.linalg.matrix_rank(Hmm))
    cond_m = float(np.linalg.cond(Hmm))
    if rank_m != 4 or not math.isfinite(cond_m):
        raise np.linalg.LinAlgError(
            f"metric auxiliary block invalid: rank={rank_m}, cond={cond_m}"
        )

    solve = np.linalg.solve(Hmm, Hmk)
    metric_map = -solve
    reduced = Hkk - Hmk.T @ solve
    reduced = 0.5 * (reduced + reduced.T)

    return DustFlatGaugeReducedAction(
        augmented_hessian=np.asarray(H, dtype=float),
        reduced_hessian=np.asarray(reduced, dtype=float),
        metric_auxiliary_hessian=np.asarray(Hmm, dtype=float),
        metric_auxiliary_rank=rank_m,
        metric_auxiliary_condition_number=cond_m,
        metric_reconstruction_matrix=np.asarray(metric_map, dtype=float),
    )
