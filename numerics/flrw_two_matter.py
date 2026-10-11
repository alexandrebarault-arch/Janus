"""Two-matter FLRW + high-k stability diagnostics for JANUS-R.

Implements the dynamical FLRW branch of ghost-free Hassan-Rosen bigravity
with separately coupled g- and f-sector dust, visible-sector radiation,
and beta_0 = 0.

Background equations follow Aoki & Maeda, arXiv:1312.7040.
High-k perturbative diagnostics follow De Felice et al., arXiv:1404.0008.

Conventions
-----------
H0 = 1, M_g = 1.
alpha = M_f / M_g and kappa = alpha^2.
Omega_f_m0 is rho_f0/(3 M_g^2 H0^2), not the f-sector critical fraction.
a_g(today)=1, y=a_f/a_g and y(today)=y0.
f-sector dust evolves as rho_f ~ a_f^-3.

Important
---------
The simple de-Sitter-looking inequality m_eff^2 > 2 H^2 is NOT used as a
general two-fluid Higuchi test. On the healthy two-fluid branch the relevant
high-k scalar no-ghost quantity is B (De Felice et al. Eq. 80/82). The code
also evaluates the scalar and vector propagation speeds. Negative scalar
c_s^2 is a gradient instability of the linearized theory; it is distinct from
a ghost and is precisely the regime in which nonlinear/Vainshtein physics may
be required.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Params:
    beta1: float = 1.0
    beta2: float = -1.75
    beta3: float = 0.0
    beta4: float = 1.8160193651823988
    alpha: float = 1.0
    omega_g_m0: float = 0.30
    omega_g_r0: float = 9.0e-5
    omega_f_m0: float = 0.03
    y0: float = 0.175
    m2_over_H02: float = 5.765024453024453


def candidate_c() -> Params:
    """Stability-extended, ~100 Mpc Compton-range research candidate.

    This point is NOT observationally fitted and NOT proven nonlinearly viable.
    It is retained as a stress-test because it delays the scalar linear
    gradient instability to z~142 while keeping m_eff,0/H0~42 and satisfies
    beta2<0, beta2^2-beta1*beta3>0 (the sufficient coefficient sign condition
    used in the homothetic nonlinear analysis of Aoki-Maeda-Namba 2015).
    """
    return Params(
        beta1=1.0,
        beta2=-4.2383993109,
        beta3=13.6801214252,
        beta4=-38.5117901844,
        alpha=0.10879548725,
        omega_g_m0=0.30,
        omega_g_r0=9.0e-5,
        omega_f_m0=0.23958426762,
        y0=0.55688253212,
        m2_over_H02=23.3348939346,
    )


def U_g(y: np.ndarray | float, p: Params):
    return 3.0 * p.beta1 * y + 3.0 * p.beta2 * y**2 + p.beta3 * y**3


def U_f(y: np.ndarray | float, p: Params):
    return (
        p.beta4
        + 3.0 * p.beta3 / y
        + 3.0 * p.beta2 / y**2
        + p.beta1 / y**3
    )


def omega_g(a: np.ndarray | float, p: Params):
    return p.omega_g_m0 * a**-3 + p.omega_g_r0 * a**-4


def omega_f_dust(a: np.ndarray | float, y: np.ndarray | float, p: Params):
    return p.omega_f_m0 * (p.y0 / (a * y)) ** 3


def friedmann_g(a: float, y: float, p: Params):
    return omega_g(a, p) + p.m2_over_H02 * U_g(y, p) / 3.0


def branch_constraint(a: float, y: float, p: Params):
    return (
        friedmann_g(a, y, p)
        - y**2 * omega_f_dust(a, y, p) / p.alpha**2
        - p.m2_over_H02 * y**2 * U_f(y, p) / (3.0 * p.alpha**2)
    )


def polynomial_coefficients(a: float, p: Params) -> np.ndarray:
    """Quartic coefficients for the dynamical branch with f-sector dust."""
    m2 = p.m2_over_H02
    a2 = p.alpha**2
    return np.array(
        [
            a2 * m2 * p.beta3 / 3.0,
            a2 * m2 * p.beta2 - m2 * p.beta4 / 3.0,
            a2 * m2 * p.beta1 - m2 * p.beta3,
            a2 * omega_g(a, p) - m2 * p.beta2,
            -p.omega_f_m0 * p.y0**3 * a**-3 - m2 * p.beta1 / 3.0,
        ],
        dtype=float,
    )


def positive_real_roots(a: float, p: Params, tol: float = 1e-8) -> np.ndarray:
    coeff = np.trim_zeros(polynomial_coefficients(a, p), trim="f")
    roots = np.roots(coeff)
    return np.asarray(sorted(r.real for r in roots if abs(r.imag) < tol and r.real > 0.0))


def solve_branch(a_grid: np.ndarray, p: Params) -> np.ndarray:
    """Follow the positive root continuously from a=1."""
    a_grid = np.asarray(a_grid, dtype=float)
    if len(a_grid) < 2 or not np.isclose(a_grid[0], 1.0):
        raise ValueError("a_grid must start at a=1")
    if not (np.all(np.diff(a_grid) < 0) or np.all(np.diff(a_grid) > 0)):
        raise ValueError("a_grid must be monotonic after a=1")

    y = np.empty_like(a_grid)
    y[0] = p.y0
    for i in range(1, len(a_grid)):
        roots = positive_real_roots(float(a_grid[i]), p)
        if roots.size == 0:
            raise RuntimeError(f"No positive real branch root at a={a_grid[i]:.8g}")
        prev = y[i - 1]
        y[i] = min(roots, key=lambda r: abs(np.log(r / prev)))
    return y


def dy_dloga(a: np.ndarray, y: np.ndarray, p: Params) -> np.ndarray:
    """Implicit derivative of the quartic branch equation."""
    a = np.asarray(a, dtype=float)
    y = np.asarray(y, dtype=float)
    coeff = np.array([polynomial_coefficients(float(ai), p) for ai in a])
    dP_dy = (
        4.0 * coeff[:, 0] * y**3
        + 3.0 * coeff[:, 1] * y**2
        + 2.0 * coeff[:, 2] * y
        + coeff[:, 3]
    )
    dP_dloga = (
        p.alpha**2
        * (-3.0 * p.omega_g_m0 * a**-3 - 4.0 * p.omega_g_r0 * a**-4)
        * y
        + 3.0 * p.omega_f_m0 * p.y0**3 * a**-3
    )
    return -dP_dloga / dP_dy


def diagnostics(a_grid: np.ndarray, y: np.ndarray, p: Params) -> dict[str, np.ndarray]:
    """Background and De-Felice high-k stability diagnostics."""
    a = np.asarray(a_grid, dtype=float)
    y = np.asarray(y, dtype=float)
    yp = dy_dloga(a, y, p)
    ctilde = 1.0 + yp / y  # n a/(N a_f); lapse ratio n/N = ctilde*y
    lapse_ratio = ctilde * y

    E2 = omega_g(a, p) + p.m2_over_H02 * U_g(y, p) / 3.0
    J = p.beta1 + 2.0 * p.beta2 * y + p.beta3 * y**2
    Jp = 2.0 * p.beta2 + 2.0 * p.beta3 * y
    Gamma = y * J + 0.5 * (ctilde - 1.0) * y**2 * Jp
    kappa = p.alpha**2

    meff2 = (
        p.m2_over_H02
        * (1.0 + kappa * y**2)
        / (kappa * y**2)
        * Gamma
    )

    W = (
        p.m2_over_H02 * (1.0 + kappa * y**2) * J / (2.0 * kappa * y)
        - E2
    )

    # f dust density in units M_g^2 H0^2, i.e. rho_f/H0^2 = 3 Omega_f.
    omega_f = omega_f_dust(a, y, p)
    # De Felice Eq. (82), flat case, f-dust pressure = 0.
    B = 2.0 * W + 3.0 * y**2 * omega_f / kappa

    with np.errstate(divide="ignore", invalid="ignore"):
        scalar_cs2 = (
            p.m2_over_H02
            / (3.0 * B)
            * (1.0 + 1.0 / (kappa * y**2))
            * (4.0 * Gamma - y * J * (ctilde + 1.0))
            + (ctilde - 4.0 * E2 * Gamma / (y * J * B)) / 3.0
        )
        vector_cv2 = (ctilde + 1.0) * Gamma / (2.0 * y * J)

    dE2_dloga = (
        -3.0 * p.omega_g_m0 * a**-3
        - 4.0 * p.omega_g_r0 * a**-4
        + p.m2_over_H02 * J * yp
    )
    q = -1.0 - 0.5 * dE2_dloga / E2

    return {
        "E2": E2,
        "E": np.sqrt(E2),
        "q": q,
        "J": J,
        "Jp": Jp,
        "Gamma": Gamma,
        "dy_dloga": yp,
        "ctilde": ctilde,
        "lapse_ratio": lapse_ratio,
        "meff2_over_H02": meff2,
        "meff2_over_H2": meff2 / E2,
        "W_over_H02": W,
        "B_over_H02": B,
        "scalar_cs2": scalar_cs2,
        "vector_cv2": vector_cv2,
    }


def first_sign_crossing(z: np.ndarray, values: np.ndarray) -> float | None:
    for i in range(len(values) - 1):
        u, v = values[i], values[i + 1]
        if not np.isfinite(u) or not np.isfinite(v):
            continue
        if u == 0.0:
            return float(z[i])
        if u * v < 0.0:
            frac = -u / (v - u)
            return float(z[i] + frac * (z[i + 1] - z[i]))
    return None


def max_background_deviation(p: Params, zmax: float = 2.0) -> float:
    a = np.geomspace(1.0, 1.0 / (1.0 + zmax), 500)
    y = solve_branch(a, p)
    d = diagnostics(a, y, p)
    omega_lambda = 1.0 - p.omega_g_m0 - p.omega_g_r0
    E_lcdm = np.sqrt(
        p.omega_g_m0 * a**-3 + p.omega_g_r0 * a**-4 + omega_lambda
    )
    return float(np.max(np.abs(d["E"] / E_lcdm - 1.0)))


def benchmark_checks(p: Params | None = None) -> None:
    p = Params() if p is None else p
    assert abs(friedmann_g(1.0, p.y0, p) - 1.0) < 1e-9
    assert abs(branch_constraint(1.0, p.y0, p)) < 1e-8

    past_a = np.geomspace(1.0, 1e-6, 2500)
    past_y = solve_branch(past_a, p)
    d = diagnostics(past_a, past_y, p)
    assert np.all(past_y > 0.0)
    assert np.all(d["lapse_ratio"] > 0.0)
    assert np.all(d["J"] > 0.0)
    assert np.all(d["E2"] > 0.0)
    assert np.all(d["B_over_H02"] > 0.0)  # high-k scalar no ghost

    future_a = np.geomspace(1.0, 100.0, 500)
    future_y = solve_branch(future_a, p)
    future = diagnostics(future_a, future_y, p)
    assert np.all(future["lapse_ratio"] > 0.0)
    assert np.all(future["J"] > 0.0)
    assert abs(future["q"][-1] + 1.0) < 2e-4


def summary(p: Params, label: str) -> None:
    a = np.geomspace(1.0, 1e-6, 5000)
    y = solve_branch(a, p)
    d = diagnostics(a, y, p)
    z = 1.0 / a - 1.0
    cs_cross = first_sign_crossing(z, d["scalar_cs2"])
    cv_cross = first_sign_crossing(z, d["vector_cv2"])

    print(label)
    print(f"  beta = (0, {p.beta1}, {p.beta2}, {p.beta3}, {p.beta4})")
    print(f"  alpha={p.alpha}, y0={p.y0}, Omega_f0={p.omega_f_m0}")
    print(f"  m^2/H0^2={p.m2_over_H02}")
    print(f"  max |H/H_LCDM-1| z<=2 = {max_background_deviation(p):.6f}")
    print(f"  q0={d['q'][0]:.6f}")
    print(f"  m_eff,0/H0={np.sqrt(d['meff2_over_H02'][0]):.6f}")
    print(f"  B_min/H0^2={np.nanmin(d['B_over_H02']):.6g}")
    print(f"  scalar c_s^2(0)={d['scalar_cs2'][0]:.6f}")
    print(f"  scalar gradient crossing z={cs_cross}")
    print(f"  vector c_V^2(0)={d['vector_cv2'][0]:.6f}")
    print(f"  vector crossing z={cv_cross}")


def main() -> None:
    baseline = Params()
    extended = candidate_c()
    benchmark_checks(baseline)
    benchmark_checks(extended)
    summary(baseline, "Baseline A")
    summary(extended, "Candidate C")


if __name__ == "__main__":
    main()
