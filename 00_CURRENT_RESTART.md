# JANUS — AUTHORITATIVE RESTART — STEP40 COMPLETED — 2026-10-20

**ACTIVE RESEARCH BRANCH:** `research/gate2b-nonhomothetic-transfer` ONLY; `main` and `research/v2-flrw` remain untouched.
**READ FIRST:** `research/STEP40_CURVATURE_BOX_AND_TWODUST_INTERVAL_AUDIT.md`.
**CURRENT REPORT:** `research/reports/gate2b-step40-report.json`.
**CODES:** `numerics/hr_step40_curvature_box.py`, `numerics/hr_step40_twodust_interval.py`.
**TESTS:** `tests/test_hr_step40_curvature_box.py`, `tests/test_hr_step40_twodust_interval.py`.

Reproduce from a branch checkout (only these four new Python files need numpy-free pure Python + pytest):

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step40_curvature_box.py tests/test_hr_step40_twodust_interval.py
# GENUINELY EXECUTED: 35 passed in 1.80 s on isolated /mnt/data/janus-step40
PYTHONPATH=. python -m numerics.hr_step40_curvature_box
PYTHONPATH=. python -m numerics.hr_step40_twodust_interval
```

ALL FOUR locally EXECUTED bytes correspond exactly to uploaded GitHub Git blob hashes, as recorded in the Step40 audit+report. Do NOT claim whole-repo suite, enabled GitHub CI, or joint Step39+40 run. Previous Step39 genuinely authenticated test groups were 32+5 separately, not reexecuted today.

## SCIENTIFIC RESULT — CONTINUUM, EXACT RATIONAL, BUT RESTRICTED

1. For EVERY independent spherical conformal curvature `|c_g|,|c_f|<=.015` and ALL r∈[0,.85] at benchmark a=.4,y=.5787707228025044: `J(Sf/Sg)>=0.5039461792087735` and `K(r)/r²>=0.15968997603142235`; the displayed figures are decimal renderings of **exact strict Fraction certificates**. A second uniform background box with a∈[.395,.405], y∈[.5787,.5789] retains J>=.5034934 and K/r²>=.1516989. These bounds concern ONLY the specified conformal spatial metric ansatz; no Dirac degrees-of-freedom result.
2. Exact negative control: antialigned `c_g=+c,c_f=-c` at r=.85 attains algebraic J=0 for c≈.07854905913576 (certified by rational bisection between .07854 and .07856), showing that unrestricted curvature positivity is false.
3. For the ACTUAL uncorrected curved/noncomoving Step37 primary family with two DISTINCT dust phase gradients and nonzero relative shift, exact outward **rational INTERVAL** arithmetic, partitioning s=r²∈[0,289/400] into 256 rational subintervals, proves `p_g(r)/r²>0.885`, `p_f(r)/r²>0.114` for ALL 0<=r<=.85. The canonical radial densities p_i(0)=0 because of r² spherical weight; positivity is strict for r>0 and normalized density remains strictly positive at r=0.
4. Robust perturbation guarantee: for ANY independent coefficients `|delta_(2k)|<=.005`, k=0..4, with all odd corrections ZERO in `Q_f=(pLf)'/(2r(1+5c_f*r²))`, exact interval arithmetic certifies `p_g/r²>0.885`, `p_f/r²>0.039` over the ENTIRE interval. These inequalities are certified even if all five corrections vary adversarially and independently; they do NOT yet establish that the specific Step39 corrected profile has coefficients within this ball. Check first!
5. Independent original unsimplified two-sector Hamiltonian formula was reconstructed in the tests and compared at several radii for baseline and nonzero perturbations. Exact interval pass is NOT based on floating-point sampling.

## NEXT SCIENTIFIC ACTION — STEP41 (HARD RED)

