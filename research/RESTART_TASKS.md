# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main`
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc` (PR #2)
Latest completed implementation checkpoint: `d26017a1b65e391d9cb80edc75ca308829819d20`

Purpose: **first file to read after any interruption**. Update it whenever the active blocker changes.

## Repository policy

- `main` remains the stable pre-V2 baseline. Do not merge research into `main` merely to reduce branch count.
- `research/v2-flrw` is the single canonical active research line.
- `research/gate2b-nonhomothetic-transfer` is historical after PR #2; do not add new work there.
- PR #1 remains a draft research PR and is not evidence that JANUS-R is a validated cosmological model.
- Do not create another long-lived branch unless an experiment truly needs isolation.
- GitHub Actions/workflows are intentionally disabled and must not be cited as verification evidence.

## Current scientific state

### Literal published Janus

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`

The published literal negative-mass / exact `+G/-G` formulation is not the active rescue target.

### Surviving research program

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN_AND_SCIENTIFICALLY_MEANINGFUL`

The surviving descendant is JANUS-R: ghost-free Hassan-Rosen bimetric gravity, two positive-energy matter sectors, separate minimal couplings, and no imposed universal exact `+G/-G` force law.

### Gate 2B

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / NOT VALIDATED`

The direct Comelli reduction is closed as a negative route: it reproduces the radiation mode but misses the physical helicity-0 gradient. The independent Lagos/De Felice quadratic-action route is active.

Established before the current checkpoint:

- independent De Felice high-k coefficients reproduce the Candidate-C scalar-speed benchmark;
- Lagos pure-metric scalar action has been reconstructed independently;
- lapse/shift auxiliaries are eliminated algebraically from the action;
- the proportional-background post-auxiliary scalar velocity Hessian has rank one;
- the unique pure-metric kinetic direction is the relative scalar metric mode.

## Latest hard result — matter action bridge

TDD commits on `research/v2-flrw`:

- RED `b12ad1d95cde5926bdbc4896454cdc4f352274cd` -> GREEN `0448eef3ad05f6937aca8fadcab9a04d4916c712`: full scalar specialization of De Felice Eq. (54);
- RED `3e13f971447213d3510c940303330355383c7eff` -> GREEN `d26017a1b65e391d9cb80edc75ca308829819d20`: explicit background-volume normalization `N a^3` and g/f coordinate-speed control.

Focused reconstructed local test run: `8 passed`.

The new matter action checks:

- free P(X) scalar: `omega^2 = c_s^2 N^2 k^2/a^2`;
- pure-lapse limit exactly reproduces the pre-existing De Felice Eq. (54) identity;
- shift occurs in the spatial combination `delta_phi/phi_dot_0 + a B/N`;
- scalar metric contractions use `Tr(H)=6 psi` and `H_ij H^ij=12 psi^2+(2/3)k^4 E^2`;
- for the f sector, `b=a r` and `Nbar=r c` give `omega_f^2=c_s,f^2 c^2 k^2/a^2` in the common coordinate time.

Caveat: this is a focused reconstructed test run, not a clean checkout/full repository pytest run. Do not call the whole suite green.

## Ordered task queue

### P0 — repository/restart hygiene

- [x] Audit branch structure and PR state.
- [x] Confirm both research branches forked from the same `main` commit.
- [x] Consolidate Gate 2B into `research/v2-flrw` through PR #2 without touching `main`.
- [x] Remove a redundant no-diff head commit created during the matter-normalization update.
- [ ] Keep this file current after every meaningful result.

### P1 — complete the double-matter scalar action

Goal: add two separately coupled matter sectors and the required background terms to the independent Lagos scalar quadratic action.

- [x] **P1a / T1c.6o.5a:** transcribe and test one-sector barotropic/P(X) scalar quadratic action.
- [x] **P1b / T1c.6o.5b:** establish independent g/f volume and lapse/scale normalization.
- [ ] **P1c / T1c.6o.5c — ACTIVE BLOCKER:** assemble Lagos metric action + g matter + f matter in one common normalization and integrate all nondynamical variables at action level.
- [ ] **P1d / T1c.6o.5d:** derive the principal kinetic/gradient matrices and recover the g-fluid, f-fluid and gravity high-k propagation eigenvalues without inserting the De Felice answer.

P1c acceptance conditions:

1. matter-free limit equals `pure_metric_lagrangian_healthy()` exactly;
2. `Phi1,Phi2,B1,B2` remain algebraic auxiliaries;
3. proportional equal-Planck/equal-matter control is exchange symmetric;
4. common normalization is explicitly derived from `M1^2 a^3`: g matter contributes `8piG * N_g * (...)`, f matter contributes `8piG * Nbar*r^3 * (...)` when `b=a*r`;
5. no failed Comelli closure equation is imported.

### P2 — extract the physical high-k scalar principal system

Acceptance conditions:

1. correct number/rank of propagating scalar modes;
2. no ghost sign in the candidate gravity scalar on the tested healthy branch;
3. Candidate-C gravity scalar speed agrees with independent De Felice at `a=1,0.5,0.2` within a documented tolerance;
4. radiation remains `c_s^2=1/3`;
5. the dust limit does not manufacture a spurious relativistic sound mode.

If these checks fail, stop transfer work and fix the action/convention bridge first.

### P3 — only after P2 passes: construct non-homothetic transfer

Required outputs: common/relative transfer amplitudes vs scale/epoch, kinetic/gradient health along the trajectory, initial-mode sensitivity, and comparison with the frozen/quasi-static bounds.

Decision rule: if the exact healthy transfer cannot generate a phenomenologically relevant relative component without instability or gross observable modifications, downgrade/close the linear-segregation route.

### P4 — reconcile with nonlinear wall evolution

Only after the exact scalar gate is understood, decide whether the existing V2 wall experiment still has enough information value to execute.

Existing sequence:

`UPSTREAM BUILD -> ZERO-F REGRESSION -> G-ONLY CONTROL -> F-ONLY DUAL CONTROL -> TWIN WALL -> RESOLUTION/COURANT MATRIX`

## Stop conditions

Stop or strongly downgrade JANUS-R if robust independent checks show any of:

- unavoidable ghost or gradient instability in the physically relevant scalar branch;
- no viable non-homothetic region after healthy kinetic/gradient conditions;
- exact transfer yields negligible segregation unless already-excluded modified gravity is introduced;
- the twin wall develops a resolution-convergent pathology while g-only and f-only controls remain healthy.

## Resume protocol after interruption

1. Read this file first.
2. Read `LATEST.md` for the broad verdict.
3. Read `research/GATE2B_CHECKPOINT.md` and `research/GATE2B_ACTION_RECONSTRUCTION.md` for the active derivation.
4. Confirm the active branch is `research/v2-flrw` and inspect commits after `d26017a1b65e391d9cb80edc75ca308829819d20`.
5. Resume **P1c / T1c.6o.5c** unless a newer commit in this file says otherwise.
6. Before stopping, record the exact result, commit SHA, test status, tolerance and next blocker here.
