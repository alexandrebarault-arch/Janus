# Segregation gate — can JANUS-R create a Janus-like anti-correlation?

Date: 2026-10-11

Status: `STRONG_NEGATIVE_RESULT_IN_LINEAR_HOMOTHETIC_REGIME__NONLINEAR_TRANSITION_REMAINS_OPEN`

## Core question

The original Janus intuition requires more than a modified force law. It requires a macroscopic state in which ordinary and opposite/twin sectors become spatially anti-correlated — schematically:

`visible overdensity <-> twin underdensity`

and

`visible void <-> twin overdensity`.

JANUS-R must therefore explain **how this relative mode is generated from cosmological initial conditions**, not simply assume the final anti-correlated configuration.

## What early nonlinear screening does

Aoki, Maeda & Namba (2015) showed that nonlinear helicity-0/Stueckelberg effects can restore a GR-like early phase in bigravity for suitable interaction parameters.

Lüben, Schmidt-May & Smirnov (2020) strengthened the cosmological interpretation: the early universe is Vainshtein screened and the massive/massless sectors effectively decouple above the spin-2 scale.

This is valuable for stability, but it has an important consequence for Janus-like segregation:

**a GR-like screened early phase does not automatically manufacture a large relative twin perturbation.**

If primordial initial conditions are nearly adiabatic, the two sectors enter the later modified regime with a small relative/isocurvature component unless some additional mechanism excites it during the transition.

Sources:

- https://arxiv.org/abs/1506.04543
- https://arxiv.org/abs/1912.09449

## Reference linear-growth diagnostic

The repository includes `numerics/segregation_growth_bound.py`.

For a transparent equal-mixing Einstein-de-Sitter proxy, take the common mode to feel ordinary GR strength (`lambda_common=1`) and the maximally modified relative mode to feel `lambda_relative=4/3`.

Then

`delta ~ a^p`,

with

`p(lambda) = [-1 + sqrt(1+24 lambda)]/4`.

Thus

`p_common = 1`,

`p_relative = (-1+sqrt(33))/4 ~= 1.18614`.

The relative/common ratio therefore grows only as

`a^0.18614`.

Representative differential gains from a transition redshift `z_t` to today are:

| z_t | relative/common gain | initial relative/common ratio required to exceed unity today |
|---:|---:|---:|
| 1.822 | 1.21 | 0.824 |
| 10 | 1.56 | 0.640 |
| 35.7 | 1.96 | 0.511 |
| 54 | 2.11 | 0.474 |
| 100 | 2.36 | 0.424 |
| 142.4 | 2.52 | 0.397 |
| 1100 | 3.68 | 0.272 |

To obtain opposite signs in the two sector contrasts from

`delta_g=(delta_common+delta_relative)/2`,

`delta_f=(delta_common-delta_relative)/2`,

one needs

`|delta_relative| > |delta_common|`.

Therefore, in this reference linear regime, even a transition as early as Candidate C's `z~142` requires an already very large relative component (~40% of the common mode) at handoff.

## Direct independent check: Aoki–Maeda 2014

Aoki & Maeda's explicit twin-matter structure-formation calculation provides a remarkably strong cross-check of the proxy above.

Their Eq. (4.34) for the relative/massive density mode contains an effective source strength

`lambda_rel(k,a) = 4 (k^2/a^2) / [3 (k^2/a^2 + m_eff^2)]`.

Therefore, well **inside** the massive-graviton Compton wavelength,

`k/a >> m_eff`,

one gets

`lambda_rel -> 4/3`,

which gives exactly the analytic asymptotic growth index

`p_rel = (-1+sqrt(33))/4 ~= 1.18614`.

Aoki & Maeda numerically report

`delta_- ~ a^1.176`

for their corresponding case (b), in excellent agreement with the analytic limiting estimate. They find much slower growth in the opposite long-wavelength regime.

This means the modest relative-mode enhancement used here is not an arbitrary toy assumption: it is the short-scale asymptote of the explicit published two-twin-matter perturbation equations in the homothetic matter-era model.

### Crucial initial-condition fact

For the numerical example in which the visible perturbation changes sign under twin-matter repulsion, Aoki & Maeda impose at decoupling

`delta_g = 10^-5`,

but

`delta_f = 10^-1`.

Thus the twin-sector perturbation is **10,000 times larger** than the visible perturbation at the starting epoch.

Their calculation demonstrates that a large pre-existing twin perturbation can strongly affect and even reverse the visible perturbation while the physical scale lies inside the Compton wavelength. It does **not** demonstrate spontaneous generation of that enormous relative mode from adiabatic or near-adiabatic initial conditions.

This is a major distinction for JANUS-R.

Reference: Aoki & Maeda, Phys. Rev. D 90, 124089 (2014), arXiv:1409.0202, especially Eqs. (4.34), (4.46) and Fig. 4.

