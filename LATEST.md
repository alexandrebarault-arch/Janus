# JANUS-R — Latest checkpoint

Date: 2026-10-11
Branch: `research/v2-flrw`
Draft PR: `#1`

Read `RESUME.md` for the full scientific history, then read this file for the newest execution boundary.

## Current scientific branch

Only the following continuation remains serious:

`ENVIRONMENT_DEPENDENT_NONLINEAR_JANUS_R`

- ghost-free Hassan-Rosen bimetric skeleton;
- two positive-energy matter sectors, each minimally coupled to its own metric;
- no literal fundamental negative mass requirement;
- no claim of universal exact `+G/-G`;
- no claim that isolated twin matter gives negative photon lensing;
- nonlinear/screened relative-mode wall is the decisive object.

## What is already passed before evolution

- two-matter time-symmetric spherical constraint solve: `PASS`;
- reference central-f / g-shell wall has positive conformal factors: `PASS`;
- exact initial two-matter lapse-ratio gate: `PASS_PRE_EVOLUTION`;
- finite same-oriented lapse basin exists: `PASS`;
- twin-fluid standard-3+1 source/lapse patch prepared against pinned upstream;
- static source-coverage audit for STD + explicit RK + `constg`: `PASS_STATIC_AUDIT`;
- exact zero-f upstream input projection implemented;
- cell/time/field zero-f output comparator implemented;
- runtime analyzer now checks constraints, lapse orientation, metric positivity, non-negative densities, physical radial speeds and separate g/f rest-mass drift;
- Actions/workflows intentionally removed/disabled. Do not use CI as evidence.

## Pinned upstream

`nubirel/bim-solver@8852e8e9921edeeedf1a447d3bf27b82ec24433c`

The current sandbox cannot resolve `github.com` from its local compiler environment, and the GitHub connector does not expose repository-archive download. Therefore the upstream C++ checkout has **not** been compiled here.

## One-command executable gate

Once a pristine pinned checkout is available locally, run from the Janus repository environment:

```bash
python -m tools.run_a1_gate /path/to/bim-solver /path/to/a1-work
```

The runner performs, in order:

1. pinned-upstream manifest verification;
2. untouched STD Release-equivalent C++ build;
3. exact common zero-f initial-state generation;
4. untouched upstream zero-f run;
5. in-place audited twin-fluid source preparation;
6. patched C++ rebuild;
7. patched zero-f run;
8. cell-by-cell/time-by-time regression over all common fields;
9. full reference twin-wall run;
10. physical-domain/constraint/conservation summary.

It deliberately stops with an error if the zero-f regression fails.

## Manual TDD evidence for newest infrastructure

Module-level only; not a C++ build:

- `upstream_baseline_input`: RED missing module -> GREEN `4 passed in 0.03s`;
- `run_a1_gate`: RED missing module -> GREEN `3 passed in 0.03s`;
- analyzer health calculations: focused numerical checks confirm 1% density change -> 1% rest-mass drift and zero->nonzero sector leakage -> infinite relative drift.

Do not convert these into a claim that the full branch or C++ solver passes.

## Latest research notes

- `research/V2_A1_RUNTIME_HEALTH_GATE.md`
- `research/V2_DYNAMIC_LITERATURE_BOUNDARY.md`
- `research/V2_NR_CONTROL_MATRIX.md`
- `research/V2_TWIN_FLUID_NR_RUNBOOK.md`

## Immediate next action

**Do not add another algebraic root scan.**

The next scientifically valid action is executable evidence from the pinned STD solver:

`UPSTREAM BUILD -> ZERO-F REGRESSION -> F-ONLY DUAL CONTROL -> TWIN WALL -> RESOLUTION/COURANT MATRIX`.

If A/B/C controls fail, fix the implementation/numerics before interpreting D.
If D alone develops a convergent wall-localized pathology while controls remain healthy, that counts against JANUS-R.
If D survives, move the resolved background to the full seven-DOF spherical stability machinery before any observational claim.
