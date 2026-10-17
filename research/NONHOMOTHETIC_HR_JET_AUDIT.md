# Gate 2B — finite-mu native Hassan–Rosen quadratic-jet audit

Date: 2026-10-17
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **FINITE-MU NATIVE METRIC-INTERACTION HESSIAN BUILT AND INDEPENDENTLY TESTED; COMPLETE NONLINEAR AUGMENTED ACTION STILL OPEN**

## Purpose and strict scope

Extend the exact quadratic Hassan–Rosen (HR) interaction **as a geometric building block**, without replacing the validated Einstein–Hilbert, exact-dust, pre-BD, or time-dependent reduction equations.

Added:

- `numerics/hr_native_quadratic_jet.py`
- `tests/test_hr_native_quadratic_jet.py`

The new routine `native_hr_scalar_jet(...)` returns `value,gradient,hessian,radial_jacobian` for the **interaction-only** density

`-m2 Mg2 sqrt(-g) sum(beta_n e_n(sqrt(g^-1 f)))`.

It uses the exact spherical two-by-two HR square-root identities, **not** finite differences of a nearly constant nonlinear potential. Eight native metric perturbations are ordered

`(Phi_g,B_g,psi_g,E_g,Phi_f,B_f,psi_f,E_f)`.

They include the two lapse perturbations, shifts, scalar traces, and Fourier scalar longitudinal shears.

## Finite-mu background chart

At a fixed cosmic-time point the relative radial chart is

`T=t+sigma(t) r^2/2, R=(1+mu(t)) r`,

`J_f=[[1+sigma_dot*r^2/2, sigma*r], [mu_dot*r,1+mu]]`.

The metric in the common chart is `f_common=J_f.T f_native J_f`, while `g` is in its native chart. The exact central background square root is

`S(r=0)=diag(n/N,xi*(1+mu),xi*(1+mu),xi*(1+mu))`,

so **at the center only**, the HR Hessian coincides algebraically with the De Felice Eq. (45)-(46) interaction evaluated with `alpha_eff=alpha*(1+mu)`. This is an exact local identity, not a promotion of the full cosmological action by an instantaneous `xi -> xi*(1+mu)` substitution.

The second-order jet computes product, reciprocal and positive square root derivatives by exact chain rules. This avoids subtracting large background and linear terms to infer the quadratic Hessian.

## Independent checks

Local reconstructed command:

`PYTHONPATH=. OPENBLAS_NUM_THREADS=1 pytest -q tests/test_hr_native_quadratic_jet.py`

Result: **10 passed in ~5 seconds** (JAX-based controls skipped only if JAX is absent).

The tests independently check:

1. all 8x8 De Felice Eqs. (45)-(46) Hessian entries at `mu=0`, including the full shift block;
2. the **finite-mu central** HR identity with `alpha_eff`;
3. `beta_0 sqrt(-g)` independent of all f metric perturbations;
4. `beta_4 sqrt(-f)` independent of all g metric perturbations, even with finite radial pullback;
5. zero-interaction-mass and regular positive radial-Jacobian guards;
6. **independent JAX x64 automatic-differentiation Hessians**, both at `mu=0` and at nonzero `mu,r,sigma,sigma_dot,mu_dot`, agreeing to `~3e-12` absolute/relative test tolerances;
7. radial parity: the nonshift/nonshift block starts at `O(r^2)` while the pointwise mixed shift/nonshift block starts at `O(r)`. The tests verify the near-center factors 4 and 2 on doubling radius.

A real feature RED was additionally witnessed by temporarily replacing the implementation with a `NotImplementedError` stub; the beta4 test failed, and after restoration all 10 tests passed.

## Significant limitation — do NOT overinterpret

This is a **local frozen-background interaction jet**. For finite `r` the f lapse `n(T)` and scale `alpha(T)` have deliberately been held at their central time values. The actual on-shell `O(r^2)` action must also include their drift along the Stückelberg time shift.

Furthermore:

- the Hessian presently varies the **eight metric fields**, not yet independent finite-mu oscillatory Stückelberg perturbations `delta T,delta R`;
- a pointwise radial real-matrix result is **not** already the phase-averaged Fourier action. Odd shift couplings require correct phase/parity handling;
- EH and dust are not contained in this helper;
- the linear `mu=0` **interaction block** is recovered, but the finite-mu **six-dimensional dispersion, constrained kinetic/gradient operator, and fold crossing are NOT**;
- the full repository test suite has not run (GitHub Actions disabled; clone DNS unavailable).

Thus there is no finite-mu stability verdict from this computation.

## Next exact implementation step (RAF)

1. Extend the interaction Hessian to **native Stückelberg map perturbations**, retaining Jacobian and angular-radius perturbations before any Fourier specialization: `delta T, delta R, delta T_t, delta T_r, delta R_t, delta R_r`. Include native background `n(T),alpha(T)` time derivatives to the required `O(r^2)` order.
2. Verify the `mu->0` limit **after** applying the existing `direct_native_augmented_transform`, so that the 16-dimensional pre-metric Hessian reproduces the known Candidate-C linear augmented interaction.
3. Independently verify the homothetic nonlinear compact-support Aoki `K_S,c_S^2` limit after metric Schur, with correct space/time integration and constraints.
4. Keep the two dust canonical phase pairs dynamical through the null-`Tdot` reduction.
5. Only after BOTH limits are GREEN, approach the first Candidate-C fold `a_1 ~ 0.0301646` and test the fully constrained kinetic/gradient operator.

Do not use the finite-radius frozen-background Hessian itself to decide whether the fold can be crossed.

`GATE_2B = OPEN`.
