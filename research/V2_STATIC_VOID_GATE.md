# V2 localized static void gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `STRONG_GRADIENT_TRANSITION_REQUIRED_FOR_JANUS_LIKE_VOID`

Primary source: Aoki, Maeda & Namba (2015), Appendix A, arXiv:1506.04543.

## Motivation

The globally nonlinear Case-A branch is not a satisfactory homogeneous late Universe. The best remaining architecture is therefore a localized nonlinear patch around a structure, matched to an asymptotically homothetic exterior:

`mu(R) -> 0` as `R -> infinity`.

A cosmic void with a twin-sector overdensity is represented as a perturbation around the homogeneous background:

- visible perturbation mass `M_g < 0`;
- twin perturbation mass `M_f > 0`.

No fundamental negative matter mass is introduced. The negative sign is only the integrated visible **density deficit** relative to the background.

Define

`q = K^2 G_f M_f / (G_g M_g)`.

A Janus-like anti-correlated configuration therefore has `q < 0`.

## Static equation

The new module

`numerics/static_void_transition.py`

specializes Eq. (A13) of Aoki-Maeda-Namba to the exterior of spherical perturbations. Tests are in

`tests/test_static_void_transition.py`.

A local RED/GREEN TDD cycle was performed:

- before implementation: import failed as expected;
- after implementation: `3 passed`.

## Double-root endpoint

For the published Case-A interaction parameters

`beta2=-3`, `beta3=3`, `m_g^2=m_f^2=0.5`, `Lambda_g=0`,

the asymptotically homothetic root connected to `mu=0` terminates at a double root when one moves inward through an anti-correlated perturbation.

For equal weighted perturbation magnitudes (`q=-1`) the endpoint is

`mu_critical ~= 0.11223734`,

`source_g,critical ~= -0.22971182`

in the code normalization.

Using the Aoki-Maeda-Namba Vainshtein radius

`R_V^3 = 2 |G_g M_g - K^2 G_f M_f| / (3 m_eff^2)`

for `Lambda_g=0`, and `m_eff^2=m_g^2+m_f^2`, the endpoint occurs at

`R_critical / R_V ~= 2.69573`.

## Robustness across anti-correlation amplitude

The endpoint radius is remarkably insensitive to the weighted twin/visible perturbation ratio in this Case-A diagnostic:

| q | R_critical / R_V |
|---:|---:|
| -0.01 | ~2.725 |
| -0.03 | ~2.724 |
| -0.10 | ~2.720 |
| -0.30 | ~2.712 |
| -1 | ~2.696 |
| -3 | ~2.680 |
| -10 | ~2.669 |

This near-universality suggests that the branch loss is tied to the nonlinear scalar structure itself rather than to one fine-tuned mass ratio.

## Meaning of the endpoint

This result must **not** be stated as "the physical solution ends at 2.7 R_V".

Aoki-Maeda-Namba explicitly warn that when the derivative of the algebraic root diverges near a branch transition, the assumption of negligible Stueckelberg gradients breaks down. Terms such as `R mu' Phi_g` must then be retained.

Therefore the correct conclusion is:

`SMOOTH_ALGEBRAIC_MATCHING_TO_MU=0 = FAILS_AROUND_2.7_RV`

while

`FULL_GRADIENT_RESOLVED_MATCHING = OPEN`.

The theory is forcing a **strong-gradient transition layer** before the conventional Vainshtein radius is reached.

## Relation to a cosmological void size

For a spherical visible density contrast at `z~0`, Eq. (A22) gives approximately

`(R_V/R_void)^3 = Omega_m |delta_g| |1-q| / [3 (m_eff/H0)^2]`.

For an illustrative deep void

`Omega_m=0.3`, `delta_g=-0.8`, `q=-1`,

we obtain:

- `m_eff/H0 = 1` -> `R_V/R_void ~= 0.543`, hence `2.7 R_V ~= 1.47 R_void`;
- `m_eff/H0 = 1.5` -> `R_V/R_void ~= 0.414`, hence `2.7 R_V ~= 1.12 R_void`;
- `m_eff/H0 = 3` -> `R_V/R_void ~= 0.261`, hence `2.7 R_V ~= 0.70 R_void`.

Thus for a cosmological spin-2 mass of order a few Hubble scales, the required strong-gradient transition can naturally fall **near the void radius / compensation wall**.

This is potentially distinctive, but it can be interpreted in two opposite ways:

1. **positive possibility:** a gradient-resolved transition could generate a sharp, observable dynamical feature near void walls while preserving a homogeneous exterior;
2. **negative possibility:** no regular stable solution exists once the neglected gradients are restored.

The algebraic calculation cannot choose between them.

## Key correction relative to positive-mass source figures

Aoki-Maeda-Namba's Appendix figures mostly discuss positive localized `M_g` and `M_f`. A Janus-like cosmic void is different because `M_g` is a **negative perturbation mass** relative to the background. It is therefore essential to use `q<0` and the correct sign of `source_g`; simply reading their positive-mass ratio plots is not sufficient.

## New main gate

The highest-value next calculation is now a **gradient-resolved spherical boundary-value problem** that solves for `mu(R)` and the metric potentials through the transition layer with

- regular interior;
- visible underdensity + twin overdensity source;
- `mu -> 0` at large radius;
- no-ghost and no-gradient conditions;
- resulting visible peculiar acceleration and Weyl/lensing potential.

If no regular stable matching exists for physically relevant void parameters, the localized JANUS-R escape route fails.
