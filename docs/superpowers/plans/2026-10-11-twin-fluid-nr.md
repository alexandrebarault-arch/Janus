# Twin-Fluid Bimetric Numerical Relativity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the public spherical `bim-solver` research code with a genuinely independent `f`-sector dust fluid, then evolve the already-validated time-symmetric Janus-like wall for a short interval while monitoring all bimetric constraints.

**Architecture:** Work in a separate GPLv3-compatible fork pinned to upstream tree/commit `8852e8e9921edeeedf1a447d3bf27b82ec24433c`; do not vendor the upstream solver into the Janus notebook. **First implement and test the twin fluid in the standard 3+1 solver (`bim-solver-STD`)**, because this is the formulation used in the published 2020 first evolutions and its matter/source equations are compact. Use explicit RK3/RK4 first. Only after a short, resolution-convergent wall evolution exists should the same state be ported to cBSSN for longer-time hardening. DIRK/Jacobian regeneration remains out of scope unless explicit evolution is demonstrably too stiff.

**Tech Stack:** C++14 spherical Hassan-Rosen standard `3+1` first, optional cBSSN second, Valencia dust hydrodynamics, existing Method-of-Lines RK3/RK4/RKDP, Python reference initial-data solver.

**Spec:** `research/V2_FULL_SPHERICAL_GATE.md`

## Global Constraints

- GitHub Actions/workflows are disabled by the user; verification must be manual/local and exact outputs recorded.
- Upstream `bim-solver` is GPLv3; preserve license and attribution in the separate fork.
- Upstream baseline is pinned to tree/commit `8852e8e9921edeeedf1a447d3bf27b82ec24433c`.
- First prototype is **dust only** in both sectors (`P=0`, `epsilon=0`, `h=1`).
- First prototype uses the time-symmetric initial slice already solved by `numerics/twin_lane_emden_initial.py`.
- First evolution uses the **standard 3+1 solver** and explicit RK3/RK4; do not touch generated DIRK Jacobians initially.
- If/when the cBSSN executable is used, compile with `-D_TEST_MODE=0`; `src/bim-solver-BSSN.cpp` otherwise defaults to `_TEST_MODE=1` and evolves the internal `u,v` test system instead of bimetric fields.
- Do not claim cosmological viability from the local time-symmetric wall test.
- Keep PR #1 in `alexandrebarault-arch/Janus` draft until the wall-evolution/stability gates are passed.

## Review Focus

1. **Sector symmetry:** the new `f` Valencia equations must use `fAlp`, `fBet`, `fA`, `fB`, `fDA`, `fK...`; any accidental `g` geometry in the `f` fluid is a physics bug.
2. **Source completeness:** the standard solver currently hard-codes `g` matter into `eq_g_rho/j/JK/JKD`, while `eq_f_rho/j/JK/JKD` contain interaction terms only. The twin-fluid patch must add the corresponding `f` matter terms exactly once.
3. **Origin parity/regularity:** `f` radial velocity and momentum must obey the same spherical parity rules as the existing `g` fluid.
4. **One-fluid regression:** setting `D_f=S_f=tau_f=0` must reproduce the upstream standard-3+1 one-fluid result to numerical tolerance.
5. **Independent conservation:** both sector rest masses must be monitored separately before physical interpretation.

---

### Task 1: Establish a reproducible standard-3+1 upstream baseline

**Files:**
- External GPL fork: `nubirel/bim-solver` at pinned commit/tree.
- Record in Janus: `research/V2_TWIN_FLUID_NR_RUNBOOK.md`.

**Interfaces:**
- Produces: exact build command, runtime config, explicit MoL method and one-fluid reference constraint history.

- [ ] Write down compiler/platform and pin upstream commit.
- [ ] Build **`bim-solver-STD`** untouched.
- [ ] Run the closest available published one-fluid dust example with RK3/RK4.
- [ ] Record constraint norms and conserved mass over the short trusted interval.
- [ ] Commit only runbook/results to Janus; do not copy GPL source into Janus.

### Task 2: Add independent f-fluid state to the standard solver

**Files in external fork:**
- Modify: `src/bim-solver-std.cpp`.

**Interfaces:**
- Existing g state: `pfD, pfS, pftau, pfv`.
- New f state: choose explicit names such as `pfFD, pfFS, pfFtau, pfFv`; add RHS and radial derivatives consistently.

- [ ] Write a state-layout diagnostic/test asserting g and f fields are distinct and both appear in input/evolution/output tables.
- [ ] Run it before implementation and verify failure.
- [ ] Add f conserved variables, RHS, primitive velocity and derivatives to enum/state registration, `bimInput`, `bimEvolvedGF`, outputs and derivative preparation.
- [ ] Build and verify the diagnostic passes.
- [ ] Verify zero f-state leaves the upstream one-fluid baseline unchanged.

### Task 3: Implement f-sector standard-3+1 Valencia dust equations

**Files in external fork:**
- Modify: `include/eom-std/eomMatter.h`.

**Interfaces:**
- Consumes: f conserved variables + f geometry/lapse/shift.
- Produces: f primitive velocity and `D_f,t`, `S_f,t`, `tau_f,t`.

The existing g equations in `eomMatter.h` are the reference. The f implementation must be the exact covariant sector analogue, replacing every g-sector geometric quantity by its f-sector counterpart.

For dust primitives/sources:

