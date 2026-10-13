# Late exact-dust matching audit

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **LATE LINEAR TRANSFER IS NOT UNIQUE WITHOUT TWO HELICITY-0 MATCHING DATA**

## Executive result

After separating the principal stability diagnostic from continuous mode identity, the strict Candidate-C-like dust benchmark becomes principal-stable only after approximately

`a ~= 0.10165`, `z ~= 8.84`

on `k=0.05...0.2 h/Mpc`.

Starting the linear calculation after that surface removes the earlier gradient-unstable interval, but it does **not** make the transfer prediction unique.

The physical matching conditions

- `delta_common = 1`,
- `delta_relative = 0`,
- `d delta_common/dN = 1`,
- `d delta_relative/dN = 0`

provide four linear constraints on the six-dimensional regular scalar phase space `(Y1,Y2,Y3,Y1_N,Y2_N,Y3_N)`.

Two independent phase-space directions remain free.  The historical late solver fixed them by imposing

`Y3 = 0`, `Y3_N = 0`.

That is a convention, not a consequence of the four adiabatic conditions and not a derived nonlinear/screened matching law.

## 1. Balanced matching system

The raw six-by-six matrix obtained after appending `Y3=0` and `Y3_N=0` is badly scaled in canonical coordinates.  At the representative healthy surface

`a_match = 0.12`, `k = 0.1 h/Mpc`,

its raw condition number is about `1.5e9` in the independent reconstruction.

Simple row/column equilibration reduces the numerical condition number to O(1e2) while preserving the physical solution and satisfying all six imposed constraints to about machine precision.

This shows that the large raw condition number is mostly a coordinate-scaling problem; it does **not** remove the two-dimensional physical matching freedom.

Production diagnostics are implemented in

- `numerics/candidate_c_dust_mode_projection.py`;
- `tests/test_candidate_c_dust_mode_projection.py`.

## 2. A fast relative-rich mode remains after the gradient boundary

At `a=0.12`, `k=0.1 h/Mpc`, the conditioned exact-dust local generator has a real growing root

`lambda_N ~= 7.6274...7.6276`

under derivative-step convergence from `1e-3` to `2e-3`.

For comparison, the other positive real root is only about `0.389` at this point.

The fast mode is relative-rich.  Its local observable ratio is approximately

`delta_relative / delta_common ~= 1.438`.

The historical `Y3=Y3_N=0` lift does not project it away.  A biorthogonal spectral projection of that lift gives, at the matching instant, contributions approximately

- common: `-4.16`;
- relative: `-5.98`;

which are cancelled by other local modes only at the initial instant to enforce total `(common,relative)=(1,0)`.

Because the modes have very different growth/decay rates, that instantaneous cancellation is not dynamically preserved.

## 3. Moving the matching surface later does not derive the missing data

Representative local fastest-mode diagnostics at `k=0.1 h/Mpc` are approximately

| a | max Re(lambda_N) | fast-mode relative/common |
|---:|---:|---:|
| 0.12 | 7.63 | 1.44 |
| 0.15 | 4.53 | 3.31 |
| 0.20 | 3.47 | 67.8 |
| 0.30 | 3.43 | -5.73 |
| 0.50 | 3.48 | -1.95 |
| 1.00 | 1.67 | -1.14 |

Thus delaying the matching surface avoids the principal gradient instability but does not make the second scalar sector disappear.  The fast eigenmode persists and undergoes strong changes of observable character.

## 4. Explicit two-parameter sensitivity

Let the two unfixed matching coordinates be

`u = Y3_i`, `v = Y3_N,i`,

while keeping the four physical common/relative conditions exactly fixed.

For `k=0.1 h/Mpc`, `a_match=0.12`, an independent 41-point conditioned reconstruction gives the approximate affine dependence at `z=0`

`delta_common,0 ~= 83.17 + 8.32e4 u + 3.13e2 v`,

`delta_relative,0 ~= -2468.7 - 2.65e6 u - 1.05e4 v`.

The numerical values are diagnostic rather than a final transfer table because the full branch suite cannot run in this environment, but the structural conclusion is robust: both free matching directions materially affect the final density observables.

In particular, an initial `Y3` of order `1e-3`, comparable to the scale of components in the historical base lift, can qualitatively change the final common/relative ratio.

The production helper `propagate_matching_sensitivity(...)` now exposes this Jacobian explicitly instead of hiding it behind `Y3=Y3_N=0`.

## 5. Consequence for the provisional large R values

Earlier provisional integrations gave large values such as `R(z=0) ~ 14`, `-30`, etc.  They cannot be promoted to physical predictions for two independent reasons:

1. the old start at `m_eff/H=1` traversed the principal unstable interval down to `z~8.84` on the relevant high-k scales;
2. even on a principal-stable later surface, the four adiabatic density conditions do not fix the two helicity-0 matching data.

Therefore the late linear subsystem alone does **not** predict a unique `R(z=0,k)`.

## 6. Scientific ruling

For the strict Candidate-C-like dust benchmark:

**A unique healthy late transfer function cannot be derived without a matching prescription from the earlier nonlinear/screened dynamics.**

This is stronger than saying that the present numerical initialization is inconvenient.  The missing information is two-dimensional phase-space data associated with the extra scalar sector.

Choosing those data to obtain a desired late segregation would be tuning unless they are produced by an independently derived nonlinear evolution.

## 7. Next required calculation

The next scientifically legitimate path is one of:

1. derive/evolve the nonlinear screened branch through the transition and read off the two helicity-0 matching data on the healthy late surface; or
2. if such a continuous healthy matching cannot be constructed, reject this Candidate-C branch for Gate 2B rather than fitting arbitrary late initial conditions.

Adding visible radiation to the final three-fluid solver remains necessary for the physical Candidate C, but radiation by itself does not supply the two missing helicity-0 phase data of the dust benchmark.

## Verification limitation

The local eigenvalue, modal-projection and matching-sensitivity numbers above were reproduced independently from the committed production formulas.  Full-repository GREEN is still unavailable because the container cannot clone GitHub and GitHub Actions are disabled.
