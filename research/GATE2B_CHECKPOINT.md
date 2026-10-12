# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **authoritative restart point after any interruption**. Read this file first and update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The direct Comelli route is closed negatively. The active route is an independent quadratic-action reconstruction. The De Felice matter action and Lagos pure-metric structural action are both available. The current combined two-matter action is still experimental, but the earlier claim that its post-lapse/shift 6x6 kinetic Hessian must already have rank 3 was **wrong**: De Felice explicitly states that after eliminating the four lapse/shift variables, six scalar variables remain, including two pure-gauge modes and one would-be BD mode. Gauge fixing and BD elimination come afterwards.

## Closed facts

### JANUS / bigravity convention bridge

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi*J`, `f1=Gamma`.
- Lagos massive-bigravity: `r=xi`, `Nbar=xi*c`, `Z=m^2 J=m^2 f2/xi`, `Z_tilde=m^2 Gamma/xi=m^2 f1/xi`.
- Independent De Felice principal-action module gives Candidate C at `a=0.5`: `c_s^2 ~= 0.69208`, `c_s ~= 0.83191`.

### Direct Comelli route — closed negative result

- Candidate C reproduces the visible radiation speed exactly but gives a false gravity pair `c~0.0159` instead of `~0.8319`.
- Dust+dust gives the same failure; at large k the false frequency tends to a constant, proving the physical helicity-0 `k^2 E` term is structurally absent from the old reduction.
- Correctly treating `B1` as nondynamical still does not recover Case-C B.5.
- Ruled out as sufficient fixes: unit conversion, matter mixture, closure-row choice, single derivative coefficient, A1/A2 typo, A.18 drop-in swap, f-trace sign flip, conditioning, selected minors, frozen-time PGCD, and merely eliminating `B1'`.
- Printed A.3/A.18 has `calE`; raw gauge invariants give `calE'` exactly and finite-tau Bianchi checks support the derived-prime identity. Keep printed-unprime only as a typo/control branch.

### Exact Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`.

- Exact branch: `a^4 xi^2 + xi - a - a^4/3 = 0`.
- `numerics/comelli_case_c.py` supplies exact background/conformal map and `rho1`, `rho2`.
- Acceptance: `E''+(3/tau)E'-(2/3)k^2E=0`.
- Equivalently `E=tau^2e(x)`, `x=k tau`: `x^2e_xx+7xe_x+8e-(2/3)x^2e=0`.

## Action reconstruction status

### Pure-metric Lagos structural layer

- `numerics/lagos_scalar_action.py` reconstructs the Lagos-Ferreira metric scalar action and algebraically eliminates `Phi1,Phi2,B1,B2`.
- On pure-metric proportional controls the post-auxiliary kinetic Hessian has one physical relative-scalar kinetic direction.
- This remains a structural control; physical two-matter validation is still pending.

### De Felice P(X) matter layer

`numerics/de_felice_matter_action.py` implements the complete scalar quadratic matter block of De Felice Eq. (54).

- Flat scalar identities: `TrH=6 psi`, `H_ij H^ij=12 psi^2+(2/3)k^4E^2`, `V_iV^i=k^2B^2`.
- Metric-off action gives `L = h/(2cs2) qdot^2 - N^2 h k^2 q^2/(2a^2)`, hence `c_coord^2=N^2 cs2/a^2` directly from the action.
- One-sector TDD: RED `9630a68`, GREEN `d686ccb`.
- Lagos -> De Felice scalar bridge:
  - `Phi_DF = Phi_L` (Lagos ADM relation `delta N=Phi_L` fixes the same lapse normalization as De Felice `g00=-N^2(1+2Phi)`; the PDF text extraction of the Lagos line element can lose the printed 2);
  - `B_DF = B_L/a_sector`;
  - `E_DF = 2E_L`;
  - `psi_DF = -Psi_L - k^2 E_L/3`.
- Lapse bridge correction TDD: RED `5340f9e`, GREEN `541b483`.
- Generic sector wrapper includes `N a_sector^3`; common-normalized wrapper divides by `M_g^2 a_ref^3`. TDD normalization: RED `cbc39fe`, GREEN `740bf02`.
- For f sector `b=a*r`, `Nbar=r*c`, metric-off speed is `(Nbar/b)^2 cs_f^2=(c/a)^2 cs_f^2`.
- Keep `cs2>0` through unreduced P(X); take dust only after constrained reduction.

### Experimental combined two-matter action

- RED test scaffold: `b9187b5`.
- Implementation: `8efad30`, `numerics/two_matter_scalar_action.py`.
- It sums the Lagos metric action + two normalized Eq. (54) matter sectors and algebraically eliminates `Phi1,Phi2,B1,B2`.
- The raw post-auxiliary 6x6 velocity Hessian can have rank 6. **This is not by itself a failure.** De Felice Sec. IV.E explicitly says that after integrating out `B,b,Phi,varphi`, the action still depends on six variables `(psi,Sigma,E,S,delta_phi_g,delta_phi_f)`; two are pure gauge and one additional combination is the non-dynamical would-be BD mode.
- De Felice then fixes the flat gauge `E=psi=0` and integrates out the BD combination, leaving three physical scalars `Y1,Y2,Y3`.
- Therefore the old test expectation “6x6 rank=3 immediately after lapse/shift elimination” is superseded and must be replaced by a gauge-fixed / BD-reduced criterion.
- In Lagos variables, g-flat gauge corresponds to `E1=0` and `Psi1=0`, because `E_DF=2E1` and `psi_DF=-Psi1-k^2E1/3`.

