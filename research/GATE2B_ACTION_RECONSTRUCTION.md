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

- De Felice 1404.0008 reduces to three physical scalar gauge invariants `Y1,Y2,Y3`; Eq. (86) gives one gravitational scalar speed plus two matter sound speeds.
- Lagos-Ferreira 1610.00553 supplies the independent raw bimetric quadratic action. In massive bigravity `Phi_A,B_A` are auxiliary and only one gravitational scalar survives after all constraints/gauge reduction.
- Exact JANUS -> Lagos map: `r=xi`, `Nbar=c xi`, `H_LF=calH/a`, `Hb_LF=H_omega/a`, `M1^2=1`, `M2^2=kappa`, `nu^2=1/kappa`, `Z=m^2 f2/xi`, `Ztilde=m^2 f1/xi`.
- Healthy branch: `db/da=xi+y_N=c xi=Nbar`.
- Spatial derivative convention: `partial_1^2=-k^2/a^2`, `partial_2^2=-k^2/b^2` for comoving `k`.
- Correct relative-shift interaction: `a M1^2 Z k^2/[2(Nbar+r)] [r B1-(Nbar/r)B2]^2`.
- Raw EH velocity Hessian has zero lapse/shift rows; sector-1/sector-2 velocity blocks from Lagos Eqs. (3.6)-(3.7) are implemented and tested.
- Source-unambiguous GR spatial constraint blocks from the same equations are now also implemented:
  - sector 1: `a^3 M1^2 (k^2/a^2)[Psi1^2-2 Phi1 Psi1+2 H Phi1 B1]`;
  - sector 2: `Nbar b^3 M2^2 (k^2/b^2)[Psi2^2-2 Phi2 Psi2+2(Hb/Nbar) Phi2 B2]`.
- The `Phi1^2` coefficient printed in Lagos Eq. (3.6) includes the quadratic metric self-interaction contributed by their specific matter scalar (`phidot_bar^2`). JANUS instead has two perfect-fluid sectors, including matter coupled to metric f. **Ruling:** do not copy Lagos' one-sided scalar-matter lapse-square coefficient into JANUS. The lapse-square/background-matter families must be derived or independently cross-checked with the two-matter De Felice formulation before A3.
- `hr_diagonal_scalar_potential_density` evaluates the exact Hassan-Rosen interaction directly and contains no precomputed `J/Gamma/Z/Ztilde`.
- Exact HR spatial mixed Hessian identities: `L_Psi1Psi2=6 a^3 M1^2 r Ztilde`, `L_Psi1E2=L_E1Psi2=2 a^3 M1^2 r Ztilde k^2`, `L_E1E2=0`.
- Exact HR lapse-spatial identities: `L_Phi1Phi2=0`, `L_Phi1Psi2=-(3/2)a^3M1^2 r Z`, `L_Phi2Psi1=-(3/2)a^3M1^2 Nbar Z`, `L_Phi1E2=-(1/2)a^3M1^2 r Z k^2`, `L_Phi2E1=-(1/2)a^3M1^2 Nbar Z k^2`.

## RED/GREEN ledger

- A1 RED `ce5aee2`; bridge implementation `dca0d52`. Full-repo bridge test still pending.
- A2 base RED `917aec5`; first implementation `f0de003`.
- Wrong initial spatial-derivative test specification was diagnosed; corrected RED `f56c58f` -> implementation `3984612`.
- Sector-1 EH velocity: RED `ee97d21` -> GREEN `fefab2d`.
- Sector-2 EH velocity: RED `e3a70e5` -> GREEN `bc16893`.
- Exact HR spatial-cross RED `b461763` -> GREEN `10781fc`; suite **5/5**.
- HR lapse RED `dec47a8` -> GREEN `357701e`; suite **6/6**.
- Sector-1 EH spatial RED `cfda8a1`; RED reproduced as missing function; GREEN `334ebb8`; combined suite **7/7**.
- Sector-2 EH spatial RED `b28f867`; RED reproduced as missing function; GREEN `d32b762`; combined local A2 suite **8/8 passed**.

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
  - [x] **A2.4c1 — sector-1 source-unambiguous EH spatial constraint block;**
  - [x] **A2.4c2 — sector-2 source-unambiguous EH spatial constraint block;**
  - [ ] **A2.4d — lapse-square/background-matter terms for TWO matter sectors. NEXT CRITICAL PATH.**
    - [ ] recover two-matter lapse coefficients from De Felice action/background constraints or an equivalent independent derivation;
    - [ ] pin sector-g coefficient with visible matter/radiation;
    - [ ] pin sector-f coefficient with twin matter and all lapse factors;
    - [ ] keep this separate from the one-sided scalar-matter Lagos coefficient.
  - [ ] **A2.5 — dRGT scalar interaction.** SUBSTANTIALLY ADVANCED.
    - [x] exact HR diagonal-spatial evaluator;
    - [x] spatial mixed Hessian / `Ztilde` regression;
    - [x] lapse extension + lapse-spatial `Z` regression;
    - [x] independent relative-shift quadratic block;
    - [ ] assemble/export full raw dRGT quadratic Hessian from validated pieces;
    - [ ] optional direct non-diagonal shift check if A3 exposes an inconsistency.
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

**Resume at A2.4d — two-matter lapse-square/background terms.**

1. Use De Felice 1404.0008, not the one-sided scalar-matter term in Lagos, to determine how `rho_g+P_g` and `rho_f+P_f` enter the auxiliary lapse sector.
2. Keep Lagos' already-validated EH velocity/spatial blocks and exact HR potential fixed.
3. Derive one lapse-square/background coefficient family at a time and write RED before implementation.
4. Preserve the f-sector `Nbar/r/nu` factors explicitly and cross-check the JANUS ↔ De Felice background relation at the same point.
5. Keep all current **8/8** A2 regressions green.
6. After both lapse sectors are pinned, assemble the raw quadratic matrices and begin A3 auxiliary elimination.
7. Update this file after every hard source fact, RED/GREEN transition, rejected coefficient reading, or restart-point change.
