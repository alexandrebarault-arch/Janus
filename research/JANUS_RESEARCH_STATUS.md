# JANUS research status and roadmap

Date: 2026-10-15
Active branch: `research/gate2b-nonhomothetic-transfer`
Status: **Gate 2B OPEN / NOT VALIDATED**

This file is the concise project-status page.  For interruption recovery, read this file first, then `research/GATE2B_LATEST_RESTART.md`, `research/GATE2B_CHECKPOINT.md`, and the active execution plan `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`.

## 1. Branch strategy

The repository currently contains three branches:

- `main` — stable historical baseline.  It is intentionally far behind the active research line and should remain untouched until a later consolidation/merge decision.
- `research/v2-flrw` — historical V2 research line.  It is **not redundant** with the current Gate-2B line: the branches have diverged substantially and this branch still contains a large body of V2/NR/initial-data experiments and documentation that are not all present on the current branch.
- `research/gate2b-nonhomothetic-transfer` — **the only active branch for the present Gate-2B scalar-transfer research**.

Recommended policy now:

1. work only on `research/gate2b-nonhomothetic-transfer`;
2. keep `main` as the stable baseline;
3. keep `research/v2-flrw` frozen as an archive/reference until Gate 2B reaches a scientific verdict and any unique material has been reviewed/cherry-picked or explicitly archived;
4. do **not** actively maintain three parallel lines and do not delete `research/v2-flrw` yet.

A future cleanup can reduce the repository to two branches after Gate 2B closes: stable `main` plus one consolidated research/history branch.

## 2. Executive scientific status

The original question was whether a mathematically healthy bimetric continuation could retain useful JANUS-like cross-sector behavior and produce a significant relative/segregation mode without inserting arbitrary late initial conditions.

At the current stage, the old scalar-action reconstruction problem is essentially closed.  The main unresolved question has been narrowed to one specific nonlinear transition:

> Can the dynamical helicity-0 scalar pass regularly from the early screened nonlinear branch through the non-homothetic fold region and determine the two canonical late matching data?

Until that question is answered, no unique late transfer matrix or final Gate-2B verdict is justified.

Approximate progress estimate for Gate 2B: **about 80% of the conceptual/technical program is complete**, but the remaining part contains the hardest discriminating calculation.

## 3. Major results already closed

### 3.1 Scalar action and degree count

Closed or independently audited:

- JANUS/Comelli to De Felice/Hassan-Rosen convention bridge;
- De Felice Einstein-Hilbert scalar action;
- P(X) matter action;
- exact quadratic Hassan-Rosen interaction sector;
- Eq. (72) physical-basis transformation;
- correct scalar degree count and BD null direction;
- preservation of the GR scalar degeneracy.

The historical Comelli scalar closure was rejected as a physical transfer closure because it projected out the physical helicity-0 high-k gradient even though it was algebraically/Bianchi consistent.

### 3.2 DF5e.4 / DF5e.5 kinetic and dispersion repair

The spurious `NG3 ~ k^2` behavior was traced to an inconsistent time derivative of the BD mixed column: the f-pressure trajectory contribution to `dot C` was omitted.

The time-dependent canonicalization restores the required

`M_iZ -> M_iZ - (dot c_i + 3 H c_i)`

terms and associated rate-block integration by parts.

With a locally on-shell regulated trajectory, the full De Felice Eq. (85) reconstruction recovers the Case-C gravity principal speed

`c_s,grav^2 = -0.6665833422935964`

against the independent target

`-0.6665833419871022`,

with relative disagreement of order `4.6e-10`.

### 3.3 Candidate-C principal scalar

On the exact Candidate-C-like dust+dust benchmark, the same action/reduction gives at `a=0.5`

`c_s,grav^2 = 0.6920714772308268`

against the independent target

`0.6920714772884699`,

with relative disagreement of order `8e-11`.

This establishes that the repaired scalar action is not a special Case-C fix.

### 3.4 Exact-dust late-time system

A regular dust limit has been built using canonical matter momenta rather than an artificial finite sound speed.

Important structural result:

- the exact dust reduction is first order;
- the two dust momenta are genuine canonical phase variables, not ordinary auxiliaries;
- the physical late scalar phase space is six-dimensional.

