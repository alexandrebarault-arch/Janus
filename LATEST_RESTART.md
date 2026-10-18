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
