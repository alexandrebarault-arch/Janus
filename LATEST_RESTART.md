# JANUS — REPRISE PRIORITAIRE : ÉTAPE 32 (2026-10-19)

**READ FIRST:** `research/COMMON_TIME_TWO_DUST_CANONICAL_STEP32_AUDIT.md`.
**New module:** `numerics/hr_two_dust_common_time_canonical.py`.
**New tests:** `tests/test_hr_two_dust_common_time_canonical.py`.
**Reproduce in one command:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step32.py gate2b-step32-report.json`.

## 32. Exact two-dust COMMON-TIME phase-space Legendre bridge GREEN — full metric-velocity, BD and physical oracles STILL OPEN

**Advance over Step31:** The previous complete positive EH_g + positive EH_f + all-beta HR + TWO *covariant* irrotational dust spherical scalar action was tested at 12 compact first variations on the **radiation-free, HOMOGENEOUS on-shell Candidate-C** trajectory. Step32 now performs an **EXACT local ADM Legendre transform** of BOTH dusts on the SAME Step31 nonlinearly perturbed spherical metric tensors, BEFORE eliminating the dust density multiplier. This preserves the two dust momenta and two dust phase variables in a single common-time, five-sector **first-order canonical** spacetime action. It additionally evaluates the full **14×14 compact preconstraint Hessian** and compares its two phase-velocity/momentum columns with a separate analytic 4π radial/time integral.

For each metric, `N=sqrt(-g_tt+g_tr²/g_rr)`, `N^r=g_tr/g_rr`, `sqrt(gamma)=sqrt(g_rr)*g_angular`. The original dust scalar density is `sqrtgamma*rho/(2N)*[(theta_dot-N^r theta_r)^2-N²(1+theta_r²/g_rr)]`. Exact Legendre gives `p=sqrtgamma*rho*(theta_dot-N^r theta_r)/N`, `H_rho=N[p²/(2sqrtgamma*rho)+sqrtgamma*rho(1+theta_r²/g_rr)/2]+N^r p theta_r`. ONLY AFTER THIS, stationary multiplier `rho*=p/[sqrtgamma sqrt(1+theta_r²/g_rr)]` yields **`L_dust,red=p theta_dot-N p sqrt(1+theta_r²/g_rr)-N^r p theta_r`**. Exact equality of off-shell covariant and Legendre dust densities is tested in BOTH sectors for nonzero perturbations, not by the trivial zero-on-clock value.

**Important auxiliary fact:** at fixed spatial fields and p, the dust Hamiltonian is affine in true ADM lapse and shift. This DOES NOT solve full coupled EH+HR constraint algebra or BD null reduction. In the 14-amplitude trial jet the seven slots per sector are `(Phi,U,psi,E,theta,p,theta_rate)`, and the two independent *local* phase-rate jets are NOT independently admissible compact theta field variations. Their linear derivatives are NONZERO and are correctly excluded from the on-shell field-tadpole test.

**Reproducible diagnostics:** full preconstraint Hessian H has `H[p_g,theta_rate_g]=+9.450339095258206e-05`, `H[p_f,theta_rate_f]=+1.3033926965066306e-05`, cross-pair zero, 2×2 symplectic block rank 2. The two independent phase-rate rows are zero elsewhere; momentum-momentum and rate-rate dust blocks vanish in this stationary-rho reduced canonical representation. Twelve valid compact metric/phase/momentum field first variations remain zero to max `3.729655473350135e-12`; HR cross-metric coefficient `H[Phi_g,psi_f]≈-0.0001842360821` remains nonzero (and is zero with m²=0, while the background lapse tadpoles then fail).

**ACTUAL TEST:** **49 PASS in ONE local focused workspace /mnt/data/janus32** = 29 original exact Step31 tests (the Step31 original module and test have exact GitHub blob hash matching local bytes) + **20 NEW Step32 tests**. Both the direct pytest suite and independent `scripts/verify_gate2b_step32.py` runner returned exit code 0 / 49 passed, manifest marks incomplete full-repo checkout, BD/De Felice/Aoki `NOT_RUN`, `GATE_2B=OPEN`. This is a real combined 29+20 test result, UNLIKE prior separate step test counts. All FOUR new files exactly match tested local Git blobs:
- numerics/hr_two_dust_common_time_canonical.py `6b6c8a8e8f5373005ff51cf169b0360fc9caec37`
- tests/test_hr_two_dust_common_time_canonical.py `020c87f1b3a805f23c66cf20516ba82fb7f1796d`
- scripts/verify_gate2b_step32.py `c2887ec07ac6aec1ca3a27716dbcb038713b4c76`
- research/COMMON_TIME_TWO_DUST_CANONICAL_STEP32_AUDIT.md `dd3a8ebddde6716b2817de69ec26cdf991e31467`

**CURRENT EXACT RED:** (1) extend the Step31 EH+HR+two dust action to retain INDEPENDENT metric spatial trace and shear TIME-RATE jets `psi_dot_g,E_dot_g,psi_dot_f,E_dot_f`; then form a coherent common-time quadratic field/rate operator and ADM lapse/shift auxiliary constraints. Do not read physical kinetic/ghost signs from the current UNREDUCED 14×14 Hessian. (2) Canonically eliminate the time-dependent HR BD-null direction while preserving BOTH independent dust (theta,p) symplectic pairs. (3) Independently solve a genuinely NONHOMOTHETIC on-shell Candidate-C two-dust background beyond the passive compensated chart; full 5-sector Einstein and matter tadpoles required. (4) Reproduce De Felice finite-H μ→0 scalar and nonlinear homothetic Aoki K_S,c_S² (stable+unstable) on the SAME reduced action before first relative μ-fold `a≈0.0301646` or any CMB prediction.

**Verdict:** `COMMON_TIME_TWO_DUST_CANONICAL_GREEN`, `METRIC_BD_REDUCTION_OPEN`, `GENUINE_NONHOMOTHETIC_ON_SHELL_OPEN`, `GATE_2B=OPEN`; JANUS-R NOT VALIDATED. Work ONLY on `research/gate2b-nonhomothetic-transfer`, leave main/v2-flrw untouched; external 2026 JHR negative-f-EH-sign audit separate.

---

# JANUS — POINT DE REPRISE PRIORITAIRE, ÉTAPE 31 (2026-10-19)

**FIRST READ:** `research/FULL_ONSHELL_TWELVE_FIELD_TADPOLES_STEP31_AUDIT.md`.
**NEW SOURCE:** `numerics/hr_full_onshell_tadpole.py`.
**NEW TESTS:** `tests/test_hr_full_onshell_tadpole.py`.
**ONE COMMAND:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step31.py gate2b-step31-report.json`.

## 31. ONE full nonlinear common-chart spherical scalar + TWO dust action on HOMOGENEOUS ON-SHELL Candidate C — 12 first variations GREEN; physical nonhomothetic Gate2B OPEN

After Step30 exact passive-chart compensation, a NEW standalone code now computes **ONE spacetime-integrated** action with five contributions (EH_g positive, EH_f positive, all-beta Hassan–Rosen, covariant dust_g, covariant dust_f) over the SAME metric/field basis, at the **actual on-shell radiation-free homogeneous dust-only Candidate-C** trajectory obtained by integrating a_dot=aH. Earlier step27's five-sector common action was OFF SHELL and step30 checked only the g lapse tadpole; this step checks TWELVE directions of independent fields on the homogeneous on-shell branch.