- `v_f = S_f / [(D_f + tau_f) fA^2]`
- `rho_f^m = (D_f + tau_f)/(fA fB^2)`
- `j_f^m = S_f/(fA fB^2)`
- `J1_f^m = S_f v_f/(fA fB^2)`
- `J2_f^m = 0`

- [ ] Write fixed-geometry sector-symmetry tests: if `g=f` and matter states match, g/f primitive and RHS values must match.
- [ ] Verify RED before implementation.
- [ ] Implement f Valencia equations with f lapse/shift/metric only.
- [ ] Verify sector-symmetry and zero-fluid tests pass.

### Task 4: Add f-matter to the standard gravitational sources

**Files in external fork:**
- Modify: `include/eom-std/eomSources.h`.
- Inspect: `include/eom-std/eomConstraints.h`, `eomEvolution.h`, `eomLapseRatios.h`.

**Interfaces:**
- Existing `eq_f_rho`, `eq_f_j`, `eq_f_JK`, `eq_f_JKD` currently contain only bimetric interaction terms.
- Add the f-matter pieces, mirroring the existing g-matter contributions.

At minimum the matter-only additions must reduce, for dust, to the sector-symmetric forms generated from the g formulas when interaction terms are removed.

- [ ] Write tests evaluating source functions with `g` matter zero and `f` matter nonzero; f Hamiltonian/momentum sources must respond while g matter source remains zero except through the interaction potential.
- [ ] Verify failure on upstream-equivalent code.
- [ ] Add f matter terms exactly once to `eq_f_rho/j/JK/JKD`.
- [ ] Verify source tests and one-fluid regression.
- [ ] Inspect the lapse-ratio formula for explicit g-fluid-only terms. If the standard lapse relation was algebraically generated under `T_f=0`, derive/regenerate the two-fluid form before evolution; do not silently reuse it.

### Task 5: Import Janus-like time-symmetric initial data

**Files:**
- External fork initial-data path.
- Reference: `numerics/twin_lane_emden_initial.py`.

**Interfaces:**
- Consumes: radial `psi_g`, `psi_f`, central f dust and g compensating shell.
- Produces: standard-3+1 grid state with zero extrinsic curvatures, `p=0`, and both fluid velocities zero.

- [ ] Export a deterministic radial profile from the Python BVP.
- [ ] Map `A_g=B_g/r=psi_g^2` and `A_f=B_f/r=psi_f^2` into the standard solver variables/regularization.
- [ ] Initialize `D_g,D_f` consistently with the conserved-density convention and set `S_g=S_f=tau_g=tau_f=0` for dust at rest.
- [ ] Evaluate both Hamiltonian constraints, both momentum constraints and the secondary constraint at multiple resolutions.
- [ ] Require Hamiltonian residual convergence and momentum/secondary residuals at discretization/roundoff scale.

### Task 6: Short explicit standard-3+1 evolution

**Files:**
- External fork runtime config.
- Record: `research/V2_TWIN_FLUID_NR_RUNBOOK.md`.

**Interfaces:**
- Consumes: Task-5 state.
- Produces: constraint/mass/lapse/metric histories.

- [ ] Run matched controls: vacuum, g-only shell, f-only center, full twin profile.
- [ ] Use RK3 or RK4 with at least three resolutions/Courant factors.
- [ ] Demonstrate convergence over the short interval where the standard formulation is trusted.
- [ ] Monitor both Hamiltonian and momentum constraints, secondary constraint, lapse ratio, metric determinants, separation `p`, both rest masses and fluid velocities.
- [ ] Reject any interpretation if density becomes negative, lapse crosses zero, metric determinant changes sign, fluid speed becomes nonphysical, or constraints grow nonconvergently.
- [ ] Record whether the wall remains regular, disperses, collapses, or immediately triggers branch/constraint failure.

### Task 7: Decide whether cBSSN hardening is warranted

**Files:**
- Only if Task 6 passes/partially passes.

- [ ] If short standard evolution fails robustly across gauge/resolution controls, stop and scientifically downgrade JANUS-R before adding cBSSN complexity.
- [ ] If it passes, port the second fluid to `src/bim-solver-BSSN.cpp` and `include/eom-BSSN/eomBSSNMatterReg.h`.
- [ ] Compile cBSSN with `-D_TEST_MODE=0` and verify evolved-field names/count before running physics.
- [ ] Start with explicit RK4/RKDP; only regenerate DIRK Jacobians if stiffness requires implicit evolution.

### Task 8: Expanding cosmological embedding

Only after the local wall survives.

- [ ] Solve the **full non-time-symmetric 3+1 constraints**, including extrinsic curvature and separation/relative shift; do not impose an ad-hoc constant `K=-3H` on the Lane-Emden slice.
- [ ] Match toward an FLRW exterior rather than asymptotic Minkowski.
- [ ] Evolve a compensated cosmic-void profile and monitor the same constraints.

### Task 9: Scientific gate decision

**Files:**
- Update: `research/V2_FULL_SPHERICAL_GATE.md`.
- Update: `RESUME.md`.

- [ ] Classify `DYNAMIC_WALL = PASS / PARTIAL / FAIL` only from resolution-convergent evidence.
- [ ] If PASS/PARTIAL, proceed to the spherical perturbative stability gate and observables.
- [ ] If FAIL robustly, strongly downgrade JANUS-R rather than tune around the failure.
