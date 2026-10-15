# Candidate C — non-homothetic weak-metric transition audit

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **PARTIAL DERIVATION CLOSED; EXACT FOLD BOUNDS IN PROGRESS**

## Purpose

This audit supersedes the instantaneous substitution `K -> xi(a)` used in the earlier Aoki proxy.  The goal is to derive, on the actual non-homothetic Candidate-C dust background, the screened Stückelberg branch and the finite weak-metric corrections needed before a dynamical screened-to-linear matching can be attempted.

Gate 2B remains OPEN.  Nothing in this file supplies the two late helicity-0 matching data `(Y3,Y3_N)` yet.

## Exact spherical pullback

A new exact helper,

- `numerics/nonhomothetic_stueckelberg.py`,

computes the elementary symmetric polynomials of `S=sqrt(g^{-1}f)` after the spherical Stückelberg pullback

`T=t+chi(t,r)`, `R=R(t,r)`.

The identity map reproduces exactly

`S = diag(n,xi,xi,xi)`.

For the local uniform radial mode

`chi = s(t) r^2/2`, `R=(1+mu(t)) r`,

the leading temporal Euler equation factorizes into an interaction factor and a kinematic factor.  On the interaction branch,

`s = -(a^2/c) [ dot(mu) + H mu (c+1+mu) ]`.

For `c=1` this reduces exactly to Aoki-Maeda-Namba Eq. (64) after converting their conformal-time relation to cosmic time.

The interaction factor is

`beta1 + 2 beta2 xi (1+mu) + beta3 xi^2 (1+mu)^2`,

which reduces to `J` at `mu=0`.

## Leading non-homothetic adiabatic radial equation

After imposing the temporal relation, the leading radial equation has a separate linear factor `mu=0`.  The two nonlinear branches satisfy

`A2 mu^2 + A1 mu + A0 = 0`,

with `e = dot(H)/H^2`,

`A2 = xi [ beta2 + beta3 xi (c+e+1) ]`,

`A1 = beta1 + beta2 xi (c+2e+5) + beta3 xi^2 (3c+2e+2)`,

`A0 = beta1 (e+3) + 2 beta2 xi (c+e+2) + beta3 xi^2 (2c+e+1)`.

For `c=1` and `e=-3(1+w)/2`, the coefficient ratios reduce exactly to the polynomial whose roots are Aoki Eq. (68).

On strict Candidate-C dust, this leading non-homothetic pair merges near

`a ~= 0.03083065`, `z ~= 31.44`,

with representative values

`xi ~= 1.93860`, `c ~= 0.23608`, `mu_merge ~= -0.7419`,

and `m_eff/H ~= 0.544`.

Because `m_eff/H` is not asymptotically small there, this leading result is not by itself a final transition verdict.

## Weak-metric interaction sources from Hassan-Rosen Y tensors

The four weak-metric source polynomials were reconstructed directly from the diagonal Hassan-Rosen interaction tensors rather than copied from Aoki.

For a homothetic background, the reconstructed combinations reproduce Aoki Eqs. (98)-(101) exactly, including the `(1+mu)^-3` f-sector factors.  This provides an independent convention oracle for the metric-response part of the transition calculation.

The same tensor construction is well defined for non-homothetic

`S = diag(xi c, xi(1+mu), xi(1+mu), xi(1+mu))`.

At the leading Candidate-C fold the radial weak sources differ qualitatively from the naive `c=1, K->xi` proxy.  Representative normalized values are

- g temporal: about `-0.276` in both cases;
- g radial: non-homothetic about `-0.213`, naive homothetic about `+0.547`;
- f temporal: about `+1.437` in both cases;
- f radial: non-homothetic about `+0.334`, naive homothetic about `-2.654`.

Thus the lapse ratio `c` cannot be omitted from the finite weak-metric correction.

## Important mass-normalization correction

Outside the homothetic limit, the static weak-metric sources are controlled by

`D = xi J = beta1 xi + 2 beta2 xi^2 + beta3 xi^3`,

not by the propagation coefficient `Gamma`.

In the repository conventions (`kappa=alpha^2` with `alpha=M_f/M_g`), the source mass scales are

`m_g^2 = m^2 D`,

`m_f^2 = m^2 D / (alpha^2 xi^2)`.

The propagation mass entering the linear principal mode instead contains `Gamma`.

At the leading fold,

`D ~= 69.75`, `Gamma ~= 5.78`, `Gamma/D ~= 0.0829`.

Using the propagation mass to source the weak metric would therefore underestimate the finite correction by roughly a factor 12.  All transition calculations after this point use `D=xi J` for the weak Einstein sources.

