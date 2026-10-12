# Gate 2B — independent scalar-action reconstruction

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **ACTIVE RESTART POINT FOR T1c.6o**

Purpose: reconstruct the healthy-branch scalar dynamics independently of the Comelli Appendix-A transcription. This file is the detailed restart checklist for T1c.6o. The parent checkpoint remains `research/GATE2B_CHECKPOINT.md`.

## Binding acceptance criteria

1. Do not use the old 12x12 Comelli closure as an input to the reconstruction.
2. Reproduce the De Felice gravitational high-k scalar speed `c_s^2` from action-derived variables on the same JANUS background map.
3. Recover the two matter sound speeds independently.
4. On exact Comelli Case C, recover an equation equivalent to `E''+(3/tau)E'-(2/3)k^2 E=0`, or derive an explicit invertible variable map to that equation.
5. Only then compare term-by-term against Comelli to localize the missing interaction structure.
6. No coefficient/sign tuning to hit a target.

## Hard source facts

- De Felice et al. arXiv:1404.0008 integrate out four nondynamical scalar modes before gauge fixing, then remove the would-be BD scalar. Their three physical gauge-invariant variables are `Y1,Y2,Y3`, with `Y3=S-E` the relative metric scalar. The final reduced action is `Ydot^T K Ydot + Ydot^T N Y - Y^T N Ydot - Y^T M Y`, with real 3x3 matrices `K,N,M`.
- Their Eq. (86) gives three high-frequency speeds: one gravitational scalar speed plus the two matter sound speeds. This is the first action-derived regression target.
- Lagos & Ferreira arXiv:1610.00553 give an explicit quadratic metric action for general non-derivative bimetric theories. In the massive-bigravity specialization, `Phi_A` and `B_A` are auxiliary; after integrating them out the kinetic term of `Psi2` vanishes, making it auxiliary too, leaving one physical gravitational scalar after gauge removal.
- Massive bigravity is obtained in their parameters with `alpha_L=0`, constant Planck masses, and their `Z,Ztilde` specialized to the dRGT beta potential.

## Active task list

- [x] **A0 — establish independent source route.** De Felice reduced action and Lagos–Ferreira explicit quadratic action identified; PDF pages visually checked.
- [ ] **A1 — close convention map JANUS ↔ Lagos–Ferreira.**
  - [ ] map `a,b,Nbar,r,H,Hb,M1,M2` to JANUS `a,xi,c,H,H_omega,kappa`;
  - [ ] map Lagos `Z,Ztilde` to JANUS `J,Gamma/f1,f2` and beta conventions;
  - [ ] verify at >=3 Candidate-C redshifts and exact Case C using background identities only.
- [ ] **A2 — encode the gravity quadratic action independently.**
  - [ ] create `numerics/bigravity_scalar_action.py` only after a failing test;
  - [ ] represent the 8 scalar metric amplitudes in Fourier space;
  - [ ] implement Einstein-Hilbert pieces + dRGT interaction from Lagos Eqs. (3.6)-(3.8), with `alpha_L=0`;
  - [ ] do not import `comelli_dae`, `comelli_transfer`, or `comelli_descriptor` in this module.
- [ ] **A3 — algebraically eliminate auxiliary lapses/shifts.**
  - [ ] eliminate `Phi1,Phi2,B1,B2` by their algebraic Euler-Lagrange equations;
  - [ ] verify the reduced kinetic Hessian loses the `Psi2` direction as Lagos states;
  - [ ] eliminate that remaining auxiliary scalar;
  - [ ] remove two gauge directions or work directly in gauge-invariant combinations.
- [ ] **A4 — principal-symbol regression.**
  - [ ] add two independent barotropic matter actions/sound-speed blocks;
  - [ ] derive the high-k generalized eigenproblem from the reduced action;
  - [ ] recover matter speeds and De Felice Eq. (86) gravitational `c_s^2` on Candidate C;
  - [ ] require >=3 `(a,k/H)` points and convergence as `k/H` increases.
- [ ] **A5 — exact Case-C regression.**
  - [ ] evaluate the action reduction on `numerics/comelli_case_c.py` background;
  - [ ] derive the pure-gravity relative scalar equation;
  - [ ] recover B.5 or an explicitly equivalent equation under an invertible variable map.
- [ ] **A6 — comparison back to Comelli.**
  - [ ] transform action variables to Comelli gauge invariants;
  - [ ] compare nondynamical constraints and f-sector spatial interaction term-by-term;
  - [ ] identify the exact source of the missing `k^2 E` term in the old transcription/reduction.
- [ ] **A7 — replace native solver.** Only after A1-A6 pass, implement/rename the native scalar system and make `tests/test_comelli_native_scalar.py` green without fitting.

## Immediate restart instruction

Resume at **A1**.

1. Read De Felice 1404.0008 around Eqs. (67)-(86), especially `Y1,Y2,Y3`, the reduced action, and `c_s^2`.
2. Read Lagos–Ferreira 1610.00553 around Eqs. (3.6)-(3.15) and the background definitions of `a,b,Nbar,r,H,Hb`.
3. Derive the exact convention map on paper/scratch first.
4. Write a failing convention-map test before production code.
5. Keep this file updated after every hard source fact, rejected mapping, RED/GREEN transition, or change in restart point.
