# JANUS — Step47: numerical curved two-dust radial IVP satisfying analytic secondary on an interior interval

**22 Oct 2026 — `research/gate2b-nonhomothetic-transfer`.** This is a new constrained **INITIAL-DATA** numerical construction; it is neither global `r=0` regularity nor time-evolved Hassan–Rosen/Dirac ghost-freedom.

## 1. Actual new construction

Step45 proved exact spherical physical Ward `W=z Hg/Lf` for all six pairs, and derived `C=K00-(K01)'` with no second canonical spatial jets. Step46 derived the EXACT AFFINE f-momentum equation on the original f primary surface:

[
p'_{L_f}(r)=-rac{C_0(r;p_{L_f})}{C_1(r;p_{L_f})}
]

where

[
C_1=-rac{m^2M_g^2A_tsqrt{1-z^2}}{2M_f^2 S_f}
      rac{L_feta_f}{S'_f B_f}.
]

The Step40–42 positive branch guarantees the coefficient is nonzero on the interior as long as the positive chart/matter conditions persist. Step47 now actually **integrates this ODE** with SciPy `solve_ivp` from `r=.05` to `r=.85`, initialized with the old near-secondary (p_{L_f}(.05)).

At each evaluation, the g gravity/dust phase/metric profiles and the shift `z=.004r` are fixed to the rationalized Step41 curved noncomoving spatial benchmark. The f-dust momentum `p_f` and f angular gravitational momentum `p_{S_f}` are **resolved afresh** algebraically from their original radial ADM primary Hamiltonian and momentum equations, not copied from the old polynomial. Then the algebraic exact-secondary equation determines `p'_{L_f}` and is integrated numerically. No 3-point or 5-point radial finite difference occurs in the ODE.

## 2. Executed numerical result

With `rtol=1e-10`, `atol=1e-14`, maximum RK step `0.02`, 338 RHS evaluations:

| Diagnostic | Actual result |
|---|---:|
| IVP radius interval | [0.05, 0.85] |
| (p_{L_f}(.05)) | −1.3126131492021531e−5 |
| (p_{L_f}(.85)) | −0.0033864293564877215 |
| Minimum sampled (p_g/r²), 33 sites | +0.8856203218885325 |
| Minimum sampled (p_f/r²), 33 sites | +0.11186483299522221 |
| Max analytic primary-substituted |C|, 33 sites | 1.583868705525928e−14 |
| Max original-density |H_g| | 1.1102230246251565e−15 |
| Max original-density |H_f| | 1.3877787807814457e−17 |
| Max original radial-diagonal-momentum residual | 1.3677210405904638e−16 |
| Max original algebraic relative-shift residual | 1.3660947373317356e−16 |

The original spherical ADM positive-EH 3-curvature and kinetic/dust Hamiltonian **densities were independently reconstructed** for the primary residual checks; the original unintegrated **twelve-variable mixed Poisson bracket oracle was not rerun** on this nonpolynomial IVP. The analytic-C substitution residual is nearly machine-small by **construction** and is NOT an independent test of the whole Poisson functional.

An independent solver-tolerance refinement gives endpoint (p_{L_f}(.85)):

| rtol | atol | Maximum step | RHS evaluations | Endpoint |
|---:|---:|---:|---:|---:|
| 1e−8 | 1e−12 | .04 | 158 | −.0033864293564835235 |
| 1e−10 | 1e−14 | .02 | 338 | −.0033864293564877215 |
| 1e−11 | 1e−15 | .01 | 590 | −.0033864293564879007 |

Differences (approx 4.20	imes10^{-15}), then (1.79	imes10^{-16}), indicate numerical convergence near the binary64 floor but **are not a rigorous certified global ODE error bound**.

## 3. Reproducibility and actual test provenance

New byte-identical executed GitHub sources:

- `numerics/hr_step47_interior_ivp.py` — blob `c558a827939f2e1fffbfc0290f2b3cc88cb69ef9`.
- `tests/test_hr_step47_interior_ivp.py` — blob `1e64b528bf87142f2d1059ac736b2d4ee7a79de5`.
- Machine summary `research/reports/gate2b-step47-report.json`.
- Full 33-sample raw JSON was actually generated locally at `/mnt/data/janus-step45/research/reports/gate2b-step47-interior-run.json`, **NOT uploaded separately to GitHub**. It can be regenerated with `integrate_interior()`.

From an actual checkout of active branch:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step45_exact_physical_ward.py \
  tests/test_hr_step45_secondary_point_certificate.py \
  tests/test_hr_step46_exact_secondary_ode.py \
  tests/test_hr_step47_interior_ivp.py
# ACTUALLY EXECUTED: 39 PASSED in ~3.94 seconds (12+12+8+7).

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step47_interior_ivp
```

This was a **targeted reconstructed algebraic and numerical code workspace**, using actual source/test blobs of Steps45–47, NOT a whole-repository regression or independently byte-identical original Step33g→44 provider re-run. GitHub Actions/workflows stay disabled.

## 4. Strict scientific limitations and Step48

1. A solver integration converging across `[.05,.85]` does **not** imply existence and uniqueness of an exact (C=0) function throughout this interval with a rigorous bound. An interval ODE method or independently validated Chebyshev enclosure is still needed.
2. Two-dust positivity was **sampled** at 33 radii, not certified continuously along the new IVP (Step40/42 interval proofs apply to the older frozen polynomial family; do not silently transfer them to an arbitrary nonpolynomial ODE solution).
3. Centre `r=0` has not been reached: the exact affine `C_1` may vanish with spherical powers at r→0, requiring an appropriate regularized even-profile equation and centre conditions. No 4D spacetime evolution was calculated.
4. Mandatory independent check: feed the new IVP into the ORIGINAL non-IBP action's six-canonical-pair Poisson bracket, as a sampled/interpolated curved solution, and verify resolution convergence in two independent lapse pairs; also check full finite-resolution Ward gates.
5. The **full secondary Dirac TIME PRESERVATION** ({C,H_{m tot}}), lapse fixing and rank (including K/J exceptional sectors) have not been computed. De Felice and Aoki same-action stability and first fold remain later tests.

**NEXT RED: Step48 independent non-IBP and certified continuous positivity/centre analysis of the IVP; only after exact constrained data, full Dirac time preservation. Gate 2B OPEN, JANUS-R NOT VALIDATED.**
