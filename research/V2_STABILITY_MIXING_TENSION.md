# V2 stability–mixing tension

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `MAJOR_CONSTRAINT__NOT_A_THEOREM`

## Executive result

The first exact healthy-branch stability diagnostic sharply changes the interpretation of the V2 FLRW background scan.

A background can reproduce Lambda-CDM-like `H(z)` extremely well and still fail the extended Higuchi/no-ghost condition almost immediately away from the present epoch.

Conversely, backgrounds that remain healthy to high redshift are readily found by moving toward the small-`alpha = M_f/M_g` GR-decoupling regime, but that same limit suppresses the visible massive spin-2 component which is needed for a strong Janus-like cross-sector signature.

This creates the present central tension:

> **early-time linear stability and strong visible-sector segregation tend to pull the theory in opposite directions.**

This is an exploratory numerical result plus an analytically expected decoupling trend, not yet a mathematical no-go theorem.

---

## 1. Exact healthy-branch quantity used

For flat FLRW on the healthy/dynamical branch, De Felice et al. define

`W = m^2 (1 + kappa y^2) J / (2 kappa y) - H^2`,

where

- `kappa = M_f^2/M_g^2 = alpha^2`,
- `y = a_f/a_g`,
- `J = beta1 + 2 beta2 y + beta3 y^2`.

The healthy branch requires `W > 0` (together with the other kinetic/gradient requirements). In the low-energy limit this reduces to the usual generalized Higuchi structure.

The implementation is in

`numerics/stability_mixing.py`.

The associated tests are in

`tests/test_stability_mixing.py`.

---

## 2. The original V2 background regression point fails

The first FLRW regression point was deliberately chosen only because it

- had `beta0 = 0`,
- had positive lapse in the background diagnostic,
- and matched flat Lambda-CDM expansion to sub-percent accuracy at low redshift.

Its parameters were

```
alpha = 0.6783820120
 y0   = 1.4009642017
beta1 = 2.8799123638
beta2 = 1.0433553613
beta3 = 0.4228370164
beta4 = 1.0561137605
m^2/H0^2 = 0.1081776935
```

At `z=0`, the exact flat-branch diagnostic gives

`W/H0^2 ~= +0.05913`.

But following the same continuous FLRW branch backwards, `W` crosses zero at only about

`z ~= 0.06`.

Representative values are approximately

- `z=1`: `W/H0^2 ~= -2.0`;
- `z=2`: `W/H0^2 ~= -7.7`;
- `z=10`: `W/H0^2 ~= -4e2`.

### Decision

`V2_BACKGROUND_REGRESSION_POINT = REJECTED_AS_LINEARLY_HEALTHY_CANDIDATE`.

It remains useful as a regression test for the background solver and as a demonstration that `H(z)` alone is a weak discriminator.

This is a significant correction to the earlier preliminary optimism about that point.

---

## 3. Why small alpha helps

The positive interaction contribution to `W` contains the factor

`1 / (alpha^2 y)`

at small `alpha`.

Therefore decreasing `alpha` can push the generalized Higuchi violation to much earlier epochs, provided the interaction coefficients and background solution remain regular.

This behavior is consistent with the known small-Planck-mass-ratio GR limit of bimetric cosmology: as the second Planck mass becomes small in the relevant convention, the visible metric aligns increasingly with the massless graviton and the massive mode decouples from ordinary visible matter.

That is simultaneously good for stability/observational viability and bad for a large Janus-like visible-sector effect.

---

## 4. Mixing proxy

For proportional backgrounds the mass eigenstate rotation is controlled by the dimensionless combination `alpha*y`.

For scan diagnostics only, define

`epsilon_mix = (alpha*y)^2 / [1 + (alpha*y)^2]`.

This is **not** an observable and is not the exact generic-FLRW coupling coefficient. It is simply a bounded indicator of distance from the small-alpha decoupling limit:

