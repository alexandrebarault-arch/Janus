# JANUS Gate 2B — all-four-scalar Einstein–Hilbert chart-pullback audit

**Date:** 2026-10-18  
**Branch:** `research/gate2b-nonhomothetic-transfer`  
**Verdict:** `FULL_NATIVE_SCALAR_EH_KINEMATIC_WARD=GREEN` on the explicitly defined compact, regular off-shell test charts. **`GATE_2B=OPEN`; no validated nonhomothetic physical scalar action.**

## Research question

Step 23 checked covariance under compact time/radial chart deformations for a positive-sign f Einstein–Hilbert FLRW action with only a **native lapse perturbation**. The new independent benchmark checks all four native scalar metric perturbation channels **lapse, radial shift, spatial trace and scalar traceless shear**, using an exact nonlinear, spherically symmetric ADM plus boundary representative of f Einstein–Hilbert. Both temporal and radial chart displacements, full finite amplitudes and native perturbation-field advection are retained.

It is essential to distinguish the achievement from the eventual goal. **This tests the pullback of a native ADM density to a common chart. It does not yet derive the quadratic f Einstein–Hilbert chart-variation Hessian in the same 24-variable HR+two-dust basis**, nor prove on-shell background, constraint reduction, kinetic positivity, the Candidate-C fold or cosmological observables.

## Geometry and action

In the native f coordinates `(T,R,theta,phi)`, define

```text
ds_f² = -n(T)²[1+2Phi(T,R)]dT² + 2n(T)a(T)U(T,R)dT dR
      + a(T)² Qr(T,R)dR² + a(T)² Qt(T,R)R² dOmega²,

Qr = 1+2psi-(2/3)k² E,    Qt=1+2psi+(1/3)k² E,
N_ADM=n sqrt(1+2Phi+U²/Qr),   N^R=n U/(a Qr).
```

Set `L=a sqrt(Qr)`, `S=a R sqrt(Qt)`, `W=S_R/L`. Then

```text
R3 = 2/S² [1-W²-2(S/L) W_R],

Kr = [a_T/a + Qr_T/(2Qr) - (N^R)_R
      - N^R Qr_R/(2Qr)] / N_ADM,

Kt = [a_T/a + Qt_T/(2Qt)
      - N^R (1/R + Qt_R/(2Qt))] / N_ADM.

L_EH,ADM = (Mf²/2) N_ADM L S² [R3 - 4Kr Kt - 2Kt²].
```

Use `Mf²=1` and smooth dimensionless off-shell native FLRW backgrounds

```text
a(T)=1+0.15T+0.035T²,  n(T)=1+0.08T+0.02T².
```

Four independent perturbation amplitudes multiply explicitly differentiable smooth polynomials in `(T,R)`; `U=O(R)`, `E=O(R²)` at the center, so the native metric is regular there. Their temporal and first/second radial native derivatives are evaluated consistently, rather than treating them as unrelated placeholders. The native metric channels are **off-shell trial functions**, not physical eigenmodes.

### Nonhomothetic background chart and finite perturbations

Pull native `(T,R)` to common `(t,r)` by

```text
T0=t+sigma(t)r²/2,   R0=[1+mu(t)]r,
sigma(t)=0.08+0.025t,    mu(t)=-0.22+0.05t.

J0 = d(T0,R0)/d(t,r),   det(J0)>0.
```

Choose independent compact interior coordinate deformations

```text
deltaT=epsilon_T A(t)F(r),    deltaR=epsilon_R r A(t)F(r),
A(t)=[1-(t/Tmax)²]^4,        F(r)=[1-(r/Rmax)²]^4.
```

Their support vanishes at all outer boundaries. Both the full finite Jacobian determinant `D=det[d(T,R)/d(t,r)]` and all four **native field values and field derivatives at the moved coordinates** are recalculated. The exact pulled-back action is

```text
S_f[epsilon,amplitudes]
  = 4*pi integral dt dr D(t,r) L_EH,ADM[T(t,r),R(t,r);
                                       Phi,U,psi,E and native derivatives].
```

As the chart deformations vanish at the boundary and preserve orientation, this integration represents the same native image domain, hence is invariant under the compact coordinate reparameterization. The result is a **geometric consistency/coordinate-change identity**, not a proof of the full dynamical diffeomorphism constraint algebra.

The deliberately incorrect control keeps the native perturbation fields **and their native derivatives** sampled at the original `(T0,R0)`, while changing the native geometry/background and Jacobian. This drops their advective response. It breaks the Ward identity as expected.

## Independent acceptance controls

New files:

- `numerics/hr_eh_full_scalar_chart_ward.py`: exact nonlinear native ADM density from independently specified scalar field derivative samples; finite chart pullback quadrature and mixed Ward table.
- `tests/test_hr_eh_full_scalar_chart_ward.py`: 8 targeted tests including a cross-check against the **separate** exact six-variable Einstein–Hilbert Hessian from step 22.
- `scripts/verify_gate2b_step24.py`: repeatable focused test runner producing a JSON provenance manifest, including git origin, SHA-256, version, pass count and deliberately unpassed physics gates.

