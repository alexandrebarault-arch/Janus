# JANUS — Gate 2B — Step39: AUTHENTIC providers, two-smearing cross oracle, fourth-order near-secondary correction

**Date:** 2026-10-20. **Branch:** `research/gate2b-nonhomothetic-transfer`. **Scientific verdict:** significant numerical controlled near-secondary advance, **not** continuum constraint closure, lapse fixing, or JANUS-R validation.

## 1. Reproducibility provenance: the former Step37 blocker is actually resolved for TARGETED tests

A coherent local `/mnt/data/janus-step39` worktree was **manually reconstituted from the actual connected GitHub files** because shell DNS cannot clone GitHub. All seven pre-existing Step33g/37/38 Python source/test Git blob SHAs and the four newly committed Step39 source/test SHAs were independently computed in the execution filesystem and MATCHED their real GitHub file blob SHAs. Original historical Step33g providers are no longer substituted with compatibility wrappers.

The authentic mixed bracket `K00=.4111349651, K01=-.0089443716, K10=.1149851368, K11=K20=.0260995945` was reproduced at r=.43, along with all prior targeted Step37/38 constraints and tests.

Targeted executable commands on a full checkout, with **two isolated Python processes**:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step37_curved_solver.py \
  tests/test_hr_step38_continuum_gate.py \
  tests/test_hr_step39_cross_oracle.py
# 32 passed in 29.43 seconds; first group standalone succeeds.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step39_highorder_secondary.py
# 5 passed in 10.50 seconds; second standalone group succeeds.
```

Thus **32 + 5 = 37 passes in TWO verified processes**, **NOT** one successful combined 37-test run. The attempted one-process combined suite stalled/time-limited after ~34 dots and was NOT marked successful; a subprocess orchestration attempt similarly timed out after the first 32-pass group although the second passes separately. No GitHub CI or WHOLE-repository suite was executed.

**Exact match Git source/test blobs**:
`numerics/hr_curved_moving_dust_primary.py` = `ee801e324ae0282f764e29c2b39ff34b1efb73f1`;
`numerics/hr_curved_primary_mixed_kernel.py` = `45ccd73177cc1588efaf1d53e3dd0179d41ec30b`;
`numerics/hr_step37_curved_solver.py` = `ce627177d7fa97bad21a7689b292ee24a63930cc`;
`numerics/hr_step37_original_nonibp_oracle.py` = `005449ade6e3582e3b9a5c3374a881a77e73e3f6`;
`tests/test_hr_step37_curved_solver.py` = `01b37200c8c547ff4572dad40a7dd21879160f86`;
`numerics/hr_step38_continuum_gate.py` = `1e4874050d2a8e478cc2414580c737f69cee6309`;
`tests/test_hr_step38_continuum_gate.py` = `cd9a7625c7a62beec0cc952b91d3b929ec1fce96`;
`numerics/hr_step39_cross_oracle.py` = `5b66a1fd416cfa0eaaaef7e43601b6a497b8e8c0`;
`tests/test_hr_step39_cross_oracle.py` = `262adbf265b1cf5c28416501cf94a7e4e9f631c8`;
`numerics/hr_step39_highorder_secondary.py` = `0da008cc7d5810235ad1bd73549ef1ac1957f656`;
`tests/test_hr_step39_highorder_secondary.py` = `acea5b8426dc96ea90a2d0764e5be9d6725c1fd9`.

## 2. Two different lapse smearings: original unintegrated vs independently integrated Euler/IBP bracket

The original Step37 mixed bracket is expanded in the full nine `Kij` lapse-jet coefficients from SIX canonical pairs. Define TWO genuinely distinct compact smooth lapse pairs with `x=(r-L)/(U-L)`:

**Pair A:** support (0.2,0.7); `N=sin(pi*x)^4`, `M=N*(1+0.2*sin(2*pi*x))`.

**Pair B:** support (0.25,0.73); same N but `M=N*(1-0.3*cos(2*pi*x)+0.12*sin(4*pi*x))`.

The module `numerics/hr_step39_cross_oracle.py` computes `N,N',N'';M,M',M''` analytically and integrates `sum_{i,j}Kij N^(i) M^(j)` with Gaussian quadrature at 48, 96 and 192 points. INDEPENDENTLY, its high-resolution original-action oracle perturbs ALL canonical grid components by complex step, re-solves the algebraic HR shift, and evaluates the UNINTEGRATED spherical EH 3D curvature + dust Hamiltonians. These methods have different discretization schemes and no common numerical spatial differentiation of the same reduced expression.

**FROZEN original Step37 profile** (`h=.001`, degree4, five iterations): 

| Pair | Direct original NON-IBP grid values | Gaussian original Euler/IBP full-jet integral (96 points) |
| --- | --- | ---: |
| A | n641: -3.15636676e-8, n1281: -3.86953553e-9, n2561: +3.05389777e-9 | **+5.36170220e-9** |
| B | n321: -2.33310676e-7, n641: -5.58232985e-8, n1281: -1.14517734e-8 | **+3.33870690e-9** |

The original nodal values scale consistently with O(dr²) leading error, with Richardson intercepts converging toward the directly integrated full-jet numbers. For pair A, the 6-grid two-level intercept is near +5.361700e-9. Pair B independent `Kij` integral is about +3.3387069e-9. Both original uncorrected bracket references are nontrivial and POSITIVE: A +0.00938743747, B +0.01672107415. Such numerical agreement is meaningful cross-validation of the original action and Euler/IBP bracket, but is not an exact mathematical interval error bound.

At n2561 the original **discrete** primary residual (~2.09e-9) becomes worse than n1281 (~1.30e-9), evidencing roundoff/second-derivative cancellation limitations. Do NOT assume ever-finer grids monotonically improve every diagnostic.

The frozen Step37 approximate secondary **does not numerically vanish exactly** in either smear pair. This conclusion DOES NOT mean no better or exact secondary-constrained initial data exists.

## 3. Isolate the finite-radial-differentiation floor

The Step37 solver forms `C_local=K00-(K01)'` using central symmetric 3-point radial finite differences with step `h` (O(h²) error). Re-iterate six times while halving `h` to separate radial discretization from physical residual:

| h | maximum sampled |C_local| | Gauss pair A integrated PB | Gauss pair B integrated PB |
|---:|---:|---:|---:|
| 0.001 | 9.3488823e-8 | +5.36116248e-9 | +3.33751144e-9 |
| 0.0005 | 2.3409840e-8 | +1.34034975e-9 | +8.34476682e-10 |
| 0.00025 | 5.8900448e-9 | +3.35146697e-10 | +2.08718202e-10 |
| 0.000125 | 1.5101312e-9 | +8.38458120e-11 | +5.22784215e-11 |
| 0.0000625 | 4.1506698e-10 | +2.10195105e-11 | +1.31670690e-11 |

At every checked iteration/site the TWO dust momenta remain positive and the four primary constraints have max roundoff ~2.22e-16. The leading integrated residual drops almost fourfold under h halving. Hence Step37's ≈5.36e-9 residual in a fixed profile was to a large extent numerical *construction* error from the derivative used to compute its momentum correction. Do not confuse this with an intrinsic obstruction to a true curved secondary.

## 4. Standalone fourth-order five-point secondary derivative and independent Gauss check

**New** `numerics/hr_step39_highorder_secondary.py` leaves historic Step37 solver SHA **untouched** while replacing the numerical derivative of `K01` and `K20` by

`f'(r)≈[-f(r+2h)+8f(r+h)-8f(r-h)+f(r-2h)]/(12h)`,

which is O(h⁴) for smooth profiles. Six radial momentum-preconditioned updates give:

| h | max sampled |C_local| | Pair A full Kij Gaussian PB | Pair B full Kij Gaussian PB |
|---:|---:|---:|---:|
| 0.004 | 5.2805867e-11 | +2.2787386e-13 | +2.2278289e-13 |
| 0.002 | 5.0336034e-11 | +8.7827171e-14 | +1.3683025e-13 |
| 0.001 | 5.0185595e-11 | +7.9111181e-14 | +1.3162937e-13 |
| 0.0005 | 5.0168040e-11 | +7.8407023e-14 | +1.3120753e-13 |

The near-plateau at ~5e-11 is **not** a machine-certified exact zero. It could come from truncating the free even f-momentum generator at degree4, floating-point cancellations, incomplete nonlinear convergence or genuine sources. Critically, the previous Step33g local `C_local(r=.43)` value ~0.47166555 came from a 3-point h=.005 derivative; the more accurate 5-point reference is ~0.471663864165, a difference ~1.69e-6. The new test **correctly updated** this historical finite-step reference instead of forcing agreement with it. This is NOT a discovery that the full Hamiltonian theory was mathematically inconsistent; it is a numerical derivative bias.

Only sampled interior radii and two compact smearing pairs are controlled. Neither a true exact continuum `C_local(r)=0` solution, continuous 2-dust positivity bounds nor the complete non-perturbative Dirac constraint rank/time preservation is established. Gaussian PB below 1e-13 can be a cancellation of positive/negative local residuals and is NOT a proof of local vanishing.

## 5. Exact current reproducibility and NEXT STEP40

The machine-readable report is `research/reports/gate2b-step39-report.json`. For a fresh checkout at this branch SHA, run the TWO separate pytest commands above, then `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m numerics.hr_step39_cross_oracle` to reproduce the 3-point h-scan and dual-smearing Gauss integrals (not the 5-point cases, which have separate tests). The high-resolution unintegrated n2561 is available through `original_nonibp_extended` and has O(n²) runtime and finite-double-precision limitations. Never silently represent archived high-resolution numbers as rerun unless actually executed.

**Next mathematical task, not optional:** derive a direct analytic/spectral radial derivative of `K01` with an independent symbolic/finitary Poisson check; then increase even-polynomial basis degree 4→6+ and systematically check physical positivity and `C_local(r)` on a CONTINUUM radial interval including center. Once a truly secondary-satisfying background exists, compute `{C_local,H_total}` with all six canonical pairs, full Dirac matrix rank and lapse fixing. Do not conflate positive-HR JANUS-R with the separately audited external negative-f-EH JHR manuscript. Only AFTER full closure pursue nonhomothetic on-shell evolution and BOTH same-action De Felice/Aoki physical controls and first fold.

**VERDICT: STEP39 AUTHENTIC TARGETED 32+5=37 PASSES in two processes; TWO SMEARING TWO ORACLES AGREE; FOURTH-ORDER NUMERIC RESIDUAL MUCH SMALLER; GENERAL BD SECONDARY/TIME PRESERVATION OPEN; GATE_2B OPEN, JANUS-R NOT VALIDATED.**