The late principal scalar becomes healthy only near

`a ~= 0.10165`, `z ~= 8.84`

for the production range `k = 0.05...0.2 h/Mpc`.

The older `m_eff/H = 1` surface at `z ~= 16.26` is therefore not a healthy linear matching surface.

### 3.5 Late matching ambiguity

Even on a healthy late surface, the four natural adiabatic conditions

- `delta_common = 1`;
- `delta_relative = 0`;
- `delta_common,N = 1`;
- `delta_relative,N = 0`

fix only four combinations in the six-dimensional scalar phase space.

Two independent helicity-0 phase-space data remain free.  The historical choice

`Y3 = 0`, `Y3_N = 0`

is only a convention, not a derived matching law.

Therefore earlier large provisional values of `R = delta_relative/delta_common` are **not physical predictions** and must not be promoted to `T_gg,T_gf,T_fg,T_ff`.

## 4. Nonlinear non-homothetic transition results

### 4.1 Exact spherical Stückelberg pullback

An exact spherical Hassan-Rosen pullback was constructed on the actual non-homothetic FLRW background.

For

`T = t + s(t) r^2/2`,
`R = (1+mu(t)) r`,

the temporal interaction equation gives

`s = -(a^2/c) [ dot(mu) + H mu(c+1+mu) ]`.

In the homothetic limit `c=1`, this reproduces the Aoki-Maeda-Namba relation.

The leading non-homothetic radial branch was derived directly rather than by the old instantaneous substitution `K -> xi(a)`.

### 4.2 Weak metric constraints and finite corrections

The weak interaction sources were reconstructed from the Hassan-Rosen `Y_(n)` tensors and reproduce the homothetic Aoki weak-metric source equations.

A key normalization result is closed:

- static weak metric sources are controlled by `D = xi J`;
- the propagation coefficient `Gamma` is not the correct static source normalization.

The exact-pullback finite weak-metric residual was calibrated against the full homothetic Aoki finite equation using targeted x64 automatic differentiation as an audit oracle.

### 4.3 Two nonlinear folds

On strict Candidate-C dust, the regular nonlinear pair has two conditioned folds:

First fold — disappearance:

`a_1 ~= 0.0301646`,
`z_1 ~= 32.151`,
`mu_1 ~= -0.768883`.

Second fold — reappearance:

`a_2 ~= 0.0491246`,
`z_2 ~= 19.356`,
`mu_2 ~= -0.67015`.

Between them, the regular adiabatic pair is absent.  A separate near-singular branch close to `mu=-1` survives, but its physical viability has not been established.

The weak metric potentials remain small on the intended Fourier scales, so the disappearance is not explained by a simple blow-up of the weak-field amplitudes.

### 4.4 New homogeneous kinetic warning

A deliberately limited homogeneous velocity-Hessian diagnostic has been calibrated against the Aoki nonlinear dust kinetic coefficient `K_S`.

On admissible positive-interaction-normalization controls, a broad scratch scan gave `27/27` sign agreement.  The repository regression includes positive and negative `K_S` controls and verifies numerical stability.

Applied to the positive-sign Candidate-C early regular branch, the homogeneous kinetic signature crosses zero near

`a_K ~= 0.030136993`,
`z_K ~= 32.18181`,
`mu_K ~= -0.76624`.

This lies only about `9.2e-4` relative in scale factor from the independently obtained first fold.

This is a strong warning of possible kinetic degeneracy/strong coupling, but **not yet a no-go theorem**, because the full finite-`m_eff/H` weak Einstein constraints have not been eliminated in the oscillation action and the full gradient coefficient is not yet known.

A separate homothetic counterexample confirms that an algebraic fold does not generically imply `K_S=0`; the Candidate-C near-coincidence is therefore not a tautology.

## 5. Current hard blocker

The next required object is the **spatially dependent six-field quadratic oscillation system** around the nonlinear branch.

Before reduction retain an equivalent set to

`(phi_g, psi_g, phi_f, psi_f, delta_eta, delta_r)`.

The four weak metric constraints and the nondynamical Stückelberg combination must be eliminated before reading kinetic or gradient characteristics.

Shortcuts already ruled out:

