# Non-homothetic Stückelberg audit — Candidate-C dust

Date: 2026-10-14
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **exact early adiabatic non-homothetic reduction derived; finite-mass transition still open**

## Purpose

The late exact-dust transfer system is underdetermined by two helicity-0 matching data, `(Y3,Y3_N)`.  The previous Aoki instantaneous proxy inserted `K -> xi(a)` into formulas derived for a homothetic background.  This document replaces that proxy at early/adiabatic order with a direct spherical Stückelberg pullback of the Hassan-Rosen interaction on the actual non-homothetic FLRW background.

This is still not the complete transition solver.  It establishes the exact adiabatic constraint and identifies where finite metric corrections become indispensable.

## Exact spherical pullback

Use g-cosmic coordinates

`ds_g^2 = -dt^2 + a(t)^2 (dr^2+r^2 dOmega^2)`

and an f-FLRW metric in its own coordinates `(T,R)` with lapse `n(T)` and scale factor `alpha(T)`.  Pull f back with arbitrary spherical Stückelberg fields `T(t,r), R(t,r)`.

For the `(t,r)` block,

`f_tt = -n^2 T_t^2 + alpha^2 R_t^2`,

`f_tr = -n^2 T_t T_r + alpha^2 R_t R_r`,

`f_rr = -n^2 T_r^2 + alpha^2 R_r^2`.

With `A = g_2^{-1} f_2`, the principal 2x2 square-root invariants are

`det S_2 = sqrt(det A)`,

`tr S_2 = sqrt(tr A + 2 sqrt(det A))`,

while the repeated angular eigenvalue is

`ell = alpha R/(a r)`.

These determine all five elementary symmetric polynomials exactly.  The identity pullback `T=t, R=r` reproduces the FLRW spectrum `(n,xi,xi,xi)` to machine precision.

Implementation: `numerics/nonhomothetic_stueckelberg.py`.

## Temporal Stückelberg constraint

For the local uniform ansatz

`T = t + s(t) r^2/2`,

`R = (1+mu(t)) r`,

expand the exact interaction Euler equation at leading nontrivial radial order.  The temporal equation factorizes into an interaction factor

`beta1 + 2 beta2 xi (1+mu) + beta3 xi^2 (1+mu)^2`

and a kinematic factor.

On the dynamical FLRW branch,

`alpha = a xi`,

`n = xi c`,

`dot(alpha)/alpha = c H_g`,

so the nontrivial interaction branch gives

`s = -(a^2/c) [ dot(mu) + H_g mu(c+1+mu) ]`.

For `c=1` this reduces exactly to the cosmic-time form of Aoki-Maeda-Namba Eq. (4.31)/(64),

`s = -a^2 [dot(mu) + H mu(2+mu)]`.

Independent local Euler-Lagrange checks show that this choice cancels the `O(r^2)` residual, leaving `O(r^4)`, while an incorrect `s=0` leaves a finite `O(r^2)` coefficient.

## Homothetic radial oracle

After imposing the temporal constraint, the exact radial interaction equation on a homothetic FLRW background factorizes into the linear root `mu=0` times a quadratic.  Defining

`D = beta1 + 2 K beta2 + K^2 beta3`,

`B2 = (K beta2 + K^2 beta3)/D`,

`B3 = K^2 beta3/D`,

the quadratic is, up to an irrelevant nonzero common factor,

`[-2 B2 + (1+3w) B3] mu^2`

`+ [6w B2 - 2 B2 - 2] mu`

`+ 3(w-1) = 0`.

This is exactly the polynomial whose roots are Aoki Eq. (4.35)/(68).  Thus the pullback reproduces both the temporal and radial early Aoki equations analytically, not merely numerically.

## Exact non-homothetic early adiabatic equation

Let

`epsilon_H = dot(H_g)/H_g^2`.

After imposing the temporal constraint, all `dot(mu)`, `ddot(mu)` and `dot(c)` terms cancel from the leading radial equation.  The separate linear branch `mu=0` remains.  The two nonlinear adiabatic branches satisfy

`A2 mu^2 + A1 mu + A0 = 0`,