## Automatic-differentiation oracle against full Aoki equation

Nested finite differences in the local Stückelberg Euler equations were too cancellation-prone.  Independent scratch calculations therefore used JAX x64 automatic differentiation for the Euler-Lagrange derivatives.  JAX is not introduced as a production dependency; it is an audit/oracle.

Two homothetic validations are closed:

1. with weak metric sources off, the exact radial Euler equation reproduces the nonlinear Aoki Eq. (68) roots;
2. after injecting the four weak potentials, the exact pullback reproduces the roots of Aoki's full `C_H^2 + C_m^2 = 0` equation to about `1e-6` or better over several independent `(m_g^2,m_f^2)` choices.

Example for the Candidate-like coupling control with `(m_g^2,m_f^2)=(0.02,0.04)`:

- exact-pullback auto-diff roots: approximately `-0.89438863`, `-0.30769990`, `0`;
- Aoki full-polynomial roots: approximately `-0.89438863`, `-0.30769909`, `0`.

This validates the finite weak-metric insertion procedure before applying it to `c != 1`.

## Candidate-C finite correction at the leading fold

At `a ~= 0.03083065`, with the correct `D=xi J` source masses, the finite weak-metric corrected local radial equation no longer contains the regular double root near `mu ~= -0.742`.

The nonzero real root found by the exact-pullback auto-diff calculation is instead

`mu ~= -0.96315`,

very close to the singular map `mu=-1` where `R=(1+mu)r` collapses.

The result is insensitive to artificial local changes of `dot(mu)` and `ddot(mu)` in the adiabatic audit.  Repeating the calculation in `N=ln a` with the actual local Candidate-C derivatives also leaves the same structure.  At the fold the measured derivatives are approximately

`c_N ~= 0.10418`, `c_NN ~= 0.17435`,

`d(dot H/H^2)/dN ~= -1.03e-3`,

and the corrected root remains near `-0.96315`.

This is evidence that the disappearance of the regular pair is not an artifact of freezing `c`, but the exact fold locations still need to be solved with a conditioned continuation calculation.

## Provisional branch track — not yet the final fold bound

A cheaper constant-`c` continuation shows the regular weak-corrected pair present at early times, absent around `a~0.031-0.04`, and present again by `a~0.05`, while a near-singular branch close to `mu=-1` persists.

Because that broad scan froze derivatives of `c`, it is only a locator.  It must not be quoted as the final transition window.

## Current scientific ruling

- `EXACT_NONHOMOTHETIC_TEMPORAL_STUECKELBERG_RELATION = DERIVED`.
- `LEADING_NONHOMOTHETIC_RADIAL_BRANCH = DERIVED`.
- `AOKI_EQ68_HOMOTHETIC_LIMIT = RECOVERED`.
- `AOKI_WEAK_METRIC_SOURCES_98_101_FROM_HR_TENSORS = RECOVERED`.
- `FULL_AOKI_FINITE_WEAK_METRIC_ROOTS = REPRODUCED_BY_EXACT_PULLBACK`.
- `WEAK_SOURCE_MASS_USES_XI_J_NOT_GAMMA = YES`.
- `REGULAR_NONLINEAR_PAIR_SURVIVES_AT_LEADING_FOLD_AFTER_FINITE_CORRECTION = NO` in the local audit.
- `NEAR_SINGULAR_MU_APPROX_MINUS_0_963_BRANCH_IS_PHYSICALLY_VIABLE = NOT ESTABLISHED`.
- `EXACT_NONHOMOTHETIC_FOLD_BOUNDS = IN PROGRESS`.
- `DYNAMICAL_OSCILLATING_HELICITY0_TRANSITION = NOT YET DERIVED`.

## Immediate next calculation

Do not rescan hundreds of `mu` values with nested JAX differentiation.  Solve the fold directly by continuation/Newton on

`E_R(mu,a)=0`, `partial E_R / partial mu = 0`,

using one compiled parameterized auto-diff residual and the exact local Candidate-C derivatives.  Locate both disappearance and reappearance folds and test whether the continuing roots remain a safe distance from `mu=-1` and whether the weak-metric expansion remains controlled.

Only after the branch topology is pinned should the oscillating nonlinear helicity-0 mode be derived and matched to `(Y3,Y3_N)`.

## Verification limitation

The hard identities above were checked with targeted reconstructed workspaces and independent auto-diff scratch calculations.  GitHub Actions remain disabled and a complete repository worktree is still unavailable; this is not a global test-suite claim.