## Important limitation

The reference result is **not a general no-go theorem** for Candidate C.

Candidate C has `alpha != 1`, a nontrivial time-dependent mixing, unequal background densities and a nonlinear transition. Its exact coupled transfer matrix could differ substantially from the simple homothetic/equal-reference regime.

The strengthened conclusion is nevertheless clear:

**ordinary linear repulsive growth in the published twin-matter model is too mild to be assumed capable of creating Janus segregation from tiny adiabatic seeds.**

Any successful model must demonstrate one of the following explicitly:

1. a much stronger relative eigenmode in the exact Candidate-C transfer matrix;
2. nonlinear production/amplification of the relative mode during the GR-to-bigravity transition;
3. a primordial twin-sector isocurvature mode of substantial amplitude;
4. a different architecture/coupling that changes the conclusion.

## CMB/isocurvature pressure

Planck 2018 strongly supports near-adiabatic primordial fluctuations. In standard mixed adiabatic+CDM-isocurvature analyses, the non-adiabatic contribution to CMB temperature variance is constrained at the percent level. In the standard fully correlated or fully anticorrelated CDI cases, the allowed primordial isocurvature fraction is around the `10^-3` level.

These numerical Planck limits **cannot be copied directly** onto a hidden `f` sector with different metric coupling. A dedicated JANUS-R Boltzmann calculation is required.

Nevertheless, they make a primordial `O(0.3-0.8)` relative mode — and especially an illustrative `delta_f/delta_g=10^4` hierarchy — a serious observational issue rather than a harmless free initial condition.

Reference: Planck 2018 results X, A&A 641 A10 (2020).

## Why Aoki–Maeda's dark-matter success is a different regime

Their dark-matter construction assumes the massive-graviton Compton wavelength is **shorter than galactic scale**, with representative `m_eff^-1 ~ 1 kpc`.

Beyond that short Compton scale the twin sector becomes effectively attractive and behaves as dark matter. Inside the Compton scale it is repulsive.

JANUS-R Late asks for nearly the opposite phenomenological window: a cross-sector relative/repulsive effect that remains important over large void/cosmic-web scales (`~100 Mpc`).

Thus Aoki–Maeda prove that twin-sector dynamics can be rich, but their successful dark-matter regime does not establish the long-range Janus segregation mechanism.

## Nonlinear loophole

Aoki-Maeda-Namba's nonlinear scalar equation contains the relative source combination

`kappa_g^2 rho_g delta_g - K^2 kappa_f^2 rho_f delta_f`.

A visible underdensity plus a twin overdensity reinforces this source, so **once anti-correlation exists**, nonlinear bigravity responds strongly to it.

What remains unproven is the causal direction we actually need:

> Can the healthy cosmological transition *generate* the large anti-correlated mode from realistic initial conditions?

Högås, Torsello & Mörtsell (2020) show that homogeneous spherical overdensities can evolve nonlinearly without the exponential catastrophe suggested by standard linear perturbation theory. Lüben et al. (2020) give a cosmological Vainshtein interpretation of the early screened era. Bassi et al. (2023) nevertheless note that the detailed transition relevant to perturbations remains unsettled.

So nonlinear physics keeps a loophole open, but it is not evidence that the needed anti-correlation is generated.

## Current scientific verdict

`SPONTANEOUS_SEGREGATION_FROM_NEAR_ADIABATIC_INITIAL_CONDITIONS = NOT_DEMONSTRATED`

`PUBLISHED_LINEAR_TWIN_MATTER_REPULSIVE_GROWTH = TOO_MILD_WITHOUT_LARGE_RELATIVE_INITIAL_MODE`

`AOKI_2014_SIGN_FLIP_EXAMPLE = REQUIRES_DELTA_F/DELTA_G = 10^4_AT_DECOUPLING`

`NONLINEAR_TRANSITION = PRINCIPAL_REMAINING_LOOPHOLE`

This is now more important than further tuning of the homogeneous background.

## Next decisive calculation

Gate 2 should focus on the exact two-matter scalar transfer matrix for Candidate C (or nearby parameter points), initialized with separately controlled adiabatic and relative/isocurvature modes.

Required outputs:

- largest relative-mode growth eigenvalue versus `k,z`;
- conversion between common and relative modes;
- minimum primordial `f`-sector isocurvature needed to reach `delta_g delta_f < 0` on 20–200 Mpc scales;
- Weyl potential and visible velocity response for the same mode;
- CMB sensitivity of that initial relative component.

If the exact transfer system still requires an order-tens-of-percent primordial relative mode, JANUS-R's spontaneous-segregation interpretation should be downgraded sharply unless a nonlinear transition calculation demonstrably creates it.
