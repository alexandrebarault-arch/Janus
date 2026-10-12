# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main`
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc` (PR #2)
Scientific implementation checkpoint before repository-hygiene pass: `af50032a23acaf58d134df16ed2e599cdbe087d9`
Repository/restart consolidation checkpoints: `8e9257719f95066c0b109501f0da77ce75bf1438`, `a616e8752d9ecb6daa69aee0448c8d684134eb91`, `523db21d7a7cb9c5ba60f370c042f922a251eeab`

Purpose: **first file to read after any interruption**. It is the authoritative queue. Update it whenever a hard result, blocker, branch policy, or verified test result changes.

## 0 — Resume in one minute

1. Work only from `research/v2-flrw` unless a genuinely isolated experiment requires a short-lived branch.
2. Read this file, then `LATEST.md`, then `research/GATE2B_CHECKPOINT.md`.
3. Do **not** return to literal published Janus, the failed direct Comelli closure, or another algebraic root scan.
4. Resume **P1c**, specifically the independent reconstruction of the full two-matter quadratic action and its background reduction.
5. First diagnostic target: determine exactly which metric-only matter terms are already contained in the Lagos background-reduced block and which are currently being removed incorrectly by `numerics/lagos_two_matter_action.py`.
6. Treat `tests/test_lagos_two_matter_action.py::test_metric_only_matter_residual_is_only_the_background_lapse_correction` as a **hypothesis test whose premise is reopened**, not as established physics.
7. Add a RED test before any production-code correction.
8. Before stopping, record exact result, commit SHA, tests/tolerances, and the next single blocker here.

## 1 — Git / repository state

Audit performed 2026-10-12.

Branches observed:

- `main` — stable pre-V2 baseline; keep.
- `research/v2-flrw` — single canonical active research line; keep.
- `research/gate2b-nonhomothetic-transfer` — redundant historical branch; **no unique work remains**.

Why the old Gate-2B branch is redundant:

- its head is `fd430d73ed7e8c4638b6d94ba1c46f54fba3f5b5`;
- merge commit `35f5edc19443a059308e8c2710deb656bfdd8fbc` on `research/v2-flrw` has that commit as a parent;
- therefore all work from that branch is already contained in the canonical line.

Cleanup decision:

- keep `main` + `research/v2-flrw` as the intended two-branch structure;
- delete `research/gate2b-nonhomothetic-transfer` when branch-ref deletion is available; the current GitHub connector can read/move/create refs but does not expose ref deletion;
- until then the historical branch is frozen: **never commit new work to it**.

Pull requests:

- PR #1 is the only open PR, remains **draft**, head `research/v2-flrw` -> base `main`;
- PR #1 must not be interpreted as validation and must not be merged merely for housekeeping.

Repository rules:

- do not create another long-lived research branch;
- GitHub Actions/workflows remain intentionally disabled and are not verification evidence;
- a focused local/reconstructed test run is not a full repository-suite result.

## 2 — Scientific state

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN_AND_SCIENTIFICALLY_MEANINGFUL`

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / NOT VALIDATED`

The direct Comelli closure is a closed negative route. The active route is an independent action reconstruction checked against De Felice et al. 1404.0008 and Lagos & Ferreira 1610.00553.

## 3 — Established results that must not be redone

TDD history:

- RED `b12ad1d95cde5926bdbc4896454cdc4f352274cd` -> GREEN `0448eef3ad05f6937aca8fadcab9a04d4916c712`: scalar P(X) matter action;
- RED `3e13f971447213d3510c940303330355383c7eff` -> GREEN `d26017a1b65e391d9cb80edc75ca308829819d20`: g/f lapse, scale and volume normalization;
- RED `b44f8305af9b501076629a033214e8e00523eb87` -> GREEN `6057075a9f3bf64763a05d4cd796ce7cf7da9e09`: first metric + two-matter assembly and auxiliary elimination;
- RED `4f32b85f9bee546910568cfcaa7051baf06ac726` -> GREEN `796662db13fc3aec595bbcd99fec87e164a13122`: remove obvious metric-only matter double counting and recover rank-3 kinetic structure on the proportional control;
- RED `0a75660a0048edb433a23a8ef8b83164e0bb3cfe` -> GREEN `af50032a23acaf58d134df16ed2e599cdbe087d9`: correct two Lagos interaction coefficients directly from Eqs. (3.6)-(3.8).

Proven Lagos coefficient corrections:

1. metric-1 shift self term: `r^2 Z/[2(Nbar+r)] k^2 B1^2` (an `r` factor had been missing);
2. common-normalized metric-2 `Z_tilde` self term: `2 r Z_tilde Psi2(3 Psi2/2 + b^2 k^2 E2)` (the previous `Nbar^2 r^5` factor was wrong).

A direct independent evaluator of Lagos Eqs. (3.6)-(3.8) agrees with the corrected interaction structures tested so far.

Fresh targeted verification after those corrections: `15 passed` — **not** a clean full-repository suite.

## 4 — Current hard failure

The frozen quadratic-pencil solver is informative rather than the leading suspect:

- g-fluid characteristic is recovered correctly;
- f-fluid characteristic is recovered correctly, including f-lapse rescaling;
- changing probe sound speeds moves those two roots as expected;
- the third scalar branch still does **not** show the required `omega ~ k` helicity-0 propagation and instead behaves like a finite mass/time-scale mode at high k.

Independent De Felice Candidate-C benchmark remains nonzero. At `a=0.5`:

- `c_grav^2 ~= 0.6920799927`;
- `c_grav ~= 0.83191345` in the physical normalization.

Therefore the current assembled Lagos route still fails the decisive gravity-gradient check.

Do not introduce a `Phi_DF = Phi_L/2` patch. The consistent bridge remains `Phi_DF = Phi_L`.

## 5 — Leading root-cause hypothesis

The current implementation contains an internal assumption that now needs to be falsified directly:

- `numerics/lagos_two_matter_action.py` says the Lagos metric block already contains metric-only matter terms and therefore subtracts `Eq.(54)` evaluated at zero matter perturbation;
- `numerics/lagos_scalar_action.py` constructs `pure_metric_lagrangian_healthy()` from an Einstein-Hilbert self-action plus interaction terms, and its own documentation explicitly notes that at least the metric-1 matter-background `Phi1^2` correction is not included there.

That makes over-subtraction of background-reduced matter terms the current **P1 hypothesis** for the missing gravity gradient.

### Exact Eq. (54) zero-matter-perturbation diagnostic

Independent algebraic expansion of the implemented De Felice Eq. (54), with the matter perturbation and its rate set to zero, gives before multiplication by the background volume `N a^3`:

`C_Phi Phi^2 - (rho/2) k^2 B_DF^2 + P[3 psi_DF^2/2 - k^4 E_DF^2/6] - 3 rho Phi psi_DF`,

with

`C_Phi = rho/2 + (rho+P)/(2 c_s^2)`.

Using the current bridge implemented in `lagos_two_matter_action.py`,

- `B_DF = B_L/a`,
- `psi_DF = -Psi_L - k^2 E_L/3`,
- `E_DF = 2 E_L`,
- `Phi_DF = Phi_L`,

the same expression becomes exactly

`[rho/2 + (rho+P)/(2 c_s^2)] Phi^2`
` - rho k^2 B^2/(2 a^2)`
` + P[3 Psi^2/2 + k^2 Psi E - k^4 E^2/2]`
` + 3 rho Phi Psi + rho k^2 Phi E`.

The current compatibility remainder restores only

`(rho+P) Phi^2/(2 c_s^2)`.

Therefore the structures presently removed by the bridge, before deciding whether background equations legitimately absorb them, are:

1. `+ rho Phi^2/2`;
2. `- rho k^2 B^2/(2 a^2)`;
3. `+ P[3 Psi^2/2 + k^2 Psi E - k^4 E^2/2]`;
4. `+ 3 rho Phi Psi`;
5. `+ rho k^2 Phi E`.

For the f sector the same bracket must be evaluated with its own scale factor `b=a*r`, lapse `Nbar`, matter background and then weighted by its own volume `Nbar*b^3`; after common normalization by `a^3` this introduces the expected `Nbar*r^3` volume factor.

**Do not add these five structures blindly.** Some can be hidden by the background Friedmann/acceleration equations used in the Lagos reduction. The task is to prove the accounting term by term.

### Test that currently bakes in the reopened assumption

`tests/test_lagos_two_matter_action.py::test_metric_only_matter_residual_is_only_the_background_lapse_correction`

currently asserts that only the susceptibility term remains. This test is no longer an acceptance oracle. P1c.1 must first replace/reframe it with an independent reference-action diagnostic. Do not delete it merely to make a new implementation pass; the old behavior should remain visible as a regression/control branch until the reference derivation settles the issue.

## 6 — Ordered task queue

### P0 — repository/restart hygiene

- [x] Audit branches and PRs.
- [x] Prove old Gate-2B branch is fully contained in `research/v2-flrw`.
- [x] Define intended two-branch policy: `main` + `research/v2-flrw`.
- [ ] Delete historical branch when a ref-delete capability is available.
- [x] Harden this restart ledger with exact SHAs, hard failure, no-go routes, and next diagnostic.
- [ ] Keep this file current after every hard result.

### P1 — exact double-matter scalar action

- [x] P1a: one-sector P(X) scalar quadratic action.
- [x] P1b: g/f volume and lapse normalization.
- [ ] **P1c — ACTIVE:** establish the exact two-matter metric+matter quadratic action without relying on an unjustified one-matter background reduction.
- [ ] P1d: derive the physical high-k kinetic/gradient system and recover all three scalar characteristics.

Immediate P1c sequence — execute in this order:

1. [x] audit Lagos interaction coefficients and commit the two proven corrections;
2. [x] derive and algebraically verify the complete zero-matter-perturbation part of implemented De Felice Eq. (54), including its exact Lagos-variable mapping;
3. [ ] **P1c.1 — CURRENT:** build an independent reference for which of the five removed metric structures survive the Lagos background reduction; start with the one-matter g sector, then independently derive the f sector;
4. [ ] P1c.2: add RED diagnostics that compare the reference action against `full - metric_only + background_lapse`, without modifying production code first;
5. [ ] P1c.3: classify every difference against `lagos_two_matter_action.py` as background-equation equivalent, convention-equivalent, or genuinely missing;
6. [ ] P1c.4: correct production code only for differences proven genuine, one RED->GREEN change at a time;
7. [ ] P1c.5: re-run auxiliary Hessian rank, proportional exchange symmetry, matter speeds, and Candidate-C gravity speed;
8. [ ] P1c.6: if gravity still lacks `omega ~ k`, derive the principal action directly from the unreduced two-matter theory and stop treating Lagos (3.6)-(3.8) as a safe two-matter starting point.

### P2 — physical high-k scalar acceptance

All must pass:

1. exactly three physical scalar modes after gauge/constraint reduction;
2. positive kinetic signs on the tested healthy branch;
3. g and f matter speeds correct;
4. Candidate-C gravity scalar speed agrees with the independent De Felice benchmark at `a=1,0.5,0.2` within documented tolerance;
5. radiation stays `c_s^2=1/3` and the dust limit does not create a fake relativistic sound mode.

If the gravity characteristic still fails after an independently reconstructed two-matter action, stop transfer work and reassess the scalar-action bridge itself.

### P3 — only after P2 passes

Construct the non-homothetic transfer solver, continuous mode tracking, `T_gg,T_gf,T_fg,T_ff`, relative-mode growth and health diagnostics.

### P4 — nonlinear wall gate

Only after the scalar gate is understood decide whether to execute:

`UPSTREAM BUILD -> ZERO-F REGRESSION -> G-ONLY CONTROL -> F-ONLY DUAL CONTROL -> TWIN WALL -> RESOLUTION/COURANT MATRIX`.

## 7 — Stop conditions

Strongly downgrade/stop JANUS-R if robust independent checks show any of:

- unavoidable ghost or gradient instability on the intended branch;
- no viable healthy non-homothetic region;
- segregation negligible unless already-excluded modified-gravity behavior is introduced;
- convergent twin-wall pathology absent in one-sector controls;
- failure of the independently reconstructed two-matter scalar action to recover the known De Felice high-k characteristic.

## 8 — Interruption protocol

Before any pause or context loss:

1. commit or explicitly record uncommitted conceptual work;
2. update the completed checkbox and exact active checkbox here;
3. write the latest tested SHA(s);
4. record the exact test command/result, or state explicitly that no executable full-suite verification was possible;
5. record one sentence beginning `NEXT:` with the single next operation;
6. never leave the next agent to infer whether a negative result was already established.

**NEXT:** execute P1c.1: derive from the original one-matter background reduction which of the five explicitly identified Eq. (54) metric structures are already absorbed by the Lagos metric coefficients; then derive the f-sector accounting independently before writing any production correction.