**FIRST:** Reconstruct/check original byte-authenticated Step33g/37/39 providers, RUN `solve_five_point(scale=.1,degree=4,iterations=6,h=.001)` and PERSIST ALL FINAL `f_delta` coefficients (they were missing from Step39 JSON summary), verifying `delta_odd=0` and `max |delta_even|<=.005` exactly with conservative float-to-rational conversion. If within ball, the Step40 theorem extends continuous dust positivity to the actual Step39 high-order **approximate-secondary** profile; otherwise enlarge or replace certificate and report. Do not silently claim this link has been made.
**SECOND:** Derive or cross-verify actual analytic/spectral derivative of K01 and solve local C(r)=0 **as a continuous constraint** with primary, two dusts, shift/center regularity.
**THIRD:** Calculate FULL six-canonical-pair Dirac `{C_local,H_T}` and lapse fixing, including K/J degeneracy. Generic HR background folklore alone is insufficient.
**FOURTH:** Only then physically nonhomothetic on-shell + both same-action De Felice/Aoki controls, Candidate-C fold and observational tests, positive-EH JANUS-R separate from external sign-reversed JHR audit.

**VERDICT: STEP40 CONTINUOUS EXACT RESTRICTED CHART+DUST POSITIVITY GREEN; CURVED EXACT SECONDARY OPEN; DIRAC TIME PRESERVATION/LAPSE FIXING OPEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.**

---

# JANUS — AUTHORITATIVE RESTART — STEP39 COMPLETED — 2026-10-20

**BRANCH TO CONTINUE ON:** `research/gate2b-nonhomothetic-transfer` ONLY. DO NOT modify `main`, `research/v2-flrw`.
**FIRST READ:** `research/STEP39_DUAL_SMEAR_AND_HIGHORDER_AUDIT.md`.
**MACHINE REPORT:** `research/reports/gate2b-step39-report.json`.
**ORIGINAL ACTION CROSS ORACLE:** `numerics/hr_step39_cross_oracle.py`.
**FOURTH-ORDER RADIAL SECONDARY:** `numerics/hr_step39_highorder_secondary.py`.
**TESTS:** `tests/test_hr_step39_cross_oracle.py` and `tests/test_hr_step39_highorder_secondary.py`.
**PREVIOUS:** `research/CONTINUOUS_SPATIAL_JK_AND_POISSON_EXTRAPOLATION_STEP38_AUDIT.md`, `research/CURVED_APPROX_SECONDARY_STEP37_AUDIT.md`.

## LATEST ACTUALLY EXECUTED, EXACT GITHUB BYTES

For the first time, **ALL historical Step33g/37/38 providers and current Step39 source/tests were reproduced with EXACT matching Git blob hashes in ONE coherent /mnt/data/janus-step39 isolated worktree, WITHOUT adapters**. Eleven source/test SHA values and full commands appear in Step39 audit/report. Shell Git clone DNS unavailable, and NOT a complete checkout/full repository suite. GitHub workflows disabled.

