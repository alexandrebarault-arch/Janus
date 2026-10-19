# JANUS Gate 2B — Step 32c: restricted four-auxiliary Schur and its limits

**Date:** 2026-10-19. **Research branch:** `research/gate2b-nonhomothetic-transfer`.

**Verdict:** `RESTRICTED_FOUR_AUXILIARY_GALERKIN_SCHUR_GREEN`; `TWO_DUST_CANONICAL_PAIRS_GREEN`; **`TRUE_METRIC_ADM_AND_TIME_DEPENDENT_BD_CONSTRAINTS_OPEN`**, **`GATE_2B_OPEN`**. This is an algebraic diagnostic and is **NOT** the constrained physical scalar kinetic matrix.

## Question actually answered

Step 31 constructed one nonlinear time/radial spherical action with positive Einstein–Hilbert for both metrics, all-beta Hassan–Rosen interaction and two dusts on the **radiation-free, physically HOMOGENEOUS on-shell Candidate-C branch**. Step 32a performed exact common-time dust Legendre transforms and retained both `(theta_i,p_i)` pairs. Step 32b added independent local probes of the four EH spatial trace/shear time derivatives. Those 18 amplitudes share the SAME scalar radial/time trial profiles and compact measure.

**Step 32c asks only whether four restricted lapse/radial-shift amplitudes can be stationarized algebraically, whether the calculation converges, and whether that operation preserves both canonical dust pairs.** It does NOT yet ask whether these restricted amplitudes exhaust the genuine ADM constraint/gauge generators.

## Exact matrix operation and assumptions

Using the Step 32b **same positive-EH_g + positive-EH_f + HR + canonical-dust_g + canonical-dust_f action**, numerically differentiate its 18 independent local trial coordinates in the unchanged ordering:

```
Phi_g, U_g, psi_g, E_g, theta_g, p_g, theta_rate_g,
Phi_f, U_f, psi_f, E_f, theta_f, p_f, theta_rate_f,
psi_rate_g, E_rate_g, psi_rate_f, E_rate_f.
```

Choose the **four trial auxiliary coordinates** `(Phi_g,U_g,Phi_f,U_f)` at indices `(0,1,7,8)`; collect all other fourteen trial coordinates in `y`. Partition the symmetric quadratic Hessian:

```
       [ A  B ]
H_18 = [ Bᵀ C ],
Q(x,y) = ½ xᵀ A x + xᵀ B y + ½ yᵀ C y.
```

**If and only if this restricted A is invertible**, the *finite-dimensional quadratic saddle* obeys

```
x_trial*(y) = - A⁻¹ B y,
Q_restricted(y) = ½ yᵀ [ C - Bᵀ A⁻¹ B ] y,
A x_trial* + B y = 0.
```

The code refuses ill-conditioned/singular matrices and compares `np.linalg.solve` with a separate inverse-based Schur calculation. A direct test evaluates the original nonlinear **full five-sector action** along a trial compensated direction and agrees with the predicted quadratic curvature to <0.7% despite nonlinear and finite-step effects. This is a different check from merely recomputing the matrix identity.

**Hessian differencing h=0.012 is intentionally distinct from first-gradient differencing h=2e-5.** Reusing the large Hessian step for on-shell tadpoles would spuriously report a nonzero O(h²) first difference; the new code prevents that failure. Only the legal compact field first variations should vanish on shell. Independent metric-rate or dust-phase-rate **local jets** have nonzero raw first variations and are NOT independently admissible compact variations of globally defined fields.

## Numerical results (dimensionless trial normalization, not observables)

With 20-point Gauss–Legendre quadrature in each time/radial direction and centered Hessian step `0.012`, the restricted 4×4 block is

```
A ≈ [[-2.29594265e-04, -1.20276066e-04,           ~0,           ~0],
     [-1.20276066e-04, +4.73843657e-07,           ~0, -4.24532949e-07],
     [          ~0,           ~0, -8.15570882e-07, -4.27248897e-07],
     [          ~0, -4.24532949e-07, -4.27248897e-07, +3.80364275e-07]]
```

- **Restricted rank:** 4 out of 4, at absolute rank tolerance 1e-11.
- **Condition number:** `545.9152166038742`.
- **Algebraic eigenvalues:** approximately `(-2.80991e-4, -9.52783e-7, +5.14715e-7, +5.18734e-5)`. Their signs **cannot diagnose physical ghosts**.
- **Restricted Schur shape:** 14×14. The retained 14 variables still include independent rate jets; this **does not** count 14 propagating physical modes.
- **Two preserved matter symplectic pairs** `(p_g,theta_rate_g),(p_f,theta_rate_f)` have coefficients approximately `(+9.45033909345e-5,+1.30339269771e-5)` and cross terms below 1e-14. The 2×2 block retains rank 2 and matches independent analytic compact integrals.
- **Metric-rate check:** the original four-rate subblock reproduces Step 32b independent ADM closed forms to around 5e-15 absolute, including nonzero tiny f shear coefficient; this block is still *unreduced*.
- Quadrature 12→20 points stabilizes `A` and the condition number; finite difference 0.012→0.008 gives the expected O(h²) variation. The deliberately restrictive `max_condition=2` guard rejects inversion.
- Exact quadratic substitution `x=-A⁻¹By` yields `Q_18(x,y)=Q_14(y)` to 1e-17 for multiple independent trial directions and makes all four *trial* auxiliary gradients vanish to 1e-17.
- **Independent nonlinear validation:** along the integrated `theta_g` trial direction with its stationarized auxiliary response, a central nonlinear-action second difference at amplitude `0.0005` agrees with the Schur quadratic to about 0.4%. This independent physical-action calculation is subject to the finite-difference Hessian approximation, and it does NOT test the full canonical constraints.

