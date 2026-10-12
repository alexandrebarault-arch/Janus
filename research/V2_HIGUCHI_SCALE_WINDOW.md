# V2 Higuchi scale window and late-growth burden

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `ANALYTIC_SCALING_CONSTRAINT`

## 1. Key identity

For the flat healthy branch, De Felice et al. define

`W = m^2 (1 + kappa y^2) J / (2 kappa y) - H^2`.

In the low-energy / pure-gravity limit they identify this as

`W = m_eff^2/2 - H^2`.

Therefore the linear Higuchi-safe regime requires

`m_eff^2 > 2 H^2`.

Reference: A. De Felice, A. E. Gumrukcuoglu, S. Mukohyama et al., JCAP 06 (2014) 037, especially the discussion around Eq. (3.28).

This is not the full generic-FLRW stability criterion, but it is an extremely useful scaling relation.

## 2. Relation to the desired Janus length scale

If the effective massive-spin-2 Compton length is

`lambda_g = c / m_eff`,

then

`m_eff/H0 = (c/H0)/lambda_g`.

For `H0 = 70 km/s/Mpc`, the Hubble length is about

`c/H0 = 4282.75 Mpc`.

The Janus-R motivation wants modifications on roughly void / cosmic-web scales, say `50-200 Mpc`.

That corresponds to

| `lambda_g` | `m_eff/H0` |
|---:|---:|
| 50 Mpc | 85.65 |
| 100 Mpc | 42.83 |
| 150 Mpc | 28.55 |
| 200 Mpc | 21.41 |

## 3. Matter-era healthy-regime crossing

Using the matter-era approximation

`H^2/H0^2 ~= Omega_m0 (1+z)^3`

with `Omega_m0=0.30`, the low-energy Higuchi threshold

`m_eff^2 = 2 H^2`

occurs at

`1+z_H ~= [ (m_eff/H0)^2 / (2 Omega_m0) ]^(1/3)`.

For the same length scales:

| `lambda_g` | approximate `z_H` |
|---:|---:|
| 50 Mpc | 22.04 |
| 100 Mpc | 13.51 |
| 150 Mpc | 10.08 |
| 200 Mpc | 8.14 |

### Interpretation

A massive mode light enough to act on void/cosmic-web scales is naturally in the regime `H >> m_eff` during the earlier Universe.

Therefore the nonlinear/Vainshtein early phase is **not optional** for the current JANUS-R strategy. The linearly healthy late regime only becomes available at redshifts of order `8-22` for the target length window.

This agrees qualitatively with the Aoki-Maeda-Namba result that nonlinear helicity-0 physics can be required to recover a healthy GR-like early Universe when `H > m_eff`.

## 4. Late linear growth is too weak to create order-unity segregation from a tiny seed

The maximally unscreened symmetric relative-mode toy growth derived in V1 is

`delta_rel ~ a^p`,

with

`p = (-1 + sqrt(33))/4 ~= 1.18614`.

If linear Janus-like growth only becomes available after `z_H`, the maximum toy growth to today is

`G_rel = (1+z_H)^p`.

| `lambda_g` | `z_H` | `G_rel` | final amplitude from `1e-5` seed |
|---:|---:|---:|---:|
| 50 Mpc | 22.04 | 41.31 | `4.1e-4` |
| 100 Mpc | 13.51 | 23.88 | `2.4e-4` |
| 150 Mpc | 10.08 | 17.33 | `1.7e-4` |
| 200 Mpc | 8.14 | 13.80 | `1.4e-4` |

Thus a primordial relative amplitude of order `1e-5` remains tiny even under this deliberately optimistic maximally-unscreened EdS estimate.

For a 100 Mpc scale, reaching a late relative amplitude of

- `0.1` requires roughly `delta_rel(z_H) ~ 4.2e-3`;
- `1` requires roughly `delta_rel(z_H) ~ 4.2e-2`.

The required seed at the nonlinear-to-linear transition is therefore percent/sub-percent scale, not primordial `1e-5` scale.

## 5. Core consequence

The surviving JANUS-R mechanism now has a very sharp burden:

> The early nonlinear phase must do more than merely hide a bad linear theory. It must either generate, preserve, or release a sizeable relative/isocurvature mode by `z ~ 8-22`.

If the nonlinear phase instead drives the two sectors onto an almost perfectly common GR-like attractor with a tiny relative mode, there is not enough late linear growth to create dramatic Janus-like segregation by today.

This is now one of the strongest falsification criteria in the project.

## 6. Relation to the nonlinear branch diagnostics

The Aoki-Maeda-Namba seventh-order scalar equation shows that real nonlinear branches exist and can connect early and late regimes for selected parameters (Case A).

But root existence does **not** answer the new key question:

`What relative density/velocity amplitude is dynamically present when the system exits the nonlinear phase?`

That requires a true time-dependent perturbation calculation, not only an algebraic adiabatic root tracker.

## 7. Decision

`VOID_SCALE_MASS_WINDOW = INTERNALLY_PLAUSIBLE`

`EARLY_NONLINEAR_PHASE = REQUIRED`

`TINY_PRIMORDIAL_RELATIVE_SEED + LATE_LINEAR_GROWTH = INSUFFICIENT`

`NONLINEAR_SEED_GENERATION_OR_PRESERVATION = NEXT_DECISIVE_GATE`

## 8. Reproducibility

The scaling calculations are implemented in

`numerics/higuchi_scale_window.py`

with regression tests in

`tests/test_higuchi_scale_window.py`.
