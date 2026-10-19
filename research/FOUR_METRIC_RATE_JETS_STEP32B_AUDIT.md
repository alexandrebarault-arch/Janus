# JANUS — Step 32b: four independent scalar metric time-rate jets added to exact dual-dust canonical five-sector action

Date: 2026-10-19. Branch `research/gate2b-nonhomothetic-transfer`.

**Verdict:** `COMMON_TIME_METRIC_RATE_JETS_PRECONSTRAINT_GREEN`, `TWO_DUST_PHASE_PAIRS_GREEN`, but `METRIC_AUXILIARY_AND_TIME_DEPENDENT_BD_REDUCTION_OPEN`, `GENUINE_NONHOMOTHETIC_BACKGROUND_OPEN`, `GATE_2B_OPEN`.

## Advancement beyond step 32a

Step31 built a real compact time/radius action integrating positive Einstein–Hilbert g+f, full Hassan–Rosen beta0..beta4, and two covariant irrotational dusts on the actual HOMOGENEOUS radiation-free two-dust Candidate-C on-shell background. Step32a transformed each dust to its exact *common-time* canonical `p theta_dot - H_dust` form, preserving two independent matter symplectic phase pairs, with a 14×14 unreduced trial Hessian and 49 combined tests (including original exact-byte Step31 tests).

The **remaining explicit velocity gap** in that calculation was that the scalar spatial trace/shear rates, `psi_dot_g, E_dot_g, psi_dot_f, E_dot_f`, were rigidly tied to the arbitrary compact field profile; they could not be independently differentiated. This step adds **FOUR independent metric time-rate JETS** to the SAME integrated action, producing a coherent **18-amplitude phase-space/spatial-metric-rate interface**. Existing g/f metric components and lapse/shift, HR interaction, two dust Hamiltonians, their field profiles, the homogeneous on-shell background and common time/radial angular measure are unchanged.

**These independent rate amplitudes are local mathematical jets.** They are not stand-alone globally admissible compact variations of the physical metric fields, so their NONZERO first action variations are expected and must not be counted as background tadpoles. Their quadratic rate block is an **unreduced** Einstein–Hilbert ADM object, not a physical scalar kinetic matrix or a BD-ghost result.

## Exact nonlinear EH ADM kinetic correction

For each sector, with unchanged spatial eigenvalues `Qr,Qt`, ADM lapse `N`, spherical volume density `sqrt(gamma) = sqrt(g_rr)*g_angular`, and extrinsic eigenvalues `K_r,K_t` from the original nonlinear scalar metric, define independent compact spatial profiles

`delta psi_t = psi_rate * T(t) F(r)` and `delta E_t = E_rate * T(t) r² F(r)`.

Their only modifications to the spatial time-derivative metric jets are:

```
Delta Qr_t = 2 Delta psi_t - (2/3) k² Delta E_t
Delta Qt_t = 2 Delta psi_t + (1/3) k² Delta E_t
Delta K_r = Delta Qr_t/(2 Qr N)
Delta K_t = Delta Qt_t/(2 Qt N)
```

The **exact** rate modification to the positive-EH ADM+GHY density, which includes all terms linear and quadratic in the new independent jets even for finite old scalar lapse/shift/trace/shear amplitudes, is:

```
Delta L_EH = (M²/2) N sqrt(gamma) * [
  -4(K_r Delta K_t + Delta K_r K_t + Delta K_r Delta K_t)
  -4 K_t Delta K_t - 2 (Delta K_t)^2
]
```

This expression is independently checked in a nontrivial tilted-in-field-space (nonzero lapse, shift, trace and shear perturbation) spherical ADM metric against direct recomputation of `-4 K_r K_t -2 K_t²` before/after changing its metric time derivatives. All *spatial intrinsic curvature*, EH coefficients, exact chart metric and dust Hamiltonian pieces are retained unchanged.

### Closed-form isotropic background oracle

On the on-shell homogeneous spatially flat background, the new 4×4 spatial-metric-rate Hessian must have NO cross-metric coupling and NO trace/shear rate mixing (before imposing constraints), with the exact values:

```
H[psi_rate_i, psi_rate_i]
 = -6 M_i² ∫4πdt dr [a_i³ r² / N_i] [T(t)F(r)]²
H[E_rate_i,E_rate_i]
 = (M_i² k⁴/6) ∫4πdt dr [a_i³ r²/N_i] [T(t) r² F(r)]²
H[psi_rate_i,E_rate_j] = 0
H[any rate_g, any rate_f] = 0
```

The numerically differenced full nonlinear common-action rates reproduce those independently integrated analytic coefficients. Representative diagonal values for quadrature 20:

```
H_metricrate,unreduced ≈ diag(
 -4.03436606e-05,  +3.04798291e-09,
 -1.78523029e-07,  +1.34875005e-11)
```

At a centered finite-difference rate step of `0.03`, absolute error compared with the independent analytic integrals is below `1e-15`; taking steps much too small causes catastrophic *relative* loss of precision on the last f shear coefficient because the total background action is ~`-9e-3`. This was explicitly tested; **an initial regression test threshold** demanding an integrated f shear effect above `1e-13` was too coarse. The correct effect at amplitude `.024` is around `3.9e-15`; tests now use a discriminating coefficient-specific bound and independent closed-form control. No physics equation was modified to force a test pass.

**The negative signs of the two trace rates are standard UNREDUCED ADM scalar/gravity signs. They are not physical tensor ghosts, BD scalar ghosts or propagating kinetic eigenvalues. The E shear test profile contains `r² F(r)` and its scale is arbitrary, so values cannot be used to infer physical scalar propagation speeds or stability.**

## Full five-sector consistency

The new 18-amplitude action ordering is exactly the Step32a 14 amplitudes:

`(Phi_g,U_g,psi_g,E_g,theta_g,p_g,theta_rate_g, Phi_f,U_f,psi_f,E_f,theta_f,p_f,theta_rate_f)`

plus `(psi_rate_g,E_rate_g,psi_rate_f,E_rate_f)`.

At all four new rates zero the new full action returns the exact 14-amplitude five-sector action, including both EH, HR, and both dust terms. When only an individual new rate is excited **only its own EH sector** changes, not HR or either dust contribution. The matter `p_g--theta_rate_g`, `p_f--theta_rate_f` symplectic block retains rank TWO and its exact positive analytical coefficients, independent of the four added metric rate jets. The existing relative HR mixed metric coupling is preserved. The new independent rate directions are not autonomous physical fields; time-integration by parts must relate their values to the true compact metric profile variations before examining Noether/constraints.

## Test provenance

New files:

- `numerics/hr_common_time_metric_rates.py` — exact nonlinear native/common spherical EH extrinsic-curvature rate modification and four closed-form rate Hessian controls, 18-amplitude five-sector action.
- `tests/test_hr_common_time_metric_rates.py` — **11** additional tests, including independently recomputed finite-amplitude ADM kinetic term, analytic rate-rate Hessian, no cross-metric or trace/shear mixing, quadrature/finite-difference precision control, both independent matter phase-space pairs, HR coupling preservation, zero-rate reduction, and malformed-input rejection.
- `scripts/verify_gate2b_step32b.py` — explicit 60-test exact-source provenance runner.

Actually executed on `/mnt/data/janus32` using byte-exact original Step31 module + test and the tested Step32a files:

```
cd /mnt/data/janus32
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
# 60 passed = 29 exact Step31 + 20 Step32a + 11 Step32b
OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step32b.py gate2b-step32b-report.json
# source manifest, 60 tests, 2 preserved matter pairs,
# De Felice/Aoki NOT_RUN and GATE_2B OPEN.
```

All 60 tests are **one actual combined focused test run** and not sums of separate historical workspace results. It is still NOT the complete repository test suite, a clean Git checkout, GitHub Actions or peer-replicated science. The new files and audit must be SHA-checked against exact GitHub blobs before reporting published success.

## What is still RED (unavoidable for viability)

1. Impose the true ADM lapse and radial shift auxiliary constraints of BOTH metrics, and the diagonal Noether gauge identities, taking full account of integrating by parts time-dependent compact metric-rate jets. Build the time-dependent BD-null canonical generator and reduce it, **retaining BOTH `(theta_g,p_g)` and `(theta_f,p_f)`**.
2. The physical nonhomothetic f native background is STILL only a passive coordinate compensation of the homogeneous solution. Solve an independent inhomogeneous/two-metric/two-dust on-shell branch or explicitly reject a specified ansatz by its first variations. This requires Einstein g/f, HR Stückelberg, both matter Euler/tadpoles on common time/radius support.
3. From ONE fully constrained action reproduce finite-H `mu→0` De Felice scalar principal speed and nonlinear homothetic Aoki `K_S,c_S²` stable+unstable controls. These independent physical oracles have not been passed. Only after both pass evaluate Candidate-C relative first `mu` fold near `a≈0.0301646`; no CMB likelihood before physical transfer is validated.

**Scientific status:** `EXACT_TWO_DUST_CANONICAL_AND_FOUR_METRIC_RATE_JETS_GREEN_PRECONSTRAINT`; **`GATE_2B=OPEN`; JANUS-R cosmology NOT validated**.
