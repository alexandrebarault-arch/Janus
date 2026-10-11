"""Reference linear twin-matter transfer solver from Aoki & Maeda (2014).

This implements the homothetic matter-era mass-eigenstate equations used in
K. Aoki & K.-i. Maeda, Phys. Rev. D 90, 124089 (2014), arXiv:1409.0202.

In the sub-horizon adiabatic-potential approximation (their Eqs. 4.34, 4.36),
the massless/common density mode obeys the standard EdS growing equation,
while the massive/relative mode has a scale-dependent effective source

    lambda_rel(a,k) = (4/3) * q^2/(1+q^2),
    q = k/(a m_eff).

Using N=ln a in an Einstein-de Sitter matter era:

    delta_common'' + 1/2 delta_common' - 3/2 delta_common = 0,
    delta_relative'' + 1/2 delta_relative'
        - 3/2 lambda_rel delta_relative = 0.

This file is intentionally a REFERENCE solver. Candidate C is non-homothetic,
has alpha != 1 and time-dependent mixing/m_eff, so this must not be presented
as its exact transfer function.

The key structural fact is exact in this reference system: common and relative
modes are linearly decoupled. Therefore an exactly adiabatic initial condition
(delta_relative=0 and derivative=0) never spontaneously generates a relative
mode.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt
import numpy as np
from scipy.integrate import solve_ivp


@dataclass(frozen=True)
class TransferResult:
    a: np.ndarray
    common: np.ndarray
    relative: np.ndarray
    common_prime: np.ndarray
    relative_prime: np.ndarray


def lambda_relative(a: float | np.ndarray, q_today: float) -> float | np.ndarray:
    """Aoki-Maeda relative-mode source eigenvalue.

    q_today = k/m_eff in units with a0=1. Physical q(a)=q_today/a.
    The asymptotes are:
      q >> 1 -> lambda_rel = 4/3 (repulsive/inside Compton regime)
      q << 1 -> lambda_rel -> 0 for the relative massive mode.
    """
    q = q_today / np.asarray(a)
    return (4.0 / 3.0) * q**2 / (1.0 + q**2)


def growing_index(lambda_g: float) -> float:
    """Growing EdS exponent for delta''+0.5delta'-1.5lambda_g delta=0."""
    return (-1.0 + sqrt(1.0 + 24.0 * lambda_g)) / 4.0


