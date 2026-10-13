# DF5e.4 — pressure-consistent time-dependent BD canonicalization

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **kinetic branch implemented and verified in executable subset; full-repository suite still unavailable.**

## Result

DF5e.4 resolves the finite-k De Felice kinetic invariant `NG3` without changing any physical coefficient.

The two required ingredients are:

1. follow the local P(X) pressure tangent when differentiating the BD mixed coefficient,
   `dot P_f = -3 n H_f c_sf^2 (rho_f+P_f)`;
2. integrate the complete `C[:,Z] Zdot` column by parts with the `N a^3` measure, including `dot c_i + 3 H c_i`.

A second numerical issue was found while implementing this: differentiating a Hessian that is itself obtained by finite-differencing the nonlinear HR potential is unnecessarily noisy.  The repository already contains the direct O(delta^2) De Felice Eqs. (45)-(46) interaction, `hr_scalar_quadratic_action_density_de_felice`.  DF5e.4 therefore uses a separate exact-quadratic Hessian backend.  This changes no HR coefficient.

## Committed implementation

- `numerics/bd_time_canonicalization.py`
  - generic background-agnostic integration-by-parts helper;
  - receives `dot_c` and `mu_measure` explicitly.
- `numerics/de_felice_two_matter_exact_quadratic.py`
  - same EH and P(X) pieces and same auxiliary Schur complement as the baseline reducer;
  - HR contribution is evaluated directly from the already-quadratic Eqs. (45)-(46) helper.
- `numerics/de_felice_bd_audit.py`
  - pressure-consistent `h_ZZ^eff`;
  - full Case-C time-dependent BD adapter;
  - uses the exact-quadratic backend for differentiated coefficients.
- regressions:
  - pressure-chain rule;
  - synthetic time-dependent canonicalizer;
  - Eq. (78) NG3 at `k=100,200,400,800`.

## Fresh executable-subset verification

The current environment cannot clone the full repository and GitHub Actions remain disabled.  A minimal executable workspace reconstructed from the committed formulas was therefore used for the DF5e.4 numerical checks.

Fresh run:

- pressure-chain + canonicalizer tests: `2 passed`;
- Eq. (78) NG3:
  - `k=100`: measured `0.0158886855`, target `0.015890`, relative `-0.008%`;
  - `k=200`: measured `0.0179238512`, target `0.017943`, relative `-0.107%`;
  - `k=400`: measured `0.0184631480`, target `0.0185421788`, relative `-0.426%`;
  - `k=800`: measured `0.0191642249`, target `0.018698`, relative `+2.493%`.

All four satisfy the existing `3%` Eq. (78) regression tolerance.  This is **not** a claim that the full repository suite is green.

At `a=0.05,k=400,c_sf^2=0.1`, the stable exact-quadratic audit gives `h_ZZ^eff ~= 6.7414`, consistent with the Eq. (78)/(79) value near `6.7418`.

## New hard finding: the old frozen speed extractor is not the De Felice dispersion relation

The Case-C three-speed regression remains RED.  This is a distinct problem from NG3.

The old helper `physical_squared_phase_speeds()` assumes frozen coefficients and solves

`K Yddot + (C.T-C) Ydot - M Y = 0`.

De Felice Eq. (73), however, has a time-dependent measure and time-dependent matrices.  Eq. (84) gives, for `N=1`,

`K Yddot + (dot K + 3 H K + 2 Nmat) Ydot + (dot Nmat + 3 H Nmat + M_DF) Y = 0`,

and Eq. (85) is the corresponding high-frequency dispersion relation.  In repository Hessian conventions,

- `C = -Nmat`;
- `M_hessian = -M_DF`;

so the same equation is

`K Yddot + (dot K + 3 H K + C.T-C) Ydot + (dot C.T + 3 H C.T - M_hessian) Y = 0`.

Therefore the frozen extractor is not a valid final acceptance test once time-dependent canonicalization is restored.

A direct nested finite-difference attempt at Eq. (85) is numerically ill-conditioned: the gravity state coefficient is obtained by cancellations of roughly nine orders of magnitude.  The two matter branches remain near their expected principal values, while the gravity branch is unstable under the outer derivative step.  Do not interpret that unstable number as a new physical instability.

## Next task — DF5e.5

**DF5e.5 — reconstruct the De Felice Eq. (85) principal dispersion from the reduced action without catastrophic cancellation.**

1. Keep DF5e.4 NG3 regressions fixed.
2. Treat Eq. (84)/(85), not the frozen Hessian eigenproblem, as the scalar-speed acceptance equation.
3. Obtain `dot K` and `dot Nmat` in a conditioned way:
   - preferably analytic differentiation of the exact-quadratic Schur/basis operations, or
   - an equivalent high-k principal reduction that can be compared term-by-term to Eq. (86).
4. Require the Case-C gravity branch to recover the independent target `c_s^2=-0.6665833419871022` while the matter branches recover `c_g^2` and `ctilde^2 c_f^2`.
5. Only then move to Candidate C / DF5d.

## Non-negotiable constraints

- no coefficient tuning;
- do not remove `-3 n H_f c_sf^2` from the f-field drift;
- keep the corrected HR shift-volume terms;
- keep GR one-metric degeneracy;
- do not claim the full suite green until an actual full repository worktree executes it.
