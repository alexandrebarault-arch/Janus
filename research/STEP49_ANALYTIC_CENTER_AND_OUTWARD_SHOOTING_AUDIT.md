# JANUS — Step49: local analytic regular-center secondary branch and outward Frobenius shooting

**Date:** 22 October 2026. **Only research branch:** `research/gate2b-nonhomothetic-transfer`. **Verdict:** A conditional mathematical local-center existence/uniqueness result has been established for the Step45–46 original spherical six-pair primary-reduced secondary equation, and supported by outward numerical integrations; global continuation and full Dirac time preservation remain **OPEN**.

## 1. The exact regularized original secondary

Step45 derived the full mixed six-canonical-pair spherical ADM/Hassan–Rosen/two-dust local secondary `C=K00-(K01)'` without any radial finite differences, under compact-lapse boundary conditions and external relative shift during the first canonical variation. Step46 imposed the f lapse and radial primaries, eliminated the two f dust canonical momenta, and proved that `C` is **affine** in `P'=pLf'`. Step48 extracted the necessary center coefficient
[
U_0=M_f^2 bleft(rac{P_g}{M_g^2a}-2z_1ight),qquad z(r)=z_1r+O(r^3).
]

Set (s=r^2) and (P(r)=p_{L_f}(r)=r^2 U(s)). A fresh symbolic substitution into the **ACTUAL physical Step45 C formula after Step46 f primary elimination**, not a manufactured Ward kernel, substitutes the full spherical parity pattern
[
S_i=r L_i(s),quad p_{L_i}=r^2 U_i(s),quad p_{S_i}=rV_i(s),quad p_i=r^2ho_i(s),quad z=r z_1(s)
]
with the corresponding regular (r)-parity for derivatives, dust phase gradients and relative-shift density (D_g=r^3ar D_g(s)).

