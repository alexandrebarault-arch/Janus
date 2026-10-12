"""Full local scalar quadratic action for ghost-free bigravity with two fluids.

This module combines three pieces without using the one-matter Lagos background
specialization:

1. De Felice et al. Eq. (44) for each Einstein-Hilbert sector;
2. the exact Hassan-Rosen non-derivative potential evaluated directly from
   sqrt(g^-1 f);
3. one De Felice Eq. (54) P(X) matter action for each metric.

The first implementation works in De Felice's g-flat gauge, psi_g=E_g=0,
and constructs the local quadratic form numerically around the background.
Lapses and shifts are then eliminated by a Schur complement.  This is an audit
and reduction layer; time-domain evolution is added only after the physical
three-field action is independently validated.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives
from numerics.de_felice_gravity_action import eh_scalar_quadratic_density_flat
from numerics.de_felice_matter_action import kessence_scalar_quadratic_density
from numerics.hr_scalar_potential import hr_scalar_potential_density_de_felice


FLAT_DYNAMIC_ORDER = ("psi_f", "E_f", "q_g", "q_f")
FLAT_RATE_ORDER = ("psi_f_dot", "E_f_dot", "q_g_dot", "q_f_dot")
AUXILIARY_ORDER = ("Phi_g", "Phi_f", "B_g", "B_f")


@dataclass(frozen=True)
class DFKessenceFluid:
    rho: float
    pressure: float
    cs2: float

    def __post_init__(self):
        vals = (self.rho, self.pressure, self.cs2)
        if not all(math.isfinite(v) for v in vals):
            raise ValueError("fluid parameters must be finite")
        if self.cs2 <= 0.0:
            raise ValueError("cs2 must be positive before the reduced dust limit")


@dataclass(frozen=True)
class FlatGaugeReducedAction:
    reduced_hessian: np.ndarray
    kinetic_hessian: np.ndarray
    auxiliary_hessian: np.ndarray
    auxiliary_rank: int
    auxiliary_condition_number: float


def _as4(values, name: str) -> np.ndarray:
    arr = np.asarray(values, dtype=float)
    if arr.shape != (4,):
        raise ValueError(f"{name} must have length 4")
    return arr


def _cosmic_background(
    bg: ScalarBackground, bgp: ScalarBackgroundDerivatives,
) -> dict[str, float]:
    """Convert JANUS conformal-g variables to De Felice g-cosmic time.

    JANUS/Comelli uses
        ds_g^2=a^2(-deta^2+...),
        ds_f^2=(a xi)^2(-c^2 deta^2+...).
    With dt=a deta, De Felice's lapses are N=1 and n=xi*c.
    """
    if bg.a <= 0.0 or bg.xi <= 0.0 or bg.c <= 0.0:
        raise ValueError("a, xi and c must be positive")

    a = bg.a
    xi = bg.xi
    c = bg.c
    alpha = a*xi
    N = 1.0
    n = xi*c

    Hg = bg.H/a
    Hf = bg.H_omega/(a*xi*c)

    # dot means d/dt with g-cosmic time dt=a deta.
    Hg_dot_over_N = (bgp.H_prime - bg.H*bg.H)/(a*a)

    log_den_prime = bg.H + bgp.xi_prime/xi + bgp.c_prime/c
    numerator = bgp.H_omega_prime - bg.H_omega*log_den_prime
    # Hf_eta = numerator/(a xi c), then d/dt=(1/a)d/deta,
    # and Eq. (44) needs Hf_dot/n.
    Hf_dot_over_n = numerator/(a*a*xi*xi*c*c)

    return dict(
        N=N, a=a, n=n, alpha=alpha,
        Hg=Hg, Hf=Hf,
        Hg_dot_over_N=Hg_dot_over_N,
        Hf_dot_over_n=Hf_dot_over_n,
    )


def flat_gauge_action_value(
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
    """Return the common-normalized local action in De Felice g-flat gauge.

    The common normalization is ``M_g^2 a^3`` with ``M_g^2=1``.  The exact
    Hassan-Rosen potential contains background and linear pieces; those are
    harmless because the public quadratic-Hessian builder differentiates this
    function twice around the background.
    """
    q = _as4(dynamic, "dynamic")
    v = _as4(rates, "rates")
    aux = _as4(auxiliaries, "auxiliaries")
    p = _cosmic_background(bg, bgp)

    psi_f, E_f, q_g, q_f = q
    psi_f_dot, E_f_dot, q_g_dot, q_f_dot = v
    Phi_g, Phi_f, B_g, B_f = aux

    psi_g = 0.0
    E_g = 0.0
    psi_g_dot = 0.0
    E_g_dot = 0.0

    k = math.sqrt(bg.k2)
    a = p["a"]
    alpha = p["alpha"]
    xi = bg.xi
    n = p["n"]

    L_eh_g = 0.5 * eh_scalar_quadratic_density_flat(
        lapse=1.0, scale_factor=a,
        H=p["Hg"], Hdot_over_lapse=p["Hg_dot_over_N"], k=k,
        Phi=Phi_g, B=B_g, psi=psi_g, E=E_g,
        psi_dot=psi_g_dot, E_dot=E_g_dot,
    )
    L_eh_f = 0.5 * bg.kappa * n * xi**3 * eh_scalar_quadratic_density_flat(
        lapse=n, scale_factor=alpha,
        H=p["Hf"], Hdot_over_lapse=p["Hf_dot_over_n"], k=k,
        Phi=Phi_f, B=B_f, psi=psi_f, E=E_f,
        psi_dot=psi_f_dot, E_dot=E_f_dot,
    )

    L_m_g = kessence_scalar_quadratic_density(
        rho=g_fluid.rho, pressure=g_fluid.pressure, cs2=g_fluid.cs2,
        lapse=1.0, scale_factor=a, k=k,
        Phi=Phi_g, B=B_g, psi=psi_g, E=E_g,
        delta_phi_over_phidot=q_g, delta_phidot_over_phidot=q_g_dot,
    )
    L_m_f = n * xi**3 * kessence_scalar_quadratic_density(
        rho=f_fluid.rho, pressure=f_fluid.pressure, cs2=f_fluid.cs2,
        lapse=n, scale_factor=alpha, k=k,
        Phi=Phi_f, B=B_f, psi=psi_f, E=E_f,
        delta_phi_over_phidot=q_f, delta_phidot_over_phidot=q_f_dot,
    )

    potential = hr_scalar_potential_density_de_felice(
        N=1.0, a=a, n=n, alpha=alpha,
        m2=bg.m2, Mg2=1.0, betas=betas, k=k,
        Phi_g=Phi_g, B_g=B_g, psi_g=psi_g, E_g=E_g,
        Phi_f=Phi_f, B_f=B_f, psi_f=psi_f, E_f=E_f,
    ) / (a**3)

    return float(L_eh_g + L_eh_f + L_m_g + L_m_f + potential)


def flat_gauge_quadratic_hessian(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    g_fluid: DFKessenceFluid,
    f_fluid: DFKessenceFluid,
    finite_difference_step: float = 5.0e-5,
) -> np.ndarray:
    """Return the 12x12 Hessian in (Y, Ydot, auxiliaries) at the background."""
    h = float(finite_difference_step)
    if not (h > 0.0 and math.isfinite(h)):
        raise ValueError("finite_difference_step must be finite and positive")

    n = 12
    zero = np.zeros(n, dtype=float)
    eye = np.eye(n, dtype=float) * h

    def L(x):
        x = np.asarray(x, dtype=float)
        return flat_gauge_action_value(
            bg, bgp, betas=betas, g_fluid=g_fluid, f_fluid=f_fluid,
            dynamic=x[:4], rates=x[4:8], auxiliaries=x[8:12],
        )

    base = L(zero)
    H = np.empty((n, n), dtype=float)
    hh = h*h
    for i in range(n):
        H[i, i] = (L(eye[i]) - 2.0*base + L(-eye[i])) / hh
        for j in range(i + 1, n):
            H[i, j] = H[j, i] = (
                L(eye[i] + eye[j])
                - L(eye[i] - eye[j])
                - L(-eye[i] + eye[j])
                + L(-eye[i] - eye[j])
            ) / (4.0*hh)
    return H


def eliminate_flat_gauge_auxiliaries(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    g_fluid: DFKessenceFluid,
    f_fluid: DFKessenceFluid,
    finite_difference_step: float = 5.0e-5,
) -> FlatGaugeReducedAction:
    """Eliminate ``Phi_g,Phi_f,B_g,B_f`` by a quadratic Schur complement."""
    Q = flat_gauge_quadratic_hessian(
        bg, bgp, betas=betas, g_fluid=g_fluid, f_fluid=f_fluid,
        finite_difference_step=finite_difference_step,
    )
    Qzz = Q[:8, :8]
    Qza = Q[:8, 8:12]
    Qaa = Q[8:12, 8:12]
    rank = int(np.linalg.matrix_rank(Qaa))
    if rank != 4:
        raise np.linalg.LinAlgError(f"auxiliary Hessian rank {rank}, expected 4")

    reduced = Qzz - Qza @ np.linalg.solve(Qaa, Qza.T)
    reduced = 0.5*(reduced + reduced.T)
    kinetic = 0.5*(reduced[4:8, 4:8] + reduced[4:8, 4:8].T)
    return FlatGaugeReducedAction(
        reduced_hessian=np.asarray(reduced, dtype=float),
        kinetic_hessian=np.asarray(kinetic, dtype=float),
        auxiliary_hessian=np.asarray(Qaa, dtype=float),
        auxiliary_rank=rank,
        auxiliary_condition_number=float(np.linalg.cond(Qaa)),
    )
