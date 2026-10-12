"""Coupled Lagos scalar metric action plus two separately coupled P(X) sectors.

This is the Gate-2B action-level bridge between the independently reconstructed
Lagos-Ferreira pure-metric scalar action and the independent De Felice P(X)
matter action. It does not import the failed Comelli scalar closure.

A crucial convention point is that Lagos' metric block has already used the
background equations and therefore already contains the metric-only matter
terms. Lagos & Ferreira explicitly separate ``S_phi^(2)`` as the terms that
contain the matter perturbation, while ``S_T1^(2)`` contains the quadratic
metric terms inherited from the matter action. Adding the complete De Felice
Eq. (54) on top of that block double-counts those terms and destroys the
expected scalar kinetic degeneracy.

The compatible assembly used here is therefore:

1. convert Lagos scalar metric variables to the De Felice decomposition;
2. add only the part of De Felice Eq. (54) that depends on ``delta_phi``;
3. add the residual background lapse susceptibility
   ``(rho+P) Phi^2 / (2 c_s^2)`` in each sector's own volume measure.

For ``c_s^2=1`` the last term reduces to the explicit canonical-scalar
correction in Lagos & Ferreira Eq. (3.6). The general P(X) form follows by
adding the only c_s-dependent pure-metric difference in De Felice Eq. (54).

All returned Lagrangians use the common pure-metric normalization ``M1^2 a^3``.
With ``M1^-2 = 8 pi G``, a sector remainder in its physical background volume
is multiplied by ``8 pi G / a^3`` before being added to the metric block.
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
    *,
    matter: KessenceBackground,
    lapse: float,
    scale_factor: float,
    k: float,
    Phi: float,
    B: float,
    psi: float,
    E: float,
    u: float,
    u_dot: float,
) -> float:
    """Return the matter remainder compatible with the Lagos metric block.

    ``psi``, ``E`` and ``B`` on entry are Lagos variables. In flat Fourier
    space their relation to the De Felice scalar decomposition is

        B_DF   = B_L / a,
        psi_DF = -Psi_L - k^2 E_L/3,
        E_DF   = 2 E_L,
        Phi_DF = Phi_L.

    The spatial mapping follows directly by equating

        a^2[(1-2 Psi_L) delta_ij + 2 d_i d_j E_L]

    to ``a^2(delta_ij + H_ij)`` with De Felice's trace/traceless split. The
    shift mapping follows from equating the ``dt dx^i`` terms.

    We subtract the ``u=u_dot=0`` De Felice action because those metric-only
    matter terms are already present in the background-reduced Lagos metric
    block. The residual lapse susceptibility is then restored explicitly.
    """
    common = dict(
        rho=matter.rho,
        pressure=matter.pressure,
        cs2=matter.cs2,
        lapse=lapse,
        scale_factor=scale_factor,
        k=k,
        Phi=Phi,
        B=B / scale_factor,
        psi=-psi - (k * k / 3.0) * E,
        E=2.0 * E,
    )
    full = kessence_scalar_quadratic_lagrangian(
        **common,
        field_ratio=u,
        field_velocity_ratio=u_dot,
    )
    metric_only = kessence_scalar_quadratic_lagrangian(
        **common,
        field_ratio=0.0,
        field_velocity_ratio=0.0,
    )
    background_lapse = (
        lapse
        * scale_factor**3
        * 0.5
        * (matter.rho + matter.pressure)
        / matter.cs2
        * Phi**2
    )
    return float(full - metric_only + background_lapse)


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


def reduced_two_matter_velocity_hessian(
    bg,
    matter_g: KessenceBackground,
    matter_f: KessenceBackground,
) -> np.ndarray:
    """Velocity Hessian of the six-field action after auxiliary elimination."""
    q = np.zeros(6, dtype=float)
    zero = np.zeros(6, dtype=float)
    base = reduced_two_matter_lagrangian(bg, matter_g, matter_f, q, zero)
    eye = np.eye(6)
    Hmat = np.empty((6, 6), dtype=float)

    for i in range(6):
        lp = reduced_two_matter_lagrangian(
            bg, matter_g, matter_f, q, eye[i]
        )
        lm = reduced_two_matter_lagrangian(
            bg, matter_g, matter_f, q, -eye[i]
        )
        Hmat[i, i] = lp + lm - 2.0 * base
        for j in range(i + 1, 6):
            lpp = reduced_two_matter_lagrangian(
                bg, matter_g, matter_f, q, eye[i] + eye[j]
            )
            lpm = reduced_two_matter_lagrangian(
                bg, matter_g, matter_f, q, eye[i] - eye[j]
            )
            lmp = reduced_two_matter_lagrangian(
                bg, matter_g, matter_f, q, -eye[i] + eye[j]
            )
            lmm = reduced_two_matter_lagrangian(
                bg, matter_g, matter_f, q, -eye[i] - eye[j]
            )
            Hmat[i, j] = Hmat[j, i] = 0.25 * (
                lpp - lpm - lmp + lmm
            )
    return Hmat
