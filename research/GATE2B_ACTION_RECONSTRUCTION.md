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
- Exact JANUS -> Lagos map:
  - `r=b/a=xi`;
  - `Nbar=c*xi`;
  - `H_LF=calH/a`, `Hb_LF=H_omega/a`;
  - `M1^2=1`, `M2^2=kappa`, `nu^2=1/kappa`;
  - `Z=m^2 J=m^2 f2/xi`;
  - `Ztilde=m^2 Gamma/xi=m^2 f1/xi`.
- Healthy branch: `db/da=xi+y_N=c*xi=Nbar` on Candidate C.
- **Spatial derivative normalization:** Lagos raises spatial indices with each sector's background spatial metric. For comoving `k`, `partial_1^2=-k^2/a^2`, `partial_2^2=-k^2/b^2`. Never reuse the rejected convention `partial^2=-k^2` inside Eq. (3.6)/(3.7) terms that already carry `a^2` or `b^2`.
- Correct relative-shift block:
  `a M1^2 Z k^2/[2(Nbar+r)] * [r B1-(Nbar/r)B2]^2`.
- Raw velocity Hessian has zero rows/columns for `Phi1,B1,Phi2,B2`.
- Sector-1 EH velocity block is now encoded directly from Eq. (3.6):
  `a^3 M1^2[-3 Psidot1^2-6 H Phi1 Psidot1-2 k^2 Edot1(Psidot1+H Phi1)+2 k^2/a^2 Psidot1 B1]`.
- Sector-2 EH velocity block is encoded directly from Eq. (3.7), retaining lapse factors:
  `Nbar b^3 M2^2[-3 Psidot2^2/Nbar^2-6 Hb Phi2 Psidot2/Nbar^2-2 k^2 Edot2(Psidot2+Hb Phi2)/Nbar^2+2 k^2 Psidot2 B2/(Nbar b^2)]`.

## RED/GREEN ledger

- A1 RED `ce5aee2`; A1 bridge implementation `dca0d52`. Full-repo bridge test still pending when a complete local checkout is available.
- A2 initial RED `917aec5`; first implementation `f0de003`.
- Initial spatial-derivative test specification was wrong. Root cause was identified before proceeding; corrected RED `f56c58f` failed on both affected coefficient families as expected.
- Correct normalization implementation `3984612`; source-normalized checks green.
- Sector-1 EH velocity RED `ee97d21`; RED reproduced as missing function; GREEN implementation `fefab2d`.
- Sector-2 EH velocity RED `e3a70e5`; RED reproduced as missing function; GREEN implementation `bc16893`.
- Combined local A2 verification after `bc16893`: **4/4 tests passed** (relative shift square, raw Hessian, sector-1 velocity block, sector-2 velocity block).

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
  - [x] **A2.4a — sector-1 EH velocity block Eq. (3.6);**
  - [x] **A2.4b — sector-2 EH velocity block Eq. (3.7);**
  - [ ] **A2.4c — remaining non-velocity EH scalar terms (`Phi/Psi/B/E` spatial and background-curvature families), one source-verified family at a time.**
  - [ ] **A2.5 — dRGT scalar interaction Eq. (3.8), one coefficient family at a time. NEXT PRIORITY.**
  - [ ] module must remain independent of old Comelli reduction modules.
- [ ] **A3 — eliminate auxiliaries from the action.**
  - [ ] eliminate `Phi1,Phi2,B1,B2`;
  - [ ] verify post-elimination kinetic Hessian loses the expected extra scalar direction;
  - [ ] eliminate remaining auxiliary scalar;
  - [ ] gauge-reduce / use gauge invariants.
- [ ] **A4 — high-k regression.**
  - [ ] add two barotropic matter blocks;
  - [ ] generalized eigenproblem;
  - [ ] recover De Felice Eq. (86) gravity speed + matter speeds;
  - [ ] >=3 Candidate-C points with high-k convergence.
- [ ] **A5 — exact Case-C regression.** Recover B.5 or explicitly equivalent equation.
- [ ] **A6 — compare validated action reduction back to Comelli** and locate missing `k^2E` structure.
- [ ] **A7 — replace native scalar solver** only after A1-A6 pass.

## Immediate restart instruction

**Resume at A2.5 (dRGT interaction), while filling A2.4c only when a coefficient family is source-unambiguous.**

1. Re-open Lagos-Ferreira Eq. (3.8) and isolate one independently readable coefficient family.
2. Prefer relative combinations (`E1-E2`, `Psi1-Psi2`, lapse/shift relative combinations) whose structure is fixed by dRGT and gauge invariance.
3. Write a failing test first and reproduce RED against `bc16893` or later branch head.
4. Implement only that family, then verify it together with the existing 4/4 A2 checks.
5. Do not guess terms whose PDF/TeX extraction is ambiguous. Record ambiguity and move to a different independently readable family.
6. Update this file after every hard source fact, RED/GREEN transition, rejected coefficient reading, or restart-point change.
