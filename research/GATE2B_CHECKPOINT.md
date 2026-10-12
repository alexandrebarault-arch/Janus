# Gate 2B — authoritative restart checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption. Update after every hard finding or task-state change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED**, but the action reconstruction has crossed an important validation threshold: the full two-matter De Felice/Hassan-Rosen action reproduces the Boulware–Deser constraint, the scalar degree count, and the Eq. (72) physical-variable basis on exact Case C. The current frontier is the physical high-k dispersion of the resulting 3-field action.

## Closed hard facts

### Background / conventions

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Independent De Felice high-k gravity target on Candidate C at `a=0.5`: `c_s^2 ~= 0.69208`, `c_s ~= 0.83191`.
- Exact Case-C background lives in `numerics/comelli_case_c.py`; acceptance remains `E''+(3/tau)E'-(2/3)k^2E=0`.

### Historical Comelli closure — rejected for physics

- It recovers visible radiation propagation but replaces the physical gravity pair by `c~0.0159`.
- Dust+dust gives the same failure; the false frequency tends to a constant at high k, proving the helicity-0 `k^2 E` term was projected out.
- Unit conversion, matter mixture, closure-row choice, simple coefficient/sign swaps, conditioning, selected minors and merely eliminating `B1'` were ruled out.

### Lagos route — retained only as audit reference

- Lagos 1610.00553 specializes its final quadratic action to matter coupled to metric 1 and uses those background equations.
- Adding an independent second Eq. (54) matter block to that specialized action produces a spurious fourth kinetic direction linear in `rho_f`.
- Therefore Lagos is useful for convention/cross-check work, but **must not be used as the final two-matter scalar action**.
- Spatial derivative audits L1-L4 are complete (`252a4dd`, `11c9b5a`, `af6b315`, `68e1c17`).
- Lagos -> De Felice lapse convention is `Phi_DF=Phi_L/2`; TDD RED/GREEN `53c9af3` / `2ee436d`.

## Validated De Felice two-matter action reconstruction

### Matter

- `numerics/de_felice_matter_action.py` implements De Felice Eq. (54) for one P(X) sector.
- Metric-off action reproduces the intrinsic matter sound speed.
- Both matter sectors are added independently, each with its own metric/lapse/scale factor.

### Einstein-Hilbert

- `numerics/de_felice_gravity_action.py` directly specializes De Felice Eq. (44) to flat scalar Fourier modes.
- TDD scaffold: RED `bb86701`, initial GREEN `85b008c`.
- A later direct contraction audit found three Fourier-sign mistakes: `B E_dot`, `Phi E`, `psi E`. RED `a7d41b3`, fix `256cefd`.
- The coefficient `12 H Phi psi_dot/N` is confirmed directly by `Tr Hdot = 6 psi_dot`; an earlier apparent factor-2 discrepancy with Lagos was an invalid cross-convention comparison and is superseded.

### Hassan-Rosen interaction

- `numerics/hr_scalar_potential.py` contains an exact local standard-beta matrix potential and a perturbative De Felice helper.
- Exact diagonal standard-beta potential matches the independent diagonal implementation at machine precision (`35fcfdb` -> `cfa9e5c`).
- A local real matrix treatment of scalar shifts is invalid for Fourier quadratic theory because `V_i=D_iB` carries k/-k phase information. Its shift Hessian disagreed with De Felice Eq. (46), including the cross-term sign.
- The physical perturbative helper therefore uses the explicit rank-one shift block
  `+(m^2 M_g^2/2) N a^3 xi J/(ctilde+1) k^2 (B_g-ctilde B_f)^2`.
  RED `04934f9`, fix `b5de9b6`.
- De Felice uses `+ alpha_i L_i(K)` with `K=I-S`; under their published alpha/beta correspondence this is **minus** the standard-beta `sum beta_n e_n(S)` potential. RED `3f345e7`, fix `9851c3d`.

### Full two-matter action and BD constraint

- `numerics/de_felice_two_matter_action.py` assembles both EH sectors, the De Felice-sign HR interaction, and both Eq. (54) matter sectors.
- It works in g-flat gauge (`psi_g=E_g=0`) and eliminates `Phi_g,Phi_f,B_g,B_f` by Schur complement.
- RED degree-count test `ea2ecb6`, initial module `2072ff6`, physical HR assembly `d79f1d2`.
- Exact Case-C verification after HR sign/shift corrections gives one null kinetic direction and exactly three scalar kinetic directions.
- The null rate direction in `(Sigma_dot,S_dot,qg_dot,qf_dot)` is `(1,0,0,1/(n H_f))`, matching De Felice Eq. (72).

### DF4 — physical basis and BD removal CLOSED

