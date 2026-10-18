# JANUS Gate 2B — Step 26: full bimetric Hassan–Rosen diagonal/relative Ward and off-shell Hessian caution

**Date:** 2026-10-18. **Research branch:** research/gate2b-nonhomothetic-transfer.
**Gate:** `COUPLED_ALL_BETA_DIAGONAL_WARD=GREEN`; `OFFSHELL_NOETHER_WARNING_CONFIRMED`; **`GATE_2B=OPEN`**.

## Scientific question and result

The prior steps 23–25 verified the coordinate-change Ward identity of the isolated native f Einstein–Hilbert action; that alone cannot verify the **coupled** bimetric potential. This step independently computes the **exact nonlinear, spacetime-integrated Hassan–Rosen interaction** with BOTH spherical Lorentzian metrics, all beta0..beta4 coefficients, four regular scalar perturbation amplitudes per metric and a genuinely time/radius-dependent nonhomothetic f chart. It distinguishes two different operations:

1. A compact **diagonal** coordinate change of BOTH g and f, with consistent pullback of all metric components and angular radii. This MUST leave the interaction action invariant.
2. A compact **relative** change of the f chart while g remains fixed. The beta1/beta2/beta3 interaction changes; beta0 and beta4 independently reduce to the g-only and f-only spacetime volumes and are invariant under the relative f chart perturbation.

**Both expectations were confirmed numerically, across all five individual beta sectors and nonzero scalar fields in both metrics.**

### Exact spherical 2×2 + angular Hassan–Rosen potential

Let `g_AB, f_AB` be the exact pulled-back temporal/radial 2×2 metric blocks, `g_Ω, f_Ω` the positive angular coefficients, and `D_g=det g_AB<0`, `D_f=det f_AB<0`. On the tested real square-root branch:

```text
s = sqrt(D_f / D_g),
tau = sqrt( tr(g_AB^{-1} f_AB) + 2s ),
ell = sqrt(f_Ω / g_Ω).

e0=1
e1=tau+2ell
e2=s+2ell*tau+ell²
e3=2ell*s+ell²*tau
e4=ell²*s.

S_HR = - 4*pi m² Mg² int dt dr sqrt(-D_g) g_Ω
         * sum_{n=0}^4 beta_n e_n.
```

The angular radius of each metric is recalculated at the **correct moved radial coordinate**, instead of being replaced by an untransported `r²` placeholder. A full `J^T metric J` pullback is performed for each radial 2×2 block.

The off-shell polynomial control backgrounds are `sigma(t)=0.08+0.025t`, `mu(t)=-0.22+0.05t`, with `T=t+sigma(t)r²/2`, `R_f=(1+mu(t))r`. Independent lapse, shift, scalar trace and traceless shear trial fields are nonzero for both g and f, with radial parity ensuring regularity at the origin. **They are NOT a solved Candidate-C cosmological trajectory or physical eigenfunctions**. Positive chart orientation and Lorentzian/principal-real branch guards are enforced.

For diagonal changes the same compact displacement `x -> x+xi(x)` pulls back BOTH metrics: `g -> J_x^T g(x+xi) J_x` and `f -> J_x^T f(x+xi) J_x`. For the f-native chart it is essential to COMPOSE its pre-existing nonhomothetic `X_f(x)` with `x+xi`, rather than adding `xi` directly to the native coordinates. Since the HR integrand is a diagonal scalar density, the change is a boundary-fixed change of variables.

### Native-relative versus common-relative displacements must NOT be conflated

Two separately tested conventions:

- **Native f displacement:** `X_f -> X_f + delta X_f`, while g is fixed.
- **Common-chart f displacement:** `X_f(x) -> X_f(x+delta x_f)`, while g is fixed.

At first order their vectors obey **`delta X_f^A = (partial_mu X_f^A) delta x_f^mu`**. For nonzero sigma, mu_dot and mu they are generally NOT numerically interchangeable under equal amplitude labels. An initial NEW test incorrectly asserted equality of the two independent finite charts and failed. Rather than force agreement, the test was corrected to assert equality only for the truly diagonal operation and to explicitly distinguish the two relative-coordinate parametrizations.

## Quantitative checks

Using all five beta coefficients `(.21,.78,-.35,.16,.11)`, 44-point time and radial quadrature, dimensionless off-shell native backgrounds/fields:

```text
baseline exact HR action:     -1.1841560984085913
minimum f background det J:  +0.7600291971379421

finite DIAGONAL deformations, delta action:
  delta time=+.04:                         0
  delta radial=-.04:                       0
  (delta time, delta radial)=(+.035,-.023): 0

finite f NATIVE-RELATIVE deformations, delta action:
  delta time=+.04:                        -5.22252957679825e-6
  delta radial=-.04:                      +1.68606625194911e-6
  (+.035,-.023):                          -1.43883746233087e-5
```

For each isolated beta0 and beta4, the f-native-relative change vanishes to floating-point precision; for each isolated beta1, beta2 and beta3 it is demonstrably nonzero. The action is linear in all betas and stable under 30/48-point quadrature.

**Independent local formula comparison:** at `t=0`, for `r=0.12,0.23,0.39`, the newly implemented direct two-metric principal-root density equals `r² * native_hr_stueckelberg_jet(...).value` from the **pre-existing** exact 14-variable Hassan–Rosen Taylor jet, with consistent lapse/scale Taylor coefficients and all metric perturbations set to zero. The r=0.23 check gives **-0.0823859285303577 on BOTH sides**, difference 0 at displayed precision. This is not merely a self-comparison of our coordinate-invariance integral.

