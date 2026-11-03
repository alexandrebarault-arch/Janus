# JANUS — b3c3d9 preliminary classifier malformed interval guard (2026-11-03)

Scientific status: GATE_2B OPEN; JANUS_R NOT_VALIDATED.

At session start main was fd857c71e0fbc32ff5d32bff97c4252dc2def48c. The latest checkpoint required testing the corrected interval verifier and attempting physical Step55/58 cells.

A separate logical defect was found in classify(a_n,a_m): before this change, reversed boxes such as A_N=[2,1], A_M=[-3,-1] could receive CERTIFIED at the per-cell classification stage, because only the lower A_N and upper A_M endpoints were checked. The downstream certify_cover already rejected malformed endpoints, so this defect did NOT establish a false full-domain certificate. It could, however, inflate the intermediate certified_cells count and label invalid rows CERTIFIED.

Fix: classify now returns INCONCLUSIVE whenever either box has lo>hi, before testing signs. New regression cases cover both reversed boxes and a valid box. Five isolated exact-Fraction classification assertions were executed in the local Python environment and passed. The full repository regression suite and physical Step55/58 computations were NOT executed: git ls-remote failed with 'Could not resolve host: github.com'; the local runtime does not contain the complete repository. These five isolated checks must not be presented as full repository tests or physical evidence.

Files changed: numerics/hr_b3c3d9_annular_direct_enclosure.py and tests/test_hr_b3c3d9_annular_direct_enclosure.py. This audit and checkpoint/index updates document the limitation. Next: run the full patched 9-test suite from a complete checkout; validate source/blob identity; run authentic Step55 barrier and the --cells 256 --max-cells 1 pilot; then all 256 cells if justified, checking jets, box endpoints, and coverage. Center, both temporal boundaries, Dirac/charges, 4D, stability and observables remain open.
