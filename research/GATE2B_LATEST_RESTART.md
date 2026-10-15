# Gate 2B — latest restart addendum

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`
Head at creation: see branch history after `497c7c9`.

This file supplements `research/GATE2B_CHECKPOINT.md` with the newest oscillation-mode work.

## Newest verified milestone

A homogeneous velocity-Hessian diagnostic has been calibrated on nonlinear homothetic Aoki dust roots.

Files:

- `numerics/nonhomothetic_oscillation_kinetic.py`;
- `tests/test_nonhomothetic_oscillation_kinetic.py`;
- `research/NONHOMOTHETIC_OSCILLATION_KINETIC_AUDIT.md`;
- `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`.

Targeted reconstructed-workspace result: `4 passed` for the kinetic-audit tests.  This is not a full-repository GREEN claim.

The usually omitted background term `dot(sigma_bg)` is essential.  Once restored, the single non-null homogeneous velocity eigenvalue agrees in sign with Aoki `K_S` on the tested nonlinear pressureless roots with positive interaction normalization.  A broader scratch scan gave `27/27` sign agreements.

The oracle is intentionally restricted to nonlinear roots; it is not the linear `mu=0` De Felice oracle and does not determine `c_S^2`.

## Candidate-C clue

On the leading non-homothetic early regular pair, the more-negative branch has the positive Aoki-calibrated homogeneous kinetic signature and the less-negative branch the opposite sign.

Following the positive-sign branch gives a robust signature zero at approximately

`a_K = 0.030136993`,
`z_K = 32.18181`,
`mu_K = -0.76624`.

A 16-point radius/finite-difference scan keeps this zero within about

`0.030136989 < a_K < 0.030137012`.

The independently derived finite weak-metric adiabatic fold is

`a_1 ~= 0.0301646`, `mu_1 ~= -0.768883`.

Their relative separation in `a` is only about `9.2e-4`.

This is a strong conditioning warning, but **not yet a kinetic no-go** because the oscillation-mode weak Einstein constraints at finite `m_eff/H` have not yet been eliminated.

Also, an algebraic fold does not generically force `K_S=0`: the homothetic dust control `B2=3`, `B3=2/3` has a double root `mu=-3/4` while `K_S=375/128>0`.  Therefore the Candidate-C near-coincidence is not a tautology.

## Failed shortcut to remember

Do not extract the spatial sound speed from the HR pullback before constraint reduction.

A raw local 2x2 Stückelberg principal symbol contains the constraint/gauge direction and gives spurious complex characteristics.  Direct finite-ball gradient Hessians are contaminated by lower-order boundary/constraint terms.  Compact profiles with derivatives scaling as `1/R` violate Aoki's epsilon counting.

Therefore the full spatial oracle must retain

`(phi_g, psi_g, phi_f, psi_f, delta_eta, delta_r)`

until the metric constraints and the nondynamical Stückelberg combination are eliminated.

## Immediate restart

Execute `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`.

First GREEN target: in the homothetic `H >> m_eff` limit, the six-field reduction must reproduce Aoki Eqs. (4.50)-(4.56), including both `K_S` and `c_S^2` for stable and unstable nonlinear roots.

Second GREEN target: the same non-homothetic system at `mu -> 0` must recover the already validated Candidate-C De Felice linear principal scalar.

Only after both pass should the finite-`m_eff/H` kinetic operator be evaluated through the fold interval or a transition trajectory be integrated.
