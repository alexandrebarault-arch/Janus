# Cross-sector lensing: direct derivation

Date: 2026-10-11

Status: `RESULT_LINEAR_FLAT_BACKGROUND`

Scope: linear weak-field ghost-free bimetric gravity with two separately coupled matter sectors, around proportional Minkowski backgrounds. This is **not** yet a cosmological or Vainshtein-screened result.

## Question

If an `f`-sector point mass repels a slow `g`-sector test mass in the short-distance linear regime, does it also act as a divergent (negative) gravitational lens for `g`-sector photons?

## Input

Using the PPN solution of Manuel Hohmann, arXiv:1701.07700 / Phys. Rev. D 95, 124049 (2017), the cross-sector Newtonian coefficient is

`alpha_gf(r) = [3 - 4 exp(-mu r)] / [24 pi (m_g^2 + m_f^2)]`.

Hence slow visible matter is repelled when

`mu r < ln(4/3)`.

The spatial metric also contains `gamma_gf(r)` and an anisotropic `theta_gf(r) x_i x_j/r^3` term. It is therefore incorrect to infer photon deflection from the sign of `alpha_gf` alone.

## Direct null-ray derivation

For an unperturbed photon moving along the `z` direction with impact parameter `b`, the first-order transverse deflection is

`Delta theta_b = (1/2) d/db integral_{-infinity}^{infinity} [h_00 + h_zz] dz`.

Substituting the full Hohmann PPN metric, including the `theta_gf` anisotropic term, the line-of-sight combination simplifies after integration to the difference between a massless and a massive spin-2 kernel.

With `u = mu b`, the cross-sector deflection is

`Delta theta_gf(b) = - C * M_f/b * [1 - u K_1(u)]`,

where `C > 0` is the positive mixing normalization (for Hohmann's rescaled variables, `C = 1/[2 pi (m_g^2 + m_f^2)]`) and `K_1` is the modified Bessel function of the second kind.

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

This remains true even in the radius range where `alpha_gf < 0` and slow visible matter is repelled.

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
| 1.00 | -4.7771132 |
| 2.00 | -8.6432188 |
| 10.0 | -11.9977621 |

The sign never reverses.

## Scientific consequence

This is a major difference from a literal negative-mass interpretation of Janus:

- slow `g` matter can be repelled by an `f` source;
- `g` photons do **not** become negatively lensed by that same source in this linear ghost-free bimetric mechanism;
- at short distance the cross-sector lensing tends to cancellation rather than sign reversal.

Therefore `JANUS-R` must not claim Petit's negative-lensing prediction.

Instead, a potentially distinctive observable is a **dynamical-lensing mismatch**: the sign/amplitude inferred from motions of slow tracers need not match the lensing mass inferred from photons.

## Limitation / next step

The theorem above is valid for the linearized proportional-Minkowski PPN solution. Cosmic voids require a cosmological background and may involve nonlinear screening. The next gate is to derive the cosmological scalar response (`Psi_g`, `Phi_g`) to an `f`-sector density perturbation and determine whether the no-negative-lensing sign property survives on FLRW backgrounds and across screening transitions.
