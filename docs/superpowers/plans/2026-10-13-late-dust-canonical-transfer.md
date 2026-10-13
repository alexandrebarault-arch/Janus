# Late Dust Canonical Transfer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first trustworthy time-domain scalar transfer solver for a strictly on-shell Candidate-C-like dust+dust benchmark, from the benchmark's own `m_eff/H=1` crossing to today, using the validated De Felice/Hassan-Rosen action and reporting physical sector-density conversion.

**Architecture:** First make the dust limit regular at the action level by Legendre-transforming each P(X) matter sector, then eliminate metric auxiliaries, dust momenta and the BD scalar to recover a regular three-coordinate quadratic action. Evolve its canonical phase variables `(Y,Pi)` so the solver never differentiates `K` or `C`, and carry explicit reconstruction maps back to the original matter momenta and density contrasts. Candidate-C background data come from one strictly on-shell dust+dust provider; the physical radiation background is used only as a comparison oracle.

**Tech Stack:** Python, NumPy, SciPy `solve_ivp`, pytest, existing JANUS `numerics/*` De Felice/Hassan-Rosen modules.

**Spec:** `docs/superpowers/specs/2026-10-13-late-dust-canonical-transfer-design.md`

## Global Constraints

- Work on branch `research/gate2b-nonhomothetic-transfer`; create an isolated worktree before implementation.
- Do not use the historical Comelli 12x12 closure as a physical input.
- Do not tune Eq. (44), Eq. (45)-(46), Eq. (54), EH, HR or matter coefficients to hit a target.
- Do not retain a finite artificial dust sound speed in production integration.
- Do not mix a dust perturbation action with the radiation-containing Candidate-C metric background.
- Every coefficient derivative used by the BD canonicalization must follow one strictly on-shell background family.
- Use the direct O(delta^2) HR interaction; never finite-difference the nonlinear HR potential in this solver.
- Preserve the already validated Eq. (72) basis and `canonicalize_linear_zdot_time_dependent()` identity.
- The six-dimensional fundamental matrix is authoritative; no 2x2 density transfer matrix may hide arbitrary velocity initial conditions.
- Full-repository GREEN claims require a real complete worktree run; minimal reconstructed subsets are not sufficient for that claim.

## Review Focus

1. **f-sector momentum normalization:** `n xi^3` must be applied exactly once when converting between canonical matter momentum and physical `delta_rho_f`; pin this in Task 2 and Task 6.
2. **Boundary-term momentum shifts:** time-dependent `Y_i Zdot` integration by parts changes canonical momenta; observable pullback must undo that shift before reading matter density; pin this in Task 6.
3. **Background consistency:** no action coefficient may be evaluated on full Candidate C while matter uses dust-only densities; pin branch constraint and derivative consistency in Task 1 and Task 4.
4. **Near-singular reductions:** auxiliary, dust-momentum, BD and physical kinetic blocks must fail fast with diagnostic condition numbers instead of silently using unstable inverses; pin in Tasks 3, 4 and 5.
5. **Mode identity/sign continuity:** the GR-connected adiabatic mode and later common/relative lift must be continuous under small changes of `a` and `k`; pin overlap/sign tests in Tasks 8 and 9.

---

### Task 1: Strictly on-shell Candidate-C dust background

**Files:**
- Modify: `numerics/flrw_two_matter.py`
- Create: `numerics/candidate_c_dust_background.py`
- Create: `tests/test_candidate_c_dust_background.py`
- Reuse: `tests/test_candidate_c_transfer_background.py`

**Interfaces:**
- Produces: `branch_log_derivatives(a: float, y: float, p: Params) -> tuple[float, float]` in `flrw_two_matter.py`.
- Produces: `candidate_c_dust_params() -> Params`.
- Produces: `CandidateCDustBackgroundPoint` with `y`, `y_N`, `y_NN`, `metric`, `derivatives`, `rho_g_m`, `rho_f_m`.
- Produces: `candidate_c_dust_background_point(a: float, *, k_hmpc: float) -> CandidateCDustBackgroundPoint`.
- Produces: `candidate_c_dust_meff_over_H(a: float) -> float` and `candidate_c_dust_linear_start() -> float` returning the scale factor where `m_eff/H=1`.