- raw two-field Stückelberg principal symbol before constraint reduction;
- finite-ball gradient Hessians dominated by boundary/constraint terms;
- arbitrary compact profiles whose derivatives violate the Aoki epsilon counting;
- forcing an algebraic branch jump across the fold gap;
- tuning the two late variables `(Y3,Y3_N)`.

## 6. Next steps — ordered acceptance gates

### Step A — homothetic six-field Aoki oracle

Construct and reduce the six-field quadratic action in the homothetic `H >> m_eff` limit.

Acceptance requires recovery of Aoki's one-field oscillation action, including:

- one physical scalar field after constraints;
- correct `K_S` sign and normalization up to one global positive action convention;
- correct `c_S^2`;
- stable and unstable nonlinear-root controls;
- the separate `mu=0` branch.

Do not proceed to Candidate C until this is GREEN.

### Step B — finite-mass homothetic control

Retain finite `m_eff/H` and verify that the zero-frequency/static sector stays consistent with the already recovered full Aoki `C_H^2 + C_m^2 = 0` roots.

This links the dynamical action to the finite weak-metric fold machinery.

### Step C — non-homothetic promotion

Promote the pre-reduction coefficients to the actual on-shell functions

`xi(N), c(N), H(N), xi_N, c_N`.

No instantaneous substitution into a final homothetic formula is accepted.

### Step D — linear De Felice oracle

Take `mu -> 0` on Candidate C.

The same reduced system must recover the independently validated De Felice/Hassan-Rosen linear principal scalar.  If it fails, the nonlinear normalization/reduction is wrong and the fold must not be interpreted.

### Step E — first-fold dynamical kinetic/gradient test

Evaluate the fully reduced kinetic and gradient operators along the regular early branch approaching

`a_1 ~= 0.0301646`.

Determine whether the homogeneous zero near `a_K ~= 0.030137` survives after all constraints are included.

This is currently the most discriminating scientific test.

### Step F — transition integration

Only if the fully reduced kinetic operator remains finite and positive should a dynamical crossing be integrated.

A viable continuous trajectory must maintain:

- real HR square root;
- `mu > -1`;
- nonsingular constraint matrix;
- positive/nonzero kinetic coefficient;
- acceptable gradient coefficient;
- finite `dmu/dN` and canonical momentum;
- continuous connection to the validated late linear helicity-0 pair.

### Step G — derive late matching data

If a healthy trajectory exists, project it onto the late variables and determine

`(Y3,Y3_N)`

on a principal-stable late surface.

Then, and only then, rerun the late fundamental transfer calculation and compute meaningful

`T_gg, T_gf, T_fg, T_ff`.

### Step H — physical three-fluid extension and final Gate-2B verdict

If the dust+dust path survives, add visible radiation explicitly and repeat the required transfer checks over multiple production `k` values.

Then run a complete repository regression suite in a real worktree and issue the final Gate-2B scientific verdict.

## 7. How much work remains?

A practical estimate is **five major scientific blocks** remaining:

1. six-field Aoki reduction;
2. linear De Felice cross-check;
3. finite-mass fold/kinetic/gradient verdict;
4. transition integration and extraction of `(Y3,Y3_N)` if viable;
5. late transfer + radiation + final validation.

A negative result can arrive earlier: if the fully reduced system develops an unavoidable ghost, kinetic zero, singular constraint system or non-crossable `mu=-1` barrier near the first fold, Candidate C can fail Gate 2B without completing all later transfer steps.

A positive result requires substantially more work because the transition must then be integrated, matched and propagated through the late linear system.

## 8. Current scientific ruling

