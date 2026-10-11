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
- Primary-source inspection of Comelli 2012 Appendix A confirms the implemented `A2-A1` and `A2+A1` relations exactly, including the signs of the `B1`, `B1'`, `E'`, `E''`, `c'`, `Psi2-Psi1`, `H` and `H_omega` terms. A simple sign error in the coded `A1/A2` reconstruction is therefore strongly disfavored.
- Comelli 2014 Appendix B explicitly contains the missing gravitational gradient: their Case-C reduced equation has an `O(k^2 E)` term, and for the quoted equal-fluid limit reduces to a definite high-k propagation factor. Therefore the published Comelli system itself does contain the helicity-0 gradient; the loss occurs in our reduction/elimination, not in the underlying equations.
- With the corrected gauge identity, the seven scalar constraint/identity equations have rank 6 at fixed `E'`: `E'` is a dynamical direction and the other six quantities are constrained.
- A 12x12 metric closure has been constructed from seven constraints/identities, two differentiated momentum equations, two spatial traces, and differentiated `g00`; differentiated `f00` is held out as a Bianchi diagnostic.
- The closure passes algebraic residual, linearity and held-out `f00` consistency tests on a Candidate-C redshift/scale grid.
- This is NOT sufficient validation: its local 8D Jacobian reproduces the visible radiation pair at `c = 1/sqrt(3)`, proving the k/time normalization is correct, but the second propagating pair is only about `c = 0.0159` at `z=1`, whereas the independent De Felice high-k scalar prediction is about `c_s = 0.8319` there.
- De Felice et al. Eq. (86) gives three scalar high-frequency speeds for the two-fluid problem: one gravitational scalar speed plus the sound speed of the g-fluid plus the sound speed of the f-fluid. Thus the slow pair in the current reduction cannot replace the missing helicity-0 pair.
- The De Felice gravitational speed target has been independently rechecked in two equivalent published forms (their high-k sound-speed formula and its alternative rearrangement). Both reproduce the JANUS `scalar_cs2` value to numerical precision at the Candidate-C comparison point, so `c_s~0.832` is not a target-transcription or normalization artifact.
- The De Felice background mapping is independently closed: on the dust+dust Candidate-C point, their exact background relation Eq. (27), `2(c-1)W = rho_g - c xi^2 rho_f/kappa`, agrees at relative precision about `2e-14` (`-131.151431995910` versus `-131.151431995913`). This strongly validates the JANUS mapping of `c, xi, kappa, m^2, rho_g, rho_f` and `W`.
- Replacing differentiated `g00` by differentiated `f00` as the twelfth closure equation leaves the local eigenvalue spectrum unchanged to numerical precision. The choice of which differentiated 00 equation closes the 12x12 system is therefore not the cause of the missing gravity pair.
- A self-consistent local dust+dust diagnostic was run with the Candidate-C interaction parameters but visible radiation set to zero in the background itself. At `a=0.5`, `k=0.5 h/Mpc`, it gives `c=0.93708463` and the independent De Felice gravitational speed `c_s=0.83190833`. The current 6D `(E,E',delta_g,u_g,delta_f,u_f)` reduction still produces only the pair `-1.95236 +/- 23.89281 i`, i.e. propagation speed `23.89281/1498.96229 = 0.0159396`, plus real dust/gravity modes. Therefore the effective visible dust+radiation approximation is decisively NOT the source of the missing helicity-0 pair.
- The same dust+dust spectrum was scanned with increasing k. The faulty oscillatory frequency approaches a constant `omega ~= 23.894 H0` while `k` grows, so its apparent speed falls as `1/k`. Correspondingly the coefficient of `E` in the reconstructed `E''` equation approaches a constant (`~ -571.4`) rather than scaling as `-c_s^2 k^2`. The helicity-0 gradient term is structurally absent, not merely mis-normalized.
- Zeroing or multiplying individual background derivatives (`H'`, `H_omega'`, `c'`, `xi'`, `f1'`, `f2'`) does not restore an `O(k^2)` term. The failure is not attributable to one background-derivative coefficient.
- The fluid conservation equations A.7-A.9 and Einstein equations A.10-A.16 have been recross-checked against the primary Comelli equations; no sign/factor mismatch was found in the currently coded matter equations or the explicit `c`, `kappa`, `xi` prefactors.
- Forcing the ambiguous A.18 relation to use `(B1-E)` instead of `(B1-E')`, together with the correspondingly differentiated relation, still leaves the high-k frequency asymptotically constant and does not recover De Felice. Thus the A.18 prime/unprime ambiguity is not the cause of the missing gradient, although `(B1-E')` remains the algebraically preferred identity.
- Leading-order high-k analysis of the current reduction gives `Phi1 ~ +(a^2 m^2 f2/2) E`, `Phi2 ~ -(a^2 m^2 f2/(2 kappa xi^2)) E`, `B1 ~ (1+c) s E`, and `A1 ~ A2 ~ s^2 E`. With these relations the g-sector spatial trace cancels at principal order, but the f-sector spatial trace does not: its interaction `A2` term and `Phi2''` term reinforce instead of cancel. Primary-source verification of the A1/A2 formula means this observation now points to the reduction/scaling rather than to a simple A2 sign typo.
- An independent bigravity perturbation formulation writes the raw f-sector interaction terms with the opposite metric-sector sign, which makes the printed Comelli f-trace sign worth auditing. However, a controlled scratch experiment flipping only the f-trace interaction sign in the existing 12x12 closure changes the slow spurious speed only from about `0.01594` to `0.01557`; it does NOT restore the De Felice `~0.832` pair. Therefore a simple isolated f-trace sign flip is rejected as a sufficient fix and no physical coefficient has been changed in Git.
- A first Comelli Case-C benchmark was found to be slightly off-shell at order `m^2`; it must not be used as a decisive regression. An exactly on-shell `a1`-only Case-C asymptotic point has now been constructed with `a=1`, `xi=1/1000`, `kappa=m^2=a1=G=1`, `w1=1/3`, `w2=0`, `H=1000`, `rho1=2999999997/1000`, `rho2=2999000000000`, `c=2000999997/1000000001`, together with consistent `c'`, `xi'`, `H'`, `H_omega'`, `f1'` and `f2'`. Future Case-C principal-symbol tests must use this exact on-shell construction or an algebraically equivalent one.
- In symbolic high-k minors of the direct Comelli system, the expected Case-C factor `3 q^2 - 2` (from their Appendix B.2 `E''-(2/3)k^2E+...=0`) appears in leading minors when the A.17 / `Fdiff` row is omitted, while minors retaining A.17 can lose it. This is a diagnostic localization only, NOT permission to delete A.17: A.17 has also been independently re-derived from the raw gauge-invariant definitions and is algebraically correct. The next task is therefore a properly scaled principal-symbol analysis on the exact on-shell background, to decide whether this is a singular/asymptotic scaling issue or a real incompatibility.
- A first naive frozen-coefficient direct matrix was assembled with 13 equations for 11 amplitudes. A row/column-normalized smallest-singular-value scan does not give a decisive root structure and must NOT be interpreted as a physical dispersion relation, because the system contains Bianchi-redundant rows and singular high-k variable scalings. T1c must explicitly remove/handle those dependencies before reading roots.
- The homothetic Aoki-Maeda transfer module already in the repo is only a reference density-mode solver, and `aoki_scalar_polynomial.py` is a nonlinear Stueckelberg diagnostic; neither is an independent general non-homothetic linear scalar solver for Candidate C.
- Therefore the present 12x12 reduction does not yet reproduce the physical helicity-0 principal symbol. Do not integrate it for physics conclusions.
- The current red TDD test is `tests/test_comelli_native_scalar.py`; it asks for a native high-k scalar system matching the De Felice propagation speed. `numerics/comelli_native_scalar.py` does not yet exist.

