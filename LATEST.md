# JANUS-R — Latest checkpoint

Date: 2026-10-12
Canonical branch: `research/v2-flrw`
Draft PR to `main`: `#1`
Authoritative interruption/restart queue: `research/RESTART_TASKS.md`

Read `RESUME.md` for the full history, `research/VERDICT_V2_JANUS.md` for the literal-Janus conclusion, and `research/GATE2B_CHECKPOINT.md` for the active scalar-action gate.

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

The surviving descendant is **not literal Janus**. JANUS-R uses:

- a ghost-free Hassan-Rosen bimetric skeleton;
- two positive-energy matter sectors, each minimally coupled to its own metric;
- no fundamental negative-mass requirement;
- no imposed universal exact `+G/-G` force law;
- no claim that isolated twin matter gives negative photon lensing.

## Git/research consolidation

The previously separate Gate 2B scalar-action line was merged into `research/v2-flrw` through PR #2 at merge commit `35f5edc19443a059308e8c2710deb656bfdd8fbc`.

Repository policy now is:

- `main` = stable pre-V2 baseline;
- `research/v2-flrw` = one canonical active research line;
- `research/gate2b-nonhomothetic-transfer` = historical only, no new work;
- PR #1 remains draft and must not be interpreted as model validation.

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

GitHub Actions/workflows are intentionally disabled and are not evidence.

## Gate 2B exact scalar-action status

The old direct Comelli scalar closure is a closed negative route: it reproduces the radiation mode but misses the physical helicity-0 gradient.

The independent Lagos/De Felice action route has now reached:

- independently reconstructed pure-metric scalar action;
- algebraic lapse/shift elimination;
- rank-one pure-metric scalar kinetic direction on proportional controls;
- independent De Felice Candidate-C gravity-speed benchmark;
- full one-sector P(X) scalar matter quadratic action;
- explicit g/f lapse, scale-factor and `N a^3` volume normalization.

Latest focused TDD result:

- RED `b12ad1d` -> GREEN `0448eef`: full scalar matter action slice;
- RED `3e13f971` -> GREEN `d26017a1`: two-sector volume/lapse normalization;
- reconstructed focused run: `8 passed`.

This is not a full repository-suite result.

## Immediate next action

**Do not return to literal Janus. Do not return to the failed Comelli closure. Do not add another algebraic root scan.**

Immediate analytic blocker:

`METRIC ACTION + g MATTER + f MATTER -> COMMON NORMALIZATION -> AUXILIARY ELIMINATION -> HIGH-k KINETIC/GRADIENT MATRIX`.

Acceptance before any exact transfer claim:

1. zero-matter limit exactly reproduces the existing pure-metric action;
2. equal-sector proportional control is exchange symmetric;
3. lapse/shift variables remain algebraic;
4. recovered matter speeds are intrinsic (`c_s`) with the correct f-lapse rescaling;
5. the gravitational scalar speed reproduces the independent De Felice Candidate-C benchmark at `a=1,0.5,0.2` without inserting that benchmark into the derivation.

Only if that scalar gate passes should we decide whether to execute the expensive nonlinear spherical sequence:

`UPSTREAM BUILD -> ZERO-F REGRESSION -> G-ONLY CONTROL -> F-ONLY DUAL CONTROL -> TWIN WALL -> RESOLUTION/COURANT MATRIX`.

## Research decision

- Literal Janus: **conclusion reached; do not spend more effort rescuing its negative-mass / exact +/-G formulation absent genuinely new mathematics.**
- JANUS-R: **continue only as targeted falsification-driven R&D.**
- Current next blocker: **T1c.6o.5c / P1c, coupled two-matter action assembly.**
- PR #1 remains draft and must not be merged as a validated cosmological model.
