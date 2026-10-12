# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **authoritative restart point after any interruption**. Read this file first and update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The Candidate-C background bridge is under control. The old direct Comelli closure and a later correctly index-reduced Comelli reconstruction both fail to recover the physical helicity-0 gradient, despite reproducing the visible radiation mode. They must not be used for transfer/segregation conclusions.

The active route is an **independent scalar quadratic-action reconstruction** from De Felice 1404.0008 and Lagos-Ferreira 1610.00553, followed only afterwards by comparison back to Comelli.

## Closed facts

### JANUS / De Felice / Lagos conventions

- JANUS -> Comelli/De Felice: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi*J`, `f1=Gamma`.
- Lagos massive-bigravity: `r=xi`, `Nbar=xi*c`, `Z=m^2 f2/xi=m^2 J`, `Z_tilde=m^2 f1/xi=m^2 Gamma/xi`.
- Thus `r*Z=m^2 f2`, `r*Z_tilde=m^2 f1`.
- Massive bigravity has `alpha_L=0`; there is no direct interaction `(partial^2 E)^2` term. The helicity-0 gradient emerges only after auxiliary elimination combined with Einstein-Hilbert structure.

### De Felice principal action

- `numerics/de_felice_action_principal.py` independently implements the high-k scalar principal coefficients from De Felice Eqs. (80),(82),(86), without calling the historical diagnostics implementation.
- Candidate-C cross-checks agree at `a=1,0.5,0.2`.
- At `a=0.5`: `c_s^2 ~= 0.69207999`, `c_s ~= 0.83191345`.
- Flat high-k scalar kinetic coefficient: `NG3 -> (3/8) m^2 a^4 xi J B`.

### Lagos scalar action reconstruction

- Interaction RED test: `tests/test_lagos_scalar_interaction.py`, commit `b51940f`.
- Interaction implementation: `894b692`.
- PDF parsing correction: Lagos Eq. (3.7) contains `nu^2*Nbar*r^2`, not `nu^2*Nbar*r/2`; correction commit `2de9354`.
- Raw Eq. (3.6)-(3.8) interaction and healthy-branch simplification agree in scratch at ~`5e-16` relative on Candidate C.
- Pure `E1/E2` has no direct interaction `E^2` term when `alpha_L=0`.
- Einstein-Hilbert RED tests: `tests/test_lagos_pure_metric_action.py`, commit `0996450`.
- EH self-action implementation (constant Planck masses): `f1b5cc3`.
- Primary PDF confirms the `E_dot` gradient-mixing factors are `a^2 k^2` for metric 1 and `b^2 k^2/Nbar^2` for metric 2; they are not divided by `a^2`/`b^2`.
- The pure metric action is exactly symmetric under `1<->2` on a proportional background in scratch.
- Auxiliary-elimination RED test: `tests/test_lagos_auxiliary_elimination.py`, commit `a9d1d8b`.
- Algebraic elimination of `Phi1,Phi2,B1,B2`: implementation commit `7fcdd15`.
- On a proportional equal-Planck background the auxiliary Hessian has rank 4 and the stationarity residual is at machine precision.
- After eliminating these four auxiliaries, the reduced velocity Hessian on `(Psi1,Psi2,E1,E2)` has **rank 1**. This persists in scratch scans over `H={0.2,0.8,1.5}` and `k={1,3,10}`.
- The nonzero kinetic direction is the relative metric scalar (the `E1-E2` sector); this is consistent with one ghost-free massive scalar metric DoF. Do not extrapolate this pure-metric proportional control directly to Candidate C before the matter/background terms are included.

### A.3 / A.18 issue

- Printed Comelli A.3/A.18 has `(calB1-calE)`; raw invariants give `(calB1-calE')` exactly.
- Bianchi finite-tau tests select the derived-prime form. Printed-unprime remains only a typo/control branch.

### Direct Comelli route — closed negative result

- Candidate C radiation speed is exactly `1/sqrt(3)`, but the supposed gravity pair is `c~0.0159` instead of `~0.8319`.
- Dust+dust fails identically.
- At large k the bad frequency approaches a constant: the physical gravity `k^2 E` term is structurally absent.
- Correctly treating `B1` as nondynamical and index-reducing the system still fails Case-C B.5.
- Ruled out: matter mixture, g00/f00 closure row, isolated derivative errors, A1/A2 typo, A.18 swap in old closure, f-trace sign flips, conditioning, selected minors, frozen-time PGCD, and eliminating `B1'` alone.

## Exact Case-C benchmark

`8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`.

- Exact branch: `a^4 xi^2 + xi - a - a^4/3 = 0`.
- `numerics/comelli_case_c.py` supplies exact branch, conformal map and derivatives.
- Acceptance B.5: `E''+(3/tau)E'-(2/3)k^2E=0`.
- With `E=tau^2e(x)`: `x^2 e_xx+7x e_x+8e-(2/3)x^2e=0`.
- High-x factor: `3q^2-2`.

## Action-route commits

- Lagos bridge test `85ede8f`; implementation `89c1482`.
- De Felice principal-action test `c761e4c`; implementation `e510107`.
- Lagos interaction test `b51940f`; implementation `894b692`; corrected Eq. (3.7) `2de9354`.
- EH/pure-metric test `0996450`; implementation `f1b5cc3`.
- Auxiliary-elimination test `a9d1d8b`; implementation `7fcdd15`.

Container network cannot clone/download GitHub, so the newly added pytest files have not been run as a repository suite. Core formulas and the key rank/symmetry checks were independently evaluated in scratch. Do not label the suite green until executable checkout becomes available.

## Active task list

- [x] Convention bridge / exact Candidate-C and Case-C backgrounds.
- [x] Audit and reject faulty direct Comelli scalar closure for Gate-2B physics.
- [x] Independent De Felice principal-action regression.
- [ ] **T1c — independently reconstruct and validate the scalar action.** IN PROGRESS.
  - [x] **T1c.6o.1 — Lagos action convention bridge.**
  - [x] **T1c.6o.2 — independent De Felice principal action.**
  - [x] **T1c.6o.3a — Lagos interaction potential in Fourier space.**
  - [x] **T1c.6o.3b — Einstein-Hilbert scalar self-actions, constant Planck masses.**
  - [x] **T1c.6o.3c — pure-metric quadratic action / exchange-symmetry control.** Scratch verified; repository pytest still pending.
  - [ ] **T1c.6o.4 — auxiliary/gauge reduction of pure metric action.**
    - [x] **6o.4a — integrate out `Phi1,Phi2,B1,B2` algebraically.**
    - [x] **6o.4b — proportional-background kinetic count:** reduced velocity Hessian rank 1 across several H,k controls.
    - [ ] **6o.4c — identify the reduced relative/gauge variables explicitly and derive the one-field pure-metric reduced action.** Verify the nonzero kinetic eigenvector is the relative `E` direction and separate the two gauge directions without choosing dynamics by hand.
  - [ ] **T1c.6o.5 — add separately coupled g/f barotropic matter actions and derive the high-k principal matrix; recover De Felice Eq. (86) rather than inserting it.**
  - [ ] **T1c.6p — compare action-derived constraints/reduced gradient to Comelli term-by-term and locate the lost structure.**
  - [ ] **T1c.6q — Case-C acceptance:** recover B.5 exactly or an explicitly equivalent action-variable equation.
  - [ ] verify Bianchi/gauge representative invariance.
- [ ] **T2 — Candidate-C full scalar validation from the new reduced action.**
- [ ] **T3 — replace faulty old scalar closure.**
- [ ] **T4 — implement native/action-based transfer scalar solver.**
- [ ] **T5 — make `tests/test_comelli_native_scalar.py` green + >=3 extra `(z,k)` regressions.**
- [ ] **T6 — full Gate-2B regression suite.**
- [ ] **T7 — time-domain transfer RHS + fundamental matrix.**
- [ ] **T8 — continuous GR-connected/adiabatic mode tracking.**
- [ ] **T9 — compute `T_gg,T_gf,T_fg,T_ff` and relative-mode growth.**
- [ ] **T10 — Gate-2B verdict with tolerances/domain.**

## Current RED regression

`tests/test_comelli_native_scalar.py` remains intentionally RED until T1c is closed.

## Immediate restart instruction

**Resume at T1c.6o.4c — explicit relative/gauge reduction.**

1. Work from `numerics/lagos_scalar_action.py`; do not return to the direct Comelli closure.
2. On the proportional equal-Planck control, diagonalize the reduced velocity Hessian after auxiliary elimination and pin its one nonzero eigenvector to the relative metric scalar sector.
3. Construct an explicit relative/common variable transform for `(Psi1,Psi2,E1,E2)` and show the common/gauge directions carry no physical kinetic eigenvalue.
4. Derive the one-field pure-metric reduced Lagrangian on this control background; use it only as a structural check, not as Candidate-C physics.
5. Then add the two separately coupled matter sectors (T1c.6o.5). Candidate-C rank/speed is not interpretable before this step.
6. Recover De Felice Eq. (86) from the reduced action, then apply the same machinery to exact Case C and require B.5.
7. Update this checkpoint after every hard finding or completed subtask.
