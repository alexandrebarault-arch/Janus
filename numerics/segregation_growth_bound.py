"""Reference growth diagnostic for spontaneous JANUS-like segregation.

This is deliberately a *proxy*, not the full Candidate-C transfer solver.
It asks how much a maximally modified symmetric relative mode can outrun the
ordinary common growing mode after a transition redshift z_t.

For an Einstein-de Sitter background and a scale-independent effective
Poisson eigenvalue lambda_G (relative to GR),

    delta'' + (1/2) delta' - (3/2) lambda_G delta = 0

(primes are d/d ln a), so the growing exponent is

    p = (-1 + sqrt(1 + 24 lambda_G))/4.

The equal-mixing ghost-free spin-2 short-distance reference used in the V1
analysis has lambda_G = 4/3 for the relative mode and lambda_G=1 for the
common mode. This gives p_rel ~= 1.186 and only mild differential growth.

Do NOT interpret this as a theorem for arbitrary Planck-mass ratio or for the
nonlinear transition. It is a transparent yardstick. The exact Gate-2 coupled
transfer functions must replace it before a final cosmological claim.
"""

from __future__ import annotations

from math import sqrt


def growing_exponent(lambda_g: float) -> float:
    return (-1.0 + sqrt(1.0 + 24.0 * lambda_g)) / 4.0


def differential_amplification(z_transition: float,
                               lambda_relative: float = 4.0 / 3.0,
                               lambda_common: float = 1.0) -> float:
    p_rel = growing_exponent(lambda_relative)
    p_com = growing_exponent(lambda_common)
    return (1.0 + z_transition) ** (p_rel - p_com)


def minimum_relative_fraction_for_sign_flip(z_transition: float,
                                             lambda_relative: float = 4.0 / 3.0,
                                             lambda_common: float = 1.0) -> float:
    """Initial |delta_rel/delta_common| needed to exceed unity by today."""
    return 1.0 / differential_amplification(
        z_transition, lambda_relative, lambda_common
    )


def main() -> None:
    p_rel = growing_exponent(4.0 / 3.0)
    print(f"p_common = {growing_exponent(1.0):.9f}")
    print(f"p_relative(reference) = {p_rel:.9f}")
    print(f"Delta p = {p_rel - 1.0:.9f}")
    print()
    print("z_transition   rel/common gain   required initial relative fraction")
    for zt in (1.822, 10.0, 35.7, 54.0, 100.0, 142.4, 1100.0):
        gain = differential_amplification(zt)
        required = 1.0 / gain
        print(f"{zt:10.3f}   {gain:15.6f}   {required:34.6f}")


if __name__ == "__main__":
    main()
