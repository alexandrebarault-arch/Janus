# Late Dust Canonical Transfer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first trustworthy time-domain scalar transfer solver for a strictly on-shell Candidate-C-like dust+dust benchmark, from that benchmark's own `m_eff/H=1` crossing to today, using the validated De Felice/Hassan-Rosen action and reporting physical sector-density conversion.

**Architecture:** Make the dust limit regular at the action level by Legendre-transforming each P(X) sector, then eliminate metric auxiliaries, dust phase momenta and the BD scalar to recover a regular three-coordinate quadratic action. Evolve canonical phase variables `(Y,Pi)` so the solver never differentiates `K` or `C`, while retaining reconstruction maps back to raw dust momenta and physical densities. All action coefficients and coefficient derivatives come from one strictly on-shell dust+dust background provider; full Candidate C with radiation is comparison data only.

**Tech Stack:** Python, NumPy, SciPy `solve_ivp`, pytest, existing JANUS `numerics/*` De Felice/Hassan-Rosen modules.

**Spec:** `docs/superpowers/specs/2026-10-13-late-dust-canonical-transfer-design.md`

## Global Constraints

- Work on `research/gate2b-nonhomothetic-transfer`; create an isolated worktree before implementation.
- Do not use the historical Comelli 12x12 closure as a physical input.
- Do not tune Eq. (44), Eq. (45)-(46), Eq. (54), EH, HR or matter coefficients.
- Do not retain a finite artificial dust sound speed in production integration.
- Do not mix a dust perturbation action with the radiation-containing Candidate-C metric background.
- Every derivative entering BD canonicalization must follow one on-shell background family.
- Use the direct O(delta^2) HR interaction, never the nonlinear-potential finite-difference route.
- Preserve Eq. (72) and `canonicalize_linear_zdot_time_dependent()`.
- The six-dimensional fundamental matrix is authoritative; a 2x2 density transfer is allowed only after an explicit phase-space lift is fixed.
- Full-repository GREEN claims require a complete worktree test run.

## Review Focus

1. **f-sector momentum normalization:** apply `n xi^3` exactly once between local matter momentum and common-normalized momentum; tests in Tasks 2 and 6.
2. **BD boundary momentum shift:** undo the time-dependent integration-by-parts generating function before reading physical matter momenta; Task 6.
3. **Background consistency:** removing radiation requires re-solving the present dust branch root `y0`, and no low-level reducer may silently accept a full-radiation metric with dust-only densities; Tasks 1 and 4.
4. **Near-singular reductions:** auxiliary, dust-momentum, BD and kinetic blocks must fail fast with condition diagnostics; Tasks 3-5.
5. **Mode identity/sign continuity:** common and relative phase directions must vary continuously under small changes in `a` and `k`; Tasks 8-9.

---

### Task 1: Strictly on-shell Candidate-C dust background

**Files:**
- Modify: `numerics/flrw_two_matter.py`
- Modify: `numerics/candidate_c_transfer.py`
- Create: `numerics/candidate_c_dust_background.py`
- Create: `tests/test_candidate_c_dust_background.py`
- Reuse: `tests/test_candidate_c_transfer_background.py`

**Interfaces:**
- Produces `branch_log_derivatives(a: float, y: float, p: Params) -> tuple[float, float]` in `flrw_two_matter.py`.
- Produces `candidate_c_dust_params() -> Params`.
- Produces `CandidateCDustBackgroundPoint(y,y_N,y_NN,metric,derivatives,rho_g_m,rho_f_m)`.
- Produces `candidate_c_dust_background_point(a: float, *, k_hmpc: float) -> CandidateCDustBackgroundPoint`.
- Produces `candidate_c_dust_meff_over_H(a: float) -> float` and `candidate_c_dust_linear_start() -> float`.

- [ ] **Step 1: Write RED tests for generic implicit branch derivatives**

