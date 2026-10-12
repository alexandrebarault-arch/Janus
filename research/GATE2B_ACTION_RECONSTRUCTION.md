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

- De Felice 1404.0008 eliminates nondynamical scalar modes and the would-be BD mode, leaving three physical gauge-invariant variables `Y1,Y2,Y3`, with `Y3=S-E`, and a reduced 3x3 quadratic action. Eq. (86) gives one gravitational scalar speed plus the two matter sound speeds.
- Lagos-Ferreira 1610.00553 gives the raw bimetric quadratic action. In massive bigravity, `Phi_A` and `B_A` are auxiliary; after eliminating them another scalar becomes auxiliary, leaving one gravitational scalar after gauge reduction.
- Massive bigravity specialization: `alpha_L=0`, constant Planck masses, dRGT `Z,Ztilde`.
- Exact JANUS -> Lagos map: `r=xi`, `Nbar=c xi`, `H_LF=calH/a`, `Hb_LF=H_omega/a`, `M1^2=1`, `M2^2=kappa`, `nu^2=1/kappa`, `Z=m^2 f2/xi`, `Ztilde=m^2 f1/xi`.
- Healthy branch: `db/da=xi+y_N=c xi=Nbar` on Candidate C.
- **Spatial derivative normalization:** for comoving `k`, Lagos has `partial_1^2=-k^2/a^2`, `partial_2^2=-k^2/b^2`. Never reuse the rejected convention `partial^2=-k^2` inside terms already carrying `a^2` or `b^2`.
- Correct relative-shift block: `a M1^2 Z k^2/[2(Nbar+r)] [r B1-(Nbar/r)B2]^2`.
- Raw velocity Hessian has zero rows/columns for `Phi1,B1,Phi2,B2`.
- Sector-1 and sector-2 EH velocity blocks from Lagos Eqs. (3.6)-(3.7) are implemented with explicit lapse/scale-factor normalization and jointly regression-tested.
- **Exact Hassan-Rosen potential evaluator added:** `hr_diagonal_scalar_potential_density` computes `m^2 M1^2 sqrt(-g) sum beta_n e_n(sqrt(g^{-1}f))` directly for diagonal scalar spatial perturbations. It does not use precomputed `J`, `Gamma`, `Z` or `Ztilde` internally.
- Independent expansion/regression of that exact potential gives the spatial mixed Hessian identities
  - `d2L/(dPsi1 dPsi2)=6 a^3 M1^2 r Ztilde`;
  - `d2L/(dPsi1 dE2)=d2L/(dE1 dPsi2)=2 a^3 M1^2 r Ztilde k^2`;
  - `d2L/(dE1 dE2)=0`.
  The vanishing `k^4 E1 E2` mixed term is a direct ghost-free tuning check, not imported from Comelli/Lagos reduced equations.

## RED/GREEN ledger

- A1 RED `ce5aee2`; A1 bridge implementation `dca0d52`. Full-repo bridge test still pending when a complete local checkout is available.
- A2 initial RED `917aec5`; first implementation `f0de003`.
- Initial spatial-derivative test specification was wrong. Root cause was identified; corrected RED `f56c58f` failed on both affected coefficient families as expected. Correct implementation `3984612`.
- Sector-1 EH velocity RED `ee97d21` -> GREEN `fefab2d`.
- Sector-2 EH velocity RED `e3a70e5` -> GREEN `bc16893`.
- Combined local verification after `bc16893`: **4/4 passed**.
- First exact dRGT/HR spatial-cross RED: `b461763` added the missing-function regression for the exact potential evaluator.
- GREEN implementation: `10781fc` added exact diagonal HR evaluator.
- Combined local verification after `10781fc`: **5/5 passed**. Numerical mixed derivatives at the test point were `Psi1-Psi2=0.2793697912`, `Psi1-E2=0.6295133859`, `E1-Psi2=0.6295131083`, `E1-E2=1.39e-7`; all satisfy the analytic `Ztilde` identities/tolerance.

## Active task list

- [x] **A0 — independent source route established.**
- [ ] **A1 — JANUS ↔ Lagos map.** CORE COMPLETE / FULL-REPO TEST PENDING.
  - [x] background dictionary;
  - [x] `Z,Ztilde` dictionary;
  - [x] `numerics/lagos_bridge.py`;
  - [ ] run full `tests/test_lagos_bridge.py` in complete checkout.
- [ ] **A2 — raw gravity quadratic action.** IN PROGRESS.
  - [x] perturbation/cosmic-time conventions locked;
  - [x] spatial/Fourier normalization locked;
  - [x] raw field order locked;
  - [x] auxiliary fields absent from raw velocity Hessian;
  - [x] relative-shift interaction square;
  - [x] raw Psi/E kinetic Hessian coefficients;
  - [x] **A2.4a — sector-1 EH velocity block;**
  - [x] **A2.4b — sector-2 EH velocity block;**
  - [ ] **A2.4c — remaining non-velocity EH scalar terms, one source-verified family at a time.**
  - [ ] **A2.5 — dRGT scalar interaction.** IN PROGRESS.
    - [x] A2.5a exact HR diagonal-spatial evaluator;
    - [x] A2.5b spatial mixed Hessian / `Ztilde` regression + vanishing `E1E2 k^4` check;
    - [ ] **A2.5c — extend exact HR evaluator to lapse perturbations `Phi1,Phi2` and pin lapse-spatial mixed Hessian families. NEXT.**
    - [ ] A2.5d — add shift-containing exact potential slice or source-verified Eq. (3.8) shift/lapse family;
    - [ ] A2.5e — assemble full raw dRGT scalar quadratic Hessian.
  - [ ] module must remain independent of old Comelli reduction modules.
- [ ] **A3 — eliminate auxiliaries from the action.**
  - [ ] eliminate `Phi1,Phi2,B1,B2`;
  - [ ] verify post-elimination kinetic Hessian loses expected extra scalar direction;
  - [ ] eliminate remaining auxiliary scalar;
  - [ ] gauge-reduce / use gauge invariants.
- [ ] **A4 — high-k regression.** Recover De Felice Eq. (86) gravity speed + matter speeds at >=3 Candidate-C points.
- [ ] **A5 — exact Case-C regression.** Recover B.5 or explicit invertible equivalent.
- [ ] **A6 — compare validated action reduction back to Comelli** and locate missing `k^2E` structure.
- [ ] **A7 — replace native scalar solver** only after A1-A6 pass.

## Immediate restart instruction

**Resume at A2.5c — lapse extension of the exact HR potential evaluator.**

1. Extend the exact diagonal evaluator using Lagos lapse convention `g00=-(1+Phi1)`, `f00=-Nbar^2(1+Phi2)`; temporal square-root eigenvalue is `Nbar sqrt((1+Phi2)/(1+Phi1))` and `sqrt(-g)` gains `sqrt(1+Phi1)`.
2. Before production change, add a RED finite-difference Hessian test for lapse-spatial mixed terms derived independently from the exact potential.
3. Keep the existing 5/5 regressions green.
4. Do not introduce `Z` or `Ztilde` inside the exact evaluator; they may appear only in expected analytic test identities.
5. After lapse-spatial families pass, proceed to shift-containing exact/source-verified interaction terms, then assemble the raw dRGT quadratic Hessian.
6. Update this file after every hard source fact, RED/GREEN transition, rejected coefficient reading, or restart-point change.
