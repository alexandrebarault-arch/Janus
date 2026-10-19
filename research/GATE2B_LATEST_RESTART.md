# Gate 2B — latest restart checkpoint

Date: 2026-10-16
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **Gate 2B OPEN; finite-H linear Stueckelberg bridge is closed; finite-mu HR promotion in the pre-metric augmented action is the active hard block.**

Read first after interruption:

1. `research/NONHOMOTHETIC_PREBD_STUECKELBERG_AUDIT.md`;
2. `research/NONHOMOTHETIC_LINEAR_BRIDGE_AUDIT.md`;
3. `research/AOKI_COMPACT_METRIC_SCHUR_AUDIT.md`;
4. `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`;
5. `research/GATE2B_CHECKPOINT.md`.

## 1. Closed results — do not redo

Unless contradictory evidence appears, the following are closed at audit level:

- De Felice/Hassan-Rosen scalar action reconstruction;
- time-dependent BD canonicalization;
- Case-C `NG3` and all three Eq. (85) principal modes;
- Candidate-C dust+dust principal gravity branch;
- exact-dust late six-dimensional scalar phase space;
- proof that four late adiabatic density conditions leave two helicity-0 matching data free;
- exact non-homothetic spherical Stueckelberg temporal relation;
- finite weak-metric Candidate-C folds;
- homogeneous kinetic-sign warning near fold 1;
- compact-support homothetic Aoki `K_S,c_S^2` oracle;
- compact weak Einstein-Hilbert + HR action with four metric potentials Schur-eliminated;
- finite-mass homothetic static control;
- principal non-homothetic `pi` map;
- finite-H pre-BD De Felice <-> Stueckelberg bridge;
- augmented transform-before-metric-Schur equivalence on Candidate C.

## 2. Candidate-C fold warning retained

Regular nonlinear pair:

- fold 1: `a_1 ~= 0.0301646`, `z_1 ~= 32.151`, `mu_1 ~= -0.768883`;
- fold 2: `a_2 ~= 0.0491246`, `z_2 ~= 19.356`, `mu_2 ~= -0.67015`.

Independent homogeneous kinetic-sign zero:

`a_K ~= 0.030136993`, `z_K ~= 32.18181`, `mu_K ~= -0.76624`.

The near-coincidence is a strong warning, **not** yet a no-go theorem.

## 3. Homothetic six-field action oracle — GREEN

The compact-support action with weak metric variables reproduces Aoki's nonlinear kinetic and gradient coefficients at about the `0.2%` level at the committed compact resolution. A finite-mass static root is also recovered at about the `0.22%` level.

Thus the homothetic action is no longer the blocker.

## 4. Principal non-homothetic map — GREEN as a high-frequency statement

The independently extracted high-k relation is

`delta eta = -(1/(c a^2)) partial_eta pi`,

`delta r = +(1/a^2) partial_r pi`,

or equivalently `T/Ldot -> -a^2/c` in g-cosmic time.

This reduces to the Aoki map for `c -> 1`, but it is **not** a complete finite-H map.

## 5. Finite-H pre-BD Stueckelberg representation — GREEN

Do not invent the missing finite-H one-field `pi` corrections.  Change variables before the BD/null coordinate is removed.

Pre-BD De Felice state order:

`(Y1,Y2,Y3,Z,p_g,p_f)`.

Relative Stueckelberg state order:

`(Y1,Y2,L,T,p_g,p_f)`.

Exact bridge:

`Y3 = -2 L`,

`Z = - n H_f T + k^2 L/3`.

On Candidate C,

`n H_f = H_omega/a`,

`d(nH_f)/dt_g = (H_omega' - H_omega H)/a^2`.

The kinetic-null `Zdot` direction maps exactly to `Tdot`.  Therefore `T` is the time-dependent algebraic/BD coordinate and `L` is the physical spatial helicity-0 coordinate.

Implementation:

- `numerics/prebd_stueckelberg_transform.py`;
- `tests/test_prebd_stueckelberg_transform.py`;
- `tests/test_prebd_stueckelberg_el_equivalence.py`.

## 6. Finite-H Candidate-C linear oracle — GREEN at current numerical accuracy

The new Stueckelberg dust reducer is

- `numerics/candidate_c_linear_stueckelberg_action.py`;
- `tests/test_candidate_c_linear_stueckelberg_action.py`.

At `a=0.5`, `k=0.2 h/Mpc`, the independent reconstructed values are approximately

- Stueckelberg basis: `c_s^2 ~= 0.69092747`;
- original De Felice basis: `c_s^2 ~= 0.69092766`.

The basis discrepancy is about `2e-7` and decreases under derivative-step refinement.  Both pass the existing finite-k/double-precision tolerance against the independent asymptotic target

`c_s^2 = 0.692071477288...`.

This closes the finite-H **coordinate/reduction bridge**; it does not yet constitute an independent finite-mu native action.

## 7. Dust feedback is order-one — mandatory architecture ruling

The helicity-0 mode is not a pure metric/Stueckelberg mode at finite H.

At `a=0.5`, `k=0.2 h/Mpc`:

- full Stueckelberg + two-dust system: `c_s^2 ~= 0.69093`;
- artificially clamping both dust coordinate/rate pairs: `c_s^2 ~= 0.49432`.

Difference: about `0.197`.

Therefore the two dust phase pairs must remain dynamical through the constrained reduction.  They must **not** be Schur-eliminated as static auxiliaries.

Regression:

- `tests/test_candidate_c_stueckelberg_matter_feedback.py`.

## 8. Pre-metric augmented insertion point — GREEN

The exact flat-gauge dust Hessian before metric elimination has old order

`(psi_f,E_f,q_g,q_f, rates[4], Phi_g,Phi_f,B_g,B_f,p_g,p_f)`.

A 14x16 map now transforms it to

- states `(Y1,Y2,L,T,p_g,p_f)`;
- six corresponding rates (`p_gdot,p_fdot` are structural zeros);
- four untouched metric auxiliaries `(Phi_g,Phi_f,B_g,B_f)`.

Direct identities:

`psi_f = k^2 L/3 - nH_f T`,

`E_f = -2L`,

`q_g = Y1`,

`q_f = Y2 - T`.

Transforming the augmented action first and then eliminating the metric auxiliaries reproduces the validated historical route to relative errors

- `4.2e-13` at `(a,k)=(0.3,0.1 h/Mpc)`;
- `5.3e-11` at `(0.5,0.2 h/Mpc)`;
- `5.8e-13` at `(0.7,0.1 h/Mpc)`.

The metric block remains rank 4.

Regression:

- `direct_flat_augmented_transform(...)` in `numerics/prebd_stueckelberg_transform.py`;
- `tests/test_candidate_c_stueckelberg_augmented_action.py`.

This is the insertion point for the finite nonlinear interaction.

## 9. Failed shortcuts — do not repeat

Do not:

- reuse the homothetic `c=1` pi map unchanged;
- read the Candidate-C speed from a frozen local WKB/Schur system;
- subtract an off-shell `H=0` reference;
- treat the dust amplitudes as static auxiliaries;
- compare raw reduced Hessians across a time-dependent point transformation instead of full Euler-Lagrange equations;
- interpret a fold itself as proof of a kinetic zero.

## 10. Current active calculation

Construct the **finite-mu Hassan-Rosen interaction Hessian/correction** in the validated augmented interface