Compare `branch_log_derivatives()` with centered differences of `solve_branch()` on full Candidate C at `z={0,10,100}` and with current `candidate_c_transfer.py` values; require `rtol<=2e-5`.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_candidate_c_dust_background.py::test_generic_branch_log_derivatives_match_candidate_c -v`
Expected: FAIL because `branch_log_derivatives` is absent.

- [ ] **Step 3: Implement the generic derivative helper and refactor `candidate_c_transfer.py` to call it**

Keep the existing analytic implicit-polynomial derivative, parameterized by `Params`; do not change full Candidate-C outputs.

- [ ] **Step 4: Verify the existing full-background tests**

Run: `pytest tests/test_candidate_c_transfer_background.py tests/test_candidate_c_dust_background.py::test_generic_branch_log_derivatives_match_candidate_c -v`
Expected: PASS.

- [ ] **Step 5: Write RED tests for `candidate_c_dust_params()`**

Require:
- `omega_g_r0 == 0`;
- `beta1..beta4`, `alpha`, `omega_g_m0`, `omega_f_m0`, `m2_over_H02` unchanged from `candidate_c()`;
- `y0` is re-solved, not copied blindly;
- present dust branch residual at `(a=1,y=y0_dust)` `<1e-12` with `omega_f=omega_f_m0`;
- select the late healthy root continuously connected to the original Candidate-C root (numerically the shift is tiny, but the equation, not that smallness, defines it).

- [ ] **Step 6: Implement the strict dust parameter construction**

Start from `candidate_c()`, set radiation to zero, solve the **present-day dust branch constraint directly for y** with the same `omega_g_m0` and `omega_f_m0`, select the root continuously connected to full Candidate C, then return `dataclasses.replace(..., omega_g_r0=0.0, y0=y0_dust)`. Do not call `positive_real_roots()` until this normalized `y0_dust` has been fixed because its polynomial constant term contains `omega_f_m0*y0^3`.

- [ ] **Step 7: Write and implement dust-background tests/provider**

At `a={1,0.5,0.1,1/17}` require branch residual `<1e-11`, correct dust density scalings, and analytic `c_N` agreement with centered on-shell branch differences to `rtol<=3e-5`. Locate a unique continuous late `m_eff/H=1` crossing on this dust provider.

- [ ] **Step 8: Compare dust benchmark to full Candidate C**

On a deterministic grid from dust crossing to today record finite relative differences in `H,y,c,m_eff/H,c_s,grav^2`. At `a=0.5`, reproduce the known principal-speed dust/full shift at order `1.2e-5` relative (tolerance loose enough to account for the newly re-solved `y0`).

- [ ] **Step 9: Run Task-1 tests and commit**

Run: `pytest tests/test_candidate_c_transfer_background.py tests/test_candidate_c_dust_background.py -v`
Expected: PASS.

Commit: `feat: add strictly on-shell Candidate C dust background`

---

### Task 2: Regular one-sector dust phase action

**Files:**
- Create: `numerics/de_felice_dust_phase_action.py`
- Create: `tests/test_de_felice_dust_phase_action.py`
- Reuse: `numerics/de_felice_matter_action.py`

**Interfaces:**
- `finite_cs2_phase_density(..., momentum: float, cs2: float) -> float`.
- `dust_phase_density(*, rho, lapse, scale_factor, k, Phi, B, psi, E, q, momentum) -> float`.
- `physical_density_from_phase_momentum(*, momentum_local, rho, psi) -> float`.
- `common_normalized_momentum(*, momentum_local, prefactor) -> float` and inverse helper.

- [ ] **Step 1: Write RED finite-`cs2` Legendre tests**

For generic tuples solve `qdot-Phi = cs2*(momentum/(rho+P)-3*psi)` and require the phase form to reproduce `kessence_scalar_quadratic_density()` after substitution to `rtol<=2e-13`.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_de_felice_dust_phase_action.py::test_finite_cs2_legendre_form_matches_eq54 -v`
Expected: FAIL because module/functions are absent.

- [ ] **Step 3: Implement finite-`cs2` phase form**

Use `A=rho+P` and `H_temp = p*Phi + cs2*(p-3A*psi)^2/(2A) - A*Phi^2/2`, keeping the Eq. (54) pressure-metric and spatial terms unchanged.

- [ ] **Step 4: Pin the exact dust limit**

Require the `P=0,cs2->0` phase density to be finite and to equal the finite-`cs2` form with only the vanishing `cs2*(p-3A psi)^2/(2A)` removed. Pin `delta_rho=p-3 rho psi`.

- [ ] **Step 5: Pin g/f normalization**

Round-trip local momentum through prefactors `1` and `n*xi**3` at `1e-14` relative.