- [ ] **Step 1: Write RED tests for the generic implicit branch derivatives**

Add tests that compare `branch_log_derivatives()` against centered finite differences of `solve_branch()` for the original Candidate C at `z=0,10,100`, and require agreement with the current `candidate_c_transfer.py` values to `rtol<=2e-5`.

- [ ] **Step 2: Run the derivative tests and witness RED**

Run: `pytest tests/test_candidate_c_dust_background.py::test_generic_branch_log_derivatives_match_candidate_c -v`
Expected: FAIL because `branch_log_derivatives` does not exist.

- [ ] **Step 3: Implement `branch_log_derivatives()` and refactor `candidate_c_transfer.py` to use it**

Keep the present implicit-polynomial analytic formula; make it parameter-generic without changing Candidate-C outputs.

- [ ] **Step 4: Verify original Candidate-C background regressions remain GREEN**

Run: `pytest tests/test_candidate_c_transfer_background.py tests/test_candidate_c_dust_background.py::test_generic_branch_log_derivatives_match_candidate_c -v`
Expected: PASS.

- [ ] **Step 5: Write RED tests for the dust benchmark background**

Require:
- `omega_g_r0 == 0` while all other `candidate_c()` interaction/matter parameters are unchanged;
- branch constraint residual `<1e-11` at `a in {1,0.5,0.1,1/17}`;
- `rho_g_m=3 Omega_gm0 a^-3` and `rho_f_m=3 Omega_fm0 (y0/(a y))^3`;
- analytic `c_N` agrees with a centered on-shell branch difference to `rtol<=3e-5`;
- the returned `m_eff/H=1` crossing brackets a unique continuous root in the late interval.

- [ ] **Step 6: Implement the dust background provider and crossing finder**

Use `dataclasses.replace(candidate_c(), omega_g_r0=0.0)`, the same positive branch-continuation rule as Candidate C, and `branch_log_derivatives()` for derivatives. The crossing finder must solve on the same dust provider, not interpolate the full-radiation diagnostics.

- [ ] **Step 7: Add a comparison regression against full Candidate C**

At a deterministic grid from the dust crossing to `a=1`, record maxima of relative differences in `H`, `y`, `c`, `m_eff/H`, and principal gravity `c_s^2`; assert they are finite and the dust/full difference at `a=0.5` reproduces the known principal-speed shift `~1.2e-5` relative.

- [ ] **Step 8: Run Task-1 tests and commit**

Run: `pytest tests/test_candidate_c_transfer_background.py tests/test_candidate_c_dust_background.py -v`
Expected: PASS.

Commit: `feat: add on-shell Candidate C dust background`

---

### Task 2: Regular one-sector dust phase action

**Files:**
- Create: `numerics/de_felice_dust_phase_action.py`
- Create: `tests/test_de_felice_dust_phase_action.py`
- Reuse: `numerics/de_felice_matter_action.py`

**Interfaces:**
- Produces: `finite_cs2_phase_density(..., momentum: float, cs2: float) -> float` for the Legendre-transformed Eq. (54) matter block before the dust limit.
- Produces: `dust_phase_density(*, rho, lapse, scale_factor, k, Phi, B, psi, E, q, momentum) -> float` for `P=0`, `cs2->0`.
- Produces: `physical_density_from_phase_momentum(*, momentum_local, rho, psi) -> float` returning `delta_rho = momentum_local - 3 rho psi`.
- Produces: `common_normalized_momentum(*, momentum_local, prefactor) -> float` and its inverse; f sector uses `prefactor=n*xi**3`.

- [ ] **Step 1: Write RED finite-`cs2` Legendre identity tests**

For several generic tuples `(rho,P,cs2,Phi,B,psi,E,q,momentum)`, solve
`qdot-Phi = cs2*(momentum/(rho+P)-3*psi)` and require
`L_phase = momentum*qdot - H` to equal `kessence_scalar_quadratic_density()` after substitution to `rtol<=2e-13`.

- [ ] **Step 2: Run and witness RED**

Run: `pytest tests/test_de_felice_dust_phase_action.py::test_finite_cs2_legendre_form_matches_eq54 -v`
Expected: FAIL because the module/functions do not exist.