- `LINEAR_SCALAR_ACTION_RECONSTRUCTION = CLOSED`.
- `CASE_C_FULL_SCALAR_DISPERSION = CLOSED`.
- `CANDIDATE_C_DUST_PRINCIPAL_SCALAR = CLOSED`.
- `STRICT_DUST_LATE_SYSTEM = BUILT`.
- `LATE_TRANSFER_UNIQUE_FROM_FOUR_ADIABATIC_CONDITIONS = NO`.
- `OLD_m_eff/H=1_MATCHING_SURFACE_HEALTHY = NO`.
- `EXACT_NONHOMOTHETIC_STUECKELBERG_KINEMATICS = DERIVED`.
- `FINITE_WEAK_METRIC_REGULAR_PAIR_CONTINUOUS = NO` over roughly `32.15 > z > 19.36`.
- `NEAR_SINGULAR_BRANCH_PHYSICALLY_VIABLE = NOT ESTABLISHED`.
- `HOMOGENEOUS_KINETIC_ZERO_NEAR_FOLD_1 = STRONGLY INDICATED`.
- `FULL_DYNAMICAL_KINETIC_NO_GO = NOT YET ESTABLISHED`.
- `MISSING_LATE_MATCHING_DATA_DERIVED = NO`.
- `GATE_2B = OPEN`.

## 9. Verification limitation

The environment still cannot clone the repository from GitHub and GitHub Actions/workflows remain disabled.  Important identities and local regressions have been executed in targeted reconstructed workspaces, and the fold/auto-diff audits have undergone conditioning scans.

This is **not** a claim that the complete repository test suite is globally GREEN.  A full clean worktree regression remains mandatory before the final Gate-2B verdict.

## 10. Immediate restart instruction

Execute `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`.

First GREEN target: recover Aoki `K_S` and `c_S^2` from the fully reduced homothetic six-field system.

Second GREEN target: recover the Candidate-C De Felice linear principal scalar in the `mu -> 0` limit.

Do not tune late matching variables and do not force an algebraic branch switch through the fold interval.

## Addendum — 2026-10-17: native finite-mu HR interaction jet

The active branch now includes `numerics/hr_native_quadratic_jet.py`,
`tests/test_hr_native_quadratic_jet.py` and the detailed
`research/NONHOMOTHETIC_HR_JET_AUDIT.md`.

This independently tested exact second-order interaction-jet construction
extends the **native metric portion** of the HR Hessian to finite nonlinear
`mu`. Its central `mu=0` limit reproduces all eight De Felice Eq. (45)-(46)
scalar potential directions (including lapse, shift, trace and shear); a
separate JAX Hessian confirms finite-mu/nonzero-radius coefficients. Targeted
verification was **10 passed** in a reconstructed workspace.

This is **not yet** the full finite-mu cosmological scalar action: the
oscillatory Stückelberg map variables, `n(T),alpha(T)` background drift,
space/time profile integration and the EH/dust constrained reduction remain
open. The pointwise `r>0` interaction Hessian contains radial-parity/phase
terms which cannot be used directly as a Fourier transfer matrix.

**Current RAF:** promote the native HR interaction Hessian to the entire
pre-metric `(Y1,Y2,L,T,p_g,p_f)` augmented action at finite `mu`, retaining
its time-dependent on-shell and compact-support structure. Pass the
`mu->0` Candidate-C De Felice limit and homothetic Aoki nonlinear
`K_S,c_S^2` limits before evaluating the first fold.

**Gate 2B: OPEN; no unique late transfer or validated fold-crossing verdict.**

## Addendum — 2026-10-17 (suite): 14x14 HR Stueckelberg + profil regulier

The earlier 8x8 metric-only finite-mu HR interaction jet is now extended
to a **14x14 interaction-only Hessian** with six independent local chart
derivative/angular jets. A regular spherical trial profile imposes the
actual kinematic constraints between these six local jets and four
amplitudes `(T,L,Tdot,Ldot)` through a 14x12 pullback. This produces
a local 12x12 interaction-only block before the metric constraints.

Files:
- `numerics/hr_native_stueckelberg_jet.py`;
- `numerics/hr_stueckelberg_profile_pullback.py`;
- their corresponding tests;
- `research/NONHOMOTHETIC_HR_JET_AUDIT.md`.

**Targeted reconstructed verification: 24 passed**, including independent
JAX x64 Hessian controls and central De Felice quadratic interaction tests.
These are not full-worktree test results.

**Still unresolved:** the coherent on-shell, space/time integrated nonlinear
action with native perturbation-field drift, EH gravity and two dust phase
pairs; its four metric constraints and time-dependent BD reduction; both
physical Aoki/De Felice acceptance oracles *on one fully assembled action*;
and whether Candidate C can cross the first fold.

For exact next instructions read
`research/GATE2B_LATEST_RESTART.md` section 16.
**Gate 2B remains OPEN.**