**All 12 independent compact time+radius first variations vanish** for `(Phi_g,U_g,psi_g,E_g,theta_g,rho_g,Phi_f,U_f,psi_f,E_f,theta_f,rho_f)`. This time includes *all spatial 3-curvature, ADM extrinsic rates, native metric trace/shear and both covariant dust phase/multiplier terms*. At time halfwidth .027, radial support .32 and quadrature 24, centered amplitude step 2e-5, max abs first variation is `1.4051260155412136e-11`; tested quadrature/step/domain refinements. Contributions are genuinely individually nonzero and cancel: dS/dPhi_g approx EH_g +3.64871135e-4, HR -6.44695537e-5, dust_g -3.00401582e-4; dS/dPhi_f approx EH_f +1.29610824e-6, HR +2.01858490e-5, dust_f -2.14819573e-5. Both matter phase and density directions cancel only after the original covariant dust action has been varied (NO prematurely imposing theta_dot=N in L).

**Independent physical trial deformation beyond Step30 pure-chart map:** varying only f spatial trace psi_f changes its physical common-chart 3-curvature and relative angular eigenvalue while keeping g fixed, and yields a NONZERO quadratic action. Mixed relative Hessian H[Phi_g,psi_f] ≈ -0.0001842360131; removing the HR interaction makes this cross-metric block vanish and immediately breaks both g/f background lapse tadpoles. Other controls independently check beta4 is f-volume-only, both native local dust Legendre phase pairs, exact tilted native f tensor pullback even with nonzero independent f perturbation. **These are UNREDUCED trial-field Hessian coefficients, NOT physical scalar speeds, canonical kinetic eigenvalues or physical ghost criteria.**

**Actually executed NEW standalone:** `PYTHONPATH=/mnt/data/janus31 OPENBLAS_NUM_THREADS=1 python -m pytest -q /mnt/data/janus31/tests/test_hr_full_onshell_tadpole.py` → **29 passed**. `scripts/verify_gate2b_step31.py` reproduced 29/29 with exit 0, `workspace_origin=standalone_focused_workspace`, `full_repo_test_suite=false`, `historical_test_suites_rerun=false`, De Felice/Aoki NOT_RUN, BD reduction NO, `GATE_2B_OPEN`. FOUR newly committed files are **exact-byte SHA identical** to local tested ones:
- numerics/hr_full_onshell_tadpole.py `e05d8f54cf4eff76a92c278ffdd971612d1ec56b`
- tests/test_hr_full_onshell_tadpole.py `68fb2302ae57c350db087ea3caf5898ca31661af`
- scripts/verify_gate2b_step31.py `6ae34372ccc5a034fc5ef6bf27339ebca9a446bf`
- research/FULL_ONSHELL_TWELVE_FIELD_TADPOLES_STEP31_AUDIT.md `b8abf50a91cdf6a75e2a4a19e6b6d2ec404b9119`

Historical steps 30 (18), 29 (21), 28 (17), 27 (75) were in SEPARATE workspaces and **NOT rerun here**: do not claim cumulative passing counts. Git clone still DNS blocked; GitHub Actions disabled. No fresh full repository verification.

**CRITICAL LIMITATION:** the homogeneous on-shell background in common chart is merely the *same physical* compensated configuration identified in Step30. An independent finite-amplitude f field variation is a valid mathematical test direction, NOT a newly solved genuinely NONHOMOTHETIC background. No full time-dependent canonical/metric/BD constraint elimination, no De Felice/Aoki independent physical oracles, no relative-mu fold crossing or cosmological likelihood yet.

**NEXT EXACT RED:** from this *single* full spherical EH_g+EH_f+HR+two-dust action derive a consistent common-time quadratic **field and rate** operator, identify all lapse/shift metric auxiliary directions and exact diagonal Noether constraints ON SHELL, and canonically reduce both dust phase/momentum pairs and the time-dependent BD-null direction. In parallel, solve full radial/time Einstein+HR+matter first variations for a **genuinely nonhomothetic** background beyond Step30 pure-chart compensation; test its tadpoles. Only from the SAME full reduced physical action attempt De Felice finite-H mu→0 and Aoki nonlinear homothetic KS,cS² stable/unstable, then first Candidate-C relative μ-fold a≈0.0301646. If impossible, publish specific failed gate; no fabricated validation.

**Verdict:** `COMMON_HOMOGENEOUS_ONSHELL_12_FIELD_ACTION_GREEN`, `GENUINE_NONHOMOTHETIC_BACKGROUND_OPEN`, `GATE_2B_OPEN`, `JANUS_R_NOT_VALIDATED`. Work ONLY in research/gate2b-nonhomothetic-transfer; leave main and research/v2-flrw untouched; external 2026 JHR opposite-f-EH-sign ghost audit separate.

---

# JANUS — POINT DE REPRISE PRIORITAIRE, ÉTAPE 30 (2026-10-18)

**READ FIRST:** `research/INVERSE_CHART_COMPENSATION_STEP30_AUDIT.md`.
**Code/tests:** `numerics/hr_compensated_native_chart.py`, `tests/test_hr_compensated_native_chart.py`.
**Reproduce:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step30.py gate2b-step30-report.json`.

## 30. EXACT native f metric+dust inverse-chart compensation established — PURE GAUGE BASELINE, NOT NEW PHYSICAL SOLUTION

Step29 proved that naïvely inserting the homogeneous on-shell Candidate-C two-dust solution into `T=t+sigma(t)r²/2, R=lambda(t)r` fails the visible g lapse equation unless the native f geometry is adjusted. Simply setting `b_native=b_hom/lambda` repairs only the central scale ratio and fails at finite radius for tilted/evolving charts.

**NEW exact inverse-chart construction:** start from the real *on-shell radiation-free homogeneous two-dust Candidate-C* metric `f_common=diag(-Nf(t)²,b(t)²)`, angular `b(t)²r²`, physical comoving f dust `theta_fdot=Nf, rho_f=Cf/b³`. On a regular nonhomothetic background chart `X=(T,R)`, `J=dX/d(t,r)`, obtain

```
f_native=J^{-T} f_common J^{-1}
f_native_ang=b(t)² r²
(theta_native,T,theta_native,R)=(Nf,0) J^{-1}
rho_native=Cf/b(t(T,R))³
native dust current density^A=Cf r² J^A_t / det(J).
```

**Critical physical restriction:** the fully transported f-native metric generically has nonzero `f_TR`, radial/angular non-FLRW components, radial-dependent dust clock and a NONZERO native radial dust flux. This is a PURE passive reparametrization of the SAME homogeneous physical f metric, NOT a new nonlinear nonhomothetic physical solution. It cannot produce the independent helicity-0 canonical matching data or demonstrate crossing the mu fold at a≈0.0301646. Imposing the old f-native diagonal/FLRW ansatz after the coordinate change is NOT an equivalent metric.

**Numerical witness:** at a=.4, t=0, r=.2, lambda=.78, sigma=.08, lambda_dot=.04, sigma_dot=.025, the exact transported native f off-diagonal component is +0.00480694489921799. All 2×2 common f metric components and angular area are recovered to ~1e-16 via `J^T f_native J`. The native dust normalization is -1 and its density current divergence is ~5.4e-12 (finite differences). The exact HR potential matches the homogeneous all-beta expression at multiple t/r, and a NONZERO off-shell native dust Lagrangian agrees with its common counterpart only after multiplying by the full Jacobian determinant.

**Physical necessary g lapse test, also integrated across COMPACT TIME+RADIUS:** on this compensated, homogeneous-on-shell baseline the direct visible lapse residual at r=.2 is ~2.66e-10 and compact time/radial first action variation is +1.30104260698e-13 (finite-difference cancellation). The deliberately truncated scale-only diagonal native ansatz gives +0.0003116455094 and +3.50278833716e-8 respectively. The tested compact action includes g positive EH ADM+GHY, canonical g dust charge and exact all-beta HR with fully transported f geometry. This is ONE necessary Euler direction, NOT full coupled five-sector tadpoles.

**ACTUALLY EXECUTED in NEW standalone `/mnt/data/janus30`: 18/18 targeted tests PASS.** Runner JSON exit 0 / 18 passed, `workspace_origin=standalone_focused_workspace`, `full_repository_regression=false`, `previous_step29_tests_rerun=false`, `DeFelice/Aoki NOT_RUN`, `GATE_2B OPEN`. All FOUR new source/test/runner/audit GitHub files have been byte-verified against the actual local git hash:
- numerics/hr_compensated_native_chart.py = `14bf842c9bcfe792a1891c7a8d758c76f37f30c9`
- tests/test_hr_compensated_native_chart.py = `b81966e9395a8fc7728773fd4b0745e704a9c13f`
- scripts/verify_gate2b_step30.py = `1036166d4bfe57ad9bf6e6c67ca157d5267c1c5b`
- research/INVERSE_CHART_COMPENSATION_STEP30_AUDIT.md = `e897229ea831f162252db2845c630b2dd4a42b47`

Previous Step29 21, Step28 17 and Step27 75 tests were run in OTHER workspaces and **not rerun together**; NEVER claim 131 tests passed in one run. Full clean repo clone still DNS-blocked and GitHub Actions disabled.

**NEXT EXACT RED:** starting FROM THIS EXACT compensated on-shell baseline, introduce a *physically independent* f native metric/Stückelberg relative deformation (e.g. independent shift, trace/shear, time/radial profiles AND both matter phases), not merely `J^{-T}f J^{-1}`. Calculate ALL g/f Einstein, HR relative chart, and both dust Euler/tadpoles on one shared time/radial action. Demand their cancellation for a genuinely nonhomothetic on-shell branch; only then derive physical constrained scalar action, reduce four metric auxiliaries and time-dependent BD-null with two canonical dust pairs, and pass the independently required SAME-ACTION De Felice finite-H mu→0 and Aoki nonlinear homothetic `K_S,c_S²` physical controls before testing the first relative-mu fold and any observational transfer.

**Verdict:** `COORDINATE_COMPENSATION_BASELINE_GREEN`; `GENUINE_NONHOMOTHETIC_ONSHELL_BRANCH_OPEN`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`. Work ONLY on research/gate2b-nonhomothetic-transfer. main and research/v2-flrw untouched. Keep external opposite-EH-sign JHR tensor critique separate.

