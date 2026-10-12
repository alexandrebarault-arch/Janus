"""Coupled Lagos scalar metric action plus two separately coupled P(X) sectors.

This is the Gate-2B action-level bridge between the independently reconstructed
Lagos-Ferreira pure-metric scalar action and the independent De Felice P(X)
matter action.  It does not import the failed Comelli scalar closure.

The common normalization is ``M1^2 a^3``.  With ``M1^-2 = 8 pi G`` the raw
matter actions therefore enter as

    (8 pi G / a^3) * [L_g + L_f],

where ``L_g`` already contains the g-sector background volume ``a^3`` and
``L_f`` contains ``Nbar b^3`` with ``b=a*r`` and ``Nbar=r*c``.

State order extends the pure-metric order by the two normalized matter-field
perturbations ``u = delta_phi / phi_dot_0``.  Rate order extends the pure-metric
rate order by ``delta_phi_dot / phi_dot_0`` for each sector.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np

from numerics.de_felice_matter_action import (
    kessence_scalar_quadratic_lagrangian,
)
from numerics.lagos_action_bridge import lagos_bigravity_parameters
from numerics.lagos_scalar_action import pure_metric_lagrangian_healthy


TWO_MATTER_STATE_ORDER = (
    "Psi1", "Psi2", "E1", "E2",
    "Phi1", "Phi2", "B1", "B2",
    "u_g", "u_f",
)
TWO_MATTER_RATE_ORDER = (
    "Psi1_dot", "Psi2_dot", "E1_dot", "E2_dot",
    "u_g_dot", "u_f_dot",
)
TWO_MATTER_DYNAMIC_ORDER = (
    "Psi1", "Psi2", "E1", "E2", "u_g", "u_f",
)
TWO_MATTER_AUXILIARY_ORDER = ("Phi1", "Phi2", "B1", "B2")


@dataclass(frozen=True)
class KessenceBackground:
    rho: float
    pressure: float
    cs2: float


@dataclass(frozen=True)
class TwoMatterAuxiliarySolution:
    auxiliaries: np.ndarray
    auxiliary_hessian_rank: int
    stationarity_residual: float
    reduced_lagrangian: float


def _matter_sector_lagrangian(
    *, matter: KessenceBackground, lapse: float, scale_factor: float,
    k: float, Phi: float, B: float, psi: float, E: float,
    u: float, u_dot: float,
) -> float:
    return kessence_scalar_quadratic_lagrangian(
        rho=matter.rho,
        pressure=matter.pressure,
        cs2=matter.cs2,
        lapse=lapse,
        scale_factor=scale_factor,
        k=k,
        Phi=Phi,
        B=B,
        psi=psi,
        E=E,
        field_ratio=u,
        field_velocity_ratio=u_dot,
    )


def two_matter_lagrangian_healthy(
    bg,
    matter_g: KessenceBackground,
    matter_f: KessenceBackground,
    state,
    rates,
) -> float:
    """Return metric + g matter + f matter in common ``M1^2 a^3`` units."""
    x = np.asarray(state, dtype=float)
    v = np.asarray(rates, dtype=float)
    if x.shape != (10,) or v.shape != (6,):
        raise ValueError("two-matter state/rates must have lengths 10/6")
    if bg.a <= 0.0 or bg.k2 < 0.0:
        raise ValueError("a must be positive and k2 non-negative")

    metric = pure_metric_lagrangian_healthy(bg, x[:8], v[:4])
    params = lagos_bigravity_parameters(bg)
    k = math.sqrt(bg.k2)
    b = bg.a * params.r
    if params.Nbar <= 0.0 or b <= 0.0:
        raise ValueError("f-sector lapse and scale factor must be positive")

    Lg = _matter_sector_lagrangian(
        matter=matter_g,
        lapse=1.0,
        scale_factor=bg.a,
        k=k,
        Phi=x[4],
        B=x[6],
        psi=x[0],
        E=x[2],
        u=x[8],
        u_dot=v[4],
    )
    Lf = _matter_sector_lagrangian(
        matter=matter_f,
        lapse=params.Nbar,
        scale_factor=b,
        k=k,
        Phi=x[5],
        B=x[7],
        psi=x[1],
        E=x[3],
        u=x[9],
        u_dot=v[5],
    )

    matter_normalized = bg.G8pi * (Lg + Lf) / bg.a**3
    return float(metric + matter_normalized)


def _state_from_dynamic_aux(dynamic, auxiliaries) -> np.ndarray:
    q = np.asarray(dynamic, dtype=float)
    aux = np.asarray(auxiliaries, dtype=float)
    if q.shape != (6,) or aux.shape != (4,):
        raise ValueError("dynamic and auxiliary vectors must have lengths 6/4")
    return np.array(
        [
            q[0], q[1], q[2], q[3],
            aux[0], aux[1], aux[2], aux[3],
            q[4], q[5],
        ],
        dtype=float,
    )


def _two_matter_auxiliary_quadratic_form(
    bg,
    matter_g: KessenceBackground,
    matter_f: KessenceBackground,
    dynamic,
    rates,
):
    """Return auxiliary Hessian A, linear term g and L(aux=0)."""
    q = np.asarray(dynamic, dtype=float)
    v = np.asarray(rates, dtype=float)
    if q.shape != (6,) or v.shape != (6,):
        raise ValueError("dynamic and rate vectors must have length 6")

    zero = np.zeros(4, dtype=float)
    base = two_matter_lagrangian_healthy(
        bg, matter_g, matter_f, _state_from_dynamic_aux(q, zero), v
    )
    eye = np.eye(4)
    grad = np.empty(4, dtype=float)
    A = np.empty((4, 4), dtype=float)

    for i in range(4):
        lp = two_matter_lagrangian_healthy(
            bg, matter_g, matter_f,
            _state_from_dynamic_aux(q, eye[i]), v,
        )
        lm = two_matter_lagrangian_healthy(
            bg, matter_g, matter_f,
            _state_from_dynamic_aux(q, -eye[i]), v,
        )
        grad[i] = 0.5 * (lp - lm)
        A[i, i] = lp + lm - 2.0 * base

        for j in range(i + 1, 4):
            lpp = two_matter_lagrangian_healthy(
                bg, matter_g, matter_f,
                _state_from_dynamic_aux(q, eye[i] + eye[j]), v,
            )
            lpm = two_matter_lagrangian_healthy(
                bg, matter_g, matter_f,
                _state_from_dynamic_aux(q, eye[i] - eye[j]), v,
            )
            lmp = two_matter_lagrangian_healthy(
                bg, matter_g, matter_f,
                _state_from_dynamic_aux(q, -eye[i] + eye[j]), v,
            )
            lmm = two_matter_lagrangian_healthy(
                bg, matter_g, matter_f,
                _state_from_dynamic_aux(q, -eye[i] - eye[j]), v,
            )
            A[i, j] = A[j, i] = 0.25 * (lpp - lpm - lmp + lmm)

    return A, grad, float(base)


def eliminate_two_matter_auxiliaries(
    bg,
    matter_g: KessenceBackground,
    matter_f: KessenceBackground,
    dynamic,
    rates,
) -> TwoMatterAuxiliarySolution:
    """Integrate out ``Phi1,Phi2,B1,B2`` by algebraic stationarity."""
    A, grad, base = _two_matter_auxiliary_quadratic_form(
        bg, matter_g, matter_f, dynamic, rates
    )
    rank = int(np.linalg.matrix_rank(A))
    if rank != 4:
        raise np.linalg.LinAlgError(
            f"combined auxiliary Hessian rank {rank}, expected 4"
        )
    aux = np.linalg.solve(A, -grad)
    residual = float(np.linalg.norm(A @ aux + grad, ord=np.inf))
    reduced = float(base + grad @ aux + 0.5 * aux @ A @ aux)
    return TwoMatterAuxiliarySolution(
        auxiliaries=np.asarray(aux, dtype=float),
        auxiliary_hessian_rank=rank,
        stationarity_residual=residual,
        reduced_lagrangian=reduced,
    )


def reduced_two_matter_lagrangian(
    bg,
    matter_g: KessenceBackground,
    matter_f: KessenceBackground,
    dynamic,
    rates,
) -> float:
    return eliminate_two_matter_auxiliaries(
        bg, matter_g, matter_f, dynamic, rates
    ).reduced_lagrangian