- Eq. (72) basis transform is implemented as `(Y1,Y2,Y3,Z_BD)` with `Z_BD=Sigma`.
- `Z_BD_dot` has no quadratic kinetic direction on exact Case C; remaining linear `Y*Zdot` terms are canonically integrated by parts at frozen coefficients.
- `Z_BD` is algebraically invertible and is eliminated by Schur complement, leaving a 6x6 quadratic Hessian for `(Y1,Y2,Y3,Y1dot,Y2dot,Y3dot)` and a positive 3x3 kinetic matrix on the Case-C control points.
- TDD/implementation trail: `9145fe1` (RED), `c7db4d1` (BD elimination), `e1c7ea5` (canonicalization RED), `2fc77e0` (canonicalization fix).

### DF5 — physical high-k dispersion ACTIVE

- A new RED regression `bb43d94` requires the physical 6x6 action on high-k Case C to recover three scalar branches in g-coordinate units:
  1. gravity `c_s^2 -> -2/3` (Comelli B.5);
  2. g-fluid `c_s^2 -> 1/3`;
  3. f-fluid `c_s^2 -> ctilde^2 c_{s,f}^2`.
- `physical_squared_phase_speeds()` was added in `3dc45ce`. It constructs the frozen Euler-Lagrange system
  `K Yddot + (C.T-C) Ydot - M Y = 0`
  from the physical Hessian and returns `c_s^2=-(a lambda/k)^2` from its +/- eigenvalue pairs.
- The extractor itself was independently checked in scratch on a decoupled synthetic action and recovered `(-2/3,1/3,0.4)` to ~`1e-16`. The same synthetic regression is now committed in `18d1fec`.
- The integrated physical Case-C speed regression has not yet been executed in the container because the repo is not mountable/cloneable there. Do **not** mark DF5 green until that physical action test is actually run or equivalently reproduced independently.

## Active task list

- [x] Convention bridge / Candidate-C / exact Case-C backgrounds.
- [x] Reject historical Comelli closure for Gate-2B physics.
- [x] Independent De Felice high-k gravity target.
- [x] De Felice Eq. (54) one-sector P(X) matter action.
- [x] Lagos audits and proof that the Lagos+two-matter hybrid is invalid.
- [ ] **T1c-DF — full De Felice two-matter scalar action.** ACTIVE.
  - [x] **DF1** — transcribe/audit both gravitational EH sectors in De Felice variables.
  - [x] **DF2** — combine two P(X) sectors + HR interaction; lapse/shift auxiliaries algebraic.
  - [x] **DF3** — g-flat gauge degree count: 4 variables before BD removal, kinetic rank exactly 3 on Case C.
  - [x] **DF4** — transform to `(Y1,Y2,Y3,Z_BD)`, remove `Z_BD_dot`, and algebraically eliminate `Z_BD`.
  - [ ] **DF5** — recover the three physical high-k speeds from the 3-field action. IN PROGRESS.
    - [x] DF5a — define frozen Euler-Lagrange mode extractor from 6x6 physical Hessian.
    - [x] DF5b — validate extractor on a synthetic exactly-solvable 3-mode action.
    - [ ] **DF5c — run/reproduce the integrated high-k Case-C action regression and confirm `(-2/3,1/3,ctilde^2 c_sf^2)`.** NEXT.
    - [ ] DF5d — once Case C is green, test the gravity branch on Candidate C against De Felice `scalar_cs2`.
  - [ ] **DF6** — Case-C acceptance: recover B.5 or exactly equivalent reduced action/equation.
- [ ] **T2** — Candidate-C validation: recover De Felice `c_s~0.8319` at >=3 `(z,k)` points.
- [ ] **T3** — identify exactly what the old Comelli 12x12 closure projected out.
- [ ] **T4** — native/action-based transfer solver.
- [ ] **T5** — make `tests/test_comelli_native_scalar.py` green + >=3 regressions.
- [ ] **T6** — full Gate-2B regression suite.
- [ ] **T7** — time-domain fundamental transfer matrix.
- [ ] **T8** — continuous GR-connected/adiabatic mode tracking.
- [ ] **T9** — compute `T_gg,T_gf,T_fg,T_ff` and relative growth.
- [ ] **T10** — Gate-2B scientific verdict.

## Test caveat

The container cannot clone the repo over the network. RED/GREEN commits are preserved in Git and focused algebra is independently reproduced in scratch. Do not claim the entire repository pytest suite is green.

## Current intentional RED

`tests/test_comelli_native_scalar.py` remains intentionally RED until the action reduction is independently validated through DF5/DF6.

## Immediate restart instruction

**Resume at T1c-DF / DF5c.**

1. Reproduce or execute the integrated Case-C test in `tests/test_de_felice_two_matter_action.py::test_case_c_high_k_physical_action_recovers_three_scalar_speed_branches`.
2. If it fails, inspect the measured three `c_s^2` values before changing any coefficient. Do not tune the test target.
3. The expected high-k branches are `-2/3`, `1/3`, and `ctilde^2 c_sf^2` in g-coordinate units.
4. If Case C passes, add Candidate-C high-k regression(s) using the independent De Felice `diagnostics()['scalar_cs2']` target.
5. Only after DF5 passes should DF6 reduce the gravity eigenvector/equation to B.5 explicitly.
6. Update this checkpoint immediately after every hard finding.