---

# JANUS — REPRISE PRIORITAIRE : ÉTAPE 29 (2026-10-18)

**FIRST READ:** `research/NONHOMOTHETIC_ONSHELL_INSERTION_STEP29_AUDIT.md`.
**Reproduce immediately:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step29.py gate2b-step29-report.json`.
**New verified code/tests:** `numerics/hr_nonhomothetic_center_obstruction.py`, `tests/test_hr_nonhomothetic_center_obstruction.py`.

## 29. Naïve on-shell Candidate-C -> finite-μ nonhomothetic insertion: EXPLICIT RED (LATEST)

**Actual scientific result: a falsified SUBSTITUTION, NOT a general no-go for JANUS.** Step28 proved the TWO-DUST, NO-RADIATION homogeneous Candidate-C background solves its homogeneous positive-EH+HR+two-dust Routhian. Step27's common full 5-sector spacetime action still uses arbitrary OFF-SHELL g/f polynomials. Step29 checks the proposed direct substitution of Step28 into the nonhomothetic f chart `T=t+σ(t)r²/2`, `R_f=λ(t)r`, `λ=1+μ>0`, leaving the previously on-shell native f scale `b(T)` unchanged. At the center the square-root spatial eigenvalues are `λ b/a`, NOT `b/a`, so the g lapse potential is `V_g(λy)` rather than `V_g(y)`. Hence the exact necessary center lapse residual is

```
R_g(λ) = 3 Mg² a adot²/Ng² - Cg - m² Mg² a³ V_g(λ y),
R_g(1)=0  on homogeneous Candidate-C dust-only branch,
R_g(λ)-R_g(1)=-m² Mg² a³ [V_g(λy)-V_g(y)],
V_g(z)=β0+3β1 z+3β2 z²+β3 z³,
d R_g/dλ |_{λ=1}=-3m² Mg² a³ y J_g(y).
```

**Quantitative decisive benchmark:** at `a=.4`, `y=.578770722803`, `Ng=1`, `Nf=.518526433828`, `λ=.78` (μ=-.22), previously on-shell `R_g(1)≈0` becomes **`R_g(.78)=+0.160780603695`** in the normalized action. The analytically independent exact 2x2 principal-root spherical Hassan–Rosen density, directly finite-differentiated with respect to the g lapse at radius 10^-4, recovers the same residual. The independently compact-radial g-EH+canonical-dust+HR first action variation for support radius .035 is **+3.20003248e-6**, matching the exact bump integral. No need to interpret raw off-shell Hessian eigenvalues. At a=.03 and λ=.231117 (relative μ fold location used only as reference), the same naïve source is +.03919434, NOT proof of physical fold failure.

**Critical NON-NO-GO counterexample:** setting `b_native=b_homogeneous/λ` for CONSTANT λ restores `λb_native/a=y` and cancels this CENTER g lapse obstruction. But at finite r, `σ≠0` introduces common-slice component anisotropy `f_rr-f_theta_theta/r²=-n(T)²σ²r²` and the direct g lapse source remains nonzero in the chosen off-shell f time/scale jets even after center compensation; q.g. at a=.4, λ=.78, r=.2, σ=.08 yields roughly -0.0017545. This is a slicing component identity, NOT invariant physical anisotropic stress and NOT a theorem that the fully corrected nonhomothetic system has no solution. Native f matter phase/charge and all metric radial/time derivatives must be re-solved.

**Actually executed new test evidence:** 21/21 PASS, `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_nonhomothetic_center_obstruction.py` in isolated `/mnt/data/janus29`. Includes independent recomputation of radiation-free Candidate-C quartic roots and f lapse `Nf=y+y_N` for FOUR epochs; independent direct spherical HR matrix-square-root differentiation at FIVE parameter points, compact g lapse action variation, analytic J slope, radius/step convergence, β4 decoupling, m²=0, compensated central scaling and residual finite radius. `scripts/verify_gate2b_step29.py` generates exact SHA-256 source manifests, diagnostic witness, `workspace_origin=standalone_focused_workspace`, `full_repository_regression=false`, `DeFelice/Aoki NOT_RUN`, `GATE_2B=OPEN`. All FOUR new source/test/script/audit Git blobs have been matched BYTE FOR BYTE against locally executed files. Prior Step27 75 tests and Step28 17 tests belong to OTHER workspaces and were NOT rerun together; do NOT claim 113 combined tests. Direct Git clone DNS fails; no CI/independent replication claimed.

**NEXT EXACT RED:** construct a chart-**COMPENSATED** f-native background `b_native(T)` and both dust phase/charge transformations consistent with the nonhomothetic common geometry and native dust conservation. Then evaluate ALL g and f lapse, radial/time/scale, scalar and Stückelberg Euler residuals from the SAME Step27 five-sector action on one common compact spacetime support, not only the center. Reject trial backgrounds with nonzero tadpoles. Only if a genuine full on-shell nonhomothetic solution is found, derive time-dependent EH+HR+two-dust physical scalar quadratic action, reduce metric auxiliaries/time-dependent BD-null with BOTH matter canonical pairs, pass BOTH De Felice finite-H μ→0 and Aoki homothetic K_S,c_S² oracles, THEN assess the first relative μ fold at a≈0.0301646. No ghost/gradient/fold/CMB viability conclusion yet.

**Verdict:** `NAIVE_HOMOGENEOUS_INSERTION_FAIL`; `CORRECTED_FULL_NONHOMOTHETIC_BACKGROUND_OPEN`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`. Preserve exact branch `research/gate2b-nonhomothetic-transfer`; do not touch main or research/v2-flrw; keep external JHR negative-f-EH ghost critique separate.

---

# JANUS — POINT DE REPRISE PRIORITAIRE, ÉTAPE 28 (2026-10-18)

**READ FIRST:** `research/MINISUPERSPACE_ONSHELL_STEP28_AUDIT.md`.

