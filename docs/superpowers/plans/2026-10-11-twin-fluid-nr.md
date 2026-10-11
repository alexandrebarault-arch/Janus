# Twin-Fluid Bimetric Numerical Relativity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the public spherical `bim-solver` research code with a genuinely independent `f`-sector dust fluid, then evolve the already-validated time-symmetric Janus-like initial wall for a short interval while monitoring all bimetric constraints.

**Architecture:** Do not vendor the GPLv3 upstream solver into this Janus notebook. Work in a separate GPL-compatible fork pinned to upstream tree/commit `8852e8e9921edeeedf1a447d3bf27b82ec24433c`. Add a second Valencia state symmetric to the existing `g` fluid, reuse the already-generic gravitational `T_f` source hooks, and use explicit MoL RK4/RKDP for the first evolution so generated DIRK Jacobians remain out of scope until stiffness proves they are necessary.

**Tech Stack:** C++ spherical bimetric `3+1` / cBSSN, Valencia hydrodynamics, existing `bim-solver` MoL RK4/RKDP, Python reference initial-data solver for regression checks.

**Spec:** `research/V2_FULL_SPHERICAL_GATE.md`

## Global Constraints

- GitHub Actions/workflows are disabled by the user; verification must be manual/local and exact outputs recorded.
- Upstream `bim-solver` is GPLv3; preserve license and attribution in the separate fork.
- First prototype is **dust only** in both sectors (`P=0`, `epsilon=0`, `h=1`).
- First prototype uses the time-symmetric initial slice already solved by `numerics/twin_lane_emden_initial.py`.
- First evolution uses an explicit MoL method (`RK4` or `RKDP45`); do not modify generated DIRK Jacobians unless explicit evolution is demonstrably inadequate.
- Do not claim cosmological viability from the local time-symmetric wall test.
- Keep PR #1 in `alexandrebarault-arch/Janus` draft; this plan is R&D, not promotion to the main scientific state.

## Review Focus

1. **Sector symmetry:** every `g` Valencia formula copied to `f` must replace lapse, shift, spatial metric determinant and radial metric component consistently; a mixed `g/f` primitive formula is a silent physics bug.
2. **Origin regularity:** new `f` radial velocity/momentum variables must obey the same spherical parity and regularization rules as the `g` fluid.
3. **Constraint sourcing:** `frho`, `fj`, `fJ11`, `fJ22` must enter the existing `f` Hamiltonian/momentum/evolution and lapse-ratio expressions without double counting.
4. **One-fluid regression:** setting all `f` conserved variables to zero must reproduce the upstream one-fluid equations/result to numerical tolerance.
5. **Matter conservation:** both sector rest masses must be independently conserved during a short evolution before any physical interpretation is attempted.

---

### Task 1: Establish a licensed, reproducible upstream baseline

**Files:**
- External fork: upstream `nubirel/bim-solver` at tree/commit `8852e8e9921edeeedf1a447d3bf27b82ec24433c`
- Record in Janus: `research/V2_TWIN_FLUID_NR_RUNBOOK.md`

**Interfaces:**
- Consumes: exact upstream source state above.
- Produces: a build/run command and a one-fluid reference output usable by later regression tasks.

- [ ] **Step 1: Build the untouched upstream solver locally**

Record compiler, platform, build command and exact commit.

- [ ] **Step 2: Run one published/available one-fluid example with explicit RK4**

Record constraint norms and output hashes/summary quantities.

- [ ] **Step 3: Commit only the runbook/results to the Janus notebook**

Do not copy GPL source into the Janus notebook.

### Task 2: Add independent `f`-fluid grid state

**Files in external fork:**
- Modify: `src/bim-solver-BSSN.cpp`
- Modify corresponding standard-3+1 source if used: `src/bim-solver-std.cpp`

**Interfaces:**
- Consumes: existing `pfD`, `pfS`, `pftau`, `pfv`, `pfW` pattern.
- Produces: `pfFD`, `pfFS`, `pfFtau`, `pfFv`, `pfFW` plus their RHS/derivative/convective grid functions (final naming may follow the upstream convention but must remain unambiguous).

- [ ] **Step 1: Write a compile-time/state-layout regression test or diagnostic asserting the new fields exist and are distinct from the g-fluid indices**
- [ ] **Step 2: Run before implementation and verify failure**
- [ ] **Step 3: Add the f-fluid fields to enum/state registration, `bimInput`, `bimEvolvedGF`, derivative descriptors and output descriptors**
- [ ] **Step 4: Build and verify the state-layout test passes**
- [ ] **Step 5: Verify zero-valued f-fluid initial data leave one-fluid baseline unchanged**

### Task 3: Implement f-sector dust Valencia primitives and stress-energy sources

**Files in external fork:**
- Modify: `include/eom-BSSN/eomBSSNMatterReg.h`
- Modify standard equivalent if the standard formulation remains in the test matrix: `include/eom-std/eomMatter.h`

**Interfaces:**
- Consumes: f-sector conserved variables plus `fAlp`, `fBet`, `fA`, `fB`, `fconf`.
- Produces: f-sector primitive velocity/Lorentz factor and `frho`, `fj`, `fJ11`, `fJ22`.

For dust, the continuum reference is the exact sector-symmetric analogue of Kocic et al. Eqs. (2.7)-(2.10):

