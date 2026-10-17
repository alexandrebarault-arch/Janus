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