## The scientifically essential obstruction: trial jets do not close under time derivatives

The Step 31 parent scalar metric perturbation uses the compact temporal bump

```
T(t) = [1-(t/Tmax)²]^4,
psi_g(t,r) = a_psi T(t) F(r).
```

Its actual physical derivative is

```
dot(psi_g) = a_psi T'(t) F(r).
```

But the extra Step 32b independent **rate jet** uses `b_psi T(t)F(r)`, **not** `a_psi T'(t)F(r)`. At the midpoint `t=0`, `T'(0)=0` while `T(0)=1`. Thus the two independent jets cannot simultaneously be treated as derivatives of the same compact parent field without extending/changing the time-support basis and enforcing its integrability (including boundary terms).

The four variables `(Phi_g,U_g,Phi_f,U_f)` are likewise **fixed scalar trial profiles**, not complete arbitrary spacetime ADM lapse/shift multiplier functions; `Phi` is a parameterization of the metric component `g_tt`, not exactly the canonical ADM lapse. Their invertible Galerkin `A` **must not** be identified with four true field-theoretic gravitational constraints. Diagonal diffeomorphism Ward generators do not generally close inside this restricted trial subspace. Finally, the Hassan–Rosen Boulware–Deser constraint and its time-dependent canonical null direction have NOT been derived; the apparent invertibility of this `A` neither proves nor disproves its existence.

For these reasons the numerical 14×14 Schur matrix is **NOT** a physical scalar kinetic/gradient operator. We publish it as an explicitly labeled, testable restricted-matrix sanity check, **not** as a passed Gate 2B constraint-reduction gate.

## Actual tests and reproducibility

New artifacts:

- `numerics/hr_metric_auxiliary_restricted.py` — same full 18-action finite Hessian, independent first-variation step, four-auxiliary algebraic Schur, refusal guards.
- `tests/test_hr_metric_auxiliary_restricted.py` — eleven tests including full 18×18 symmetry, rank/signature/conditioning, legitimate on-shell lapse tadpoles, exact Schur saddle, alternate inverse implementation, preserved two dust phase pairs, independent four-metric-rate oracle, quadrature/step refinement, explicit time-integrability counterexample, domain guards and an independent nonlinear action second-variation check.
- `scripts/verify_gate2b_step32c.py` — source SHA-256 manifest and one-command focused regression; declares all unpassed physical gates.

**Actually executed together** in `/mnt/data/janus32`:

```
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests
# 71 passed (29 Step31 + 20 Step32a + 11 Step32b + 11 new Step32c)

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step32c.py gate2b-step32c-report.json
# tests_exit_code=0; 71 passed; restricted auxiliary rank=4,
# condition≈545.9152; dual dust symplectic rank=2;
# full_repository_regression=false; Gate2B OPEN;
# DeFelice/Aoki NOT_RUN; actual metric/BD constraint NOT reduced.
```

**Provenance limitation:** previous Step 31/32a/32b scripts/modules are exact-byte matches to committed source files but this local focused workspace is **not** a complete clean repository checkout. Previous Step27–30 suites are not part of the 71 tests. GitHub Actions are disabled and direct git clone was previously blocked by DNS. Do not advertise a full GitHub suite or independent external reproduction. SHA comparisons against the GitHub repository should be completed before considering Step 32c saved.

## Mandatory next RED work, not optional

1. **Integrable compact metric velocity basis:** make each `psi_dot` and `E_dot` the actual time derivative of the *same* compact parent spatial metric perturbation, with a common temporal basis, full EH 3-curvature and correct time integration by parts. Rerun the diagonal on-shell Ward and all 12 Step 31 valid tadpoles and dual-dust canonical pair controls.
2. **Actual ADM lapse/shift constraints:** use the true ADM lapse and shift (possibly nonlinear HR relative-shift redefinitions), retain arbitrary test functions before spatial reduction, derive four field equations and their time-dependent constraint Poisson algebra from this complete action. Do not substitute the restricted 4×4 Schur for it.
3. **Boulware–Deser elimination:** derive the actual time-dependent HR BD null/canonical constraint and eliminate it while leaving BOTH dust `(theta,p)` pairs intact.
4. **Independent genuinely nonhomothetic on-shell background:** solve/certify all g/f Einstein, HR/Stückelberg, and two-dust radial/time tadpoles beyond the Step 30 purely compensated chart. At present the on-shell background is physically homogeneous.
5. **Only then** reproduce both SAME-CONSTRAINED-ACTION finite-H `mu→0` De Felice and nonlinear homothetic Aoki `K_S,c_S²` (stable + unstable controls). Only after those pass attempt Candidate-C first relative-mu fold around `a≈0.0301646` and possible cosmological predictions. If an obstruction persists, document a negative Gate 2B result.

**Scientific conclusion for circulation:** `RESTRICTED_FOUR_AUXILIARY_SCHUR_ALGEBRA_GREEN`; `TRUE_METRIC_BD_CONSTRAINT_REDUCTION_RED/OPEN`; `GATE_2B_OPEN`; `JANUS_R_NOT_VALIDATED`.