**Sources + 17 new tests:** `numerics/hr_minisuperspace_onshell.py`, `tests/test_hr_minisuperspace_onshell.py`.

**Repeatable step28 runner:** `python scripts/verify_gate2b_step28.py gate2b-step28-report.json`.

## 28. Candidate-C TWO-DUST homogeneous on-shell background and compact action tadpoles GREEN — full nonhomothetic Gate 2B OPEN

The previous Step27 has ONE full nonlinear **OFF-SHELL** spacetime integral for EH_g (+), EH_f (+), all-beta HR and two separately coupled irrotational dust sectors on shared native metric coordinates, but its polynomial backgrounds do NOT satisfy the two metric Friedmann equations. Step28 establishes an **independent exact on-shell HOMOGENEOUS** five-sector minisuperspace Routhian and validates its first variations:

```
L = -3 Mg² a a_dot²/Ng -3 Mf² b b_dot²/Nf
    -m² Mg² a³[Ng (β0+3β1 y+3β2 y²+β3 y³)
              +Nf (β1+3β2 y+3β3 y²+β4 y³)]
    -Ng Cg-Nf Cf,    y=b/a.
```

**Critical matter issue (NEW regression):** the homogeneous covariant dust Lagrangian evaluates to zero on its normalized clock, but its *partial lapse variation* does NOT vanish: ∂L_dust/∂N|theta_dot,rho = -C. Early on-shell substitution before variation would erase both dust Friedmann sources. The fixed-charge Routhian terms -Ng Cg -Nf Cf are derived by canonical Legendre/Routh reduction and preserve both independent matter phase momenta. All four scale/lapse Euler residuals are analytically derived from this ONE action and separately tested by numerical partial differences.

**Candidate C scope STRICT:** radiation is REMOVED intentionally (Ω_g,r0=0) to match existing `candidate_c_dust_background.py` stress test, NOT the complete radiation-era model. Re-solve present y0 after this removal: y0=0.5568825591873054; E(1)=0.9999551638376833, not exactly 1. On its regular dynamical homogeneous branch with Ng=1 and Nf=y+y_N, the two Friedmann constraints, two acceleration Euler equations, Bianchi relation and both conserved dust constants pass to max ~5.4e-13 over representative points a=1,.8,.4,.2,.09,.05,.03. Independent implicit polynomial derivatives supply y_N,y_NN; no tuned acceleration input.

**NEW real time-domain tadpole test:** solve da/dt=aE(a) in both time directions, sample on-shell a,b,Ng,Nf on Gauss–Legendre temporal points, independently perturb each with compact F(t)=(1-t²/T²)^4 and the correct derivative Fdot for scale factors. The first variation of the **integrated homogeneous Routhian** vanishes in all four directions. At time half-window .025, 26 quadrature points and finite amplitude 1e-6: (-1.8041e-10,+1.3878e-11,0,-6.9389e-12) in order (a,b,Ng,Nf). Refinement tests 18/26/32 and different time supports pass. A test with too-large initial variation steps 1e-5/2e-5 showed O(h²) truncation (1e-8/1e-7); reduced step to 1e-6, not edited physical equations.

**Negative controls:** increasing Nf by 2% at a=.4 causes f lapse residual -2.90764390585e-4 and Bianchi failure; increasing Cf by 1% induces exactly -0.01 Cf shift of f lapse constraint. Generic polynomial off-shell sample has nonzero lapse and scale Euler residuals. A smooth homogeneous y(a) on either side of the previously found local nonlinear **relative-μ** folds at a~.0301646/.0491246 is NOT a proof of Stückelberg fold crossing.

**ACTUAL testing now:** 17 new focused tests PASS (Python 3.13.5, standalone `/mnt/data/janus28`). Runner exit 0 / 17 passed / `standalone_focused_workspace` / `full_repository_regression=false` / `DeFelice/Aoki NOT_RUN` / `GATE_2B OPEN`. **Do not claim 75+17=92 executed together**: 75 prior tests belong to earlier separate reconstructed workspace; no clean full Git clone or CI run. FOUR new source/test/runner/audit files are EXACT byte-matched GitHub blobs (SHA in audit). Branch only `research/gate2b-nonhomothetic-transfer`; main/v2-flrw unchanged.

**NEXT EXACT RED — priority:** substitute the actual on-shell Candidate-C TWO-DUST background into the full Step27 **nonhomothetic common spacetime five-sector action**, including native chart T(t,r),R(t,r) and all lapse/scale derivative transport. Demand first variations/tadpoles of actual shared action vanish, without imposing dust clock constraints before varying. Then construct shared **time-dependent scalar quadratic action**, keep BOTH canonical dust phase pairs, eliminate metric auxiliaries and time-dependent BD-null constraint. From the SAME physical action reproduce finite-H μ→0 De Felice and homothetic nonlinear Aoki K_S,c_S² before attempting relative-μ fold 1 and later cosmological predictions.

**Verdict:** `CANDIDATE_C_DUST_ONLY_HOMOGENEOUS_ON_SHELL_GREEN`; `STEP27_NONHOMOTHETIC_ON_SHELL_STILL_RED`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`. External JHR negative f EH sign tensor-ghost objection remains separate.

---

# JANUS — REPRISE PRIORITAIRE, ETAPE 27 (2026-10-18)

**FIRST READ:** `research/UNIFIED_FIVE_SECTOR_SPACETIME_STEP27_AUDIT.md`.
**One-command reproducibility:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step27.py gate2b-step27-report.json`.

## 27. Real common nonlinear spacetime EH_g + EH_f + HR + 2 covariant dusts (LATEST)

**SIGNIFICANT new structural gate:** there is NOW ONE **off-shell common native-field-space** 2D spacetime integral with five real action densities: positive EH_g and EH_f ADM+GHY, all-beta HR, and two irrotational pressureless covariant dust actions. Same nonhomothetic T(t,r),R(t,r) chart and Jacobians, same exact g/f spherical metric perturbations for ALL terms, same radial/time integration, no double angular factor. Native dust backgrounds separately satisfy rho_g a^3=const, rho_f alpha^3=const, theta_gdot=N_g, theta_f,T=n_f; full coupled gravity background remains OFF SHELL.

The **five independently integrated sector actions** each remain invariant under simultaneous compact DIAGONAL coordinate changes. Under a relative f-native chart displacement EH_g, EH_f, dust_g and dust_f are individually invariant, while **only the HR interaction responds**. The new HR action matches the older independent exact Step26 HR spacetime action at multiple finite chart displacements with factor hr_mass2=0.7. Both native EH lapse/shift specializations reproduce the older independent exact flat spherical ADM density; all native metric components agree with the HR input. At 48-point quadrature baseline 5 pieces are approximately (-0.1013110024,-0.0509346122,-0.8289092689,-0.0044339941,+0.0023538524); total -0.9832350252 (arbitrary dimensionless control). For relative f shift (+.035,-.023), HR alone changes by -1.00718622362e-5; rest remain unchanged to numerical precision.

**Separate exact native dust canonical/Legendre control:** covariant irrotational action -rho sqrt(-g)(g^-1 dtheta dtheta+1)/2 yields p_theta=gamma rho(theta_T-N^R theta_R)/N, Hamiltonian H=N[p²/(2gamma rho)+gamma rho(1+theta_R²/gamma_RR)/2]+N^R p theta_R; on stationary rho it reduces to N p sqrt(1+theta_R²/gamma_RR)+N^R p theta_R. Both native matter momentum/velocity derivatives are positive and rank TWO. This preserves independent pairs in this **native local canonical identity**, NOT an already established common-time canonical reduction on a Candidate-C trajectory.

**ACTUALLY TESTED:** 18 new targeted tests (13 unified sectors, 5 native Legendre) + 57 prior = **75 tests passed**, `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests`. Step27 provenance runner returned exit_code 0/75 passed, workspace_origin **non_git_workspace_reconstruction**, full_repository_regression=false, DeFelice/Aoki NOT_RUN, GATE_2B=OPEN. The six new source/test/runner/audit files have been transferred from the ACTUAL local files and each GitHub blob SHA was compared exactly to local `git hash-object`. **Historical HR/dust prerequisites in this local environment are still algorithm-preserving but not all byte-exact GitHub checkout files.** No full repo/CI or independent review claimed.

