# V2 A1 — Runtime health and exact-baseline readiness

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `READY_TO_EXECUTE__CXX_RUNTIME_NOT_YET_RUN`

Read `RESUME.md` first. This checkpoint records the last work that can be verified without materializing and compiling the pinned GPL upstream solver.

## 1. Exact upstream regression input is now defined

Pinned upstream:

`nubirel/bim-solver@8852e8e9921edeeedf1a447d3bf27b82ec24433c`

The untouched standard-3+1 `fld::bimInput` order is exactly 22 fields after the radius:

`gA,gB,gK,gKD,gDA,gDB,gSig,`

`fA,fB,fK,fKD,fDA,fDB,fSig,`

`q,gAlp,fAlp,gDAlp,p,`

`pfD,pfS,pftau`.

The prepared twin-fluid patch appends only

`pfFD,pfFS,pfFtau`

to that initial-data layout.

Therefore a strict zero-f regression can use **the exact same geometry, lapses, separation and g-fluid state** and produce the upstream input merely by deleting those three trailing zero columns.

Implemented in:

- `numerics/upstream_baseline_input.py`
- `tests/test_upstream_baseline_input.py`.

The converter refuses a patched state if any of the three twin-fluid conserved variables is nonzero, preventing an accidental invalid upstream comparison.

Manual focused TDD evidence from the available Python environment:

- RED before module implementation: expected `ModuleNotFoundError`;
- GREEN after implementation: `4 passed in 0.03s`.

This is module-level evidence only, not a C++ regression.

## 2. Static source-coverage audit

A repository-wide search of the pinned upstream for the standard-fluid variables `pfD`, `pfS`, and `pftau` was repeated.

For the **standard 3+1 + explicit RK + `constg` slicing** path selected for A1, the matter-dependent locations are the seven already covered by the prepared patch:

1. `src/bim-solver-std.cpp`
2. `include/eom-std/eomMatter.h`
3. `include/eom-std/eomSources.h`
4. `include/eom-std/eomConstraints.h`
5. `include/eom-std/eomMiscEquations.h`
6. `include/eom-std/eomEvolution.h`
7. `include/eom-std/eomLapseRatios.h`

The only additional standard-3+1 block containing explicit g-fluid assumptions is `include/maximalSlice.h`.

That file is intentionally **not used** in the first experiment:

- the reference config uses `slicing.method = constg`;
- the upstream file itself contains `TODO/fixme` warnings about its physical source/factor;
- the A1 protocol uses the general bimetric lapse ratio instead.

BSSN and generated DIRK Jacobian files also contain g-fluid assumptions but are outside A1 by design. They must be addressed only if the first explicit standard-3+1 wall survives.

Decision:

`SOURCE_COVERAGE_CONSTG_EXPLICIT_STD = PASS_STATIC_AUDIT`

This is not a compiler proof.

## 3. Runtime analyzer hardened to the scientific stop conditions

`tools/analyze_bim_solver_output.py` already monitored:

- `C_1..C_4`;
- same-oriented lapse ratio `W=gAlp/fAlp > 0`;
- separation `p`;
- metric ratio `R=fB/gB`;
- initial rest-dust momentum identities.

It now additionally monitors the quantities required by the A2 protocol before any physical interpretation:

### Spatial metric domain

Require

`gA>0, gB>0, fA>0, fB>0`

throughout the interior grid.

Outputs:

- `metric_min_factor` per frame;
- `metric_positive` per frame and globally.

### Dust-density domain

Require conserved Valencia densities

`pfD >= 0`, `pfFD >= 0`.

Outputs:

- minimum and maximum magnitude per sector/frame;
- `density_nonnegative` per frame and globally.

### Physical radial speed

Since the radial spatial metric is `gamma_rr=A^2`, the physical Eulerian radial speed magnitude is monitored as

`|A_g v_g|`, `|A_f v_f|`.

Require strictly subluminal values before interpretation.

Outputs:

- `g_speed_max`, `f_speed_max`;
- `fluid_subluminal` per frame and globally.

### Independent rest-mass conservation

For the spherical Valencia conserved variable `D`, the diagnostic rest mass is

`M0 = 4 pi integral D r^2 dr`.

The absolute number is grid/convention dependent; the useful gate is its **relative drift on the same grid**.

Outputs:

- `rest_mass_g`, `rest_mass_f` per frame;
- `rest_mass_g_rel_drift_max`;
- `rest_mass_f_rel_drift_max`.

A sector that starts exactly empty is treated specially: remaining exactly empty gives zero drift; spontaneous appearance of finite conserved mass gives infinite relative drift and cannot be hidden by division through an epsilon.

Focused numerical checks confirm that a 1% injected density change produces a 1% mass-drift diagnostic and that zero-to-nonzero leakage is flagged as infinite drift.

New regression tests:

- `tests/test_analyze_bim_solver_health.py`.

Full branch CI is **not** claimed because GitHub Actions/workflows are disabled and the current execution environment cannot materialize the upstream C++ repository.

## 4. Upstream build command is simple but remains unexecuted here

The pinned CodeBlocks project specifies for the standard Release target:

- C++14;
- `-O3`;
- OpenMP;
- `-m64`;
- `-DV_SIGN=-`;
- `-DCFDS_ORDER=4`;
- include path `include`;
- source `src/bim-solver-std.cpp`.

A direct Linux-equivalent build to try in a materialized GPL checkout is therefore approximately:

```bash
g++ -std=c++14 -O3 -fopenmp -m64 -DV_SIGN=- -DCFDS_ORDER=4 \
    -Iinclude src/bim-solver-std.cpp -o bim-solver-std
```

This command is recorded as an execution starting point, **not as a successful build claim**.

The current sandbox still fails DNS resolution for `github.com`, and direct archive retrieval also remains unavailable. Therefore no untouched or patched C++ executable has been produced here.

## 5. Exact next executable sequence

When the pinned upstream checkout can be materialized:

1. compile untouched `bim-solver-STD`;
2. generate a patched reference wall with `pfFD=pfFS=pfFtau=0`;
3. project that same state to the 23-column upstream format with `upstream_baseline_input.py`;
4. run the untouched upstream baseline;
5. verify the upstream manifest and apply `tools/prepare_bim_solver_twin.py`;
6. compile the patched solver;
7. run the exact same zero-f state in patched 26-column form;
8. compare common output fields cell-by-cell/time-by-time, not only summary norms;
9. run the sector-dual f-only control;
10. only after those regressions pass, run the full reference twin wall;
11. use `tools/analyze_bim_solver_output.py` to enforce physical-domain, constraint and conservation gates;
12. repeat vacuum/g-only/f-only/twin controls at at least three resolutions/Courant factors.

## 6. Scientific status

No new evidence here upgrades or downgrades JANUS-R physically.

What changed is experimental readiness:

`A1_ANALYTIC_PATCH = READY`

`A1_EXACT_ZERO_F_BASELINE = READY`

`A1_RUNTIME_HEALTH_ANALYZER = READY`

`A1_UPSTREAM_BUILD = BLOCKED_BY_CURRENT_RUNTIME_NETWORK`

`DYNAMIC_WALL = NOT_RUN`

The first genuine new physics result now requires executable evidence. Static algebra or additional root scans should not substitute for that run.
