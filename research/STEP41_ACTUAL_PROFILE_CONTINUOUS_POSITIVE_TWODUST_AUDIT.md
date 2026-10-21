# JANUS Gate 2B — Step41: the ACTUAL corrected Step39 profile inherits Step40's continuous two-dust positivity

**Date:** 2026-10-21. **Active research branch:** `research/gate2b-nonhomothetic-transfer`. **Verdict:** The Step40 continuous positive-dust certificate now applies to the **specific computed Step39 fifth-order near-secondary canonical initial-data profile**. General exact BD secondary, time preservation and lapse fixing remain **OPEN**; JANUS-R is **NOT VALIDATED**.

## Precise previously open question

The Step40 exact rational interval arithmetic proved strict normalized positive two-dust momenta for ALL `0<=r<=0.85` on the curved, noncomoving, two-canonical-dust primary family, for EVERY independently varying correction coefficient `|delta_(2k)|<=1/200=.005`, k=0..4, with odd corrections zero. However, Step40 clearly left OPEN whether the actual iterative high-order corrected profile of Step39 lay in that admissible coefficient ball.

Step41 closes **that exact logical gap**, without confusing the separate exact local-secondary and Dirac-algebra questions.

## 1. Actual corrected f radial momentum coefficients

Recomputed the Step39 `solve_five_point(scale=.1, degree=4, iterations=6, h=.001)` primary+approximate-secondary canonical data on the benchmark

`a=.4, y=b/a=.5787707228025044, c_g=.0015, c_f=-.0012, z=.004 r, theta'_g=.0012 r L_g, theta'_f=-.0016 r L_f`,

and the same original full six-canonical-pair Step33g Poisson functional kernel; baseline Kij at r=.43 was reproduced (K00≈.4111349651, K01≈-.0089443716, K10≈.1149851368, K11=K20≈.0260995945) and the final historical Step39 sample secondary residual exactly reproduced to the printed significant digits.

The free f-momentum `Q_f(r)=P_f+sum_{k=0}^4 delta_(2k) r^(2k)` has the following nine finite binary64 coefficients for powers r^0,...,r^8:

```json
[-0.000021921905214999423,
 0.0,
 0.0015479757723131573,
 0.0,
 -0.000020933708880890434,
 0.0,
 -0.0000001757101536020765,
 0.0,
 -0.0000000029380881416697167]
```

**IMPORTANT numerical array provenance:** the first nonzero coefficient is negative, the **largest absolute** is the r² coefficient `+0.0015479757723131573`, and every odd coefficient is **exactly zero** in the finite-float representation. SHA-256 of canonical compact JSON array:
`bff542954a2ddba0505223d0d08075e3714dcebed23cd3c9012bd67c91d28b2d`.

`numerics/hr_step41_profile_bridge.py` converts each finite Python float to its **EXACT binary-rational** `Fraction.from_float`, checks parity, and checks each of five independent even coefficients against the exact rational limit `1/200`. The resulting exact positive safety margin is

```
1/200 - max(|delta_(2k)|)
= 397991296652400363 / 115292150460684697600
≈ 0.0034520242276868426 > 0.
```

This is not a floating tolerance or appeal to the printed rounded decimal. An adversarial coefficient 0.0050001 is rejected. Binary float literal `0.005` is itself *slightly greater* than exact rational `1/200`, and is correctly **rejected**, while `math.nextafter(.005,0.)` is accepted. This is a deliberate test of the proof boundary, not a physical instability. **Our computed coefficients are safely inside the bound by more than 0.00345.**

## 2. Continuous physical dust positivity now transfers to the specific corrected data

Because the Step40 proven interval certificate covers **every** vector in the independent five-coefficient ball, it covers the EXACT binary64 vector recomputed above. No additional sampled positivity assumption is required:

[
oxed{p_g(r)/r^2 > 0.885,quad p_f(r)/r^2 > 0.039quad orall rin[0,0.85].}
]

The original exact `fractions.Fraction` lower bounds (not their decimal representations) are produced from 256 outward rational subintervals of s=r² by `numerics/hr_step40_twodust_interval.py`. Rounded conservative bound outputs are g≈0.8854472033872441 and f≈0.03930997556977505. The metric family also lies in Step40's exact parameter-uniform spatial curvature box `|c_g|,|c_f|<=.015`, so the corresponding conditional spatial chart bounds are `J(S_f/S_g)>0.5039461792`, `K(r)/r²>0.159689976` throughout.

**Coordinate center:** the canonical radial densities `p_g,p_f` themselves carry the spherical measure r² and vanish at r=0. What is strictly positive **including** r=0 is the continuously extended normalized coefficient `p_i/r²`; the actual momenta are strictly positive for every r>0.

