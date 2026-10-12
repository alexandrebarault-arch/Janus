"""Combined scalar quadratic action for Hassan-Rosen bigravity + two P(X) fluids.

This module is the action-level Gate-2B replacement for the historical Comelli
12x12 closure. The pure metric action is supplied by ``lagos_scalar_action``;
the two matter sectors use De Felice et al. Eq. (54), each minimally coupled to
its own metric. Lapses and shifts are eliminated algebraically from the total
quadratic action. Their constraint equations are never differentiated.

All Lagrangians returned here use the same common normalization as
``pure_metric_lagrangian_healthy``: the full action divided by ``M_g^2 a^3``.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground
from numerics.de_felice_matter_action import kessence_lagos_sector_common_normalized_lagrangian
from numerics.lagos_action_bridge import lagos_bigravity_parameters
from numerics.lagos_scalar_action import pure_metric_lagrangian_healthy


DYNAMIC_ORDER = ("Psi1", "Psi2", "E1", "E2", "q_g", "q_f")
RATE_ORDER = ("Psi1_dot", "Psi2_dot", "E1_dot", "E2_dot", "q_g_dot", "q_f_dot")
AUXILIARY_ORDER = ("Phi1", "Phi2", "B1", "B2")
FLAT_GAUGE_ORDER = ("Psi2", "E2", "q_g", "q_f")


@dataclass(frozen=True)
class KessenceFluid:
    rho: float
    pressure: float
    cs2: float

    def __post_init__(self):
        if not all(math.isfinite(v) for v in (self.rho, self.pressure, self.cs2)):
            raise ValueError("fluid parameters must be finite")
        if self.cs2 <= 0.0:
            raise ValueError("cs2 must be positive before the reduced dust limit")


@dataclass(frozen=True)
class CombinedAuxiliarySolution:
    auxiliaries: np.ndarray
    auxiliary_hessian_rank: int
    stationarity_residual: float
    reduced_lagrangian: float


def _dynamic(x) -> np.ndarray:
    arr = np.asarray(x, dtype=float)
    if arr.shape != (6,):
        raise ValueError("combined dynamic vector must have length 6")
    return arr


def _rates(v) -> np.ndarray:
    arr = np.asarray(v, dtype=float)
    if arr.shape != (6,):
        raise ValueError("combined rate vector must have length 6")
    return arr


def _auxiliary(a) -> np.ndarray:
    arr = np.asarray(a, dtype=float)
    if arr.shape != (4,):
        raise ValueError("combined auxiliary vector must have length 4")
    return arr


def _metric_state(dynamic, auxiliary) -> np.ndarray:
    q = _dynamic(dynamic)
    aux = _auxiliary(auxiliary)
    return np.array([q[0], q[1], q[2], q[3], aux[0], aux[1], aux[2], aux[3]], dtype=float)


def combined_scalar_lagrangian(
    bg: ScalarBackground, dynamic, rates, auxiliaries, *,
    g_fluid: KessenceFluid, f_fluid: KessenceFluid, M_g2: float = 1.0,
) -> float:
    """Return the metric + two-matter scalar quadratic Lagrangian."""
    q = _dynamic(dynamic)
    v = _rates(rates)
    aux = _auxiliary(auxiliaries)
    if not (math.isfinite(M_g2) and M_g2 > 0.0):
        raise ValueError("M_g2 must be finite and positive")
    if bg.k2 < 0.0:
        raise ValueError("k2 must be non-negative")

    metric_state = _metric_state(q, aux)
    metric_part = pure_metric_lagrangian_healthy(bg, metric_state, v[:4])

    p = lagos_bigravity_parameters(bg)
    r, nbar = p.r, p.Nbar
    a = bg.a
    b = a * r
    k = math.sqrt(bg.k2)
    Phi1, Phi2, B1, B2 = aux
    Psi1, Psi2, E1, E2, qg, qf = q
    qg_dot, qf_dot = v[4], v[5]

    g_part = kessence_lagos_sector_common_normalized_lagrangian(
        reference_scale_factor=a, M_g2=M_g2,
        rho=g_fluid.rho, pressure=g_fluid.pressure, cs2=g_fluid.cs2,
        lapse=1.0, scale_factor=a, k=k,
        Phi_lagos=Phi1, B_lagos=B1, Psi_lagos=Psi1, E_lagos=E1,
        delta_phi_over_phidot=qg, delta_phidot_over_phidot=qg_dot,
    )
    f_part = kessence_lagos_sector_common_normalized_lagrangian(
        reference_scale_factor=a, M_g2=M_g2,
        rho=f_fluid.rho, pressure=f_fluid.pressure, cs2=f_fluid.cs2,
        lapse=nbar, scale_factor=b, k=k,
        Phi_lagos=Phi2, B_lagos=B2, Psi_lagos=Psi2, E_lagos=E2,
        delta_phi_over_phidot=qf, delta_phidot_over_phidot=qf_dot,
    )
    return float(metric_part + g_part + f_part)


def _auxiliary_quadratic_form(
    bg: ScalarBackground, dynamic, rates, *,
    g_fluid: KessenceFluid, f_fluid: KessenceFluid, M_g2: float,
):
    q = _dynamic(dynamic)
    v = _rates(rates)
    n = len(AUXILIARY_ORDER)
    z = np.zeros(n, dtype=float)
    eye = np.eye(n)

    def L(aux):
        return combined_scalar_lagrangian(
            bg, q, v, aux, g_fluid=g_fluid, f_fluid=f_fluid, M_g2=M_g2
        )

    base = L(z)
    grad = np.empty(n, dtype=float)
    A = np.empty((n, n), dtype=float)
    for i in range(n):
        lp = L(eye[i])
        lm = L(-eye[i])
        grad[i] = 0.5 * (lp - lm)
        A[i, i] = lp + lm - 2.0 * base
        for j in range(i + 1, n):
            lpp = L(eye[i] + eye[j])
            lpm = L(eye[i] - eye[j])
            lmp = L(-eye[i] + eye[j])
            lmm = L(-eye[i] - eye[j])
            A[i, j] = A[j, i] = 0.25 * (lpp - lpm - lmp + lmm)
    return A, grad, float(base)


def eliminate_combined_auxiliaries(
    bg: ScalarBackground, dynamic, rates, *,
    g_fluid: KessenceFluid, f_fluid: KessenceFluid, M_g2: float = 1.0,
) -> CombinedAuxiliarySolution:
    """Integrate out ``Phi1,Phi2,B1,B2`` by algebraic stationarity."""
    A, grad, base = _auxiliary_quadratic_form(
        bg, dynamic, rates, g_fluid=g_fluid, f_fluid=f_fluid, M_g2=M_g2
    )
    rank = int(np.linalg.matrix_rank(A))
    if rank != len(AUXILIARY_ORDER):
        raise np.linalg.LinAlgError(
            f"combined auxiliary Hessian rank {rank}, expected {len(AUXILIARY_ORDER)}"
        )
    aux = np.linalg.solve(A, -grad)
    residual = float(np.linalg.norm(A @ aux + grad, ord=np.inf))
    reduced = float(base + grad @ aux + 0.5 * aux @ A @ aux)
    return CombinedAuxiliarySolution(
        auxiliaries=np.asarray(aux, dtype=float),
        auxiliary_hessian_rank=rank,
        stationarity_residual=residual,
        reduced_lagrangian=reduced,
    )


def reduced_combined_lagrangian(
    bg: ScalarBackground, dynamic, rates, *,
    g_fluid: KessenceFluid, f_fluid: KessenceFluid, M_g2: float = 1.0,
) -> float:
    return eliminate_combined_auxiliaries(
        bg, dynamic, rates, g_fluid=g_fluid, f_fluid=f_fluid, M_g2=M_g2
    ).reduced_lagrangian


def _quadratic_velocity_hessian(lagrangian, n: int) -> np.ndarray:
    z = np.zeros(n, dtype=float)
    base = lagrangian(z)
    eye = np.eye(n)
    Hmat = np.empty((n, n), dtype=float)
    for i in range(n):
        lp = lagrangian(eye[i])
        lm = lagrangian(-eye[i])
        Hmat[i, i] = lp + lm - 2.0 * base
        for j in range(i + 1, n):
            lpp = lagrangian(eye[i] + eye[j])
            lpm = lagrangian(eye[i] - eye[j])
            lmp = lagrangian(-eye[i] + eye[j])
            lmm = lagrangian(-eye[i] - eye[j])
            Hmat[i, j] = Hmat[j, i] = 0.25 * (lpp - lpm - lmp + lmm)
    return Hmat


def reduced_combined_velocity_hessian(
    bg: ScalarBackground, *, g_fluid: KessenceFluid,
    f_fluid: KessenceFluid, M_g2: float = 1.0,
) -> np.ndarray:
    """Return the ungauged 6x6 velocity Hessian after lapse/shift elimination.

    This object still contains two scalar gauge directions and must not be used
    directly as a physical degree-count diagnostic.
    """
    q = np.zeros(6, dtype=float)
    return _quadratic_velocity_hessian(
        lambda v: reduced_combined_lagrangian(
            bg, q, v, g_fluid=g_fluid, f_fluid=f_fluid, M_g2=M_g2
        ),
        6,
    )


def _flat_gauge_embed(values) -> np.ndarray:
    """Embed ``(Psi2,E2,q_g,q_f)`` into g-flat gauge ``Psi1=E1=0``."""
    x = np.asarray(values, dtype=float)
    if x.shape != (4,):
        raise ValueError("flat-gauge vector must have length 4")
    return np.array([0.0, x[0], 0.0, x[1], x[2], x[3]], dtype=float)


def reduced_flat_gauge_lagrangian(
    bg: ScalarBackground, dynamic, rates, *,
    g_fluid: KessenceFluid, f_fluid: KessenceFluid, M_g2: float = 1.0,
) -> float:
    """Reduced action after De Felice's g-flat gauge ``E_g=psi_g=0``.

    In current Lagos variables this is exactly ``E1=Psi1=0``. The remaining
    coordinate order is ``(Psi2,E2,q_g,q_f)``. One further non-dynamical
    would-be BD combination is expected before the final three-field action.
    """
    return reduced_combined_lagrangian(
        bg, _flat_gauge_embed(dynamic), _flat_gauge_embed(rates),
        g_fluid=g_fluid, f_fluid=f_fluid, M_g2=M_g2,
    )


def reduced_flat_gauge_velocity_hessian(
    bg: ScalarBackground, *, g_fluid: KessenceFluid,
    f_fluid: KessenceFluid, M_g2: float = 1.0,
) -> np.ndarray:
    """Return the 4x4 kinetic Hessian after g-flat gauge fixing."""
    q = np.zeros(4, dtype=float)
    return _quadratic_velocity_hessian(
        lambda v: reduced_flat_gauge_lagrangian(
            bg, q, v, g_fluid=g_fluid, f_fluid=f_fluid, M_g2=M_g2
        ),
        4,
    )
