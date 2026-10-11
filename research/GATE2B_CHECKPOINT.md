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
- A self-consistent local dust+dust diagnostic was run with the Candidate-C interaction parameters but visible radiation set to zero in the background itself. At `a=0.5`, `k=0.5 h/Mpc`, it gives `c=0.93708463` and the independent De Felice gravitational speed `c_s=0.83190833`. The current 6D `(E,E',delta_g,u_g,delta_f,u_f)` reduction still produces only the pair `-1.95236 +/- 23.89281 i`, i.e. propagation speed `23.89281/1498.96229 = 0.0159396`, plus real dust/gravity modes. Therefore the effective visible dust+radiation approximation is decisively NOT the source of the missing helicity-0 pair.
- The same dust+dust spectrum was scanned with increasing k. The faulty oscillatory frequency approaches a constant `omega ~= 23.894 H0` while `k` grows, so its apparent speed falls as `1/k`. Correspondingly the coefficient of `E` in the reconstructed `E''` equation approaches a constant (`~ -571.4`) rather than scaling as `-c_s^2 k^2`. The helicity-0 gradient term is structurally absent, not merely mis-normalized.
- Zeroing or multiplying individual background derivatives (`H'`, `H_omega'`, `c'`, `xi'`, `f1'`, `f2'`) does not restore an `O(k^2)` term. The failure is not attributable to one background-derivative coefficient.
- The fluid conservation equations A.7-A.9 and Einstein equations A.10-A.16 have been recross-checked against the primary Comelli equations; no sign/factor mismatch was found in the currently coded matter equations or the explicit `c`, `kappa`, `xi` prefactors.
- Forcing the ambiguous A.18 relation to use `(B1-E)` instead of `(B1-E')`, together with the correspondingly differentiated relation, still leaves the high-k frequency asymptotically constant and does not recover De Felice. Thus the A.18 prime/unprime ambiguity is not the cause of the missing gradient, although `(B1-E')` remains the algebraically preferred identity.
- Leading-order high-k analysis of the current reduction gives `Phi1 ~ +(a^2 m^2 f2/2) E`, `Phi2 ~ -(a^2 m^2 f2/(2 kappa xi^2)) E`, `B1 ~ (1+c) s E`, and `A1 ~ A2 ~ s^2 E`. With these relations the g-sector spatial trace cancels at principal order, but the f-sector spatial trace does not: its interaction `A2` term and `Phi2''` term reinforce instead of cancel. This localizes the current leading suspect to the f-sector spatial/A2 reduction or its interpretation.
- Therefore the present 12x12 reduction does not yet reproduce the physical helicity-0 principal symbol. Do not integrate it for physics conclusions.
- The current red TDD test is `tests/test_comelli_native_scalar.py`; it asks for a native high-k scalar system matching the De Felice propagation speed. `numerics/comelli_native_scalar.py` does not yet exist.

## Rejected / resolved hypotheses

- Unit conversion or `k` normalization error: rejected because the same 8D Jacobian exactly recovers the radiation speed `1/sqrt(3)`.
- Missing generic `k^2` term in the spatial trace: rejected as a generic explanation; the anisotropic contribution cancels after the slip relation in the published scalar equations, while the remaining problem is specifically the f-sector principal balance.
- Replacing `(B1-E')` by `(B1-E)` to match extracted PDF text: rejected as the cause of the high-k failure. Direct substitution of the gauge-invariant definitions prefers `(B1-E')`, and the alternative does not restore the gradient anyway.
- Treating the current 12x12 closure as validated just because Bianchi residuals vanish: rejected. A Bianchi-consistent reduction can still project out the physical helicity-0 mode.
- Blaming the use of differentiated `g00` rather than differentiated `f00`: rejected; swapping them does not change the spectrum.
- Blaming the Candidate-C visible dust+radiation mixture or the single-effective-fluid approximation: rejected by the self-consistent dust+dust background test; the same slow spurious pair remains while De Felice predicts `c_s~0.832`.
- Blaming a single background derivative: rejected by direct sensitivity tests; the missing `k^2` term is structural.

## Active task list

- [x] Map JANUS beta conventions to Comelli `a_n`, `f1`, `f2`.
- [x] Implement/test scalar constraints and gauge identities.
- [x] Establish rank-6 constraint manifold with dynamic `E'`.
- [x] Implement/test metric acceleration layer.
- [x] Implement exact Candidate-C transfer background adapter.
- [x] Implement/test 12x12 algebraic metric closure and held-out Bianchi diagnostic.
- [x] Add independent high-k scalar-speed regression against De Felice.
- [x] Diagnose local 8D eigenmodes: radiation correct, helicity-0 speed wrong/missing.
- [ ] **T1 — Derive the high-k principal symbol directly from the published Comelli scalar equations, retaining only terms that scale as `omega^2`, `omega k`, or `k^2`.** IN PROGRESS. Current localization: f-sector spatial/A2 principal balance.
- [x] **T1a — Build a self-consistent one-fluid-per-metric local background (dust+dust, no visible radiation) and test the closure there.** Result: same failure; mixture hypothesis rejected.
- [ ] **T1b — Obtain/inspect original TeX source for Comelli 2012/2014 and rederive the f-sector spatial equation plus A2 from raw variables/macros, bypassing PDF text extraction.**
- [ ] **T2 — Compare the directly derived principal symbol with the De Felice scalar speed on the same dust+dust background and on Candidate C at (`a=0.5`, `k=0.5 h/Mpc`).**
- [ ] **T3 — Identify which equation/identity in the 12x12 closure changes the principal-symbol rank or removes the helicity-0 pair. Test equation substitutions one at a time; do not tune coefficients.** `d(g00)` vs `d(f00)`, matter mixture, individual background derivatives, and A.18 prime/unprime are already ruled out.
- [ ] **T4 — Implement the minimal corrected native scalar system in `numerics/comelli_native_scalar.py`.**
- [ ] **T5 — Make `tests/test_comelli_native_scalar.py` green, then add at least three additional `(z,k)` high-k speed regression points.**
- [ ] **T6 — Re-run all Gate-2B algebraic/constraint/Bianchi tests. No regression is allowed.**
- [ ] **T7 — Only after T1-T6 pass, build the time-domain 8D transfer RHS and integrate a fundamental transfer matrix.**
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

Start at **T1b**. The failure is now localized to a structural loss of the helicity-0 `k^2` term, with the f-sector spatial/A2 principal balance the leading suspect. Obtain the original TeX source for Comelli 2012/2014 and rederive that sector from raw definitions rather than PDF text extraction. Do not modify physical coefficients merely to fit De Felice. Every change must be justified by a published equation or a direct derivation from the gauge-invariant definitions, followed by a red/green test. Update this file immediately after every new ruling or completed task.
