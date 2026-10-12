# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main`
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc` (PR #2)
Latest completed implementation checkpoint: `796662db13fc3aec595bbcd99fec87e164a13122`

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

JANUS-R keeps only the healthy descendant: ghost-free Hassan-Rosen bimetric gravity, two positive-energy matter sectors, separate minimal couplings, and no imposed universal exact `+G/-G` force law.

### Gate 2B

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / NOT VALIDATED`

The direct Comelli reduction is a closed negative route. The independent Lagos/De Felice quadratic-action route is active.

Established before the current checkpoint:

- independent De Felice high-k coefficients reproduce the Candidate-C scalar-speed benchmark;
- Lagos pure-metric scalar action has been reconstructed independently;
- `Phi1,Phi2,B1,B2` are algebraic auxiliaries;
- the proportional-background pure-metric post-auxiliary scalar velocity Hessian has rank one.

## Latest hard result — corrected two-matter action bridge

TDD history on `research/v2-flrw`:

- RED `b12ad1d95cde5926bdbc4896454cdc4f352274cd` -> GREEN `0448eef3ad05f6937aca8fadcab9a04d4916c712`: scalar specialization of De Felice Eq. (54);
- RED `3e13f971447213d3510c940303330355383c7eff` -> GREEN `d26017a1b65e391d9cb80edc75ca308829819d20`: explicit g/f `N a^3` normalization;
- RED `b44f8305af9b501076629a033214e8e00523eb87` -> GREEN `6057075a9f3bf64763a05d4cd796ce7cf7da9e09`: initial metric + two-matter assembly and algebraic auxiliary elimination;
- RED `4f32b85f9bee546910568cfcaa7051baf06ac726` -> GREEN `796662db13fc3aec595bbcd99fec87e164a13122`: fix the Lagos/De Felice matter split and preserve the physical scalar kinetic degeneracy.

The important debugging result was that adding the complete De Felice Eq. (54) on top of the background-reduced Lagos metric action double-counted metric-only matter terms. That incorrect bridge produced a reduced velocity Hessian of rank 6. Lagos explicitly puts the metric-only matter pieces in its metric block and separates the terms involving the matter perturbation. The corrected bridge therefore adds:

1. only the `delta_phi`-dependent difference of the De Felice matter action;
2. the residual background lapse susceptibility `(rho+P) Phi^2/(2 c_s^2)` in each sector's own volume measure;
3. the exact scalar-variable conversion between the Lagos and De Felice decompositions.

On the proportional control used by the regression, the corrected six-variable post-auxiliary velocity Hessian has eigenvalues numerically

`~{0,0,0,9.0823,26.0576,83.2826}`

and therefore rank 3, matching two matter scalars plus one helicity-0 gravity scalar. The three nonzero directions are positive on this control.

Fresh reconstructed focused verification after the correction:

`13 passed in 0.37 s`

This is **not** a clean checkout/full repository test run; do not describe the whole suite as green.

## Ordered task queue

### P0 — repository/restart hygiene

- [x] Audit branch structure and PR state.
- [x] Confirm both research branches forked from the same `main` commit.
- [x] Consolidate Gate 2B into `research/v2-flrw` through PR #2 without touching `main`.
- [x] Remove a redundant no-diff head commit created during the matter-normalization update.
- [ ] Keep this file current after every meaningful result.

### P1 — complete the double-matter scalar action

- [x] **P1a / T1c.6o.5a:** one-sector barotropic/P(X) scalar quadratic action.
- [x] **P1b / T1c.6o.5b:** independent g/f lapse, scale-factor and volume normalization.
- [x] **P1c / T1c.6o.5c:** metric + g matter + f matter in one normalization; algebraic elimination of `Phi1,Phi2,B1,B2`; zero-matter and exchange controls; corrected no-double-counting matter bridge.
- [ ] **P1d / T1c.6o.5d — ACTIVE BLOCKER:** derive the physical principal kinetic/gradient system and recover the g-fluid, f-fluid and gravity high-k propagation eigenvalues without inserting the De Felice answer.

P1d immediate sequence:

1. [x] verify the reduced velocity Hessian has rank 3 on a proportional two-matter control;
2. [ ] construct the full frozen-background quadratic principal form, including velocity-position mixing;
3. [ ] project/eliminate the three zero-kinetic constraint/gauge directions without imposing the desired eigenvalues;
4. [ ] recover the two intrinsic matter speeds with the correct f-lapse rescaling;
5. [ ] recover the gravity scalar speed and compare only afterwards to the independent De Felice benchmark;
6. [ ] repeat at Candidate-C `a=1,0.5,0.2` and document tolerances.

### P2 — physical high-k scalar acceptance

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
4. Confirm the active branch is `research/v2-flrw` and inspect commits after `796662db13fc3aec595bbcd99fec87e164a13122`.
5. Resume **P1d / T1c.6o.5d**, starting from construction of the full frozen-background quadratic principal form.
6. Before stopping, record the exact result, commit SHA, test status, numerical tolerance and next blocker here.
