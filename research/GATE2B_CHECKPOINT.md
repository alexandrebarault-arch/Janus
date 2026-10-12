# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **authoritative restart point after any interruption**. Read this file first and update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The direct Comelli route is closed negatively. The active route is an independent quadratic-action reconstruction. The De Felice matter action is now under control, but the first attempt to append it to the background-reduced Lagos metric action fails the single-fluid GR degree-count control. Therefore `numerics/two_matter_scalar_action.py` is currently an **experimental RED implementation**, not a validated physical solver.

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
- A.3/A.18 printed form contains `calE`; raw gauge-invariant definitions give `calE'` exactly. Finite-tau Bianchi checks support the derived-prime identity. Keep printed-unprime only as a typo/control branch.

### Exact Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`.

- Exact branch: `a^4 xi^2 + xi - a - a^4/3 = 0`.
- `numerics/comelli_case_c.py` supplies the exact background and conformal map.
- Acceptance equation: `E''+(3/tau)E'-(2/3)k^2E=0`.
- Equivalently `E=tau^2e(x)`, `x=k tau`: `x^2e_xx+7xe_x+8e-(2/3)x^2e=0`.

## Action reconstruction status

### Pure metric Lagos layer

- `numerics/lagos_scalar_action.py` reconstructs the Lagos-Ferreira massive-bigravity scalar metric action and algebraically eliminates `Phi1,Phi2,B1,B2`.
- On pure-metric proportional controls the post-auxiliary kinetic Hessian has rank 1 and only the relative scalar `E-` carries kinetic weight.
- This layer remains useful as a structural bigravity check, but it is **not yet safe to combine with an independently added general matter action**, because Lagos Eq. (3.6)-(3.7) is background-reduced and already contains matter-background metric terms in its one-matter derivation.

### De Felice P(X) matter layer — validated algebraically

`numerics/de_felice_matter_action.py` now implements the complete scalar quadratic matter block of De Felice Eq. (54).

- Flat scalar identities: `TrH=6 psi`, `H_ij H^ij=12 psi^2+(2/3)k^4E^2`, `V_iV^i=k^2B^2`.
- With metric perturbations off: `L = h/(2cs2) qdot^2 - N^2 h k^2 q^2/(2a^2)`, so the action itself gives `c_coord^2=N^2 cs2/a^2`.
- One-sector full-action TDD: RED `9630a68`, GREEN `d686ccb`.
- Lagos -> De Felice scalar bridge currently used:
  - `Phi_DF = Phi_L` (corrected after checking Lagos ADM relation `delta N = Phi_L`; PDF text extraction can lose the factor 2 in `g_00`);
  - `B_DF = B_L/a_sector`;
  - `E_DF = 2 E_L`;
  - `psi_DF = -Psi_L - k^2 E_L/3`.
- Bridge correction TDD: RED `5340f9e`, GREEN `541b483`.
- Generic sector wrapper includes volume `N a_sector^3`.
- For f sector `b=a*r`, `Nbar=r*c`, metric-off propagation gives `(Nbar/b)^2 cs_f^2=(c/a)^2 cs_f^2`.
- Common normalization helper divides each full matter sector by `M_g^2 a_ref^3`, matching the normalization of the Lagos metric action. TDD: RED `cbc39fe`, GREEN `740bf02`.
- Keep `cs2>0` through unreduced P(X); take dust only after constrained reduction.

### First combined two-matter attempt — RED / diagnostic only

- RED test: `b9187b5`.
- Experimental implementation: `8efad30`, `numerics/two_matter_scalar_action.py`.
- It sums the Lagos metric action with two normalized Eq. (54) matter sectors and algebraically eliminates `Phi1,Phi2,B1,B2`.
- Auxiliary stationarity can be solved, but the physical degree-count control fails:
  - arbitrary proportional background: reduced 6-variable kinetic Hessian rank 6, not 3;
  - actual on-shell Candidate-C background: still rank 6;
  - more decisively, **single-metric GR + one P(X) fluid already gives rank 3 instead of the expected one scalar mode** when the current Lagos/EH block is combined with Eq. (54).
- Therefore the failure occurs before bigravity and before the second matter sector.
- Do **not** tune coefficients or proceed to propagation eigenvalues from `two_matter_scalar_action.py`.

## Root-cause localization

The present best explanation is an **action-layer mismatch**, not a two-fluid instability:

- Lagos Eq. (3.6)-(3.7) is written after using background equations and explicitly includes metric-only matter-background contributions in their one-matter setup.
- Appending the completely general De Felice Eq. (54) matter action to that background-reduced Lagos gravitational block double-counts / mismatches the terms needed for scalar gauge degeneracy.
- This is why the GR one-fluid kinetic rank already fails.

The clean repair is to reconstruct the gravitational quadratic action directly in **De Felice conventions**, from their general Einstein-Hilbert Eq. (44), and combine it with Eq. (54) before using background equations. Only after the single-fluid GR control is correct should the second metric and Hassan-Rosen interaction be added.

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
  - [ ] **6o.5c-R1 — rebuild a matter-compatible Einstein-Hilbert scalar action directly from De Felice Eq. (44).**
    - [ ] **R1.1 — transcribe flat scalar Eq. (44) in De Felice variables `(Phi,B,psi,E)` without using matter background substitutions.**
    - [ ] **R1.2 — combine Eq. (44)+Eq. (54) for one GR metric + one regular P(X) fluid.**
    - [ ] **R1.3 — algebraically eliminate lapse and shift and require physical scalar kinetic rank = 1.**
    - [ ] **R1.4 — derive the remaining high-k eigenvalue and require `c^2=N^2 cs2/a^2` without inserting it.**
  - [ ] **6o.5c-R2 — duplicate the validated EH+matter sector for the f metric (`n,b,M_f`).**
  - [ ] **6o.5c-R3 — add the Hassan-Rosen interaction using De Felice Eq. (45)-(46) / equivalent source-consistent form before background reduction.**
  - [ ] **6o.5c-R4 — eliminate four bimetric lapse/shift auxiliaries; require exactly 3 scalar kinetic directions for two fluids + helicity-0.**
  - [ ] **6o.5d — derive the three high-k speeds; gravity must match independent De Felice Eq. (86), matter speeds must match sector light-cone rescalings.**
  - [ ] 6o.6p — compare action-derived constraints with Comelli and identify the structure lost by the old closure.
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

- `tests/test_comelli_native_scalar.py` remains intentionally RED until T1c is closed.
- `tests/test_two_matter_scalar_action.py` rank=3 requirement is also intentionally RED under the current experimental Lagos+Eq54 assembly; do not make it green by coefficient tuning.

## Immediate restart instruction

**Resume at T1c / 6o.5c-R1.1 — De Felice Einstein-Hilbert Eq. (44).**

1. Do not return to the direct Comelli closure.
2. Do not use the experimental combined Lagos+matter action for physical conclusions.
3. Work entirely in De Felice variables for the GR control: Eq. (44) + Eq. (54), same lapse/shift/spatial decomposition and same coordinate time.
4. Preserve background `H`, `dot H`, lapse `N`, and scale factor `a` until after the quadratic action is assembled.
5. Integrate shift time-derivative terms by parts only at the action level; never differentiate a constraint equation.
6. First acceptance gate: one metric + one P(X) fluid on an on-shell GR FLRW background must reduce to exactly one scalar kinetic direction.
7. Second gate: its high-k speed must emerge as `N^2 cs2/a^2`.
8. Only then add the f-sector EH action and Hassan-Rosen mixing.
9. Update this file immediately after every hard finding or completed subtask.