- [ ] **Step 3: Implement the finite-`cs2` phase form**

Use the exact identity
`H_temp = p*Phi + cs2/(2A)*(p-3A psi)^2 - A*Phi^2/2`, `A=rho+P`, plus the unchanged Eq. (54) metric-pressure and spatial blocks.

- [ ] **Step 4: Write and pass the exact dust-limit tests**

Require the analytic `cs2->0`, `P->0` result to remain finite and equal the finite-`cs2` phase density limit after subtracting the vanishing `cs2*(p-3A psi)^2/(2A)` term. Pin `delta_rho = p-3 rho psi`.

- [ ] **Step 5: Pin g/f normalization**

With `prefactor=1` for g and `prefactor=n*xi**3` for f, round-trip local momentum -> common-normalized momentum -> local momentum at `1e-14` relative.

- [ ] **Step 6: Run Task-2 tests and commit**

Run: `pytest tests/test_de_felice_matter_action.py tests/test_de_felice_dust_phase_action.py -v`
Expected: PASS.

Commit: `feat: add regular De Felice dust phase action`

---

### Task 3: Exact-quadratic two-dust auxiliary reduction

**Files:**
- Create: `numerics/de_felice_two_dust_action.py`
- Create: `tests/test_de_felice_two_dust_action.py`
- Reuse: `numerics/de_felice_gravity_action.py`
- Reuse: `numerics/hr_scalar_potential.py`
- Reuse: `numerics/de_felice_two_matter_action.py::bd_basis_transform`

**Interfaces:**
- Produces constants `DUST_DYNAMIC_ORDER=("psi_f","E_f","q_g","q_f")`, `DUST_RATE_ORDER=(...)`, `DUST_AUXILIARY_ORDER=("Phi_g","Phi_f","B_g","B_f","p_g","p_f")`.
- Produces dataclass `DustFlatGaugeReducedAction` containing `reduced_hessian: np.ndarray` (8x8), `metric_auxiliary_condition_number`, `dust_momentum_condition_number`, and reconstruction matrices for `(Phi_g,Phi_f,B_g,B_f,p_g,p_f)` from old states/rates.
- Produces `eliminate_flat_gauge_two_dust(bg,bgp,*,betas,rho_g,rho_f) -> DustFlatGaugeReducedAction`.

- [ ] **Step 1: Write RED structural tests for the augmented exact quadratic action**

Require the augmented Hessian in order `(4 states,4 rates,4 metric auxiliaries,2 dust momenta)` to be symmetric and finite, with no finite-`cs2` argument anywhere in the public API.

- [ ] **Step 2: Run and witness RED**

Run: `pytest tests/test_de_felice_two_dust_action.py::test_two_dust_augmented_action_is_exact_quadratic_and_symmetric -v`
Expected: FAIL because the module does not exist.

- [ ] **Step 3: Implement the augmented action from audited pieces**

Reuse Eq. (44), direct O(delta^2) HR Eqs. (45)-(46), and Task-2 dust phase sectors. Evaluate its Hessian by exact quadratic polarization with unit basis vectors; do not use a small perturbation amplitude.

- [ ] **Step 4: Write RED Schur/reconstruction tests**

At Case C and Candidate-C dust control points require:
- metric auxiliary block rank 4;
- after metric-aux elimination, dust-momentum block rank 2;
- final 8x8 old-variable Hessian finite/symmetric;
- substituting the returned reconstruction map into the unreduced action agrees with the Schur-reduced quadratic value to `rtol<=1e-10` for deterministic test vectors.

- [ ] **Step 5: Implement two-stage elimination with fail-fast conditioning**

Reject rank loss and non-finite condition numbers. Store reconstruction maps instead of discarding eliminated-variable information.

- [ ] **Step 6: Run Task-3 tests and commit**

Run: `pytest tests/test_de_felice_two_dust_action.py -v`
Expected: PASS.

Commit: `feat: reduce exact two-dust scalar action`

---

### Task 4: Time-dependent BD reduction on an on-shell trajectory

