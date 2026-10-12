# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main`
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc`
Last scientific implementation checkpoint before this diagnostic pass: `af50032a23acaf58d134df16ed2e599cdbe087d9`

Purpose: **first file to read after any interruption**. Update it after every hard result, blocker, branch-policy change, or verified test result.

## 0 — Resume in one minute

1. Work only from `research/v2-flrw` unless a genuinely isolated short experiment requires otherwise.
2. Read this file, then `research/GATE2B_ACTION_RECONSTRUCTION.md`, `research/GATE2B_CHECKPOINT.md`, and `LATEST.md`.
3. Do **not** return to literal published JANUS, the failed direct Comelli closure, a new algebraic root scan, or coefficient/sign tuning.
4. The previous P1c.1 suspicion — blindly missing De Felice Eq. (54) metric-only terms — is **closed as the leading cause**. Lagos' one-matter background reduction legitimately absorbs those raw terms; do not add them back by hand.
5. The full frozen quadratic spectral problem, including the antisymmetric mixed `qdot*q` matrix, has been independently reconstructed and still gives the same failure: both matter characteristics propagate correctly, while the third scalar frequency saturates instead of scaling as `omega ~ k`. The spectral solver is therefore **cleared as the leading cause**.
6. Resume the independent **raw two-matter De Felice action route**, starting at A2.4d/A3: EH(g)+EH(f)+exact HR interaction+Eq.(54) for both matter sectors, with Eqs. (13)-(16) used only as background identities.
7. Do not use the one-matter Lagos-reduced metric action as the oracle for the f-matter extension.
8. First production change must still obey TDD: observe a RED diagnostic before changing production code.

## 1 — Git / repository state

Audit repeated 2026-10-12 before this pass:

- `main` — `aead63f4098f0d15a849e579105af034b6317b30`; stable pre-V2 baseline; keep untouched.
- `research/v2-flrw` — canonical active research line; keep.
- `research/gate2b-nonhomothetic-transfer` — `fd430d73ed7e8c4638b6d94ba1c46f54fba3f5b5`; redundant historical branch, fully absorbed by merge `35f5edc19443a059308e8c2710deb656bfdd8fbc`; freeze and delete when ref deletion is available.

PR #1 remains draft, head `research/v2-flrw` -> base `main`. Do not merge it as housekeeping and do not interpret it as validation.

GitHub Actions/workflows remain intentionally disabled. A local/reconstructed diagnostic is not a full repository-suite result.

## 2 — Scientific status

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN / FALSIFICATION-DRIVEN`

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / NOT VALIDATED`

The current blocker is precise: the assembled two-matter scalar action reproduces the two matter characteristics but not the known Hassan-Rosen helicity-0 high-k gravity characteristic.

Independent De Felice Candidate-C benchmark at `a=0.5`:

- `c_grav^2 ~= 0.6920799927`
- `c_grav ~= 0.83191345`

## 3 — Established results that must not be redone

TDD history already completed:

- RED `b12ad1d95cde5926bdbc4896454cdc4f352274cd` -> GREEN `0448eef3ad05f6937aca8fadcab9a04d4916c712`: scalar P(X) matter action.
- RED `3e13f971447213d3510c940303330355383c7eff` -> GREEN `d26017a1b65e391d9cb80edc75ca308829819d20`: g/f lapse, scale and volume normalization.
- RED `b44f8305af9b501076629a033214e8e00523eb87` -> GREEN `6057075a9f3bf64763a05d4cd796ce7cf7da9e09`: first metric + two-matter assembly and auxiliary elimination.
- RED `4f32b85f9bee546910568cfcaa7051baf06ac726` -> GREEN `796662db13fc3aec595bbcd99fec87e164a13122`: remove obvious metric-only matter double counting and recover rank-3 kinetic structure on the proportional control.
- RED `0a75660a0048edb433a23a8ef8b83164e0bb3cfe` -> GREEN `af50032a23acaf58d134df16ed2e599cdbe087d9`: correct two Lagos interaction coefficients from Eqs. (3.6)-(3.8).

Proven Lagos coefficient corrections:

1. metric-1 shift self term: `r^2 Z/[2(Nbar+r)] k^2 B1^2`;
2. common-normalized metric-2 `Z_tilde` self term: `2 r Z_tilde Psi2(3 Psi2/2 + b^2 k^2 E2)`.

Last targeted repository verification before this diagnostic pass: `15 passed`; this was **not** a clean full-repository suite.

## 4 — P1c.1 result: the five raw Eq. (54) structures are not a patch

The zero-matter-perturbation part of implemented De Felice Eq. (54), mapped to current Lagos variables, is

`[rho/2 + (rho+P)/(2 c_s^2)] Phi^2`
` - rho k^2 B^2/(2 a^2)`
` + P[3 Psi^2/2 + k^2 Psi E - k^4 E^2/2]`
` + 3 rho Phi Psi + rho k^2 Phi E`.

Earlier we flagged five structural families apparently removed by `full - metric_only + background_lapse`. The source-level one-matter audit now changes that interpretation:

- Lagos' reduced metric block has already used the background equations and contains/cancels the metric-only matter pieces;
- for a canonical scalar the explicit residual is `(rho+P) Phi^2/2`;
- the general P(X) extension is `(rho+P) Phi^2/(2 c_s^2)`;
- therefore the current g-sector subtraction logic is conceptually consistent with the one-matter Lagos reduction.

**Do not add the five raw structures back individually.** Exploratory insertion of full raw metric-only terms does not restore the gravity characteristic and can introduce/remove spurious branches.

The f-sector local normalization itself is also consistent:

- `B_DF = B_f / b` with `b=a*r`;
- f matter volume is `Nbar*b^3`, hence common normalization `Nbar*r^3` after division by `a^3`;
- no extra `1/kappa` multiplies the raw f matter action when all matter densities are expressed in `M_g` normalization.

But this does **not** prove that a one-matter Lagos background-reduced metric block can simply be extended by a second f matter remainder. That generalization is now the leading structural suspect.

## 5 — Convention audit closed

Do not introduce `Phi_DF = Phi_L/2`.

The consistent bridge remains `Phi_DF = Phi_L`. A text extraction of the Lagos metric appeared to lose a factor of two, but the action coefficients settle the convention: De Felice's `2 H Phi Tr(Hdot)` with `Tr H = -6 Psi + ...` and the overall EH `1/2` reproduces the Lagos `-6 H Phi Psidot` coefficient used in the code.

## 6 — Spectral solver audit: leading suspicion cleared

De Felice's reduced scalar action has the generic form

`L = 1/2 qdot^T K qdot + qdot^T C q + 1/2 q^T Q q`,

with the physical antisymmetric mixed matrix `A = C - C^T` (equivalent to the paper's antisymmetric `N`). The frozen-background characteristic is therefore not merely `det(-omega^2 K + M)=0`; the `i omega A` term is required.

An independent reconstruction of the current repository action included this full mixed term and solved the generalized quadratic eigenproblem. At Candidate C, `a=0.5`, with deliberately regular probe sound speeds `c_g^2=0.4`, `c_f^2=0.3`:

- background: `y=0.5682421398850359`, `ctilde=0.9370868721221998`, `Nbar=0.5324922494728938`;
- at `k=1000`, positive frequencies are approximately `86.36`, `1029.82`, `1264.92`;
- physical g-time speeds `omega*a/k` are approximately `0.04318`, `0.51491`, `0.63246`;
- g matter target `sqrt(0.4)=0.63246`: recovered;
- f matter target `ctilde*sqrt(0.3) ~= 0.513`: recovered;
- gravity target `~0.83191`: **not recovered**.

High-k sequence for the third branch:

- `k=250`: `omega ~ 81.97`, `omega a/k ~ 0.16394`;
- `k=500`: `omega ~ 85.51`, `omega a/k ~ 0.08551`;
- `k=1000`: `omega ~ 86.36`, `omega a/k ~ 0.04318`;
- `k=2000`: `omega ~ 86.56`, `omega a/k ~ 0.02164`.

Thus `omega` saturates near a finite mass/time scale while the physical propagation speed tends to zero. This reproduces the existing hard failure even with the correct mixed matrix.

**Conclusion:** do not modify/tune the spectral solver to force the benchmark. The defect is upstream in the action/background reduction.

This diagnostic was performed in an independent reconstructed calculation, not by a clean full-repository pytest run.

## 7 — Raw De Felice two-matter route is now authoritative

The existing detailed checkpoint `research/GATE2B_ACTION_RECONSTRUCTION.md` already contains the correct independent route. Reactivate it.

Primary raw ingredients:

1. EH quadratic action for g and f separately (De Felice Eq. 44 and f analogue).
2. Exact Hassan-Rosen interaction quadratic action (De Felice Eqs. 45-46), not a one-matter reduced Lagos block.
3. P(X) matter action Eq. (54), independently for g and f.
4. Background identities Eqs. (13)-(16) and healthy-branch relation only after the raw pieces are assembled.
5. Gauge-reduce/eliminate lapses and shifts, then compare the three physical high-k characteristics with De Felice Eq. (86).

Useful background identities for flat Candidate C (`K=0`):

- `m^2 rhohat_g = 3 H^2 - rho_g/M_g^2`;
- `m^2 rhohat_f = 3 kappa H_f^2 - rho_f/M_g^2`;
- `Hdot/N = 1/2 [m^2 xi J (ctilde-1) - (rho_g+P_g)/M_g^2]`;
- `Hfdot/n = -1/2 [m^2 J (ctilde-1)/(kappa xi^3 ctilde) + (rho_f+P_f)/(kappa M_g^2)]`.

These allow a raw action benchmark without guessing beta-to-U normalization inside intermediate determinant terms.

## 8 — Ordered task queue

### P0 — repository/restart hygiene

- [x] audit branches/PRs and freeze redundant historical branch;
- [x] harden restart ledger;
- [ ] delete historical branch only when ref-delete capability exists;
- [ ] keep this file current after every hard result.

### P1 — exact two-matter scalar action

- [x] P1a: one-sector P(X) scalar quadratic action.
- [x] P1b: g/f local matter lapse/scale/volume normalization.
- [x] P1c.1: audit the five apparent Eq. (54) metric-only terms; **closed: not a valid add-back patch**.
- [x] P1c.2: audit `Phi` factor-of-two convention; **closed: `Phi_DF=Phi_L`**.
- [x] P1c.3: audit full quadratic spectral solver including antisymmetric mixed term; **closed: solver still reproduces hard failure, so it is not the leading cause**.
- [ ] **P1c.4 / A2.4d — ACTIVE:** reconstruct raw two-matter De Felice quadratic action in one normalization using EH(g)+EH(f)+HR+matter(g)+matter(f), with background identities applied only after assembly.
- [ ] A3: eliminate `Phi,varphi,B,b` and the remaining nondynamical scalar after g-flat gauge reduction.
- [ ] A4: recover exactly three high-k scalar characteristics and compare at Candidate C `a=1,0.5,0.2`.
- [ ] A5: exact Case-C regression.
- [ ] A6: only after A4/A5 pass, compare the validated reduction back to Lagos/Comelli and localize the missing structure.

### P2 — physical acceptance

All must pass:

1. exactly three physical scalar modes after constraints/gauge reduction;
2. positive kinetic signs on the tested healthy branch;
3. g and f matter speeds correct;
4. Candidate-C gravity scalar speed agrees with independent De Felice at `a=1,0.5,0.2` within documented tolerance;
5. radiation remains `c_s^2=1/3` and the dust limit is taken only after constrained reduction, without a fake relativistic dust mode.

If the independently reconstructed raw action itself cannot reproduce Eq. (86), stop transfer work and audit the raw transcription/conventions before any phenomenology.

### P3 — only after P2 passes

Construct non-homothetic transfer/mode tracking and the segregation observables.

## 9 — Interruption protocol

Before any pause/context loss:

1. commit or explicitly record conceptual work;
2. update completed/active checkboxes here;
3. record the exact active SHA(s);
4. record exact test/diagnostic commands and results, or explicitly say verification was reconstructed/not full-suite;
5. record one sentence beginning `NEXT:`;
6. never leave a future restart to infer whether a negative result was already established.

**NEXT:** implement the raw De Felice two-matter scalar benchmark in g-flat gauge from Eqs. (44)-(46) + Eq. (54), first as a testable independent oracle. Observe a RED high-k Candidate-C gravity-speed regression before any production correction to the Lagos bridge.