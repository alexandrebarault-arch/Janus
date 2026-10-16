# Candidate C — finite-mu native Hassan-Rosen promotion audit

Date: 2026-10-16
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **NATIVE FINITE-MU HR PULLBACK / CORRECTION INFRASTRUCTURE BUILT AND CONTROLLED; LOCAL SHELL HESSIAN REJECTED AS PRODUCTION OPERATOR; COMPACT-SUPPORT PROMOTION IS NEXT**

## Purpose

The finite-H De Felice <-> pre-BD Stueckelberg bridge is already closed.  The active problem is to promote only the Hassan-Rosen interaction away from the linear `mu=0` background while leaving the validated Einstein-Hilbert and dust phase sectors untouched.

The new architecture uses a finite-mu interaction correction

`Delta H_HR(mu) = H_HR^exact(mu) - H_HR^exact(mu=0)`

in the same native relative-coordinate convention.  This correction vanishes identically at `mu=0`, so the already validated finite-H linear Candidate-C action is recovered without retuning EH, matter, or any HR coefficient.

This audit establishes the native pullback and numerical infrastructure.  It does **not** yet claim that a local spherical-shell Hessian is the physical Fourier operator.

## 1. Exact native relative pullback

Added:

- `numerics/nonhomothetic_hr_relative_native.py`;
- `tests/test_nonhomothetic_hr_relative_native.py`.

The g-sector cosmic FLRW chart is used as common chart.  The f native coordinates are pulled back by

`t_f = t + s r^2/2 - T`,

`R_f = (1+mu) r - partial_r L`.

The f lapse and scale factor are evaluated on a local second-order native background jet,

`n(t_f)` and `alpha(t_f)`,

so the quadratic interaction retains the background-rate terms required by a finite-H Hessian.

The radial Jacobian keeps

- `Tdot`, `T_r`;
- `Ldot_r`, `L_rr`;
- `mu_dot`;
- `s`, `sdot`.

Native weak metric auxiliaries `(Phi_g,Phi_f,B_g,B_f)` remain explicit.

### Controls

Three independent controls pass:

1. for a static finite `mu`, the principal square-root eigenvalues are exactly
   `(n, xi(1+mu), xi(1+mu), xi(1+mu))`;
2. at `mu=0`, linearizing the native pullback reproduces the validated pre-BD bridge
   `Phi_f,common = Phi_f,native - Tdot - (ndot/n) T` and
   `B_f,common = B_f,native + (n/alpha) T - (alpha/n) Ldot`;
3. the finite-mu correction density vanishes identically when `mu=mu_dot=s=sdot=0`.

## 2. Independent weak-source oracle

Added:

- `tests/test_nonhomothetic_hr_relative_sources.py`.

On a homothetic static finite-mu control, derivatives of the new exact density with respect to the native lapses reproduce independently derived diagonal Hassan-Rosen source tensors.

For the g lapse, the correction tadpole equals the change in `V_g^0_0` times the native reduced volume.

For the f lapse, the correct native volume factor appears explicitly,

`K^4 (1+mu)^3 V_f^0_0(mu) - K^4 V_f^0_0(0)`.

This checks the new pullback at the constraint/source level rather than only at the square-root eigenvalue level.

## 3. Candidate-C native background jets

Added:

- `numerics/candidate_c_native_hr_jets.py`;
- `tests/test_candidate_c_native_hr_jets.py`.

Five-point derivatives in `N=ln a` provide

- `n = xi c`;
- `alpha = a xi`;
- `ndot/n`;
- `nddot/n`;
- `alphadot/alpha`;
- `alphaddot/alpha`;

along the same strict on-shell Candidate-C dust trajectory.

The generic conversion uses

`d/dt = H_g d/dN`,

`fddot/f = [H H_N f_N + H^2 f_NN]/f`.

The first derivatives reproduce the independent exact background identities for `n` and `alpha`; the second derivatives are stable under step refinement.

## 4. Early adiabatic Stueckelberg branch jets

Added:

- `numerics/candidate_c_adiabatic_stueckelberg_jets.py`;
- `tests/test_candidate_c_adiabatic_stueckelberg_jets.py`.

This helper follows the more-negative member of the **leading** regular non-homothetic quadratic pair at early times and returns

`mu, mu_N, mu_dot, s, s_N, sdot`.

The temporal shift is not fitted; it is fixed by the exact relation

`s = -(a^2/c) [mu_dot + H_g mu(c+1+mu)]`.

The helper deliberately raises once two regular real roots are absent.  It is an early-branch architecture oracle only and must not replace the independently localized finite weak-metric folds.