Run as TWO SEPARATE pytest processes due all-in-one time/memory issues:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step37_curved_solver.py tests/test_hr_step38_continuum_gate.py tests/test_hr_step39_cross_oracle.py
# independently executed 32 PASSED

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step39_highorder_secondary.py
# independently executed 5 PASSED

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step39_cross_oracle
# independently executed; emits two-smearing IBP Poisson and five-point h scan
```

**IMPORTANT PROVENANCE:** 32+5 = 37 TARGETED PASSES in TWO workers. The combined single-worker attempt TIMED OUT after ~34 dots. A subprocess aggregator also timed out after first group despite second group separately succeeding. Do NOT claim one successful combined 37-test suite. No full GitHub repo test run or external validation.

## NEW SCIENTIFIC RESULT

1. Frozen Step37 h=.001 degree4 five-correction curved two-positive-dust profile: two independent compact lapse pairs A (support .2-.7) and B (.25-.73). Direct original non-IBP six-pair bracket at N up to **2561** vs analytic IBP full Kij lapse-jet Gaussian integral give conditional continuum estimates **A +5.3617022e-9**, **B +3.3387069e-9**. Both methods agree under grid extrapolation, so do NOT call Step37 frozen profile an exact zero-secondary solution. Discrete original primary residual has floating-point roundoff increase at N2561.
2. Re-solving with three-point radial derivative step h halved from .001 to .0000625 yields pair A full-jet bracket **+5.3611625e-9 -> +2.1019511e-11**; local max sampled |C| **9.3489e-8 -> 4.1507e-10**. Strong O(h²) derivative floor explains much of the old residual.
3. New **FIVE-POINT O(h^4)** derivative with six iterations, even-degree4 f momentum generator: at h=.001 max sampled |C_local| ≈**5.02e-11**, pair A full-jet integral ≈**7.91e-14**, pair B ≈**1.32e-13**. Result plateaus under h refinement; may be polynomial fit/roundoff/physical, **NO proof C_local(r)=0 for all r**.
4. Improved 5-point baseline coefficient at r=.43 is **0.471663864165** rather than 3-point h=.005 **0.471665550745** (prior approximate reference had O(h²) bias). Tests explicitly updated instead of forcing agreement with old low-order reference.
5. At sampled radii both independent dust canonical momenta remain positive, exact curved primaries roundoff ≈2.2e-16. Continuous J(Sf/Sg), K/r² positivity for the fixed metric was PROVED at Step38. Two-dust continuous-interval positivity, exact central regularity and arbitrary deformations are NOT certified.

## NEXT HARD RED: STEP40

- Seek exact analytic/spectral radial derivative of K01 (independently check the ORIGINAL EH+HR+two-dust bracket), then degree4→6+ or a convergent spectral solver and direct, interval-wide |C(r)|/r² error and both positive dust bounds. Report a negative obstruction if encountered, do not force exact zero.
- On genuinely simultaneous primary+EXACT secondary data compute field-theory FULL DIRAC TIME PRESERVATION `{C_local,H_T}` across all six canonical pairs and lapse fixing; test K/J exceptional branches and r=0 coordinate factors carefully.
- Only after proving or refuting this: physically nonhomothetic ON-SHELL dynamics, SAME physical action De Felice finite-H mu→0 and Aoki nonlinear K_S,c_S² stable/unstable oracles; then fold and observations.

**VERDICT: STEP39 NUMERIC TWO-ORACLE IMPROVED SECONDARY; GENERAL BD/DIRAC CONSTRAINT PRESERVATION OPEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.** Distinct external sign-reversed f-EH JHR manuscript track unchanged.

---

# JANUS — REPRISE PRIORITAIRE : STEP38 — 20 OCT 2026

**ACTIVE BRANCH ONLY:** `research/gate2b-nonhomothetic-transfer`. Do not touch `main` or `research/v2-flrw`.
**FIRST READ:** `research/CONTINUOUS_SPATIAL_JK_AND_POISSON_EXTRAPOLATION_STEP38_AUDIT.md`.
**SOURCE:** `numerics/hr_step38_continuum_gate.py` (`1e4874050d2a8e478cc2414580c737f69cee6309`).
**TESTS:** `tests/test_hr_step38_continuum_gate.py` (`cd9a7625c7a62beec0cc952b91d3b929ec1fce96`).
**NEW PERSISTED REPORT:** `research/reports/gate2b-step38-report.json`.
**REPRO COMMANDS:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_step38_continuum_gate.py` and `PYTHONPATH=. python numerics/hr_step38_continuum_gate.py` from repo root.

## ACTUALLY COMPLETED AT STEP38

- 11/11 new targeted tests PASS in isolated `/mnt/data/janus-step38` Python workspace (~0.08 seconds); **new source and test Git blobs exactly match the locally executed bytes and the current GitHub source**. The local workspace reused the four exact numerical PB data rows of the Step37 published JSON in a minimized fixture; NOT a full GitHub checkout or Step37 recomputation. The Step37 provider modules were NOT byte-exactly exercised this session, and CI remains disabled.
- **Continuous EXACT-RATIONAL interval proof, fixed Step37 metric ansatz only:** at a=.4,y=.5787707228025044, cg=.0015,cf=-.0012, and **every** radius 0<=r<=.85, J(Sf/Sg)>=0.6598708967925059, and K(r)/r²>=0.22774976204166372. For 0<r<=.85, K(r)>0; K(0)=0 from coordinate r². This is not a proof of central Dirac rank, arbitrary metric variation or continuous positivity of the dust densities.
- **Numerical correction to Step37 interpretation:** from exact four archived original non-IBP mixed-bracket records n=81,161,321,641, two-level Richardson (assumes even h² expansion) estimates **CONTINUUM B0≈+5.361704637064764e-9 after** five corrections and **B0≈+0.009387437474193680 uncorrected**. Two independent R4 windows differ 1.2721120e-13, but this is NOT a rigorous uncertainty bound, does NOT prove exact nonzero B0, and certainly does not prove B0=0. The n=641 negative bracket is affected by O(h²) discretization.
- Neither the exact curved local C(r)=0 **nor** its Dirac time preservation, two-dust lapse-fixing, the fully nonhomothetic Einstein-HR on-shell solution, De Felice/Aoki same-action physical oracles, fold regularity or observations are validated.

