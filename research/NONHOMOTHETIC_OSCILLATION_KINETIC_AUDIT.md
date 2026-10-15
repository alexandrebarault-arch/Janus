# Candidate C — nonlinear oscillation kinetic-sign audit

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **HOMOGENEOUS NONLINEAR-BRANCH KINETIC ORACLE CALIBRATED; FIRST-FOLD KINETIC DEGENERACY STRONGLY INDICATED, FULL DYNAMICAL ACTION STILL OPEN**

## Purpose

`NONHOMOTHETIC_FOLD_AUDIT.md` established that the finite weak-metric adiabatic regular pair disappears at

`a_1 ~= 0.03016463`, `z_1 ~= 32.1514`, `mu_1 ~= -0.7688837`.

The missing question is whether the omitted oscillating helicity-0 mode can dynamically cross that fold.  A necessary condition is that its kinetic sector remain nondegenerate.  This audit constructs a deliberately limited homogeneous velocity Hessian from the exact spherical HR pullback and calibrates its sign against Aoki-Maeda-Namba before applying it as a local diagnostic.

It is **not** yet the full spatial Stückelberg action and does not determine `c_S^2`.

## Crucial correction to the scratch calculation

The adiabatic homothetic map contains

`sigma_bg = -(a H/2) mu(2+mu) r^2`.

The first scratch Hessian kept `sigma'_bg` but accidentally set `dot(sigma_bg)=0`.  That omission is of the same `(aHr)^2` order as the kinetic term itself.

For a constant-`w` homothetic control normalized at `a=H=1`,

`dot(sigma_bg) = -(1 + dot(H)/H^2) mu(2+mu) r^2/2`.

Restoring this term changes the result qualitatively and is mandatory.

## Homothetic Aoki calibration

Define the exact spherical HR interaction action on a small ball and vary independently the homogeneous velocity perturbations

`delta mu_dot`, `delta sigma_dot`.

The resulting 2x2 velocity Hessian has one physical eigenvalue and one constraint/null direction.

For nonlinear Aoki roots with positive interaction normalization

`D = beta1 K + 2 beta2 K^2 + beta3 K^3 > 0`,

the sign of the non-null Hessian eigenvalue was compared with Aoki's analytic

`K_S = (3/4)(3w-1)(2+mu)(1+2 B2 mu+B3 mu^2)`

for pressureless controls.

A broad scratch scan gave

`27 / 27` sign agreements for admissible nonlinear dust roots with `D>0`.

The apparent three counterexamples in the pre-correction scan all had `D<0`, outside the positive-effective-mass assumption used by the Aoki stability criterion.

The repository regression pins both positive- and negative-`K_S` examples and verifies that the single physical sign is stable against radius and finite-difference-step changes.

Important scope restriction: the separate linear `mu=0` branch is not represented by this nonlinear-root oracle.  The homogeneous Hessian is therefore not a substitute for the already validated De Felice linear action.

## Candidate-C leading non-homothetic application

For the exact early non-homothetic adiabatic pair of `NONHOMOTHETIC_STUECKELBERG_AUDIT.md`, the same exact pullback diagnostic was evaluated with the actual Candidate-C dust `xi(a), c(a), H(a)` and with the background `mu_N` and `sigma` drift taken along each algebraic branch.

Representative signs are:

| a | more-negative root | signature | less-negative root | signature |
|---:|---:|:---:|---:|:---:|
| 0.010 | -0.93058 | + | -0.36196 | - |
| 0.020 | -0.86536 | + | -0.65408 | - |
| 0.025 | -0.82545 | + | -0.68715 | - |
| 0.029 | -0.78382 | + | -0.71046 | - |

Thus only one member of the early regular pair carries the Aoki-calibrated positive nonlinear kinetic signature.

## Kinetic-sign zero before the first fold

Following the more-negative regular branch toward its leading-order merger, the physical homogeneous velocity eigenvalue changes sign.

A bracketed solve gives

`a_K ~= 0.030136993`,

`z_K ~= 32.18181`,

`mu_K ~= -0.76624`.

This zero is numerically extremely stable.  A 16-point scan over

- radial integration radius `R = 0.003, 0.005, 0.008, 0.012`;
- velocity Hessian step `h = 0.003, 0.006, 0.01, 0.02`;

kept the zero within approximately

`0.030136989 < a_K < 0.030137012`.

The finite weak-metric fold independently found from the full local adiabatic residual is

`a_1 ~= 0.03016463`.

The relative separation is only

`|a_1-a_K|/a_1 ~= 9.2e-4`.

This near-coincidence is a strong warning that the regular-branch fold is associated with a kinetic degeneracy / strong-coupling surface, rather than being merely an innocent algebraic turning point.

## Why this is not yet a no-go theorem

The kinetic diagnostic above uses the exact nonlinear HR pullback but not the **oscillation-mode weak Einstein constraints** at finite `m_eff/H`.  Those weak metric perturbations are small in amplitude, but the first fold occurs at finite `m_eff/H`, so their contribution to the quadratic kinetic operator cannot be assumed zero merely from their small background amplitude.

Also, the full scalar stability problem requires the spatially dependent Aoki mode `pi`; the homogeneous velocity Hessian does not determine the gradient coefficient `c_S^2`.

Therefore the current result is:

- much stronger than the old algebraic fold topology alone;
- a concrete target for the full dynamical reduction;
- **not** yet proof that every nonadiabatic trajectory must hit a ghost/kinetic zero.

## Implementation / targeted verification

Added:

- `numerics/nonhomothetic_oscillation_kinetic.py`;
- `tests/test_nonhomothetic_oscillation_kinetic.py`.

Targeted reconstructed-workspace verification on 2026-10-15:

`3 passed`.

The broader 27/27 homothetic sign scan and the 16-point Candidate-C zero-conditioning scan were independent scratch checks.  GitHub Actions remain disabled; this is not a full-repository GREEN claim.

## Next calculation

Derive the **spatially dependent quadratic oscillation action** around the nonlinear non-homothetic branch, retaining

`(phi_g, psi_g, phi_f, psi_f, delta eta, delta r)`

until the weak metric constraints are eliminated.

First oracle: in the homothetic `H >> m_eff` limit recover Aoki Eqs. (4.50)-(4.56), including both `K_S` and `c_S^2`.

Second oracle: in the `mu -> 0` Candidate-C limit recover the already validated De Felice linear principal scalar.

Only after both oracles pass should the finite-`m_eff/H` kinetic eigenvalue be evaluated through `a ~= 0.03016` and the fold interval integrated.
