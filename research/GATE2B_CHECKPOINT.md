# Gate 2B — authoritative restart checkpoint

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption. Update after every hard finding or task-state change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The historical Comelli 12x12 closure is rejected for physics because it loses the helicity-0 `k^2 E` gradient. The active route is an independent quadratic-action reconstruction. A Lagos+two-matter hybrid was useful as an audit tool but is now proven unsuitable as the final two-matter action because Lagos 1610.00553 specializes the background/action reduction to matter coupled only to metric 1.

## Closed hard facts

### JANUS / bimetric bridge

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Independent De Felice high-k target on Candidate C at `a=0.5`: `c_s^2 ~= 0.69208`, `c_s ~= 0.83191`.
- Exact Case-C benchmark is in `numerics/comelli_case_c.py`; acceptance remains `E''+(3/tau)E'-(2/3)k^2 E=0`.

### Historical Comelli closure

- Radiation propagation is recovered exactly, but the supposed gravity pair is `c~0.0159` instead of `~0.8319`.
- Dust+dust gives the same failure; at large k the false frequency tends to a constant, proving the gravity gradient is structurally absent.
- Unit conversion, matter mixture, row choice, individual background derivatives, simple sign changes, conditioning, selected minors and merely eliminating `B1'` were ruled out.
- Raw gauge-invariant definitions require the A.3/A.18 relation with `calE'`; the printed unprimed form is kept only as a typo/control branch.

### De Felice matter block

- `numerics/de_felice_matter_action.py` implements the scalar P(X) quadratic matter block of De Felice Eq. (54).
- Metric-off action reproduces intrinsic sound speed.
- Correct Lagos -> De Felice scalar bridge is now:
  - `Phi_DF = Phi_L / 2`;
  - `B_DF = B_L / a_sector`;
  - `E_DF = 2 E_L`;
  - `psi_DF = -Psi_L - k^2 E_L/3`.
- The lapse factor 1/2 follows directly from Lagos `g00=-N^2(1+Phi_L)` versus De Felice `g00=-N^2(1+2 Phi_DF)`.
- TDD commits for this correction: RED `53c9af3`, GREEN `2ee436d`.

### Lagos spatial-derivative audit

Completed on the branch:

- L1/L2 tests pin self-sector Laplacians to the sector background metric.
- L3 corrected EH contractions (`252a4dd` -> `11c9b5a`).
- L4 audited and corrected interaction spatial gradients (`af6b315` -> `68e1c17`).
- Lagos Appendix A indeed states spatial indices are raised/lowered with the background metric of the field on which the derivative acts.

### Critical new finding: Lagos hybrid cannot be the final two-matter action

After the spatial corrections, the Case-C g-flat 4x4 kinetic Hessian became rank 4 when the old matter lapse bridge was used. Correcting `Phi_DF=Phi_L/2` restores near-rank-3 at very early times, but the residual eigenvalue is not numerical noise and grows as `~a^2`.

At exact Case C `a=0.2`, `k=20`, holding the geometry fixed and multiplying only the f-sector matter density by a factor `r_f`, the smallest eigenvalue is:

- `r_f=0`: `0`;
- `0.1`: `0.00149811`;
- `0.5`: `0.00749056`;
- `1.0`: `0.01498111`;
- `2.0`: `0.02996214`.

Thus the spurious kinetic direction is **linear in the second-sector density** and disappears when `rho_f=0`.

This is exactly consistent with the scope of Lagos 1610.00553: the paper assumes metric 1 is minimally coupled to matter; its final quadratic metric action uses those one-matter background relations and explicitly includes metric terms originating from that matter action. Therefore adding a second independent Eq. (54) matter sector to the already-specialized Lagos action is not a valid general two-matter construction.

**Ruling:** keep `lagos_scalar_action.py` as a convention/audit reference, but do not use the Lagos+two-matter hybrid to identify the BD mode or physical scalar speeds.

## Active task list

- [x] Convention bridge / Candidate-C / exact Case-C backgrounds.
- [x] Reject historical Comelli closure for Gate-2B physics.
- [x] Independent De Felice high-k gravity-speed target.
- [x] De Felice Eq. (54) one-sector P(X) matter action.
- [x] Correct Lagos/De Felice scalar-variable bridge, including `Phi_DF=Phi_L/2`.
- [x] Lagos self-sector Laplacian audit (L1-L3).
- [x] Lagos interaction-gradient audit (L4).
- [x] L5 diagnostic: show Lagos+second-matter hybrid violates rank-3 in proportion to `rho_f`.
- [ ] **T1c-DF — reconstruct/use the full De Felice two-matter quadratic scalar action.** ACTIVE.
  - [ ] DF1 — audit/transcribe the gravitational quadratic action used by De Felice before scalar reduction, in the same variables as Eq. (54), without importing Lagos one-matter background simplifications.
  - [ ] DF2 — combine both P(X) sectors and verify auxiliary lapse/shift equations are algebraic.
  - [ ] DF3 — impose g-flat gauge and reproduce the published count: four variables before BD elimination, kinetic rank 3 exactly/on-shell.
  - [ ] DF4 — identify and eliminate the BD/non-dynamical scalar combination at action level.
  - [ ] DF5 — obtain the final 3x3 kinetic/gradient matrices and recover the three high-k speeds (g-fluid, f-fluid, gravity).
  - [ ] DF6 — Case-C acceptance: recover B.5 or an exactly equivalent reduced equation.
- [ ] T2 — apply validated action reduction to Candidate C and recover De Felice `c_s~0.8319` over >=3 `(z,k)` points.
- [ ] T3 — identify precisely what the old Comelli 12x12 closure projected out.
- [ ] T4 — implement the native/action-based transfer solver.
- [ ] T5 — make `tests/test_comelli_native_scalar.py` green + >=3 regressions.
- [ ] T6 — full Gate-2B regression suite.
- [ ] T7 — time-domain fundamental transfer matrix.
- [ ] T8 — continuous GR-connected/adiabatic mode tracking.
- [ ] T9 — compute `T_gg,T_gf,T_fg,T_ff` and relative growth.
- [ ] T10 — Gate-2B scientific verdict with tolerances/domain.

## Test execution caveat

The container cannot clone the GitHub repository over the network. Git commits preserve RED/GREEN steps; focused algebraic controls are reproduced in scratch. Do not claim the entire repository pytest suite is green.

## Current intentional RED

`tests/test_comelli_native_scalar.py` remains RED until the action reduction is independently validated.

## Immediate restart instruction

**Resume at T1c-DF / DF1.**

1. Use De Felice 1404.0008 as the primary two-matter action framework, not the Lagos one-matter specialization.
2. Keep all metric and matter variables in De Felice conventions through auxiliary elimination; only map to JANUS variables after the reduced action is validated.
3. First recover the correct scalar degree count (rank 3 after gauge fixing, before/after explicit BD elimination as appropriate).
4. Then derive the high-k 3x3 kinetic/gradient matrices and compare to De Felice's published gravity speed.
5. Only after that return to Candidate C transfer integration.
6. Update this file after each hard finding.
