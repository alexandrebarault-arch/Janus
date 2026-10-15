# Aoki oscillation-mode acceptance oracle

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **PUBLISHED HOMOTHETIC OSCILLATION ORACLE PINNED IN EXECUTABLE FORM**

## Purpose

The next hard block is the spatially dependent nonlinear helicity-0 action. Before building that reducer, the published Aoki-Maeda-Namba early-time result is now pinned as an independent executable acceptance oracle.

This file does not claim that the six-field reduction is already complete. It fixes what that reduction must reproduce.

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

This explains why previous finite-ball / shrinking-radius gradient probes were unreliable: changing the radial domain without preserving the epsilon counting changes the relative derivative orders and can inject the adiabatic branch displacement into the putative gradient coefficient.

The six-field derivation must therefore expand by epsilon order before taking the local principal limit.

## Executable implementation

Added:

- `numerics/aoki_oscillation_oracle.py`;
- `tests/test_aoki_oscillation_oracle.py`.

Targeted reconstructed-workspace verification:

`4 passed`.

The tests pin:

- the linear `mu=0` coefficients;
- the nonlinear `K_S c_S^2` identity;
- the `pi -> (delta_eta,delta_r)` map;
- the known counterexample showing that an algebraic double root need not imply `K_S=0`.

## Next RED

Construct the homothetic oscillation action with the Aoki epsilon bookkeeping and the full common-coordinate pullbacks. The first nontrivial RED must require the reduced quadratic coefficients to reproduce both `K_S` and `K_S c_S^2` on at least one nonlinear dust root.

Only after this homothetic oracle is GREEN should weak metric auxiliaries be retained at finite `m_eff/H` and the construction promoted to the non-homothetic Candidate-C background.