**DO NOT GENERALIZE:** This result covers one fixed curved noncomoving primary ansatz with the corrected f-momentum polynomial of Step39, not arbitrary curvature, gravitational time evolution or a universal HR-JANUS positivity theorem.

## 3. Independent dense NUMERICAL secondary/primary tests: not a continuum theorem

A separate 73-radius check over `0.03<=r<=0.85`, deliberately more extensive than Step39's original nine off-fit radii, gave:

| Control | Value |
| --- | ---: |
| max sampled abs local `C_local=K00-(K01)'` (5-point h=.001) | 6.551957240641393e-11 |
| max sampled abs `C_local/r²` | 9.068452928223382e-11 |
| max abs 4 primary residuals | 3.885780586188048e-16 |
| sampled min normalized g dust | 0.8856073159229202 |
| sampled min normalized f dust | 0.11186483299541422 |

This 73-point result is solely a **NUMERICAL DIAGNOSTIC**. It is independent of the **CONTINUUM** two-dust proof transferred by the coefficient-ball inclusion; it is not a proof `C_local(r)=0` for all r and not the field-theoretic Dirac algorithm. The canonical dust positivity certificate requires no local C vanishing, and the local near-zero C requires no claim of exact positive kinetic matrix.

## 4. Actually executed code, tests and critical provider provenance

New committed files:
- `numerics/hr_step41_profile_bridge.py` Git blob `26f4d5d24069dac469bf449da4c5997db6a15253`.
- `tests/test_hr_step41_profile_bridge.py` Git blob `34fd411dad5bfa87ec30245cff949102a1328731`.
- `research/reports/gate2b-step41-report.json` with all nine f_delta, their compact-JSON SHA, exact safety margin, dense-site diagnostics and explicitly open physical gates.

Actual execution:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step41_profile_bridge.py
# 11 passed in 4.84s — isolated reconstructed /mnt/data/janus_step41/repo
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m numerics.hr_step41_profile_bridge
```

All **NEW Step41** source/test local Git blobs EXACTLY matched the committed GitHub blobs. The local Step39 mathematical primary/Euler/solver module used here was reconstituted from the previously audited formulae and independently reproduced the Step33g reference Kij and the exact-to-reported-precision Step39 final residual; **unlike the Step39 verified run, its older provider source files were NOT byte-for-byte identical to original GitHub provider blobs in this Step41 local execution.** The local Step40 interval proof source was a faithful independent reproduction of its Fraction expressions and returned precisely the published Step40 certified lower-bound floating outputs; it was **not** the authentic Step40 GitHub file bytes. Therefore do not represent Step41 as a complete clean-original-provider GitHub checkout test. Step39 previously passed 32+5 targeted tests on byte-authenticated original modules in separate workers, and Step40 previously passed 35 original targeted mathematical tests separately; they are NOT added into one claimed single run here.

One red test exposed a beneficial **binary64 boundary subtlety** (float `0.005` vs exact rational `1/200`); the test was corrected to require rejection of the rounded-above value, not by relaxing the theorem's limit. Final Step41 11 tests passed. No GitHub CI/workflows; full repository test suite still not executed.

## 5. Next genuine scientific red — Step42

1. **Provenance:** run the 11 committed Step41 tests against the BYTE-IDENTICAL actual Step33g/37/39/40 provider files in one coherent worktree and persist all original provider hashes; do not rely on mathematical adapters indefinitely.
2. **Exact secondary:** derive or validate an analytic derivative of `K01` and systematically establish `C_local(r)=0` on the full radial continuum (not merely 73 points), with proper center/boundary treatment and a convergent/rigorous interval/spectral bound. If no exact solution is possible report obstruction clearly. Having proved primary positive two-dust data is necessary but NOT sufficient.
3. **Time preservation:** on truly simultaneously primary-and-secondary constrained data, calculate the complete functional `{C_local,H_g[N]+H_f[M]+D[\xi]}` including all SIX canonical pairs and derivatives/boundary terms. Establish actual Dirac rank and lapse-fixing function including J=0/K=0 exceptional sectors.
4. **Only then:** genuinely nonhomothetic on-shell background, same-reduced-action De Felice finite-H mu→0 and Aoki nonlinear K_S,c_S² (healthy/unhealthy checks) and physical first-fold/observations.

**VERDICT:** `STEP41_CORRECTED_PROFILE_CONTINUUM_DUST_POSITIVITY=PROVEN_CONDITIONALLY_ON_FIXED_ANSATZ`; `GENERAL_LOCAL_BD_SECONDARY=OPEN`; `DIRAC_TIME_PRESERVATION=OPEN`; `LAPSE_FIXING=OPEN`; `GATE_2B=OPEN`; `JANUS-R NOT VALIDATED`. The separate negative-EH-f-sign external JHR paper audit remains a separate track.