**IMMEDIATE SCIENTIFIC RED:** (1) make the now-shared off-shell full action a truly **ON-SHELL Candidate-C** solution satisfying BOTH metric Friedmann equations, HR background and two independent dust conservation and cancel all tadpoles; (2) derive the coherent common-time *quadratic* field/rate Hessian and exact covariant→canonical dust phase pair equivalence, including f chart derivative sampling and compact time boundary terms; (3) eliminate four metric auxiliaries plus time-dependent BD-null variable without dropping either dust pair; (4) pass finite-H mu→0 De Felice and nonlinear homothetic Aoki K_S, c_S² on the SAME reduced physical action. Only THEN assess Candidate-C first fold a≈0.0301646. Never infer physical kinetic signs/ghost freedom from off-shell test Hessians. No JANUS cosmological validity claim.

**VERDICT: FIVE_SECTOR_OFFSHELL_ACTION_GREEN_AS_REGRESSION; GATE_2B=OPEN; JANUS_R_NOT_VALIDATED.** Work only on `research/gate2b-nonhomothetic-transfer`, NOT main/v2-flrw. Preserve separate external JHR tensor ghost criticism.

---

# JANUS — POINT DE REPRISE PRIORITAIRE: ETAPE 26 (2026-10-18)

**READ FIRST:** `research/COUPLED_DIAGONAL_NOETHER_STEP26_AUDIT.md`. The full nonlinear potential, its four-chart Hessian, and reproducible tests are:
- `numerics/hr_coupled_diagonal_ward.py`
- `numerics/hr_coupled_chart_hessian.py`
- `tests/test_hr_coupled_diagonal_ward.py`
- `tests/test_hr_coupled_chart_hessian.py`
- `scripts/verify_gate2b_step26.py`.

**Single command:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step26.py gate2b-step26-report.json`.

## 26. All-five-beta full bimetric diagonal Ward GREEN — OFF-SHELL Hessian caution (LATEST)

**Novel coupled result:** on a genuinely time-dependent nonhomothetic f chart (T=t+sigma(t)r²/2, R_f=[1+mu(t)]r), the exact nonlinear HR potential for ALL five beta0..beta4 coefficients, with full g/f spherical 2x2 metric blocks + angular radii, is integrated over compact time and radial support. Four scalar lapse/shift/trace/shear perturbations per sector are sampled at correctly displaced coordinates. The finite **DIAGONAL** diffeomorphism acting on both metrics preserves the full interaction action to machine precision. A relative f-only native chart displacement gives NONZERO beta1,beta2,beta3 action variations, while beta0 and beta4 remain separately invariant (g volume/f volume controls). This is a true coupled-action Ward test, beyond the earlier f-only EH chart checks.

**Cross-oracle:** the new directly evaluated 2x2 principal-square-root HR density equals `r² * native_hr_stueckelberg_jet(...).value` from the prior independent exact native HR jet at t=0, r=.12,.23,.39. At r=.23 both are -0.0823859285303577. Fully independent g/f coordinate pullbacks agree in diagonal mode.

**Critical observed RED-to-GREEN:** an initial test equated an f-native displacement delta(T,R) to an f displacement delta(t,r) with the same amplitudes; that is WRONG when the background Jacobian is nontrivial. They obey deltaX_f^A=J0^A_mu delta x_f^mu to FIRST order and have different finite expressions. The corrected tests distinguish both charts. A separate positive-orientation check has replaced a placeholder diagnostic. All changed file bytes verified.

**Off-shell Noether/gauge caution:** finite diagonal coordinate paths preserve the action exactly, so their directional first and quadratic second derivatives vanish. But the independent 4x4 g/f chart Hessian H on the arbitrary off-shell background does **NOT** necessarily satisfy H v_diag=0, since the nonlinearly field-dependent Ward generator obeys S_,ij R^j = -S_,j partial_i R^j and the tadpoles S_,j are nonzero. Numerically `||H v_T||~3.0e-4`, `||H v_R||~1.73e-3`, even though direct finite diagonal action changes are ~0. The finite-difference directional `v^T H v` error decays as O(h²), verified. **NEVER infer BD or physical gauge-null eigenvectors from OFF-SHELL raw Hessian.**

**Actual local evidence:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests` => **57 passed** in `/mnt/data/janus-next`. 16 new tests and the 41 prior focused. `scripts/verify_gate2b_step26.py` returned exit 0/57 passed, provenance `non_git_workspace_reconstruction`, `full_repository_regression=false`, `DeFelice/Aoki=NOT_RUN`, `GATE_2B=OPEN`. All FIVE new source/test/runner files byte-identical to live GitHub blob SHA (see audit). Earlier HR/dust prerequisites are still algorithm-preserving local reconstructions, **NOT a clean Git clone** (DNS access blocked); no full repository suite or independent verification.

**IMMEDIATE NEXT RED:** assemble one shared **time-dependent EH_g+EH_f+HR+TWO dust phase** action using the SAME native/common profiles, chart Jacobians, angular density and time-supported boundary terms. Impose one ON-SHELL Candidate-C trajectory and both dust conservations, verify all first-order tadpoles vanish, THEN derive four true metric auxiliary constraints and time-dependent BD-null canonical reduction with both phase pairs preserved. Reproduce finite-H mu->0 De Felice physical scalar plus nonlinear homothetic Aoki K_S,c_S² from the SAME action, THEN test fold 1 a≈0.0301646. If failing, issue negative physical gate; do not invent observational viability.

**Scientific verdict: coupled all-beta diagonal Ward GREEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.** Work ONLY on branch `research/gate2b-nonhomothetic-transfer`; leave main and research/v2-flrw untouched. Separate external JHR opposite-sign EH ghost prepublication audit unchanged.

---

# JANUS — RESTART POINT / CURRENT HEAD: STEP 25 (2026-10-18)

**READ FIRST:** research/EH_CHART_QUADRATIC_STEP25_AUDIT.md.
**Reproduction:** python scripts/verify_gate2b_step25.py gate2b-step25-report.json.
**Code:** numerics/hr_eh_full_scalar_quadratic_chart.py, tests/test_hr_eh_full_scalar_quadratic_chart.py.

## 25. f-Einstein–Hilbert exact spacetime 6×6 chart Hessian: isolated gauge-null directions GREEN (LATEST)

New analytic/geometric result: differentiate the **exact nonlinear full native-scalar Einstein–Hilbert ADM+GHY action** on a compact time/radial common domain with respect to six independent amplitudes (deltaT,deltaR,Phi_f,U_f,psi_f,E_f). The chart variations are compact and vanish at outer boundaries. With all native metric field values AND native derivative jets sampled at their moved (T,R) positions, the resulting 6×6 Hessian has both chart rows/columns zero within ~8.7e-13 finite-difference residual while the native 4×4 metric block is substantial (Frobenius norm ~11.089). The metric block itself stays invariant under a finite compact chart deformation to ~4.63e-12.

Reason: first chart variation of D rho(X) is the total divergence div[rho Cof(J) xi] by the Piola identity; it vanishes on the fixed spacetime boundary. Thus the isolated f-EH sector has no independent chart kinetic terms in this native parametrization. This is a **boundary/Noether acceptance control**, NOT the BD constraint or complete coupled physical action. Freezing metric field sampling breaks the null block decisively (up to ~0.312 mixed residual). A separate HR beta1–beta3 compact radial Hessian retains NONZERO relative chart response (chart Hessian Frobenius norm ~0.22018; metric/chart cross ~0.51215), which turns off when m²=0. Its profile/integration differs: the numbers are NOT physical comparable magnitudes.

