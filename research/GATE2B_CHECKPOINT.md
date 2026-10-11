# Gate 2B — persistent checkpoint and task list

Date: 2026-10-11
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: this file is the single restart point after any interruption. Update it whenever a task changes state or a new hard fact is established.

## Scientific goal

Close Gate 2B: determine the full non-homothetic scalar transfer of Candidate C without inventing an effective interaction. The implementation must reproduce independently published high-k physics before any Candidate-C time integration is interpreted.

## Current hard facts

- The Candidate-C FLRW background adapter exists and maps JANUS conventions to Comelli/De Felice conventions.
- The factorial mapping is `beta_n = n! a_n`; the interaction identities are `f2 = y J` and `f1 = Gamma`.
- The scalar constraint system uses the gauge-invariant Comelli variables and the corrected identity containing `(B1 - E')`. Direct substitution of the gauge-invariant definitions requires the prime even though the searchable PDF text is ambiguous/inconsistent.
- The `(B1-E')` identity has been re-derived directly from the 2012 raw gauge-invariant definitions: `Xi1=B1_raw+E1'`, `Xi2=B2_raw+E2'`, and `calB1=Xi2-c^2 Xi1+E'`. The corresponding `A1/A2` sum/difference identities used in the acceleration layer were also re-derived and agree with the code.
- With that identity, the seven scalar constraint/identity equations have rank 6 at fixed `E'`: `E'` is a dynamical direction and the other six quantities are constrained.
- A 12x12 metric closure has been constructed from seven constraints/identities, two differentiated momentum equations, two spatial traces, and differentiated `g00`; differentiated `f00` is held out as a Bianchi diagnostic.
- The closure passes algebraic residual, linearity and held-out `f00` consistency tests on a Candidate-C redshift/scale grid.
- This is NOT sufficient validation: its local 8D Jacobian reproduces the visible radiation pair at `c = 1/sqrt(3)`, proving the k/time normalization is correct, but the second propagating pair is only about `c = 0.0159` at `z=1`, whereas the independent De Felice high-k scalar prediction is about `c_s = 0.8319` there.
- De Felice et al. Eq. (86) gives three scalar high-frequency speeds for the two-fluid problem: one gravitational scalar speed plus the sound speed of the g-fluid plus the sound speed of the f-fluid. Thus the slow pair in the current reduction cannot replace the missing helicity-0 pair.
- Replacing differentiated `g00` by differentiated `f00` as the twelfth closure equation leaves the local eigenvalue spectrum unchanged to numerical precision. The choice of which differentiated 00 equation closes the 12x12 system is therefore not the cause of the missing gravity pair.
- Candidate C itself has visible dust + visible radiation coupled to g and twin dust coupled to f, i.e. one more matter scalar than the two-fluid De Felice setup. A clean diagnostic must therefore also test an exactly one-fluid-per-metric background before blaming the Comelli reduction.
- Therefore the present 12x12 reduction does not yet reproduce the physical helicity-0 principal symbol. Do not integrate it for physics conclusions.
- The current red TDD test is `tests/test_comelli_native_scalar.py`; it asks for a native high-k scalar system matching the De Felice propagation speed. `numerics/comelli_native_scalar.py` does not yet exist.

## Rejected / resolved hypotheses

- Unit conversion or `k` normalization error: rejected because the same 8D Jacobian exactly recovers the radiation speed `1/sqrt(3)`.
- Missing generic `k^2` term in the spatial trace: rejected; the anisotropic contribution cancels after the slip relation in the published scalar equations.
- Replacing `(B1-E')` by `(B1-E)` to match extracted PDF text: rejected for now; direct substitution of the gauge-invariant definitions yields `(B1-E')`. Any reversal requires an explicit derivation from the raw definitions, not PDF OCR/text extraction.
- Treating the current 12x12 closure as validated just because Bianchi residuals vanish: rejected. A Bianchi-consistent reduction can still project out the physical helicity-0 mode.
- Blaming the use of differentiated `g00` rather than differentiated `f00`: rejected; swapping them does not change the spectrum.

## Active task list

- [x] Map JANUS beta conventions to Comelli `a_n`, `f1`, `f2`.
- [x] Implement/test scalar constraints and gauge identities.
- [x] Establish rank-6 constraint manifold with dynamic `E'`.
- [x] Implement/test metric acceleration layer.
- [x] Implement exact Candidate-C transfer background adapter.
- [x] Implement/test 12x12 algebraic metric closure and held-out Bianchi diagnostic.
- [x] Add independent high-k scalar-speed regression against De Felice.
- [x] Diagnose local 8D eigenmodes: radiation correct, helicity-0 speed wrong/missing.
- [ ] **T1 — Derive the high-k principal symbol directly from the published Comelli scalar equations, retaining only terms that scale as `omega^2`, `omega k`, or `k^2`.** IN PROGRESS.
- [ ] **T1a — Build a self-consistent one-fluid-per-metric local background (preferably dust+dust, no visible radiation) and test the closure there.** This separates a genuine metric-reduction error from the effective-fluid approximation used on Candidate C.
- [ ] **T2 — Compare that principal symbol with the De Felice scalar speed on the same background, and on Candidate C at (`a=0.5`, `k=0.5 h/Mpc`).**
- [ ] **T3 — Identify which equation/identity in the 12x12 closure changes the principal-symbol rank or removes the helicity-0 pair. Test equation substitutions one at a time; do not tune coefficients.** `d(g00)` vs `d(f00)` has already been ruled out.
- [ ] **T4 — Implement the minimal corrected native scalar system in `numerics/comelli_native_scalar.py`.**
- [ ] **T5 — Make `tests/test_comelli_native_scalar.py` green, then add at least three additional `(z,k)` high-k speed regression points.**
- [ ] **T6 — Re-run all Gate-2B algebraic/constraint/Bianchi tests. No regression is allowed.**
- [ ] **T7 — Only after T1–T6 pass, build the time-domain 8D transfer RHS and integrate a fundamental transfer matrix.**
- [ ] **T8 — Define the adiabatic/GR-connected initial mode by continuous mode tracking, not simply `delta_g=delta_f`.**
- [ ] **T9 — Compute `T_gg, T_gf, T_fg, T_ff` and relative-mode growth over the stable linear interval.**
- [ ] **T10 — Record Gate 2B verdict: pass/fail/inconclusive, with numerical tolerances and the exact redshift/scale domain.**

## T1 acceptance test

At fixed background, freeze slowly varying coefficients and form the local Fourier ansatz `exp(-i omega eta)`. The principal scalar system must contain:

1. a distinct gravitational scalar pair approaching the independent De Felice `scalar_cs2` value;
2. the appropriate matter acoustic pairs (`1/sqrt(3)` for visible radiation, zero intrinsic sound speed for dust); on the exactly two-fluid comparison, the two matter speeds must match De Felice's `c_g` and `ctilde c_f`;
3. no extra propagating scalar pair beyond the physical degree count.

If this cannot be obtained from the equations currently transcribed, stop and re-audit the equation transcription before any transfer integration.

## Immediate restart instruction

Start at **T1/T1a**. First test the reduction on a self-consistent one-fluid-per-metric background so that the De Felice two-fluid degree count applies exactly. Then inspect the principal high-k coefficients of the Comelli equations and the existing closure. Do not modify physical coefficients merely to fit De Felice. Every change must be justified by a published equation or a direct derivation from the gauge-invariant definitions, followed by a red/green test. Update this file immediately after every new ruling or completed task.
