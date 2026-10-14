"""Instantaneous full Aoki polynomial proxy on the strict Candidate-C dust branch.

This module evaluates Aoki-Maeda-Namba (2015) Eq. (5.8) with the instantaneous
strict Candidate-C dust background.  It is a diagnostic proxy only: Candidate C
is non-homothetic, so this does not derive the missing nonlinear transition
system.  Its purpose is to test whether the early nonlinear algebraic branch
can adiabatically approach the late linear ``mu=0`` branch.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np
from numpy.polynomial import Polynomial as Poly

from numerics.candidate_c_dust_background import (
    candidate_c_dust_background_point,
    candidate_c_dust_params,
)
from numerics.flrw_two_matter import diagnostics


@dataclass(frozen=True)
class AokiFullBranchTrack:
    a: np.ndarray
    mu: np.ndarray
    mu_imag: np.ndarray
    nearest_root_separation: np.ndarray
    normalized_polynomial_slope: np.ndarray


def _background_inputs(a: float) -> tuple[float, float, float, float, float, float]:
    p = candidate_c_dust_params()
    point = candidate_c_dust_background_point(float(a), k_hmpc=0.0)
    d = diagnostics(np.array([float(a)]), np.array([point.y]), p)
    H2 = float(d["E2"][0])
    meff2 = float(d["meff2_over_H02"][0])
    q = float(d["q"][0])
    w_eff = (2.0*q - 1.0)/3.0

    y = point.y
    den = p.beta1*y + 2.0*p.beta2*y*y + p.beta3*y**3
    scale = max(1.0, abs(p.beta1*y), abs(2.0*p.beta2*y*y), abs(p.beta3*y**3))
    if abs(den) <= 1.0e-14*scale:
        raise np.linalg.LinAlgError("Aoki normalized-coupling denominator is singular")
    beta2 = (p.beta2*y*y + p.beta3*y**3)/den
    beta3 = p.beta3*y**3/den

    alpha2_y2 = p.alpha**2*y*y
    mg2 = meff2*alpha2_y2/(1.0 + alpha2_y2)
    mf2 = meff2/(1.0 + alpha2_y2)
    return H2, w_eff, float(beta2), float(beta3), float(mg2), float(mf2)


def exact_polynomial_coefficients(
    a: float,
    *,
    source_g: float = 0.0,
    source_f: float = 0.0,
) -> np.ndarray:
    """Return descending coefficients of Aoki et al. Eq. (5.8).

    Unlike ``aoki_scalar_polynomial.polynomial_coefficients()``, this helper
    constructs the polynomial algebraically rather than by Vandermonde
    interpolation.  That matters when branch separation is itself the object
    of the diagnostic.
    """
    vals = (a, source_g, source_f)
    if not all(math.isfinite(float(v)) for v in vals) or a <= 0.0:
        raise ValueError("a must be positive and all inputs finite")

    H2, w, beta2, beta3, mg2, mf2 = _background_inputs(float(a))
    u = Poly([0.0, 1.0])
    one = Poly([1.0])

    g = mg2*(one + u)**2*(
        9.0
        + 18.0*beta2*u
        + (6.0*beta2**2 + 4.0*beta3)*u**2
        - beta3**2*u**4
    )
    f = mf2*(
        9.0
        + 18.0*(1.0 + beta2)*u
        + (10.0 + 34.0*beta2 + 4.0*beta3 + 6.0*beta2**2)*u**2
        + (2.0 + 14.0*beta2 + 8.0*beta3 + 12.0*beta2**2)*u**3
        + (
            2.0*beta2 + 2.0*beta3 + 2.0*beta2**2
            - beta3**2 + 4.0*beta2*beta3
        )*u**4
    )
    C_m2 = u*(g + f)
    C_H2 = -3.0*H2*u*(one + u)**2*(
        3.0*(1.0 - w)
        + 2.0*(1.0 + (1.0 - 3.0*w)*beta2)*u
        + (2.0*beta2 - (1.0 + 3.0*w)*beta3)*u**2
    )
    C_matter = (one + u)**2*(
        source_g*(one - beta3*u**2)
        - source_f*(one + u)*(one + 2.0*u + (2.0*beta2 - beta3)*u**2)
    )

    coeff = np.asarray((C_m2 + C_H2 + C_matter).coef[::-1], dtype=float)
    scale = max(1.0, float(np.max(np.abs(coeff))))
    coeff[np.abs(coeff) < 1.0e-14*scale] = 0.0
    return coeff


def roots_at_a(
    a: float,
    *,
    source_g: float = 0.0,
    source_f: float = 0.0,
) -> np.ndarray:
    coeff = np.trim_zeros(
        exact_polynomial_coefficients(a, source_g=source_g, source_f=source_f),
        trim="f",
    )
    return np.roots(coeff)


def real_roots_at_a(
    a: float,
    *,
    source_g: float = 0.0,
    source_f: float = 0.0,
    tol: float = 1.0e-9,
) -> np.ndarray:
    roots = roots_at_a(a, source_g=source_g, source_f=source_f)
    return np.asarray(sorted(
        r.real for r in roots if abs(r.imag) < tol and r.real > -1.0
    ), dtype=float)


def track_early_stable_branch(
    a_grid,
    *,
    equal_source_fraction: float = 0.0,
) -> AokiFullBranchTrack:
    """Track the early admissible negative branch continuously in ``a``.

    ``equal_source_fraction`` is a dimensionless sensitivity probe only.  It
    sets both Aoki matter-source terms to ``fraction * H^2`` and is not a
    replacement for the actual nonlinear perturbation source history.
    """
    a = np.asarray(a_grid, dtype=float)
    if (
        a.ndim != 1 or len(a) < 2 or not np.all(np.isfinite(a))
        or np.any(a <= 0.0) or not np.all(np.diff(a) > 0.0)
    ):
        raise ValueError("a_grid must be finite, positive and strictly increasing")
    eps = float(equal_source_fraction)
    if not math.isfinite(eps) or eps < 0.0:
        raise ValueError("equal_source_fraction must be finite and non-negative")

    mus: list[float] = []
    imags: list[float] = []
    separations: list[float] = []
    slopes: list[float] = []
    previous: complex | None = None

    for aa in a:
        H2, *_ = _background_inputs(float(aa))
        source = eps*H2
        coeff = exact_polynomial_coefficients(
            float(aa), source_g=source, source_f=source,
        )
        roots = np.roots(np.trim_zeros(coeff, trim="f"))

        if previous is None:
            admissible = [
                r for r in roots
                if abs(r.imag) < 1.0e-8 and -1.0 < r.real < -1.0e-8
            ]
            if not admissible:
                raise RuntimeError("no admissible early nonlinear root")
            # The Aoki-stable early branch is the admissible negative root
            # closest to zero for the Candidate-C coupling set.
            root = max(admissible, key=lambda r: r.real)
        else:
            root = min(roots, key=lambda r: abs(r - previous))

        distances = [abs(r - root) for r in roots if abs(r - root) > 1.0e-10]
        separation = min(distances) if distances else math.inf
        derivative = abs(np.polyval(np.polyder(coeff), root))
        polynomial_scale = max(
            1.0,
            float(np.polyval(np.abs(coeff), abs(root))),
        )

        mus.append(float(root.real))
        imags.append(float(root.imag))
        separations.append(float(separation))
        slopes.append(float(derivative/polynomial_scale))
        previous = root

    return AokiFullBranchTrack(
        a=a.copy(),
        mu=np.asarray(mus),
        mu_imag=np.asarray(imags),
        nearest_root_separation=np.asarray(separations),
        normalized_polynomial_slope=np.asarray(slopes),
    )
