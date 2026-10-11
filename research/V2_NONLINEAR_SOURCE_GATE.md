# V2 nonlinear anti-correlated source gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `NONLINEAR_ESCAPE_EXISTS_FOR_SOME_PARAMETERS__NOT_YET_DYNAMICAL_PROOF`

## Question

The linear V2 scan exposes a stability–mixing tension: the easiest way to obtain an early healthy branch is to approach the small-`alpha` GR-decoupling regime, but this suppresses the visible massive spin-2 response required for a strong Janus-like segregation signal.

The remaining credible escape is nonlinear generation/amplification of the relative mode.

This note tests the first necessary condition:

> Does the Aoki–Maeda–Namba nonlinear scalar branch remain real and continuously connected when a Janus-like anti-correlated source is increased?

This is **not** yet a full time-dependent proof.

---

## Diagnostic

The repository already implements the seventh-order scalar equation of Aoki, Maeda & Namba (2015) in

`numerics/aoki_scalar_polynomial.py`.

A new continuation diagnostic is in

`numerics/nonlinear_source_continuation.py`.

Tests are in

`tests/test_nonlinear_source_continuation.py`.

At fixed `H^2`, the source is varied as

`source_g = -s`,

`source_f = +s`,

which has the sign structure of a visible underdensity plus a twin-sector overdensity.

The code follows the real scalar root continuously connected to a chosen branch. A sudden loss of a nearby real root is flagged as a branch endpoint/merger candidate.

The finite-step criterion is only a numerical topology diagnostic. A true physical singularity requires refinement and the full dynamical equations.

---

## Case A: robust connected nonlinear branch

For the published Case A interaction parameters

`beta2 = -3`,

`beta3 = +3`,

with

`m_g^2 = m_f^2 = 0.5`,

and at the illustrative late value

`H^2 = 0.01`,

the zero-source nonlinear root is near

`mu ~= 0.6921`.

Increasing the anti-correlated source continuously to at least

`s = 5`

does **not** destroy the connected real branch in this diagnostic.

As the source grows the scalar root shifts smoothly rather than running into an immediate root merger.

### Result

`CASE_A_ANTI_CORRELATED_SOURCE_CONTINUITY = PASS_IN_THIS_ALGEBRAIC_GATE`.

This establishes that a strong relative source does not generically force the nonlinear scalar equation to become complex or disconnected.

It does **not** establish kinetic/gradient stability or actual density amplification.

---

## Case B: finite source endpoint

For the published Case B interaction parameters

`beta2 = -1`,

`beta3 = +0.5`,

with the same illustrative

`m_g^2 = m_f^2 = 0.5`, `H^2 = 0.01`,

start from the late linear root

`mu = 0`.

Under the same anti-correlated source continuation, the connected root terminates/merges at approximately

`s ~= 0.476`

in the finite-step diagnostic.

Refining the source step from `1e-2` to `1e-4` places the endpoint near `0.4757`.

### Result

`CASE_B_ANTI_CORRELATED_SOURCE_CONTINUITY = FAIL_BEYOND_FINITE_SOURCE`.

This reproduces the qualitative branch-risk emphasized by Aoki–Maeda–Namba: nonlinear roots can merge and disappear as the matter/source configuration changes.

---

## Scientific interpretation

The nonlinear escape route is therefore neither automatically dead nor automatically safe.

The useful conclusion is structural:

- there **are** parameter choices where a Janus-like anti-correlated source can live on a real connected nonlinear scalar branch;
- there are also nearby-looking choices where the desired branch ends at finite source amplitude;
- therefore branch continuity is a genuine model-selection criterion, not a detail.

This strengthens the case for a targeted parameter search around Case-A-like regions rather than a generic claim that Vainshtein screening saves JANUS-R.

---

## Crucial limitation

The algebraic Stueckelberg equation answers

`what scalar configuration is compatible with a chosen H and matter source?`

It does **not** answer

`does the theory dynamically create a large twin/visible anti-correlation from realistic initial conditions?`

The latter requires the time-dependent coupled perturbation/fluid equations.

Thus the present result is only a **necessary topology gate**.

The central unresolved question remains whether a branch can simultaneously

1. be regular through the early nonlinear regime;
2. return to an observationally acceptable near-GR phase;
3. generate or preserve a substantial relative density mode;
4. emerge late enough to produce a measurable dynamics/lensing mismatch;
5. avoid CMB/LSS constraints.

---

## Updated decision

`LINEAR_STRONG_JANUS = SEVERELY_CONSTRAINED`

`NONLINEAR_BRANCH_EXISTENCE = PASS_FOR_SELECTED_PARAMETERS`

`NONLINEAR_DYNAMIC_GENERATION_OF_SEGREGATION = OPEN`

The next worthwhile calculation is the dynamical evolution of the relative matter mode through a Case-A-like nonlinear-to-linear transition. Merely finding more algebraic roots is no longer sufficient.
