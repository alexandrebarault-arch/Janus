"""Two-matter FLRW background diagnostic for ghost-free Hassan-Rosen bigravity.

Research branch: JANUS-R V2

This module implements the spatially flat dynamical FLRW branch with
separately coupled g- and f-sector fluids.

Conventions
-----------
We use

    ds_g^2 = -N_g^2 dt^2 + a_g^2 dx^2
    ds_f^2 = -N_f^2 dt^2 + a_f^2 dx^2

and define

    y = a_f / a_g,
    alpha = M_f / M_g.

The interaction potential is parameterized by beta_0 ... beta_4 and the
observable-sector Friedmann equation is

    3 H_g^2 = rho_g/M_g^2
                + m^2 [beta_0 + 3 beta_1 y + 3 beta_2 y^2 + beta_3 y^3].

On the dynamical Bianchi branch,

    H_f = H_g / y,
    N_f/N_g = d a_f / d a_g = y + d y/d ln(a_g).

Equating the two Friedmann equations yields an algebraic equation F(y,a)=0.
The code solves this equation continuously in scale factor rather than
integrating an independent differential equation for y.

Important limitation
--------------------
Passing the background checks in this file is NOT a perturbative stability
proof. In particular, a model can have a smooth lapse-positive background and
still fail because of scalar/vector/tensor ghosts or gradient instabilities.
The generalized Higuchi / kinetic-matrix test belongs to Gate 2.

References
----------
K. Aoki & K.-i. Maeda, Phys. Rev. D 89, 064051 (2014), arXiv:1312.7040.
S. F. Hassan & R. A. Rosen, JHEP 02 (2012) 126, arXiv:1109.3515.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq


@dataclass(frozen=True)
class Beta:
    beta0: float = 0.0
    beta1: float = 0.0
    beta2: float = 0.0
    beta3: float = 0.0
    beta4: float = 0.0


@dataclass(frozen=True)
class Model:
    beta: Beta
    alpha: float
    y0: float
    omega_g_m0: float = 0.30
    omega_g_r0: float = 9.0e-5
    # Derived / calibrated quantities, in H0=M_g=1 units.
    m2: float | None = None
    omega_f_m0: float | None = None

    def calibrated(self) -> "Model":
        """Calibrate m^2 and present f-dust density from H_g(a=1)=H0.

        The input y0 is treated as a branch label. With beta0=0 this is a
        convenient way to scan self-accelerating backgrounds without inserting
        an explicit visible-sector cosmological constant.
        """
        if self.alpha <= 0 or self.y0 <= 0:
            raise ValueError("alpha and y0 must be positive")

        omega_g0 = self.omega_g_m0 + self.omega_g_r0
        ug0 = u_g(self.y0, self.beta)
        if ug0 <= 0:
            raise ValueError("u_g(y0) must be positive for m^2 > 0 calibration")

        m2 = 3.0 * (1.0 - omega_g0) / ug0
        omega_f_m0 = 1.0 / self.y0**2 - (m2 / (3.0 * self.alpha**2)) * u_f(
            self.y0, self.beta
        )
        if m2 <= 0:
            raise ValueError("calibration produced non-positive m^2")
        if omega_f_m0 < 0:
            raise ValueError("calibration produced negative present f density")

        return Model(
            beta=self.beta,
            alpha=self.alpha,
            y0=self.y0,
            omega_g_m0=self.omega_g_m0,
            omega_g_r0=self.omega_g_r0,
            m2=m2,
            omega_f_m0=omega_f_m0,
        )


def _require_calibrated(m: Model) -> None:
    """Reject use of background equations before model calibration.

    ``m2`` and ``omega_f_m0`` are the two derived quantities required by the
    FLRW background functions below.  Keeping this guard explicit avoids
    silently converting ``None`` through ``float()`` and gives callers a clear
    instruction to use ``Model.calibrated()`` first.
    """
    if m.m2 is None or m.omega_f_m0 is None:
        raise ValueError("model must be calibrated() before FLRW evolution")


def u_g(y: float | np.ndarray, b: Beta):
    return b.beta0 + 3.0 * b.beta1 * y + 3.0 * b.beta2 * y**2 + b.beta3 * y**3


def u_f(y: float | np.ndarray, b: Beta):
    return (
        b.beta4
        + 3.0 * b.beta3 / y
        + 3.0 * b.beta2 / y**2
        + b.beta1 / y**3
    )


def j_mix(y: float | np.ndarray, b: Beta):
    """Derivative combination controlling mass/mixing on proportional backgrounds."""
    return b.beta1 + 2.0 * b.beta2 * y + b.beta3 * y**2


def densities(a: float, y: float, m: Model) -> tuple[float, float]:
    """Return rho_g/M_g^2 and rho_f/M_g^2 in H0=1 units.

    g matter contains pressureless matter plus radiation. The current V2
    background gate keeps the f sector pressureless. f-dust conservation uses
    a_f = y a_g and a_f0 = y0.
    """
    _require_calibrated(m)
    rho_g = 3.0 * (
        m.omega_g_m0 * a ** -3 + m.omega_g_r0 * a ** -4
    )
    rho_f = (
        3.0
        * m.alpha**2
        * float(m.omega_f_m0)
        * (m.y0 / (y * a)) ** 3
    )
    return rho_g, rho_f


def match_equation(y: float, a: float, m: Model) -> float:
    """Algebraic dynamical-branch equation obtained from both Friedmann equations."""
    _require_calibrated(m)
    rho_g, rho_f = densities(a, y, m)
    return (
        m.alpha**2 * rho_g
        - y**2 * rho_f
        + float(m.m2)
        * (
            m.alpha**2 * u_g(y, m.beta)
            - y**2 * u_f(y, m.beta)
        )
    )


def hubble2_g(a: float, y: float, m: Model) -> float:
    _require_calibrated(m)
    rho_g, _ = densities(a, y, m)
    return (rho_g + float(m.m2) * u_g(y, m.beta)) / 3.0


def effective_spin2_mass2(y: float | np.ndarray, m: Model):
    """Proportional-background mass proxy used only as a diagnostic.

    This quantity is not, by itself, a full FLRW no-ghost condition.
    """
    _require_calibrated(m)
    return (
        float(m.m2)
        * (1.0 + 1.0 / (m.alpha**2 * y**2))
        * y
        * j_mix(y, m.beta)
    )


def roots_at_a(
    a: float,
    m: Model,
    y_min: float = 1.0e-7,
    y_max: float = 1.0e4,
    samples: int = 800,
) -> np.ndarray:
    """Find positive real roots by logarithmic bracketing."""
    grid = np.logspace(np.log10(y_min), np.log10(y_max), samples)
    roots: list[float] = []
    x0 = grid[0]
    f0 = match_equation(x0, a, m)
    for x1 in grid[1:]:
        f1 = match_equation(x1, a, m)
        if np.isfinite(f0) and np.isfinite(f1) and f0 * f1 < 0.0:
            root = brentq(lambda yy: match_equation(yy, a, m), x0, x1, maxiter=200)
            if not roots or abs(root - roots[-1]) > 1e-8 * max(1.0, abs(root)):
                roots.append(root)
        x0, f0 = x1, f1
    return np.asarray(roots)


def track_from_today(
    m: Model,
    a_min: float = 1.0e-4,
    points: int = 500,
) -> tuple[np.ndarray, np.ndarray]:
    """Track the continuous root connected to y(a=1)=y0 backwards in time."""
    _require_calibrated(m)
    a_values = np.geomspace(1.0, a_min, points)
    y_values = [m.y0]
    previous = m.y0

    for a in a_values[1:]:
        local = roots_at_a(
            a,
            m,
            y_min=max(1.0e-8, previous / 12.0),
            y_max=min(1.0e6, previous * 12.0),
            samples=360,
        )
        if len(local) == 0:
            local = roots_at_a(a, m)
        if len(local) == 0:
            raise RuntimeError(f"branch lost: no positive root at a={a:g}")
        chosen = min(local, key=lambda yy: abs(np.log(yy / previous)))
        y_values.append(float(chosen))
        previous = float(chosen)

    return a_values, np.asarray(y_values)


def branch_diagnostics(a: np.ndarray, y: np.ndarray, m: Model) -> dict[str, np.ndarray]:
    """Compute background quantities without claiming perturbative stability."""
    ln_a = np.log(a)
    dy_dln_a = np.gradient(y, ln_a)
    lapse_ratio = y + dy_dln_a
    h2 = np.asarray([hubble2_g(ai, yi, m) for ai, yi in zip(a, y)])
    meff2 = effective_spin2_mass2(y, m)
    return {
        "H2": h2,
        "H": np.sqrt(np.where(h2 >= 0.0, h2, np.nan)),
        "lapse_ratio": lapse_ratio,
        "J": j_mix(y, m.beta),
        "m_eff2": meff2,
    }


def lcdm_hubble(a: np.ndarray, omega_m0: float = 0.30, omega_r0: float = 9e-5):
    omega_lambda0 = 1.0 - omega_m0 - omega_r0
    return np.sqrt(omega_m0 * a**-3 + omega_r0 * a**-4 + omega_lambda0)


def regression_model() -> Model:
    """A reproducible background-only point found in the first V2 scan.

    It is deliberately NOT called a viable cosmological model. Its purpose is
    to regression-test branch continuity and show why background expansion is
    a weak discriminator: this point mimics flat Lambda-CDM at sub-percent
    level for z <= 2 while beta0=0.
    """
    return Model(
        beta=Beta(
            beta0=0.0,
            beta1=2.879912363842445,
            beta2=1.0433553612848283,
            beta3=0.4228370163756705,
            beta4=1.0561137605362703,
        ),
        alpha=0.67838201203862,
        y0=1.4009642016702197,
    ).calibrated()


def self_check() -> None:
    m = regression_model()
    assert abs(match_equation(m.y0, 1.0, m)) < 1.0e-9
    assert abs(hubble2_g(1.0, m.y0, m) - 1.0) < 1.0e-10

    a, y = track_from_today(m, a_min=1.0e-3, points=300)
    d = branch_diagnostics(a, y, m)
    assert np.all(np.isfinite(d["H"]))
    assert np.min(d["lapse_ratio"]) > 0.0
    assert np.min(d["J"]) > 0.0

    mask = a >= 1.0 / 3.0
    h_ref = lcdm_hubble(a[mask], m.omega_g_m0, m.omega_g_r0)
    frac = d["H"][mask] / h_ref - 1.0
    rms = float(np.sqrt(np.mean(frac**2)))
    max_abs = float(np.max(np.abs(frac)))
    assert rms < 0.005
    assert max_abs < 0.01

    # At very early times the visible radiation/matter terms dominate and the
    # chosen branch approaches the corresponding GR expansion rate.
    h_gr_early = np.sqrt(
        m.omega_g_m0 * a[-1] ** -3 + m.omega_g_r0 * a[-1] ** -4
    )
    assert abs(d["H"][-1] / h_gr_early - 1.0) < 1.0e-5

    print("FLRW background regression: PASS")
    print(f"m^2/H0^2 = {m.m2:.9g}")
    print(f"Omega_f,m0 = {m.omega_f_m0:.9g}")
    print(f"min lapse ratio = {np.min(d['lapse_ratio']):.9g}")
    print(f"z<=2 LCDM RMS fractional H difference = {rms:.6g}")
    print(f"z<=2 LCDM max fractional H difference = {max_abs:.6g}")


if __name__ == "__main__":
    self_check()
