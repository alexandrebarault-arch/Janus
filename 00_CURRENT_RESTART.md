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
