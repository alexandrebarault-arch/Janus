# JANUS — b3c3d9 integrity fix (03/11/2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** This is a report-verifier integrity correction, NOT a Step55/58 physical certificate.

## Exact counterexample to the former verifier

Before the fix, `certify_cover([{'r':['1/4','17/20'],'A_N':['2','1'],'A_M':['-1','-2'],'status':'CERTIFIED'}])` returned True. Both intervals have lower endpoint greater than upper endpoint. A direct Python reproduction of the former function returned `INVALID_REVERSED_BOUNDS_ACCEPTED=True`.

The former verifier only checked `A_N.lower>0` and `A_M.upper<0`, not whether the interval endpoints were ordered. This is a logical defect in report acceptance; it does NOT establish that the interval arithmetic engine itself ever emits inverted endpoints.

## Repair

`numerics/hr_b3c3d9_annular_direct_enclosure.py`: parse both endpoints of each `A_N` and `A_M` box, reject either inverted box, then enforce strict signs. `tests/test_hr_b3c3d9_annular_direct_enclosure.py`: add a regression rejecting both inversions and accepting ordered boxes.

**Verification limitation:** The full repository is not mounted and direct git access fails DNS (`Could not resolve host: github.com`). Only the former function's counterexample was executed locally; the newly published regression suite and Step55/58 physical runner were **not** executed in this session. The GitHub connector can publish/read sources but does not run Python. No physical cell or continuum sign is certified.

## Next step

Run the patched unit suite in a complete checkout, then run `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1`, followed by all 256 cells and an independent verifier of the resulting rational intervals. Investigate interval correlations and jet validity. Centre, temporal boundary conditions and Dirac remain open.