`(Y1,Y2,L,T,p_g,p_f, rates, Phi_g,Phi_f,B_g,B_f)`.

The Einstein-Hilbert and dust phase sectors are already validated and must not be retuned.

The finite-mu construction must pass two independent limits:

1. `mu -> 0`: recover the augmented linear HR block and therefore the finite-H Candidate-C De Felice/Stueckelberg spectrum;
2. homothetic early-time limit: recover the already GREEN compact Aoki nonlinear `K_S,c_S^2` oracle.

Only after both limits are GREEN may the same action be evaluated on the regular Candidate-C nonlinear branch approaching

`a_1 ~= 0.0301646`.

## 11. After the finite-mu action passes both oracles

1. eliminate the four metric auxiliaries;
2. perform the time-dependent `Tdot` null/BD reduction;
3. retain both dust phase pairs;
4. compute the full kinetic and gradient operators toward fold 1;
5. determine whether the homogeneous kinetic-sign zero survives;
6. integrate a fold-crossing trajectory only if the constraint and kinetic systems remain regular;
7. derive `(Y3,Y3_N)` from that trajectory;
8. rerun the late exact-dust transfer;
9. add visible radiation only if the dust path survives.

## 12. Verification limitation

The new algebraic/EL map tests were executed directly in a reconstructed local workspace.  The Candidate-C spectral and augmented pre-metric equivalence numbers were independently reproduced from the committed formulas.  GitHub Actions remain disabled and the full repository has not been executed in one clean worktree.

`GATE_2B = OPEN`.


## 2026-10-17 incremental audit — finite-mu HR spherical spectral derivatives

New files:
- `numerics/finite_mu_hr_spectrum.py`
- `tests/test_finite_mu_hr_spectrum.py`

For the finite spherical interaction eigenvalues `(t,r,ell,ell)`, an independent closed polynomial evaluator now returns `U=sum beta_n e_n` plus the exact 3-vector first derivative and 3x3 Hessian. Tests cover direct four-eigenvalue symmetric-polynomial enumeration, independent centered-difference derivatives, Hessian symmetry, and the equal-radial/angular first-variation relation on both `mu=0` and `mu != 0` backgrounds.

Verification in the reconstructed local test workspace: `python -m pytest -q tests/test_finite_mu_hr_spectrum.py` -> **3 passed**. This is a targeted test, not the full suite.

**Scope warning:** these are eigenvalue-space algebraic derivatives, not yet derivatives of the full pullback `S=sqrt(g^-1 f)` with off-diagonal temporal/radial perturbations, and not a validated finite-mu dynamical action. They may be used only as an independent algebraic oracle for the forthcoming HR Hessian insertion.

Immediate next RED: construct the exact finite-mu HR pre-metric Hessian in the native augmented variables, differentiate the full common-chart square root including the off-diagonal radial block, and demonstrate that its `mu -> 0` Hessian equals the previously validated augmented linear HR action before attempting a finite-mu fold diagnosis.

## 13. 2026-10-17 — exact finite-mu native HR metric quadratic jet

**New tested deliverables:**

- `numerics/hr_native_quadratic_jet.py`;
- `tests/test_hr_native_quadratic_jet.py`;
- `research/NONHOMOTHETIC_HR_JET_AUDIT.md`.

A second-order Taylor-jet evaluator computes the exact native spherical HR
interaction potential, gradient, and complete 8x8 **metric-only** quadratic
Hessian at nonzero `mu` without perturbation-amplitude differencing.

The strictly central `r=0` Hessian recovers the De Felice Eq. (45)-(46)
quadratic HR interaction at `mu=0` (ALL lapse/shift/trace/shear variables).
At finite `mu` the central interaction-only identity is reproduced with
`alpha_eff=alpha*(1+mu)`. Independent JAX x64 Hessians also agree away
from the center, along with beta0/beta4 sector decoupling.

**Fresh reconstructed local verification:**
`PYTHONPATH=. OPENBLAS_NUM_THREADS=1 pytest -q tests/test_hr_native_quadratic_jet.py`
=> **10 passed** (JAX tests optional if not installed).

**Important limitation:** at `r>0`, this helper holds native `n,alpha`
at the center time and does **not** retain their shift-induced time drift;
the oscillatory `delta T,delta R` columns of the Hessian are **not yet
implemented**. Odd radial metric-shift terms start at `O(r)` and cannot
be mistaken for already phase-averaged Fourier coefficients. No new
full nonlinear/kinetic/gradient stability verdict follows.

