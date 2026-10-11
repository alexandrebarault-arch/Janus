# V2 Twin-Fluid Numerical-Relativity Runbook

Date: 2026-10-11
Status: `DESIGN_READY__GENERAL_TWIN_LAPSE_FOUND__UPSTREAM_BUILD_NOT_YET_EXECUTABLE_IN_CURRENT_SANDBOX`

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

Direct attempts to download the arXiv ancillary Mathematica files also failed in the local runtime, although arXiv exposes them publicly on the paper page.

Therefore no claim is made that the upstream C++ solver has been compiled or run in this session. Source inspection is grounded through the GitHub connector and published equations.

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
   - radial derivatives and preparation;
   - origin/right-boundary parity and extrapolation.
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
   - the lapse relation contains explicit `D_g,S_g,tau_g` terms and was algebraically specialized to the one-fluid case.
8. `include/maximalSlice.h`
   - the maximal-slicing operator also hard-codes the g fluid and contains upstream TODO/fixme notes about the source/factor. Do not use this implementation as a twin-fluid physical diagnostic without rederivation.

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

This agrees structurally with the general mixed constraint of Kocic-Lundkvist-Torsello, which contains the matter momenta from both sectors. It is a useful regression identity: the corrected `C_3` must reduce exactly to the upstream expression when `S_f=0`.

## Source-function correction structure

The existing `eq_f_rho`, `eq_f_j`, `eq_f_JK`, `eq_f_JKD` are interaction-only. Add the sector-symmetric matter pieces.

At minimum:

`eq_f_rho += (D_f + tau_f)/(fA fB^2)`

`eq_f_j += S_f/(fA fB^2)`.

The `JK/JKD` additions must be obtained by the exact g<->f sector symmetry of the matter-only portions of `eq_g_JK` and `eq_g_JKD`, not by modifying interaction terms.

## Major correction: the general twin-matter lapse ratio is already published

Primary reference:

M. Kocic, A. Lundkvist, F. Torsello, *On the ratio of lapses in bimetric relativity*, Class. Quantum Grav. 36 (2019) 225013, arXiv:1903.09646.

The paper starts from the fully general action with **both** minimally coupled matter sectors and derives the standard-3+1 constraints with both matter momenta. Preservation of the secondary bimetric constraint gives, in spherical symmetry,

`0 ~= W_g alpha + W_f alpha_f`

(up to their common nonzero normalization `W_c`), hence

`alpha = -(W_f/W_g) alpha_f`.

The authors explicitly state that `W_g` and `W_f` depend on spatial metrics, extrinsic curvatures, derivatives **and the matter stress-energy tensors**, and therefore matter coupled to either metric automatically affects the lapse of the other metric.

The explicit formulas are Eqs. (2.20)-(2.22), with coefficient functions `c_i,d_i` in Appendix D. The paper also gives the duality

`g <-> f`, `beta_{4-n} <-> beta_n`, `p <-> -p`,

under which `W_g <-> -W_f`.

### Ancillary derivation files

The arXiv record explicitly lists machine-readable ancillary material, including:

- `src/02-lapse-ratio.nb`
- `src/bimetric-lapses-nr.m`
- `src/bimetric-ss-nr.m`

and the later dust-collapse paper arXiv:1904.08617 also publishes `bimetric-lapses-nr.m` and related source files.

The current sandbox could not download these files because of network/cache restrictions. **Do not manually transcribe the full Appendix-D algebra into production C++ if the ancillary source can be obtained in the actual fork environment.** Prefer importing/translating the authors' symbolic expressions and validating them.

### Required implementation strategy for the lapse

Replace the old vague instruction "derive a two-fluid lapse" with this concrete gate:

1. obtain the published ancillary symbolic expression;
2. implement general `W_g,W_f` with both matter sectors;
3. unit-test the `g <-> f` duality;
4. set all f-matter variables to zero and require numerical/algebraic agreement with upstream `eomLapseRatios.h` over randomized regular states;
5. only then enable twin-fluid evolution.

This regression is mandatory. The existing one-fluid lapse formula must **not** be silently retained.

### Gauge after the ratio is known

Once `W=-W_f/W_g` is available, one lapse remains a gauge choice. A symmetric geometric-mean gauge is available through the published relation

`H^2 lambda = alpha alpha_f`.

For a chosen geometric-mean lapse `H`, the two sector lapses follow from `W`. This is preferable for a symmetric twin-matter diagnostic to arbitrarily fixing both lapses.

Cases where `W_g` or `W_f` vanishes/diverges are physical/numerical branch warnings and must be monitored explicitly.

## Maximal-slicing shortcut rejected

The upstream `include/maximalSlice.h` solves a lapse BVP whose source explicitly contains the g perfect fluid, and the file itself carries TODO/fixme comments about the factor/source choice. It was designed for the existing one-fluid experiments.

Therefore do **not** use this routine to infer the initial acceleration of twin matter. The correct two-fluid lapse ratio is the general `W_g,W_f` relation above.

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
- lapse ratio `W` and separately `W_g,W_f`;
- separation `p`;
- metric determinants / positivity;
- g and f conserved rest masses separately;
- max fluid velocities;
- convergence order over the trusted short interval.

## Known upstream numerical limitations

The 2020 paper reports only short reliable bimetric evolutions in the standard formulation and notes numerical sensitivity of the lapse ratio near the origin/boundary. Treat any apparent late-time instability as numerical until resolution/gauge/constraint checks separate it from a physical failure.

Conversely, do not excuse a nonconvergent immediate wall failure as 'just numerics' without a successful control run.

The standard-3+1 **constraint propagation subsystem** has separately been shown to be first-order symmetric hyperbolic in bimetric relativity; this supports using convergent constraint growth as a meaningful diagnostic, while it does not by itself establish strong hyperbolicity of every gauge-fixed evolution implementation.

## Next execution checkpoint

When a local clone/fork can actually be materialized:

1. build untouched `bim-solver-STD`;
2. reproduce one one-fluid baseline;
3. obtain the arXiv symbolic lapse-ratio ancillary files;
4. write RED tests for the second matter state and general `W_g,W_f`;
5. implement second state + symmetric Valencia equations;
6. correct all hard-coded matter assumptions listed above;
7. prove `T_f=0` lapse/source regression against upstream;
8. validate time-symmetric constraints;
9. run the short wall evolution.

No cosmological or observational claim is allowed before this sequence.
