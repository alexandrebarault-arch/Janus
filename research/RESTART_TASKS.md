# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main`
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc` (PR #2)

Purpose: this file is the first restart point after any interruption. Update it before ending a work session or whenever the active blocker changes.

## Repository policy

- `main` remains the stable pre-V2 baseline. Do not merge research into `main` merely to reduce branch count.
- `research/v2-flrw` is now the single canonical active research line.
- `research/gate2b-nonhomothetic-transfer` is historical after PR #2; do not add new work there.
- PR #1 remains a draft research PR. It is not evidence that JANUS-R is a validated cosmological model.
- Do not create another long-lived branch unless an experiment truly needs isolation. Prefer commits on `research/v2-flrw` with explicit checkpoints.
- GitHub Actions/workflows are intentionally disabled and must not be cited as verification evidence.

## Current scientific state

### Closed conclusion on literal published Janus

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`

The published literal negative-mass / exact `+G/-G` formulation is not the active rescue target. Continue only with the healthy two-positive-sector bimetric descendant when the calculation has enough information value.

### Surviving research program

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN_AND_SCIENTIFICALLY_MEANINGFUL`

The surviving descendant is the repository's JANUS-R program: ghost-free Hassan-Rosen bimetric gravity, two positive-energy matter sectors, separate minimal couplings, and no imposed universal exact `+G/-G` force law.

### Gate 2B status

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / NOT VALIDATED`

The direct Comelli reduction is closed as a negative route: it reproduces the radiation mode but misses the physical helicity-0 gradient. The independent Lagos/De Felice quadratic-action route is the active route.

Already established on the action route:

- independent De Felice high-k principal coefficients reproduce the Candidate-C scalar speed benchmark;
- Lagos pure-metric scalar action has been reconstructed independently;
- lapse/shift auxiliaries are eliminated algebraically from the action;
- the post-auxiliary proportional-background scalar velocity Hessian has rank one;
- the unique kinetic direction is the relative scalar metric mode;
- the one-field pure-metric relative slice is structural only and must not be interpreted as Candidate-C physics before matter and background terms are included.

## Ordered task queue

### P0 — keep the restart point correct

- [x] Audit branch structure and PR state.
- [x] Confirm both research branches forked from the same `main` commit and are independently ahead of it.
- [x] Consolidate Gate 2B into `research/v2-flrw` through PR #2 without touching `main`.
- [ ] At every scientifically meaningful checkpoint, update this file with the newest commit, result, and next single blocker.

### P1 — complete the double-matter scalar action

Goal: add the two separately coupled matter sectors and required background terms to the independent Lagos scalar quadratic action.

Acceptance conditions:

1. matter contributions are derived/implemented without importing the failed Comelli closure;
2. lapse/shift variables remain algebraic auxiliaries and are eliminated at action level;
3. proportional/equal-sector controls preserve exchange symmetry;
4. the matter-free limit reduces exactly to the existing pure-metric implementation;
5. a one-sector-matter control agrees with the corresponding De Felice principal coefficient where the conventions overlap.

### P2 — extract the physical high-k scalar principal system

Goal: identify the reduced physical scalar kinetic/gradient matrices after auxiliary elimination.

Acceptance conditions:

1. correct number/rank of propagating scalar modes for the chosen matter model;
2. no ghost sign in the candidate gravity scalar on the tested healthy branch;
3. Candidate-C gravity scalar speed agrees with the independent De Felice benchmark at `a = 1, 0.5, 0.2` within a documented numerical tolerance;
4. radiation control remains at `c_s^2 = 1/3`;
5. dust controls do not manufacture a spurious relativistic sound mode.

If these checks fail, stop the transfer calculation and fix the action/convention bridge first.

### P3 — only after P2 passes: construct non-homothetic transfer

Goal: evolve the validated reduced scalar system on the Candidate-C background instead of using the failed Comelli closure or the frozen quasi-static proxy.

Required outputs:

- common/relative transfer amplitudes versus scale and epoch;
- kinetic and gradient health diagnostics along the trajectory;
- sensitivity to initial adiabatic/isocurvature content;
- comparison with the existing optimistic frozen/quasi-static bounds.

Decision rule: if the exact healthy transfer cannot generate a phenomenologically relevant relative component without instability or gross observable modifications, downgrade/close the linear-segregation route.

### P4 — reconcile Gate 2B with the nonlinear wall program

Only after the exact scalar gate is understood, decide whether the existing V2 nonlinear wall experiment still has enough information value to justify execution.

The existing V2 executable sequence remains:

`UPSTREAM BUILD -> ZERO-F REGRESSION -> G-ONLY CONTROL -> F-ONLY DUAL CONTROL -> TWIN WALL -> RESOLUTION/COURANT MATRIX`

Do not interpret algebraic scans as a substitute for this evolution test.

## Stop conditions

Stop or strongly downgrade JANUS-R if any of the following is robust under independent reconstruction/checks:

- unavoidable ghost or gradient instability in the physically relevant scalar branch;
- no viable non-homothetic parameter region after enforcing healthy kinetic/gradient conditions;
- exact transfer shows the needed segregation is too small unless already-excluded modified gravity is introduced;
- the twin wall develops a resolution-convergent pathology while g-only and f-only controls remain healthy.

## Resume protocol after interruption

1. Read `research/RESTART_TASKS.md` first.
2. Read `LATEST.md` for the broad V2 verdict.
3. For the active Gate 2B derivation read `research/GATE2B_CHECKPOINT.md` and `research/GATE2B_ACTION_RECONSTRUCTION.md`.
4. Confirm the active branch is `research/v2-flrw` and inspect commits after the checkpoint recorded above.
5. Continue only the first unchecked task in the ordered queue unless new evidence changes the decision tree.
6. Before stopping, record the exact result, commit SHA, failed/passed acceptance test, and next blocker here.
