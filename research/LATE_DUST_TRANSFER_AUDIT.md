# Late exact-dust transfer audit

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **NUMERICALLY CONDITIONED / SCIENTIFIC VERDICT STILL OPEN, WITH A REAL EARLY-LATE INSTABILITY ON k >= 0.05 h/Mpc**

## Purpose

This checkpoint records the first time-domain work after the De Felice/Hassan-Rosen scalar action was closed on Case C and on the Candidate-C dust+dust local benchmark.

The subsystem is the deliberately restricted, strictly on-shell Candidate-C-like dust+dust benchmark.  It starts at its own `m_eff/H=1` crossing,

- `a_start = 0.057951440818742664`,
- `z_start = 16.25582635861885`,

and omits visible radiation consistently from both background and perturbations.

It is not yet the full physical Candidate C transfer solver.

## Numerical blockers closed

### 1. Exact quadratic polarization was losing mixed coefficients

The dust phase action is exactly quadratic, but its Hessian coefficients span powers up to `k^6`.  Unit-vector polarization therefore recovered small mixed terms by subtracting numbers as large as `~1e16` at the early/high-k control point.

The fix changes no physical coefficient.  Each perturbation coordinate is scaled using its diagonal quadratic curvature before four-point symmetric polarization, and the result is transformed back to the original variables.

Regression:

`test_candidate_dust_local_gravity_branch_converges_at_late_start`

Before conditioning, the extracted exact-dust gravity branch at `k=0.2 h/Mpc` changed from about `-0.0481` to `-0.00185` when the derivative step was halved.  After conditioning the two evaluations agree within the committed convergence tolerance.

### 2. Public output sampling must not define the dynamics

The original trajectory spline differentiated the physical Hessian on the same grid requested for public output.  At `k=0.2 h/Mpc`, `grid_size=61` gave an approximately 50% generator error relative to the conditioned direct local stencil.

The trajectory now uses two independent grids:

- `grid_size`: public/output sampling only;
- `coefficient_grid_size`: internal dynamical coefficients, default `41`.

At off-node control points the 41-point generator spline reproduces the direct conditioned generator at roughly `1e-6` relative or better, versus the committed acceptance threshold `2e-3`.

Regression:

`test_high_k_internal_coefficient_grid_is_independent_of_public_output_grid`

### 3. KKT momentum regression uses the actual floating-point floor

One canonical momentum is reconstructed as the difference of terms of order `~7e7` to obtain a number of order unity.  The old absolute tolerance was below the IEEE-754 subtraction floor.  The regression now keeps the same strict dust algebraic constraints but bounds the momentum residual by the larger of the historical tolerance and a scale-aware machine-rounding floor.

## Important mathematical ruling: exact dust and k-essence high-k limits do not commute

A temporary diagnostic incorrectly required the exact-dust time-domain system at the initial epoch to match the De Felice Eq. (86) gravity speed obtained from the finite-sound-speed k-essence system.

That test was not committed because the two limits are singular in opposite order.

After BD reduction, the exact-dust algebraic matter-momentum block contains an eigenvalue that scales approximately as `k^-2`.  A finite regulator `c_s^2=s>0` adds an algebraic term of order `s/rho`.  Therefore, for every fixed `s>0`, the regulator eventually dominates as `k -> infinity`, whereas that term is absent when `s=0` is imposed first.

Consequently:

- De Felice Eq. (86) remains the correct oracle for the regulated k-essence order of limits used in the earlier DF5 audit;
- it is not, by itself, a valid high-k oracle for the exact pressureless phase system with `c_s^2=0` imposed before `k -> infinity`.

This does not retract the earlier Case-C/Candidate-C finite-`c_s^2` action validation.  It only limits how that result may be used to validate the singular exact-dust transfer system.

## Local exact-dust spectrum at the planned start

Using the conditioned exact-dust DAE with derivative step `1e-3`, at `a_start`:

| k [h/Mpc] | max Re(lambda_N) | min Re(lambda_N) | three local squared phase-speed diagnostics |
|---:|---:|---:|---|
| 0.01 | 0.7300 | -4.2297 | `[2.46e-4, 5.34e-3, +1.13e-3]` |
| 0.05 | 3.6918 | -9.2451 | `[1.01e-5, 2.25e-3, -8.26e-3]` |
| 0.10 | 9.0194 | -15.4452 | `[2.47e-6, 5.64e-4, -8.43e-3]` |
| 0.20 | 21.1865 | -27.7407 | `[6.14e-7, 1.34e-4, -8.89e-3]` |

Interpretation:

- `k=0.01 h/Mpc` does not show the same negative gravity-gradient branch at the initial point; its positive local growth rate alone is not evidence of a gradient instability.
- `k=0.05, 0.10, 0.20 h/Mpc` do show a converged negative exact-dust gravity-gradient diagnostic at the intended initial epoch.
- The growth rate strengthens rapidly with k, as expected for a gradient-type pathology rather than ordinary scale-independent matter growth.

This means the planned `m_eff/H=1` matching surface is **not a healthy linear starting surface over three of the four required production scales**.

## Provisional transfer runs

These numbers are diagnostics, not a final Gate-2 transfer table.

At `k=0.1 h/Mpc`, using the conditioned 41-point coefficient grid, two ODE tolerances gave

- `R(z=0) = 14.3731518897` for `rtol=1e-7`,
- `R(z=0) = 14.3731518323` for `rtol=3e-9`.

The ODE itself is therefore converged at this level, but the large result is not evidence for a healthy Janus-like conversion: the initial GR-matched state has a substantial projection onto the locally growing branch and the interval begins in the negative-gradient regime.

At `k=0.05 h/Mpc`, a provisional conditioned run gave

- `R(z=0) ~= -30.30`.

At `k=0.01 h/Mpc`, a provisional conditioned run gave

- `R(z=0) ~= -12.61`.

The low-k result requires additional mode-identity/initial-lift auditing because its initial local gravity diagnostic is not negative.  No scientific conclusion should be drawn from the magnitude alone.

## Current scientific consequence

The first late-dust solver has **not** produced a healthy order-unity relative mode.

Instead, it has exposed a sharper discriminator:

> For the strict Candidate-C-like dust+dust benchmark, the intended linear start at `m_eff/H=1` already lies in an exact-pressureless scalar-gradient-unstable regime for `k >= 0.05 h/Mpc`.

The large relative amplitudes generated from that surface cannot be counted as successful segregation; they are contaminated/dominated by an unhealthy linear mode.

This is a negative result for the strict late dust benchmark as presently initialized.  It is not yet a proof that full Candidate C with visible radiation and nonlinear screening fails, because that physical problem has different matter content and may require matching from a nonlinear screened branch rather than declaring the system linear at `m_eff/H=1`.

## Next discriminating work

1. Track the exact-dust gravity branch continuously in `(a,k)` instead of re-sorting local eigenvalues independently.
2. Map the stability boundary `c_s^2=0` / growing-gradient onset over `k=0.01...0.2 h/Mpc`.
3. Audit the GR-connected initial lift with scale-balanced variables and continuous stable/unstable subspaces.
4. For scales that possess a genuinely healthy late interval, measure conversion only after a mathematically defined stable matching surface.
5. Do not promote the provisional `R` values to `T_gg,T_gf,T_fg,T_ff` until the matching problem is solved.
6. If the physically relevant Candidate-C scales cannot be connected to the healthy late branch without traversing the unstable interval, record Gate 2B as failed for this candidate and move to parameter/branch rejection rather than fitting the transfer output.