with

`A2 = xi [ beta2 + beta3 xi (c + epsilon_H + 1) ]`,

`A1 = beta1 + beta2 xi (c + 2 epsilon_H + 5)`
`     + beta3 xi^2 (3 c + 2 epsilon_H + 2)`,

`A0 = beta1(epsilon_H+3)`
`     + 2 beta2 xi(c+epsilon_H+2)`
`     + beta3 xi^2(2c+epsilon_H+1)`.

For `c=1` and `epsilon_H=-3(1+w)/2`, the coefficient ratios reduce exactly to the Aoki homothetic polynomial.  This is pinned by regression tests.

The cancellation of time derivatives is itself important: the interaction on weak metrics frozen to their backgrounds only determines the adiabatic branch.  It cannot generate the two dynamical helicity-0 matching data.  This agrees with Aoki's separation between adiabatic and oscillation modes.

## Candidate-C dust evaluation

On the strict Candidate-C dust background:

- `a=0.01` (`z=99`): nonlinear roots approximately `-0.93058`, `-0.36196`;
- `a=0.02` (`z=49`): roots approximately `-0.86536`, `-0.65408`;
- near the former late-linear start `a=0.05795144` (`z=16.26`): no real nonlinear roots;
- at `a=0.12`: no real nonlinear roots;
- at `a=0.20`: roots approximately `-0.30488`, `+0.40173`;
- at `a=1`: the admissible root is approximately `-0.24911` (the second root lies below `-1`).

The discriminant has two zero crossings:

1. `a = 0.03083065061191108`, `z = 31.43525453250283`, repeated `mu ~= -0.74187828`;
2. `a = 0.15868841564247294`, `z = 5.3016572189681`, repeated `mu ~= -0.19206857`.

At both crossings the temporal interaction branch factor is nonzero, so these are radial-branch mergers rather than loss of the temporal interaction branch.

## Crucial finite-mass caveat

At the first merger,

`m_eff/H ~= 0.544361`.

Representative values are approximately

- `a=0.01`: `m_eff/H ~= 0.288`;
- `a=0.02`: `0.404`;
- first merger: `0.544`;
- `a=0.05795144`: `1`;
- `a=0.10165`: `2.03`.

Therefore the first merger is earlier than `H=m_eff`, but it is not deep in the asymptotic `m_eff/H -> 0` regime.  Corrections from the weak metric perturbations, of relative order `m_eff^2/H^2`, are already order `0.30` at the merger and can quantitatively move or remove it.

**Scientific ruling:** the early non-homothetic adiabatic calculation is a strong warning but is not a no-go theorem for Candidate C.

## Literature cross-check

Aoki-Maeda-Namba explicitly state that their adiabatic equation contains no scalar-graviton dynamical degree of freedom and that the oscillation mode must be restored separately.  Their oscillation analysis keeps weak metric perturbations, eliminates them, and obtains a quadratic action for a Stückelberg scalar.  Their treatment is controlled only for `H >> m_eff` and `H << m_eff`; they state that the transition `H ~ m_eff` may require a full numerical analysis.

Lueben-Schmidt-May-Smirnov (arXiv:1912.09449) interpret the early linear instability as cosmological Vainshtein screening, but do not derive the nonlinear perturbation transition system; they leave such a nonlinear cosmological perturbation study as future work.

## Next hard block

Derive the finite-mass, weak-metric, non-homothetic Stückelberg system:

1. retain the four weak spherical metric potentials for g and f;
2. keep the Stückelberg map nonlinear in `mu`;
3. expand only in weak metric amplitudes / oscillation amplitudes;
4. eliminate the nondynamical metric potentials without assuming `m_eff/H -> 0`;
5. recover Aoki's full homothetic `C_m2 + C_H2` equation as the first oracle;
6. recover the already validated De Felice linear principal scalar as `mu -> 0` on Candidate C as the second oracle;
7. only then integrate through the merger/`H~m_eff` interval and extract `(Y3,Y3_N)` for the late exact-dust transfer system.

Do not tune `(Y3,Y3_N)` and do not force an algebraic branch switch.
