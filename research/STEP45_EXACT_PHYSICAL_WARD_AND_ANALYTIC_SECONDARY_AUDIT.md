# JANUS Gate 2B — Step45: EXACT physical Ward identities and finite-difference-free secondary

**Date:** 22 October 2026. **Active branch:** `research/gate2b-nonhomothetic-transfer`. This investigation also incorporates the brief preexisting `research/STEP45_CHECKPOINT.txt` committed as `e960f774` by another session. That checkpoint only recorded the Ward identities without executable source. The present work independently rederived them directly from the original six-pair reduced ADM+HR+two-dust Hamiltonian densities, published the actual executable proof/test source, and advanced to an exact rational-interval countercheck of the frozen Step41 secondary. **Gate 2B OPEN; JANUS-R NOT VALIDATED.**

## 1. Exact original spherical action density, not a fabricated Ward kernel

Use the original file `numerics/hr_curved_primary_mixed_kernel.py` (Git blob `45ccd73177cc1588efaf1d53e3dd0179d41ec30b`). After the original radial integrations by parts the independent lapse Hamiltonians have density

\[
F_g[N]=N A_g+N'B_g,\qquad F_f[M]=M A_f+M'B_f.
\]

The complete expressions `A_g,B_g,A_f,B_f`, including both positive Einstein–Hilbert sectors, all five \(\beta_n\), **both** moving canonical dusts and the algebraic shift \(z,z'\), are reconstructed exactly in `numerics/hr_step45_exact_physical_ward.py`. Each of TWELVE independent canonical fields \(q_i\) has first and second radial jets, and \(z,z',z''\) are kept as independent external jet coordinates for the initial functional variation. No curved initial-data fit is assumed to derive the identities.

