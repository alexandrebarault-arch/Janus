# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-11
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **single restart point after any interruption**. Read this file first. Update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Scientific goal

Close Gate 2B: compute the full non-homothetic scalar transfer of Candidate C from published ghost-free bigravity equations. No Candidate-C transfer or segregation result is scientifically interpretable until the implementation independently reproduces the published high-k helicity-0 propagation.

## Current verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The Candidate-C background/convention bridge is under control. The current 12x12 perturbation closure is algebraically consistent but removes the physical helicity-0 gradient and must not be used for physics conclusions.

## Hard facts already established

### Background / conventions

- JANUS -> Comelli/De Felice: `beta_n=n! a_n`, `f2=yJ`, `f1=Gamma`, `xi=y`, `kappa=alpha^2`, `c=ctilde`.
- `numerics/candidate_c_transfer.py` maps Candidate C to the perturbation conventions.
- De Felice background Eq. (27), `2(c-1)W = rho_g - c xi^2 rho_f/kappa`, matches JANUS at ~`2e-14` relative on the dust+dust comparison point.
- The independently published De Felice high-k scalar-speed target agrees with `flrw_two_matter.py::diagnostics()['scalar_cs2']`.

### Published scalar equations

- Comelli matter conservation A.7-A.9, Einstein scalar equations A.10-A.16, slips, and the A1/A2 auxiliary identities have been independently re-audited.
- The complete primary-source A.12/A.16 spatial equations have now been checked **before** slip reduction. Each contains an anisotropic block `(partial_i partial_j-delta_ij Delta)(...)` plus a pure-trace block. The JANUS slip relations are exactly the vanishing of those anisotropic brackets, so after imposing the slips the remaining trace equations in `comelli_scalar_equations.py`/`comelli_dae.py` are not missing an explicit spatial-gradient term. This closes T1c.5.
- A.17 is algebraically valid; do not remove it to improve a determinant.
- A.18 has a real notation/typography issue. From the raw gauge-invariant definitions,
  `Xi2-c^2 Xi1 = calB1-calE'`, so the derived identity contains `(calB1-calE')`; the printed appendix shows `(calB1-calE)`. Both variants have been tested in the present reduction and neither alone restores the physical mode.
- Comelli Appendix B.2 explicitly contains the missing helicity-0 gradient. For `w1=1/3`, `w2=0`, `a2=a3=0`, hence `f1=f2`, B.5 reduces inside the horizon to
  `E'' + (3/tau) E' - (2/3) k^2 E = 0`.
  Therefore the benchmark high-k dispersion must contain `q^2=2/3` (equivalently factor `3q^2-2`) for `s=qk`.

### Current JANUS closure failure

- The seven scalar constraints/identities have rank 6 at fixed `E'`.
- The metric-acceleration layer and 12x12 closure pass algebraic residual, linearity, and held-out `f00` Bianchi checks.
- Candidate C at `a=0.5`, `k=0.5 h/Mpc` gives radiation speed exactly `1/sqrt(3)`, so k/time normalization is correct.
- The supposed gravity pair is only `c~0.0159`, versus independent De Felice `c_s~0.8319`.
- On a self-consistent dust+dust Candidate-C background the same spurious pair remains.
- As k grows, its frequency tends to `omega~23.894 H0`, so speed falls as `1/k`; the reconstructed `E''` coefficient tends to ~`-571`, rather than `-c_s^2 k^2`. The physical gradient is structurally absent.
- Swapping differentiated `g00`/`f00`, perturbing individual background derivatives, changing A.18 prime/unprime, an isolated f-trace interaction-sign flip, and high-precision linear solving do not repair the Candidate-C closure.

## Case-C asymptotics — corrected physical trajectory

Two previous scratch constructions must NOT be treated as decisive Case-C regressions:

1. **Fixed `xi=X` while `epsilon=m/H -> 0`:** useful as a transverse algebraic diagnostic, but it is not the cosmological Case-C trajectory for `w1=1/3,w2=0`.
2. **`xi=epsilon` with `a=1`:** it has the qualitatively correct `xi~epsilon` scaling, but varying epsilon while freezing `a` violates the background fluid conservation equations. Its Bianchi/Fredholm contradictions were therefore artifacts of an off-shell time trajectory.

