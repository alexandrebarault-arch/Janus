# Gate 2B — authoritative restart checkpoint

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption. Update after every hard finding or task-state change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED**, but the action reconstruction has crossed an important validation threshold: the full two-matter De Felice/Hassan-Rosen action now reproduces the published Boulware–Deser constraint and scalar degree count on exact Case C without using the Lagos one-matter specialization.

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

- `numerics/de_felice_two_matter_action.py` assembles:
  1. both De Felice Eq. (44) EH sectors;
  2. the De Felice-sign HR interaction with analytic relative-shift block;
  3. both Eq. (54) matter sectors.
- It works in g-flat gauge (`psi_g=E_g=0`) and eliminates `Phi_g,Phi_f,B_g,B_f` by Schur complement.
- RED degree-count test `ea2ecb6`, initial module `2072ff6`, physical HR assembly `d79f1d2`.
- Exact Case-C scratch verification after the HR sign/shift corrections gives one kinetic eigenvalue null to relative precision roughly `1e-11`–`1e-14` at `a=0.1,0.2,0.4`, leaving exactly three scalar kinetic directions.
- The null rate direction in `(Sigma_dot,S_dot,qg_dot,qf_dot)` is
  `(1,0,0,1/(n H_f))` within numerical precision, exactly matching the De Felice Eq. (72) transformation at fixed `Y1,Y2,Y3` in g-flat gauge.
- This is the first reconstruction in the branch that simultaneously reproduces the ghost-free degree count and the published physical-variable basis without tuning.

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
  - [ ] **DF4 — transform to `(Y1,Y2,Y3,Z_BD)` using Eq. (72), verify `Z_BD_dot` disappears, and algebraically eliminate `Z_BD`.** NEXT.
  - [ ] **DF5** — obtain physical 3x3 kinetic/gradient matrices and recover the three high-k speeds (g fluid, f fluid, gravity).
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

**Resume at T1c-DF / DF4.**

1. In g-flat gauge define normalized physical variables using De Felice Eq. (72):
   - `Y1 ~ q_g`;
   - `Y3 = S`;
   - `Y2/phi_f_dot = q_f - (Sigma + k^2 S/6)/(n H_f)` for `Delta=-k^2`.
2. Introduce one fourth variable `Z_BD=Sigma`.
3. Transform the full post-auxiliary 8x8 quadratic Hessian, not only the 4x4 kinetic block.
4. Verify the row/column of `Z_BD_dot` vanishes to numerical tolerance on exact Case C.
5. Eliminate the algebraic `Z_BD` position by Schur complement, leaving a 6x6 quadratic form for `(Y1,Y2,Y3,Y1dot,Y2dot,Y3dot)`.
6. Only then extract 3x3 kinetic/gradient principal matrices and compare their speeds to De Felice.
7. Update this checkpoint after each hard finding.
