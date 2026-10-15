# Gate 2B — latest restart checkpoint

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **Gate 2B OPEN; homothetic oscillation action with weak-metric Schur now controlled; non-homothetic promotion is the active hard block.**

Read this file first after interruption, then:

1. `research/AOKI_COMPACT_METRIC_SCHUR_AUDIT.md`;
2. `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`;
3. `research/GATE2B_CHECKPOINT.md`.

## 1. What is already closed

Do not redo the following unless new contradictory evidence appears:

- De Felice/Hassan-Rosen scalar action reconstruction;
- BD time-dependent canonicalization;
- Case-C `NG3` and all three Eq. (85) principal modes;
- Candidate-C dust+dust principal gravity branch;
- exact-dust late phase-space construction;
- proof that four adiabatic density conditions leave two helicity-0 matching data free;
- exact non-homothetic spherical Stückelberg temporal relation;
- finite weak-metric Candidate-C folds;
- calibrated homogeneous kinetic-sign warning near fold 1.

Gate 2B is still open because the nonlinear/non-homothetic oscillating helicity-0 transition has not yet been carried through the fold interval.

## 2. Candidate-C fold warning retained

The regular finite weak-metric adiabatic pair disappears at approximately

`a_1 ~= 0.0301646`, `z_1 ~= 32.151`, `mu_1 ~= -0.768883`,

and reappears near

`a_2 ~= 0.0491246`, `z_2 ~= 19.356`, `mu_2 ~= -0.67015`.

The independent homogeneous nonlinear kinetic-sign diagnostic crosses zero near

`a_K ~= 0.030136993`, `z_K ~= 32.18181`, `mu_K ~= -0.76624`.

The relative separation between `a_K` and the first fold is only about `9.2e-4`, but this is **not yet a no-go theorem** because the full constrained oscillation action at finite `m_eff/H` must decide whether the zero survives.

## 3. Compact Aoki action oracle — closed

Boundary-contaminated local principal-symbol shortcuts have been superseded by compact-support action audits.

The exact HR compact oracle already reproduced Aoki's nonlinear

- kinetic coefficient `K_S`;
- gradient coefficient / `c_S^2`;

including opposite-sign nonlinear controls.

The reason previous local probes failed is now understood: the physical scalar action starts at `O((a L H)^2)`, so naive pointwise principal-symbol extraction discards terms of the same order as the mode itself.

## 4. New compact weak-metric action layer — GREEN

New production/audit files:

- `numerics/spherical_eh_compact_action.py`;
- `numerics/aoki_compact_metric_pi_action.py`;
- `numerics/aoki_compact_metric_schur.py`;
- `tests/test_spherical_eh_compact_action.py`;
- `tests/test_spherical_eh_compact_hessian.py`;
- `tests/test_aoki_compact_metric_pi_action.py`;
- `tests/test_aoki_compact_metric_schur.py`.

The exact spherical Einstein-Hilbert compact density is independently controlled by FLRW, Minkowski and warped-sphere identities.

The homothetic compact variables are

`(pi, phi_g, psi_g, phi_f, psi_f)`.

The four weak metric amplitudes are retained in the action and eliminated by a Schur complement.

Structural controls:

- at `m^2=0`, the `pi` row/column/gradient vanish exactly;
- for `m^2/H^2 -> 0`, the reduced result tends to the already validated HR-only compact action;
- the metric block remains full rank in the tested controls.

## 5. Aoki kinetic/gradient after metric elimination — GREEN

For the Candidate-like pressureless homothetic control

`(beta1,beta2,beta3)=(1,-4.2383993109,13.6801214252)`,
`K=1`, `mu~-0.6692344`,

the published compact target is approximately

`kinetic_HR ~= -0.6131123`,
`c_S^2 ~= 13.27614`.

After retaining and Schur-eliminating the four weak metric potentials, the controlled small-`m^2/H^2` extraction gives approximately

`kinetic_reduced/(-m^2) ~= -0.61418`,
`c_S^2 ~= 13.25294`.

The disagreement is about `0.2%` at the chosen compact quadrature / finite-difference resolution.

A numerical-conditioning issue was identified and closed: the nested `H^2` extraction requires the same `~2e-3` amplitude step already validated by the original compact oracle; `7e-4` caused cancellation bias. No physical coefficient was changed.

## 6. Finite-mass homothetic static control — GREEN

The compact reduced linear gradient in `pi` provides a static branch residual after the four metric amplitudes are eliminated.

For

`H=0.25`, `m^2=1e-3`, `kappa=1`,

with

`m_g^2=m_f^2=m^2 D`,

Aoki's full finite-mass polynomial gives the regular root

`mu ~= -0.67145`.

The independent compact-action Schur residual gives

`mu ~= -0.67294`.

Relative disagreement is about `0.22%`.

Therefore the homothetic finite-mass action control is no longer the blocker.

## 7. Fresh targeted verification

Latest reconstructed-workspace command covering the new compact EH/HR/Schur chain:

`14 passed`.

This is **not** a full-repository GREEN claim. GitHub Actions remain disabled and the current environment still does not provide a complete clean clone/worktree.

## 8. Current active task

Proceed to **non-homothetic promotion before reduction**.

Promote the compact action coefficients to the actual strict Candidate-C dust background functions

`xi(N), c(N), H(N), xi_N, c_N`

(and higher local derivatives only where the action requires them).

Do **not** substitute `K -> xi` into the final homothetic Aoki formulas.

The time-dependent/non-homothetic quantities must enter the pulled-back metrics and the action **before** the four metric potentials are eliminated.

## 9. Next mandatory oracle

Before interpreting the folds, take

`mu -> 0`

on the real non-homothetic Candidate-C background.

The reduced high-k scalar must recover the independently validated De Felice/Hassan-Rosen Candidate-C principal gravity branch.

If this fails, the non-homothetic action promotion is wrong and no fold verdict may be drawn.

If it passes, evaluate the fully reduced kinetic and gradient coefficients along the early regular nonlinear branch toward

`a_1 ~= 0.0301646`.

The decisive question remains:

> Does the fully constrained helicity-0 kinetic/gradient operator remain regular and healthy through the first fold, or does Candidate C hit a genuine strong-coupling/ghost/constraint singularity?

Only a healthy continuous trajectory may determine the missing late matching data `(Y3,Y3_N)`.