**Actual executed local focused tests:** PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests => **41 passed** (32 step24 controls + 9 new step25). The new step25 manifest runner independently reports 41 passed / exit_code 0 / origin non_git_workspace_reconstruction / full_repository_regression false / DeFelice and Aoki NOT_RUN / Gate2B OPEN. Three new source/test/runner blobs EXACTLY match live GitHub; historical HR/dust prerequisites remain local algorithmic reconstructions rather than a clean Git checkout. DO NOT claim full repo or external reproduction.

**CURRENT EXACT RED:** one shared time-dependent, on-shell full EH+HR+TWO-dust action with consistent native/common f metric derivative transport and compact boundary treatment. Demand both background dust conservations and all tadpoles zero; derive true metric auxiliary constraints then time-dependent BD-null reduction preserving both dust canonical momenta. From that SAME constrained action pass (a) finite-H mu->0 De Felice scalar and (b) nonlinear homothetic Aoki K_S, c_S² oracles. Only then test Candidate-C fold 1 a≈0.0301646. Do NOT diagonalize off-shell 6×6, 24×24 or 22×22 as physical kinetic matrices.

**Scientific status: isolated full-scalar f-EH chart quadratic GREEN; Gate 2B OPEN; JANUS-R NOT VALIDATED.** Preserve external JHR opposite-sign EH criticism as a separate audit. Commit ONLY on branch research/gate2b-nonhomothetic-transfer, leave main and v2-flrw untouched.

---

# JANUS — POINT DE REPRISE PRIORITAIRE, ETAPE 24 (2026-10-18)

**READ FIRST:** `research/FULL_SCALAR_EH_CHART_WARD_STEP24_AUDIT.md`.
**New direct executable research:** `numerics/hr_eh_full_scalar_chart_ward.py`, `tests/test_hr_eh_full_scalar_chart_ward.py`.
**Reproduce with:** `python scripts/verify_gate2b_step24.py gate2b-step24-report.json`.

## 24. Full native EH scalar kinematic chart Ward GREEN; physical Gate 2B OPEN (LATEST)

The native f Einstein–Hilbert ADM+boundary density is now calculated **nonlinearly with all four independent spherical scalar channels**: lapse Phi, radial shift U, scalar spatial trace psi and traceless shear E, including the necessary native first/second radial derivatives and time rates. It is pulled into a moving/tilted common chart with the exact time+radius Jacobian. For compact interior chart variations, the full finite-action change is zero and the eight mixed Ward derivatives (4 fields x 2 chart modes) vanish to max ~3.25e-12 under finite differences. All eight controls where field sampling is intentionally frozen instead fail by nonzero amounts (min ~1.10e-5; max ~0.312). A simultaneously excited four-field finite-chart action differs by only ~1.73e-18.

**Crucial independent cross-check:** the NEW native ADM nonlinear density, finite-differentiated on the same native compact scalar field/rate profiles, reproduces the prior **independently implemented exact 6-variable EH quadratic Hessian** from `hr_full_scalar_eh_homothetic.py`, including shift/trace/shear kinetic terms. It separately recovers the old repository's spatially flat native ADM EH primitive.

**Actually executed local suite:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests` => **32 passed** (previous 24 focused + 8 new). New step24 manifest script ran and reported exit 0 / 32 passed / non_git_workspace_reconstruction / Git HEAD null / full_repository_regression=false / DeFelice and Aoki NOT_RUN / Gate2B OPEN. The THREE new source/test/runner files are now byte-identical to live GitHub (see SHA in audit). The existing HR/dust prerequisites are still manual algorithm-preserving reconstructions, NOT a clean complete Git worktree. Do not conflate the 32 focused tests with a full independent regression.

**Scope caution:** the result is a **kinematic change-of-variable identity of the f-native ADM+GHY scalar density**. It does NOT implement the complete EH **chart-perturbation quadratic Hessian** in the same native HR+two-dust action, nor prove the full diffeomorphism constraint algebra. The background remains OFF SHELL. No physical kinetic/gradient/fold conclusion can be drawn.

**NEXT EXACT RED:** derive full f-native scalar EH chart variation with `deltaT,deltaR` and all native metric modes on the SAME time-supported compact basis, including boundary terms and native derivative transport, then assemble true EH+HR+two dust action with on-shell Candidate-C background/tadpoles, eliminate four metric auxiliaries and time-dependent BD-null direction, KEEP both dust phase pairs, and pass both independent physical De Felice `mu->0` finite-H and homothetic Aoki `K_S,c_S²` oracles before testing fold 1 at a~0.0301646. If the action cannot pass, report a negative Gate-2B result, not tuned late matching.

**Research branch ONLY:** `research/gate2b-nonhomothetic-transfer`; leave `main` and `research/v2-flrw` untouched. **GATE_2B=OPEN**, JANUS-R NOT VALIDATED; external opposite-EH-sign JHR critical manuscript audit remains separate.

---

## 23.1 — One-command test/provenance runner (2026-10-18; latest addition)

File `scripts/verify_gate2b_step23.py` was committed and exact SHA verified (Git blob `17c7a7693dfd2ed7f0191d8d22b65345da8f952e`). In a complete Git clone on the active research branch, run:

```bash
python scripts/verify_gate2b_step23.py gate2b-step23-report.json
```

It launches the four precisely scoped pytest files, records test exit code/count, Python version, SHA-256 of relevant sources/tests, git commit/worktree origin where available, and explicitly declares `GATE_2B=OPEN`, `full_repository_regression=false`, `DeFelice/Aoki NOT_RUN`. **ACTUAL local reconstructed run:** `tests_passed_count=24`, `tests_exit_code=0`, `workspace_origin=non_git_workspace_reconstruction`, `git_head=null`. No clean Git clone has been run yet; passing on a future clean clone remains a separate acceptance gate. Research audit: `research/REAL_PROVIDER_AND_EH_WARD_AUDIT_2026_10_18.md`.

**Resume next RED unchanged:** full f-native trace/shear+shift EH chart variation and complete spacetime Ward with time tilt, then on-shell background/two-dust/metric/BD constraints and same-action De Felice+Aoki acceptance before first Candidate-C fold. No final JANUS-R physical validation.

---

# JANUS — CURRENT RESUME HEAD, 2026-10-18 (STEP 23)

**FIRST READ:** research/REAL_PROVIDER_AND_EH_WARD_AUDIT_2026_10_18.md. Code/tests: numerics/hr_eh_spacetime_ward.py; tests/test_hr_eh_spacetime_ward.py; tests/test_hr_full_scalar_eh_two_dust_real.py.

## 23. Real native EH+HR+two-dust integration + independent f EH chart Ward (LATEST)

Previous section 22.1 left the real-provider 24-slot combined action as an UNEXECUTED test. **That test has NOW EXECUTED GREEN**, with the actual HR native Hessian algorithms and both real dust canonical blocks (not a MOCK). Two added real-provider regressions pass: 18/30-point combined radial Hessian/gradient quadrature convergence and m²=0 pure EH+two-dust limit. Independent canonical pairs p_g/Y_gdot and p_f/Y_fdot remain rank 2. The diagnostic gradient is NOT zero (off-shell background), so do not interpret matrix eigenvalues as physical stability.

**Independent NEW f Einstein–Hilbert FLRW spacetime diffeomorphism/Ward control is GREEN:** full ADM native lapse density times complete 2D chart determinant, with time/radial compact displacements and moving native perturbation sampling, integrates to zero mixed variation (~1e-18). If native lapse perturbation sampling is deliberately frozen, nonzero residuals remain (-3.22107248e-4, -2.77619145e-5). Direct finite-displacement action and the repo's native ADM primitive confirm the result. This is a **FLRW lapse-only** control, not the full scalar EH Ward. The two new Ward files were byte SHA-verified against GitHub; direct ADM primitive likewise.

**ACTUAL focused local test run:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests` => **24 passed** (11 direct EH, 2 mock-assisted structure, 4 real-provider integration, 7 f EH Ward). Existing HR/dust prerequisites had to be manually reconstructed from GitHub tool source: **same algorithms but NOT byte-identical to GitHub blobs** (docstrings/formatting were compacted); therefore this is NOT a clean checkout or full branch regression. Actions disabled; DNS blocks clone. Do not combine this 24 count with previous separate-session counts.

