"""Numerically stable two-matter Hessian using the exact O(delta^2) HR action.

The baseline two-matter module historically evaluates an exact nonlinear HR
potential and then finite-differences it to recover a quadratic Hessian.  That
is adequate for many frozen-coefficient checks but becomes noisy when the
resulting Hessian is differentiated again along a background trajectory.

This backend changes no physical coefficient.  It keeps the same EH and P(X)
blocks and the same auxiliary Schur complement, but evaluates the interaction
with ``hr_scalar_quadratic_action_density_de_felice``, the direct
De Felice Eqs. (45)-(46) O(delta^2) expression already audited in the repo.
"""

from __future__ import annotations

import math
import numpy as np

from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives
from numerics.de_felice_gravity_action import eh_scalar_quadratic_density_flat
from numerics.de_felice_matter_action import kessence_scalar_quadratic_density
from numerics.hr_scalar_potential import hr_scalar_quadratic_action_density_de_felice
from numerics.de_felice_two_matter_action import (
    DFKessenceFluid,
    FlatGaugeReducedAction,
    _cosmic_background,
    matter_log_phidot_rates,
)


def _as4(values, name: str) -> np.ndarray:
    arr = np.asarray(values, dtype=float)
    if arr.shape != (4,):
        raise ValueError(f"{name} must have length 4")
    return arr


def flat_gauge_action_value_exact_quadratic(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    g_fluid: DFKessenceFluid,
    f_fluid: DFKessenceFluid,
    dynamic,
    rates,
    auxiliaries,
) -> float:
    """Return the already-quadratic g-flat action density."""
    q = _as4(dynamic, "dynamic")
    v = _as4(rates, "rates")
    aux = _as4(auxiliaries, "auxiliaries")
    p = _cosmic_background(bg, bgp)

    psi_f, E_f, q_g, q_f = q
    psi_f_dot, E_f_dot, q_g_dot, q_f_dot = v
    Phi_g, Phi_f, B_g, B_f = aux
    psi_g = E_g = psi_g_dot = E_g_dot = 0.0

    k = math.sqrt(bg.k2)
    a = p["a"]
    alpha = p["alpha"]
    xi = bg.xi
    n = p["n"]
    rg, rf = matter_log_phidot_rates(
        bg, bgp, g_fluid=g_fluid, f_fluid=f_fluid,
    )
    delta_phidot_ratio_g = q_g_dot + rg * q_g
    delta_phidot_ratio_f = q_f_dot + rf * q_f

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

    L_m_g = kessence_scalar_quadratic_density(
        rho=g_fluid.rho, pressure=g_fluid.pressure, cs2=g_fluid.cs2,
        lapse=1.0, scale_factor=a, k=k,
        Phi=Phi_g, B=B_g, psi=psi_g, E=E_g,
        delta_phi_over_phidot=q_g,
        delta_phidot_over_phidot=delta_phidot_ratio_g,
    )
    L_m_f = n * xi**3 * kessence_scalar_quadratic_density(
        rho=f_fluid.rho, pressure=f_fluid.pressure, cs2=f_fluid.cs2,
        lapse=n, scale_factor=alpha, k=k,
        Phi=Phi_f, B=B_f, psi=psi_f, E=E_f,
        delta_phi_over_phidot=q_f,
        delta_phidot_over_phidot=delta_phidot_ratio_f,
    )

    potential = hr_scalar_quadratic_action_density_de_felice(
        N=1.0, a=a, n=n, alpha=alpha,
        m2=bg.m2, Mg2=1.0, betas=betas, k=k,
        Phi_g=Phi_g, B_g=B_g, psi_g=psi_g, E_g=E_g,
        Phi_f=Phi_f, B_f=B_f, psi_f=psi_f, E_f=E_f,
    ) / a**3

    return float(L_eh_g + L_eh_f + L_m_g + L_m_f + potential)


def flat_gauge_quadratic_hessian_exact_quadratic(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    g_fluid: DFKessenceFluid,
    f_fluid: DFKessenceFluid,
    finite_difference_step: float = 5.0e-5,
) -> np.ndarray:
    """Finite-difference a function that is itself exactly quadratic."""
    h = float(finite_difference_step)
    if not (h > 0.0 and math.isfinite(h)):
        raise ValueError("finite_difference_step must be finite and positive")

    nvar = 12
    zero = np.zeros(nvar, dtype=float)
    eye = np.eye(nvar, dtype=float) * h

    def L(x):
        x = np.asarray(x, dtype=float)
        return flat_gauge_action_value_exact_quadratic(
            bg, bgp, betas=betas,
            g_fluid=g_fluid, f_fluid=f_fluid,
            dynamic=x[:4], rates=x[4:8], auxiliaries=x[8:12],
        )

    base = L(zero)
    H = np.empty((nvar, nvar), dtype=float)
    hh = h * h
    for i in range(nvar):
        H[i, i] = (L(eye[i]) - 2.0 * base + L(-eye[i])) / hh
        for j in range(i + 1, nvar):
            H[i, j] = H[j, i] = (
                L(eye[i] + eye[j])
                - L(eye[i] - eye[j])
                - L(-eye[i] + eye[j])
                + L(-eye[i] - eye[j])
            ) / (4.0 * hh)
    return H


def eliminate_flat_gauge_auxiliaries_exact_quadratic(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    g_fluid: DFKessenceFluid,
    f_fluid: DFKessenceFluid,
    finite_difference_step: float = 5.0e-5,
) -> FlatGaugeReducedAction:
    """Apply the same 4-auxiliary Schur complement as the baseline reducer."""
    Q = flat_gauge_quadratic_hessian_exact_quadratic(
        bg, bgp, betas=betas,
        g_fluid=g_fluid, f_fluid=f_fluid,
        finite_difference_step=finite_difference_step,
    )
    Qzz = Q[:8, :8]
    Qza = Q[:8, 8:12]
    Qaa = Q[8:12, 8:12]
    rank = int(np.linalg.matrix_rank(Qaa))
    if rank != 4:
        raise np.linalg.LinAlgError(f"auxiliary Hessian rank {rank}, expected 4")

    reduced = Qzz - Qza @ np.linalg.solve(Qaa, Qza.T)
    reduced = 0.5 * (reduced + reduced.T)
    kinetic = 0.5 * (reduced[4:8, 4:8] + reduced[4:8, 4:8].T)
    return FlatGaugeReducedAction(
        reduced_hessian=np.asarray(reduced, dtype=float),
        kinetic_hessian=np.asarray(kinetic, dtype=float),
        auxiliary_hessian=np.asarray(Qaa, dtype=float),
        auxiliary_rank=rank,
        auxiliary_condition_number=float(np.linalg.cond(Qaa)),
    )
