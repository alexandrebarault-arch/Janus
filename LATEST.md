# JANUS-R — Latest checkpoint

Date: 2026-10-11
Branch: `research/v2-flrw`
Draft PR: `#1`

Read `RESUME.md` for the full scientific history. Read `research/VERDICT_V2_JANUS.md` for the current conclusion on literal Janus.

## Current conclusion

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`.

If forced into a binary true/false decision on Jean-Pierre Petit's published Janus model today, this research selects:

**MOST LIKELY FALSE OR FUNDAMENTALLY INCOMPLETE AS WRITTEN.**

Main reasons:

- Janus 2024 does not specify the exact general nonlinear cross-sector interaction tensor; the paper explicitly leaves that object for possible future construction;
- the 2015 constrained variation does not uniquely derive two independent field equations;
- the exact universal `+G/-G` force law is not recovered in the healthy ghost-free two-metric reconstruction;
- fundamental negative mass is not required by the surviving physics and creates additional theoretical burden;
- isolated positive-energy twin matter does not reproduce Petit's claimed negative photon lensing in the healthy reconstruction;
- a complete CMB+BAO+SN+growth+lensing validation of literal Janus has not been demonstrated.

However:

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN_AND_SCIENTIFICALLY_MEANINGFUL`.

The surviving descendant is **not literal Janus**. It is the repository's `ENVIRONMENT_DEPENDENT_NONLINEAR_JANUS_R` program:

- ghost-free Hassan-Rosen bimetric skeleton;
- two positive-energy matter sectors, each minimally coupled to its own metric;
- no literal fundamental negative mass requirement;
- no imposed universal exact `+G/-G`;
- no claim that isolated twin matter gives negative photon lensing;
- nonlinear/screened relative-mode wall is the decisive object.

## What is already passed before evolution

- two-matter time-symmetric spherical constraint solve: `PASS`;
- regular positive-matter segregated initial data (central f / external g shell): `PASS_IN_PRINCIPLE`;
- reference central-f / g-shell wall has positive conformal factors: `PASS`;
- exact initial two-matter lapse-ratio gate: `PASS_PRE_EVOLUTION`;
- finite same-oriented lapse basin exists: `PASS`;
- twin-fluid standard-3+1 source/lapse patch prepared against pinned upstream;
- static source-coverage audit for STD + explicit RK + `constg`: `PASS_STATIC_AUDIT`;
- exact zero-f upstream input projection implemented;
- cell/time/field zero-f output comparator implemented;
- runtime analyzer checks constraints, lapse orientation, metric positivity, non-negative densities, physical radial speeds and separate g/f rest-mass drift;
- constrained g-only and exact sector-dual f-only initial controls are generated independently;
- g-only and f-only dual constraint solutions exchange metric sectors to machine precision in the checked symmetric setup;
- Actions/workflows intentionally removed/disabled. Do not use CI as evidence.

## New Gate A0 independent check

`numerics/two_sector_initial_constraints.py` implements the Kocic-Torsello-Högås-Mörtsell conformally-flat two-sector Hamiltonian constraints, restoring the f-matter term already present in the general published constraint.

Local TDD:

- RED: `ModuleNotFoundError` before implementation;
- GREEN: `3 passed in 0.51s` after implementation.

Exploratory positive-matter core/shell scan:

- moderate grid: `100/100` converged;
- deliberately strong grid: `47/48` converged.

This confirms only initial-data existence. It does not prove dynamical generation or stability.

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
9. freshly constraint-solved patched g-only control;
10. freshly constraint-solved patched f-only **sector-dual** control with reversed interaction coefficients;
11. full reference twin-wall run;
12. physical-domain/constraint/conservation summaries for the patched controls and twin experiment.

It deliberately stops with an error if the zero-f regression fails. The command also reports a hard physical-domain failure if g-only, f-only or twin evolution leaves the finite/same-oriented/positive-density/positive-metric/subluminal domain.

## Immediate next action

**Do not add another algebraic root scan. Do not attempt to restore literal Janus.**

The only remaining experiment with enough information value to justify further work is:

`UPSTREAM BUILD -> ZERO-F REGRESSION -> G-ONLY CONTROL -> F-ONLY DUAL CONTROL -> TWIN WALL -> RESOLUTION/COURANT MATRIX`.

If controls fail, fix implementation/numerics before interpretation.
If the twin run alone develops a resolution-convergent wall-localized pathology while controls remain healthy, downgrade/stop JANUS-R.
If the twin wall survives, apply the full seven-DOF spherical stability machinery before any observational claim.

## Research decision

- Literal Janus: **conclusion reached; do not spend more research time trying to rescue its negative-mass / exact +/-G formulation unless genuinely new mathematics appears.**
- JANUS-R: **keep only as targeted R&D.**
- PR #1 remains draft and must not be merged as a validated cosmological model.
