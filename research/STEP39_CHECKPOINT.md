# JANUS — Step39 live checkpoint — 20 October 2026

Research branch: `research/gate2b-nonhomothetic-transfer`. Preserve main and research/v2-flrw. This file is an interruption-safe **verified intermediate checkpoint**; the authoritative `00_CURRENT_RESTART.md` will be advanced after new code/report commit.

## GENUINE byte-for-byte provider reproduction achieved (previous Step37 RED)

Reconstructed under `/mnt/data/janus-step39` directly from the *actual GitHub source text*, with computed local Git blob SHA-1 hashes exactly matching GitHub:
- `numerics/hr_curved_moving_dust_primary.py` = `ee801e324ae0282f764e29c2b39ff34b1efb73f1`
- `numerics/hr_curved_primary_mixed_kernel.py` = `45ccd73177cc1588efaf1d53e3dd0179d41ec30b`
- `numerics/hr_step37_curved_solver.py` = `ce627177d7fa97bad21a7689b292ee24a63930cc`
- `numerics/hr_step37_original_nonibp_oracle.py` = `005449ade6e3582e3b9a5c3374a881a77e73e3f6`
- `tests/test_hr_step37_curved_solver.py` = `01b37200c8c547ff4572dad40a7dd21879160f86`
- `numerics/hr_step38_continuum_gate.py` = `1e4874050d2a8e478cc2414580c737f69cee6309`
- `tests/test_hr_step38_continuum_gate.py` = `cd9a7625c7a62beec0cc952b91d3b929ec1fce96`

Ran FROM ONE AUTHENTIC RECONSTRUCTED WORKTREE:

```sh
cd /mnt/data/janus-step39
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_step37_curved_solver.py tests/test_hr_step38_continuum_gate.py
# 23 passed in 8.97s (no adapter providers)
```

A **full GitHub project clone, complete repository suite and CI were NOT executed**. Numerical source and test dependencies for these two targeted test modules are byte-identical GitHub blobs, not adapters.

## Step39 independent higher-resolution Poisson/IBP data (actual runs)

At Step37 scale=.1, even radial f-momentum degree4, five corrections, fixed Candidate-C a=.4, y=.5787707228025044, two positive canonical dusts; original UNINTEGRATED EH/HR/two-dust six-pair nodal Poisson oracle (`original_pb`) re-executed, with ONLY its local hardcoded maximum `n>1001` raised at runtime for resolution stress. Source mathematical function otherwise unchanged:

| N | original non-IBP bracket after 5 corrections |
|---:|---:|
| 641 | -3.156366756851270e-8 |
| 1281 | -3.8695355253359764e-9 |
| 2561 | +3.053897773552805e-9 |

At N=2561 original discrete primary residual ≈2.0938e-9, *worse* than at N=1281 ≈1.2963e-9, a roundoff-sensitive caution. Two-level Richardson estimates from the above plus earlier historical N=81,161,321 data converge near **+5.361700e-9**, but these are not rigorous error bounds or proof of exact nonzero field-theory secondary.

A SECOND independent compact smooth smearing pair, supported on r∈(.25,.73) rather than (.2,.7), gives original nodal corrected brackets n321 -2.333106762508752e-7; n641 -5.582329845599254e-8; n1281 -1.1451773446191638e-8, uncorrected n641 +0.016721014982276794. Richardson suggests ≈+3.3387e-9.

INDEPENDENT from original nodal discretization, integrate the **actual analytic-IBP local full mixed Kij** (all three lapse jets, all six canonical pairs) against the SAME TWO smooth compact lapse pairs using 48,96,192-point Gauss-Legendre quadrature:
- pair A corrected: +5.361702257197131e-9, +5.361702202418646e-9, +5.361702243120870e-9; baseline +0.009387437474191377.
- pair B corrected: +3.3387069193509795e-9, +3.338706902130900e-9, +3.338706920162197e-9; baseline +0.016721074146539398.

Thus the corrected **SMEARED bracket is demonstrably not at exact zero in these numerical evaluations**, and two computational formulations agree near ≈5.36e-9 and ≈3.34e-9. Nonzero approximate integrated brackets do NOT by themselves characterize the full Dirac algebra or pointwise C(r); exact physical nonzero remains to be rigorously proved. This reveals the **Step37 secondary is an approximation**, as already qualified.

## NEXT ACTION IF INTERRUPTED

1. Commit source + tests for transparent reproducible Gauss lapse-jet oracle and upgraded high-resolution nodal oracle (original cap must be raised WITHOUT modifying earlier historical SHA provenance ambiguously); preserve two independent lapse pairs.
2. Persist machine-readable Step39 report, run tests with authenticated GitHub dependencies and update this checkpoint + `00_CURRENT_RESTART.md` + README.
3. Verify full Dirac SECONDARY PRESERVATION/lapse fixing separately; currently OPEN. Establish exact continuum C(r)=0, positive dust and center regularity before physics/stability claims.
4. NEVER CLAIM JANUS-R VALIDATED. `GATE_2B=OPEN`. External wrong-sign-f-EH JHR critique remains distinct.

**STATUS:** STEP39_23_BYTE_EXACT_TARGETED_TESTS=PASS; STEP39_TWO_SMEAR_CROSS_ORACLE=NUMERICALLY_CONFIRMED; CONTINUUM_EXACT_SECONDARY=OPEN; FULL_DIRAC=OPEN; GATE_2B=OPEN.