## Addendum — 2026-10-18 (latest Gate 2B work)

**Scientific status remains OPEN.** The physical finite-mu constrained kinetic and gradient operators and a regular Candidate-C fold crossing have not been demonstrated.

Two new independent *interaction-only* geometry/chain-rule controls have been added:

- Compact regular radial action: `numerics/hr_compact_radial_interaction.py`, 12 amplitudes, correct spherical metric-shift/shear parity, explicit 4*pi*r² integral. Targeted 6 tests passed.
- Native f metric perturbation displaced-chart sampling: `numerics/hr_native_field_sampling.py`, extends 14x14 native jet to 22x22 algebraic matrix including 8 f-field time/radius derivative slots. Targeted 5 tests passed.

**Combined locally reconstructed regression: 11 passed**, not a full GitHub or repository suite. These new matrices are NOT the final physical Hessian after EH, two-dust phase terms, metric constraints and time-dependent BD null elimination. In particular, treating the derivative slots as independent physical modes would be an error.

**The single authoritative restart record is `research/GATE2B_LATEST_RESTART.md`, section 18.** The detailed scientific caveats and next mathematical step are in `research/COMPACT_RADIAL_HR_INTERACTION_AUDIT.md`.

Branch policy remains unchanged: active work only on `research/gate2b-nonhomothetic-transfer`, with `main` retained as a stable baseline and `research/v2-flrw` archived intact.


## Addendum 2026-10-18 — full compact beta4 Ward checked on exact GitHub sources

New **interaction-only**, two-route Ward acceptance gate is now GREEN, documented in research/BETA4_SPACETIME_WARD_AUDIT.md. The explicit full spacetime beta4 f-volume change-of-variables integral and the existing finite-mu 22x22 native HR interaction jet agree after compact time/radial integration, including perturbation-field transport. Removing sampling fails with nonzero mixed residuals, providing a discriminating negative control. Four f-native scalar directions were audited.

**27 local targeted tests passed** on an exact-hash-verified copy of six relevant GitHub modules/tests. The full repository suite has NOT been run, and no physical kinetic/gradient/fold verdict follows. No cosmological validation of JANUS-R or external JHR manuscript is claimed.

**Authoritative next checkpoint:** LATEST_RESTART.md at repository root. Full EH + TWO dust phase + HR action assembly remains the active RED step. Must pass both De Felice and Aoki physical limits on one constrained finite-mu action before evaluating the Candidate-C first fold.

## Addendum 2026-10-18 — time-local HR plus canonical two-dust preconstraint gate

The 22-variable compact spatial **partial** Hessian now includes both f/g dust canonical momentum-phase pairs and the existing sampled native HR interaction on the same radial basis. 10 new targeted tests passed, 37 total local reconstructed-workspace tests passed, exact new source blobs matched GitHub. It includes the corrected single 4*pi measure and the tilt-induced native f spatial-gradient time-rate square. Neither EH nor full metric/BD constraint reduction is included: **GATE_2B OPEN**. See research/HR_TWO_DUST_PRECONSTRAINT_AUDIT.md and root LATEST_RESTART.md.

## Addendum 2026-10-18 — flat native EH/HR/two-dust interface

Both native flat-spatial EH ADM lapse/shift Hessians integrated on the same non-homothetic f background chart and compact radius with HR plus two dust phase pairs. 10 new targeted tests passed; 47 tests in local reconstructed suite. Full scalar EH and chart variation NOT included; no constrained physical mode result. See root LATEST_RESTART.md and research/FLAT_EH_HR_TWO_DUST_BRIDGE_AUDIT.md. GATE_2B=OPEN.

## Addendum 2026-10-18 — full native scalar ADM EH on untilted chart

Native spherical Einstein–Hilbert quadratic action now includes lapse, shift, spatial trace/shear and their rates for BOTH sectors, in restricted T=t and constant radial ratio 1+mu. 11 direct EH tests and 2 mock-only HR/two-dust wrapper tests pass in a fresh focused workspace (13 total). A cross-HR metric audit corrected the f E and E_dot m² amplitude transformation. No full real combined action run or physical reduction/oracles yet. GATE_2B_OPEN. Details research/FULL_NATIVE_SCALAR_EH_UNTILTED_AUDIT.md and root LATEST_RESTART.md.

