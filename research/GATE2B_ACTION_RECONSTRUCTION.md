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
- Exact JANUS -> Lagos background dictionary is now fixed analytically:
  - `r=b/a=xi`;
  - `Nbar=c*xi`;
  - `H_LF=calH/a` and `Hb_LF=H_omega/a` because Lagos uses g-sector cosmic time;
  - with `M_g^2=1`, `M_1^2=1`, `M_2^2=kappa`, `nu^2=1/kappa`;
  - Lagos Eq. (3.14): `Z=m^2(beta1+2 beta2 r+beta3 r^2)=m^2 J=m^2 f2/xi`;
  - Lagos Eq. (3.15): `Ztilde=m^2[beta1+beta2(r+Nbar)+beta3 r Nbar]=m^2 Gamma/xi=m^2 f1/xi`.
- The healthy-branch kinematics also gives `db/da=xi+y_N=c*xi=Nbar` on Candidate C, providing a background-only cross-check independent of perturbations.

## RED/GREEN ledger

- A1 RED: `tests/test_lagos_bridge.py` added in commit `ce5aee2`; production module absent.
- RED was reproduced locally as `ModuleNotFoundError: numerics.lagos_bridge`.
- A1 GREEN core: minimal bridge formulas passed 2/2 standalone scratch tests and were committed as `numerics/lagos_bridge.py` in `dca0d52`.
- Full repository execution of `tests/test_lagos_bridge.py` remains to be run when the complete checkout is locally available; the test itself covers Candidate C at `a=1,0.5,0.1`, exact Case C, and the healthy-branch `db/da=Nbar` identity.

## Active task list

- [x] **A0 — establish independent source route.** De Felice reduced action and Lagos–Ferreira explicit quadratic action identified; PDF pages visually checked.
- [ ] **A1 — close convention map JANUS ↔ Lagos–Ferreira.** CORE MAP COMPLETE / FULL-REPO TEST PENDING.
  - [x] map `a,b,Nbar,r,H,Hb,M1,M2` to JANUS `a,xi,c,H,H_omega,kappa`;
  - [x] map Lagos `Z,Ztilde` to JANUS `J,Gamma/f1,f2` and beta conventions;
  - [x] encode map independently in `numerics/lagos_bridge.py`;
  - [ ] run `tests/test_lagos_bridge.py` against the complete repository checkout and record exact output.
- [ ] **A2 — encode the gravity quadratic action independently.** NEXT ACTIVE TASK.
  - [ ] inspect/lock scalar perturbation normalization used in Lagos Eqs. (3.6)-(3.8);
  - [ ] write a failing action-structure test before production code;
  - [ ] create `numerics/bigravity_scalar_action.py` only after RED;
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

Resume at **A2**.

1. Read Lagos–Ferreira 1610.00553 Eqs. (3.6)-(3.8) and the scalar perturbation definitions around Eqs. (2.24)-(2.29).
2. Lock the exact Fourier/sign/normalization convention for `Phi_A,B_A,Psi_A,E_A` before writing action code.
3. Write a failing test that checks the auxiliary-field structure (`Phi_A,B_A` have no time-derivative Hessian entries) and at least one independently readable interaction coefficient from Eq. (3.8).
4. Implement only enough of the action to make that test green, then extend by RED/GREEN slices.
5. Keep this file updated after every hard source fact, rejected mapping, RED/GREEN transition, or change in restart point.