**Updated immediate RAF (supersedes section 10's first implementation substep):**

1. Promote the new native HR jet to a full `delta T,delta R` +
   native metric **pre-Schur** Hessian, including `n(T),alpha(T)` drift
   and the `O(r^2)` background expansion; respect Fourier phases/parity.
2. Compare at `mu->0` with the independently validated
   `direct_native_augmented_transform` / De Felice Candidate-C
   linear interaction block.
3. Match the homothetic Aoki compact-support nonlinear
   `K_S,c_S^2` oracle **after** four metric constraints.
4. Then — and only then — calculate the finite-mu canonical/gradient
   matrices near fold 1, retaining both dust phase pairs.

**Gate 2B remains OPEN.** This was a local targeted RED/GREEN; full-worktree
regression has not yet run.

## 14. 2026-10-17 — additional native background drift GREEN

The finite-mu interaction helper now supports `n_dot,alpha_dot,n_ddot,alpha_ddot`
and evaluates these **background** quantities at
`T=t+sigma*r^2/2` by a second-order Taylor jet. The source and tests are
committed. Two newly witnessed RED→GREEN tests check the shifted-time
identity and preservation of the central `r=0` result. **12 targeted
local tests passed** (not the repository-wide suite).

**Immediate remaining input:** extend the interaction jet to the independent
oscillatory `delta T,delta R` perturbations and their Jacobian/radial-angle
components. The background shift is now included; the perturbative shift and
its derivative couplings still are not. Then link the resulting columns to
the validated native 16-dimensional augmented Hessian.

## 15. 2026-10-17 — 14x14 native finite-mu HR/Stueckelberg interaction Hessian

New files committed:
- `numerics/hr_native_stueckelberg_jet.py`;
- `tests/test_hr_native_stueckelberg_jet.py`.

The **local interaction-only** quadratic expansion now includes eight native
metric variables and six independent local chart-perturbation jets
`(deltaT,deltaT_t,deltaT_r,deltaR_t,deltaR_r,deltaR_over_r)`.
The f native background `n(T),alpha(T)` includes its supplied first and
second time derivatives under the full local `deltaT` perturbation.

Fresh reconstructed local verification together with the 8x8 module:
`PYTHONPATH=. OPENBLAS_NUM_THREADS=1 pytest -q tests/test_hr_native_stueckelberg_jet.py tests/test_hr_native_quadratic_jet.py`
**19 passed**. This includes independent JAX x64 14x14 Hessian controls at
both `mu=0` and finite `mu,r`, beta0/beta4 separation, and the exact
metric-only 8x8 principal block. See
`research/NONHOMOTHETIC_HR_JET_AUDIT.md` for limitations.

**Do not mistake the six chart jets for independent physical modes.** The
new matrix must still be pulled back to coherent `delta T(t,r),delta R(t,r)`
profiles, then assembled with the native EH+two-dust phase action and the
correct spatial/time profile integration. Terms involving derivatives of
native metric perturbations evaluated at shifted `T` are also not yet
included. No finite-mu kinetic/gradient/fold verdict is available.

**Next RAF:** implement/test a profile-to-jet map into the 14x14 HR Hessian,
then the complete 16-dimensional pre-metric augmented `(Y1,Y2,L,T,p_g,p_f)`
interaction (with full constraint/phase bookkeeping). Require both the
Candidate-C linear De Felice oracle and the nonlinear homothetic Aoki
`K_S,c_S^2` oracle after reduction before approaching fold 1.

`GATE_2B = OPEN`.

## 16. 2026-10-17 — regular radial profile projection (new restart head)

Added `numerics/hr_stueckelberg_profile_pullback.py` and corresponding tests.
This is a **kinematic interface** from a smooth spherical trial profile
`deltaT=T(t)F(r), deltaR=r L(t)F(r)` to the six chart jets in the newly
validated finite-mu 14x14 native HR interaction Hessian.

The new 14x12 map yields a local projected 12x12 interaction-only quadratic
form in eight native metric coordinates and `(T,L,Tdot,Ldot)`. A regular
`j0(kr)=sin(kr)/(kr)` profile is used only as a control of the map/center.
The complete gradient and Hessian transform consistently.

Fresh reconstructed local verification on three HR modules:
`PYTHONPATH=. OPENBLAS_NUM_THREADS=1 pytest -q tests/test_hr_stueckelberg_profile_pullback.py tests/test_hr_native_stueckelberg_jet.py tests/test_hr_native_quadratic_jet.py`
=> **24 passed** (JAX-dependent tests optional). The new profile cycle was
witnessed RED with an unimplemented stub and GREEN after implementing it.

**Important:** this is still not the Aoki physical eigenprofile or a complete
on-shell six-field action. No new physical `K_S`, `c_S^2`, or fold verdict
has been derived from this trial profile.

**Immediate next action for autonomous continuation:**
1. Build a coherent compact Fourier/spherical profile integral of the
   finite-mu native interaction, with background time drift and the full
   pullback of native perturbation-field rates;
2. insert it *before* the four metric constraints in the validated
   pre-BD `(Y1,Y2,L,T,p_g,p_f)` augmented action, with EH and both
   dust phase pairs retained;
3. require **both** previously validated independent oracles:
   finite-H Candidate-C `mu->0` De Felice linear principal scalar, and
   homothetic nonlinear Aoki `K_S,c_S^2`;
4. only after both pass, evaluate the true reduced kinetic and gradient
   coefficients on Candidate C through the first fold.

`GATE_2B = OPEN`; repository-wide regression is still unavailable.


## 17. 2026-10-18 — COMPACT REGULAR RADIAL HR INTEGRATION (CURRENT RESTART HEAD)

**New committed code and tests:**

- `numerics/hr_compact_radial_interaction.py`;
- `tests/test_hr_compact_radial_interaction.py`;
- `research/COMPACT_RADIAL_HR_INTERACTION_AUDIT.md`.

The preceding 14x14 native Hessian is now integrated over a finite spherical domain using an explicit C^3 compact scalar bump and Gauss-Legendre quadrature. The new 14x12 amplitude map makes native radial metric shifts odd and scalar traceless shears vanish at the center. It also consistently derives all six local chart jets from the same `(T,L,Tdot,Ldot)` amplitudes rather than treating them as independent physical fields.

**Independent targeted local run** (reconstructed exact native HR module):

`PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_compact_radial_interaction.py`
=> **6 passed**.

The tests cover exact radial profile derivatives, regularity/parity, 16/26-point quadrature convergence, action bilinear identity, beta0/beta4 sector separation, and invalid input checks.

**Scientific scope:** this is an **interaction-only spatial integration**, NOT a full time-domain constrained action or a finite-mu physical helicity-0 propagation operator. No new kinetic/gradient or fold crossing conclusion is supported. Do not diagonalize this 12x12 interaction Hessian to infer physical ghosts.

**Next exact action (RED):** include native f-field *perturbation-rate* sampling when its chart time is displaced by deltaT; independently test those cross-Hessian terms. Then integrate the same regular compact profiles into the EH + two-dust phase sectors, assemble before metric Schur/BD reduction and require both finite-H mu->0 De Felice and nonlinear homothetic Aoki oracles GREEN **on the same action**. Only then test Candidate-C fold 1.

**Resume order:** this section -> `research/COMPACT_RADIAL_HR_INTERACTION_AUDIT.md` -> `numerics/hr_compact_radial_interaction.py` -> `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`.

**Repository policy:** commit only on `research/gate2b-nonhomothetic-transfer`; leave `main` and `research/v2-flrw` intact. GitHub Actions are disabled; do not describe the local 6-test run as a full-branch regression.

**Gate 2B: OPEN.**


## 18. 2026-10-18 — NATIVE F-FIELD DISPLACED-CHART SAMPLING GREEN (LATEST)

**New files committed:** `numerics/hr_native_field_sampling.py` and `tests/test_hr_native_field_sampling.py`.

The native 14x14 interaction jet already varies the **f background** n(T),alpha(T) under deltaT, but it did not yet account for variation of the four independent **f-native perturbation fields** evaluated at displaced (T,R). The correct second-order chain rule has now been isolated without changing the original 14x14 Hessian:

- `q_f(T+deltaT,R+deltaR)=q_f+q_{f,T}deltaT+q_{f,R}deltaR+O(3)`;
- the native displacement obeys `deltaR=r deltaR_over_r`;
- the eight new field-gradient slots have exactly `H[deltaT,q_{f,T}]=dL/dq_f` and `H[deltaR_over_r,q_{f,R}]=r dL/dq_f`.

The local **22x22 interaction jet** preserves the original 14x14 principal block. The 8 new derivative slots are **not** independent physical scalar fields.

**Fresh reconstructed targeted run:**
`PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_native_field_sampling.py tests/test_hr_compact_radial_interaction.py`
=> **11 passed** (5 + 6). No full-worktree or GitHub Actions run.

**CURRENT EXACT RED:** promote the 22x22 time/radius sampling jet into the coherent compact spherical action. Crucially distinguish the f-native gradient `partial_R` from common `partial_r`; at `R=(1+mu(t))r` the moving radial profile itself contributes to `partial_T q_f`. Do not integrate this 22x22 object by treating its 8 rate/gradient coordinates as independent dynamical amplitudes.

After this projection: assemble full Einstein-Hilbert and two-dust canonical actions *before* metric Schur/BD reduction, then pass both mandatory mu->0 De Felice and homothetic Aoki oracles on one action. Test fold 1 only after that. The branch has **no** current physical kinetic/gradient or fold-crossing verdict.

**Resume order:** section 18 -> `research/COMPACT_RADIAL_HR_INTERACTION_AUDIT.md` (last addendum) -> the two new numerics modules/tests -> `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`.

`GATE_2B = OPEN`. Main stays unchanged; work on `research/gate2b-nonhomothetic-transfer`.


## 19. 2026-10-18 — beta4 full spacetime Ward verified (current head)

Read the root LATEST_RESTART.md **first** and research/BETA4_SPACETIME_WARD_AUDIT.md for full derivation and numerical controls. New Python sources/tests: numerics/hr_beta4_spacetime_ward.py, numerics/hr_beta4_native_jet_ward.py, tests/test_hr_beta4_spacetime_ward.py, tests/test_hr_beta4_native_jet_ward.py.

The finite-mu native interaction Hessian WITH f-field sampling obeys the beta4 f-volume Ward identity **after compact time and radial integration**, independently matched to a separate exact finite-amplitude coordinate transformation. The exact mixed terms cancel to order 1e-17 in the diagnostic; intentionally removing sampling leaves a nonzero residual. The f-native spatial trace contributes 3x the lapse coefficient; shift and traceless shear have zero linear native-volume source.

**27 targeted tests passed in the reconstructed local workspace using GitHub-hash-identical versions of the six relevant existing/new modules/tests.** This is not a clean full worktree or an Actions pass. An indexing bug introduced during extension to four f-native scalar channels caused four temporary RED tests and was corrected; this was a test harness issue.

**Physical scientific verdict unchanged: GATE_2B OPEN.** The beta4-only off-shell geometric Ward identity is NOT the final EH+HR+two-dust constrained action. Now implement that one complete action; pass finite-H mu->0 De Felice and homothetic nonlinear Aoki scalar oracles; only then consider fold 1. Keep main and v2-flrw untouched.

## 20. 2026-10-18 — finite-mu HR plus BOTH canonical dust phase pairs (NEWEST)

**First read:** `research/HR_TWO_DUST_PRECONSTRAINT_AUDIT.md`, then `numerics/hr_two_dust_preconstraint.py` and `tests/test_hr_two_dust_preconstraint.py`.

New **time-local spatial compact 22x22 partial-action Hessian** combines the validated 16-amplitude finite-mu native HR interaction with two independent canonical dust phase pairs `(Y_g,p_g)` and `(Y_f,p_f)`. The f phase includes the relative time chart variable `q_f=(Y_f-T)F`; all f-native phase gradients are pulled back by the full inverse non-homothetic Jacobian. The f dust momentum is kept dynamical: `H[p_f,Y_f_dot]=-H[p_f,T_dot]`. Both momentum/velocity pairs have rank 2.

**Two actual RED-to-GREEN findings:** (1) the initial new dust implementation doubled `4*pi` in the spherical measure; an independent canonical normalization test failed by precisely `4*pi`; fixed in BOTH sectors. (2) an initial test incorrectly expected the f phase-rate-square block to vanish. The inclined f-native foliation induces a nonzero negative coordinate rate-square from the *native spatial gradient*: `H[Y_f_dot,Y_f_dot]=-4*pi*n_f^3 alpha rho_f(1+mu)^2 int dr r^2 (sigma r)^2 F^2/D`; independently derived and verified, zero when sigma=0. It must not be incorrectly read as a physical ghost before EH/BD constraints.

**Verification:** 10 new targeted tests passed, 37 total tests passed in the reconstructed local workspace; both new file git blob hashes matched live GitHub (see audit). NOT a clean entire repository suite, NOT a physical propagation/fold conclusion.

**LATEST EXACT RED:** include complete native Einstein-Hilbert contributions on THE SAME spacetime compact profiles and common/f-native chart, check tadpoles/IBP and the four metric constraints, then reduce the time-dependent BD null coordinate while retaining both canonical dust pairs. Pass BOTH finite-H mu->0 De Felice and nonlinear homothetic Aoki `K_S,c_S^2` acceptance oracles on this **one** physical action. Fold 1 remains out of scope until both pass.

**Scientific verdict:** `HR_TWO_DUST_PRECONSTRAINT=GREEN_AS_PARTIAL_ACTION`; `GATE_2B=OPEN`. Do not assert JANUS validation. Main and v2-flrw remain untouched.


## 21. 2026-10-18 — native-flat Einstein-Hilbert interface (CURRENT)

**START HERE:** research/FLAT_EH_HR_TWO_DUST_BRIDGE_AUDIT.md; numerics/hr_flat_eh_two_dust_bridge.py; tests/test_hr_flat_eh_two_dust_bridge.py.

A restricted 22-amplitude EH+HR+two-dust partial Hessian now includes BOTH positive Einstein–Hilbert native lapse/radial-shift ADM blocks evaluated on the same regular compact radial profile as finite-mu HR and two independently preserved dust canonical pairs. The f-native shift radial derivative uses the full inverse chart, producing a B_f-B_f_dot mixed term when the background f-time foliation is tilted. At static g background, the flat ADM shift quadratic integrates to an exact radial boundary.

**ACTUAL local targeted tests:** 10 new tests passed; 47 total tests passed in a reconstructed workspace. Both new source/test files are byte-identical to the exact live GitHub blobs. Independent finite-difference controls required refining a too-large amplitude step 2e-4 to 2e-5; see audit. No full worktree suite or GitHub Actions run.

**CRITICAL LIMIT:** EH spatial traces/shears (psi_g, E_g, psi_f, E_f) and EH relative-chart perturbation columns are MISSING. Thus this is NOT a full EH+HR+dust action; its restricted lapse-shift 4x4 rank 4 does NOT validate the full metric constraints or BD elimination. The background is an off-shell Taylor control, not the on-shell Candidate-C cosmological solution. No ghost/gradient/fold conclusion.

**NEXT EXACT RED:** construct the full native scalar Einstein–Hilbert trace/shear and time/radial chart-variation terms on a single compact spacetime support; test EH diffeomorphism Ward identity, on-shell dust/background tadpoles, metric auxiliary and time-dependent BD-null reductions preserving both phase pairs. Then require both independent physical oracles: finite-H mu->0 De Felice and homothetic nonlinear Aoki K_S,c_S^2. Only then inspect fold 1 a≈0.0301646.

**Gate 2B OPEN. Main/v2-flrw untouched.**


## 22. 2026-10-18 — full native scalar ADM EH on untilted constant-mu chart (LATEST)

**Immediate first read:** root LATEST_RESTART.md then research/FULL_NATIVE_SCALAR_EH_UNTILTED_AUDIT.md.

New files: numerics/hr_full_scalar_eh_homothetic.py, tests/test_hr_full_scalar_eh_homothetic.py, numerics/hr_full_scalar_eh_two_dust_untilted.py and tests/test_hr_full_scalar_eh_two_dust_untilted.py. The exact six-amplitude native spherical ADM Hessian now includes both spatial scalar trace and traceless shear, intrinsic 3-curvature and all native extrinsic curvature derivatives. Both native sectors integrated in a common compact spatial chart T=t, Rf=(1+mu)r, mu constant. The result adds TWO g-native trace/shear rate slots to the previous 22-field HR+two-dust partial action; f rate slots reused.

**CRITICAL cross-action RED corrected:** f-native E potential and E_dot MUST rescale with (1+mu)^2 under native radial coordinate rescaling, while f shift rescales with (1+mu). Initial f-EH internal coordinate invariance by itself failed to catch the mismatch; an explicit native HR physical metric-shear matching test found it. Both columns were corrected and the radial/angular matching test is now GREEN.

Actual **fresh focused workspace**: 13/13 passed, comprising 11 direct native EH geometry tests and 2 MOCK-backed wrapper/strict-domain tests. Do NOT report the real full EH+HR+dust integration as exercised in this new workspace; no clean full-branch test exists. Prior 47 targeted results belong to the previous reconstructed workspace and were not rerun this session. All four new source/test git blob hashes verified exactly against live GitHub. See audit for hashes.

**Exact next RED:** run complete 24-slot composed EH+real HR+real dust on one verified workspace, then extend the full native EH tensor to sigma != 0, mu_dot != 0 with coherent background+perturbation chart transport, boundary terms and diffeo Ward; impose on-shell Candidate-C and both dust background evolutions; then metric/BD constraints and the De Felice/Aoki independent physical limits before fold 1.

Scientific status: FULL_NATIVE_SCALAR_EH_UNTILTED_GREEN, GATE2B_OPEN, JANUS_R_COSMOLOGY_NOT_VALIDATED.

### Pending real HR+two-dust native EH provider test

**NEXT UNEXECUTED FULL-PROVIDER TEST:** tests/test_hr_full_scalar_eh_two_dust_real.py has now been committed. It imports the REAL hr_two_dust_preconstraint module and the new native scalar EH assembly and checks 24x24 block addition, both canonical dust momentum-rate entries, the two new g trace/shear rate channels and positive f Planck scaling. Its exact GitHub blob SHA is 3ecbf81ea429d5475e902cde2b24fd7441204126. This test has been syntax-compiled locally, but NOT executed because the full prerequisite GitHub worktree cannot be cloned in this environment; do not count it among the 13 passed tests. **Immediate resume action: reconstruct/fetch all real provider modules, RUN this test, fix any actual failure, and record full evidence before extending the chart.**


## 23. 2026-10-18 — REAL EH+HR+TWO-DUST PROVIDER RUN AND f-EH FLRW WARD (LATEST)

**Authoritative restart:** root `LATEST_RESTART.md` (step 23); full audit `research/REAL_PROVIDER_AND_EH_WARD_AUDIT_2026_10_18.md`.

The formerly pending tests in `tests/test_hr_full_scalar_eh_two_dust_real.py` have now been **EXECUTED**, and pass without mock providers, using the real HR Hessian algorithm and both dust canonical phase sectors. Two extra real-provider tests confirm quadrature convergence and the m²=0 EH+dust limit. The combined untilted 24x24 action retains rank-two dust canonical momentum-rate coupling. This is still time-local and **OFF SHELL**.

New files `numerics/hr_eh_spacetime_ward.py`, `tests/test_hr_eh_spacetime_ward.py`: independent f-native FLRW lapse Einstein–Hilbert compact spacetime Ward gate. Background T=t+sigma(t)r²/2 and R=(1+mu(t))r, both with time dependence. Full native-lapse sampling in the compact chart gives mixed variation at ~1e-18; freezing sampling fails by ~3.22e-4 and ~2.78e-5. The native ADM action density also matches the existing repository `spherical_flat_adm_eh.py` primitive exactly. This is NOT the full spherical trace/shear EH Ward.

**Actually executed:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests` => **24 passed** in focused local `/mnt/data/janus-next`: 11 direct EH, 2 mock-backed structure, 4 real provider, 7 new Ward. Existing HR/dust providers were reauthored from GitHub source, preserving algorithms but NOT byte-identical file blobs; new Ward files/test and real-provider tests are exact GitHub hashes. Do not advertise full checkout, full regression, or physical acceptance.

**Next strict RED:** full f scalar EH chart time/radius perturbations, spatial trace/shear, native sampling and compact time integration; full EH Ward; on-shell Candidate-C with two dust phases and tadpoles; metric and BD time-dependent null reduction; both De Felice/Aoki physical oracles on SAME action, then fold. Main/v2-flrw untouched. `GATE_2B=OPEN`.

## 24. 2026-10-18 — full f-native spherical scalar EH chart Ward (LATEST)

**Authoritative restart:** root `LATEST_RESTART.md` (step 24), `research/FULL_SCALAR_EH_CHART_WARD_STEP24_AUDIT.md`. New `numerics/hr_eh_full_scalar_chart_ward.py`, `tests/test_hr_eh_full_scalar_chart_ward.py`, `scripts/verify_gate2b_step24.py`.

An independent exact **nonlinear native spherical ADM+GHY density** now includes all four f-native metric scalar perturbation fields Phi, U, psi, E, with their native spatial first/second and temporal derivatives, positive native Planck sign and regular center. Its spacetime integral is pulled back through an inclined, nonhomothetic (T,R)(t,r) chart including full Jacobian and compact time/radius chart variations. Eight mixed Ward derivatives vanish at <=3.25e-12; freezing native field sampling intentionally breaks all eight channels (minimum residual ~1.10e-5). The simultaneous four-field finite chart deformation changes the integrated native action by ~1.73e-18.

**Independent physical-formula regression:** a six-field finite-difference Hessian of the new nonlinear ADM density agrees with the previously implemented analytic native scalar EH six-field Hessian, and the flat-lapse/shift special case agrees with the independent old ADM primitive. This reduces self-reference risk; the chart integral remains a kinematic identity, not the constrained physics.

**Actual local tests:** 32 passed in reconstructed /mnt/data/janus-next; 8 new, 24 previous focused tests. The Step24 runner also returned exit 0 / 32 passed, emitted source digests and explicitly marked NON_GIT_WORKSPACE_RECONSTRUCTION, full_repository_regression=false, Gate2B=OPEN, both physical oracles NOT_RUN. The three new file Git blob hashes matched GitHub exactly. Existing HR/dust prerequisites reconstructed preserving algorithms, not byte-identical/full clone; Actions disabled and git clone DNS blocked.

**NEXT RED:** full EH chart variation *quadratic action with deltaT/deltaR* in common/native shared compact time basis, with both f metric spatial modes and derivatives, then on-shell Candidate-C background with BOTH dust conservation/tadpole cancellation, four metric auxiliaries and time-dependent BD-null reduction, same-action finite-H mu->0 De Felice and nonlinear Aoki K_S,c_S², only then first fold a≈0.0301646. No physical stability/CMB validation from Ward identity.

**GATE_2B=OPEN; JANUS-R NOT VALIDATED.** Keep main/v2-flrw unchanged.

## 25. 2026-10-18 — isolated full f Einstein–Hilbert spacetime CHART QUADRATIC (LATEST)

**Read first:** root LATEST_RESTART.md; research/EH_CHART_QUADRATIC_STEP25_AUDIT.md. Files numerics/hr_eh_full_scalar_quadratic_chart.py, tests/test_hr_eh_full_scalar_quadratic_chart.py, scripts/verify_gate2b_step25.py.

The exact nonlinear native spherical ADM+GHY Einstein–Hilbert action was differentiated to second order after time/radial compact integration on six independent amplitudes: (deltaT,deltaR,Phi_f,U_f,psi_f,E_f). With all four f native fields AND their derivative jets sampled at moved (T,R), the 2×6 chart Hessian rows vanish to max ~8.7e-13, while the native metric 4×4 block has Frobenius norm ~11.09 and is invariant under finite chart changes to ~4.63e-12. The proof uses the Piola total-divergence identity: this is an isolated f-EH coordinate-change/boundary gate, NOT physical constraint reduction. Frozen-native-sampling negative control produces mixed chart/field residual up to ~0.312.

Crucially a separately computed beta1–beta3 HR interaction-only compact radial test has a nonzero relative chart block (~0.22018 Frobenius norm) and metric/chart cross (~0.51215). Its trial basis and spatial-only integration differ; numerical magnitudes are NOT physically comparable. This confirms that pure f-EH diffeomorphism redundancy must not be conflated with HR relative chart dynamics.

**Actual local focused run** in /mnt/data/janus-next: 41 pytest tests passed, including nine new; step25 runner produced exit 0 / 41 passed / NON_GIT_WORKSPACE_RECONSTRUCTION / full_repository_regression false / DeFelice+Aoki NOT_RUN. Three new source/test/runner files EXACT git SHA match; previous HR/dust prerequisites are manually reconstructed algorithms, not a complete clone.

**NEXT STRICT RED:** one common time-supported and on-shell EH+HR+two-dust action with all field derivative transports and boundary terms; dust conservation/tadpoles; four metric auxiliaries and time-dependent BD-null reduction retaining both dust phase pairs; same-action De Felice finite-H mu→0 and Aoki nonlinear homothetic K_S,c_S²; only then Candidate-C fold near a≈0.0301646.

**GATE_2B OPEN; JANUS-R NOT VALIDATED; main and v2-flrw untouched.**

## 26. 2026-10-18 — full coupled beta0..beta4 diagonal/relative Hassan–Rosen Ward (LATEST)

**Authoritative restart:** root `LATEST_RESTART.md` (step 26); `research/COUPLED_DIAGONAL_NOETHER_STEP26_AUDIT.md`; `scripts/verify_gate2b_step26.py`.

NEW exact nonlinear spacetime-integrated bimetric Hassan–Rosen action with independent regular scalar perturbations Phi/U/psi/E of BOTH g and f, correct spherical angular areas and exact f nonhomothetic time/radial background chart. A common diagonal coordinate change of BOTH metrics leaves the entire all-beta interaction invariant to machine precision; a relative native f chart displacement creates nonzero beta1/2/3 variations, while beta0 g-volume and beta4 f-volume decouple. The new direct potential density matches the older independent exact native HR Stueckelberg jet at three radii (r=.23: -0.0823859285303577 each).

Critical NEW negative test uncovered a common-native coordinate-variation mixup: delta(T,R) and delta(t,r) are connected by the background inverse/Jacobian, not interchangeable amplitude profiles. Corrected before committing tests. The new 4x4 independent g/f chart Hessian shows an **OFF-SHELL Noether caveat**: exact finite diagonal action invariance and diagonal directional quadratic zero do NOT imply H*v_diagonal=0 for an arbitrary off-shell Hessian when gauge generators depend nonlinearly on fields and tadpoles are nonzero. Direct finite difference truncation decreases O(step²). Do not invent an early BD eigenmode or physical ghost/stability verdict.

**Actually tested locally:** 57 focused tests pass, 16 new, manifest runner exit 0 and marks NON_GIT_WORKSPACE_RECONSTRUCTION, full_repository_regression=false, DeFelice/Aoki NOT_RUN. All five newly committed program/test/runner Git blobs match the executed source byte for byte; older local HR/dust prerequisites are algorithmic reconstructions rather than a full repository checkout. Clean clone still DNS-blocked, Actions disabled; no external validation.

**NEXT RED:** same-profile time-dependent EH_g+EH_f+HR+TWO dust canonical phase-pair action; impose Candidate-C ON-SHELL and separate dust conservation/tadpoles, then actual auxiliary/BD time-dependent constraint elimination retaining BOTH dust pairs; pass finite-H mu->0 De Felice and nonlinear homothetic Aoki K_S,c_S² on the SAME action before fold 1. `GATE_2B=OPEN`, JANUS-R cosmology not validated.

## 27. 2026-10-18 — ONE native-consistent five-sector nonlinear spacetime action (LATEST)

**First read** root LATEST_RESTART.md (Step 27), then research/UNIFIED_FIVE_SECTOR_SPACETIME_STEP27_AUDIT.md. Executable sources: numerics/hr_unified_spacetime_offshell.py, numerics/hr_unified_dust_legendre.py. Tests: tests/test_hr_unified_spacetime_offshell.py and tests/test_hr_unified_dust_legendre.py. Reproducibility: scripts/verify_gate2b_step27.py.

Prior steps tested EH_f, HR, and matter on nonidentical or time-frozen bases. **Now a single nonlinear off-shell compact time/radius action explicitly integrates five pieces evaluated on the SAME two native spherical metrics:** EH_g (+), EH_f (+), all beta0..4 HR interaction, pressureless irrotational covariant dust_g and dust_f. The two dust backgrounds satisfy separate native continuity rho a^3=constant and theta_T=n in the zero-perturbation sector. An independent dust Legendre transform gives two separate positive momentum/phase canonical pairs in each NATIVE chart. This is NOT the full physical common-time canonical constraint reduction; no on-shell metric equations are imposed.

All five action integrals obey the finite **diagonal** compact chart Ward identity. Under finite f-only relative chart shift (+.035,-.023), four isolated EH/dust actions remain invariant and HR alone changes -1.00718622362e-5 in the illustrative dimensionless control. HR contribution equals the older independent Step26 full HR integral with interaction mass²=0.7. Both native flat ADM lapse/shift subsectors agree with the old independent EH primitive, and f/g metric tensors are the SAME for all sources.

**Local focused verification: 75 passed, 18 NEW.** The exact new source/test/runner/audit contents were pushed from staged copies of actual executed local files and their git hashes matched live GitHub blobs. Runner exit 0/75 passed, origin NON_GIT_WORKSPACE_RECONSTRUCTION, full_repository_regression=false, DeFelice+Aoki NOT_RUN. Older local HR/dust prerequisites still not guaranteed byte-identical; no clean full Git checkout, actions or independent peer reproduction. **GATE2B OPEN**.

**NEXT EXACT RED:** on-shell Candidate-C bimetric+dust background/tadpoles; translate new covariant matter clock/multiplier to exact common-time two-dust canonical phase pairs, form same time-supported physical scalar quadratic action, impose metric auxiliaries/BD-null canonical reduction, pass SAME-ACTION De Felice finite-H mu→0 and nonlinear Aoki KS,cS² oracles (both roots) before Candidate-C first fold. No ghost/fold/CMB validation claimed.


## 28. 2026-10-18 — genuine Candidate-C dust-only HOMOGENEOUS on-shell Routhian and temporal tadpoles (LATEST)

**FIRST READ:** root `LATEST_RESTART.md` (step 28) and `research/MINISUPERSPACE_ONSHELL_STEP28_AUDIT.md`. Code `numerics/hr_minisuperspace_onshell.py`; tests `tests/test_hr_minisuperspace_onshell.py`; `scripts/verify_gate2b_step28.py` (17 independent new tests).

The prior unified FIVE-sector Step27 compact spacetime trial action was OFF SHELL. Step28 derives the exact homogeneous FRW positive-EH g+f, full all-beta HR, TWO fixed-charge dust Routhian on ONE physical homogeneous set of scale factors/lapses. Crucial point: the covariant dust on-shell Lagrangian vanishes, but its PARTIAL lapse derivative does not; eliminating the dust clock before variation destroys Friedmann dust sources. Correct canonical Routh reduction yields independent -Ng Cg -Nf Cf and retains two matter canonical momenta.

Both lapse Friedmann constraints, both independent scale Euler equations, the dynamical Bianchi relation and both dust conservation laws satisfy strict on-shell tests on the **radiation-free Candidate-C dust variant only**, using implicit y_N,y_NN from the exact quartic. Re-solve present y0 after radiation removal: 0.5568825591873054; E(1)=0.9999551638376833. At a=1,.8,.4,.2,.09,.05,.03 max 5-component homogeneous residual ~5.4e-13. Independent finite differences of original ONE Routhian reproduce four Euler residuals.

**More important:** integrate the action in actual g cosmic time along a numerically solved Candidate-C homogeneous trajectory, with independent compact variations of (a,b,Ng,Nf). Four action-level temporal tadpoles vanish: at 26 points / width .025 / step 1e-6, approximately (-1.804e-10,+1.388e-11,0,-6.94e-12). Varying Nf by 2% or f conserved dust charge deliberately breaks f lapse constraint; wrong early dust on-shell substitution is an independent negative regression. A preliminary overlarge finite-difference h produced O(h²) error (10^-7/10^-8), corrected by numerical refinement, not a physical equation change.

**Earlier relative Stückelberg mu folds** at a~.0301646 and .0491246 occur in a separate nonlinear scalar equation. The background y(a) remains regular there but gives NO evidence of a physical helicity-0 fold crossing.

**Actually executed new tests:** 17/17 PASS in NEW standalone /mnt/data/janus28 (NOT the earlier 75 tests). Step28 JSON runner passed 17, origin `standalone_focused_workspace`, `full_repository_regression=false`, physical DeFelice and Aoki `NOT_RUN`, `GATE_2B OPEN`. Four new source/test/runner/audit files exactly match the executed local bytes and GitHub blobs. Earlier 75-step suite **not rerun here**, so DO NOT claim 92 combined tests in one run. No complete Git checkout or GitHub Actions run.

**NEXT EXACT RED:** insert this on-shell dust-only Candidate-C branch into the ACTUAL Step27 full nonhomothetic common-space-time action with correctly transformed f time/radius chart, dust phase clock variation and boundary terms; cancel all first variations; construct one dynamical quadratic scalar action, reduce metric auxiliary and time-dependent BD constraints retaining both dust pairs, reproduce SAME-ACTION De Felice mu→0 finite-H and homothetic nonlinear Aoki K_S,c_S², THEN approach fold. `GATE_2B=OPEN`, `JANUS_R_NOT_VALIDATED`.

## 29. 2026-10-18 — precise RED for naïve homogeneous-on-shell → relative finite-μ chart insertion (LATEST)

**Read first:** root `LATEST_RESTART.md` (Step29), `research/NONHOMOTHETIC_ONSHELL_INSERTION_STEP29_AUDIT.md`; code `numerics/hr_nonhomothetic_center_obstruction.py`, tests `tests/test_hr_nonhomothetic_center_obstruction.py`, runner `scripts/verify_gate2b_step29.py`.

Step28 proved the homogeneous radiation-free two-dust Candidate-C Routhian on-shell; Step27 integrated the full OFF-SHELL five-sector spacetime action. **The proposed naïve promotion is mathematically false:** at r→0, the f-native relative radial map R=(1+μ)r changes three g^{-1}f spatial square-root eigenvalues from y=b/a to λy=(1+μ)y, while the original native f scale is held fixed. This shifts the necessary g lapse/Friedmann source by exactly -m² Mg² a³[V_g(λy)-V_g(y)], with V_g=β0+3β1 y+3β2 y²+β3 y³. At a=.4, λ=.78, homogeneous lapse residual ≈0 becomes +0.160780603695; at a=.03 λ=.231117 the same naive source is +0.03919434. These are dimensionless necessary field-equation residuals, NOT measurements or physical fold stability diagnoses.

**Non-tautological checks:** derivative of the fully nonlinear pulled-back spherical HR 2x2 principal-square-root density with respect to the g lapse, normalized by r², agrees with the analytic center source as r→0 at five parameters. The finite compact radial g-EH+two canonical dust g charge+HR action first variation gives +3.20003248e-6 at a=.4, λ=.78, support radius=.035, matching independent radial bump normalization. Candidate y/Nf values independently reproduce the Step28 quartic/implicit Bianchi lapse. β4 decouples from g lapse, zero m² removes the relative interaction source. Restoring b_native=b_hom/λ for constant λ cancels the CENTER residual: this is **NOT a universal nonhomothetic no-go**. However native time tilt σ=.08 introduces spatial-slice component mismatch f_rr-f_θθ/r²=-n(T)²σ²r², and after center compensation a nonzero finite-radius lapse source remains for the tested f off-shell time jets. Need genuinely coupled radial/time background fields and dust charge/phase transport.

**Actually executed local:** 21 tests PASS in new /mnt/data/janus29 standalone workspace. Step29 manifest script also exit 0/21 passed/standalone_focused_workspace, source SHA-256, physics oracles NOT_RUN, GATE2B OPEN, full_repository_regression=false. All four new GitHub file blobs exactly match local executed/report bytes. The earlier 75 and 17 tests were NOT rerun here: NEVER claim 113 total passed together. Git clone DNS block and CI disabled; external full-worktree reproduction pending.

**NEXT RED:** chart-compensated f scale, separate f dust conservation and matter clock, f metric radial/time backreaction; compute ALL common 5-sector Euler/tadpole residuals across time+radius from one action. Only when they vanish derive coherent dynamical physical scalar quadratic action, time-dependent BD-null/metric constraints with both dust pairs, De Felice finite-H μ→0 and Aoki homothetic K_S,c_S² same-action oracles, THEN first relative μ fold at a≈0.0301646. `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`; research branch only.

## 30. 2026-10-18 — EXACT inverse f-chart compensation: coordinate baseline GREEN, no new physical branch (LATEST)

**Authoritative restart:** root `LATEST_RESTART.md` Step30; detailed `research/INVERSE_CHART_COMPENSATION_STEP30_AUDIT.md`. Code `numerics/hr_compensated_native_chart.py`; tests `tests/test_hr_compensated_native_chart.py`; one-command runner `scripts/verify_gate2b_step30.py`.

Step29 found a necessary g lapse equation obstruction when the on-shell dust-only homogeneous Candidate-C f native scale was inserted unchanged into `R=lambda(t)r`. Step30 derives the entire **inverse-coordinate transformed f-native metric** `f_native=J^{-T} f_hom J^{-1}`, angular area `b(t)²r²`, native dust phase gradient `(Nf,0)J^{-1}`, density `Cf/b³`, and native conserved current `Cf r² J^A_t/det J`. Nontrivial time tilt and lambda_dot induce nonzero f-native shift, native radial/angular anisotropy (coordinate component effect), and native dust radial phase/current: merely setting `b_native=b_hom/lambda` and forcing native f diagonal cannot represent the same physical metric at finite radius.

Both positive controls: (i) exactly recovered common metric tensor, native dust normalization -1 and current divergence ~5.4e-12, full HR beta0..4 density identical to physical homogeneous expression, and **nonzero off-shell covariant dust density** obeys exact scalar-Jacobian transformation; (ii) actual time+radial compact first variation of a shared g EH ADM+GHY+g canonical dust+nonlinear HR necessary g lapse sub-action cancels to ~1.30e-13 after full compensation. Deliberately restricted scale-only native diagonal ansatz gives point g lapse residual +3.116e-4 at a=.4,r=.2 and nonzero compact action variation +3.503e-8. The full-compensated native offdiag f_TR=+0.00480694489921799 at this point.

**CRITICAL logical distinction:** this is a **PASSIVE REPARAMETRIZATION** of the ALREADY on-shell homogeneous solution, not an independent relative-Stückelberg physical mode or an on-shell native FLRW nonlinear screened branch. Therefore it does not resolve the relative-mu folds, stability or cosmological data. The compensated geometry is a strict regression/Noether control baseline against which physical perturbations can later be separated.

**Actual local:** 18/18 targeted tests pass in fresh standalone `/mnt/data/janus30`. Step30 JSON runner marks non-git standalone workspace, prior Step29 not rerun, Gate2B OPEN, De Felice/Aoki NOT_RUN. FOUR new source/test/runner/audit files were uploaded as exact bytes from the executed workspace and GitHub blob hashes checked identical (listed in audit/root). Historical test suites 21 Step29 / 17 Step28 / 75 Step27 were NOT combined this session. Direct GitHub clone blocked by DNS, CI disabled.

**NEXT strict RED:** introduce physically independent f-native scalar/shift/shear AND matter clock deformations beyond exact coordinate compensation; construct all on-shell Einstein+HR+two-dust first variations in one common spacetime action, then full dynamic quadratic constraints/BD and two De Felice/Aoki physical acceptance limits, then relative-mu fold. `GATE_2B=OPEN`, JANUS-R NOT VALIDATED.

## 31. 2026-10-19 — same common time/radial five-sector physical metric action, 12 homogeneous-on-shell scalar/matter tadpoles (LATEST)

**Read FIRST:** root `LATEST_RESTART.md`, detailed `research/FULL_ONSHELL_TWELVE_FIELD_TADPOLES_STEP31_AUDIT.md`, program `numerics/hr_full_onshell_tadpole.py`, test `tests/test_hr_full_onshell_tadpole.py`, runner `scripts/verify_gate2b_step31.py`.

**New advancement over Step30:** evaluate actual 5-contribution nonlinear spherical spacetime action with positive EH_g+EH_f full 3-curvature/extrinsic scalar trace-shear, exact HR all-beta interaction, and both covariant irrotational dust clock + multiplier sources, on the **actual homogeneous dust-only Candidate-C on-shell** trajectory. Independently vary TWELVE common-chart compact-time-and-radius fields `(Phi_g,U_g,psi_g,E_g,theta_g,rho_g,Phi_f,U_f,psi_f,E_f,theta_f,rho_f)`. ALL 12 first variations vanish, maximum local measured |tadpole| = 1.4051260155e-11 with amplitude h=2e-5, quadrature 24 and support (T=.027,R=.32). Both EH/HR/matter sector contributions are *independently nonzero* and cancel; for Phi_g: EH_g +3.64871135e-4, HR -6.44695537e-5, dust_g -3.00401582e-4. For Phi_f: EH_f +1.29610824e-6, HR +2.01858490e-5, dust_f -2.14819573e-5. Independent dust phase/multiplier must be varied BEFORE norm constraint substitution. Tests run quadrature/step/domain refinements and a local two-dust Legendre check.

One physically independent f metric scalar trial perturbation (not Step30 passive f coordinate compensation) changes spatial curvature and relative angular metric ratio and yields genuine NONZERO UNREDUCED quadratic response. Mixed H[Phi_g,psi_f] ≈ -1.84236013e-4; this cross-metric entry vanishes after HR interaction mass is set zero, but then the baseline also fails the lapse tadpole due to missing interaction. Relative trial coupling IS NOT a physical scalar propagation/ghost verdict. Native chart consistency is checked by tensor inverse Jacobian including f shift, but the background itself is still PHYSICALLY HOMOGENEOUS; NO new finite-μ Stückelberg on-shell branch was constructed.

**Actually executed:** 29 new focused tests pass in NEW standalone /mnt/data/janus31. Manifest JSON exit 0/29 passed, stand-alone origin, full_repo_test_suite false, DeFelice/Aoki NOT_RUN, BD not reduced, Gate2B OPEN. FOUR new GitHub source/test/runner/audit files were verified exactly against the actual locally run source hashes. Historical Step30 18, Step29 21, Step28 17, Step27 75 suites were NOT run here; do NOT claim combined count. Git clone DNS blocked; CI disabled, external full-worktree reproduction pending.

**NEXT RED:** derive full common-time quadratic field/velocity Hessian, diagonal Noether/metric lapse-shift auxiliary and BD-null constraint with two *canonical* dust pairs on this same action; independently solve all Einstein/HR/two-matter PDE tadpoles for a truly nonhomothetic physical background beyond compensated chart; pass SAME-ACTION De Felice finite-H μ→0 and Aoki nonlinear homothetic KS,cS² benchmarks prior to first relative μ fold a≈.0301646. `GATE_2B_OPEN`, JANUS-R NOT VALIDATED.

## 32. 2026-10-19 — exact common-time two-dust ADM Legendre bridge and 14×14 UNREDUCED trial Hessian (LATEST)

**Start with** root `LATEST_RESTART.md`, `research/COMMON_TIME_TWO_DUST_CANONICAL_STEP32_AUDIT.md`, new `numerics/hr_two_dust_common_time_canonical.py`, `tests/test_hr_two_dust_common_time_canonical.py`, `scripts/verify_gate2b_step32.py`.

The Step31 full nonlinearly perturbed spherical positive EH_g/f + all-beta HR + two covariant dust on the **HOMOGENEOUS on-shell radiation-free Candidate-C** trajectory is transformed to an exact FIRST-ORDER common-time canonical action by Legendre transformation of both dust phases and positive momenta, with dust multiplier rho eliminated ONLY AFTER the Legendre transform. Exact original covariant/nonzero off-shell dust density equals `p theta_dot-H(rho)` under the independently calculated Legendre map in BOTH sectors. Stationary rho elimination gives `H=N p sqrt(1+theta_r²/g_rr)+N^r p theta_r`. This is affine in true ADM lapse and shift at fixed spatial geometry/phase/p, a necessary metric constraint-interface fact, NOT the full coupled BD constraint.

Actual **14×14 common-action preconstraint Hessian** contains TWO independent symplectic momentum/phase-rate entries `H[p_g,rate_g]=+9.450339095e-5`, `H[p_f,rate_f]=+1.303392697e-5`, off-diagonal ZERO, rank 2, verified against independent exact analytic time/radial integrals. Two independent phase-rate rows otherwise zero, momentum and rate pure Hessian entries zero. Twelve legal compact field first variations cancel to ~3.73e-12. Two extra local phase-time-rate jet amplitudes have NONZERO first derivatives: they are NOT globally admissible independent variations, and no false tadpole status claimed. HR cross-metric Hessian H[Phi_g,psi_f]≈-1.84236e-4 remains present. No time-independent metric trace/shear rates have yet been added as separate jets; **14×14 is NOT physical scalar kinetic/ghost/speed matrix**.

**ACTUAL combined run:** 49 focused tests PASS in ONE new local workspace /mnt/data/janus32 = 29 original byte-exact Step31 source/tests PLUS 20 new Step32 tests. JSON runner returns 49 passed, exit 0, origin incomplete Git checkout, BD/De Felice/Aoki NOT_RUN, Gate2B OPEN. Four new Step32 files exact Git blob SHA verified with live GitHub; earlier Step27–30 suites remain historical NOT included.

**NEXT hard RED:** add four independent metric spatial rate jets psi_dot_g,E_dot_g,psi_dot_f,E_dot_f into SAME common-time full action, then derive complete metric lapse/shift ADM auxiliaries and time-dependent BD-null canonical reduction preserving both dust pairs. Parallel genuinely nonhomothetic on-shell two-metric/two-matter solution STILL UNFOUND. BOTH De Felice finite-H μ→0 and Aoki homothetic nonlinear KS,cS² not tested. No fold physics. GATE_2B OPEN.
