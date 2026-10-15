# Aoki compact weak-metric Schur audit

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **HOMOTHETIC AOKI KINETIC/GRADIENT ORACLE WITH WEAK METRICS ELIMINATED = GREEN AT COMPACT-ACTION AUDIT LEVEL; FINITE-MASS STATIC REGULAR ROOT ALSO RECOVERED**

## Purpose

The previous compact-support audit showed that the exact Hassan-Rosen interaction alone reproduces Aoki-Maeda-Namba's nonlinear oscillation coefficients `K_S` and `c_S^2` when boundary terms are removed correctly. The next question was whether the four weak metric potentials could be retained and eliminated at the action level without spoiling that oracle.

This audit builds that missing compact action layer.

## New exact spherical Einstein-Hilbert compact density

Added:

- `numerics/spherical_eh_compact_action.py`;
- `tests/test_spherical_eh_compact_action.py`;
- `tests/test_spherical_eh_compact_hessian.py`.

For

`ds^2 = a(eta)^2[-exp(2 phi)deta^2 + exp(2 psi)dr^2] + (a r)^2 dOmega^2`,

the implementation uses the exact warped-product Ricci scalar rather than a copied perturbative action.

Independent controls:

- unperturbed flat FLRW gives exactly `R = 6 a''/a^3`;
- Minkowski gives `R=0`;
- a constant spherical radial rescaling reproduces the exact warped-geometry curvature;
- on compact support in Minkowski the linear EH term vanishes and the `(phi,psi)` Hessian is symmetric and quadrature-stable.

The common angular factor `4 pi` and Planck prefactors are deliberately omitted from the helper and restored only in relative action normalization when needed.

## Compact five-field HR action

Added:

- `numerics/aoki_compact_metric_pi_action.py`;
- `tests/test_aoki_compact_metric_pi_action.py`.

The compact variables are

`(pi, phi_g, psi_g, phi_f, psi_f)`.

The Aoki map is used only for the homothetic acceptance oracle:

`pi -> (delta_eta, delta_r)`.

The two metrics are pulled into the same spherical chart and the exact principal `sqrt(g^-1 f)` is evaluated before forming the Hassan-Rosen potential. The metric potentials remain independent amplitudes.

The resulting five-by-five HR Hessian is symmetric and finite, vanishes when all interaction beta coefficients vanish, and its `pi-pi` entry is stable to quadrature changes. The action gradient is retained as well as the Hessian so the finite-mass static branch can be tested.

## Weak metric Schur reduction

Added:

- `numerics/aoki_compact_metric_schur.py`;
- `tests/test_aoki_compact_metric_schur.py`.

The audit convention is

`S_EH = (M^2/2) int sqrt(-g) R`,

`S_int = -m^2 M_g^2 int sqrt(-g) sum beta_n e_n`.

The total compact Hessian is assembled as

`H_total = -m^2 H_HR + (1/2) H_EH,g + (kappa/2) H_EH,f`

in the metric blocks, with `kappa=M_f^2/M_g^2`.

The four metric amplitudes are then eliminated by an ordinary Schur complement. The corresponding linear gradient is reduced with the same metric block.

Two exact structural controls pass:

1. at `m^2=0`, the Stückelberg `pi` row, column, gradient and reduced action vanish;
2. for `m^2/H^2 -> 0`, the reduced action tends to the previously validated HR-only compact action.

## Numerical-conditioning ruling

A first nested `H^2` extraction used an amplitude step `7e-4` and missed the published Aoki kinetic/gradient coefficients by about one percent after taking several nested finite differences.

This was diagnosed as numerical cancellation, not a physical coefficient error. Reusing the already validated compact-action amplitude step `2e-3` removes the bias.

No interaction, EH or Aoki coefficient was tuned.

## Homothetic Aoki kinetic/gradient acceptance

For the Candidate-like pressureless control

`(beta1,beta2,beta3) = (1,-4.2383993109,13.6801214252)`,
`K=1`,
with the regular nonlinear root near `mu=-0.6692344`,

the published compact HR target is approximately

`kinetic_HR = -0.6131123`,
`c_S^2 = 13.27614`.

After including both EH metric sectors and Schur-eliminating the four potentials, then taking the controlled small-`m^2/H^2` limit, the compact reduced action gives approximately

`kinetic_reduced / (-m^2) = -0.61418`,
`c_S^2 = 13.25294`,

an error of roughly `0.2%` at the chosen audit resolution.

This is the first executable action-level control in the repository in which the weak metric potentials are retained and eliminated while the published Aoki kinetic and gradient coefficients remain recovered.

## Finite-mass static control

The reduced compact linear gradient in `pi` is not identically zero away from an adiabatic branch. It can therefore be used as a compact static branch residual.

For the finite control

`H = 0.25`,
`m^2 = 1e-3`,
`kappa = 1`,

with effective Aoki source masses

`m_g^2 = m_f^2 = m^2 D`,

where

`D = beta1 + 2 beta2 + beta3`,

the full Aoki finite-mass polynomial gives the regular root

`mu ~= -0.67145`.

The compact action after weak-metric Schur elimination gives

`mu ~= -0.67294`.

The relative disagreement is about `0.22%`.

This is an independent finite-mass homothetic check beyond the asymptotic `H >> m_eff` `K_S,c_S^2` oracle.

## Targeted verification

Fresh reconstructed-workspace command on 2026-10-15 covered:

- exact spherical EH geometry;
- compact EH Hessian;
- five-field compact HR Hessian/gradient;
- compact metric Schur limits;
- Aoki `K_S,c_S^2` recovery;
- finite-mass static regular-root recovery.

Result:

`14 passed`.

This remains a targeted reconstructed-workspace result, not a complete repository GREEN claim.

## Scientific ruling

- `COMPACT_EH_SPHERICAL_ACTION = BUILT_AND_CONTROLLED`.
- `COMPACT_HR_PI_PLUS_FOUR_METRIC_POTENTIALS = BUILT`.
- `FOUR_WEAK_METRIC_POTENTIALS_ELIMINATED_AT_ACTION_LEVEL = YES` for the homothetic compact oracle.
- `AOKI_KS_AFTER_METRIC_SCHUR = RECOVERED` at audit resolution.
- `AOKI_CS2_AFTER_METRIC_SCHUR = RECOVERED` at audit resolution.
- `FINITE_MASS_AOKI_REGULAR_STATIC_ROOT = RECOVERED` at about `2e-3` relative accuracy.
- `STEP_A_HOMOTHETIC_ACTION_ORACLE = GREEN` at compact-audit level.
- `STEP_B_FINITE_MASS_HOMOTHETIC_CONTROL = GREEN` for the regular branch control.
- `NONHOMOTHETIC_DYNAMIC_OPERATOR = NOT YET DERIVED`.
- `CANDIDATE_C_FOLD_KINETIC_VERDICT = STILL OPEN`.

## Immediate next calculation

Promote the **pre-reduction compact action**, not the final Aoki formulas, to the actual non-homothetic on-shell background:

`xi(N), c(N), H(N), xi_N, c_N`.

The first mandatory non-homothetic oracle is the linear limit `mu -> 0`: the reduced high-k scalar coefficient must agree with the independently validated De Felice/Hassan-Rosen Candidate-C principal scalar.

Only after that oracle is GREEN should the fully reduced compact kinetic/gradient coefficients be followed toward the first Candidate-C fold near `a ~= 0.0301646`.