**NEW IMMEDIATE RED:** extend the full 6-variable f-native spherical scalar EH (including shift, spatial trace/shear, their derivatives and f-chart perturbation jets) through inclined T(t,r), R(t,r), with full compact TIME integration and EH diffeo Ward. Then same-action on-shell Candidate-C background, both dust conservation laws, metric auxiliary/BD-null reduction retaining canonical pairs, and TWO physical oracles (finite-H mu->0 De Felice plus homothetic nonlinear Aoki K_S,c_S²) before first fold a≈0.0301646. No kinetic/fold/CMB validation.

**Status: REAL-ALGORITHM UNTILTED PARTIAL ACTION GREEN; EH FLRW LAPSE WARD GREEN; GATE_2B=OPEN; JANUS-R NOT VALIDATED.** Continue ONLY branch research/gate2b-nonhomothetic-transfer; leave main/v2-flrw unchanged. Keep external JHR critical manuscript audit separate.

---

## 22.1 — Real provider action integration pending (2026-10-18)

**NEXT UNEXECUTED FULL-PROVIDER TEST:** tests/test_hr_full_scalar_eh_two_dust_real.py has now been committed. It imports the REAL hr_two_dust_preconstraint module and the new native scalar EH assembly and checks 24x24 block addition, both canonical dust momentum-rate entries, the two new g trace/shear rate channels and positive f Planck scaling. Its exact GitHub blob SHA is 3ecbf81ea429d5475e902cde2b24fd7441204126. This test has been syntax-compiled locally, but NOT executed because the full prerequisite GitHub worktree cannot be cloned in this environment; do not count it among the 13 passed tests. **Immediate resume action: reconstruct/fetch all real provider modules, RUN this test, fix any actual failure, and record full evidence before extending the chart.**

---

# JANUS — restart checkpoint HEAD (2026-10-18, step 22)

**FIRST READ** research/FULL_NATIVE_SCALAR_EH_UNTILTED_AUDIT.md, then numerics/hr_full_scalar_eh_homothetic.py and tests/test_hr_full_scalar_eh_homothetic.py.

## 22. FULL NATIVE SCALAR EH WITH TWO SECTORS ON AN UNTILTED CHART — LATEST

NEW GitHub files:
- numerics/hr_full_scalar_eh_homothetic.py
- tests/test_hr_full_scalar_eh_homothetic.py
- numerics/hr_full_scalar_eh_two_dust_untilted.py
- tests/test_hr_full_scalar_eh_two_dust_untilted.py
- research/FULL_NATIVE_SCALAR_EH_UNTILTED_AUDIT.md

The native Einstein–Hilbert ADM spatial scalar action now retains BOTH trace and traceless shear of each metric, including their independent temporal rates, intrinsic spherical 3-curvature and extrinsic curvature, in addition to native lapse/radial shift. An exact 6-variable analytic quadratic Taylor jet was checked against an independently written nonlinear spherical ADM density and previous flat-spatial EH limit. The two-metric 24-slot compact spatial projection is valid only on an UNTILTED chart T=t, R_f=(1+mu)r, mu constant.

**Important RED-to-GREEN issue:** f spatial shear potential requires E_f,native=(1+mu)^2 E_f,common and the same scaling for E_f,dot, while f radial shift B_f,native=(1+mu)B_f,common. A cross-HR/EH physical metric shear matching test exposed the missing m² scaling; code corrected. Radial-coordinate rescaling then passes after consistent field redefinition.

**Actual local test evidence:** 13/13 tests PASS in newly created /mnt/data/janus-next. Eleven directly test EH; two use a **MOCK** of the existing HR+two-dust provider to check wrapper structure. The actual combined full 24-slot action has NOT been numerically exercised with the real HR/dust provider in this fresh workspace. Previous 47 targeted test results are historical from a separate session, not re-run; never claim 60 new tests passed. All four newly tested source/test files have exact GitHub blob SHA matching the local bytes (in audit).

**Next immediate RED:** get the actual full 24-slot combined native EH+HR+two-dust provider to run on a single verified workspace, THEN extend EH to nonhomothetic sigma/mu_dot chart with f-native second derivative and chart variation/compact time support. Verify full f EH diffeomorphism Ward. Tie to on-shell Candidate-C, then constraints/BD reduction retaining both dust phase pairs, and reproduce both De Felice and Aoki physical limits before fold.

Scientific result is strictly NATIVE_FULL_SCALAR_EH_UNTILTED_GREEN, GATE_2B_OPEN; full JANUS cosmology is NOT validated. Keep main and research/v2-flrw untouched, work ONLY on research/gate2b-nonhomothetic-transfer.

---

# JANUS — authoritative restart head

## 21. 2026-10-18 — native-flat Einstein-Hilbert interface (CURRENT)

**START HERE:** research/FLAT_EH_HR_TWO_DUST_BRIDGE_AUDIT.md; numerics/hr_flat_eh_two_dust_bridge.py; tests/test_hr_flat_eh_two_dust_bridge.py.

A restricted 22-amplitude EH+HR+two-dust partial Hessian now includes BOTH positive Einstein–Hilbert native lapse/radial-shift ADM blocks evaluated on the same regular compact radial profile as finite-mu HR and two independently preserved dust canonical pairs. The f-native shift radial derivative uses the full inverse chart, producing a B_f-B_f_dot mixed term when the background f-time foliation is tilted. At static g background, the flat ADM shift quadratic integrates to an exact radial boundary.

**ACTUAL local targeted tests:** 10 new tests passed; 47 total tests passed in a reconstructed workspace. Both new source/test files are byte-identical to the exact live GitHub blobs. Independent finite-difference controls required refining a too-large amplitude step 2e-4 to 2e-5; see audit. No full worktree suite or GitHub Actions run.

**CRITICAL LIMIT:** EH spatial traces/shears (psi_g, E_g, psi_f, E_f) and EH relative-chart perturbation columns are MISSING. Thus this is NOT a full EH+HR+dust action; its restricted lapse-shift 4x4 rank 4 does NOT validate the full metric constraints or BD elimination. The background is an off-shell Taylor control, not the on-shell Candidate-C cosmological solution. No ghost/gradient/fold conclusion.

**NEXT EXACT RED:** construct the full native scalar Einstein–Hilbert trace/shear and time/radial chart-variation terms on a single compact spacetime support; test EH diffeomorphism Ward identity, on-shell dust/background tadpoles, metric auxiliary and time-dependent BD-null reductions preserving both phase pairs. Then require both independent physical oracles: finite-H mu->0 De Felice and homothetic nonlinear Aoki K_S,c_S^2. Only then inspect fold 1 a≈0.0301646.

**Gate 2B OPEN. Main/v2-flrw untouched.**


---

# JANUS — authoritative restart head

## 20. 2026-10-18 — finite-mu HR plus BOTH canonical dust phase pairs (NEWEST)

**First read:** `research/HR_TWO_DUST_PRECONSTRAINT_AUDIT.md`, then `numerics/hr_two_dust_preconstraint.py` and `tests/test_hr_two_dust_preconstraint.py`.

New **time-local spatial compact 22x22 partial-action Hessian** combines the validated 16-amplitude finite-mu native HR interaction with two independent canonical dust phase pairs `(Y_g,p_g)` and `(Y_f,p_f)`. The f phase includes the relative time chart variable `q_f=(Y_f-T)F`; all f-native phase gradients are pulled back by the full inverse non-homothetic Jacobian. The f dust momentum is kept dynamical: `H[p_f,Y_f_dot]=-H[p_f,T_dot]`. Both momentum/velocity pairs have rank 2.