## Addendum 2026-10-18 — real-provider untilted integration and f-EH FLRW chart Ward

Four real-algorithm EH+HR+two-dust 24-slot integration tests now PASS in the focused local workspace (no mock for these four), including radial quadrature refinement and zero-HR limit. A NEW f-native FLRW Einstein–Hilbert lapse compact spacetime Ward identity passes seven independently written tests, including a direct match to the repository's old ADM primitive and a negative control where omitting field sampling yields nonzero residual. Total newly combined focused suite: **24 passed**. Manual reconstructions of older HR/dust provider modules match algorithmic structure but not byte SHA; this is not a full clean-checkout repo suite. See `research/REAL_PROVIDER_AND_EH_WARD_AUDIT_2026_10_18.md` and root `LATEST_RESTART.md`. **No full f scalar EH chart variation, on-shell background, metric/BD reduction, De Felice/Aoki same-action pass or Candidate-C fold result. GATE_2B OPEN.**

### Addendum 2026-10-18 — all-four-scalar f ADM compact chart pullback gate

Exact nonlinear native f ADM+GHY density now independently checked with lapse, shift, trace and shear field sampling under time/radius compact chart variations. Eight mixed coordinate/field Ward variations vanish, eight frozen-field sampling controls fail, and direct Hessian matches independent existing EH six-field jet. 8 NEW tests, 32 focused local reconstructed total, exact SHA for three new source/test/runner files; no full worktree clone. Root LATEST_RESTART.md step24 and research/FULL_SCALAR_EH_CHART_WARD_STEP24_AUDIT.md. It is a kinematic coordinate-change check ONLY; full finite-mu EH chart Hessian and both physical De Felice/Aoki oracles remain missing, GATE2B=OPEN.

## Addendum 2026-10-18 — isolated f-EH full scalar chart quadratic

Step25 derived/executed the 6×6 time-and-radial integrated native f Einstein–Hilbert chart-plus-metric quadratic Hessian. Its 2×6 chart rows vanish to ~8.7e-13 for compact coordinate changes with complete field derivative sampling, while 4×4 metric block is nonzero; frozen field sampling fails. A separate beta1-3 HR radial interaction Hessian has a nonzero relative chart sector. 9 new tests, 41 total focused local tests passed; exact git blob SHA for three new files; local older HR dependencies not exact clean Git clone. Crucially this is a Piola/boundary diffeomorphism check, not the physical coupled BD/metric constraint oracles. See research/EH_CHART_QUADRATIC_STEP25_AUDIT.md and root LATEST_RESTART.md. **GATE_2B OPEN.**

## Addendum 2026-10-18 — step26 coupled HR diagonal Ward and off-shell Hessian

With all five beta_n Hassan–Rosen interaction sectors, both native scalar metric field sets and an inclined nonhomothetic f chart, a **DIAGONAL common** diffeomorphism of both metrics now passes a compact spacetime nonlinear action Ward test; relative f shifts change beta1/2/3 while beta0/4 decouple. Direct interaction density matches the prior independent 14-jet HR oracle. An independent 4x4 g/f chart Hessian demonstrates that off-shell H*v_diag need NOT vanish even if the entire finite diagonal gauge orbit leaves S unchanged; tadpoles/gauge-generator derivatives enter the differentiated Noether identity. 16 NEW tests, 57 total local focused tests passed, five new files exact GitHub SHA; older reconstructed HR/dust prerequisites are not a full clean checkout. Current full dynamical action/on-shell dust/BD and two physical oracle gates remain OPEN. See research/COUPLED_DIAGONAL_NOETHER_STEP26_AUDIT.md and root LATEST_RESTART.md.

## Addendum 2026-10-18 — Step27 full five-sector off-shell spacetime consistency gate