The primary Comelli Case-C result is
`xi = xi_in * a^[3(w1-w2)/(1+3w2)]`.
For `w1=1/3,w2=0`, this gives **`xi proportional to a`**. During the visible radiation era, `a proportional to tau`, `calH=1/tau`, hence `epsilon=m/calH proportional to tau`; therefore **`xi proportional to epsilon` on the physical trajectory**, but `a` must evolve consistently.

### Dynamically on-shell a1-only benchmark

Use units `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`. Choose conserved-density normalizations

- `rho1 = 3/a^4`,
- `rho2 = 3/(a xi)^3`.

Combining the two Friedmann equations gives the exact algebraic branch relation

`a^4 xi^2 + xi - a - a^4/3 = 0`,

with positive root

`xi(a) = [-1 + sqrt(1 + 4 a^5 + (4/3) a^8)] / (2 a^4)`.

Early-time series:

- `xi(a) = a + a^4/3 - a^6 - (2/3)a^9 + ...`;
- visible Friedmann gives `calH^2 = 1/a^2 + a^2 xi` and therefore `a' = sqrt(1+a^4 xi)`;
- `a'(a) = 1 + a^5/2 + a^8/6 - 5a^10/8 + ...`;
- `tau(a) = a - a^6/12 - a^9/54 + 7a^11/88 + ...`;
- inverted, `a(tau) = tau + tau^6/12 + tau^9/54 - 5tau^11/132 + ...`;
- `xi(tau) = tau + tau^4/3 - 11tau^6/12 - 29tau^9/54 + ...`.

Leading physical background:

`a~tau`, `xi~tau`, `calH~1/tau`, `calH_omega~2/tau`, `rho1~3/tau^4`, `rho2~3/tau^6`, `c->2`.

This leading background satisfies the two fluid conservation laws. It replaces the old frozen-a epsilon family for all future B.5 regressions.

### Fredholm findings on the dynamic background

- With `E=tau^2 E_N`, shifts/velocity potentials weighted as `O(tau)`, and the direct row-scaled scalar system, the leading matrix has a gravitational nullspace rather than killing the mode.
- The first compatibility conditions collapse to a single relation among gravitational kernel amplitudes (one convenient basis gives `-4 a1 + a2 + 12 a3 = 0`).
- After imposing that relation, the next lower-order compatibility vanishes, as expected for a singular constrained system.
- Continuing with a local WKB substitution on the direct equations has still **not** produced `3q^2-2`, for either the derived `(B1-E')` or printed `(B1-E)` A.18. This is not yet evidence against B.5: local substitution before differential elimination may change the singular hierarchy.
- The full A.12/A.16 audit rules out an omitted post-slip anisotropic `k^2` term. The remaining task is true differential-operator elimination on the dynamically on-shell series, keeping `Phi1/Phi2` and the constrained variables until elimination is complete.

## Rejected / resolved hypotheses

- k/time-unit normalization — rejected by exact radiation speed.
- visible dust+radiation mixture — rejected by dust+dust Candidate C.
- differentiated `g00` vs `f00` choice — rejected.
- one bad background derivative — rejected.
- De Felice normalization/transcription — rejected.
- simple A1/A2 typo — rejected by primary-source audit.
- omitted anisotropic/spatial-gradient block in A.12/A.16 after slip reduction — rejected by full primary-source audit.
- A.18 prime/unprime as the sole cause — rejected in current closure; typography issue remains relevant to exact derivation bookkeeping.
- isolated f-trace interaction-sign flip as sufficient repair — rejected on Candidate C.
- floating-point conditioning — rejected by 80-digit solve.
- Bianchi residuals as proof of physical mode content — rejected.
- selected high-k minors as the dispersion relation — rejected.
- fixed-`xi` epsilon family as the physical Case-C trajectory — rejected.
- frozen-`a`, `xi=epsilon` family as dynamically on-shell — rejected because it violates background conservation.

## Active task list