- [ ] **Step 6: Run and commit**

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

**Interfaces:**
- `DUST_DYNAMIC_ORDER=("psi_f","E_f","q_g","q_f")`.
- `DUST_RATE_ORDER=("psi_f_dot","E_f_dot","q_g_dot","q_f_dot")`.
- `DUST_AUXILIARY_ORDER=("Phi_g","Phi_f","B_g","B_f","p_g","p_f")`.
- `DustFlatGaugeReducedAction` stores final 8x8 Hessian, separate metric-aux/dust-momentum condition numbers, and reconstruction maps for all six eliminated variables from old states/rates.
- `eliminate_flat_gauge_two_dust(bg,bgp,*,betas,rho_g,rho_f) -> DustFlatGaugeReducedAction`.

- [ ] **Step 1: Write RED exact-quadratic structural test**

Require augmented order `(4 states,4 rates,4 metric auxiliaries,2 dust momenta)`, symmetry/finite Hessian, and no public finite-`cs2` argument.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_de_felice_two_dust_action.py::test_two_dust_augmented_action_is_exact_quadratic_and_symmetric -v`
Expected: FAIL.

- [ ] **Step 3: Implement augmented action**

Reuse audited Eq. (44), direct O(delta^2) HR, and Task-2 dust phase sectors. Extract the Hessian by exact quadratic polarization with unit basis vectors, not a tiny perturbation amplitude.

- [ ] **Step 4: Write RED Schur/reconstruction tests**

At Case C and Candidate-C dust control points require metric auxiliary rank 4, then dust-momentum rank 2 after metric elimination; final 8x8 Hessian finite/symmetric; reconstruction substitution must reproduce the Schur-reduced action for deterministic vectors to `rtol<=1e-10`.

- [ ] **Step 5: Implement two-stage elimination with diagnostics**

Fail on rank loss, non-finite blocks or unusable condition numbers. Preserve reconstruction maps.

- [ ] **Step 6: Run and commit**

Run: `pytest tests/test_de_felice_two_dust_action.py -v`
Expected: PASS.

Commit: `feat: reduce exact two-dust scalar action`

---

### Task 4: Time-dependent BD physical reduction on one on-shell family

**Files:**
- Create: `numerics/de_felice_dust_physical_action.py`
- Create: `tests/test_de_felice_dust_physical_action.py`
- Reuse: `numerics/bd_time_canonicalization.py`
- Reuse: `numerics/de_felice_two_matter_action.py::bd_basis_transform`

**Interfaces:**
- `validate_dust_background_consistency(bg,bgp,*,betas,rho_g,rho_f,rtol: float=1e-8) -> None`.
- `DustPhysicalAction` stores transformed/canonical/physical Hessians, `K,C,M`, BD coefficient/residual, condition diagnostics, and composed reconstruction maps.
- `dust_physical_action(bg,bgp,*,betas,rho_g,rho_f,dot_c,mu_measure,validate_background=True) -> DustPhysicalAction`.
- `candidate_c_dust_physical_action(a: float, *, k_hmpc: float, derivative_step_N: float=1e-4) -> DustPhysicalAction`.

- [ ] **Step 1: Write RED three-direction/BD tests**

At deterministic Case-C and Candidate-C dust points require `Zdot` kinetic residual `<1e-8`, algebraic `Z` invertibility and exactly three physical kinetic directions.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_de_felice_dust_physical_action.py::test_two_dust_bd_reduction_has_three_physical_directions -v`
Expected: FAIL.

- [ ] **Step 3: Implement generic BD reduction with map composition**

Apply Eq. (72), `canonicalize_linear_zdot_time_dependent()`, then algebraic Z Schur elimination; retain the inverse/reconstruction information required by observables.

- [ ] **Step 4: Implement on-shell `dot_c` adapter**

Compute `C[:,Z]` at `N±h,N±2h` on `candidate_c_dust_background_point()` and use a five-point derivative; `mu_measure=3H_g`. Compare `h={2e-4,1e-4,5e-5}` and require `rtol<=2e-3` for non-negligible components with scale-aware absolute tolerance for near-zero components.

- [ ] **Step 5: Pin background-consistency rejection**

