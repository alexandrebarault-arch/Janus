"""Linear relative-mode gate for JANUS-R V2.

This is deliberately a transparent toy diagnostic, not a Boltzmann solver.
It quantifies the tension between

1. a spin-2 Compton scale large enough to affect late large-scale structure,
2. the resulting strength of the linear relative/segregation mode, and
3. the limited time available for that mode to grow from a small seed.

The formulas are the symmetric equal-Planck-mass, proportional-background,
sub-horizon limit already derived in research/LINEAR_MODES_AND_SEGREGATION.md.

For x = k^2 / (k^2 + a^2 m_eff^2),

    mu_common   = 1,
    mu_relative = 4 x / 3.

During Einstein-de Sitter evolution a mode delta ~ a^p has

    p(mu) = [-1 + sqrt(1 + 24 mu)] / 4.

No Planck isocurvature limit is hard-coded here: the JANUS-R relative mode is
not identical to standard CDM isocurvature and requires its own transfer
functions before observational limits can be mapped consistently.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


C_KM_S = 299_792.458
# H0/c expressed in h/Mpc because H0 = 100 h km/s/Mpc.
H0_OVER_C_H_MPC = 100.0 / C_KM_S


def compton_wavenumber_hmpc(m_eff_over_h0: float, a: float = 1.0) -> float:
    """Return a*m_eff/c in h/Mpc for m_eff specified in units of H0."""
    if m_eff_over_h0 < 0 or a <= 0:
        raise ValueError("m_eff/H0 must be non-negative and a must be positive")
    return a * m_eff_over_h0 * H0_OVER_C_H_MPC


def x_kernel(k_hmpc: float, m_eff_over_h0: float, a: float = 1.0) -> float:
    """Massive spin-2 interpolation factor x in [0,1]."""
    if k_hmpc < 0:
        raise ValueError("k must be non-negative")
    kc = compton_wavenumber_hmpc(m_eff_over_h0, a)
    if k_hmpc == 0 and kc == 0:
        return 0.0
    return k_hmpc**2 / (k_hmpc**2 + kc**2)


def mu_relative(x: float) -> float:
    if not 0.0 <= x <= 1.0:
        raise ValueError("x must lie in [0,1]")
    return 4.0 * x / 3.0


def eds_growth_exponent(mu_eff: float) -> float:
    """Growing-mode exponent p for delta proportional to a^p in EdS."""
    if mu_eff < 0:
        raise ValueError("mu_eff must be non-negative")
    return (-1.0 + math.sqrt(1.0 + 24.0 * mu_eff)) / 4.0


def absolute_growth(z_start: float, p: float) -> float:
    if z_start < 0:
        raise ValueError("z_start must be non-negative")
    return (1.0 + z_start) ** p


def relative_advantage(z_start: float, p_relative: float) -> float:
    """Growth of relative mode divided by GR/common delta~a growth."""
    return (1.0 + z_start) ** (p_relative - 1.0)


@dataclass(frozen=True)
class GatePoint:
    m_eff_over_h0: float
    k_hmpc: float
    a: float = 1.0

    @property
    def x(self) -> float:
        return x_kernel(self.k_hmpc, self.m_eff_over_h0, self.a)

    @property
    def mu_rel(self) -> float:
        return mu_relative(self.x)

    @property
    def p_rel(self) -> float:
        return eds_growth_exponent(self.mu_rel)


def self_check() -> None:
    # Fully unscreened analytic limit recorded in V1.
    p_max = eds_growth_exponent(4.0 / 3.0)
    expected = (-1.0 + math.sqrt(33.0)) / 4.0
    assert abs(p_max - expected) < 1e-14
    assert abs(p_max - 1.1861406616345072) < 1e-14

    # A graviton mass of order H0 is already deep in the modified kernel on
    # conventional LSS modes k=0.01--0.2 h/Mpc.
    p = GatePoint(m_eff_over_h0=1.5, k_hmpc=0.01)
    assert p.x > 0.997

    # Even under the deliberately optimistic assumption of uninterrupted,
    # maximally-unscreened EdS growth since recombination, a tiny 1e-5 seed
    # only reaches order 4e-2 today.
    growth_rec = absolute_growth(1100.0, p_max)
    assert 4000.0 < growth_rec < 4100.0
    assert 0.040 < 1e-5 * growth_rec < 0.041

    # If modification switches on only at z=10, the relative mode has almost
    # no time to build a nonlinear segregation from a tiny primordial seed.
    growth_z10 = absolute_growth(10.0, p_max)
    assert 17.0 < growth_z10 < 17.3

    print("Relative-mode gate: PASS")
    print(f"H0/c = {H0_OVER_C_H_MPC:.9g} h/Mpc")
    print(f"p_relative,max = {p_max:.12g}")
    print(
        "x(k=0.01 h/Mpc, m_eff=1.5 H0, a=1) = "
        f"{GatePoint(1.5, 0.01).x:.9g}"
    )
    print(f"max relative/common growth advantage since z=1100 = {relative_advantage(1100.0, p_max):.6g}")
    print(f"1e-5 seed -> {1e-5 * growth_rec:.6g} by z=0 (optimistic EdS toy limit)")
    print(f"1e-5 seed switched on at z=10 -> {1e-5 * growth_z10:.6g}")


if __name__ == "__main__":
    self_check()
