# Candidate C — local Aoki nonlinear-screening proxy audit

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **NONLINEAR EARLY SCREENING NOT EXCLUDED BY COUPLINGS; MATCHING NOT DERIVED**

## Question

The exact-dust late transfer audit exposed two independent blockers:

1. the finite-speed principal scalar is gradient-unstable until approximately `a ~= 0.10165` (`z ~= 8.84`) on `k=0.05...0.2 h/Mpc`;
2. after that healthy boundary, the four common/relative adiabatic conditions leave two helicity-0 phase-space data unfixed.

The only scientifically legitimate way to fix those data is to evolve or derive the preceding nonlinear/screened phase.  The repository already contains the seventh-order Aoki-Maeda-Namba adiabatic scalar polynomial, so the first question is whether Candidate C lies in the interaction-coupling class for which their cosmological Vainshtein mechanism can exist.

## Published Aoki result used

Aoki, Maeda & Namba (2015) consider a **homothetic** background

`f_{mu nu} = K^2 g_{mu nu}`

with constant `K`.  Their normalized nonlinear couplings are

`beta2_A = (b2 K^2 + b3 K^3)/(b1 K + 2 b2 K^2 + b3 K^3)`,

`beta3_A = b3 K^3/(b1 K + 2 b2 K^2 + b3 K^3)`.

For `H >> m_eff` their nonlinear adiabatic roots are `mu_+` and `mu_-` from Eq. (4.35).  Their scalar stability coefficients are Eqs. (4.55)-(4.56), with stability requiring

`K_S > 0`, `c_S^2 > 0`.

They reduce the sufficient interaction-coupling condition to

`b2 < 0`,

`b2^2 - b1 b3 > 0`

(assuming positive effective graviton mass), except for the exactly radiation-degenerate limit requiring separate care.

## Candidate-C raw coupling check

For the working Candidate C,

- `b1 = 1`;
- `b2 = -4.2383993109`;
- `b3 = 13.6801214252`.

Hence

`b2^2 - b1*b3 ~= 4.28 > 0`,

and `b2 < 0`.

Therefore Candidate C is **not excluded** by the simple Aoki early nonlinear-stability coupling criterion.

This agrees with the earlier reason for retaining this coefficient set as a nonlinear-screening stress test.

## Local instantaneous-K proxy

Candidate C is not homothetic.  As a deliberately limited diagnostic only, set

`K -> xi(a)`

instantaneously in the Aoki normalized coupling formulas and evaluate the early `w=0` roots and stability coefficients.

Representative results for the unique admissible (`mu > -1`) stable root are:

| a | xi | ctilde | mu | K_S | c_S^2 |
|---:|---:|---:|---:|---:|---:|
| 0.02 | 2.7181 | 0.2076 | -0.8841 | 0.00331 | 168.2 |
| 0.05795 | 1.2310 | 0.3359 | -0.7360 | 0.0260 | 24.08 |
| 0.08 | 1.0055 | 0.4120 | -0.6712 | 0.0485 | 13.50 |
| 0.10 | 0.8878 | 0.4733 | -0.6222 | 0.0738 | 9.16 |
| 0.12 | 0.8105 | 0.5280 | -0.5804 | 0.1027 | 6.75 |

The second early algebraic root is below `mu=-1` over this interval and is rejected by the Aoki coordinate-orientation ansatz.

The admissible local-proxy root varies smoothly and remains positive in both stability coefficients.

## Why this is not a Candidate-C nonlinear solution

The mismatch with the Aoki derivation is large, not perturbative:

- Aoki assumes constant `K` and homothetic lapse relation;
- Candidate C has evolving `xi(a)`;
- at `a=0.02`, `ctilde ~= 0.208` rather than 1;
- at the old late-linear start `a ~= 0.05795`, `ctilde ~= 0.336` rather than 1.

Therefore replacing `K` by `xi(a)` does **not** derive a nonlinear Candidate-C trajectory.  It is only a coupling-space/local algebraic proxy.

The early asymptotic formulas themselves also assume `H >> m_eff`; the old linear start is defined by `H ~ m_eff`, precisely where those formulas cease to be controlled.

## More fundamental matching limitation

In the Aoki adiabatic approximation, `mu` is determined algebraically.  The paper explicitly notes that this adiabatic solution contains no dynamical scalar-graviton oscillation degree of freedom; that oscillation mode is analyzed separately.

This matters directly for JANUS-R: the late exact-dust transfer requires **two phase-space matching data** for the helicity-0 sector.  An algebraic value of `mu(a)` cannot by itself provide both members of that canonical pair.

Aoki et al. further state that for realistic `w < 1/3`, a transition from the early GR phase to the linear late bigravity phase can occur faster than a Hubble time, invalidating their adiabatic assumption around `H ~ m_eff`; they call for a numerical treatment beyond that approximation.

That is exactly the transition region in which our missing two matching data must be determined.

## Scientific ruling

The Aoki proxy **rescues possibility, not predictivity**:

- `NONLINEAR_SCREENING_EXCLUDED_BY_COUPLINGS = NO`;
- `PUBLISHED_AOKI_ADIABATIC_ROOT_FIXES_JANUS_R_MATCHING = NO`;
- `FULL_NONHOMOTHETIC_DYNAMICAL_TRANSITION_REQUIRED = YES`.

Thus the strict Candidate-C dust branch cannot yet be rejected solely because its naive linearization is unstable before `z~8.84`: the interaction coefficients lie in a class known to admit nonlinear early screening on homothetic backgrounds.

But the same result cannot be used to choose `Y3` and `Y3_N` by hand.  Until a nonhomothetic dynamical screened-to-linear transition is derived and evolved, the late transfer functions remain non-unique.

## Implemented diagnostic

- `numerics/candidate_c_aoki_proxy.py`
- `tests/test_candidate_c_aoki_proxy.py`

The module labels every result as `homothetic_proxy_only` to prevent accidental promotion to an exact Candidate-C calculation.

## Next step

The next genuinely new calculation would have to go beyond the published algebraic Aoki polynomial: derive a dynamical helicity-0 transition system on the nonhomothetic Candidate-C background (including the time-dependent `xi`/lapse structure), then evolve it through `H ~ m_eff` and read the two late phase-space matching data on the principal-stable surface.

That is a new nonlinear derivation, not a small extension of the current linear transfer code.
