# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main` (`aead63f4098f0d15a849e579105af034b6317b30`)
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc`
Current active head before this documentation commit: `a3f0b13ef8e80c1da6449b771d2be0a3a2232bb4`

Purpose: **first file to read after any interruption**.

## 0 — Resume in one minute

1. Work only from `research/v2-flrw`; keep `main` untouched.
2. Do not return to literal published JANUS, the failed direct Comelli closure, blind coefficient/sign tuning, or the old frozen-background pencil.
3. The authoritative scalar route is the independent raw De Felice two-matter action plus the time-dependent physical-variable / BD reduction.
4. Correct equations after quadratic reduction are
   `K qddot + (Kdot + C - C^T) qdot + (Cdot - Q) q = 0`.
5. Physical f-sector scalar in g-flat gauge:
   `Y2hat = u_f - (Sigma + k^2 S/6)/(n H_f)` with the full `Rdot` term retained in `u_f_dot`.
6. Candidate-C `a=0.5` remains a passing 3-mode regression.
7. The former `a=0.2` catastrophic high-k failure is now **GREEN** after replacing nested finite-difference reduction by direct joint quadratic assembly + matrix Schur reduction + explicit derivative of the null-coordinate Schur complement.
8. The old exact Eq. (86) gravity target at Candidate-C `a=0.2` must **not** be used as an acceptance oracle for the arbitrary probe speeds `c_g^2=0.4`, `c_f^2=0.3`; those probes are not a self-consistent single-P(X) realization of the actual matter+radiation / dust background.
9. The independent Eq. (86) oracle is now validated separately with a self-consistent constant-w P(X) control in `numerics/de_felice_consistent_px_control.py`.
10. NEXT: freeze the `a=1` regression and verify gravitational kinetic signs against De Felice Eq. (80)/(82) at all accepted epochs; then compare the validated raw route back to Lagos and identify exactly what the old transfer code loses.

## 1 — Git / repository state

- `main` — stable pre-V2 baseline; untouched.
- `research/v2-flrw` — canonical active line.
- `research/gate2b-nonhomothetic-transfer` — historical/redundant; fully absorbed; frozen until ref deletion is available.
- PR #1 remains draft (`research/v2-flrw` -> `main`); do not merge as model validation.
- GitHub Actions/workflows remain intentionally disabled.

Latest relevant lineage:

- `64bfd19a184a7df39b9d075822f9a621c62fd59f` — RED Eq. (44) Fourier shift-cancellation regression.
- `7d9f57d8a892cf51c1c9823b9c74655f2e914e71` — GREEN Eq. (44) `B*E_dot` sign fix.
- `0ba69ef36b0396fc5eb7457f6fda52e21a95a445` — RED generic time-dependent BD reduction.
- `a2e47995bec88d61501e36da8c02b83333420edf` — GREEN generic null-coordinate reduction + `Y2hat` map.
- `afce1faaf404393b03f89e1d33534e37f81be737` — RED null-Schur conditioning regression.
- `e865ccf3e1fc4eb6c7191cec3aebc7cc814d0ea5` — GREEN local conditioning scale.
- `2553b53bd8a2a9aac8482300651602d3ad0360c2` — RED Candidate-C physical 3-mode regression.
- `cebd1e2b04c7a7b0ae1c2deb9d8dcc7246efae7e` — GREEN Candidate-C `a=0.5` benchmark.
- `fb75b9614e82ab986ec135472b4fcb38ddf51525` — first RED `a=0.2` regression (later corrected because its exact gravity oracle was invalid for arbitrary probes).
- `0a5d730e1730bb76631b5a7f4f121d8b75ba18cb` — detailed early-epoch diagnostic note.
- `e3fcdcd6f8315c6438c7df952b45e283887fe146` — RED self-consistent P(X) control.
- `d334a89031949fa6f19ef38275fce0dce25b00af` — GREEN self-consistent P(X) control.
- `fc91cde90609c2e860cd82cb3bb4636e9604a79f` — corrected `a=0.2` RED: finite/mode-complete conditioning gate only, no invalid Eq. (86) target.
- `a3f0b13ef8e80c1da6449b771d2be0a3a2232bb4` — GREEN stabilized Candidate-C time-dependent scalar reduction.

## 2 — Scientific status

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN / FALSIFICATION-DRIVEN`

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / RAW ROUTE NOW MULTI-EPOCH NUMERICALLY STABLE, FINAL SIGN/MAPPING CHECKS PENDING`

The healthy Hassan-Rosen two-matter scalar route survives the helicity-0 gate. This does **not** rescue literal JANUS.

## 3 — Raw-action facts closed unless contradicted

- Eq. (54) P(X) matter action implemented independently.
- `Phi_DF = Phi_L`; no `/2` patch.
- f volume relative to g: `ctilde*xi^4`.
- f EH relative weight: `kappa*ctilde*xi^4`.
- no ad hoc f-matter `1/kappa` factor.
- Eq. (44) Fourier cross coefficient: `-2 k^4 B E_dot/(3 N a)`.
- pure-E `B E_dot` cancellation under the De Felice/Lagos bridge is exact.
- de Sitter EH/background-determinant mapping to Lagos is exact.
- proportional HR relative block maps exactly to the healthy Lagos interaction.
- Minkowski Eq. (44)+Fierz-Pauli gives high-k `c_s^2=1`.

Important subtlety retained:

- Eq. (54) uses `delta phi_dot / phi_dot_0`.
- if `u = delta phi / phi_dot_0`, then on an evolving background `delta phi_dot / phi_dot_0 = u_dot + (phi_ddot_0/phi_dot_0)u`.
- the Candidate-C probe benchmark uses arbitrary sound speeds on a background that is not a pair of single P(X) fluids, so its gravity branch is a conditioning/mode-completeness diagnostic, not an exact Eq. (86) target.
- exact Eq. (86) comparison is instead delegated to the self-consistent P(X) control.

## 4 — Why the old route failed

Two separate failures were found and closed:

1. **Frozen-background BD reduction** — removing the kinetic-null coordinate after freezing loses `Kdot`, `Cdot` and `Rdot` contributions and produces a false finite-frequency third branch.
2. **Nested finite differences** — the Candidate-C implementation then differentiated coefficient matrices that had themselves been constructed by finite differencing an already reduced Lagrangian. At early epochs/high k this produced a spurious branch of order `~5.8`.

The stabilized implementation now:

- forms one joint quadratic Hessian in auxiliaries + physical coordinates + rates;
- eliminates lapse/shift by a direct matrix Schur complement;
- differentiates the resulting primary `K,C,Q` matrices in `x=ln a`;
- differentiates the null-coordinate Schur complement explicitly;
- rescales the geometric direction using `k^2 S` before the eigensolve.

No physical coefficient is tuned.

## 5 — Independent self-consistent P(X) control

Implementation: `numerics/de_felice_consistent_px_control.py`.
Tests: `tests/test_de_felice_consistent_px_control.py`.

The control uses constant barotropic fluids `w_g=c_g^2=0.4`, `w_f=c_f^2=0.3`, solves the bimetric background self-consistently, and uses the correct Eq. (54) field-velocity variable.

Representative non-homothetic checks:

- `a=0.50`: Eq. (86) target `~0.67503`, raw route tends to `~0.6752`.
- `a=0.40`: target `~0.48017`, raw route `~0.48070` at k=1800.
- `a=0.35`: target `~0.35817`, raw route `~0.35762` at k=1800.
- `a=0.30`: target `~0.22337`, raw route `~0.22314` at k=1800.

This closes the previous suspicion that the `~1e-3` Candidate-C early gravity bias required an HR coefficient patch. It does not.

## 6 — Current targeted verification

Local reconstructed command:

`python -m pytest -q tests/test_time_dependent_quadratic_reduction.py tests/test_de_felice_raw_scalar_action.py tests/test_de_felice_candidate_c_reduction.py tests/test_de_felice_consistent_px_control.py`

Result after `a3f0b13...`: **`19 passed in 0.23s`**.

This is **not** a clean full-repository-suite result.

## 7 — Multi-epoch A4 status

### `a=0.5`

PASS. Existing exact-probe regression remains within committed tolerance after the stabilization.

### `a=0.2`

PASS for the correct acceptance question: three finite oscillatory scalar branches remain present at high k; the two independently imposed matter characteristics are recovered; the third gravity branch stays regular rather than blowing up.

Do **not** require the arbitrary-probe Candidate-C gravity branch to equal Eq. (86) exactly.

### `a=1`

Still needs a committed robust regression. Previous preliminary result was close (`~7.6e-4` gravity-speed error under the older route), but this must be recomputed with the stabilized implementation before acceptance.

## 8 — Ordered task queue

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
- [x] identify null BD direction.
- [x] time-dependent null-coordinate elimination.
- [x] `Y2hat` + `Rdot`.
- [x] physical 3x3 Euler-Lagrange system.
- [x] remove nested finite-difference conditioning failure.

### A4 — high-k falsification gate

- [x] `a=0.5` three-mode regression.
- [x] `a=0.2` finite/mode-complete high-k regression.
- [x] independent self-consistent P(X) Eq. (86) gravity control on non-homothetic backgrounds.
- [x] recover both matter characteristics in the stabilized route.
- [ ] **ACTIVE:** recompute and freeze robust `a=1` regression with stabilized reduction.
- [ ] verify gravitational kinetic sign against independent De Felice Eq. (80)/(82) at accepted epochs.
- [ ] add step/window robustness regression for the stabilized coefficient derivatives.

### A5/A6 — only after A4 closes

- [ ] compare validated raw reduction back to Lagos/old transfer.
- [ ] identify exactly which time-dependent/null-mode terms old production transfer lost.
- [ ] repair Lagos production transfer with RED/GREEN tests.
- [ ] only then resume JANUS-R phenomenology / nonlinear-wall work.

## 9 — Interruption protocol

Before any pause:

1. update this file;
2. record exact commit SHAs;
3. record exact targeted commands/results or state full-suite execution is unavailable;
4. state rejected experiments as well as accepted ones;
5. end with one explicit `NEXT:` instruction.

**NEXT:** using the stabilized reduction at `a3f0b13ef8e80c1da6449b771d2be0a3a2232bb4`, recompute Candidate-C `a=1`, add a committed acceptance regression if stable, then compare physical kinetic eigenvalues at `a=1,0.5,0.2` against the independent De Felice Eq. (80)/(82) no-ghost sign benchmark. Do not return to Lagos production repair until these A4 checks are closed.
