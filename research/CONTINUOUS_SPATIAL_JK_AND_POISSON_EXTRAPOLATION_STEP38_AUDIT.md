# JANUS Gate 2B — Step 38: continuous spatial J/K sign certificate and finite-grid mixed-PB asymptotic audit

**Date:** 20 October 2026. **Active branch:** `research/gate2b-nonhomothetic-transfer`. **Verdict:** restricted mathematical sign gate closed; mixed-bracket continuum zero **NOT DEMONSTRATED**; full Dirac preservation/lapse fixing OPEN; JANUS-R NOT VALIDATED.

## 1. Why Step38 is necessary

Step37 constructed curved, non-comoving, positive-two-dust primary-constrained spherical canonical initial data and used five iterations of a restricted inverse to reduce the numerical local secondary coefficient `C_local=K00-(K01)'` to around `9.58446e-8` on nine off-fit radii. It additionally reported an independent original NON-integrated-by-parts finite-grid Poisson bracket of `-3.15637e-8` at n=641. Neither fact proves the continuum bracket vanishes or that the BD secondary is preserved. Moreover the Step37 test suite was run in a reconstructed environment with **compatibility adapters** for original Step33g providers, NOT one byte-exact complete GitHub checkout. Step38 does not mislabel that provenance gap as closed.

Step38 independently checks two distinct questions:
1. Can J(Sf/Sg) and the spherical algebraic shift coefficient K vanish BETWEEN the finite radial grid points for the exact fixed Step37 metric data?
2. Do the four prior non-IBP grid results extrapolate consistently toward ZERO, or toward a small but finite residual?

## 2. Continuous, EXACT-RATIONAL positivity for fixed Step37 radial geometry

At `a=0.4`, `y=b/a=0.5787707228025044`, `c_g=+0.0015`, `c_f=-0.0012`, and `0<=r<=0.85`, use

```text
L_g = a (1+c_g*r^2)^2; S_g = r*L_g
L_f = b (1+c_f*r^2)^2; S_f = r*L_f
s = r^2
eta(s) = S_f/S_g = y * [(1+c_f*s)/(1+c_g*s)]^2
J(eta) = beta1 + 2 beta2*eta + beta3*eta^2
K(r) = m2*Mg2*L_g*L_f*S_g^2*J(eta)
     = r^2 * m2*Mg2*L_g^3*L_f*J(eta).
```

Here `beta1=1`, `beta2=-4.2383993109`, `beta3=13.6801214252`, `m2=23.3348939346`, `Mg2=1`. Treat every quoted decimal as an exact terminating rational for this CONDITIONAL certificate, not as a claim of exact physical parameter determination.

Let `u_g=1+c_g*s`, `u_f=1+c_f*s`. Throughout s∈[0,0.85²], both factors are strictly positive and

```text
d(u_f/u_g)/ds = (c_f-c_g)/(1+c_g*s)^2 < 0.
```

Hence eta is strictly decreasing and `eta(s)>=eta(0.85²)`. On this interval `J'(eta)=2(beta2+beta3 eta)>0`, certified by its strict rational inequality at the LOWER eta endpoint. Thus

```text
J(eta(r)) >= J(eta(0.85^2)) = 0.6598708967925059... > 0.6.
K(r)/r² >= m2*Mg2*a³*b*(1+c_f*0.85²)^2*J(eta(0.85²))
        = 0.22774976204166372... > 0.
```

The new `fractions.Fraction` module evaluates these endpoint inequalities exactly, with no reliance on 51 radial sample points. The strict K/r² lower bound is valid on the closed stated interval, while `K(0)=0` due to its **coordinate** r² factor. This certificate does NOT prove the physical Dirac constraint matrix remains regular at the spherical center or under arbitrary canonical perturbations. It also does NOT certify the positivity of both dust densities continuously; Step37 only sampled these. A different metric, more strongly curved chart, alternate beta set or time-evolved solution requires a new proof.

## 3. Independent asymptotic analysis of the SAVED original non-IBP bracket

Read **unchanged** four n-point records from `research/reports/gate2b-step37-report.json` (not from the new IBP kernel):

| n | Original uncorrected bracket | Step37 corrected bracket |
|---:|---:|---:|
| 81 | +9.385071811900278e-3 | -2.3602199738792518e-6 |
| 161 | +9.386846507406330e-3 | -5.855849393721080e-7 |
| 321 | +9.387289760635464e-3 | -1.423468184436061e-7 |
| 641 | +9.387400547562790e-3 | -3.156366751300155e-8 |

Because n-1 doubles on each refinement, `dr` halves. Test the *conditional* smooth even-error expansion

