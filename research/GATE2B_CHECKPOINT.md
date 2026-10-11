# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-11
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **single restart point after any interruption**. Read this file first. Update it whenever a hard fact, rejected hypothesis, task state, or restart instruction changes.

## Scientific goal

Close Gate 2B: compute the full non-homothetic scalar transfer of Candidate C from published ghost-free bigravity equations. No Candidate-C time integration is scientifically interpretable until the implementation independently reproduces the published high-k helicity-0 propagation speed.

## Current verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The Candidate-C background is under control, but the current 12x12 metric closure removes the physical helicity-0 gradient. It must not be used for transfer-function or segregation conclusions yet.

## Hard facts already established

### Background / convention bridge

- JANUS to Comelli/De Felice convention map is closed: `beta_n = n! a_n`, `f2 = y J`, `f1 = Gamma`, `xi=y`, `kappa=alpha^2`, `c=ctilde`.
- Candidate-C background adapter exists in `numerics/candidate_c_transfer.py`.
- De Felice background relation Eq. (27), `2(c-1)W = rho_g - c xi^2 rho_f/kappa`, matches the JANUS background at relative precision ~`2e-14` on the dust+dust comparison point.
- De Felice high-k scalar-speed target has been checked in two equivalent published forms and agrees numerically with `numerics/flrw_two_matter.py::diagnostics()['scalar_cs2']`.

### Published scalar equations

- Comelli matter conservation A.7-A.9 and Einstein scalar equations A.10-A.16 have been independently recross-checked against the primary paper.
- Slip relations used by JANUS agree with Comelli Eq. (4.1).
- The implemented A1/A2 sum/difference identities agree with the primary Comelli 2012 formulas, including the signs of `B1`, `B1'`, `E'`, `E''`, `c'`, `Psi2-Psi1`, `H`, and `H_omega`.
- A.17 is algebraically valid and must not be deleted merely because some selected minors look better without it.
- A.18 remains a notation/typography ambiguity: direct substitution of the gauge-invariant definitions gives `(B1-E')`, while the printed 2014 equation shows `(B1-E)`. Testing either choice inside the existing closure does **not** restore the missing high-k pair.
- Comelli Appendix B.2 explicitly proves the underlying published system contains the helicity-0 gradient. For Case C, Eq. (B.5) contains an `O(k^2 E)` term.
- In the benchmark `w1=1/3`, `w2=0`, `a2=a3=0` so `f1=f2`, B.5 decouples to
  `E'' + (3/tau) E' - (2/3) k^2 E = 0` inside the horizon. Therefore the first required Case-C principal factor is `3 q^2 - 2` for a local growing/decaying ansatz with `s=q k` at `k tau >> 1`.

### Current JANUS closure and failure

- Seven scalar constraints/identities have rank 6 at fixed `E'`; the other six nondynamical quantities can be solved.
- Metric acceleration layer and Candidate-C 12x12 closure are implemented and pass algebraic residual, linearity, and held-out `f00` Bianchi checks.
- These checks are insufficient physically.
- At Candidate C, `a=0.5`, `k=0.5 h/Mpc`, the local 8D Jacobian correctly recovers visible radiation propagation at `1/sqrt(3)`, proving the time/k normalization is correct.
- The second oscillatory pair is only `c~0.0159`, while the independent De Felice gravitational scalar prediction is `c_s~0.8319`.
- On a self-consistent dust+dust Candidate-C background the same spurious pair remains. Visible dust+radiation mixing is therefore not the cause.
- Increasing k makes the faulty oscillatory frequency approach a constant `omega~23.894 H0`, so its apparent speed falls as `1/k`; the reconstructed `E''` coefficient tends to about `-571`, not `-c_s^2 k^2`. The gradient term is structurally absent.
- Swapping differentiated `g00` and differentiated `f00` as the closure equation leaves the spectrum unchanged.
- Zeroing or varying individual background derivatives does not restore the gradient.
- Flipping only the f-sector spatial-trace interaction sign changes the slow speed only from about `0.01594` to `0.01557`; it is rejected as a sufficient fix. No physical coefficient was changed in Git.
- The closure matrix is ill-conditioned (`cond~1.7e9` at the Candidate-C comparison point), but this is **not** the cause: an 80-digit solve gives `E''=-571.3163904968205`, while double precision differs by only ~`4e-16` relative. The missing `k^2` term is not floating-point loss.

### Correct Case-C asymptotic ordering

- The original Comelli derivation first expands in the early-time parameter `epsilon=m/H`, then studies sub-horizon `k tau >> 1`.
- The exact a1-only on-shell Case-C family can be parameterized by `epsilon=xi`, with `H=1/epsilon`, `rho1=3/epsilon^2-3 epsilon`, `rho2=3/epsilon^4-1/epsilon^3`, and `c -> 2` for `w1=1/3`, `w2=0`.
- The authors normalize the gravitational scalar as `E_N=E/tau^2`; in radiation `tau~epsilon`, so `E~epsilon^2 E_N`.
- Natural first-step scalings are therefore: `E/epsilon^2`, `Phi1`, `Phi2`, `F1`, `F2`, density contrasts = `O(1)`; shifts and velocity potentials = `O(epsilon)`.
- Taking only `k->infinity` at fixed epsilon is not the correct regression for Comelli B.5; the limits are singular and need the `epsilon` hierarchy first.
- With the proper `epsilon` normalization, the leading 13x11 direct system has rank 9. Its two-dimensional right kernel lies in the gravitational `(E,B,F)` sector. The dispersion therefore appears through higher-order solvability, not through a naive leading determinant.
- The first `O(epsilon)` compatibility calculation still does not reproduce B.5, with either printed or derivative A.18. This means the gravity dispersion appears at a higher compatibility order and/or requires retaining the complete spatial-equation hierarchy. Do not interpret a first-order determinant as the physical dispersion relation.

