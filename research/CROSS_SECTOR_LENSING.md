# Cross-sector lensing and force: direct derivation

Date: 2026-10-11

Status: `RESULT_LINEAR_FLAT_BACKGROUND`

Scope: linear weak-field ghost-free bimetric gravity with two separately coupled matter sectors, around proportional Minkowski backgrounds. This is **not** yet a cosmological or Vainshtein-screened result.

## Question

If an `f`-sector point mass repels a slow `g`-sector test mass in the short-distance linear regime, does it also act as a divergent (negative) gravitational lens for `g`-sector photons?

## Input: Hohmann point-source solution

Using the PPN solution of Manuel Hohmann, arXiv:1701.07700 / Phys. Rev. D 95, 124049 (2017), the cross-sector coefficient multiplying the Newtonian `1/r` potential is

`alpha_gf(r) = [3 - 4 exp(-mu r)] / [24 pi (m_g^2 + m_f^2)]`

in the author's general rescaled notation (with the equal-Planck-mass specialization differing only by the corresponding overall normalization).

Hohmann notes that this coefficient becomes negative for

`mu r < ln(4/3) ~= 0.287682`

and interprets this as a repulsive regime.

### Important correction: potential-sign threshold != force-sign threshold

Because `alpha_gf` depends on radius, the physical acceleration is obtained by differentiating the full potential, not by inspecting `alpha_gf` alone.

Up to a positive normalization, the cross Newtonian potential is

`U_gf(r) ~ [1 - (4/3) exp(-mu r)] / r`.

The slow-particle radial acceleration is proportional to

`dU_gf/dr ~ -[1 - (4/3)(1 + u) exp(-u)]/r^2`,

where `u = mu r` and an inward/attractive acceleration corresponds to the usual positive long-range Newton coupling.

Therefore the actual cross force is **repulsive** when

`1 - (4/3)(1 + u) exp(-u) < 0`,

or equivalently

`4(1 + u) exp(-u) > 3`.

The unique positive root is

`u_force = 0.9612787631...`.

Thus the physical point-particle force remains repulsive out to

`r < 0.96128 / mu`,

which is substantially farther than the radius `ln(4/3)/mu` at which the potential itself changes sign.

This distinction follows directly from differentiating Hohmann's radius-dependent cross potential and is retained in JANUS-R as a correction to the shorthand interpretation based only on the position-dependent PPN coefficient.

## Photon metric is not determined by `alpha_gf` alone

The spatial metric also contains `gamma_gf(r)` and an anisotropic `theta_gf(r) x_i x_j/r^3` term. It is therefore incorrect to infer photon deflection from either the sign of the potential or the sign of the slow-particle force alone.

## Direct null-ray derivation

For an unperturbed photon moving along the `z` direction with impact parameter `b`, the first-order transverse deflection is

`Delta theta_b = (1/2) d/db integral_{-infinity}^{infinity} [h_00 + h_zz] dz`.

Substituting the full Hohmann PPN metric, including the `theta_gf` anisotropic term, the line-of-sight combination simplifies after integration to the difference between a massless and a massive spin-2 kernel.

With `u = mu b`, the cross-sector deflection is

`Delta theta_gf(b) = - C * M_f/b * [1 - u K_1(u)]`,

where `C > 0` is the positive mixing normalization and `K_1` is the modified Bessel function of the second kind.

The sign convention here takes negative transverse deflection to mean bending toward a positive source located at the origin.

## Sign theorem

For `u > 0`,

`d/du [u K_1(u)] = -u K_0(u) < 0`,

and

`lim_{u -> 0+} u K_1(u) = 1`,

`lim_{u -> infinity} u K_1(u) = 0`.

Therefore

`0 < 1 - u K_1(u) < 1`

for every finite `u > 0`.

Hence

**the cross-sector photon deflection is never divergent in this linear solution.**

It interpolates between:

- `Delta theta_gf -> 0` as `mu b -> 0`;
- ordinary convergent/attractive lensing as `mu b -> infinity`.

This remains true throughout the larger physical-force repulsive range `mu r < 0.96128`.

## Independent physical check

The same result follows from the spin-2 propagator structure.

A cross-sector source excites a difference of massless and massive spin-2 propagators. For a photon, the stress tensor is traceless, so the helicity-0 trace coupling that gives the well-known `4/3` enhancement of the massive mode in the nonrelativistic force is absent. The photon therefore samples schematically

`1/k^2 - 1/(k^2 + mu^2)`

rather than the slow-matter combination whose massive contribution carries the `4/3` factor.

Fourier transforming gives the lensing kernel

`(1 - exp(-mu r))/r`,

which is non-negative and vanishes as `r -> 0`. Projecting along the line of sight yields exactly the Bessel factor above.

## Numerical cross-check

The full PPN metric was integrated numerically before simplifying analytically. For equal Planck masses the dimensionless deflection coefficient agrees with

`-12 [1 - u K_1(u)]`

(to numerical integration precision) for tested values from `u = 0.01` to `u = 10`.

Examples:

| `u = mu b` | dimensionless deflection |
|---:|---:|
| 0.01 | -0.0031327 |
| 0.10 | -0.1753863 |
| 0.28768 | -0.9379823 |
| 0.50 | -2.0613533 |
| 0.96128 | -4.5798769 |
| 1.00 | -4.7771132 |
| 2.00 | -8.6432188 |
| 10.0 | -11.9977621 |

The sign never reverses.

## Scientific consequence

This is a major difference from a literal negative-mass interpretation of Janus:

- slow `g` matter can be repelled by an `f` source;
- `g` photons do **not** become negatively lensed by that same source in this linear ghost-free bimetric mechanism;
- at short distance the cross-sector lensing tends to cancellation rather than sign reversal;
- the physical repulsive-force range is wider than suggested by the zero of the radius-dependent potential coefficient.

Therefore `JANUS-R` must not claim Petit's negative-lensing prediction.

Instead, a potentially distinctive observable is a **dynamical-lensing mismatch**: the sign/amplitude inferred from motions of slow tracers need not match the lensing mass inferred from photons.

## Limitation / next step

The theorem above is valid for the linearized proportional-Minkowski PPN solution. Cosmic voids require a cosmological background and may involve nonlinear screening. The next gate is to derive the cosmological scalar response (`Psi_g`, `Phi_g`) to an `f`-sector density perturbation and determine whether the no-negative-lensing sign property survives on FLRW backgrounds and across screening transitions.
