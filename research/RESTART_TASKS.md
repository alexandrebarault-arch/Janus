# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main` (`aead63f4098f0d15a849e579105af034b6317b30`)
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc`

Purpose: **first file to read after any interruption**.

## 0 — Resume in one minute

1. Work only from `research/v2-flrw`; keep `main` untouched.
2. Do not return to literal published JANUS, the failed direct Comelli closure, blind coefficient/sign tuning, or the old pre-BD frozen pencil.
3. The authoritative scalar route is the independent raw De Felice two-matter action plus a **time-dependent physical-variable/BD reduction**.
4. The old “third scalar frequency saturates” failure was mainly caused by freezing the background before removing the null BD coordinate. The correct Euler-Lagrange system uses
   `K qddot + (Kdot + C - C^T) qdot + (Cdot - Q) q = 0`.
5. Physical f-sector variable in g-flat gauge:
   `Y2hat = u_f - (Sigma + k^2 S/6)/(n H_f)`.
   With `R=1/(n H_f)`, retain
   `u_f_dot = Y2hat_dot + R(Sigma_dot+k^2 S_dot/6) + Rdot(Sigma+k^2 S/6)`.
6. Candidate-C `a=0.5` is a **committed passing 3-mode regression**: both matter modes and the De Felice helicity-0 speed are recovered.
7. Candidate-C `a=0.2` now has a **committed RED** (`fb75b9614e82ab986ec135472b4fcb38ddf51525`): production nested finite-difference reduction becomes non-physical at high k.
8. Read `research/A4_A02_DIAGNOSTIC.md` before touching the early-epoch reduction. A stable local matrix prototype removes the catastrophic conditioning failure, but still leaves an unexplained `~1e-3` gravity-speed bias and is therefore **NOT GREEN**.
9. NEXT: remove the ambiguity caused by the current inconsistent probe-fluid embedding. Build a self-consistent single-P(X) control or an analytic matter-eliminated principal-symbol control; only then decide whether the residual gravity bias is source/reduction error and promote the stable matrix route with RED/GREEN tests.

## 1 — Git / repository state

- `main` — stable pre-V2 baseline; untouched.
- `research/v2-flrw` — canonical active line.
- `research/gate2b-nonhomothetic-transfer` — historical/redundant; fully absorbed; frozen until ref deletion is available.
- PR #1 remains draft (`research/v2-flrw` -> `main`); do not merge as model validation.
- GitHub Actions/workflows remain intentionally disabled.

Latest implementation / diagnostic lineage:

- `64bfd19a184a7df39b9d075822f9a621c62fd59f` — RED Eq. (44) Fourier shift-cancellation regression.
- `7d9f57d8a892cf51c1c9823b9c74655f2e914e71` — GREEN fix of Eq. (44) `B*E_dot` sign.
- `0ba69ef36b0396fc5eb7457f6fda52e21a95a445` — RED generic time-dependent BD reduction.
- `a2e47995bec88d61501e36da8c02b83333420edf` — GREEN generic time-dependent null-coordinate reduction and `Y2hat` map.
- `afce1faaf404393b03f89e1d33534e37f81be737` — RED null-Schur conditioning-scale regression.
- `e865ccf3e1fc4eb6c7191cec3aebc7cc814d0ea5` — GREEN local null-block conditioning scale.
- `2553b53bd8a2a9aac8482300651602d3ad0360c2` — RED Candidate-C physical 3-mode regression.
- `cebd1e2b04c7a7b0ae1c2deb9d8dcc7246efae7e` — GREEN Candidate-C `a=0.5` physical 3-mode benchmark.
- `fb75b9614e82ab986ec135472b4fcb38ddf51525` — RED Candidate-C `a=0.2` three-mode gate.
- `0a5d730e1730bb76631b5a7f4f121d8b75ba18cb` — diagnostic note freezing the early-epoch conditioning/source audit.

## 2 — Scientific status

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN / FALSIFICATION-DRIVEN`

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / NOT YET MULTI-EPOCH VALIDATED`

Important change: the raw healthy Hassan-Rosen two-matter scalar action **does recover the known helicity-0 high-k mode when reduced correctly**. This does not rescue literal JANUS; it means the healthy JANUS-R scalar route survives this gate so far.

## 3 — Raw-action facts now closed

Do not redo these unless new contradictory evidence appears:

- The five raw Eq. (54) metric-only structures are not a blind add-back patch; Lagos' one-matter background reduction absorbs/cancels them.
- `Phi_DF = Phi_L`; no `/2` convention patch.
- f volume relative to g is `ctilde*xi^4`.
- f EH relative weight is `kappa*ctilde*xi^4`.
- f matter carries no ad hoc `1/kappa`.
- Correct Eq. (44) Fourier cross term is `-2 k^4 B E_dot/(3 N a)`.
- Under the De Felice/Lagos bridge, the pure-E `B E_dot` term cancels exactly.
- On de Sitter, the source-level EH plus the background determinant term maps exactly to the Lagos EH block.
- At `ctilde=xi=1`, the raw HR relative block maps exactly to the healthy Lagos interaction block.
- In Minkowski, raw Eq. (44)+Fierz-Pauli gives `omega^2=k^2+m_eff^2` (up to internal mass normalization), hence high-k `c_s^2=1`.

Open subtlety — **do not silently close this**:

- De Felice Eq. (54) uses `delta phi_dot / phi_dot_0`.
- If `u = delta phi / phi_dot_0`, then on an evolving background `delta phi_dot / phi_dot_0 = u_dot + (phi_ddot_0/phi_dot_0) u`.
- The present Candidate-C regression intentionally imposes probe sound speeds on a background that is g=matter+radiation and f=dust, so it is not a self-consistent pair of single P(X) backgrounds. A naive `phi_ddot/phi_dot` add-back was tested locally and rejected as a production patch because it changes the probe embedding itself.

## 4 — Why the old frozen pencil failed

After eliminating `(Phi,B,varphi,b)`, the coordinate basis `(Sigma,S,u_g,u_f)` has a rank-3 kinetic Hessian. Its null direction is precisely the De Felice BD combination.

Eliminating this null coordinate while freezing the background loses terms from the time-dependent variable map and integration by parts. A pre-BD frozen pencil of the form

`det(-omega^2 K - i omega(C-C^T) - Q)=0`

is therefore not the correct gravity-speed oracle.

The generic implementation now lives in `numerics/time_dependent_quadratic_reduction.py`:

- integrate the null-coordinate velocity term by parts;
- use `Cdot` in the null Schur complement;
- eliminate the algebraic null coordinate;
- only then form the physical 3x3 Euler-Lagrange matrices with `Kdot` and `Cdot`.

Pure-gravity analytic control restores exactly

`lim_{k->infinity} omega^2/(k^2/a^2)=1`.

## 5 — Candidate-C committed benchmark

Implementation: `numerics/de_felice_candidate_c_reduction.py`.

Tests: `tests/test_de_felice_candidate_c_reduction.py`.

At `a=0.5`, probes `c_g^2=0.4`, `c_f^2=0.3`, using `k=(100,150,250)` and a linear `1/k^2` extrapolation:

- f matter extrapolation: `~0.51313903`; independent target `ctilde*sqrt(0.3) ~ 0.51326362`;
- g matter extrapolation: `~0.63245555`; target `sqrt(0.4) = 0.63245553`;
- gravity extrapolation: `~0.83187090`; independent De Felice target `sqrt(0.6920799927) = 0.83191345`;
- gravity absolute error: about `4.3e-5`;
- physical 3x3 kinetic matrix is positive in the committed `a=0.5, k=150` regression.

Last clean targeted reconstructed verification **before** adding the new `a=0.2` RED:

`python -m pytest -q tests/test_time_dependent_quadratic_reduction.py tests/test_de_felice_raw_scalar_action.py tests/test_de_felice_candidate_c_reduction.py`

Result on 2026-10-12: **`16 passed in 4.07s`**.

After commit `fb75b...`, the targeted Candidate-C test is intentionally RED at `a=0.2`. Do not quote `16 passed` as current branch status.

## 6 — Multi-epoch A4 status

### `a=1`

Preliminary two-point derivative benchmark:

- independent gravity target `c_grav ~ 0.97345679`;
- extrapolated gravity `~0.97421582`;
- error `~7.6e-4`;
- both matter modes also converge to their independent targets.

Promising, but not yet frozen as an acceptance regression.

### `a=0.2` — ACTIVE BLOCKER / COMMITTED RED

Independent targets for the default probes:

- gravity `c_grav ~ 0.33742855`;
- f matter `ctilde*sqrt(0.3) ~ 0.38012193`;
- g matter `sqrt(0.4) ~ 0.63245553`.

Production reduction with `k=(250,600,1000)` becomes non-physical at high k; one extracted branch grows to `~5.8` instead of approaching the gravity characteristic. This is now frozen by the RED test in `fb75b...`.

Read `research/A4_A02_DIAGNOSTIC.md` for the complete experiment log. Key facts:

- sorting roots only by speed is insufficient because the two slow branches approach/cross;
- nested finite-difference Hessians and time derivatives are the main source of the catastrophic production instability;
- a local direct-matrix/Schur prototype restores three regular branches and stable matter characteristics;
- 70-digit `mpmath` reproduction shows the remaining small gravity bias is **not** ordinary floating-point roundoff;
- at `a=0.2`, the stable prototype tends near `0.339` while Eq. (86) gives `0.33742855`;
- the bias grows with non-homotheticity (`ctilde` farther from 1), localizing the remaining audit to the gravity interaction/background reduction or benchmark embedding;
- no interaction coefficient tuning is allowed.

Do not widen tolerances or cherry-pick favorable k values.

## 7 — Ordered task queue

### A2 — raw action

- [x] Eq. (54) P(X) matter action.
- [x] g/f normalization.
- [x] raw Eq. (44) EH scalar contraction.
- [x] raw Eqs. (45)-(46) HR block.
- [x] full raw g-flat two-matter density.
- [x] Eq. (44) Fourier-sign regression.

### A3 — physical reduction

- [x] eliminate four primary lapse/shift auxiliaries.
- [x] verify reduced rank-3 kinetic structure.
- [x] identify the null BD direction.
- [x] implement/test time-dependent null-coordinate elimination.
- [x] implement/test `Y2hat` including `Rdot`.
- [x] construct physical 3x3 Euler-Lagrange system.

### A4 — high-k falsification gate

- [x] committed `a=0.5` three-mode regression.
- [x] recover g matter speed at `a=0.5`.
- [x] recover f matter speed at `a=0.5`.
- [x] recover De Felice gravity speed at `a=0.5`.
- [x] commit explicit RED for `a=0.2` production failure.
- [x] demonstrate locally that direct matrix assembly removes the catastrophic high-k branch blow-up.
- [x] falsify ordinary double-precision roundoff as the explanation for the residual gravity bias using 70-digit arithmetic.
- [ ] **ACTIVE:** build self-consistent single-P(X) early-epoch control OR matter-eliminated analytic principal-symbol control.
- [ ] decide whether the residual `~1e-3` gravity bias is source/reduction error or inconsistent probe-fluid embedding.
- [ ] GREEN the `a=0.2` committed regression without tolerance inflation.
- [ ] freeze robust `a=1` regression.
- [ ] verify gravitational kinetic sign against the independent De Felice Eq. (80)/(82) benchmark at all accepted epochs.

### A5/A6 — only after A4 passes

- [ ] compare the validated raw reduction back to Lagos/old transfer.
- [ ] identify exactly which time-dependent/null-mode terms the old production transfer lost.
- [ ] repair production transfer code with RED/GREEN tests.
- [ ] only then resume JANUS-R phenomenology/nonlinear-wall work.

## 8 — Preferred next numerical / analytic strategy

For `a=0.2`, priority is now:

1. **Do not implement the local stable matrix prototype in production yet.** It fixes the large conditioning failure but not the independent Eq. (86) agreement to the required standard.
2. Build a self-consistent P(X) control where `(rho,P,c_s^2,phi_dot)` obey Eqs. (18)-(19), or analytically eliminate matter from the high-k principal symbol so the gravity branch can be compared without the arbitrary probe-fluid embedding.
3. Keep mode continuation by eigenvector overlap in physically rescaled coordinates (`u_g`, `Y2hat`, `k^2 S`) as the preferred identification method once the principal-symbol ambiguity is closed.
4. Preserve the already-passing `a=0.5` regression and require step/window stability. No target-driven choice of k, derivative step, polynomial degree, or coefficient scaling.

## 9 — Interruption protocol

Before any pause:

1. update this file;
2. record exact commit SHAs;
3. record exact targeted commands/results or state that full-suite execution is unavailable;
4. state rejected numerical experiments as well as accepted ones;
5. end with one explicit `NEXT:` instruction.

**NEXT:** read `research/A4_A02_DIAGNOSTIC.md`; construct a self-consistent single-P(X) control or an analytic matter-eliminated principal-symbol control for Candidate-C-like non-homothetic backgrounds. Use it to determine whether the residual early-epoch gravity-speed bias is physical/source-level or only caused by the current inconsistent probe-fluid embedding. Only after that turn the stable matrix/Schur prototype into a GREEN production implementation for the committed `a=0.2` RED.
