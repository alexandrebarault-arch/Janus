# V2 Twin-Fluid Numerical-Relativity Runbook

Date: 2026-10-11
Status: `DESIGN_READY__UPSTREAM_BUILD_NOT_YET_EXECUTABLE_IN_CURRENT_SANDBOX`

## Purpose

This is the operational companion to `docs/superpowers/plans/2026-10-11-twin-fluid-nr.md`. It records the exact upstream baseline, the source-level twin-fluid extension points, verification traps, and the shortest path to a falsifiable dynamic wall test.

## Upstream baseline

Repository: `nubirel/bim-solver`

Pinned tree/commit:

`8852e8e9921edeeedf1a447d3bf27b82ec24433c`

License: GPLv3.

Do not copy the upstream source wholesale into this Janus research notebook. Use a separate GPL-compatible fork when execution becomes available.

### Current environment limitation

Direct local clone/download from GitHub failed in the current execution environment with:

`Could not resolve host: github.com`

Therefore no claim is made that the upstream C++ solver has been compiled or run in this session. Source inspection is grounded through the GitHub connector only.

## First formulation to extend

Use **standard 3+1 (`bim-solver-STD`) first**, not cBSSN.

Reasons:

1. It is the formulation used for the published first dust-cloud evolutions (Kocic et al. 2020).
2. The state and matter equations are significantly smaller and easier to audit.
3. The first research gate only asks whether the time-symmetric compensation wall survives a short, resolution-convergent evolution.
4. If that local gate fails robustly, cBSSN complexity is not justified.

Only port to cBSSN after a short standard-3+1 PASS/PARTIAL.

### cBSSN compilation trap

`src/bim-solver-BSSN.cpp` defines `_TEST_MODE=1` by default. The provided CodeBlocks BSSN project does not visibly override it. Any future physics build must explicitly compile with:

`-D_TEST_MODE=0`

and verify the evolved-field list/names before interpreting output.

## Explicit integrator first

The upstream MoL layer provides explicit RK methods (`RK1..RK4`) and adaptive `RKDP45`; DIRK is a separate path.

For the first wall test:

- prefer RK3/RK4 (matching/near the published architecture);
- do not regenerate DIRK Jacobians initially;
- only invoke DIRK work if explicit time integration fails because of demonstrated stiffness rather than a physics/constraint failure.

## Existing standard-3+1 matter architecture

### Single conserved fluid state

`src/bim-solver-std.cpp` currently evolves only one Valencia state:

- `pfD`
- `pfS`
- `pftau`
- primitive `pfv`

and their radial derivatives/RHS.

A second independent state must be added for the `f` fluid.

### Existing g-fluid equations

`include/eom-std/eomMatter.h` contains the dust Valencia equations. In the current conventions:

`v_g = S_g / [(D_g + tau_g) A_g^2]`

`rho_g^m = (D_g + tau_g)/(A_g B_g^2)`

`j_g^m = S_g/(A_g B_g^2)`

`J1_g^m = S_g v_g/(A_g B_g^2)`

`J2_g^m = 0`.

The `f` equations must be the sector-covariant analogue using `fAlp`, `fBet`, `fA`, `fB`, etc. Never reuse g geometry in f hydrodynamics.

## Files with hard-coded one-fluid assumptions

A search for the existing `pf*` state in the standard formulation identifies at least:

1. `src/bim-solver-std.cpp`
   - state registration;
   - evolved/input/output fields;
   - radial derivatives and preparation.
2. `include/eom-std/eomMatter.h`
   - g Valencia RHS/primitives.
3. `include/eom-std/eomSources.h`
   - g matter is directly included in `g_rho`, `g_j`, `g_JK`, `g_JKD`;
   - corresponding f functions contain interaction terms but no f matter.
4. `include/eom-std/eomConstraints.h`
   - `C_3` directly assumes only `S_g` matter.
5. `include/eom-std/eomMiscEquations.h`
   - `eq_base_p_g` contains `S_g`; `eq_base_p_f` assumes `S_f=0`.
6. `include/eom-std/eomEvolution.h`
   - `gSig_t` contains a direct `S_g` matter term; the f-symmetric term is absent.