**Files:**
- Create: `numerics/de_felice_dust_physical_action.py`
- Create: `tests/test_de_felice_dust_physical_action.py`
- Reuse: `numerics/bd_time_canonicalization.py`
- Reuse: `numerics/de_felice_two_matter_action.py::bd_basis_transform`

**Interfaces:**
- Produces dataclass `DustPhysicalAction` with `transformed_hessian`, `canonical_hessian`, `physical_hessian` (6x6), `K`, `C`, `M`, `bd_algebraic_coefficient`, `zdot_kinetic_residual`, `condition_numbers`, and a composed reconstruction map to old states/rates/auxiliaries/dust momenta.
- Produces `dust_physical_action(bg,bgp,*,betas,rho_g,rho_f,dot_c,mu_measure) -> DustPhysicalAction`.
- Produces Candidate-C adapter `candidate_c_dust_physical_action(a: float, *, k_hmpc: float, derivative_step_N: float=1e-4) -> DustPhysicalAction`.

- [ ] **Step 1: Write RED tests for time-dependent BD canonicalization on the dust reducer**

At deterministic Case-C and Candidate-C dust points require `Zdot` kinetic residual `<1e-8`, algebraic `Z` invertibility, and exactly three physical kinetic directions.

- [ ] **Step 2: Run and witness RED**

Run: `pytest tests/test_de_felice_dust_physical_action.py::test_two_dust_bd_reduction_has_three_physical_directions -v`
Expected: FAIL because the adapter does not exist.

- [ ] **Step 3: Implement generic BD reduction while preserving reconstruction maps**

Apply Eq. (72), `canonicalize_linear_zdot_time_dependent()`, then the algebraic `Z` Schur complement. Compose the Task-3 auxiliary/momentum reconstruction with the Eq. (72) transform and `Z` solution.

- [ ] **Step 4: Implement the on-shell `dot_c` adapter with convergence check**

Compute `C[:,Z]` on the dust background at `N±h` and `N±2h` and use the five-point derivative; use `mu_measure=3H_g`. Add a test comparing `h=2e-4,1e-4,5e-5` at `a=0.5,k=0.1 h/Mpc` and require each `dot_c` component to converge within a documented tolerance (`rtol<=2e-3` for non-negligible components, absolute scale-aware tolerance otherwise).

- [ ] **Step 5: Pin off-shell rejection**

Add a test that deliberately passes a full-radiation Candidate-C metric point with dust-only densities through the Candidate-C dust adapter and require an explicit background-consistency error rather than silent evaluation.

- [ ] **Step 6: Run Task-4 tests and commit**

Run: `pytest tests/test_bd_time_canonicalization.py tests/test_de_felice_dust_physical_action.py -v`
Expected: PASS.

Commit: `feat: add on-shell dust BD physical reduction`

---

### Task 5: Canonical phase RHS and fundamental matrix

**Files:**
- Create: `numerics/canonical_quadratic_evolution.py`
- Create: `tests/test_canonical_quadratic_evolution.py`

**Interfaces:**
- Produces `canonical_phase_matrix(*, K, C, M, H_g) -> np.ndarray` returning the 6x6 cosmic-time matrix for state `(Y,Pi)`.
- Produces `canonical_rhs(t, state, *, coefficients_provider) -> np.ndarray`.
- Produces `fundamental_rhs(t, flat_matrix, *, coefficients_provider) -> np.ndarray` for a 6x6 fundamental matrix.

- [ ] **Step 1: Write RED synthetic constant-coefficient Hamilton tests**

For diagonal `K`, `C=0`, and known `M`, require `canonical_phase_matrix()` eigenvalues to match the analytic oscillator/growing-mode roots.

- [ ] **Step 2: Run and witness RED**

Run: `pytest tests/test_canonical_quadratic_evolution.py::test_canonical_phase_matrix_matches_known_quadratic_system -v`
Expected: FAIL because the module does not exist.

- [ ] **Step 3: Implement the canonical equations**

Use only
`Ydot = solve(K, Pi-C.T@Y)` and
`Pidot = M@Y + C@Ydot - 3H_g*Pi`.
Do not numerically differentiate `K` or `C`.

- [ ] **Step 4: Add time-dependent synthetic equivalence test**