- [x] Map JANUS conventions to Comelli/De Felice.
- [x] Implement/test scalar constraints and identities.
- [x] Establish rank-6 constraint manifold with dynamic `E'`.
- [x] Implement/test metric acceleration layer.
- [x] Implement exact Candidate-C transfer background adapter.
- [x] Implement/test 12x12 closure plus held-out Bianchi diagnostic.
- [x] Add independent De Felice high-k regression.
- [x] Diagnose local 8D modes: radiation correct, helicity-0 missing.
- [x] **T1a** — self-consistent dust+dust Candidate-C comparison.
- [x] **T1b** — primary-source audit of Comelli equations and De Felice target.
- [ ] **T1c — Reproduce Comelli Case-C B.5 from the direct equations using a dynamically on-shell early-time background.** IN PROGRESS.
  - [x] T1c.1 — identify that the old frozen-`a` epsilon family violates background conservation.
  - [x] T1c.2 — derive the exact dynamically on-shell `a1`-only relation `xi(a)` and early-time `a(tau),xi(tau)` series.
  - [x] T1c.3 — verify the leading dynamic background satisfies both fluid conservations and yields a nontrivial gravitational kernel.
  - [x] T1c.4 — show the first Fredholm compatibility reduces to a single kernel-amplitude relation rather than the previous off-shell contradiction.
  - [x] **T1c.5 — audit the complete A.12/A.16 spatial equations from primary source, including every anisotropic/spatial-gradient term before slip reduction.** Result: post-slip trace implementation is complete; no missing explicit `k^2` block.
  - [ ] **T1c.6 — eliminate nondynamical variables as differential operators on the dynamic Case-C series, then derive the E equation before substituting `D->qk`. Acceptance: recover B.5 and high-k `3q^2-2`.**
  - [ ] T1c.7 — verify the result is invariant under Bianchi-redundant row representatives and under consistent A.18 derivation bookkeeping.
- [ ] **T2 — Apply the validated reduction to dust+dust Candidate C and recover the independent De Felice gravity speed.**
- [ ] **T3 — Identify the exact structural mistake in the current 12x12 closure by term-by-term comparison with the validated reduction.**
- [ ] **T4 — Implement corrected `numerics/comelli_native_scalar.py`.**
- [ ] **T5 — Make `tests/test_comelli_native_scalar.py` green and add >=3 additional `(z,k)` high-k regressions.**
- [ ] **T6 — Re-run all Gate-2B constraint/acceleration/Bianchi tests; no regression allowed.**
- [ ] **T7 — Only then build the time-domain transfer RHS and integrate a fundamental transfer matrix.**
- [ ] **T8 — Track the GR-connected/adiabatic mode continuously; do not define it merely by `delta_g=delta_f`.**
- [ ] **T9 — Compute `T_gg`, `T_gf`, `T_fg`, `T_ff` and relative-mode growth over the linearly stable interval.**
- [ ] **T10 — Record Gate-2B pass/fail/inconclusive verdict with numerical tolerances and domain.**

## Current RED regression

`tests/test_comelli_native_scalar.py` imports the not-yet-created `numerics/comelli_native_scalar.py` and requires a native scalar gravity pair matching De Felice at Candidate C. Do not implement around this test until T1c is closed.

## Immediate restart instruction

**Resume at T1c.6.**

1. Use the dynamically on-shell Case-C branch above. Never vary epsilon at frozen `a`.
2. The full A.12/A.16 spatial audit is complete; do not reopen it unless a new contradiction points there.
3. Keep `Phi1`, `Phi2`, `F1`, `F2`, shifts and matter variables until differential elimination is complete. In particular, do not set the potentials to zero merely because B.5 decouples after reduction.
4. Keep the equations as differential operators during constraint elimination. Do **not** substitute `s=qk` until a reduced E equation has been obtained.
5. Use `E_N=E/tau^2` and the consistent early-time background series.
6. Acceptance is Comelli B.5; for `w1=1/3,w2=0,f1=f2`, the sub-horizon E equation must give factor `3q^2-2`.
7. Do not delete A.17, tune coefficients, or change physical signs merely to fit the target.
8. Update this file immediately after every new hard ruling.
9. Only after B.5 is recovered move to T2 Candidate C.