7. `include/eom-std/eomLapseRatios.h`
   - the lapse relation contains explicit `D_g,S_g,tau_g` terms and was algebraically generated under the one-fluid assumption.

Therefore a physically complete twin-fluid extension is broader than merely adding `f_rho`.

## Exact momentum-constraint correction

This part can be derived without guessing.

Let

`A_g = 3 D_Bg K_Dg + d_r K_Dg - d_r K_g`,

`A_f = 3 D_Bf K_Df + d_r K_Df - d_r K_f`.

The two geometric momentum constraints in the standard source are

`Cjg = 2 A_g/3 + 2 K_Dg/r`,

`Cjf = 2 A_f/3 + 2 K_Df/r`.

With both dust fluids, the physical momentum sources are

`j_g^m = S_g/(A_g_metric B_g^2)`,

`j_f^m = S_f/(A_f_metric B_f^2)`.

The bimetric interaction contributes equal/opposite p-dependent pieces. Solving each momentum constraint for the separation `p` gives the known g expression plus the missing f-matter correction:

`base_p_f -> base_p_f - S_f/(A_f_metric A_g_metric B_g^2 P_2_1(R))`.

Combining the two momentum constraints to eliminate `p` shows that the current mixed constraint `C_3` must acquire the f term so that its matter contribution is

`- k_g k_f (S_g + S_f)/(2 B_g^2)`

in the current code conventions (`R=B_f/B_g`).

This is a useful regression identity: the corrected `C_3` must reduce exactly to the upstream expression when `S_f=0`.

## Source-function correction structure

The existing `eq_f_rho`, `eq_f_j`, `eq_f_JK`, `eq_f_JKD` are interaction-only. Add the sector-symmetric matter pieces.

At minimum:

`eq_f_rho += (D_f + tau_f)/(fA fB^2)`

`eq_f_j += S_f/(fA fB^2)`.

The `JK/JKD` additions must be obtained by the exact g<->f sector symmetry of the matter-only portions of `eq_g_JK` and `eq_g_JKD`, not by modifying interaction terms.

## Lapse-ratio warning

`include/eom-std/eomLapseRatios.h` explicitly contains the g Valencia variables. It is not safe to assume that merely adding f source functions elsewhere yields the correct two-fluid lapse relation.

Before the first evolution, one must either:

1. regenerate/derive the lapse relation with both conserved matter tensors; or
2. use a gauge/lapse prescription whose validity follows directly from the full 3+1 constraint propagation with both matter sectors.

Do **not** silently retain the one-fluid lapse formula and call the result twin-matter bigravity.

## Initial-data reference already available

`numerics/twin_lane_emden_initial.py` provides a time-symmetric constrained slice with:

- central positive f density;
- g-sector compensating shell;
- `K_ij=0`;
- `p=0`;
- zero fluid velocities;
- positive conformal factors.

Module-level TDD evidence already recorded:

RED: `ModuleNotFoundError`

GREEN: `3 passed in 0.48s`.

This is the initial state for the first dynamic wall gate.

## Controls required before interpreting the wall

Run the same solver/configuration for:

1. vacuum;
2. g-only shell;
3. f-only center;
4. full g-shell + f-center profile.

Use at least three radial resolutions/Courant factors and monitor:

- both Hamiltonian constraints;
- both momentum constraints;
- secondary bimetric constraint;
- lapse ratio;
- separation `p`;
- metric determinants / positivity;
- g and f conserved rest masses separately;
- max fluid velocities;
- convergence order over the trusted short interval.

## Known upstream numerical limitations

The 2020 paper reports only short reliable bimetric evolutions in the standard formulation and notes numerical sensitivity of the lapse ratio near the origin/boundary. Treat any apparent late-time instability as numerical until resolution/gauge/constraint checks separate it from a physical failure.

Conversely, do not excuse a nonconvergent immediate wall failure as 'just numerics' without a successful control run.

## Next execution checkpoint

When a local clone/fork can actually be materialized:

1. build untouched `bim-solver-STD`;
2. reproduce one one-fluid baseline;
3. write RED tests/diagnostics for the second state;
4. implement second state + symmetric Valencia equations;
5. correct all hard-coded matter assumptions listed above;
6. validate time-symmetric constraints;
7. run the short wall evolution.

No cosmological or observational claim is allowed before this sequence.