## Rejected / resolved hypotheses

- Unit conversion or `k` normalization error: rejected because the same 8D Jacobian exactly recovers the radiation speed `1/sqrt(3)`.
- Missing generic `k^2` term in the published spatial dynamics: rejected. Comelli Appendix B explicitly contains the gravitational `k^2 E` contribution.
- A simple sign/transcription error in the implemented `A1/A2` sum/difference relations: strongly disfavored by direct comparison with the primary 2012 relations.
- Replacing `(B1-E')` by `(B1-E)` to match extracted PDF text: rejected as the cause of the high-k failure. Direct substitution of the gauge-invariant definitions prefers `(B1-E')`, and the alternative does not restore the gradient anyway.
- Treating the current 12x12 closure as validated just because Bianchi residuals vanish: rejected. A Bianchi-consistent reduction can still project out the physical helicity-0 mode.
- Blaming the use of differentiated `g00` rather than differentiated `f00`: rejected; swapping them does not change the spectrum.
- Blaming the Candidate-C visible dust+radiation mixture or the single-effective-fluid approximation: rejected by the self-consistent dust+dust background test; the same slow spurious pair remains while De Felice predicts `c_s~0.832`.
- Blaming a single background derivative: rejected by direct sensitivity tests; the missing `k^2` term is structural.
- Blaming De Felice convention normalization or the target sound-speed transcription: rejected to practical numerical precision by the exact background-relation match and two equivalent sound-speed formulas.
- Flipping only the f-sector spatial-trace interaction sign: rejected as a sufficient fix by direct scratch eigenvalue test; the gravity pair remains missing.

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
- [x] **T1a — Build a self-consistent one-fluid-per-metric local background (dust+dust, no visible radiation) and test the closure there.** Result: same failure; mixture hypothesis rejected.
- [x] **T1b — Validate the direct Comelli equations/auxiliary identities independently of PDF text extraction.** Primary-source equations and raw gauge-invariant definitions have been recross-checked; A1/A2 agree with the implementation, Comelli Appendix B independently proves the `k^2 E` gravity term exists, and De Felice's target speed has been independently revalidated. No simple transcription error explains the loss.
- [ ] **T1c — Construct the properly scaled principal symbol on the exact on-shell Comelli Case-C background.** Determine whether the `3q^2-2` gravity factor survives all exact identities after correct variable/row scaling; explicitly handle Bianchi-redundant rows and resolve the apparent A.17 conflict without deleting a valid identity.
- [ ] **T2 — Compare the directly derived principal symbol with the De Felice scalar speed on the same dust+dust background and on Candidate C at (`a=0.5`, `k=0.5 h/Mpc`).**
- [ ] **T3 — Identify which equation/identity in the 12x12 closure changes the principal-symbol rank or removes the helicity-0 pair. Test equation substitutions one at a time; do not tune coefficients.** `d(g00)` vs `d(f00)`, matter mixture, individual background derivatives, A1/A2 transcription, A.18 prime/unprime, isolated f-trace sign, and the De Felice target normalization are already ruled out.
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

Start at **T1c**. Use the exact on-shell Comelli Case-C background and construct the direct Fourier/principal matrix with explicit variable and row powers of `k`; identify and remove only Bianchi-redundant equations by rank/left-nullspace analysis, never by choosing the rows that give the desired answer. Verify that the physical determinant/minors are invariant under swapping equivalent redundant rows. The first required regression is recovery of the published Case-C factor `3 q^2 - 2`; only then proceed to the Candidate-C De Felice speed in T2. Update this file immediately after every new ruling or completed task.