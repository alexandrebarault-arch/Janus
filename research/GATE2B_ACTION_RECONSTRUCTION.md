# Gate 2B — independent scalar-action reconstruction

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **ACTIVE RESTART POINT FOR T1c.6o**

Purpose: reconstruct the healthy-branch scalar dynamics independently of the Comelli Appendix-A transcription. This file is the detailed restart checklist for T1c.6o. The parent checkpoint remains `research/GATE2B_CHECKPOINT.md`.

## Binding acceptance criteria

1. Do not use the old 12x12 Comelli closure as an input.
2. Reproduce the De Felice gravitational high-k `c_s^2` from action-derived variables on the JANUS background map.
3. Recover the two matter sound speeds independently.
4. On exact Case C, recover an equation equivalent to `E''+(3/tau)E'-(2/3)k^2E=0` or an explicit invertible variable map to it.
5. Only then compare back to Comelli.
6. No coefficient/sign tuning to hit a target.

## Hard source facts

- De Felice 1404.0008 reduces to three physical scalar gauge invariants `Y1,Y2,Y3`, with one gravitational scalar speed plus two matter sound speeds in Eq. (86).
- Lagos-Ferreira 1610.00553 supplies the independent raw bimetric quadratic action; in massive bigravity `Phi_A,B_A` are auxiliary and only one gravitational scalar survives after all constraints/gauge reduction.
- Exact JANUS -> Lagos map: `r=xi`, `Nbar=c xi`, `H_LF=calH/a`, `Hb_LF=H_omega/a`, `M1^2=1`, `M2^2=kappa`, `nu^2=1/kappa`, `Z=m^2 f2/xi`, `Ztilde=m^2 f1/xi`.
- Healthy branch: `db/da=xi+y_N=c xi=Nbar`.
- Spatial derivative convention is fixed: `partial_1^2=-k^2/a^2`, `partial_2^2=-k^2/b^2` for comoving `k`.
- Correct relative-shift interaction: `a M1^2 Z k^2/[2(Nbar+r)] [r B1-(Nbar/r)B2]^2`.
- Raw EH velocity Hessian has zero lapse/shift rows, and the sector-1/sector-2 velocity blocks from Lagos Eqs. (3.6)-(3.7) are implemented and tested.
- `hr_diagonal_scalar_potential_density` evaluates the exact Hassan-Rosen interaction directly from `sqrt(-g) sum beta_n e_n(sqrt(g^{-1}f))`; it contains no precomputed `J/Gamma/Z/Ztilde`.
- Exact HR spatial mixed Hessian identities:
  - `L_Psi1Psi2=6 a^3 M1^2 r Ztilde`;
  - `L_Psi1E2=L_E1Psi2=2 a^3 M1^2 r Ztilde k^2`;
  - `L_E1E2=0`.
- Exact HR lapse-spatial mixed Hessian identities:
  - `L_Phi1Phi2=0`;
  - `L_Phi1Psi2=-(3/2) a^3 M1^2 r Z`;
  - `L_Phi2Psi1=-(3/2) a^3 M1^2 Nbar Z`;
  - `L_Phi1E2=-(1/2) a^3 M1^2 r Z k^2`;
  - `L_Phi2E1=-(1/2) a^3 M1^2 Nbar Z k^2`.
  These identities were derived from the exact potential and verified numerically; they are not imported from the old Comelli reduction.

## RED/GREEN ledger

