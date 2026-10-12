"""Quasi-static reference bounds for Candidate-C Gate 2B.

This module deliberately separates three levels of statement.

1. ``spin2_static_kernels`` is the proportional-background linear spin-2
   result after diagonalizing the massless and Fierz-Pauli massive modes.
2. ``candidate_c_frozen_kernel`` freezes the non-homothetic Candidate-C
   background at one epoch and inserts its instantaneous mixing ratio and
   effective spin-2 mass into that proportional kernel.  This is a diagnostic,
   not an exact cosmological transfer function.
3. ``late_linear_rotation_bound`` is an intentionally optimistic reference
   bound.  It assumes that the entire late change of the instantaneous mixing
   angle can be converted into the relative density mode, and then lets that
   mode grow at the maximal Aoki-Maeda short-wavelength rate.  It is useful as
   a falsification yardstick, not as a theorem.

The exact non-homothetic relativistic transfer system remains a separate Gate
2B task.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import atan, degrees, sin, sqrt

from scipy.optimize import brentq

from numerics.candidate_c_transfer import candidate_c_background_point


@dataclass(frozen=True)
class FrozenKernelDiagnostic:
    a: float
    k_hmpc: float
    r: float
    mixing_angle_rad: float
    meff_over_H: float
    yukawa_fraction: float
    q_gg: float
    q_gf: float
    q_ff: float


@dataclass(frozen=True)
class LateLinearRotationBound:
    z_cross: float
    theta_cross_deg: float
    theta_today_deg: float
    delta_theta_deg: float
    kinematic_conversion_reference: float
    max_differential_growth: float
    final_relative_to_common_upper_reference: float


def spin2_static_kernels(
    *,
    r: float,
    yukawa_fraction: float,
) -> tuple[float, float, float]:
    """Return normalized (gg, gf, ff) frozen proportional spin-2 kernels.

    ``r`` is the instantaneous Planck/mixing ratio alpha*y.  The Yukawa
    fraction is S=k^2/(k^2+mu^2), with 0 <= S <= 1.  Normalization is chosen
    so every channel tends to the same long-range massless value Q=1.

    The Fierz-Pauli scalar polarization supplies the 4/3 coefficient:

        Q_gg = 1 + (4/3) r^2 S
        Q_gf = 1 - (4/3) S
        Q_ff = 1 + (4/3) S/r^2
    """
    r = float(r)
    S = float(yukawa_fraction)
    if not r > 0.0:
        raise ValueError("r must be positive")
    if not 0.0 <= S <= 1.0:
        raise ValueError("yukawa_fraction must lie in [0, 1]")

    q_gg = 1.0 + (4.0 / 3.0) * r * r * S
    q_gf = 1.0 - (4.0 / 3.0) * S
    q_ff = 1.0 + (4.0 / (3.0 * r * r)) * S
    return float(q_gg), float(q_gf), float(q_ff)


def _effective_mass_squared(point) -> float:
    """De-Felice healthy-branch effective spin-2 mass in H0^2 units."""
    bg = point.metric
    if bg.kappa <= 0.0 or bg.xi <= 0.0:
        raise ValueError("Candidate-C kappa and xi must be positive")

    # candidate_c_transfer maps Comelli f1 exactly to JANUS Gamma.
    gamma = bg.f1
    meff2 = (
        bg.m2
        * (1.0 + bg.kappa * bg.xi**2)
        / (bg.kappa * bg.xi**2)
        * gamma
    )
    if meff2 <= 0.0:
        raise ValueError("effective spin-2 mass squared must be positive")
    return float(meff2)


def candidate_c_frozen_kernel(
    *,
    a: float,
    k_hmpc: float,
) -> FrozenKernelDiagnostic:
    """Evaluate the instantaneous frozen-background kernel for Candidate C."""
    if not a > 0.0:
        raise ValueError("a must be positive")
    if k_hmpc < 0.0:
        raise ValueError("k_hmpc must be non-negative")

    point = candidate_c_background_point(float(a), k_hmpc=float(k_hmpc))
    bg = point.metric
    meff2 = _effective_mass_squared(point)

    # bg.H is conformal Hubble calH=a*H_phys, all in H0 units.
    H_phys = bg.H / bg.a
    meff_over_H = sqrt(meff2) / H_phys

    # The Fourier k stored by the background adapter is comoving.  Hence the
    # comoving inverse Compton scale is a*m_eff.
    mu2_comoving = bg.a**2 * meff2
    if bg.k2 == 0.0:
        S = 0.0
    else:
        S = bg.k2 / (bg.k2 + mu2_comoving)

    r = sqrt(bg.kappa) * bg.xi
    q_gg, q_gf, q_ff = spin2_static_kernels(r=r, yukawa_fraction=S)
    return FrozenKernelDiagnostic(
        a=float(bg.a),
        k_hmpc=float(k_hmpc),
        r=float(r),
        mixing_angle_rad=float(atan(r)),
        meff_over_H=float(meff_over_H),
        yukawa_fraction=float(S),
        q_gg=q_gg,
        q_gf=q_gf,
        q_ff=q_ff,
    )


def find_h_equals_meff_redshift(
    *,
    z_min: float = 0.0,
    z_max: float = 142.0,
) -> float:
    """Find the Candidate-C crossing m_eff/H=1 on the late branch."""
    if z_min < 0.0 or z_max <= z_min:
        raise ValueError("require 0 <= z_min < z_max")

    def residual(z: float) -> float:
        d = candidate_c_frozen_kernel(
            a=1.0 / (1.0 + z),
            k_hmpc=0.0,
        )
        return d.meff_over_H - 1.0

    f_min = residual(float(z_min))
    f_max = residual(float(z_max))
    if f_min == 0.0:
        return float(z_min)
    if f_max == 0.0:
        return float(z_max)
    if f_min * f_max > 0.0:
        raise ValueError("m_eff/H=1 is not bracketed by the requested redshifts")
    return float(brentq(residual, float(z_min), float(z_max), xtol=1e-12, rtol=1e-12))


def late_linear_rotation_bound(
    *,
    z_start: float | None = None,
) -> LateLinearRotationBound:
    """Optimistic reference bound on late linear common->relative conversion.

    If ``z_start`` is omitted, the late regime begins at the Candidate-C
    crossing m_eff/H=1.  The bound then makes two deliberately favorable
    assumptions:

    * all of the instantaneous basis rotation |Delta theta| converts common
      amplitude into relative amplitude, with fraction sin(|Delta theta|);
    * that relative component grows from z_start to today at the maximal
      Aoki-Maeda short-wavelength exponent p=(-1+sqrt(33))/4, while the common
      mode grows as a.

    This is a transparent upper-reference yardstick.  It is not the exact
    non-homothetic transfer matrix and must not be quoted as a rigorous bound
    on arbitrary nonlinear evolution.
    """
    z_cross = find_h_equals_meff_redshift() if z_start is None else float(z_start)
    if z_cross < 0.0:
        raise ValueError("z_start must be non-negative")

    start = candidate_c_frozen_kernel(
        a=1.0 / (1.0 + z_cross),
        k_hmpc=0.0,
    )
    today = candidate_c_frozen_kernel(a=1.0, k_hmpc=0.0)

    delta_theta = abs(start.mixing_angle_rad - today.mixing_angle_rad)
    conversion = sin(delta_theta)

    p_relative_max = (-1.0 + sqrt(33.0)) / 4.0
    p_common = 1.0
    differential_growth = (1.0 + z_cross) ** (p_relative_max - p_common)
    final_reference = conversion * differential_growth

    return LateLinearRotationBound(
        z_cross=float(z_cross),
        theta_cross_deg=float(degrees(start.mixing_angle_rad)),
        theta_today_deg=float(degrees(today.mixing_angle_rad)),
        delta_theta_deg=float(degrees(delta_theta)),
        kinematic_conversion_reference=float(conversion),
        max_differential_growth=float(differential_growth),
        final_relative_to_common_upper_reference=float(final_reference),
    )


def main() -> None:
    print("Candidate-C frozen quasi-static diagnostics")
    print("z      k[h/Mpc]      r        S       Qgg       Qgf        Qff")
    for z in (0.0, 1.0, 10.0, 100.0, 140.0):
        for k in (0.01, 0.03, 0.1):
            d = candidate_c_frozen_kernel(a=1.0/(1.0+z), k_hmpc=k)
            print(
                f"{z:5.1f}  {k:9.3f}  {d.r:7.4f}  {d.yukawa_fraction:7.4f}  "
                f"{d.q_gg:8.4f}  {d.q_gf:8.4f}  {d.q_ff:10.3f}"
            )

    b = late_linear_rotation_bound()
    print()
    print(f"m_eff/H=1 crossing: z={b.z_cross:.6f}")
    print(
        "late mixing rotation: "
        f"{b.theta_cross_deg:.6f} deg -> {b.theta_today_deg:.6f} deg, "
        f"Delta={b.delta_theta_deg:.6f} deg"
    )
    print(f"kinematic conversion reference = {b.kinematic_conversion_reference:.6f}")
    print(f"max differential growth = {b.max_differential_growth:.6f}")
    print(
        "final relative/common upper reference = "
        f"{b.final_relative_to_common_upper_reference:.6f}"
    )


if __name__ == "__main__":
    main()