**The crucial non-tautological cross-check:** at a native diagnostic `T=0.13, R=0.26`, the newly evaluated nonlinear ADM density, with six compact radial profile amplitudes `Phi,B,psi,E,psi_dot,E_dot`, is independently finite-differentiated and agrees with **half** the analytic Hessian returned by `numerics/hr_full_scalar_eh_homothetic.py` (half because the new action already includes the positive `M_f²/2` prefactor). In its spatially flat limit with `psi=E=0`, it also reproduces `numerics/spherical_flat_adm_eh.py` directly. Thus the new density is not only being tested against itself via a coordinate-invariant integration.

The eight new tests also cover coordinate invariance of the fully nonlinear native action for each individual mode, simultaneous excitation of all four modes, changed compact support sizes, spherical-center parity/regularity, finite-difference mixed Ward variations and invalid/singular metric/chart guards.

## Quantitative off-shell regression table

At quadrature order 42 with two finite-difference steps 0.002, the matrix of mixed derivatives `d²S/(d epsilon_chart d amplitude_native)` has rows `(Phi, U, psi, E)` and columns `(time chart, radial chart)`:

| Native field | Complete: time | Complete: radial | Field sampling artificially frozen: time | Frozen: radial |
|---|---:|---:|---:|---:|
| Phi | +2.17e-13 | -4.34e-13 | -2.86155e-4 | -1.10418e-5 |
| U | 0.00 | -4.34e-13 | -2.24105e-3 | -1.22448e-2 |
| psi | -1.30e-12 | 0.00 | +4.39267e-3 | +1.76104e-2 |
| E | +3.25e-12 | +1.52e-12 | +2.91498e-2 | +3.11530e-1 |

The maximum correct residual is `3.25e-12`, which is consistent with floating-point cancellation amplified by taking finite second differences of an invariant integral. The smallest frozen-sampling residual magnitude is `1.10e-5`; every negative control remains clearly nonzero.

For an additional combined four-field perturbation `(0.025,-0.022,0.032,-0.012)` and chart displacement `(epsilon_T,epsilon_R)=(0.04,-0.03)`, the action is `0.01019034860125542`, with a change of approximately `1.73e-18` under the compact chart deformation (on the arbitrary dimensionless diagnostic background).

**These are code-regression values, NOT observational predictions, physical kinetic eigenvalues or constraints on the cosmological parameters.**

## Reproducibility and exact-source provenance

Executed locally in `/mnt/data/janus-next`, with Python 3.13.5, NumPy and pytest:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
# 32 passed

python scripts/verify_gate2b_step24.py gate2b-step24-report.json
# tests_passed_count=32, tests_exit_code=0,
# workspace_origin=non_git_workspace_reconstruction,
# full_repository_regression=false,
# DeFelice/Aoki=NOT_RUN, Gate2B=OPEN
```

The three new source/test/verification files were matched **byte-for-byte by Git blob SHA** against GitHub on this active research branch:

```text
numerics/hr_eh_full_scalar_chart_ward.py
    b69b6b15245e04634822e1d4b61003f7b0a7ea3a
tests/test_hr_eh_full_scalar_chart_ward.py
    cd2d5cd89ec099789acd49b8f17f6c709d602518
scripts/verify_gate2b_step24.py
    d1bffdd7fa94cbb9c8e80166bdf424715f2bc17b
```

**Reproducibility limitation:** the existing pre-step-24 HR/dust prerequisites in this particular reconstructed workspace were manually reauthored preserving their algorithms but are not all byte-identical to GitHub. The 32 tests were NOT run on a full clean repository checkout. GitHub Actions were disabled previously and direct git clone failed DNS. The reproducibility script explicitly marks the workspace origin; no independent external peer verification is claimed.

## Precise remaining RED gates before scientific validation

1. **Action-level chart variation:** use the native full scalar ADM oracle to build the actual finite-time compact quadratic EH **chart-perturbation Hessian**, including `deltaT,deltaR`, perturbations of all native scalar metric fields, their first/second derivatives, integration by parts and time-dependent background. A pullback scalar-density Ward identity alone does **not** yield this physical preconstraint matrix.
2. On ONE consistent common spacetime support, unite that EH chart Hessian with the earlier finite-mu HR interaction and BOTH exact dust canonical phase sectors. Derive the f-native field-derivative pullbacks and gauge/measure normalization from one action, not separately tuned Hessian blocks.
3. Impose the same on-shell nonhomothetic Candidate-C background `a,n,alpha,mu,sigma`, two separately conserved dust backgrounds, and cancel every background tadpole.
4. Eliminate four metric auxiliary constraints, followed by time-dependent BD-null canonical reduction. Keep both matter phase pairs dynamical. Only the **constrained** operators can diagnose ghosts and gradients.
5. On the SAME fully assembled action, reproduce independently the finite-H Candidate-C `mu->0` De Felice physical scalar dispersion and the homothetic nonlinear Aoki `K_S,c_S²` limits (stable and unstable roots).
6. **Only if both oracles pass**, evaluate the first Candidate-C fold `a≈0.0301646`; report either a regular physical crossing with derived late data or a negative Gate-2B verdict. Any observational transfer/CMB fit is later and presently unperformed.

**Disposition for community circulation:** present this as a **numerical/mathematical audit and open research**, not as a validated JANUS cosmology. The external JHR manuscript's opposite-sign EH tensor ghost objection remains a separate unresolved issue.