The new SymPy verifier `numerics/hr_step49_analytic_center.py` checks **exactly** that the primary-reduced expression `C(r)/r²` is even under (rmapsto-r), has a finite central limit, and that its central coefficient of
[
W=rac{p'_{L_f}(r)}r
]
is
[
left.rac{partial(C/r^2)}{partial W}ight|_{r=0}
=-rac{m^2 M_g^2 A_*}{2M_f^2 b},quad
A_* =a^2eta_1+2abeta_2+b^2eta_3.
]
When (A_*>0), both spatial metric amplitudes and both matter mass scales are nonzero, this coefficient is strictly nonzero. The implicit equation therefore yields a **locally analytic** (W=G(s,U)), with the exact center identity, for arbitrary nearby (U),
[
G(0,U)=3U_0-U.
]

### Conditional local-existence theorem (not a global cosmological theorem)

Assume that the **prescribed remaining background** g-primary canonical fields, spatial metrics, dust clocks and relative shift are real analytic in (s) at the center and have the explicit regular parities above. Also assume that the lapse-dust denominators, algebraic shift square root, (M_g^2,M_f^2,m^2,A_*,S_f') are nonzero there. These hypotheses hold for the local benchmark chart as far as the explicit algebraic backgrounds and center signs are concerned, but they do **not** assert any time evolution.

Because (P'=r[2U+2s U_s]), the constraint (C=0) becomes
[
2s U_s=G(s,U)-2U
quadLongleftrightarrowquad
s U_s=-rac32(U-U_0)+rac{s}{2}R(s,U)
]
where (R=(G-3U_0+U)/s) is analytic near ((0,U_0)). Writing (w=U-U_0), the exact Volterra equation for the nonsingular branch is
[
w(s)=rac{1}{2s^{3/2}}int_0^s t^{3/2}R(t,U_0+w(t)),dt.
]
For sufficiently small (s), the integral operator is contractive on a small bounded analytic-function neighborhood (its local Lipschitz factor is bounded by (ssup|partial_U R|/5)). This establishes a **unique bounded regular analytic local solution** (U(s)) near (s=0) for such an analytic prescribed background. The homogeneous (U-U_0=C s^{-3/2}), corresponding to (p_{L_f}=C/r), is excluded by center regularity. Coefficient matching gives
[
U(s)=U_0+U_1s+cdots,qquad
U_1=rac15partial_sG(0,U_0).
]

This is a local theorem **within the reduced spherical action and prescribed analytic initial-data family**. It does not establish global continuation to (r=.85), absence of shocks/zeros in denominators outside a neighborhood, four-dimensional spacetime regularity, or the Dirac time preservation/lapse-fixing algorithm. Only a finite numerical estimate of (U_1) is currently available; a symbolic exact closed form is the next useful extension.

## 2. Both central dust coefficients certified strictly positive with EXACT fractions

The same new module implements independent `Fraction` formulas for the original TWO positive-EH spherical ADM lapse primaries at the center. It encloses the positive background (H=sqrt{H^2}) outward using exact rational integer-`isqrt` bounds on a (10^{-50}) grid. The regular `U_0=-2M_f^2b(aH+z_1)` is enclosed accordingly, and both dust source coefficients are checked without any binary64 tolerance.

The exact g normalized dust coefficient is
[
oxed{ar p_g(0)=p_g/r^2=1107/1250=0.8856>0.8855.}
]
The exact f source (ar p_f(0)) is enclosed in a **strictly positive rational interval** yielding
[
oxed{ar p_f(0)>0.1242,qquad
ar p_f(0)approx0.1242700002620524.}
]
The center interaction chart has (J(y)>0.65) (decimal display (approx0.6763833272458436)). Because the analytic local branch and both normalized source densities are continuous, strict center positivity carries to **some sufficiently small neighborhood** (0le r<arepsilon_*). Neither the size of (arepsilon_*) nor positivity on the full interval has been certified.

The exact rational coefficients can be regenerated and independently checked with:
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step49_analytic_center
```

## 3. Outward shooting is far better conditioned than inward extrapolation

New module: `numerics/hr_step49_regular_center_shoot.py`.

The ODE from Step46 is numerically integrated from a **strictly positive** radius (epsilon) to (r=.85), with initial momentum
[
p_{L_f}(epsilon)=U_0epsilon^2
quad	ext{or}quad
p_{L_f}(epsilon)=U_0epsilon^2+U_1epsilon^4.
]
The program estimates (U_1) by an empirical finite-radius Richardson limit of the exact symbolic (pLf') function, obtaining **(U_1approx0.0007897451669079507)**, *not* a mathematically certified exact coefficient. All RHS evaluations use the Step46 analytic formula; no finite difference in (K'_{01}).

SciPy `solve_ivp` was run with rtol=2e−12, atol=1e−18 and max step .012. The reference integration from (epsilon=.001) with (U_1) gives (p_{L_f}(.85)=-0.003386429356487895). The following table shows *absolute differences from that reference*, NOT certified numerical error bounds:

| Starting (epsilon) | Only (U_0epsilon^2) | Include (U_1epsilon^4) |
|---:|---:|---:|
| .05 | 2.90869715e−10 | 9.27253066e−15 |
| .025 | 9.08994017e−12 | 7.06899816e−17 |
| .0125 | 2.84063571e−13 | 1.73472348e−18 |
| .00625 | 8.87831475e−15 | 4.33680869e−18 |

Without the (U_1) term, halving the cutoff reduces this endpoint difference by approximately **32**, consistent with missing (O(epsilon^4)) initial momentum transported outward by the (1/r) homogeneous sensitivity, i.e. an (O(epsilon^5)) endpoint effect. With (U_1), the initial improvement is compatible with an (O(epsilon^7)) effect, eventually limited by binary64 roundoff. This is robust **numerical evidence**, not an interval bound.

At 129 sampled radii on [.05,.85], the reference outward branch has
[
min_{m sampled}(p_g/r^2)=0.8856203218885321,qquad
min_{m sampled}(p_f/r^2)=0.11186483299522024
]
and (max_{m sampled}|C_{m analytic substitution}|approx1.74	imes10^{-14}). The latter is nearly zero **by construction**, and positivity is **only sampled**, not proved continuously outside the analytically controlled center neighborhood.

## 4. Executed tests and source provenance

On the isolated `/mnt/data/janus-step49` runtime:
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step49_regular_center_shoot.py \
  tests/test_hr_step49_analytic_center.py
# 21 PASSED in ~4.41 seconds.
```

All FOUR NEW Python source/test files are byte-identical to their actual committed GitHub blobs:
- `numerics/hr_step49_regular_center_shoot.py` — `ef1316505f03ee030b29b91e0edfaa5e480132cc`
- `tests/test_hr_step49_regular_center_shoot.py` — `2db400a4b41541983dd49a5fab2d4d0777789aa4`
- `numerics/hr_step49_analytic_center.py` — `d570948912885d45a625fa2db31c6a5435b6a654`
- `tests/test_hr_step49_analytic_center.py` — `8f14de90a296f53f372dde4a29fc63149473644b`

**Important provenance limit:** the historical Step45/46/47 dependencies in this isolated local runtime were faithful mathematical reproductions/compatibility adapters, NOT byte-identical full GitHub copies. The new exact parity and center positivity formulas derive from their originally published canonical symbolic densities, but this is **not a clean full original-provider regression**. The TWO Step48 tests previously deselected pending a coherent five-original-provider checkout are still PENDING. No full repo suite and no GitHub Actions/workflows were run. The local detailed JSONs are `/mnt/data/janus-step49/step49-local.json` and `/mnt/data/janus-step49/step49-center-theorem.json`; their essential content is retained in `research/reports/gate2b-step49-report.json` and reproducible with the new sources.

## 5. Highest-priority next scientific gates — Step50

1. **Source-authentic regression:** fetch full original Step45,46,47 source bytes into ONE coherent worktree, run both Step48 formerly deselected tests and Steps49's 21 tests without mathematical adapters. Save actual SHA hashes and failures; do not claim this is done until verified.
2. **Certified global continuation:** use a truly interval-validated ODE method or rigorous Chebyshev barrier to continue the analytically center-regular (U(s)) through (s=.85^2), bound numerical error and strictly positive normalized TWO dusts across the entire new nonpolynomial solution. Also prove that all required chart denominators remain nonzero.
3. **Full Dirac:** only with constrained admissible data derive and compute ({C,H_{m total}}) for the original SIX canonical pairs, determine true lapse fixing and constraint rank, exceptional (J/K) branches and boundary contributions. Do not infer ghost freedom from spatial Ward identities or center existence alone.
4. Then and only then pursue truly nonhomothetic on-shell cosmology, same-action De Felice/Aoki controls, Candidate-C fold and empirical tests. Keep the externally audited opposite-sign-(f)-EH JHR manuscript separate.

**SCIENTIFIC VERDICT: Step49 regular-center SECONDARY has a conditional unique analytic local solution for analytic prescribed backgrounds, with exactly positive TWO dusts at the center. Numerical outward shooting is strongly consistent through [.001,.85], but globally certified dynamics and Dirac time preservation are OPEN. Gate 2B OPEN; JANUS-R NOT VALIDATED.**
