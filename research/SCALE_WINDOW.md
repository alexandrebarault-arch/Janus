# Candidate scale window for JANUS-R Late

Date: 2026-10-11

Status: `ORDER_OF_MAGNITUDE_GATE`

This note identifies a physically interesting scale window. It is **not** a fitted parameter result for the two-matter JANUS-R theory.

## 1. Current external benchmark

A 2025 analysis of standard (single-visible-matter-sector) bimetric cosmology using DESI DR2 BAO + CMB + SNe reports

`m_FP > 3.0e-32 eV` at 68% credibility,

with `H0 = 69.0 +/- 0.4 km/s/Mpc`.

Source: Högås & Mörtsell, arXiv:2507.03743.

This constraint **cannot be copied directly** to JANUS-R, because JANUS-R contains an additional separately coupled matter sector. It is used here only to identify a scale already encountered in an observationally studied ghost-free bimetric theory.

## 2. Convert the mass to cosmological scales

For `H0 = 69 km/s/Mpc`,

`hbar H0 = 1.47185e-33 eV`,

and

`c/H0 = 4344.82 Mpc`.

Define

`q = m_FP / (hbar H0)`.

For `m_FP = 3e-32 eV`,

`q = 20.38`.

The reduced Compton length is

`lambda = hbar c / m_FP = (c/H0)/q ~= 213.2 Mpc`.

## 3. Correct physical cross-force radius

For the equal-Planck-mass linear point-source solution, the cross potential is proportional to

`[1 - (4/3) exp(-r/lambda)] / r`.

The physical force changes sign when

`4 (1 + u) exp(-u) = 3`, `u = r/lambda`.

The positive root is

`u_force = 0.9612787631`.

Therefore, if the linear unscreened solution applies,

`r_repulsive ~= 0.9613 lambda`.

At `m_FP = 3e-32 eV`,

`r_repulsive ~= 205 Mpc`.

This is an important correction to the smaller radius obtained by looking only at the zero of the position-dependent potential coefficient (`ln(4/3) lambda ~= 61 Mpc`).

## 4. Cosmological transition proxy

Aoki-Maeda-Namba show that when `H >> m_eff`, nonlinear helicity-0 effects can restore a GR-like stable early-Universe regime for suitable bimetric parameters. It is therefore useful to ask when `H ~ m_FP` would occur.

Using flat Lambda-CDM only as an order-of-magnitude clock,

`H(z)/H0 = sqrt[Omega_m (1+z)^3 + Omega_Lambda]`,

with `Omega_m=0.3`, `Omega_Lambda=0.7`, the equation `H(z)=q H0` gives

`1+z = [(q^2 - Omega_Lambda)/Omega_m]^(1/3)`.

Representative values:

| `q=m/H0` | `lambda=c/m` | proxy `z(H=m)` | point-force repulsive radius `0.961 lambda` |
|---:|---:|---:|---:|
| 10 | 434 Mpc | 5.92 | 418 Mpc |
| 20 | 217 Mpc | 10.00 | 209 Mpc |
| 20.38 | 213 Mpc | 10.14 | 205 Mpc |
| 30 | 145 Mpc | 13.42 | 139 Mpc |
| 50 | 86.9 Mpc | 19.27 | 83.5 Mpc |
| 100 | 43.4 Mpc | 31.18 | 41.8 Mpc |

Hence a mass scale `m/H0 ~ 20-50` naturally places the free linear crossover on `~80-200 Mpc` scales and the crude `H~m` transition after recombination but before the low-redshift Universe.

This is unusually well aligned with large-void / supervoid / cosmic-web scales.

## 5. But the scale match does not prove segregation

The linear relative-sector growth enhancement is modest. In the maximally unscreened equal-density toy limit,

`delta_relative ~ a^1.186`,

while the common mode grows as

`delta_common ~ a`.

If unscreening began around the proxy transition:

- `q=20`, `z~10`: relative/common advantage to today is only `~1.56`;
- `q=50`, `z~19`: advantage is only `~1.75`.

Thus this mechanism is much more credible as a **late modification of void dynamics** than as a mechanism that creates the entire cosmic web from essentially zero initial relative-sector perturbations.

## 6. Vainshtein scaling for a cosmic density contrast

As an order-of-magnitude diagnostic, use

`r_V ~ (r_g lambda^2)^(1/3)`

with

`r_g = 2 G |Delta M|/c^2`.

For a spherical region of radius `R` and density contrast `delta` relative to the cosmic mean,

`|Delta M| = (4 pi/3) rho_m |delta| R^3`,

which gives approximately

`r_V/R ~ [Omega_m |delta| / q^2]^(1/3)`

(up to model-dependent order-unity and coupling factors).

For a deep void with `|delta|=0.8` and `q=20.38`,

`r_V/R ~= 0.083`.

So for a `50 Mpc` void the crude source-based Vainshtein scale is only `~4 Mpc`, suggesting that most of the void volume could lie outside its own screened core.

**Caution:** this is only a scaling estimate. Bimetric Vainshtein solutions depend strongly on the interaction parameters, background branch and sign of the density contrast. It must not be promoted to a prediction before solving the nonlinear spherical equations.

## 7. Current interpretation

The scale coincidence is sufficiently good to justify continuing JANUS-R Late:

- early Universe: potentially nonlinear/GR-like when `H >> m_eff`;
- dense local objects: Vainshtein screened;
- large low-density voids: plausible unscreened laboratory;
- characteristic interaction length: tens to hundreds of Mpc;
- strongest expected signature: velocity/dynamics versus weak-lensing mismatch, not negative lensing by an isolated positive-energy `f` mass.

## Gate

`SCALE_WINDOW = PLAUSIBLE_BUT_NOT_VALIDATED`

The project now requires a nonlinear spherical void solution on an FLRW background. If no healthy branch connects the screened interior/environment to the unscreened cosmological solution, JANUS-R Late fails regardless of the attractive scale coincidence.