## NEXT NONNEGOTIABLE RED — STEP39

1. **REAL-PROVIDER CLEAN REPRODUCTION FIRST:** Assemble a coherent byte-identical GitHub worktree of original Step33g provider modules, modified Step37 builder, Step37 solver/tests and Step38 analyzer/tests; execute actual targeted suites and runner. Current shell DNS cannot directly clone GitHub; do not claim it has been done.
2. Recompute original non-IBP finite-grid Poisson bracket with stronger resolution (n>=1281 after efficiency changes) and at least two unrelated compact smearings; compare extrapolated B0 with integral of independent C_local(r) and derivative-stencil h scans. Reject any false apparent zero.
3. Establish continuous/controlled C_local=0 with certified two-dust positive densities and center/boundary regularity; independently handle J/K exceptional branches. Current Step37 finite points NOT SUFFICIENT.
4. Compute **full six-canonical-pair field-theory Dirac preservation** of secondary and lapse-fixing. If it fails, register the negative result.
5. Only then genuine nonhomothetic on-shell evolution, independent De Felice finite-H mu->0 and homothetic nonlinear Aoki kinetic/gradient oracles on SAME reduced action before first Candidate-C fold.

**VERDICT: STEP38 exact spatial J/K positivity conditional GREEN; Richardson PB limit DIAGNOSTIC only; GATE_2B OPEN; JANUS-R NOT VALIDATED.** The external negative f-EH-sign JHR manuscript audit remains a DIFFERENT project thread.

---

# JANUS — AUTHORITATIVE RESTART — 2026-10-20 — STEP37 (CURRENT)

ACTIVE BRANCH ONLY: research/gate2b-nonhomothetic-transfer. Preserve main and research/v2-flrw.

FIRST READ: research/CURVED_APPROX_SECONDARY_STEP37_AUDIT.md
CODE: numerics/hr_step37_curved_solver.py, numerics/hr_step37_original_nonibp_oracle.py, updated numerics/hr_curved_moving_dust_primary.py
TESTS: tests/test_hr_step37_curved_solver.py
RUNNER: scripts/verify_gate2b_step37.py
COMMITTED REPORT: research/reports/gate2b-step37-report.json

REPRODUCTION in a true, complete branch worktree:
  OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step37_curved_solver.py
  OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step37.py /tmp/gate2b-step37-repro.json

## LATEST VERIFIED

- Curved nonproportional and noncomoving two-dust spherical primary data, nonzero HR shift, two independent positive dust canonical momenta. Even-momentum parity near the center.
- Five iterative corrections applied to the ACTUAL CURVED local mixed Hamiltonian Poisson coefficient C_local=K00-(K01)' after radial smearing derivative cancellation. On NINE off-fit radii, max absolute local C decreases 0.801743553 -> 9.58445952e-8; all primary constraints at those sites have residual <=2.22e-16. Not a rigorous continuous exact solution.
- Independent ORIGINAL NON-IBP nodal six-canonical-pair bracket at 641 nodes decreases +.00938740055 -> -3.15636675e-8, with expected second-order grid residual decrease, not zero to machine precision.
- Real 12 NEW tests PASS (isolated reconstructed /mnt/data/janus-step37); NEW solver, oracle and test source Git blob SHAs match executed bytes. CRITICAL PROVENANCE: Step33g core modules were mathematical compatibility adapters in the fresh local workspace, NOT the literal GitHub original dependencies. Original provider clean regression PENDING. Earlier Step33/35/36 tests were not combined with the 10. GitHub Actions remain disabled.
- Implementation fix: polynomial momentum generator Q_f=(pLf)'/(2r) needs conversion (n+2)/2 to modify pLf/r²; omission caused a spurious residual plateau. Protected by flat controls.
- Parity regular at formal center by ansatz, but fully center-regular 4D evolution NOT SHOWN. Spherical K(r) coordinate factors vanish at r=0, and both positive dust values are NUMERICAL sample checks, not certified interval bounds.

