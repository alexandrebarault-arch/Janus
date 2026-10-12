# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main`
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc` (PR #2)
Latest completed implementation checkpoint: `af50032a23acaf58d134df16ed2e599cdbe087d9`

Purpose: **first file to read after any interruption**. Update it whenever the active blocker changes.

## Repository policy

- `main` remains the stable pre-V2 baseline.
- `research/v2-flrw` is the single canonical active research line.
- `research/gate2b-nonhomothetic-transfer` is historical after PR #2; do not add work there.
- PR #1 remains a draft research PR and is not evidence that JANUS-R is validated.
- Do not create another long-lived branch unless an experiment truly needs isolation.
- GitHub Actions/workflows are intentionally disabled and are not verification evidence.

## Scientific state

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN_AND_SCIENTIFICALLY_MEANINGFUL`

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / NOT VALIDATED`

The direct Comelli closure is a closed negative route. The active route remains an independent action reconstruction checked against De Felice et al. 1404.0008 and Lagos & Ferreira 1610.00553.

## Established action results

TDD history:

- RED `b12ad1d95cde5926bdbc4896454cdc4f352274cd` -> GREEN `0448eef3ad05f6937aca8fadcab9a04d4916c712`: scalar P(X) matter action;
- RED `3e13f971447213d3510c940303330355383c7eff` -> GREEN `d26017a1b65e391d9cb80edc75ca308829819d20`: g/f lapse, scale and volume normalization;
- RED `b44f8305af9b501076629a033214e8e00523eb87` -> GREEN `6057075a9f3bf64763a05d4cd796ce7cf7da9e09`: first metric + two-matter assembly and auxiliary elimination;
- RED `4f32b85f9bee546910568cfcaa7051baf06ac726` -> GREEN `796662db13fc3aec595bbcd99fec87e164a13122`: remove obvious metric-only matter double counting and recover rank-3 kinetic structure on the proportional control;
- RED `0a75660a0048edb433a23a8ef8b83164e0bb3cfe` -> GREEN `af50032a23acaf58d134df16ed2e599cdbe087d9`: correct two independent Lagos interaction coefficients directly from Eqs. (3.6)-(3.8).

The two coefficient corrections are:

1. metric-1 shift self term: `r^2 Z/[2(Nbar+r)] k^2 B1^2` (an `r` factor was missing);
2. common-normalized metric-2 `Z_tilde` self term: `2 r Z_tilde Psi2(3 Psi2/2 + b^2 k^2 E2)` (the previous `Nbar^2 r^5` factor was wrong).

A direct independent evaluator of Lagos Eqs. (3.6)-(3.8) confirms these discrepancies and agrees with the other tested interaction structures.

Fresh reconstructed targeted verification after these corrections: `15 passed` (not a clean full-repository suite).

## Current hard failure / active blocker

The frozen quadratic-pencil solver is now informative because it independently recovers both matter characteristics and tracks them when the probe sound speeds are changed. On Candidate-C backgrounds it finds:

- g-fluid branch: correct intrinsic sound characteristic;
- f-fluid branch: correct intrinsic sound characteristic including the f-lapse rescaling;
- third scalar branch: still lacks the required `omega ~ k` helicity-0 propagation and behaves as a finite mass/time-scale mode at high k.

Independent De Felice benchmark remains nonzero, e.g. at `a=0.5`, `c_grav^2 ~= 0.6920799927` (`c_grav ~= 0.83191345` in the physical normalization). The current assembled Lagos route therefore **still fails the decisive gravity-gradient check**.

Important convention diagnostic: do **not** introduce a `Phi_DF = Phi_L/2` correction. The text extraction of Lagos Eq. (2.21) can drop the printed factor 2; its ADM relation `delta N1=Phi1` and Lagos' other presentation show the standard `1+2 Phi` convention. Current `Phi_DF = Phi_L` is the consistent bridge.

### Leading root-cause hypothesis now being tested

Lagos Eqs. (3.6)-(3.8) are background-reduced for a setup with matter coupled to metric 1. Extending that already-reduced action to **two separately coupled matter sectors** by appending a symmetric f-sector matter remainder may omit background-reduced metric terms required by the second matter sector. This is now more plausible than a pencil/eigensolver error because the two matter speeds are recovered correctly while the gravity branch is not.

## Ordered task queue

### P0 — repository/restart hygiene

- [x] Audit branches and PRs; consolidate Gate 2B into `research/v2-flrw` without touching `main`.
- [x] Remove the accidental no-diff head commit from the earlier session.
- [ ] Keep this file current after every hard result.

### P1 — exact double-matter scalar action

- [x] P1a: one-sector P(X) scalar quadratic action.
- [x] P1b: g/f volume and lapse normalization.
- [ ] **P1c — REOPENED / ACTIVE:** establish the exact two-matter metric+matter quadratic action without relying on a one-matter background reduction.
- [ ] P1d: derive physical high-k kinetic/gradient system and recover all three scalar characteristics.

Immediate P1c sequence:

1. [x] term-by-term Lagos interaction audit; commit the two proven coefficient corrections;
2. [ ] construct an independent two-matter reference action directly from the underlying Hassan-Rosen/De Felice formulation, or equivalently rederive the background-reduced metric terms with both matter sectors present;
3. [ ] compare that reference action term-by-term with `lagos_two_matter_action.py`;
4. [ ] add RED tests for every missing/different term before correcting production code;
5. [ ] re-run auxiliary rank, matter speeds and Candidate-C gravity speed.

### P2 — physical high-k scalar acceptance

Must pass all:

1. exactly three physical scalar modes after gauge/constraint reduction;
2. positive kinetic signs on the tested healthy branch;
3. g and f matter speeds correct;
4. Candidate-C gravity scalar speed agrees with independent De Felice at `a=1,0.5,0.2` within documented tolerance;
5. radiation stays `c_s^2=1/3` and dust limit does not create a fake relativistic sound mode.

If the gravity characteristic still fails after an independently reconstructed two-matter action, stop transfer work and reassess the whole scalar-action bridge.

### P3 — only after P2 passes

Construct the non-homothetic transfer solver, continuous mode tracking, `T_gg,T_gf,T_fg,T_ff`, relative-mode growth and health diagnostics.

### P4 — nonlinear wall gate

Only after the scalar gate is understood decide whether to execute:

`UPSTREAM BUILD -> ZERO-F REGRESSION -> G-ONLY CONTROL -> F-ONLY DUAL CONTROL -> TWIN WALL -> RESOLUTION/COURANT MATRIX`

## Stop conditions

Strongly downgrade/stop JANUS-R if robust independent checks show unavoidable ghost/gradient instability, no viable healthy non-homothetic region, negligible exact segregation unless excluded modified gravity is introduced, or a convergent twin-wall pathology absent in one-sector controls.

## Resume protocol after interruption

1. Read this file first.
2. Read `LATEST.md` and `research/GATE2B_CHECKPOINT.md`.
3. Confirm active branch `research/v2-flrw` and inspect commits after `af50032a23acaf58d134df16ed2e599cdbe087d9`.
4. Resume **P1c**, specifically the independent two-matter reference action / background-reduction audit.
5. Do not alter the quadratic pencil merely to force the benchmark; its matter-characteristic controls currently pass.
6. Before stopping, record exact result, commit SHA, tests/tolerances and the next blocker here.