- `rho_f = (tau_f + D_f) / sqrt(phi)`
- `j_f = S_f / sqrt(phi)`
- `J11_f = v_f S_f` after the same regularized-coordinate convention used upstream
- `J22_f = 0`

- [ ] **Step 1: Add unit/reference tests for zero velocity, finite radial velocity and zero-fluid limits**
- [ ] **Step 2: Verify tests fail because f primitives/sources are absent**
- [ ] **Step 3: Implement the f primitive/source formulas using only f geometry and f shift/lapse**
- [ ] **Step 4: Verify tests pass and no g source changes**

### Task 4: Implement f-sector Valencia evolution RHS

**Files in external fork:**
- Modify: `include/eom-BSSN/eomBSSNMatterReg.h`
- Modify derivative/convective preparation in `src/bim-solver-BSSN.cpp`

**Interfaces:**
- Consumes: f conserved/primitives + f lapse/shift/spatial geometry.
- Produces: `D_f,t`, `S_f,t`, `tau_f,t` suitable for existing MoL explicit evolution.

- [ ] **Step 1: Add sector-symmetry tests on a fixed synthetic metric pair: when `g=f` and the two fluids have identical state, g and f RHS must agree**
- [ ] **Step 2: Verify failure before implementation**
- [ ] **Step 3: Implement f Valencia RHS by the covariant sector-symmetric map, not by manually reusing g lapse/shift variables**
- [ ] **Step 4: Verify equality test and zero-fluid regression pass**

### Task 5: Connect existing f gravitational/lapse source hooks

**Files in external fork:**
- Inspect/verify: `include/eom-BSSN/eomBSSNLapseRatiosReg.h`
- Inspect/verify constraint/evolution source files under `include/eom-BSSN/`

**Interfaces:**
- Consumes: new `eq_pf_frho`, `eq_pf_fj`, `eq_pf_fJ11`, `eq_pf_fJ22`.
- Produces: no new equations if existing source hooks are already generic; otherwise only the minimal missing connections.

- [ ] **Step 1: Add a diagnostic test with nonzero f density and zero g density showing the f Hamiltonian/source diagnostics respond while g matter source remains zero**
- [ ] **Step 2: Verify failure with upstream zero-return stubs**
- [ ] **Step 3: Replace zero stubs with the Task-3 source functions and connect only missing source paths**
- [ ] **Step 4: Verify both sector constraint/source responses**

### Task 6: Import Janus-like time-symmetric initial data

**Files:**
- External fork initial-data loader/generator path identified during Task 1
- Reference: `numerics/twin_lane_emden_initial.py`

**Interfaces:**
- Consumes: radial `psi_g`, `psi_f`, central f dust and g compensating shell.
- Produces: complete upstream grid state with `K=0`, `p=0`, both fluid velocities zero.

- [ ] **Step 1: Export a deterministic radial reference profile from the Python BVP**
- [ ] **Step 2: Import it into the fork and reconstruct BSSN/3+1 geometry consistently**
- [ ] **Step 3: Numerically evaluate both Hamiltonian constraints, both momentum constraints and the secondary constraint on the initial slice**
- [ ] **Step 4: Require Hamiltonian residuals to converge downward with radial resolution; require momentum/secondary residuals to remain at discretization/roundoff scale**

### Task 7: Short explicit evolution of the wall

**Files:**
- External fork runtime parameters/configuration
- Record: `research/V2_TWIN_FLUID_NR_RUNBOOK.md`

**Interfaces:**
- Consumes: Task-6 initial state.
- Produces: short time series for constraints, matter masses, lapse ratio, metric determinants, null-cone/separation diagnostics.

- [ ] **Step 1: Run matched controls: vacuum, g-only shell, f-only center, and full twin profile**
- [ ] **Step 2: Run RK4 at at least three radial resolutions / Courant factors**
- [ ] **Step 3: Demonstrate convergence of constraint violations over the short trusted interval**
- [ ] **Step 4: Verify separate g/f rest-mass conservation and absence of negative density, zero lapse, determinant sign flip or superluminal fluid velocity**
- [ ] **Step 5: Record whether the compensation wall remains regular, disperses, collapses or triggers rapid constraint growth**

### Task 8: Decide whether DIRK/cBSSN hardening is necessary

**Files:**
- No changes unless triggered by Task 7 evidence.

- [ ] **Step 1: If explicit RK4/RKDP converges cleanly for the required short wall test, stop: do not touch DIRK Jacobians**
- [ ] **Step 2: If stiffness prevents convergence, document the failure mode first**
- [ ] **Step 3: Only then regenerate/extend DIRK Jacobians for the added f-fluid variables or migrate the test to the cBSSN path**

### Task 9: Scientific gate decision

**Files:**
- Update: `research/V2_FULL_SPHERICAL_GATE.md`
- Update: `RESUME.md`

- [ ] **Step 1: Classify `DYNAMIC_WALL` as PASS / PARTIAL / FAIL based on resolution-convergent constraint behavior**
- [ ] **Step 2: If PASS/PARTIAL, proceed to expanding/cosmological constraint data and wall stability**
- [ ] **Step 3: If FAIL robustly across gauge/resolution controls, strongly downgrade JANUS-R rather than tuning around the failure**