## NEXT EXACT RED — STEP38

1. Run the Step37 test and regeneration runner with BYTE-EXACT real Step33g provider modules in a coherent complete Git checkout; fix any regressions.
2. Test radial fit-degree/h/support convergence and both dust positivity on an entire interval, ideally prove or find exact curved C_local=0. Nine-point near-zero is insufficient.
3. On simultaneous primary+secondary data calculate full Dirac time preservation brackets with ALL six canonical pairs, their rank, and solve the lapse-fixing condition. Handle J(Sf/Sg)=0 and K=0 separately from spherical coordinate r=0.
4. Only after that: genuinely nonhomothetic Einstein-HR two-dust on-shell evolution, same-action De Felice finite-H mu->0 and nonlinear Aoki K_S,c_S² controls, then test Candidate-C first fold a~0.0301646 and physics.

VERDICT: Step37 NUMERICAL APPROXIMATE secondary GREEN; GATE_2B OPEN; JANUS-R NOT VALIDATED. Distinct external wrong-sign-f-EH JHR critique is unchanged.

---

# JANUS — ACTIVE RESTART / 20 October 2026 — Step36 (CURRENT)

**WORK BRANCH:** `research/gate2b-nonhomothetic-transfer` ONLY. Do NOT touch `main` or `research/v2-flrw`.

**READ FIRST:** `research/CONTINUOUS_J_GATE_STEP36_AUDIT.md`
**SOURCE:** `numerics/candidate_c_continuous_j_certificate.py`
**TESTS:** `tests/test_candidate_c_continuous_j_certificate.py`
**REPORT:** `research/reports/gate2b-step36-report.json`

Run targeted reproduction:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_candidate_c_continuous_j_certificate.py
python numerics/candidate_c_continuous_j_certificate.py
```

## What actually ran, and what is new

- Step36 `19/19` targeted exact-rational certificate tests PASS in **isolated reconstructed** `/mnt/data/janus-step36`. Source/test committed Git blob SHA byte-identical to local executed source/test: `375e6c3197fb9d82f19b35c66331bab2675cd506` and `5b2634d0ac8a99915617ba27785b728f03a1ec00`.
- A **continuous conditional algebraic proof**, replacing Step35's 30-point scan: for every DUST-only Candidate-C a∈[0.025,1], there is exactly one calibrated quartic branch root y∈(0.556,2.3), with **J(y)>1/2** throughout. Other quartic roots outside this interval not excluded. Decimal parameters are taken as exact terminating rationals for the proof, not universally exact physics constants.
- Independent 85-step strict rational bisection: at earlier proposed fold a≈0.0301646, y≈1.971261154529 and J≈37.4491969831. **Thus J=0 is NOT a cause of that fold within this DUST-only calibrated background**. This is NOT a kinetic/gradient/constraint regularity or physical fold-crossing verdict.
- **NEW JOINT REPRODUCTION:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_regular_secondary_flat.py tests/test_candidate_c_continuous_j_certificate.py` -> **30 passed in 0.35 s**, one isolated reconstructed `/mnt/data/janus-step36` workspace. All FOUR Step35+36 Python source/test Git blobs match exactly. **Not** a full-repository suite or GitHub CI. The orphaned Step34 checkpoint remains unresolved.

## NEXT HARD RED (Step37) — do not confuse with previous algebraic proof

