# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **authoritative restart point after any interruption**. Read this file first and update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The direct Comelli route is closed negatively. The active route is an independent quadratic-action reconstruction. The combined two-matter action now passes the published De Felice scalar degree-count **after the correct gauge-fixing order** on exact Case C, but a newly isolated Lagos spatial-derivative convention must be audited before the BD mode and propagation speeds can be trusted.

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

### De Felice P(X) matter layer

`numerics/de_felice_matter_action.py` implements the complete scalar quadratic matter block of De Felice Eq. (54).

- Flat scalar identities: `TrH=6 psi`, `H_ij H^ij=12 psi^2+(2/3)k^4E^2`, `V_iV^i=k^2B^2`.
- Metric-off action gives `L = h/(2cs2) qdot^2 - N^2 h k^2 q^2/(2a^2)`, hence `c_coord^2=N^2 cs2/a^2` directly from the action.
- One-sector TDD: RED `9630a68`, GREEN `d686ccb`.
- Lagos -> De Felice bridge currently used:
  - `Phi_DF = Phi_L`;
  - `B_DF = B_L/a_sector`;
  - `E_DF = 2E_L`;
  - `psi_DF = -Psi_L - k^2 E_L/3`.
- Lapse bridge correction TDD: RED `5340f9e`, GREEN `541b483`.
- Generic sector wrapper includes `N a_sector^3`; common-normalized wrapper divides by `M_g^2 a_ref^3`. TDD normalization: RED `cbc39fe`, GREEN `740bf02`.
- For f sector `b=a*r`, `Nbar=r*c`, metric-off speed is `(Nbar/b)^2 cs_f^2=(c/a)^2 cs_f^2`.
- Keep `cs2>0` through unreduced P(X); take dust only after constrained reduction.

### Combined two-matter action and correct degree count

- `numerics/two_matter_scalar_action.py` sums the Lagos metric block and two normalized Eq. (54) matter sectors and algebraically eliminates `Phi1,Phi2,B1,B2`.
- Initial scaffold `b9187b5`, implementation `8efad30`.
- The old expectation that the ungauged post-auxiliary 6x6 velocity Hessian must already have rank 3 was wrong. De Felice Sec. IV.E leaves six variables at this stage: two scalar gauge directions plus one non-dynamical BD combination are still present.
- Correct De Felice order: eliminate lapse/shift -> fix two scalar gauges -> expose/eliminate BD -> three physical scalars.
- g-flat test RED `b654ad5`; implementation `28c27bd` imposes `Psi1=E1=0` after auxiliary elimination, leaving `(Psi2,E2,q_g,q_f)`.
- Exact Case-C scratch control at `a=0.1`, `k=12`, visible radiation `cs_g^2=1/3`, f dust regularized with `cs_f^2=0.1` gives a 4x4 kinetic Hessian with **rank 3** and one numerically null eigenvalue, as required before BD elimination.
- Representative eigenvalues were approximately `[-3.9998e4, -6.6776e2, 6.9e-7, 2.998e-2]`; the smallest is ~`1.7e-11` of the dominant scale.
- Therefore 6o.5c.4a and 6o.5c.4b are closed in scratch. Full pytest remains unavailable because the container cannot clone GitHub.

### De Felice-only GR cross-check

A private direct reconstruction of De Felice Eq. (44) + Eq. (54), in the same De Felice variables, was used as an independent control.

- After lapse/shift elimination and flat gauge in single-metric GR, exactly one scalar remains.
- Its high-k coordinate speed approaches its intrinsic `cs^2` without inserting the target. Example control with `cs^2=0.35`: measured speed squared approaches `0.3485` at `k=30` and `0.349985` at `k=300`.
- This strongly validates the Eq. (54) matter transcription and provides a reference against which the Lagos self-action bridge can be tested.

## New hard finding — Lagos spatial derivative convention

Before eliminating the BD combination, the Lagos metric action must be re-audited for its Fourier/Laplacian convention.

Lagos Appendix A defines spatial index raising/lowering with the **background metric of the metric sector on which the derivative acts**. Thus on flat FLRW:

- metric 1: `partial^2 -> -k_com^2/a^2`;
- metric 2: `partial^2 -> -k_com^2/b^2`.

This matters because the published action contains explicit factors such as `a^2 partial^2 E1_dot` and `b^2 partial^2 E2_dot`; those should reduce to common comoving `-k_com^2 E_dot`, not `-a^2 k_com^2 E_dot` or `-b^2 k_com^2 E_dot`.

