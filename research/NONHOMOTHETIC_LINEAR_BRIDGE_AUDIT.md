# Candidate C — non-homothetic linear Stueckelberg bridge audit

Date: 2026-10-16
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **PRINCIPAL DE FELICE↔STUECKELBERG MAP CLOSED; FINITE-H TIME-DEPENDENT REDUCTION STILL OPEN**

## Purpose

The homothetic compact six-field action is already calibrated against Aoki's nonlinear scalar action.  The next mandatory oracle is the actual non-homothetic Candidate-C linear limit `mu -> 0`, where the result must agree with the independently validated De Felice/Hassan-Rosen principal scalar.

A naive promotion of the homothetic Aoki map failed this oracle.  This audit isolates the failure without tuning any interaction coefficient or sound speed.

## 1. Native conformal background jets

The two natural conformal charts are not interchangeable when `c != 1`.

For the g chart,

`a'_g = a H`,

`a''_g = a (H^2 + H')`.

For the f natural conformal time, with

`d eta_f / d eta_g = c`,

and `b=a xi`, the dynamical branch gives

`db/d eta_f = b H`,

`d2b/d eta_f2 = b (H^2 + H'/c)`.

These identities are implemented in

- `numerics/nonhomothetic_compact_background.py`;
- `tests/test_nonhomothetic_compact_background.py`.

The reconstructed targeted test was `3 passed`.

## 2. Exact gauge bridge to De Felice variables

Put the relative coordinate displacement in the g chart, then perform the common transformation to g-flat gauge.  In De Felice variables,

`E_f = -2 L`,

`psi_f + k^2 E_f/6 = - n H_f T`.

Therefore

`T = - [1/(n H_f)] (psi_f + k^2 E_f/6)`,

`L = -E_f/2`.

This is exactly compatible with De Felice Eq. (72), since a pure relative diffeomorphism has

`q_f = [1/(n H_f)] (psi_f + k^2 E_f/6) = -T`.

The time derivative and induced f lapse/shift are also pinned in

- `numerics/nonhomothetic_linear_stueckelberg_bridge.py`;
- `tests/test_nonhomothetic_linear_stueckelberg_bridge.py`.

Fresh reconstructed verification after the principal-map extension: `5 passed`.

## 3. Independent extraction of the principal non-homothetic map

An independent scratch reconstruction of the committed exact-dust Candidate-C local DAE was used.  It reproduced the expected gravity branch near `a=0.5`; representative squared-speed estimates were approximately

| k | gravity `c_s^2` |
|---:|---:|
| 100 | 0.72997 |
| 200 | 0.69987 |
| 400 | 0.69232 |
| 800 | 0.69044 |

The independent principal target is

`c_s^2 = 0.692071477288...`.

For the oscillatory gravity eigenvector, reconstruct `Z` with the committed time-dependent BD map and then reconstruct `(T,L)` with the gauge bridge above.  The ratio

`[(T/L)/(-lambda)]`

converges in its real part to

`a^2/c`.

Representative high-k values are:

| a | c | extracted at k=3200 | `a^2/c` |
|---:|---:|---:|---:|
| 0.3 | 0.8222461 | 0.1094746 + 0.00708 i | 0.1094563 |
| 0.5 | 0.9370846 | 0.2668165 + 0.02862 i | 0.2667849 |
| 0.7 | 0.9736869 | 0.5033082 + 0.08904 i | 0.5032418 |

The imaginary correction decreases with increasing k.  The principal map is therefore

`delta eta = -(1/(c a^2)) partial_eta pi`,

`delta r   = +(1/a^2) partial_r pi`,

or equivalently in g cosmic time

`T/Ldot -> -a^2/c`.

This reduces to the homothetic Aoki map when `c -> 1`.

This result is exposed deliberately as a **principal-symbol** helper only.  It must not be used to invent the finite-H subleading map.

## 4. Why the corrected principal map is not yet the finite-H answer

Injecting only the missing `1/c` factor into the compact one-profile Schur does **not** recover the De Felice Candidate-C speed.  Even on smaller sub-horizon compact supports the fitted result remains incompatible with `0.692071...`.

This does not invalidate the principal bridge.  It shows that the finite-H reduction is not determined by the principal coordinate map alone.

Two structural effects remain:

1. the matter scalars respond dynamically to the gravity mode and cannot be represented as arbitrary static Schur amplitudes;
2. on a non-homothetic evolving background the reduced matrices are time-dependent, so the physical equation contains `Kdot` and `Cdot` terms.

The latter is exactly the failure mode previously found and repaired in DF5e.5.  A frozen-coefficient Schur must therefore not be used as the Candidate-C linear acceptance equation.

## 5. Frozen-background subtraction is invalid

A proposed shortcut was to subtract an instantaneous reference with the same `(a,xi,c,rho_g,rho_f,m^2)` but with all background derivatives set to zero.

That reference is off-shell: setting `H=0` while retaining the interaction and matter densities destroys the Friedmann cancellation.  Its tadpoles and quadratic coefficients therefore have no invariant physical interpretation.

`FROZEN_OFFSHELL_SUBTRACTION = REJECTED`.

## 6. Time-dependent reducer restored to the active branch

The generic time-dependent quadratic reducer from the historical `research/v2-flrw` line has been ported into the active branch:

- `numerics/time_dependent_quadratic_reduction.py`;
- `tests/test_time_dependent_quadratic_reduction.py`.

It retains

- the derivative `Cdot` when eliminating a kinetic-null coordinate;
- `Kdot` and `Cdot` in the Euler-Lagrange matrices;
- the `Rdot` term in the De Felice Eq. (72) map.

Fresh reconstructed verification: `4 passed`.

## 7. Scientific ruling

- `NONHOMOTHETIC_PRINCIPAL_PI_MAP = DERIVED`.
- `MISSING_TIME_MAP_FACTOR = 1/c`.
- `HOMOTHETIC_MAP_USED_UNCHANGED_ON_CANDIDATE_C = INVALID`.
- `FROZEN_OFFSHELL_SUBTRACTION = INVALID`.
- `STATIC_COMPACT_SCHUR_SUFFICIENT_FOR_MU_TO_0_ORACLE = NO`.
- `TIME_DEPENDENT_CONSTRAINT_REDUCTION_REQUIRED = YES`.
- `DE_FELICE_LINEAR_ORACLE_PASSED_BY_NEW_NATIVE_ACTION = NOT YET`.
- `GATE_2B = OPEN`.

## 8. Immediate next calculation

Construct local non-homothetic quadratic matrices before the final scalar reduction,

`L2 = 1/2 qdot^T K qdot + qdot^T C q + 1/2 q^T Q q`,

on one strict on-shell Candidate-C dust trajectory.

Then:

1. eliminate only genuine algebraic metric constraints;
2. differentiate the reduced coefficients along the same on-shell trajectory;
3. perform the time-dependent null/BD reduction with `Cdot` retained;
4. construct the full Euler-Lagrange matrices including `Kdot` and `Cdot`;
5. require the `mu -> 0` gravity pair to converge to the independent De Felice target `c_s^2 ~= 0.692071477288` at `a=0.5`.

Only after that oracle is GREEN may the same pre-reduction construction be evaluated at finite nonlinear `mu` near the first fold.

## Verification limitation

The De Felice-to-Stueckelberg convergence table above comes from an independent reconstructed scratch implementation of the committed exact-dust equations.  The new small modules have targeted RED/GREEN verification, but the full repository suite is still unavailable because GitHub Actions are disabled and the current container cannot clone GitHub.