## A subtle off-shell Noether lesson: directional Ward != Hessian null eigenvector

New code `numerics/hr_coupled_chart_hessian.py` independently varies **FOUR** chart amplitudes:

```text
(epsilon_g,time, epsilon_g,radial, epsilon_f,time, epsilon_f,radial).
```

The diagonal paths `epsilon_g=epsilon_f` leave the action exactly invariant, for arbitrary finite compact changes, hence their **first directional derivative and diagonal second directional derivative** vanish.

Nevertheless, on the arbitrarily chosen **OFF-SHELL** background, a diagonal vector `v` does not have to be a zero eigenvector of the raw Hessian `H`. The off-shell Noether identity is:

```text
S_,i R^i = 0
  => S_,ij R^i + S_,i (partial_j R^i) = 0.
```

The second term is nonzero unless one is sufficiently on shell and the chosen gauge-coordinate map makes the generator constant. The raw Hessian can therefore have `H v != 0` **even though** the action is exactly invariant along the finite gauge orbit. A naive attempt to identify BD or diagonal gauge-null constraints by eigenvectors of an arbitrary off-shell Hessian is scientifically invalid.

At the diagnostic point with four-chart finite-difference step 0.0015:

```text
relative g chart tadpoles: (+0.00258729923,+0.00001645726)
relative f chart tadpoles: (-0.00258729884,-0.00001645641)

v_time=(1,0,1,0):
  v_time^T H v_time  = -6.84686875e-7 (O(step²) stencil error)
  ||H v_time||       = +3.00375085e-4 (nonzero off-shell)

v_radial=(0,1,0,1):
  v_radial^T H v_radial = -1.23358e-9
  ||H v_radial||        = +1.72585482e-3 (nonzero off-shell)
```

The finite-difference diagonal quadratic residual falls by approximately a factor of four when its step is halved; the direct finite-amplitude diagonal action variation is zero to numerical precision. **The nonzero `Hv` is not a ghost or a violation of covariance**: it is an off-shell Hessian and the coordinates on its gauge orbit are nonlinear.

## Reproducibility and exact file hashes

Committed sources:

- `numerics/hr_coupled_diagonal_ward.py`
- `numerics/hr_coupled_chart_hessian.py`
- `tests/test_hr_coupled_diagonal_ward.py`
- `tests/test_hr_coupled_chart_hessian.py`
- `scripts/verify_gate2b_step26.py`

All FIVE files match their **executed local Python source** byte for byte against live GitHub blob SHA:

```text
numerics/hr_coupled_diagonal_ward.py  cf77b66fdb576a1c305ec9adc6d8842a0816fdd3
numerics/hr_coupled_chart_hessian.py  85044fc2bcafec6951078048394406c7df018813
tests/test_hr_coupled_diagonal_ward.py 04b1a7f5e6d9dd0ec7641188873188865e673f00
tests/test_hr_coupled_chart_hessian.py 3f9e2eb25e49449a520fdb54198df069a3248ab6
scripts/verify_gate2b_step26.py      fabd5259f66e558bc6d0b67a2bfd950f55989267
```

Actually executed from local `/mnt/data/janus-next`:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
# 57 passed

OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step26.py checkpoint-26-local.json
# tests_exit_code=0, tests_passed_count=57
# workspace_origin=non_git_workspace_reconstruction
# full_repository_regression=false
# DeFelice/Aoki: NOT_RUN
# gate2b=OPEN
```

**Remaining reproducibility limit:** direct `git clone` still fails DNS in this runtime; the older prereq HR/dust modules in the local reconstructed workspace preserve their algorithms but are NOT all byte-identical to GitHub blobs. Five new files, however, have been SHA-matched to the pushed branch. The 57 tests are a **focused local collection**, not a full checkout of the full GitHub test tree, GitHub Actions, or an independent peer replication.

## Exact next RED gates, ordered

1. **One common dynamical time-domain action:** use the new coupled HR potential on the SAME time-dependent scalar metric profiles and time/radial support as both native EH operators and BOTH dust canonical phase-pair actions. The prior EH chart Ward and this diagonal HR Ward must become automatic regression gates in the **same** field basis. No double counting of chart advection, angular measure or matter phase rates.
2. Impose one **on-shell nonhomothetic Candidate-C** trajectory satisfying both metric Friedmann/background equations and independent g/f dust conservation, and verify that ALL first-order tadpoles cancel. The off-shell Hessian warning prevents premature constraint/gauge-kernel interpretation.
3. Derive four metric auxiliary constraints, time-dependent BD-null canonical reduction and complete scalar kinetic/gradient operators, retaining both canonical dust pairs.
4. Pass two independent **physical** oracles on that **same** constrained action: finite-H `mu->0` De Felice scalar characteristic, and nonlinear homothetic Aoki `K_S,c_S²` including stable and unstable roots.
5. ONLY then approach Candidate-C fold 1 (`a≈0.0301646`) and report a real positive or negative physical verdict. No observational transfer/CMB or viability claim before these gates.

**Publication status:** `COUPLED_DIAGONAL_WARD_GREEN`; `GATE_2B_OPEN`; `JANUS_R_NOT_VALIDATED`. The external negative-EH-sign JHR prepublication ghost objection remains a separate audit.