Call the **generic** `dust_physical_action()` with a full-radiation `candidate_c_background_point()` plus dust-only densities and `validate_background=True`; require a clear consistency error. Separately assert the Candidate-C dust adapter's internally used metric/densities equal `candidate_c_dust_background_point()` so the high-level path cannot mix families.

- [ ] **Step 6: Run and commit**

Run: `pytest tests/test_bd_time_canonicalization.py tests/test_de_felice_dust_physical_action.py -v`
Expected: PASS.

Commit: `feat: add on-shell dust BD physical reduction`

---

### Task 5: Canonical phase RHS and fundamental matrix

**Files:**
- Create: `numerics/canonical_quadratic_evolution.py`
- Create: `tests/test_canonical_quadratic_evolution.py`

**Interfaces:**
- `canonical_phase_matrix(*, K,C,M,H_g) -> np.ndarray` returns the 6x6 cosmic-time matrix for `(Y,Pi)`.
- `canonical_phase_matrix_N(*, K,C,M,H_g) -> np.ndarray` returns the matrix for `d/dN`, i.e. cosmic matrix divided by `H_g`.
- `canonical_rhs(t,state,*,coefficients_provider) -> np.ndarray`.
- `fundamental_rhs(t,flat_matrix,*,coefficients_provider) -> np.ndarray`.

- [ ] **Step 1: Write RED constant-system test**

For diagonal `K`, `C=0`, known `M`, require analytic oscillator/growing roots.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_canonical_quadratic_evolution.py::test_canonical_phase_matrix_matches_known_quadratic_system -v`
Expected: FAIL.

- [ ] **Step 3: Implement canonical equations**

Use only `Ydot=solve(K,Pi-C.T@Y)` and `Pidot=M@Y+C@Ydot-3H_g*Pi`; never differentiate `K` or `C`.

- [ ] **Step 4: Add time-dependent synthetic equivalence test**

Compare canonical integration to the explicitly expanded Euler-Lagrange equation containing analytic `dot K,dot C,3H`; require `rtol<=1e-8` over a short interval.

- [ ] **Step 5: Add singular-K failure test**

Rank-deficient or non-finite K must fail with condition diagnostics.

- [ ] **Step 6: Run and commit**

Run: `pytest tests/test_canonical_quadratic_evolution.py -v`
Expected: PASS.

Commit: `feat: add canonical quadratic phase evolution`

---

### Task 6: Physical density observable pullback

**Files:**
- Create: `numerics/de_felice_dust_observables.py`
- Create: `tests/test_de_felice_dust_observables.py`
- Modify: `numerics/de_felice_dust_physical_action.py` only if one missing reconstruction matrix must be exposed.

**Interfaces:**
- `DustObservables(delta_rho_g,delta_rho_f,delta_g,delta_f,delta_common,delta_relative)`.
- `undo_bd_boundary_momentum_shift(...)`.
- `reconstruct_dust_observables(action: DustPhysicalAction, *, Y,Pi,rho_g,rho_f,bg) -> DustObservables`.

- [ ] **Step 1: Write RED boundary-shift round-trip test**

For synthetic nonzero `c_i`, apply and undo the generating function `F=sum_{i!=Z} c_i Y_i Z + 1/2 c_Z Z^2`; require momentum round-trip to `1e-13`.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_de_felice_dust_observables.py::test_boundary_momentum_pullback_round_trips -v`
Expected: FAIL.

- [ ] **Step 3: Implement full reconstruction**

Recover `Ydot`, Z, old states/rates, metric auxiliaries and dust momenta. Divide f common-normalized momentum by `n*xi**3` exactly once; then use `delta_rho=p_local-3rho psi`.

- [ ] **Step 4: Add finite-`cs2` oracle regression**

At a generic regulated point compare phase-momentum density with the direct Eq. (54) P(X) density identity for both sectors; `rtol<=1e-9`.

- [ ] **Step 5: Add linear scaling and density-domain tests**

Scale the whole perturbation state by `{0.1,3,-2}` and require linear observable scaling. Reject non-positive background densities.

- [ ] **Step 6: Run and commit**

Run: `pytest tests/test_de_felice_dust_observables.py -v`
Expected: PASS.

Commit: `feat: reconstruct dust density observables`

---

### Task 7: Local physics regressions for the exact-dust phase system