- `epsilon_mix -> 0`: visible metric almost purely massless/GR-like;
- `epsilon_mix ~ O(1)`: substantial massless/massive mixing is possible.

Any final claim must replace this proxy with the actual transfer-function response.

---

## 5. Exploratory scan with moderate interaction coefficients

A random scan was performed over approximately 12,000 calibrated background points with

- `0.03 <= alpha <= 1`,
- positive present twin dust density,
- `beta0 = 0`,
- `|beta_n| <= 100` after calibration,
- low-redshift expansion RMS error `< 1%` relative to flat Lambda-CDM over roughly `0 <= z <= 2`,
- continuous positive `y(a)` branch.

This is not a statistical posterior and the prior is not physically unique. It is a stress test for the stability/mixing tradeoff.

Among the accepted low-redshift backgrounds, the largest present mixing proxy found subject to increasingly early `W>0` continuity was approximately:

| healthy at least to | max `epsilon_mix` found | interpretation |
|---:|---:|---|
| `z >= 1` | `~0.56` | strong mixing still possible very late |
| `z >= 5` | `~0.23` | substantial mixing possible |
| `z >= 10` | `~0.021` | only few-percent proxy |
| `z >= 20` | `~0.0055` | sub-percent proxy |
| `z >= 50` | `~8.7e-4` | near decoupling |
| `z >= 100` | `~2.5e-4` | strong GR-limit tendency |

A second scan allowing coefficients up to about `|beta_n| <= 1000` changed details but not the qualitative trend. Representative maxima were approximately

- `z >= 10`: `epsilon_mix ~ 0.028`;
- `z >= 50`: `~0.0018`;
- `z >= 100`: `~4.4e-4`.

No claim is made that these are global optima.

### Interpretation

The scan supports the qualitative expectation:

`earlier linear health  ->  smaller visible massive-mode mixing proxy`.

It does **not** prove that no tuned finite-alpha solution exists.

---

## 6. Extreme small-alpha solutions exist, but illustrate the problem

Allowing `alpha` to become extremely small readily produces branches with

- `W > 0` to very high redshift,
- an almost exact Lambda-CDM expansion history despite `beta0=0`,
- sometimes large mutually cancelling interaction coefficients.

An example scan point had roughly

`alpha ~ 1e-7`,

with `epsilon_mix` of order `1e-15` to `1e-16`.

Such a solution is useful as an existence proof for a healthy-looking background, but it is essentially useless for the original Janus goal if the visible massive-mode interference is suppressed at the same level.

This is the core no-free-lunch problem.

---

## 7. What nonlinear screening can still change

The result above concerns the **linear healthy-branch criterion**.

Aoki–Maeda–Namba showed that in bimetric cosmology the early regime `H >> m_eff` can be governed by nonlinear helicity-0/Vainshtein physics and that suitable nonlinear solutions can cure instabilities visible in the naive linear expansion.

Therefore failure of linear `W>0` at high redshift is not automatically a complete theory-level death sentence.

However, this makes the burden stronger, not weaker:

- the nonlinear branch must be regular;
- it must connect continuously to the late healthy branch;
- it must reproduce early GR-like cosmology;
- and it must somehow generate or preserve enough relative/twin-sector structure to produce the desired late Janus-like effect.

A model that invokes nonlinear screening merely to erase every observable massive-mode effect has again collapsed back toward GR.

---

## 8. Current decision

`JANUS_R_LINEAR_STRONG_SEGREGATION = SEVERELY_CONSTRAINED`

`JANUS_R_NONLINEAR_GENERATION = STILL_OPEN`

The main research target is no longer simply "find a smooth FLRW branch".

It is now:

> Find a branch that passes either the full linear healthy conditions or a demonstrably regular nonlinear early phase **without** suppressing the late visible massive-mode response to irrelevance.

If no such overlap exists, JANUS-R fails as a meaningful continuation of Petit's segregation mechanism even though ghost-free bimetric cosmology itself remains viable in its GR-like limit.
