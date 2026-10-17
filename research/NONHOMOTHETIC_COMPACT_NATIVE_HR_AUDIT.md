# Gate 2B — compact native finite-mu HR audit

Date: 2026-10-17
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **FINITE-MU HR INTERACTION ORACLE GREEN; MATTERLESS FLAT-GAUGE SCHUR REJECTED; COMPACT DUST PHASE IS NEXT HARD BLOCK**

## Purpose

This audit records the compact-support promotion of the finite-`mu` Hassan-Rosen interaction into the native relative variables used by the validated pre-BD Candidate-C bridge.

The central question was whether the nonlinear HR pullback itself could be inserted consistently before the four metric auxiliaries are eliminated, while preserving both independent acceptance limits:

1. exact disappearance of the nonlinear correction at `mu -> 0`;
2. recovery of the published nonlinear homothetic Aoki scalar action.

The interaction sector now passes both structural requirements at audit level.  The remaining failure found during this work is not in HR: it occurs if one attempts to eliminate the flat-gauge metric auxiliaries without retaining the dust phase variables.  That shortcut is therefore rejected.

## 1. Compact finite-mu native HR correction

Added:

- `numerics/nonhomothetic_compact_hr_correction.py`;
- `tests/test_nonhomothetic_compact_hr_correction.py`.

The compact variables are

`(L,T,Phi_g,Phi_f,B_g,B_f)`.

The action difference is formed pointwise as

`Delta S_HR(mu) = S_HR(mu) - S_HR(mu=0)`

using the **same native perturbation fields but separately evaluating the f-sector compact profile in each native pullback**.  This distinction is required because the f-native time/radius coordinates differ between the finite-`mu` and reference maps.

The resulting six-by-six Hessian has the following verified properties:

- the correction vanishes numerically at `mu=0`;
- the finite-`mu` Hessian is finite and symmetric;
- the small-`mu` limit is regular and linear in `mu` over the committed control range;
- the Hessian is stable under amplitude-step refinement.

## 2. Time-dependent native background jet

`numerics/nonhomothetic_hr_relative_native.py` now accepts

- `a_dot_over_a`;
- `a_ddot_over_a`;
- `common_time_offset`.

Across compact support it evolves

`a(t)`, `mu(t)`, `s(t)`,

and samples the f lapse/scale jet at the total native f-time offset

`t_f = t + s(t) r^2/2 - T`.

Regression:

- `tests/test_relative_native_time_jet.py`.

The zero-time / zero-new-rate path reproduces the historical geometry exactly.

Targeted reconstructed-workspace verification after this promotion:

`7 passed`

for the compact correction plus time-jet subset.

## 3. Independent Aoki cross-gauge oracle — GREEN

Added:

- `numerics/aoki_native_relative_hr_oracle.py`;
- `tests/test_aoki_native_relative_hr_oracle.py`.

This is an action-level coordinate-covariance test, not a substitution of published formulas into the implementation.

Start from the Aoki homothetic nonlinear map in conformal coordinates.  Change the common chart to the native g cosmic chart.  The relative native radial perturbation obeys

`L_r = (1+mu) delta r`,

while the native f time perturbation is the pullback of

`(1+sigma_eta) delta_eta + sigma_r delta r`

converted to cosmic time.

The resulting `(L,T)` jets are inserted directly into the shared exact native HR density and integrated on compact support.  The `H^2` coefficient is extracted from `+H,-H,0` controls and fitted independently to the kinetic and radial-gradient profile integrals.

Three nonlinear dust controls were tested, including both signs of the Aoki kinetic coefficient.

Representative Candidate-like homothetic control:

- `mu ~= -0.6692344189`;
- analytic HR kinetic Hessian target `-2 D K_S ~= -0.61311226`;
- native-relative result `~= -0.61177365`;
- kinetic disagreement `~= 0.22%`;
- analytic `c_S^2 ~= 13.27614266`;
- native-relative result `~= 13.29793872`;
- sound-speed disagreement `~= 0.16%`;
- compact fit residual `~= 4.6e-6`.

The other committed controls remain within the `1.5%` acceptance tolerance and include the opposite kinetic-sign case.

**Scientific ruling:** the finite-`mu` native HR interaction/pullback is now independently connected to the published Aoki nonlinear scalar action.

## 4. Native spatially-flat spherical Einstein-Hilbert primitive

Added:

- `numerics/spherical_flat_adm_eh.py`;
- `tests/test_spherical_flat_adm_eh.py`.

For the native metric convention

