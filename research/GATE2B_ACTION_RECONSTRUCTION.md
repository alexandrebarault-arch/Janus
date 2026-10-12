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
- Source-unambiguous GR spatial constraint blocks are implemented:
  - sector 1: `a^3 M1^2 (k^2/a^2)[Psi1^2-2 Phi1 Psi1+2 H Phi1 B1]`;
  - sector 2: `Nbar b^3 M2^2 (k^2/b^2)[Psi2^2-2 Phi2 Psi2+2(Hb/Nbar) Phi2 B2]`.
- Do not copy Lagos' one-sided scalar-matter `Phi1^2` coefficient into JANUS: their Eq. (3.6) includes their specific matter scalar, while JANUS has matter coupled to both metrics.
- De Felice Eq. (54) gives the two-sector `P(X)` matter quadratic action; the f-sector action is obtained identically. Setting matter fluctuation, shift and spatial-metric perturbations to zero yields the pure-lapse coefficient in De Felice lapse convention `g00=-N^2(1+2 Phi)`:
  `C_matter(Phi^2) = -P/2 + [(1+c_s^2)/(2 c_s^2)] (rho+P)`.
  This applies separately to g and f before their background volume/lapse factors are multiplied in.
- **Dust ruling:** the unreduced `P(X)` coefficient is singular at `c_s^2=0`; do not substitute exact dust into this coefficient. Take the dust limit only after the constrained matter/action reduction, or use an equivalent dust action.
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
- Sector-1 EH spatial RED `cfda8a1` -> GREEN `334ebb8`; suite **7/7**.
- Sector-2 EH spatial RED `b28f867` -> GREEN `d32b762`; suite **8/8**.
- De Felice two-matter lapse RED `8f94c83` reproduced as `ModuleNotFoundError`.
- GREEN module `numerics/de_felice_matter_action.py` commit `c68bcdd`; combined local scratch run of new matter tests + existing A2 action tests: **8/8 passed**.

## Active task list

- [x] **A0 — independent source route established.**
- [ ] **A1 — JANUS ↔ Lagos map.** CORE COMPLETE / FULL-REPO TEST PENDING.
  - [x] background dictionary;
  - [x] `Z,Ztilde` dictionary;
  - [x] `numerics/lagos_bridge.py`;
  - [ ] run full `tests/test_lagos_bridge.py` in complete checkout.
- [ ] **A2 — raw gravity + two-matter quadratic action.** IN PROGRESS.
  - [x] perturbation/cosmic-time conventions;
  - [x] spatial/Fourier normalization;
  - [x] raw field order;
  - [x] auxiliary fields absent from raw velocity Hessian;
  - [x] relative-shift interaction square;
  - [x] sector-1 EH velocity block;
  - [x] sector-2 EH velocity block;
  - [x] sector-1 EH spatial constraint block;
  - [x] sector-2 EH spatial constraint block;
  - [ ] **A2.4d — lapse/background terms for TWO matter sectors. IN PROGRESS / NEXT.**
    - [x] derive and TDD-pin generic De Felice `P(X)` pure-lapse matter coefficient;
    - [x] verify same generic formula applies independently to g and f sectors before background volume factors;
    - [ ] derive total g-sector lapse Hessian = EH + HR + matter in one consistent normalization;
    - [ ] derive total f-sector lapse Hessian with all lapse/volume/Planck factors;
    - [ ] derive matter-lapse/metric cross terms needed for auxiliary elimination;
    - [ ] handle dust by constrained limit, not raw `cs2=0` substitution.
  - [ ] **A2.5 — dRGT scalar interaction.** SUBSTANTIALLY ADVANCED.
    - [x] exact HR diagonal-spatial evaluator;
    - [x] spatial mixed Hessian / `Ztilde` regression;
    - [x] lapse extension + lapse-spatial `Z` regression;
    - [x] independent relative-shift quadratic block;
    - [ ] assemble/export full raw dRGT quadratic Hessian from validated pieces;
    - [ ] optional direct non-diagonal shift check if A3 exposes an inconsistency.
- [ ] **A3 — eliminate auxiliaries from the action.**
  - [ ] eliminate metric lapses/shifts together with appropriate matter auxiliaries;
  - [ ] verify expected kinetic-rank drop / remaining auxiliary scalar;
  - [ ] eliminate it and gauge-reduce.
- [ ] **A4 — high-k regression.** Recover De Felice Eq. (86) gravity speed + matter speeds at >=3 Candidate-C points.
- [ ] **A5 — exact Case-C regression.** Recover B.5 or explicitly equivalent equation.
- [ ] **A6 — compare validated action reduction back to Comelli** and locate missing `k^2E` structure.
- [ ] **A7 — replace native scalar solver** only after A1-A6 pass.

## Immediate restart instruction

**Resume at A2.4d total auxiliary-lapse block.**

1. Stay in De Felice normalization while deriving the total lapse sector; do not mix raw Lagos and De Felice lapse variables until the explicit variable bridge is written.
2. Use De Felice generic EH quadratic action + exact HR interaction + Eq. (54) matter action to build the g-sector and f-sector lapse Hessian/mixed blocks separately.
3. Write RED tests for one coefficient family at a time before implementation.
4. Derive the De Felice↔Lagos normalization bridge for lapse/shift/spatial scalar variables before combining these blocks with the already-coded Lagos EH pieces.
5. Keep current action regressions green.
6. Treat exact dust only after constrained reduction; do not insert `cs2=0` into unreduced P(X) formulas.
7. Update this file after every hard source fact, RED/GREEN transition, rejected mapping, or restart-point change.
