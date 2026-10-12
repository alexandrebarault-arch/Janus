# JANUS-R — Latest checkpoint

Date: 2026-10-12
Canonical branch: `research/v2-flrw`
Draft PR to `main`: `#1`
Authoritative interruption/restart queue: `research/RESTART_TASKS.md`

Read `research/RESTART_TASKS.md` first after any interruption. Read `RESUME.md` for the broader history, `research/VERDICT_V2_JANUS.md` for the literal-Janus conclusion, and `research/GATE2B_CHECKPOINT.md` for the active scalar gate.

## Current conclusion

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`.

If forced into a binary true/false decision on Jean-Pierre Petit's published Janus model today, this research selects:

**MOST LIKELY FALSE OR FUNDAMENTALLY INCOMPLETE AS WRITTEN.**

Main reasons remain:

- the published nonlinear cross-sector interaction is not specified in a complete general form;
- the constrained-variation route does not uniquely establish the claimed two independent field equations;
- healthy ghost-free two-metric reconstruction does not recover a universal exact `+G/-G` law;
- fundamental negative mass is not required by the surviving physics and adds theoretical burden;
- isolated positive-energy twin matter does not reproduce the claimed negative photon lensing in the healthy reconstruction;
- no complete CMB+BAO+SN+growth+lensing validation of literal Janus has been established.

However:

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN_AND_SCIENTIFICALLY_MEANINGFUL`.

The surviving descendant is **not literal Janus**. JANUS-R uses a ghost-free Hassan-Rosen bimetric skeleton with two positive-energy matter sectors, each minimally coupled to its own metric. It does not impose fundamental negative mass, a universal exact `+G/-G` force law, or isolated negative photon lensing by twin matter.

## Git/research consolidation

The former Gate-2B branch was merged into `research/v2-flrw` through PR #2 at merge commit `35f5edc19443a059308e8c2710deb656bfdd8fbc`.

Audit on 2026-10-12 confirms:

- `main` = stable pre-V2 baseline;
- `research/v2-flrw` = single canonical active research line;
- `research/gate2b-nonhomothetic-transfer` = redundant historical branch whose head `fd430d73ed7e8c4638b6d94ba1c46f54fba3f5b5` is already a parent of the consolidation merge; no new work belongs there;
- intended final structure is only `main` + `research/v2-flrw`;
- branch deletion itself is not exposed by the current GitHub connector, so the historical ref remains only as a frozen cleanup item;
- PR #1 is the only open PR, remains draft, and must not be interpreted as model validation.

GitHub Actions/workflows remain intentionally disabled and are not evidence.

## Pre-evolution nonlinear-wall preparation already passed

- two-matter time-symmetric spherical constraint solve: `PASS`;
- positive-matter segregated initial data: `PASS_IN_PRINCIPLE`;
- reference central-f / g-shell wall has positive conformal factors: `PASS`;
- exact initial two-matter lapse-ratio gate: `PASS_PRE_EVOLUTION`;
- finite same-oriented lapse basin exists: `PASS`;
- twin-fluid standard-3+1 source/lapse patch prepared against pinned upstream;
- static source-coverage audit: `PASS_STATIC_AUDIT`;
- exact zero-f input projection and output comparator implemented;
- g-only and exact sector-dual f-only controls generated;
- checked symmetric g/f initial constraint solutions exchange sectors to machine precision.

Pinned upstream remains:

`nubirel/bim-solver@8852e8e9921edeeedf1a447d3bf27b82ec24433c`

## Gate 2B exact scalar-action status

The direct Comelli closure is a closed negative route. The independent Lagos/De Felice action route has reached:

- independently reconstructed pure-metric scalar action;
- algebraic lapse/shift elimination;
- rank-one pure-metric scalar kinetic direction on proportional controls;
- independent De Felice Candidate-C gravity-speed benchmark;
- full one-sector P(X) scalar matter quadratic action;
- explicit g/f lapse, scale-factor and volume normalization;
- first two-matter assembly and rank-3 reduced kinetic structure;
- a frozen quadratic-pencil diagnostic that correctly recovers and tracks both matter characteristics;
- two independently proven Lagos interaction-coefficient corrections.

Latest focused verification before this documentation pass was `15 passed`; this is **not** a clean full-repository-suite result.

### Hard failure

The third scalar characteristic still does not recover the physical helicity-0 `omega ~ k` propagation. At Candidate-C `a=0.5`, the independent target remains approximately

`c_grav^2 = 0.6920799927` (`c_grav = 0.83191345`).

The current assembled branch behaves instead like a finite mass/time-scale mode at high `k`.

### Leading root cause

The current two-matter bridge subtracts the complete zero-matter-perturbation part of De Felice Eq. (54), assuming that those metric-only matter terms are already contained in the Lagos metric block, then restores only the lapse susceptibility `(rho+P) Phi^2/(2 c_s^2)`.

That assumption is now reopened. `pure_metric_lagrangian_healthy()` is explicitly EH + interaction and its own implementation notes that at least a matter-background lapse correction is not included. The priority is therefore to determine whether the bridge has **over-subtracted metric-only matter structures** needed for the gravity gradient.

The independent Eq. (54) audit target, before multiplication by `N a^3`, is

`C_Phi Phi^2 - (rho/2) k^2 B_DF^2 + P[3 psi_DF^2/2 - k^4 E_DF^2/6] - 3 rho Phi psi_DF`,

with

`C_Phi = rho/2 + (rho+P)/(2 c_s^2)`.

This is a diagnostic derivation, not yet a justified production patch.

## Immediate next action

**Do not return to literal Janus. Do not return to the failed Comelli closure. Do not add another root scan. Do not tune the quadratic pencil.**

Resume `P1c.1 / T1c.6o.5c-R`:

1. map the full De Felice Eq. (54) metric-only remainder into Lagos variables for the g sector;
2. independently map the f sector with its own lapse/scale/volume factors;
3. add a RED diagnostic showing which shift/spatial/`Phi*psi`/lapse structures the current `full - metric_only + background_lapse` bridge removes;
4. reconstruct the two-matter background reduction independently and classify every difference;
5. correct only terms proven genuinely missing;
6. re-check matter characteristics and the De Felice gravity benchmark at `a=1,0.5,0.2`.

Only if the scalar gate passes should the expensive nonlinear spherical sequence be executed:

`UPSTREAM BUILD -> ZERO-F REGRESSION -> G-ONLY CONTROL -> F-ONLY DUAL CONTROL -> TWIN WALL -> RESOLUTION/COURANT MATRIX`.

## Research decision

- Literal Janus: **conclusion reached; do not spend more effort rescuing its negative-mass / exact +/-G formulation absent genuinely new mathematics.**
- JANUS-R: **continue only as targeted falsification-driven R&D.**
- Current blocker: **exact two-matter background-reduced scalar action, with metric-only matter over-subtraction as the leading hypothesis.**
- PR #1 remains draft and must not be merged as a validated cosmological model.