A single native-consistent nonlinear two-metric compact spacetime trial action now evaluates positive Einstein–Hilbert g and f sectors, all-beta Hassan–Rosen interaction, and both covariant irrotational pressureless dust actions on exactly the same field/metric/chart sources. The *five separate* action terms pass diagonal coordinate Ward and only HR varies under a relative f-native coordinate displacement. A separate exact native Legendre transform preserves two independent dust phase/momentum pairs and confirms the rho multiplier stationary reduction (NOT the full common-time two-dust canonical equivalence). Old exact ADM and old HR action cross-checks passed. 18 NEW tests, 75/75 targeted local tests passed; exact GitHub SHA verified for six new source/test/runner/audit files; older prerequisites reconstructed locally, not a clean clone. Detailed proof, numbers, limitations and next RED in research/UNIFIED_FIVE_SECTOR_SPACETIME_STEP27_AUDIT.md and root LATEST_RESTART.md. No on-shell Candidate-C background, tadpole cancellation, physical metric/BD reduction, Aoki/DeFelice acceptance, first fold or cosmological validation; GATE_2B=OPEN.

## Addendum 2026-10-18 — Step28 on-shell homogeneous two-dust Candidate-C background

A single exact FRW minisuperspace positive-sign Einstein–Hilbert g+f + all-beta Hassan–Rosen + two independently conserved canonical dust Routhian now reconstructs the **radiation-REMOVED Candidate-C** branch and passes both lapse/Friedmann constraints, both scale Euler equations and dynamical Bianchi residuals (~5.4e-13 max over representative epochs), independently checked by action finite differences. A real g-cosmic-time compact first-variation test of the time-integrated action finds all FOUR background tadpoles ~1e-10 or smaller. Premature on-shell substitution of dust clocks would incorrectly erase their lapse source; negative tests enforce correct fixed-momentum Routh procedure. 17 NEW targeted tests passed in standalone workspace; earlier 75 tests NOT rerun, therefore NO combined 92-test claim. Four new files exact GitHub SHA. Smooth homogeneous y across mu fold locations is NOT physical relative-Stückelberg fold crossing. Detailed science `research/MINISUPERSPACE_ONSHELL_STEP28_AUDIT.md`, restart `LATEST_RESTART.md`. **Full Step27 nonhomothetic action remains OFF SHELL; Gate2B OPEN.**

## Step29 (2026-10-18): homogeneous-to-nonhomothetic insertion RED

The Candidate-C dust-only homogeneous background cannot be inserted unchanged into R_f=(1+mu)r. At r->0 the HR g-lapse source depends on V_g((1+mu)*b/a), not V_g(b/a). At a=0.4 and mu=-0.22 the necessary g-lapse residual is +0.160780603695 in normalized units, versus approximately zero on the homogeneous solution. Direct exact HR square-root differentiation and compact radial action variation confirm this. Rescaling the f-native scale can repair the center source, so this is not a universal JANUS no-go. Native time tilt still requires radial backreaction. 21 Step29 tests passed in a standalone workspace; previous test suites were not rerun. Read research/NONHOMOTHETIC_ONSHELL_INSERTION_STEP29_AUDIT.md and root LATEST_RESTART.md. Corrected full nonhomothetic background and physical constraints remain open. Gate2B OPEN.

## Addendum 2026-10-18 — Step30 exact coordinate-compensated native f and dust baseline

Step30 derives the **complete inverse-Jacobian** compensation of the f-native 2×2 metric, angular area, dust clock phase gradient and conserved current from the on-shell homogeneous dust-only Candidate-C solution. Full g-common pulled-back f metric and HR all-beta potential are invariant, native f dust norm and covariant current conservation pass, and a nonzero off-shell dust Lagrangian obeys the exact Jacobian. A compact time+radial g lapse sub-action tadpole is ~1.30e-13; freezing the native f shift/spatial component changes and only compensating b produces a ~3.50e-8 tadpole, pointwise +3.116e-4. The correct f-native metric generically has shift, coordinate radial/angular anisotropy and radial dust gradient/current. **This is a pure coordinate relabelling of the already homogeneous physical solution, NOT a new nonhomothetic physical screened mode, a fold crossing, or proof of ghost freedom.** 18 NEW tests pass in standalone workspace, prior test suites not rerun; four new git source/test/audit/runner blobs exact SHA-matched. Full genuine on-shell nonhomothetic branch, constraints, De Felice/Aoki remain open. See research/INVERSE_CHART_COMPENSATION_STEP30_AUDIT.md and root LATEST_RESTART.md. GATE2B OPEN.