`g_tt = -n^2(1+2 Phi)`,

`g_tr = n a U`,

with exactly flat spatial slices, the ADM lapse is

`N = n sqrt(1+2 Phi+U^2)`.

The radial/tangential mixed extrinsic-curvature eigenvalues are

`k_r = (adot/a - n U_r/a)/N`,

`k_t = (adot/a - n U/(a r))/N`.

The exact radial EH density per `sin(theta)` is therefore

`N a^3 r^2 (-4 k_r k_t - 2 k_t^2)`

before the overall `M^2/2` factor.

Independent controls pin:

- the exact FLRW background density;
- finite constant-lapse rescaling;
- a static Minkowski isotropic radial-shift configuration.

## 5. Structural compact native EH+HR assembly

Added:

- `numerics/nonhomothetic_compact_native_gravity.py`;
- `tests/test_nonhomothetic_compact_native_gravity.py`.

This module assembles, in one native flat-gauge compact chart,

`EH_g + EH_f + HR`

for variables

`(L,T,Phi_g,Phi_f,B_g,B_f)`.

Structural tests establish:

- a finite symmetric 6x6 Hessian;
- rank-four metric auxiliary block on the committed control;
- a two-dimensional Stueckelberg block after metric Schur reduction;
- zero Stueckelberg dynamics at zero interaction mass.

These are architecture tests only.  They are **not** a physical Aoki acceptance of the matterless flat-gauge Schur.

## 6. Matterless flat-gauge Schur — rejected shortcut

An exploratory local implementation attempted to recover Aoki after eliminating only

`(Phi_g,Phi_f,B_g,B_f)`

from the flat-gauge EH+HR compact action, with no matter phase variables.

This route failed decisively and was not committed as an accepted scientific module.

At small interaction mass the raw projected HR `pi-pi` entry continues to agree with the Aoki HR oracle, but the metric Schur correction is much larger than the expected perturbative signal.  The weak metric block develops directions whose singular values scale with the interaction mass, so eliminating them produces an order-`m^2` correction rather than a small correction to the HR-only early-time action.

This is not evidence against the HR interaction.  It is the wrong constrained system.

The already validated Candidate-C dust action proves that the two matter phase pairs feed the finite-H helicity-0 mode at order unity:

- full dust system at the representative control: `c_s^2 ~= 0.69093`;
- artificially dust-clamped result: `c_s^2 ~= 0.49432`.

Therefore a spatially-flat metric Schur that omits the dust phase variables cannot serve as a physical acceptance oracle.

**Ruling:** do not tune EH/HR coefficients and do not loosen tolerances.  Carry the dust phase pairs through the compact constrained action.

## 7. Current insertion point

The validated production linear architecture remains authoritative at `mu=0`:

- relative pre-BD states `(Y1,Y2,L,T,p_g,p_f)`;
- six corresponding rates, with structural zero rates for the two momenta;
- metric auxiliaries `(Phi_g,Phi_f,B_g,B_f)`;
- exact bridge `Y3=-2L`, `Z=-nH_f T+k^2L/3`;
- `T` is the algebraic/BD coordinate;
- `L` is the spatial helicity-0 coordinate;
- dust momenta remain canonical variables and are never ordinary Schur auxiliaries.

The new compact `Delta S_HR(mu)` must be added at this **pre-metric** level.

## 8. Immediate next block

Derive and test the real-space native pressureless phase action in the same `(Phi,B)` convention.

The local dust phase structure corresponding to the validated De Felice Fourier action is

`p qdot + p r_phi q - p Phi + rho Phi^2/2`

` - (n^2 rho / 2 a^2) (grad q + a B/n)^2`,

where `r_phi = dot(phi_background)/phi_background`; for the production f-dust variable this supplies the mandatory `n_dot/n` drift.

Then:

1. integrate both dust sectors on compact support;
2. pull the f sector through the same native Jacobian as HR;
3. retain `(q_g,q_f,p_g,p_f)` as phase variables;
4. eliminate only the four metric auxiliaries;
5. require the `mu=0` compact/pre-BD result to reproduce the validated De Felice/Stueckelberg linear system;
6. add `Delta S_HR(mu)` without changing EH or dust coefficients;
7. only after the `mu=0` oracle is GREEN, evaluate the early regular finite-`mu` Candidate-C branch toward fold 1.

## Verification limitation

All new tests cited here were run in reconstructed targeted workspaces because the environment still cannot clone the repository and GitHub Actions remain disabled.  This is not a full-repository GREEN claim.

`GATE_2B = OPEN`.