**Two actual RED-to-GREEN findings:** (1) the initial new dust implementation doubled `4*pi` in the spherical measure; an independent canonical normalization test failed by precisely `4*pi`; fixed in BOTH sectors. (2) an initial test incorrectly expected the f phase-rate-square block to vanish. The inclined f-native foliation induces a nonzero negative coordinate rate-square from the *native spatial gradient*: `H[Y_f_dot,Y_f_dot]=-4*pi*n_f^3 alpha rho_f(1+mu)^2 int dr r^2 (sigma r)^2 F^2/D`; independently derived and verified, zero when sigma=0. It must not be incorrectly read as a physical ghost before EH/BD constraints.

**Verification:** 10 new targeted tests passed, 37 total tests passed in the reconstructed local workspace; both new file git blob hashes matched live GitHub (see audit). NOT a clean entire repository suite, NOT a physical propagation/fold conclusion.

**LATEST EXACT RED:** include complete native Einstein-Hilbert contributions on THE SAME spacetime compact profiles and common/f-native chart, check tadpoles/IBP and the four metric constraints, then reduce the time-dependent BD null coordinate while retaining both canonical dust pairs. Pass BOTH finite-H mu->0 De Felice and nonlinear homothetic Aoki `K_S,c_S^2` acceptance oracles on this **one** physical action. Fold 1 remains out of scope until both pass.

**Scientific verdict:** `HR_TWO_DUST_PRECONSTRAINT=GREEN_AS_PARTIAL_ACTION`; `GATE_2B=OPEN`. Do not assert JANUS validation. Main and v2-flrw remain untouched.


---

## CURRENT CHECKPOINT — 2026-10-18, compact spacetime beta4 Ward

**Read FIRST:** research/BETA4_SPACETIME_WARD_AUDIT.md.

Four new committed files:
- numerics/hr_beta4_spacetime_ward.py
- numerics/hr_beta4_native_jet_ward.py
- tests/test_hr_beta4_spacetime_ward.py
- tests/test_hr_beta4_native_jet_ward.py

**GREEN only for the off-shell beta4 geometric identity** sqrt(-g)e4(sqrt(g^-1 f))=sqrt(-f) after full compact time/radial integration. Two independent routes agree: direct f-volume variation and the already committed 22x22 native HR jet with coherent native f-field time/radial sampling. If f-field sampling is deliberately omitted, mixed chart/field residuals are nonzero (~+7.13598e-3 and +6.0751e-4 in negative-sign HR jet conventions). Added the f spatial trace factor-3 control and zero linear shift/shear source.

**Actual local targeted verification:** PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests -> 27 passed. The EXACT two existing native HR prerequisite files plus the four new source/test files were matched to live GitHub SHA with git hash-object before final rerun. This is NOT the repository-wide suite (GitHub clone DNS blocked; Actions disabled).

**RED → GREEN incident documented:** while extending field controls the new test harness temporarily reused the field index as the chart-mode loop index, causing four failing tests. Corrected to mode_index; all 27 rerun passed. Do not interpret this diagnostic coding error as physical instability.

**NEXT EXACT RED:** coherent **Einstein–Hilbert + Hassan–Rosen + TWO dust phase** compact spacetime action on an on-shell non-homothetic background. Check beta4 Ward throughout assembly, all boundary/tadpole terms, then four metric constraints and time-dependent BD-null reduction, preserving both dust canonical pairs. Require BOTH the finite-H mu->0 De Felice physical scalar and homothetic nonlinear Aoki K_S,c_S² oracles before any Candidate-C first-fold kinetic/gradient verdict.

**Scientific verdict remains GATE_2B=OPEN; Janus-R not validated.** Preserve JHR external manuscript critical audit as a separate line. Work ONLY on research/gate2b-nonhomothetic-transfer, not main/v2-flrw.

---

# JANUS Gate 2B — point de reprise prioritaire

Date: 2026-10-18
Active branch: research/gate2b-nonhomothetic-transfer
Scientific status: GATE_2B_OPEN

**Read this file first after an interrupted session.** The larger historical journal is research/GATE2B_LATEST_RESTART.md (sections 1–18); the NEW mathematical details are in research/FINITE_MU_NATIVE_TRANSPORT_AUDIT.md.

## Latest commits/results

- numerics/hr_native_sampling_compact.py — 22x16 profile pullback based on the FULL inverse f-native background chart Jacobian, then finite-radius 4*pi*r^2 integration.
- tests/test_hr_native_sampling_compact.py — 10 targeted tests passed in a locally reconstructed environment.
- research/FINITE_MU_NATIVE_TRANSPORT_AUDIT.md — full derivation, assumptions, tests, limitations, ordered next gates.

The inverse-chart identity is

```text
T=t+sigma(t)*r^2/2,   R=(1+mu(t))*r
D=(1+sigma_dot*r^2/2)*(1+mu)-sigma*mu_dot*r^2>0
q_T=((1+mu)*q_t-mu_dot*r*q_r)/D
q_R=(-sigma*r*q_t+(1+sigma_dot*r^2/2)*q_r)/D
```

An actual RED test caught a missing `1/k` in the derivative of the radial metric shift profile; this was corrected. All 10 new targeted tests pass after correction, including finite quadrature convergence and beta0/beta4 sector separation.

**NO physical kinetic or dispersion conclusions follow**: these 16 trial action slots are not the historical 16-dimensional physical pre-metric De Felice state, and the four f-native perturbation amplitude rates are not independent new propagating fields.

## Exact next RED, in order

1. Assemble a coherent time-supported Einstein-Hilbert + native HR + TWO dust canonical phase actions, using this same common/native chart and regular radial support, including all background and perturbation field transports.
2. Check integration by parts, tadpoles, native f-volume/Noether boundary identity and metric auxiliary block rank.
3. Reduce the four metric auxiliaries and the time-dependent BD null coordinate; KEEP both dust canonical phase pairs dynamical.
4. From the SAME completed action reproduce (a) finite-H Candidate-C mu->0 De Felice physical scalar speed, and (b) homothetic Aoki nonlinear kinetic/gradient K_S,c_S^2 including stable AND unstable branches.
5. Only then approach fold 1 (a ~ 0.0301646) and test constrained kinetic/gradient regularity. Continue with transition/late transfer only if healthy.

## Verification and branch rules

- Last targeted local run: `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_native_sampling_compact.py` -> 10 passed. These tests used locally reconstructed prerequisite sources from the committed implementations.
- Whole repository suite NOT run; clone DNS failure and disabled GitHub Actions.
- Keep main and research/v2-flrw untouched; commit on research/gate2b-nonhomothetic-transfer.
- Keep an explicit FAIL/OPEN verdict if the two physical acceptance oracles fail, rather than claiming JANUS validated.

## Parallel audit — external SJHR note, 2026-10-18

**Mandatory reading before external scientific circulation:** `research/JHR_EXTERNAL_PREPUBLICATION_AUDIT_2026_10_18.md`. The corresponding executable tests are `tests/test_jhr_prepublication_gates.py` (4 targeted tests passed in a reconstructed local workspace).

The externally supplied 2026 JHR action is **not** the ongoing positive-kinetic JANUS-R continuation. The source note's *negative* f Einstein–Hilbert sign creates an indefinite common-time TT kinetic form if both couplings are positive. The HR BD constraint does not repair this tensor kinetic sign. The stellar Noether numerical sum cancellation does not establish each separate metric Bianchi constraint, the stated 1 meV strong-coupling scale is incompatible with m~1e-32 eV under the displayed Lambda3 formula, and the apparent CMB third-peak fit is a tunable forced-oscillator output rather than a predicted C_ell.

**Publication gate: external JHR as written FAILS current validation. Do not present as proven.** Keep this audit distinct from Gate 2B, which remains OPEN.