## Addendum 2026-10-19 — Step31 genuine 12-direction scalar/matter tadpole checks on homogeneous on-shell background

Now ONE full time/radial spherical EH_g+EH_f (positive Einstein–Hilbert), all-beta HR and TWO original covariant dust field action is evaluated with EXACTLY identical g/f common chart tensor fields on the radiation-free homogeneous on-shell Candidate-C background. All TWELVE independent metric/dust scalar compact first variations cancel numerically, largest residual 1.4051e-11; separate EH+HR+dust pieces demonstrably nonzero and cancel in both lapse sectors. Removing HR destroys both background lapse equations; an f-only spatial trace trial varies relative metric curvature/area and has nonzero unreduced quadratic response; H[Phi_g,psi_f]≈-1.84236e-4 disappears for m²=0. Local two-dust Legendre checks performed. **29 NEW targeted tests pass in fresh standalone**, all four new executable/test/audit source blobs EXACT to live GitHub, historical suites not rerun. The background remains PHYSICALLY HOMOGENEOUS and only the independent *perturbations* are nonhomogeneous: no genuine finite-μ on-shell solution/BD reduction/De Felice/Aoki speed/first-fold verdict. Detailed `research/FULL_ONSHELL_TWELVE_FIELD_TADPOLES_STEP31_AUDIT.md`, authoritative root `LATEST_RESTART.md`. **GATE_2B=OPEN**.

## Addendum 2026-10-19 — Step32 exact two-dust common-time canonical action

Two dust multipliers/phase rates now have an exact **OFF-SHELL** covariant-to-first-order ADM Legendre transform on the same Step31 on-shell homogeneous-background full positive EH_g/f+HR+two-dust spherical action. Eliminating rho only after Legendre yields H_dust=N p sqrt(1+theta_r²/g_rr)+N^r p theta_r, linear in true ADM lapse/shift. Independent canonical (p_g,theta_g) and (p_f,theta_f) survive: the 14×14 UNREDUCED compact action Hessian has momentum–phase-rate block rank 2, diagonal +9.450339095e-5 and +1.303392697e-5, cross zero, and 12 valid compact field tadpoles ~3.73e-12. Local separate phase-rate jets are NOT legal independent compact field variations, so their nonzero first variations do not represent tadpoles. **49 combined focused tests** actually passed together (29 original exact-byte Step31 plus 20 new), all four newly committed files exact Git blob matches. Still missing independent four metric velocities, metric/BD canonical constraints, genuinely nonhomothetic on-shell solution, both physical De Felice/Aoki oracle acceptances and first fold. Detailed research/COMMON_TIME_TWO_DUST_CANONICAL_STEP32_AUDIT.md and root LATEST_RESTART.md. GATE_2B OPEN.

## Addendum 2026-10-19 — Step32b full four EH scalar metric time-rate jets + exact dual dust symplectic pairs

One REAL common-time five-sector positive EH_g/f+all-beta HR+TWO dust on-shell HOMOGENEOUS Candidate-C scalar action now has an **18-amplitude** field/velocity jet interface: 14 from exact canonical dual-dust Legendre action plus four independently varied ADM EH spatial trace/shear rates of both metrics. The 4×4 UNREDUCED EH rate Hessian reproduces independent closed-form trace/shear kinetic coefficients to <1e-15 absolute, cross-sector and trace/shear rate mixed zero. 2 canonical dust p--phase-rate entries remain independent, rank 2. **Negative trace signs are preconstraint, not physical ghosts.** Local phase/metric rates are independent differential jets, NOT globally free compact perturbations; no premature on-shell tadpole inference. Actually 60 targeted tests passed in ONE workspace combining 29 original byte-identical Step31, 20 Step32a and 11 Step32b; new files GitHub SHA exact matches, NOT full repo clean clone. Remaining RED: 4 ADM auxiliaries and time-dependent BD-null reduction, genuine nonhomothetic on-shell background, two De Felice/Aoki physical acceptance controls and fold. See research/FOUR_METRIC_RATE_JETS_STEP32B_AUDIT.md and root LATEST_RESTART.md. **GATE_2B OPEN; JANUS-R NOT VALIDATED.**