def solve_modes(
    a_initial: float,
    a_final: float,
    q_today: float,
    common_initial: float = 1.0,
    relative_initial: float = 0.0,
    common_prime_initial: float | None = None,
    relative_prime_initial: float | None = None,
    samples: int = 1000,
) -> TransferResult:
    """Integrate common and relative homothetic density modes.

    Primes are d/d ln(a). If slopes are omitted, the common growing slope is
    used and the relative slope is initialized to the local instantaneous
    growing index times delta_relative.
    """
    if not (0.0 < a_initial < a_final):
        raise ValueError("Require 0 < a_initial < a_final")
    if q_today < 0.0:
        raise ValueError("q_today must be non-negative")

    if common_prime_initial is None:
        common_prime_initial = common_initial
    if relative_prime_initial is None:
        lam_i = float(lambda_relative(a_initial, q_today))
        relative_prime_initial = growing_index(lam_i) * relative_initial

    N0, N1 = log(a_initial), log(a_final)
    N_eval = np.linspace(N0, N1, samples)

    def rhs(N: float, y: np.ndarray) -> np.ndarray:
        a = np.exp(N)
        lam = float(lambda_relative(a, q_today))
        dc, vc, dr, vr = y
        return np.array([
            vc,
            -0.5 * vc + 1.5 * dc,
            vr,
            -0.5 * vr + 1.5 * lam * dr,
        ])

    sol = solve_ivp(
        rhs,
        (N0, N1),
        [common_initial, common_prime_initial, relative_initial, relative_prime_initial],
        t_eval=N_eval,
        rtol=1e-10,
        atol=1e-13,
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    return TransferResult(
        a=np.exp(sol.t),
        common=sol.y[0],
        relative=sol.y[2],
        common_prime=sol.y[1],
        relative_prime=sol.y[3],
    )


def relative_to_common_gain(z_initial: float, q_today: float) -> float:
    """Differential transfer gain (D_rel/D_common) from z_initial to today."""
    ai = 1.0 / (1.0 + z_initial)
    res = solve_modes(
        ai,
        1.0,
        q_today,
        common_initial=1.0,
        relative_initial=1.0,
    )
    return float((res.relative[-1] / res.relative[0]) /
                 (res.common[-1] / res.common[0]))


def required_initial_relative_fraction(z_initial: float, q_today: float) -> float:
    """Reference initial |delta_rel/delta_common| needed to reach unity today."""
    gain = relative_to_common_gain(z_initial, q_today)
    return np.inf if gain <= 0.0 else 1.0 / gain


def q_today_from_k(k_h_mpc: float, lambda_compton_mpc: float, h: float = 0.7) -> float:
    """Convert k [h/Mpc] and reduced Compton scale 1/m [Mpc] to k/m.

    No 2*pi is inserted: k is the Fourier wavenumber itself and 1/m is the
    reduced Compton length corresponding to that inverse wavenumber.
    """
    return k_h_mpc * h * lambda_compton_mpc


def regression_checks() -> None:
    # Exactly adiabatic initial condition: the relative mode remains exactly 0.
    ad = solve_modes(1e-3, 1.0, q_today=10.0, relative_initial=0.0)
    assert np.max(np.abs(ad.relative)) < 1e-14

    # Deep inside the Compton wavelength, the asymptotic growing exponent is
    # p=(-1+sqrt(33))/4 ~= 1.18614. Initialize on that eigenmode.
    p = growing_index(4.0 / 3.0)
    deep = solve_modes(
        1e-3,
        1.0,
        q_today=1e3,
        common_initial=1.0,
        relative_initial=1.0,
        relative_prime_initial=p,
    )
    p_num = np.log(deep.relative[-1] / deep.relative[0]) / np.log(1e3)
    assert abs(p_num - p) < 2e-5, (p_num, p)

    # A q_today around 1.6 reproduces the ~a^1.176 effective growth reported
    # numerically by Aoki & Maeda for their stable case (b), to ~1e-3.
    case_b = solve_modes(
        1e-3,
        1.0,
        q_today=1.6,
        common_initial=1.0,
        relative_initial=1.0,
        relative_prime_initial=p,
    )
    p_case = np.log(case_b.relative[-1]) / np.log(1e3)
    assert abs(p_case - 1.176) < 1e-3, p_case


def candidate_c_reference_table() -> None:
    """Scale-dependent reference bound for lambda_C ~=101.2 Mpc.

    This deliberately gives the relative mode every advantage: it starts at
    recombination and uses the homothetic Aoki-Maeda transfer law. Candidate C
    is expected to be screened/nonlinear during a substantial part of this
    interval, so these gains are optimistic upper-reference numbers, not an
    exact Candidate-C prediction.
    """
    z_i = 1100.0
    lambda_c = 101.2
    print("k[h/Mpc]  q0=k/m   Drel/Dcommon   required initial rel/common")
    for k in (0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2):
        q0 = q_today_from_k(k, lambda_c)
        gain = relative_to_common_gain(z_i, q0)
        req = 1.0 / gain
        print(f"{k:8.3f}  {q0:8.4f}  {gain:13.6f}  {req:27.6f}")


def main() -> None:
    regression_checks()
    print("Aoki-Maeda reference regression checks: PASS")
    print(f"p_max = {growing_index(4.0/3.0):.9f}")
    candidate_c_reference_table()


if __name__ == "__main__":
    main()