## Important correction to the previous diagnosis

The earlier checkpoint claimed that a single-fluid GR post-auxiliary Hessian rank >1 proved an EH/matter action mismatch. That criterion was premature: before fixing scalar gauge, the reduced variables still contain gauge directions. The authoritative De Felice reduction confirms the correct order:

1. expand full action;
2. integrate out lapse/shift auxiliaries;
3. fix the two scalar coordinate gauges (e.g. g-flat `E=psi=0`);
4. identify and eliminate the remaining non-dynamical BD combination;
5. only then count three physical bimetric scalars and extract propagation speeds.

The Lagos+matter assembly is therefore **not cleared**, but neither is it rejected by the raw 6x6 rank test.

## Active task list

- [x] Convention bridge / Candidate-C / Case-C backgrounds.
- [x] Reject direct Comelli closure for Gate-2B physics.
- [x] Independent De Felice high-k target.
- [x] Pure metric Lagos structural reconstruction.
- [x] Full one-sector De Felice Eq. (54) P(X) matter action.
- [x] Lagos/De Felice scalar-variable bridge and g/f sector volume normalization.
- [x] Common `M_g^2 a^3` normalization helper.
- [ ] **T1c — independent scalar action reconstruction.** IN PROGRESS.
  - [x] 6o.5a — one-sector P(X) action.
  - [x] 6o.5b — two-sector normalization/bridge.
  - [ ] **6o.5c — combined metric + two-fluid quadratic action.**
    - [x] 6o.5c.1 — common normalization.
    - [x] 6o.5c.2 — add `(q_g,q_f)` at action level.
    - [x] 6o.5c.3 — algebraically eliminate `Phi1,Phi2,B1,B2`.
    - [ ] **6o.5c.4 — replace invalid raw-rank test by De Felice reduction order.**
      - [ ] 6o.5c.4a — impose g-flat gauge `Psi1=E1=0` after auxiliary elimination.
      - [ ] 6o.5c.4b — compute 4-variable gauge-fixed velocity Hessian on exact Case C / another on-shell healthy control; acceptance: one null/nondynamical BD direction and rank 3.
      - [ ] 6o.5c.4c — identify the null/BD combination and eliminate it algebraically at action level.
      - [ ] 6o.5c.4d — express the three remaining variables in a basis equivalent to De Felice `Y1,Y2,Y3`.
  - [ ] **6o.5d — derive 3x3 high-k principal kinetic/gradient matrices and recover three speeds.**
    - g-fluid speed from its own light cone;
    - f-fluid speed from its lapse-rescaled light cone;
    - gravity speed must equal independent De Felice Eq. (86) without importing Eq. (86) into the calculation.
  - [ ] 6o.6p — compare action-derived constraints with Comelli and identify what the old closure lost.
  - [ ] 6o.6q — Case-C acceptance: recover B.5 or explicitly equivalent action equation.
- [ ] T2 — Candidate-C full scalar validation.
- [ ] T3 — replace faulty old scalar closure.
- [ ] T4 — native/action-based transfer solver.
- [ ] T5 — make `tests/test_comelli_native_scalar.py` green + >=3 extra `(z,k)` regressions.
- [ ] T6 — full Gate-2B regression suite.
- [ ] T7 — time-domain transfer matrix.
- [ ] T8 — continuous GR-connected mode tracking.
- [ ] T9 — `T_gg,T_gf,T_fg,T_ff` and relative growth.
- [ ] T10 — Gate-2B scientific verdict.

## Current RED regressions

- `tests/test_comelli_native_scalar.py` remains intentionally RED until T1c closes.
- `tests/test_two_matter_scalar_action.py` currently contains the **obsolete** expectation that the ungauged post-auxiliary 6x6 kinetic Hessian has rank 3. Replace this test before interpreting its failure.

## Immediate restart instruction

**Resume at T1c / 6o.5c.4a — De Felice gauge reduction.**

1. Do not return to the direct Comelli closure.
2. Keep the current combined action experimental until the De Felice gauge/BD reduction passes.
3. After eliminating `Phi1,Phi2,B1,B2`, impose g-flat gauge `E_DF=psi_DF=0`, i.e. `E1=Psi1=0` in the current Lagos variables.
4. Work with remaining variables `(Psi2,E2,q_g,q_f)` and their rates.
5. On an exact on-shell background, the gauge-fixed kinetic Hessian should have one non-dynamical direction and rank 3. Use exact Case C first because it supplies radiation + f-dust background equations; keep `cs_f^2>0` as a regulator until after reduction.
6. Identify and eliminate the BD direction from the action, then transform to a three-variable gauge-invariant-equivalent basis.
7. Only after the 3-variable action is obtained compute high-k propagation eigenvalues.
8. Update this file immediately after every hard finding or task-state change.
