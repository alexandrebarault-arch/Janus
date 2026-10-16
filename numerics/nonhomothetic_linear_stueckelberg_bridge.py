"""Linear bridge between g-flat De Felice variables and relative Stueckelberg fields."""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class RelativeStueckelberg:
    T: float
    L: float
    T_dot: float
    L_dot: float


@dataclass(frozen=True)
class InducedFAuxiliaries:
    Phi_f: float
    B_f: float


@dataclass(frozen=True)
class PrincipalPiMap:
    eta_pi_t: float
    radial_pi_r: float
    cosmic_T_per_Ldot: float


def _finite(*values: float) -> None:
    if not all(math.isfinite(float(v)) for v in values):
        raise ValueError("all inputs must be finite")


def flat_gauge_to_relative_stueckelberg(
    *, psi_f: float, E_f: float, psi_f_dot: float, E_f_dot: float,
    k: float, inv_nHf: float, inv_nHf_dot: float,
) -> RelativeStueckelberg:
    """Recover the relative time/longitudinal shifts from g-flat variables.

    With the relative diffeomorphism placed in the g chart and a subsequent
    common transformation to g-flat gauge,

      E_f = -2 L,
      psi_f + k^2 E_f/6 = - n H_f T.

    ``inv_nHf`` is ``1/(n H_f)`` (``a/H_omega`` in repository variables).
    Dots are g-cosmic-time derivatives.
    """
    _finite(psi_f, E_f, psi_f_dot, E_f_dot, k, inv_nHf, inv_nHf_dot)
    if k < 0.0:
        raise ValueError("k must be nonnegative")
    C = k*k/6.0
    combo = psi_f + C*E_f
    combo_dot = psi_f_dot + C*E_f_dot
    T = -inv_nHf*combo
    T_dot = -(inv_nHf_dot*combo + inv_nHf*combo_dot)
    return RelativeStueckelberg(
        T=float(T), L=float(-0.5*E_f),
        T_dot=float(T_dot), L_dot=float(-0.5*E_f_dot),
    )


def pure_stueckelberg_qf(*, psi_f: float, E_f: float, k: float, inv_nHf: float) -> float:
    """Return the f matter gauge variable for a pure relative diffeomorphism.

    Eq. (72) gives ``q_f=Y2+A(Z+k^2 Y3/6)``.  For a pure Stückelberg mode
    ``Y2=0``, hence ``q_f=A(psi_f+k^2 E_f/6)=-T``.
    """
    _finite(psi_f, E_f, k, inv_nHf)
    if k < 0.0:
        raise ValueError("k must be nonnegative")
    return float(inv_nHf*(psi_f + k*k*E_f/6.0))


def induced_f_auxiliaries(
    *, T: float, T_dot: float, L_dot: float,
    n: float, alpha: float, n_dot_over_n: float,
) -> InducedFAuxiliaries:
    """Return the f lapse/shift induced by the common flattening diffeomorphism."""
    _finite(T, T_dot, L_dot, n, alpha, n_dot_over_n)
    if n <= 0.0 or alpha <= 0.0:
        raise ValueError("n and alpha must be positive")
    return InducedFAuxiliaries(
        Phi_f=float(-(T_dot + n_dot_over_n*T)),
        B_f=float((n/alpha)*T - (alpha/n)*L_dot),
    )


def principal_pi_map_coefficients(*, a: float, c: float) -> PrincipalPiMap:
    """Return the high-frequency non-homothetic pi-map coefficients.

    This is a principal-symbol statement only.  The time-dependent constrained
    reduction must supply all subleading background terms before a finite-H
    propagation speed is read.  In g conformal coordinates the principal map is

      delta_eta = -(c a^2)^-1 partial_eta pi,
      delta_r   =  a^-2 partial_r pi.

    Equivalently, in g cosmic time ``T/Ldot -> -a^2/c`` at high frequency.
    """
    _finite(a, c)
    if a <= 0.0 or c <= 0.0:
        raise ValueError("a and c must be positive")
    inva2 = 1.0/(a*a)
    return PrincipalPiMap(
        eta_pi_t=float(-inva2/c),
        radial_pi_r=float(inva2),
        cosmic_T_per_Ldot=float(-a*a/c),
    )