`B(h)=B_0+c_2 h²+c_4 h⁴+O(h⁶)`.

The first Richardson transform is `R2=(4 B(h/2)-B(h))/3`; the second is `R4=(16 R2(h/2)-R2(h))/15`. Applying **decimal high-precision arithmetic** to the recorded values gives for corrected data:

```text
R2 at n=161  +5.960072130273267e-9
R2 at n=321  +5.399221865894560e-9
R2 at n=641  +5.364049463866627e-9

R4 at n=321  +5.361831848269313e-9
R4 at n=641  +5.361704637064764e-9
Difference of last two R4 estimates ~1.2721120e-13.
```

The corresponding uncorrected R4 last estimate is `+0.009387437474193680`. The observed ratios of consecutive finite-grid *differences* are compatible with factor four, as expected for leading O(h²) discretization error. The R4 pair is internally stable; this does **NOT** supply a rigorous error bound, since the assumed error expansion, high-order coefficients, original field sampling and IBP equivalence have not been proven by these four data alone.

**Key interpretative correction:** the negative `-3.156e-8` at n=641 cannot be read as a sequence demonstrably converging to zero. The available asymptotic model points instead to a very small **POSITIVE** continuum intercept `~+5.362e-9`. We must not claim this nonzero number has itself been rigorously established; it is a model-dependent extrapolated estimate from the prior data. Most importantly **both an exact and a nonzero physical continuum secondary remain unproved**. The distinction matters because the target is `C_local(r)=0` pointwise, not just a small integrated smeared mixed bracket.

## 4. Executed independent test and provenance

New committed files:
- `numerics/hr_step38_continuum_gate.py`, Git blob `1e4874050d2a8e478cc2414580c737f69cee6309`.
- `tests/test_hr_step38_continuum_gate.py`, Git blob `cd9a7625c7a62beec0cc952b91d3b929ec1fce96`.
- `research/reports/gate2b-step38-report.json` (current interpretation and acceptance matrix).

**Actual local execution** in an isolated reconstructed `/mnt/data/janus-step38` workspace:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_step38_continuum_gate.py
# 11 passed in 0.08s
PYTHONPATH=. python numerics/hr_step38_continuum_gate.py
```

Both executable source/test Git blobs were compared against the actual bytes executed and then matched the GitHub fetched blob SHAs. This workspace contained a **minimized Step37 JSON fixture** carrying the exact same four bracket records and OPEN verdict as the real GitHub file; on the full repo the module reads the full original report path automatically. The live historical Step37 provider modules and original non-IBP bracket have NOT been re-executed; no whole-repository regression, enabled GitHub Actions, or external replication is claimed.

## 5. Step39 mandatory RED gates, in order

1. Reconstruct a coherent worktree from the EXACT live GitHub source bytes, including the original unmodified Step33g `hr_curved_primary_mixed_kernel.py` and extended `hr_curved_moving_dust_primary.py`, then run Step37 tests + Step37 standalone report generator and Step38 tests in that same workspace. The current hosted runtime cannot fetch GitHub source via ordinary shell DNS; the GitHub connector verifies the committed sources but does not execute them.
2. Re-run the ACTUAL independent non-IBP bracket for n≥1281 (after redesign of O(12*n²) implementation so this is feasible), several smearing pairs, and **compare independently to the integrated local C profile**. Verify the extrapolated nonzero intercept and separate finite radial step h contamination.
3. Establish a genuine continuum local C(r)=0 (or demonstrate failure) with well-conditioned radial spectral/interval bounds and TWO positive dust charges; distinguish exact central parity and regularity, boundary conditions and shift chart J/K.
4. Compute the FULL Dirac preservation functional bracket `{C_local,H_T}` and lapse fixing with all six canonical pairs on actual secondary-satisfying data. If this fails, issue a transparent negative model-specific conclusion rather than invoking HR's generic historical BD theorem as if sufficient for this coupled setup.
5. Only thereafter derive a truly nonhomothetic ON-SHELL two-dust background and run De Felice finite-H mu→0 and nonlinear Aoki K_S,c_S² stable/unstable limits on one physical action, before a Candidate-C fold/observational verdict.

**VERDICT: STEP38_SPATIAL_J_K_SIGN=PROVED_CONDITIONALLY; STEP38_PB_EXTRAPOLATION=DIAGNOSTIC; GENERAL_LOCAL_SECONDARY_EXACT=OPEN; FULL_DIRAC=OPEN; GATE_2B=OPEN, JANUS-R NOT VALIDATED.** Keep the independent opposite-EH-sign JHR manuscript audit separate, and leave `main` / `research/v2-flrw` unchanged.
