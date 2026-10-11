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
- The implemented A1/A2 sum/difference identities agree with the primary Comelli 2012 formulas.
- A.17 is algebraically valid and must not be deleted merely because selected minors look better without it.
- A.18 remains a notation/typography ambiguity: direct substitution of the gauge-invariant definitions gives `(B1-E')`, while the printed equation shows `(B1-E)`. Testing either choice in the current closure does not restore the missing high-k pair.
- Comelli Appendix B.2 explicitly contains the helicity-0 gradient. For `w1=1/3`, `w2=0`, `a2=a3=0`, hence `f1=f2`, B.5 reduces inside the horizon to
  `E'' + (3/tau) E' - (2/3) k^2 E = 0`.
  The required leading sub-horizon factor is therefore `3 q^2 - 2` for a local ansatz `s=q k`.

### Current JANUS closure and failure

- Seven scalar constraints/identities have rank 6 at fixed `E'`; the other six nondynamical variables can be solved.
- Metric acceleration and the Candidate-C 12x12 closure pass algebraic residual, linearity, and held-out `f00` Bianchi checks, but these checks are not sufficient physically.
- Candidate C at `a=0.5`, `k=0.5 h/Mpc` recovers visible radiation at exactly `1/sqrt(3)`, proving the k/time normalization is correct.
- The second oscillatory pair is only `c~0.0159`, while independent De Felice gives gravitational `c_s~0.8319`.
- A self-consistent dust+dust Candidate-C background gives the same spurious pair; the visible dust+radiation mixture is not the cause.
- Increasing k makes the faulty frequency approach `omega~23.894 H0`; its apparent speed falls as `1/k`. The reconstructed `E''` coefficient tends to about `-571`, rather than `-c_s^2 k^2`: the gradient term is structurally absent.
- Swapping differentiated `g00`/`f00`, varying individual background derivatives, changing A.18 prime/unprime, and an isolated f-trace interaction-sign flip do not repair the Candidate-C closure.
- The closure conditioning is not the cause: an 80-digit solve agrees with double precision at ~`4e-16` relative for the relevant `E''` coefficient.

## Correct Case-C asymptotics — IMPORTANT CORRECTION

A previous scratch benchmark incorrectly imposed **`xi = epsilon`**, where `epsilon = m/H`. That mixes two distinct limits and is **not** the Case-C expansion used by Comelli. Treat all results that depended on `xi=epsilon` as mixed-limit diagnostics only, not decisive Case-C regressions.

The correct ordering is:

1. `epsilon = m/H -> 0` while `xi = X` is held `O(1)` at leading order;
2. only after the early-time epsilon expansion, take the sub-horizon limit `k tau >> 1`.

For the exact on-shell `a1`-only benchmark in units `a=1`, `m^2=kappa=a1=8piG=1`, with `w1=1/3`, `w2=0`, `H=1/epsilon`, and independent fixed `xi=X`:

- `rho1 = 3/epsilon^2 - 3 X`;
- `rho2 = 3/(epsilon^2 X^2) - 1/X^3`;
- `c = -(3 X^2 epsilon^2 - 2X - epsilon^2)/(X*(X epsilon^2+1)) = 2 + epsilon^2*(1/X - 5X) + O(epsilon^4)`;
- `f1=f2=X` for the `a1`-only benchmark;
- consistent derivatives are generated from this exact family; do not insert the old `xi=epsilon` derivatives.

Use the authors' normalized gravitational scalar `E_N=E/tau^2`. Natural weights are `E~epsilon^2 E_N`, `B~epsilon`, velocity potentials `u~epsilon`, while `Phi`, `F`, and density contrasts are `O(1)`.

With the correct fixed-X family and row/variable scaling:

- the leading direct 13x11 system has rank 9 and a two-dimensional gravitational right kernel;
- the full `O(epsilon)` Fredholm compatibility operator is **exactly zero**. This is a major consistency check and replaces the earlier mixed-limit result where a spurious first-order obstruction appeared;
- the first nontrivial compatibility is therefore `O(epsilon^2)`;
- at large sub-horizon `K=k epsilon`, the `O(epsilon^2)` compatibility matrix in one convenient kernel basis has leading form

  ```text
  [ -X/6      2X    ]
  [ -X q/4    3X q  ]
  [  1/(6X)  -2/X   ]
  [  q/(4X)   q/X   ]
  ```

  for the equations as currently transcribed. The first three rows require kernel-amplitude ratio `a=12 b`, while the fourth requires `a=-4 b` for `q!=0`. The remaining incompatibility is therefore localized to the f-sector compatibility/spatial hierarchy at this order.
- As a diagnostic only, flipping the f-trace interaction block makes the **leading** large-K rows mutually consistent (`a=12b`), but this is not accepted as a correction: the same isolated sign flip already fails the Candidate-C speed test, and subleading compatibility has not yet yielded `3 q^2-2`.
- Do not change a physical sign in Git unless the full Case-C B.5 regression and independent Candidate-C De Felice regression both require it.