## 5. Phase-averaged local HR correction Hessian

Added:

- `numerics/nonhomothetic_hr_relative_mode.py`;
- `tests/test_nonhomothetic_hr_relative_mode.py`.

The 8-variable interaction-only order is

`(L,T,Ldot,Tdot,Phi_g,Phi_f,B_g,B_f)`.

The correction can be embedded in the validated 16-variable augmented order at indices

`(2,3,8,9,12,13,14,15)`.

All `Y1,Y2,p_g,p_f` coordinates and their rate slots remain exactly untouched by the interaction correction.

### High-k conditioning correction

A raw common finite-difference step is invalid because

`L_rr ~ k^2 L`.

At production `k`, a nominal `5e-4` raw step in `L` can move the radial Jacobian through zero and falsely leave the real HR branch.

The Hessian now uses geometry-scaled polarization steps:

- `L` scales as `r/k`;
- `T` and `Ldot` as `1/k`;
- metric shifts according to the gradient factors entering their native metric blocks.

The resulting Hessian is reconstructed in the original coordinates by dividing each polarization by its own scale.

A Candidate-C early control at `a=0.025`, `k=0.1 h/Mpc` (`k ~= 300 H0`) is finite and stable under a factor-two amplitude-step change.

## 6. Local-shell production test — FAILED / shortcut rejected

After correcting the numerical scaling, the phase-averaged local Hessian was evaluated at fixed Candidate-C points while varying `kr`.

The result remains strongly shell dependent.  Representative at `a=0.025`, `k=0.1 h/Mpc`:

- `kr=1`: infinity norm about `2.0e13`;
- `kr=2`: about `5.1e12`;
- `kr=4`: about `1.3e12`;
- `kr=8`: about `3.3e11`;
- `kr=16`: about `9.9e10`.

The `L-L` entry shows approximately the same strong radial scaling over the first part of this sequence.

Therefore a finite spherical shell is **not** a radius-independent Fourier action.  This is the same class of boundary/constraint contamination already encountered in the earlier Aoki gradient scratch work.

Ruling:

`LOCAL_SPHERICAL_SHELL_FINITE_MU_HESSIAN = AUDIT_ONLY / NOT_PRODUCTION`.

Do not choose `r=1/k` and interpret the resulting matrix as the physical Candidate-C kinetic/gradient operator.

## 7. Targeted verification

Fresh reconstructed-workspace verification after the high-k conditioning repair covered:

- exact native finite-mu pullback;
- mu=0 bridge identities;
- independent HR lapse-source oracle;
- finite-mu correction Hessian and 16x16 embedding;
- Candidate-C native first/second background jets;
- early regular Stueckelberg branch jets;
- high-k finite-difference conditioning.

Result:

`14 passed`.

This is a targeted reconstructed-workspace result, not a full-repository GREEN claim.

## 8. Scientific ruling

- `FINITE_MU_NATIVE_HR_PULLBACK = BUILT`.
- `MU_ZERO_NATIVE_PREBD_BRIDGE = RECOVERED`.
- `FINITE_MU_HR_WEAK_SOURCE_ORACLE = GREEN`.
- `CANDIDATE_C_NATIVE_BACKGROUND_JETS = BUILT`.
- `EARLY_ADIABATIC_MU_S_JETS = BUILT_AS_CONTROL_ONLY`.
- `HIGH_K_HESSIAN_NUMERICAL_BRANCH_EXIT = FIXED`.
- `LOCAL_SHELL_HESSIAN_RADIUS_INDEPENDENT = NO`.
- `LOCAL_SHELL_HESSIAN_USABLE_FOR_FOLD_VERDICT = NO`.
- `COMPACT_SUPPORT_FINITE_MU_PROMOTION_REQUIRED = YES`.
- `GATE_2B = OPEN`.

## 9. Immediate next calculation

Promote the **compact-support action**, not the local shell matrix, to the finite-mu non-homothetic native pullback.

The correct next sequence is:

1. construct compact independent `L,T` profiles plus the four native metric potentials using `native_hr_potential_density` / the new native relative pullback;
2. subtract the same compact `mu=0` HR action to form `Delta S_HR(mu)`;
3. add this correction to the already validated compact/linear EH+dust architecture without altering those sectors;
4. first oracle: in the homothetic early-time limit recover the existing Aoki `K_S,c_S^2` result;
5. second oracle: as `mu -> 0` on Candidate C recover the finite-H De Felice/Stueckelberg action;
6. only then evaluate the reduced compact kinetic/gradient operators toward fold 1.

The arbitrary local radius must not re-enter the final verdict.