For any first-order density \(N A(q,q')+N'B(q,q')\), the three functional Euler jets multiplying \(N,N',N''\) are exactly

\[
E_0^a=\partial_{q_a}A-\partial_r(\partial_{q'_a}A),\quad
E_1^a=\partial_{q_a}B-\partial_{q'_a}A-\partial_r(\partial_{q'_a}B),\quad
E_2^a=-\partial_{q'_a}B.
\]

Compute all **nine** mixed Poisson coefficients \(K_{ij}=\sum_{\text{6 pairs}}(E^q_{g,i}E^p_{f,j}-E^p_{g,i}E^q_{f,j})\) exactly, with derivatives over ALL canonical jets. SymPy `cancel/together` produces strict symbolic zero for each of NINE distinct residual identities (including the shift algebraic stationarity identities), **not numerical near-zero**.

## 2. Exact physical Ward result

The symbolic identities (where denominators \(L_g,L_f\) and dust/shift square-root domains are regular) are

\[
K_{02}=K_{12}=K_{21}=K_{22}=0,
\qquad
K_{11}=K_{20}=\frac{2M_g^2 S_g S'_g z}{L_gL_f}.
\]

Define \(H_g=A_g-\partial_r B_g\), i.e. the original unsmeared curved g-lapse Hamiltonian density, \(C=K_{00}-\partial_rK_{01}\), and \(W=K_{01}-K_{10}+\partial_r K_{20}\). The exact **off-primary-surface** identity is

\[
\boxed{W=\frac{z H_g}{L_f}}.
\]

This is stronger than claiming \(W=0\) numerically: it vanishes **EXACTLY ON \(H_g=0\)**. With compactly supported independent smearing functions \(N,M\), the exact bracket identity is

\[
\{H_g[N],H_f[M]\}
=\int dr\,N\,\Big[C\,M+(WM)'\Big]
\]

after using the proven high-jet and \(K_{11}=K_{20}\) identities. On the primary \(H_g=0\), it reduces to \(\int N C M\), under the stated regular chart and boundary assumptions. This proves an exact **STRUCTURAL WARD REDUCTION IN THIS SPHERICALLY REDUCED MODEL**, not \(C=0\), the full Dirac algorithm or general 4D degrees-of-freedom counting.

The relative shift stationarity identities are also exact:

\[
F_z=D_g-\frac{Kz}{\sqrt{1-z^2}},\qquad
\frac{\partial H_g}{\partial z}=\frac{F_z}{L_g},
\qquad
\frac{\partial H_f}{\partial z}=\frac{F_z}{L_f}.
\]

They justify *the first functional variation* with the relative shift held external on the algebraic shift shell \(F_z=0\). They do NOT demonstrate its second-order Dirac rank or arbitrary time evolution.

## 3. New analytic, no-finite-difference local secondary \(C\)

The exact program computes **all** \(K_{ij}\), builds \(C=K_{00}-\partial_rK_{01}\) by formal differentiation over the twelve canonical first and second jets and \(z,z',z''\), and simplifies it.

**New result:** all SECOND spatial canonical jets \(q''\) and \(z''\) cancel IDENTICALLY from the simplified exact \(C\). It is an explicit algebraic expression in \(q,q',z,z'\) and couplings only. The expression remains **NONZERO off-shell**; no proof of a continuum secondary-satisfying profile has been produced. This precise formula removes the finite-\(h\) differentiator of Step37/39, opening the next analytically controlled ODE or algebraic construction.

## 4. Frozen Step41 high-order collocation profile is rigorously NOT exactly secondary-constrained in a specified arithmetic model

The second new program `numerics/hr_step45_secondary_point_certificate.py` uses the published nine Step41 even-generator correction coefficients, with each frozen binary64 coefficient mapped to an **EXACT** rational using `Fraction.from_float`. Benchmark model decimal inputs (e.g. \(\beta_n,a,y,c_g,c_f,m^2\)) are separately interpreted as exact terminating **DECIMAL RATIONALS**, consistently with earlier Step38/40/42 interval certificates. The original curved two-dust primary reconstruction at fixed rational \(r\) uses exact rational arithmetic; every square root is bounded outward using integer `isqrt` at grid \(10^{-70}\). The symbolic no-finite-difference \(C\) is then evaluated by a second independent recursive rational interval-expression evaluator; no floating tolerance or numerical derivative enters the mathematical **sign** decision.

At six rational radii, the exact interval excludes zero:

| \(r\) | Strict sign of frozen \(C(r)\) | Decimal display (not proof) |
|---|---|---:|
| 0.11 | positive | +1.6499669319600964e−14 |
| 0.21 | negative | −1.3518654702078266e−13 |
| 0.43 | positive | +5.179207281993937e−13 |
| 0.71 | positive | +1.8478837243471333e−12 |
| 0.83 | positive | +5.021130792732132e−11 |
| 0.85 | positive | +6.554528852343134e−11 |

**Especially at \(r=17/20=0.85\), a mathematically certified outward decimal rational enclosure is:**

\[
\boxed{6.5545288523431\times10^{-11}
<C_{\rm frozen}(17/20)
<6.5545288523432\times10^{-11}.}
\]

The actual exact `Fraction` intervals are orders of magnitude narrower. The machine report stores rational **outward** endpoints at \(10^{-24}\) precision for each radius, and the Python function prints full exact endpoints.

Consequently **the archived, finite-degree, numerically corrected Step41 initial-data profile is NOT an exact solution of \(C(r)=0\)** in this explicit rational benchmark interpretation, despite extremely small discrete residuals. This is an actual **falsification of the claim that this specific frozen approximation exactly meets the secondary**, *not* of the existence of a different, exactly secondary-constrained solution, and not a no-go for the broader theory.

**CAVEAT (critical for honest provenance):** The underlying ORIGINAL Step33g Python code used ordinary binary64 intermediate arithmetic, including `math.sqrt` and SymPy `sp.Float`. The rigorous interval theorem instead rationalizes input printed benchmark decimals and encloses their algebraic square roots. Thus it applies EXACTLY to that consistently defined rationalized benchmark, and cannot be silently characterized as a rigorous bound on each instruction of the historical binary64 execution. The historical numerical Step44 benchmark \(|C(.85)|\approx6.55\times10^{-11}\) agrees closely, but the source-semantics interval extension is still to do. With positive dusts and regular center, this is a strong controlled **near-solution** obstruction, not a cosmological viability theorem.

## 5. Executable, byte-identical GitHub source and tests

Four new committed files; the exact Git blob SHA-1 of each **actually executed local source and test** matches its GitHub file:

- `numerics/hr_step45_exact_physical_ward.py` — `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
- `tests/test_hr_step45_exact_physical_ward.py` — `64c32464df011e87c11e7ca7ff0d9d101bb167aa`.
- `numerics/hr_step45_secondary_point_certificate.py` — `6ab94dacb0c6429bdce8d71311161a6b76ecc0e6`.
- `tests/test_hr_step45_secondary_point_certificate.py` — `d2c04e5961cfb31867ea40b8d003c8e35ced9eb8`.

Verified from `/mnt/data/janus-step45`:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step45_exact_physical_ward.py \
  tests/test_hr_step45_secondary_point_certificate.py
# ACTUALLY EXECUTED: 24 passed in 1.30 seconds.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step45_exact_physical_ward
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step45_secondary_point_certificate
```

Exact tests check all six pairs and nine \(K_{ij}\), four high-jet zeros, off-shell \(K_{20}\) formula and \(K_{11}\) relation, nontrivial primary-proportional \(W\), shift stationarity, analytic \(C\) independent of second jets, and negative guard on zero \(L_f\) domain. Pointwise certificates test all six signs, strict exact endpoint bounds, positivity of source correction-ball coefficient membership, shift constraint \(F_z=0\) enclosed at the endpoint, rational square-root enclosure and invalid-domain guards. **These are TARGETED, standalone tests** of new symbolic algebra and reconstructed benchmark; the full repository tests, a true evolved JANUS solution and full Dirac preservation were not executed. GitHub workflows stay disabled.

## 6. Next genuine physical red — Step46

1. Treat the explicit algebraic \(C(q,q',z,z')=0\) as an **exact differential/algebraic equation for one free radial canonical datum** (e.g. \(p_{L_f}\) or its generator), with simultaneous exact primaries, positive 2-dusts and regular centre. Solve it over a nontrivial curved, noncomoving radial interval or derive a rigorous obstruction. Preserve the exact Ward reduction on \(H_g=0\). A finite polynomial collocation approximation cannot count as exact.
2. Independently validate that solution and the \(z\)-eliminated original source action, including on-shell boundary conditions. If targeting historic binary64 reproduction, prove a certified enclosure of its evaluation semantics separately instead of conflating that with rationalized calibration.
3. Then compute the **time preservation of the secondary** \(\{C(r),H_{\rm tot}\}\) with all SIX canonical pairs, full Dirac matrix rank and lapse fixing including exceptional \(J/K\) branches and spherical centre.
4. Only after that: genuinely nonhomothetic on-shell evolution, same-reduced-action De Felice finite-H mu→0 and Aoki nonlinear \(K_S,c_S^2\) healthy/unhealthy oracles, Candidate-C fold and observational implications.

**FINAL: exact spherical physical Ward reduction CONFIRMED; analytic no-stencil C DERIVED; frozen Step41 near-solution NOT exact in a rigorous rationalized benchmark; exact C-satisfying continuum solution, preservation and lapse fixing OPEN. Gate 2B OPEN; JANUS-R NOT VALIDATED.**
