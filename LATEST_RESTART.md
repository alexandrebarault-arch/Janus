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