**Files:**
- Create: `numerics/de_felice_dust_local_modes.py`
- Create: `tests/test_de_felice_dust_local_regressions.py`

**Interfaces:**
- `local_phase_squared_speeds(action: DustPhysicalAction, *, a,k,H_g) -> np.ndarray` from high-k eigenvalues of the canonical **N-time** phase matrix, paired into physical modes.

- [ ] **Step 1: Write RED Case-C regression**

At Case C `a=0.05`, use `k={800,1600,3200}` and `1/k^2` extrapolation; require gravity `c_s^2=-0.6665833419871022` to `rtol<=5e-5`, two dust branches -> 0.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_de_felice_dust_local_regressions.py::test_case_c_exact_dust_phase_recovers_principal_gravity_branch -v`
Expected: FAIL until pipeline is complete.

- [ ] **Step 3: Implement mode pairing**

Pair `+/-` eigenvalues by squared phase speed, preserve zero dust branches, reject unpaired complex contamination above scale-aware tolerance.

- [ ] **Step 4: Add Candidate-C dust regression**

At `a=0.5`, require gravity extrapolation `0.6920714772884699` to `rtol<=5e-5`, two dust branches -> 0.

- [ ] **Step 5: Add GR/decoupled dust control**

Require standard pressureless growing/decaying behavior and no spurious acoustic branch.

- [ ] **Step 6: Run and commit**

Run: `pytest tests/test_de_felice_dust_local_regressions.py -v`
Expected: PASS.

Commit: `test: validate exact dust scalar principal modes`

---

### Task 8: Late integration and GR-connected adiabatic mode

**Files:**
- Create: `numerics/candidate_c_dust_late_transfer.py`
- Create: `tests/test_candidate_c_dust_late_transfer.py`

**Interfaces:**
- `LateDustTransferResult(a,Y,Pi,delta_g,delta_f,delta_common,delta_relative,R,conditioning)`.
- `select_gr_connected_adiabatic_mode(a: float, *, k_hmpc: float) -> np.ndarray`.
- `solve_candidate_c_dust_late(k_hmpc: float, *, samples=600, rtol=1e-9, atol=1e-12) -> LateDustTransferResult`.
- `fundamental_matrix_candidate_c_dust(k_hmpc: float, ...)` returning sampled 6x6 matrices.

- [ ] **Step 1: Write RED mode-selection test**

At the dust crossing, eigendecompose the canonical `N`-matrix. Among regular finite directions select the real/growing direction minimizing a documented score dominated by `|delta_relative|/|delta_common|` and then `|growth_index-1|`; normalize `delta_common=1`, require `|delta_relative|<1e-6`, positive growth and sign/overlap continuity under `k -> k*(1±1e-3)`.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_candidate_c_dust_late_transfer.py::test_gr_connected_initial_mode_is_adiabatic_and_continuous -v`
Expected: FAIL.

- [ ] **Step 3: Implement mode selection and continuity convention**

Fix sign by positive common density. Later times are not re-sorted: integration itself carries the mode identity.

- [ ] **Step 4: Implement `N=ln a` integration**

Use `canonical_phase_matrix_N()`, adaptive `solve_ivp`, deterministic output grid, and coefficient caching only if it does not cross a failed rank/condition check.

- [ ] **Step 5: Add tolerance convergence**

For `k=0.1 h/Mpc`, compare `rtol={1e-8,3e-9,1e-9}`; final R must converge within a declared numerical tolerance before scientific interpretation.

- [ ] **Step 6: Add required scales**

Run `k={0.01,0.05,0.1,0.2} h/Mpc`. Require finite outputs, no rank loss, finite condition diagnostics and `R(a_initial)≈0`. Do not fit/assert the old quasi-static `0.123` reference.

- [ ] **Step 7: Verify the fundamental matrix reproduces direct propagation**

Propagate the initial adiabatic vector through the sampled fundamental matrix and compare with direct integration to `rtol<=2e-7` after scale-aware normalization.

- [ ] **Step 8: Run and commit**

Run: `pytest tests/test_candidate_c_dust_late_transfer.py -v`
Expected: PASS.

Commit: `feat: integrate late Candidate C dust transfer`

---

### Task 9: Explicit common/relative input lift and 2x2 density transfer

