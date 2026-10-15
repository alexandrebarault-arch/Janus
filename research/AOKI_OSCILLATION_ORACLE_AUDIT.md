# Aoki oscillation-mode acceptance oracle

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **PUBLISHED HOMOTHETIC OSCILLATION ORACLE PINNED; PRINCIPAL-SYMBOL SHORTCUT RULED OUT**

## Purpose

The next hard block is the spatially dependent nonlinear helicity-0 action. Before building that reducer, the published Aoki-Maeda-Namba early-time result is now pinned as an independent executable acceptance oracle.

This file does not claim that the six-field reduction is already complete. It fixes what that reduction must reproduce and records which shortcuts have been explicitly ruled out.

## Published control relations

For the oscillation mode on a homothetic nonlinear branch, Aoki Eqs. (4.50)-(4.51) express the two spherical Stückelberg coordinate perturbations in terms of one scalar `pi`:

`delta_eta = a^-2[-pi_eta + (a r H mu/(1+mu)) pi_r] + O(epsilon^2)`,

`delta_r = a^-2[pi_r/(1+mu) + (a r H mu/(1+mu)) pi_eta] + O(epsilon^2)`.

The reduced action is

`S2 proportional to integral (a r H)^2 K_S [(pi_eta)^2 - c_S^2 (pi_r)^2]`.

For the linear branch `mu=0`,

`K_S = 3(1+3w)/4`,

`c_S^2 = (w-1)/(1+3w)`.

For a nonlinear branch,

`K_S = 3(3w-1)(2+mu)(1+2 beta2 mu+beta3 mu^2)/4`,

`c_S^2 = 2[3(1-w)+(1-(3w-1)beta2)mu] / {3(3w-1)(2+mu)(1+2 beta2 mu+beta3 mu^2)}`.

Here `beta2,beta3` are Aoki's normalized nonlinear couplings, not the raw Hassan-Rosen beta_n coefficients.

## Useful invariant

Multiplying the two nonlinear coefficients cancels the entire common kinetic factor:

`K_S c_S^2 = 1/2 [3(1-w) + (1-(3w-1) beta2) mu]`.

This gives a strong two-part acceptance test for the future reducer:

1. its kinetic normalization/sign must match `K_S` up to one global positive convention;
2. its gradient coefficient must independently match `K_S c_S^2`.

A reducer can therefore no longer pass merely by producing the correct ratio accidentally.

## Power counting

The Aoki derivation works on a sub-horizon scale `L` with

`epsilon = a L H << 1`.

Adiabatic variables change on the Hubble time, whereas oscillation variables obey

`|partial_eta chi_osc| ~ |partial_r chi_osc| >> |a H chi_osc|`.

The physical one-field action itself carries the explicit factor

`(a r H)^2 = O(epsilon^2)`.

Therefore the scalar kinetic/gradient operator is not encoded solely in the highest-derivative principal symbol of the raw `(delta_eta,delta_r)` system. The curvature/subprincipal terms at `O(epsilon^2)` are part of the leading physical answer.

This explains why previous finite-ball / shrinking-radius gradient probes were unreliable: changing the radial domain without preserving the epsilon counting changes the relative derivative orders and can inject the adiabatic branch displacement into the putative gradient coefficient.

## Principal-symbol shortcut explicitly ruled out

A common-coordinate HR square-root helper was added so that both `g` and `f` can be pulled back before forming `sqrt(g^-1 f)`. It passes the strong covariance control that a common arbitrary radial/time pullback of a homothetic pair `f=K^2 g` leaves the four square-root eigenvalues equal to `K`.

Using that corrected geometry, two additional scratch controls were performed:

1. a WKB shell average, designed to suppress finite-ball boundary terms;
2. an x64 auto-diff principal Hessian in the raw `(delta_eta,delta_r)` jets, projected afterward onto the published Aoki `pi` combination.

Neither produces a stable convergence to the published `c_S^2` when only the principal derivative operator is retained.

This is not treated as a failure of the HR interaction. It is the expected consequence of discarding the `O((arH)^2)` curvature/subprincipal terms that constitute the physical scalar action.

**Ruling:** do not attempt another raw principal-symbol or shrinking-ball extraction. The next derivation must perform the Aoki epsilon expansion through `O(epsilon^2)` before eliminating the nondynamical combination.

## Executable implementation

Added:

- `numerics/aoki_oscillation_oracle.py`;
- `tests/test_aoki_oscillation_oracle.py`;
- generalized `square_root_invariants_from_blocks(...)` in `numerics/nonhomothetic_hr_spherical.py`;
- `tests/test_general_spherical_square_root.py`.

Targeted reconstructed-workspace verification after the common-coordinate refactor:

`6 passed`.

The tests pin:

- the linear `mu=0` coefficients;
- the nonlinear `K_S c_S^2` identity;
- the `pi -> (delta_eta,delta_r)` map;
- the known counterexample showing that an algebraic double root need not imply `K_S=0`;
- equivalence with the previous diagonal-g square-root path;
- common-coordinate covariance of a homothetic metric pair.

## Next RED

Construct the **full homothetic quadratic action through `O(epsilon^2)`**, not just its principal symbol, using the common-coordinate pullbacks and the published Aoki power counting.

The first nontrivial RED must require the reduced coefficients to reproduce both `K_S` and `K_S c_S^2` on at least one nonlinear dust root.

Only after this homothetic oracle is GREEN should weak metric auxiliaries be retained at finite `m_eff/H` and the construction promoted to the non-homothetic Candidate-C background.