- A1 RED `ce5aee2`; bridge implementation `dca0d52`. Full-repo bridge test still pending when complete checkout is locally available.
- A2 base RED `917aec5`; first implementation `f0de003`.
- Wrong initial spatial-derivative test specification was diagnosed and replaced by corrected RED `f56c58f`; correct implementation `3984612`.
- Sector-1 EH velocity: RED `ee97d21` -> GREEN `fefab2d`.
- Sector-2 EH velocity: RED `e3a70e5` -> GREEN `bc16893`.
- First exact HR spatial-cross RED `b461763` -> GREEN evaluator `10781fc`; combined local suite **5/5 passed**.
- HR lapse-spatial RED `dec47a8` reproduced as `unexpected keyword argument Phi1`.
- HR lapse extension GREEN `357701e`; combined local suite **6/6 passed** without tolerance changes. Example finite-difference values: `Phi1Phi2=-6.94e-8`, `Phi1Psi2=-0.06775025`, `Phi2Psi1=-0.06047149`, `Phi1E2=-0.15266378`, `Phi2E1=-0.13626184`, all matching the analytic `Z` identities.

## Active task list

- [x] **A0 — independent source route established.**
- [ ] **A1 — JANUS ↔ Lagos map.** CORE COMPLETE / FULL-REPO TEST PENDING.
  - [x] background dictionary;
  - [x] `Z,Ztilde` dictionary;
  - [x] `numerics/lagos_bridge.py`;
  - [ ] run full `tests/test_lagos_bridge.py` in complete checkout.
- [ ] **A2 — raw gravity quadratic action.** IN PROGRESS.
  - [x] perturbation/cosmic-time conventions;
  - [x] spatial/Fourier normalization;
  - [x] raw field order;
  - [x] auxiliary fields absent from raw velocity Hessian;
  - [x] relative-shift interaction square;
  - [x] sector-1 EH velocity block;
  - [x] sector-2 EH velocity block;
  - [ ] **A2.4c — remaining non-velocity EH scalar terms. NEXT CRITICAL PATH.**
    - [ ] sector-1 spatial/background-curvature coefficient families;
    - [ ] sector-2 lapse-rescaled mirror families;
    - [ ] cross-check GR single-metric constraint structure before combining with dRGT.
  - [ ] **A2.5 — dRGT scalar interaction.** SUBSTANTIALLY ADVANCED.
    - [x] exact HR diagonal-spatial evaluator;
    - [x] spatial mixed Hessian / `Ztilde` regression;
    - [x] lapse extension + lapse-spatial `Z` regression;
    - [x] independent relative-shift quadratic block;
    - [ ] assemble/export full raw dRGT quadratic Hessian from the validated pieces;
    - [ ] optional direct non-diagonal exact-potential shift check if needed for A3.
  - [ ] module must remain independent of old Comelli reduction modules.
- [ ] **A3 — eliminate auxiliaries from the action.**
  - [ ] eliminate `Phi1,Phi2,B1,B2`;
  - [ ] verify expected kinetic-rank drop / remaining auxiliary scalar;
  - [ ] eliminate it and gauge-reduce.
- [ ] **A4 — high-k regression.** Recover De Felice Eq. (86) gravity speed + matter speeds at >=3 Candidate-C points.
- [ ] **A5 — exact Case-C regression.** Recover B.5 or explicitly equivalent equation.
- [ ] **A6 — compare validated action reduction back to Comelli** and locate missing `k^2E` structure.
- [ ] **A7 — replace native scalar solver** only after A1-A6 pass.

## Immediate restart instruction

**Resume at A2.4c — non-velocity Einstein-Hilbert scalar terms.**

1. Re-open Lagos-Ferreira Eqs. (3.6)-(3.7) from the primary PDF/source and extract only source-unambiguous coefficient families.
2. Start with the sector-1 GR family controlling `Phi1-Psi1` spatial gradients and background-curvature/lapse terms, because A3 cannot eliminate lapses without them.
3. Write RED tests coefficient-family by coefficient-family; reproduce RED before production changes.
4. Mirror to sector 2 only after sector 1 passes, preserving all `Nbar,b,Hb` factors explicitly.
5. Keep all current 6/6 A2 regressions green.
6. Do not compare against Comelli until independent A3-A5 validation.
7. Update this file after every hard source fact, RED/GREEN transition, rejected coefficient reading, or restart-point change.