### Exact benchmark point retained for numerical checks

For `epsilon=1/1000`:

- `a=1`, `xi=1/1000`, `kappa=m^2=a1=G=1`, `w1=1/3`, `w2=0`, `H=1000`;
- `rho1=2999999997/1000`;
- `rho2=2999000000000`;
- `c=2000999997/1000000001`;
- background derivatives must be generated consistently from the exact family, not inserted approximately.

## Rejected / resolved hypotheses

- k/time unit conversion error — rejected by exact radiation speed.
- visible dust+radiation mixture — rejected by dust+dust background.
- choosing `d(g00)` rather than `d(f00)` — rejected.
- one bad background derivative — rejected.
- De Felice normalization/transcription error — rejected.
- simple A1/A2 sign typo — strongly rejected by primary-source comparison.
- A.18 prime vs unprime as the sole cause — rejected by direct closure tests; notation issue remains open only for exact derivation consistency.
- isolated f-trace interaction-sign flip — rejected as sufficient fix.
- double-precision conditioning — rejected by 80-digit solve.
- interpreting Bianchi residuals as proof of correct physical mode content — rejected.
- interpreting a single selected high-k minor as the dispersion relation — rejected.

## Active task list

- [x] Map JANUS conventions to Comelli/De Felice.
- [x] Implement/test scalar constraints and gauge identities.
- [x] Establish rank-6 constraint manifold with dynamic `E'`.
- [x] Implement/test metric acceleration layer.
- [x] Implement exact Candidate-C transfer background adapter.
- [x] Implement/test 12x12 closure plus held-out Bianchi diagnostic.
- [x] Add independent De Felice high-k regression.
- [x] Diagnose local 8D modes: radiation correct, helicity-0 missing.
- [x] Rule out dust/radiation mixture, d00 choice, derivative coefficients, simple A1/A2 typo, isolated f-trace sign, target normalization, and floating-point loss.
- [x] **T1a** — self-consistent one-fluid-per-metric dust+dust comparison.
- [x] **T1b** — primary-source audit of Comelli equations and De Felice target.
- [ ] **T1c — Reproduce Comelli Case-C B.5 from the direct equations using the correct double asymptotic expansion.** IN PROGRESS.
  - [x] T1c.1 — construct exact on-shell `epsilon` family.
  - [x] T1c.2 — introduce `E_N=E/epsilon^2` and natural epsilon weights.
  - [x] T1c.3 — compute leading system; rank is 9 with a two-dimensional gravitational right kernel.
  - [x] T1c.4 — compute first-order left/right-kernel solvability; insufficient to recover B.5.
  - [ ] **T1c.5 — carry the singular solvability expansion to the next nonzero order until the common Case-C compatibility factor is obtained. Acceptance: recover B.5 and `3 q^2-2` without deleting valid equations or tuning coefficients.**
  - [ ] T1c.6 — verify the result is invariant under replacing Bianchi-redundant row representatives.
- [ ] **T2 — Apply the validated principal reduction to a dust+dust Candidate-C point and recover the independent De Felice gravity speed.**
- [ ] **T3 — Locate the exact structural mistake in the current 12x12 closure by comparing it term-by-term with the validated reduction.**
- [ ] **T4 — Implement the corrected native scalar system in `numerics/comelli_native_scalar.py`.**
- [ ] **T5 — Make `tests/test_comelli_native_scalar.py` green and add >=3 additional `(z,k)` high-k regressions.**
- [ ] **T6 — Re-run all Gate-2B constraint/acceleration/Bianchi tests; no regression allowed.**
- [ ] **T7 — Only then build the time-domain transfer RHS and integrate a fundamental transfer matrix.**
- [ ] **T8 — Track the GR-connected/adiabatic mode continuously; do not define it merely by `delta_g=delta_f`.**
- [ ] **T9 — Compute `T_gg`, `T_gf`, `T_fg`, `T_ff` and relative-mode growth over the linearly stable interval.**
- [ ] **T10 — Record Gate-2B pass/fail/inconclusive verdict with numerical tolerances and domain.**

## Current red regression

`tests/test_comelli_native_scalar.py`

It imports the not-yet-created `numerics/comelli_native_scalar.py` and requires a native scalar system whose high-k gravity pair matches De Felice at Candidate C.

## Immediate restart instruction

**Resume at T1c.5.**

1. Use the symbolic exact `epsilon` family, not a fixed-epsilon `k->infinity` shortcut.
2. Work with `E_N=E/epsilon^2`, density contrasts rather than raw `delta rho`, and the established natural epsilon weights.
3. Expand the row-scaled direct 13x11 polynomial system beyond first compatibility order using right/left nullspaces (singular perturbation / Fredholm solvability).
4. Continue until a nonzero compatibility matrix produces the published Case-C equation B.5. In the `w1=1/3`, `w2=0`, `f1=f2` benchmark, the sub-horizon factor must reduce to `3 q^2-2`.
5. Do not delete A.17, do not tune coefficients, and do not change physical signs merely to fit the target.
6. After every new hard ruling, update this file before proceeding.
7. Only after B.5 is recovered move to T2 and Candidate C.