**Files:**
- Create: `numerics/candidate_c_dust_transfer_matrix.py`
- Create: `tests/test_candidate_c_dust_transfer_matrix.py`

**Interfaces:**
- `DensityModeLift(common_phase: np.ndarray, relative_phase: np.ndarray, density_matrix: np.ndarray)`.
- `build_density_mode_lift(a: float, *, k_hmpc: float) -> DensityModeLift`.
- `density_transfer_matrix(k_hmpc: float, *, a_final: float=1.0) -> np.ndarray`, sector order `(g,f)`.

- [ ] **Step 1: Write RED lift normalization test**

Require common phase `delta_common=1,delta_relative≈0`; relative phase `delta_common≈0,delta_relative=1`; finite, linearly independent, continuous under small k changes.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_candidate_c_dust_transfer_matrix.py::test_common_relative_lift_has_declared_density_normalization -v`
Expected: FAIL.

- [ ] **Step 3: Implement regular relative/isocurvature lift**

Use the local regular phase subspace at the initial crossing. Remove the common-mode projection in **density-observable space**, then choose the remaining finite direction with maximal relative-density projection; normalize `delta_relative=1`, require `delta_common≈0`, and fix sign positive. If no unique continuous finite direction exists, fail explicitly and keep only the 6D fundamental matrix rather than inventing a 2x2 lift.

- [ ] **Step 4: Build/test sector-density transfer**

Use the 6D fundamental matrix and explicit lift. For both input basis columns, require 2x2 output to agree with full phase propagation + observable pullback.

- [ ] **Step 5: Add basis-rescaling invariance**

Rescale either raw phase direction before normalization; final 2x2 matrix unchanged to `rtol<=1e-10`.

- [ ] **Step 6: Run and commit**

Run: `pytest tests/test_candidate_c_dust_transfer_matrix.py -v`
Expected: PASS or an explicitly documented non-existence of a unique regular 2x2 lift; the latter does not invalidate the 6D solver.

Commit: `feat: expose dust sector density transfer matrix`

---

### Task 10: Gate-2B verification and scientific checkpoint

**Files:**
- Modify: `research/GATE2B_CHECKPOINT.md`
- Modify: `research/GATE2B_RAF.md`
- Create: `research/LATE_DUST_TRANSFER_RESULT.md`

**Interfaces:** consumes Tasks 1-9; produces the authoritative late-dust numerical table and restart state.

- [ ] **Step 1: Run focused complete-worktree suite**

Run:
`pytest tests/test_candidate_c_dust_background.py tests/test_de_felice_dust_phase_action.py tests/test_de_felice_two_dust_action.py tests/test_de_felice_dust_physical_action.py tests/test_canonical_quadratic_evolution.py tests/test_de_felice_dust_observables.py tests/test_de_felice_dust_local_regressions.py tests/test_candidate_c_dust_late_transfer.py tests/test_candidate_c_dust_transfer_matrix.py -v`
Expected: all applicable tests PASS; Task-9 may explicitly report no unique 2x2 lift while the 6D solver remains valid.

- [ ] **Step 2: Run existing De Felice/Gate-2 regressions**

At minimum include Eq. (54), exact-quadratic two-matter, BD canonicalization, Case-C audits, Candidate-C background and principal-action tests. No unexplained new failures.

- [ ] **Step 3: Run full repository suite**

Run: `pytest -q`
Record exact pass/fail counts. Any intentional historical RED must be named and its premise classified as still active or superseded; do not claim full GREEN otherwise.

- [ ] **Step 4: Record scientific outputs without fitting prior expectations**

For each `k={0.01,0.05,0.1,0.2} h/Mpc` record final `delta_g,delta_f,delta_common,delta_relative,R`, conditioning maxima, tolerance convergence, and dust/full-background deviation over the integrated interval.

- [ ] **Step 5: Apply decision rule**

Late-linear spontaneous conversion is strongly disfavored if validated runs keep `|R(z=0,k)| << 1` on all required scales. Any `|R|=O(1)` is accepted for interpretation only if auxiliary/BD/kinetic regularity and continuous mode identity also hold.

- [ ] **Step 6: Update checkpoint/RAF and commit**

Commit: `research: record late dust transfer verdict`

The three-fluid radiation extension is a later task only if this dust benchmark is validated and the scientific result warrants the added matter degree of freedom.