"""Linear JANUS-R void response diagnostic.

This is intentionally *not* a cosmological likelihood code. It implements the
closed-form equal-Planck-mass linear response kernels recorded in
research/LINEAR_MODES_AND_SEGREGATION.md and research/OBSERVATIONAL_GATE.md.

Conventions
-----------
Visible void:       delta_g = -D, D > 0
Twin overdensity:   delta_f = R * D, R >= 0
x = k^2/(k^2 + a^2 mu^2), 0 <= x <= 1

Amplitudes are normalized to the GR response of the same visible density
contrast with no twin-sector perturbation.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Response:
    x: float
    twin_ratio: float
    lens: float
    dynamics: float

    @property
    def lens_to_dynamics(self) -> float:
        return self.lens / self.dynamics


def response(x: float, twin_ratio: float) -> Response:
    if not 0.0 <= x <= 1.0:
        raise ValueError("x must lie in [0,1]")
    if twin_ratio < 0.0:
        raise ValueError("twin_ratio must be non-negative")

    lens = (1.0 + x) - twin_ratio * (1.0 - x)
    dynamics = (1.0 + 4.0 * x / 3.0) - twin_ratio * (
        1.0 - 4.0 * x / 3.0
    )
    return Response(x, twin_ratio, lens, dynamics)


def equal_anticorrelated(x: float) -> Response:
    """delta_f = -delta_g in equal weighted units."""
    return response(x, 1.0)


def x_from_equal_mode_lensing(amplitude: float) -> float:
    """For R=1, A_lens=2x."""
    return amplitude / 2.0


def twin_ratio_for_gr_lensing(x: float) -> float:
    """Solve A_lens=1 for R at fixed x."""
    if not 0.0 <= x < 1.0:
        raise ValueError("requires 0 <= x < 1")
    return x / (1.0 - x)


def k_over_amu_from_x(x: float) -> float:
    """Invert x=k^2/(k^2+a^2 mu^2)."""
    if not 0.0 < x < 1.0:
        raise ValueError("requires 0 < x < 1")
    return math.sqrt(x / (1.0 - x))


def sartori_2025_toy() -> None:
    """Toy single-scale inversion of A_kappa=1.016+/-0.054.

    This is not a formal likelihood fit. It assumes an equal anti-correlated
    twin perturbation and identical visible void profile to the LCDM mock.
    """
    A = 1.016
    sigma_A = 0.054
    x = x_from_equal_mode_lensing(A)
    sigma_x = sigma_A / 2.0
    r = equal_anticorrelated(x)

    # In the equal mode A_dyn=(4/3) A_lens.
    sigma_dyn = (4.0 / 3.0) * sigma_A

    print(f"x = {x:.3f} +/- {sigma_x:.3f}")
    print(f"k/(a mu) = {k_over_amu_from_x(x):.3f}")
    print(f"A_lens = {r.lens:.3f}")
    print(f"A_dyn = {r.dynamics:.3f} +/- {sigma_dyn:.3f}")
    print(f"A_lens/A_dyn = {r.lens_to_dynamics:.3f}")


def regression_checks() -> None:
    # Equal anti-correlated identities.
    for x in (0.1, 0.5, 0.9):
        r = equal_anticorrelated(x)
        assert abs(r.lens - 2.0 * x) < 1e-12
        assert abs(r.dynamics - 8.0 * x / 3.0) < 1e-12
        assert abs(r.lens_to_dynamics - 0.75) < 1e-12

    # Exact crossover: GR-like lensing, enhanced dynamics.
    r = equal_anticorrelated(0.5)
    assert abs(r.lens - 1.0) < 1e-12
    assert abs(r.dynamics - 4.0 / 3.0) < 1e-12

    # General GR-lensing degeneracy curve.
    for x in (0.1, 0.3, 0.7):
        R = twin_ratio_for_gr_lensing(x)
        assert abs(response(x, R).lens - 1.0) < 1e-12


if __name__ == "__main__":
    regression_checks()
    print("Regression checks: PASS")
    sartori_2025_toy()