Choose analytic scalar `K(t),C(t),M(t)` and compare the canonical first-order solution with direct integration of the expanded Euler-Lagrange equation containing `dot K`, `dot C`, and `3H` over a short interval; require `rtol<=1e-8`.

- [ ] **Step 5: Add condition-number failure test**

A singular or numerically rank-deficient `K` must raise `LinAlgError` with the kinetic condition number included in the diagnostic object/message.

- [ ] **Step 6: Run Task-5 tests and commit**

Run: `pytest tests/test_canonical_quadratic_evolution.py -v`
Expected: PASS.

Commit: `feat: add canonical quadratic phase evolution`

---

### Task 6: Physical density observable pullback

**Files:**
- Create: `numerics/de_felice_dust_observables.py`
- Create: `tests/test_de_felice_dust_observables.py`
- Modify: `numerics/de_felice_dust_physical_action.py` only if an additional reconstruction matrix must be exposed.

**Interfaces:**
- Produces dataclass `DustObservables(delta_rho_g,delta_rho_f,delta_g,delta_f,delta_common,delta_relative)`.
- Produces `reconstruct_dust_observables(action: DustPhysicalAction, *, Y, Pi, rho_g, rho_f, bg) -> DustObservables`.
- Produces low-level `undo_bd_boundary_momentum_shift(...)` for a separately testable boundary transformation.

- [ ] **Step 1: Write RED test for the BD boundary momentum shift**

Build a synthetic Eq. (72) Hessian with nonzero `c_i` and verify that applying then undoing the boundary generating function
`F=sum_{i!=Z} c_i Y_i Z + 1/2 c_Z Z^2`
round-trips canonical momenta to `1e-13`.

- [ ] **Step 2: Run and witness RED**

Run: `pytest tests/test_de_felice_dust_observables.py::test_boundary_momentum_pullback_round_trips -v`
Expected: FAIL because the observable module does not exist.

- [ ] **Step 3: Implement reconstruction through all stored maps**

Recover `Ydot`, then `Z`, old states/rates, metric auxiliaries and local dust momenta. Convert f common-normalized momentum by dividing `n*xi**3` exactly once. Use `delta_rho = p_local-3 rho psi`.

- [ ] **Step 4: Add finite-`cs2` oracle regression**

At a generic regulated two-matter point, compare the density reconstructed by the phase-momentum identity with the direct P(X) relation implied by Eq. (54); require `rtol<=1e-9` for g and f.

- [ ] **Step 5: Add physical normalization tests**

Scale the full perturbation state by factors `{0.1,3,-2}` and require every reconstructed density contrast to scale linearly. Require finite values when `rho_g,rho_f>0`, and explicit rejection when either background density is non-positive.

- [ ] **Step 6: Run Task-6 tests and commit**

Run: `pytest tests/test_de_felice_dust_observables.py -v`
Expected: PASS.

Commit: `feat: reconstruct dust density observables`

---

### Task 7: Local physics regressions for the dust phase system

**Files:**
- Create: `tests/test_de_felice_dust_local_regressions.py`
- Optionally create: `numerics/de_felice_dust_local_modes.py` if mode extraction is more than a small helper.

**Interfaces:**
- Produces `local_phase_squared_speeds(action: DustPhysicalAction, *, a, k) -> np.ndarray` from the high-k eigenvalues of the canonical phase matrix.

- [ ] **Step 1: Write RED Case-C principal regression**

At exact Case C `a=0.05`, require the gravity branch to approach `-0.6665833419871022` with the two dust branches approaching zero as `k` increases. Use at least `k={800,1600,3200}` and an extrapolation in `1/k^2`; gravity extrapolation tolerance `rtol<=5e-5`.

- [ ] **Step 2: Run and witness RED**

Run: `pytest tests/test_de_felice_dust_local_regressions.py::test_case_c_exact_dust_phase_recovers_principal_gravity_branch -v`
Expected: FAIL until the dust physical pipeline is complete.

- [ ] **Step 3: Implement/finish the local canonical-mode extraction**

Pair `+/-` eigenvalues by squared phase speed, preserve zero dust branches, and reject unpaired complex contamination above a scale-aware tolerance.

- [ ] **Step 4: Add Candidate-C dust regression**