## Rejected / resolved hypotheses

- k/time unit conversion error — rejected by exact radiation speed.
- visible dust+radiation mixture — rejected by dust+dust background.
- choosing `d(g00)` rather than `d(f00)` — rejected.
- one bad background derivative — rejected.
- De Felice normalization/transcription error — rejected.
- simple A1/A2 typo — rejected by primary-source comparison.
- A.18 prime vs unprime as sole cause — rejected.
- isolated f-trace sign flip as sufficient fix — rejected on Candidate C; remains only a Case-C diagnostic clue.
- double-precision conditioning — rejected by high-precision solve.
- Bianchi residuals as proof of correct mode content — rejected.
- a selected high-k minor as the dispersion relation — rejected.
- `xi=epsilon` as the Case-C asymptotic family — **rejected; it mixes limits**.

## Active task list

- [x] Map JANUS conventions to Comelli/De Felice.
- [x] Implement/test scalar constraints and gauge identities.
- [x] Establish rank-6 constraint manifold with dynamic `E'`.
- [x] Implement/test metric acceleration layer.
- [x] Implement exact Candidate-C transfer background adapter.
- [x] Implement/test 12x12 closure plus held-out Bianchi diagnostic.
- [x] Add independent De Felice high-k regression.
- [x] Diagnose local 8D modes: radiation correct, helicity-0 missing.
- [x] **T1a** — self-consistent one-fluid-per-metric dust+dust comparison.
- [x] **T1b** — primary-source audit of Comelli equations and De Felice target.
- [ ] **T1c — Reproduce Comelli Case-C B.5 from the direct equations with the correct two-stage asymptotics.** IN PROGRESS.
  - [x] T1c.1 — replace the invalid `xi=epsilon` path by an exact two-parameter on-shell family (`epsilon->0`, `xi=X=O(1)`).
  - [x] T1c.2 — apply `E_N=E/tau^2` and natural epsilon weights.
  - [x] T1c.3 — compute leading system: rank 9, gravitational right kernel dimension 2.
  - [x] T1c.4 — show the `O(epsilon)` compatibility operator vanishes exactly on the correct family.
  - [ ] **T1c.5 — compute the next Fredholm/sub-horizon compatibility orders until the published B.5 factor `3 q^2-2` is recovered without deleting valid equations or tuning coefficients.**
  - [ ] T1c.6 — verify invariance under Bianchi-redundant row representatives.
- [ ] **T2 — Apply the validated principal reduction to dust+dust Candidate C and recover the independent De Felice gravity speed.**
- [ ] **T3 — Locate the exact structural mistake in the current 12x12 closure by comparing it term-by-term with the validated reduction.**
- [ ] **T4 — Implement corrected `numerics/comelli_native_scalar.py`.**
- [ ] **T5 — Make `tests/test_comelli_native_scalar.py` green and add >=3 additional `(z,k)` high-k regressions.**
- [ ] **T6 — Re-run every Gate-2B constraint/acceleration/Bianchi test; no regression allowed.**
- [ ] **T7 — Only then build the time-domain transfer RHS and integrate a fundamental transfer matrix.**
- [ ] **T8 — Track the GR-connected/adiabatic mode continuously; do not define it merely by `delta_g=delta_f`.**
- [ ] **T9 — Compute `T_gg`, `T_gf`, `T_fg`, `T_ff` and relative-mode growth over the linearly stable interval.**
- [ ] **T10 — Record Gate-2B pass/fail/inconclusive verdict with numerical tolerances and domain.**

## Current red regression

`tests/test_comelli_native_scalar.py` imports the not-yet-created `numerics/comelli_native_scalar.py` and requires a native scalar high-k gravity pair matching De Felice at Candidate C. Do not implement around this test until T1c is closed.

## Immediate restart instruction

**Resume at T1c.5 on the fixed-X family.**

1. Keep `epsilon=m/H` and `xi=X` independent; never restore `xi=epsilon`.
2. Use the exact on-shell background and consistent derivatives.
3. Work with `E_N=E/tau^2`, density contrasts, and established epsilon row/variable weights.
4. Starting from the exact result `M1=0`, compute the `O(epsilon^2)` and higher Fredholm compatibility together with the large-`K=k epsilon` expansion.
5. Allow the kernel vector/amplitude ratio itself to have a `1/K` expansion; do not infer dispersion from one leading ratio or selected minor.
6. Acceptance remains the published B.5 result and, in the benchmark, the high-k factor `3 q^2-2`.
7. Do not delete A.17, tune coefficients, or change physical signs merely to fit the target.
8. Update this file after every new hard ruling.
9. Only after B.5 is recovered move to T2 Candidate C.