1. On the earlier exact curved/noncomoving TWO-dust primary family (`numerics/hr_curved_moving_dust_primary.py`) explicitly compute `C_local(r)=K00(r)-(K01)'(r)` from the actual mixed functional Poisson bracket, over a **radial interval**, not only r=.43.
2. Find an independent radial momentum/metric profile satisfying **BOTH** primary constraints, diagonal momentum and regular shift AND `C_local(r)=0` pointwise while BOTH dust densities stay strictly positive. A mere vanishing integrated smear bracket is insufficient. A useful linearized candidate for curvature source S is `delta X(r)=-int_0^r S(s) ds /(A r^3)`, A=m² Mg² a² J/2, ONLY after computing genuine source S and proving center regularity. No curved continuation is solved yet.
3. Then explicitly calculate the FULL Dirac preservation and local lapse-fixing bracket with all six canonical pairs, including curvature terms and `K=0,J=0` exceptional sectors. Distinguish the coordinate center r=0 (spherical r² factors) from physical degeneracy.
4. Finally genuinely nonhomothetic ON-SHELL two-dust Einstein-HR dynamics and **both** same-physical-action De Felice finite-H μ→0 and Aoki nonlinear K_S,c_S² stable/unstable oracles BEFORE first fold, then observational gates if justified.

**VERDICT: STEP36=PASS as restricted algebraic background certificate; GATE_2B=OPEN; JANUS-R NOT VALIDATED.** Opposite-EH-sign external JHR manuscript audit remains separate.

---

# JANUS — ACTIVE RESTART / 20 October 2026 — Step35

BRANCH: research/gate2b-nonhomothetic-transfer. Leave main and research/v2-flrw untouched.

**FIRST READ:** research/RESTRICTED_REGULAR_CENTER_SECONDARY_STEP35_AUDIT.md
**SOURCE:** numerics/hr_regular_secondary_flat.py
**TEST:** tests/test_hr_regular_secondary_flat.py
**REPORT:** research/reports/gate2b-step35-report.json
**REPRO:** OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_regular_secondary_flat.py

## Latest actually executed

11/11 targeted tests passed in isolated reconstructed /mnt/data/janus-step35 (Python with numpy and pytest), using source/test with Git blob SHAs d30281a11d854084270a4f536e24e2dc857d58fc and 6425b1c36c8d7e4401bfffe6dabf4f9b31f58cc6. Whole repository and other prior Step33/34 tests were NOT rerun. GitHub workflows disabled; full clone DNS unavailable.

## Scientific increment

On previously derived Step33f exact flat/comoving, nondegenerate-J local mixed Poisson bracket, C_flat = (m² Mg² a² J/2)*(r³ X)' with X=Pg/(Mg²a)-Pf/(Mf²b). Hence local C=0 implies r³ X=constant; CENTER REGULARITY forces X=0 everywhere. This NECESSITY (not just sufficiency) holds only in this restricted family.

An explicit radially varying positive TWO-dust primary+restricted-secondary witness at a=.4 has pg/r²>=.9, pf/r²>=.124128 on [0,1] for eps=.08; 5 eps cases including -.15 remain positive. Deliberately perturbing Pf separately retains the primaries but violates the secondary. Thirty dust-only Candidate-C points have J>.52; J=0 is an EXCLUDED degenerate relative-shift chart, not proven safe.

## WARNING: orphaned Step34 checkpoint

research/STEP34_CHECKPOINT.txt exists but referenced Step34 audit, test, runner and JSON do not appear in branch tree; only its source numerics/hr_original_discrete_pb.py exists. No new claim that historical Step34 tests can be rerun from this repository.

## HARD NEXT RED

Construct curved/noncomoving primary+LOCAL SECONDARY=0 on continuous radial interval using C_local=K00-(K01)' (not mere integral); preserve positivity of both dust densities, relative-shift K/J nondegeneracy, center regularity. THEN compute Dirac time preservation, full bracket rank and lapse fixing; THEN same-action nonhomothetic on-shell + De Felice/Aoki physical oracles before first fold. Distinct external JHR wrong-EH-sign audit stays separate.

VERDICT: STEP35 restricted rigidity tested; GATE_2B=OPEN; JANUS-R NOT VALIDATED. No physical ghost/gradient/fold/CMB viability conclusion.