At `a=0.5`, require gravity extrapolation `0.6920714772884699` to `rtol<=5e-5`, with both dust matter branches approaching zero.

- [ ] **Step 5: Add GR/decoupled control**

In a one-metric/decoupled pressureless control, require the regular scalar matter mode to reproduce standard dust growth and no spurious propagating acoustic branch.

- [ ] **Step 6: Run Task-7 tests and commit**

Run: `pytest tests/test_de_felice_dust_local_regressions.py -v`
Expected: PASS.

Commit: `test: validate exact dust scalar principal modes`

---

### Task 8: Late Candidate-C-like integration and adiabatic mode tracking

**Files:**
- Create: `numerics/candidate_c_dust_late_transfer.py`
- Create: `tests/test_candidate_c_dust_late_transfer.py`

**Interfaces:**
- Produces dataclass `LateDustTransferResult` containing deterministic arrays `a`, `Y`, `Pi`, `delta_g`, `delta_f`, `delta_common`, `delta_relative`, `R`, plus conditioning diagnostics.
- Produces `select_gr_connected_adiabatic_mode(a: float, *, k_hmpc: float) -> np.ndarray` returning a normalized six-component phase vector.
- Produces `solve_candidate_c_dust_late(k_hmpc: float, *, samples: int=600, rtol: float=1e-9, atol: float=1e-12) -> LateDustTransferResult`.
- Produces `fundamental_matrix_candidate_c_dust(k_hmpc: float, ...) -> np.ndarray` sampled on the same grid.

- [ ] **Step 1: Write RED initial-mode selection tests**

At the dust benchmark crossing, choose the local regular mode with density pullback closest to `delta_g=delta_f`, positive common growth, and growth index nearest the GR growing value. Require normalization `delta_common=1`, `|delta_relative|<1e-6`, and sign continuity under `k -> k*(1±1e-3)`.

- [ ] **Step 2: Run and witness RED**

Run: `pytest tests/test_candidate_c_dust_late_transfer.py::test_gr_connected_initial_mode_is_adiabatic_and_continuous -v`
Expected: FAIL because the late-transfer module does not exist.

- [ ] **Step 3: Implement continuous mode selection**

Use the canonical phase matrix at the crossing, the observable pullback, and overlap/sign continuity. Do not independently sort modes by eigenvalue at each later time; integration itself carries identity.

- [ ] **Step 4: Implement `N=ln a` integration**

Convert the cosmic canonical matrix by `d/dN=(1/H_g)d/dt`. Cache background/action coefficients on repeated RHS calls if needed, but do not interpolate across a rank/condition failure. Sample a deterministic `N` grid.

- [ ] **Step 5: Add zero-length and tolerance-convergence controls**

Require identity/fundamental behavior for `a_initial=a_final` in a low-level helper, and compare `rtol={1e-8,3e-9,1e-9}` for a representative `k=0.1 h/Mpc`; final `R` must converge within a predeclared numerical tolerance before scientific interpretation.

- [ ] **Step 6: Add the four required late scales**

Run `k={0.01,0.05,0.1,0.2} h/Mpc`. Tests require finite outputs, no rank loss, bounded condition diagnostics, and `R(a_initial)` consistent with zero. Do **not** assert the quasi-static `0.123` value; only persist the computed result after it is independently stable.

- [ ] **Step 7: Verify the fundamental matrix reproduces the direct adiabatic run**

Multiply the sampled fundamental matrix by the selected initial phase vector and compare with direct integration to `rtol<=2e-7` for all six phase components after scale-aware normalization.

- [ ] **Step 8: Run Task-8 tests and commit**

Run: `pytest tests/test_candidate_c_dust_late_transfer.py -v`
Expected: PASS.

Commit: `feat: integrate late Candidate C dust transfer`

---

### Task 9: Explicit common/relative input lift and 2x2 density transfer

**Files:**
- Create: `numerics/candidate_c_dust_transfer_matrix.py`
- Create: `tests/test_candidate_c_dust_transfer_matrix.py`