Current `numerics/lagos_scalar_action.py` declares `partial^2 -> -k^2` while keeping explicit `a^2` and `b^2` factors. Since `ScalarBackground.k2` is comoving/Fourier `k^2` everywhere else in JANUS, this is a concrete convention mismatch candidate.

Examples in the current EH code that require audit:

- `-2*a^2*k2*E1_dot*(Psi1_dot+H Phi1)` should be tested against Lagos `2 a^2 partial^2 E1_dot(...)` with `partial^2=-k_com^2/a^2`;
- shift term `+2*k2*Psi1_dot*B1` should be checked for the corresponding `1/a^2` contraction;
- sector-2 counterparts require `b`, not `a`;
- interaction cross-gradient terms must be audited separately because their contraction convention can differ from a pure self-sector Laplacian.

Do **not** identify/eliminate the BD mode or interpret its kinetic signs until this convention audit is closed.

## Active task list

- [x] Convention bridge / Candidate-C / Case-C backgrounds.
- [x] Reject direct Comelli closure for Gate-2B physics.
- [x] Independent De Felice high-k target.
- [x] Full one-sector De Felice Eq. (54) P(X) matter action.
- [x] Lagos/De Felice scalar-variable bridge and g/f volume normalization.
- [x] Common `M_g^2 a^3` normalization helper.
- [ ] **T1c — independent scalar action reconstruction.** IN PROGRESS.
  - [x] 6o.5a — one-sector P(X) action.
  - [x] 6o.5b — two-sector normalization/bridge.
  - [ ] **6o.5c — combined metric + two-fluid quadratic action.**
    - [x] 6o.5c.1 — common normalization.
    - [x] 6o.5c.2 — add `(q_g,q_f)` at action level.
    - [x] 6o.5c.3 — algebraically eliminate `Phi1,Phi2,B1,B2`.
    - [ ] **6o.5c.4 — De Felice gauge/BD reduction.**
      - [x] 6o.5c.4a — g-flat gauge `Psi1=E1=0` implemented.
      - [x] 6o.5c.4b — exact Case-C 4x4 gauge-fixed kinetic rank = 3 with one null direction (scratch verified).
      - [ ] **6o.5c.4-L — audit/fix Lagos spatial derivative (`partial^2`) convention before trusting the BD vector.**
        - [ ] L1 — add RED regression for sector-1 EH `E_dot-Psi_dot` coefficient: it must depend on comoving `k^2`, not `a^2 k^2`.
        - [ ] L2 — add corresponding sector-2 `b`/`Nbar` regression.
        - [ ] L3 — correct Lagos EH self-sector spatial contractions and re-run pure-metric structural controls.
        - [ ] L4 — audit interaction spatial-gradient contractions separately against Lagos Eq. (3.8).
        - [ ] L5 — re-run exact Case-C g-flat rank-3 control after corrections.
      - [ ] 6o.5c.4c — identify the null/BD combination and eliminate it algebraically at action level.
      - [ ] 6o.5c.4d — express three remaining variables in a basis equivalent to De Felice `Y1,Y2,Y3`.
  - [ ] **6o.5d — derive 3x3 high-k kinetic/gradient matrices and recover three speeds.**
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

## Test execution caveat

Container network cannot clone/download the GitHub repository. Newly added pytest files therefore cannot currently be run as a full checkout suite. TDD RED/GREEN commits are preserved in Git and core algebra is independently checked in scratch. Do not claim the full repository suite is green.

## Current RED regressions

- `tests/test_comelli_native_scalar.py` remains intentionally RED until T1c closes.
- Next intended RED is the Lagos EH spatial-Laplacian regression in `tests/test_lagos_pure_metric_action.py`.

## Immediate restart instruction

**Resume at T1c / 6o.5c.4-L1 — Lagos Laplacian convention audit.**

1. Treat `ScalarBackground.k2` as comoving Fourier `k^2`.
2. In Lagos self-sector derivatives use the sector background metric when translating `partial^2`: metric1 `k^2/a^2`, metric2 `k^2/b^2`.
3. First write a RED test isolating the `E1_dot * Psi1_dot` EH coefficient at two different `a`; after correct translation its mixed coefficient is proportional to `-2 k_com^2` and is independent of `a`.
4. Add the analogous sector-2 test including `Nbar` and the overall second-metric factor.
5. Only after self-sector EH is fixed, audit interaction Eq. (3.8) cross-gradient contractions; do not blindly apply the same metric factor to cross terms.
6. Re-run (scratch if necessary) pure-metric exchange symmetry, auxiliary stationarity, relative kinetic rank, and exact Case-C g-flat rank=3.
7. Only then identify/eliminate the BD combination and proceed to 3x3 propagation speeds.
8. Update this checkpoint after every hard finding or completed subtask.