**Interfaces:**
- Produces dataclass `DensityModeLift(common_phase: np.ndarray, relative_phase: np.ndarray, density_matrix: np.ndarray)`.
- Produces `build_density_mode_lift(a: float, *, k_hmpc: float) -> DensityModeLift`.
- Produces `density_transfer_matrix(k_hmpc: float, *, a_final: float=1.0) -> np.ndarray` with sector order `(g,f)` only after the lift is invertible and regression-tested.

- [ ] **Step 1: Write RED lift tests**

Require the common vector to have `delta_common=1`, `delta_relative≈0`; require the relative vector to have `delta_common≈0`, `delta_relative=1`; both must be regular finite phase-space directions and linearly independent.

- [ ] **Step 2: Run and witness RED**

Run: `pytest tests/test_candidate_c_dust_transfer_matrix.py::test_common_relative_lift_has_declared_density_normalization -v`
Expected: FAIL because the lift does not exist.

- [ ] **Step 3: Implement the regular relative/isocurvature lift**

Select the finite local mode/direction with maximal relative-density projection subject to orthogonality from the common density direction; fix its sign by positive `delta_relative` and track continuity by overlap.

- [ ] **Step 4: Build and test the sector-density 2x2 transfer**

Use the six-dimensional fundamental matrix and the explicit lift. Verify that applying the 2x2 matrix to the sector-density basis agrees with full phase propagation followed by observable pullback for both basis columns.

- [ ] **Step 5: Add basis-rescaling invariance**

Rescale either phase lift vector before normalization and require the final 2x2 density transfer to remain unchanged to `rtol<=1e-10`.

- [ ] **Step 6: Run Task-9 tests and commit**

Run: `pytest tests/test_candidate_c_dust_transfer_matrix.py -v`
Expected: PASS.

Commit: `feat: expose dust sector density transfer matrix`

---

### Task 10: Gate-2B verification and scientific checkpoint

**Files:**
- Modify: `research/GATE2B_CHECKPOINT.md`
- Modify: `research/GATE2B_RAF.md`
- Create: `research/LATE_DUST_TRANSFER_RESULT.md`
- No production coefficient changes in this task.

**Interfaces:**
- Consumes all Task-1..9 outputs.
- Produces the authoritative numerical table for `k={0.01,0.05,0.1,0.2} h/Mpc` and the updated restart instruction.

- [ ] **Step 1: Run the focused full solver suite in a complete worktree**

Run:
`pytest tests/test_candidate_c_dust_background.py tests/test_de_felice_dust_phase_action.py tests/test_de_felice_two_dust_action.py tests/test_de_felice_dust_physical_action.py tests/test_canonical_quadratic_evolution.py tests/test_de_felice_dust_observables.py tests/test_de_felice_dust_local_regressions.py tests/test_candidate_c_dust_late_transfer.py tests/test_candidate_c_dust_transfer_matrix.py -v`
Expected: all PASS.

- [ ] **Step 2: Run the existing De Felice/Gate-2 regressions**

At minimum run existing tests covering matter Eq. (54), exact-quadratic two-matter action, BD time canonicalization, Case-C audits, Candidate-C background and principal-action diagnostics. Expected: no new failures relative to the branch baseline.

- [ ] **Step 3: Run the complete repository test suite**

Run: `pytest -q`
Expected: record exact pass/fail counts. Any intentionally RED historical test must be identified by name and either updated because its premise is superseded or left documented; do not call the branch GREEN while unexplained failures remain.

- [ ] **Step 4: Record the scientific outputs without fitting them to the prior bound**

For each required `k`, record final `delta_g`, `delta_f`, `delta_common`, `delta_relative`, `R`, conditioning maxima, solver tolerance convergence, and dust-vs-full-background deviation over the integrated interval.

- [ ] **Step 5: Apply the decision rule**

Classify the late-linear spontaneous-conversion hypothesis as strongly disfavored if the validated solver keeps `|R(z=0,k)| << 1` on all required scales. If any `|R|=O(1)`, require regularity, kinetic/BD/auxiliary conditioning and mode continuity before treating it as a physical result.

- [ ] **Step 6: Update checkpoint/RAF and commit**

Commit: `research: record late dust transfer verdict`

The next task after this plan is the three-fluid visible-radiation extension only if the dust benchmark survives its validation and the scientific question warrants the added degree of freedom.