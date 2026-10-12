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
- Exact JANUS -> Lagos background dictionary is fixed analytically:
  - `r=b/a=xi`;
  - `Nbar=c*xi`;
  - `H_LF=calH/a` and `Hb_LF=H_omega/a` because Lagos uses g-sector cosmic time;
  - with `M_g^2=1`, `M_1^2=1`, `M_2^2=kappa`, `nu^2=1/kappa`;
  - `Z=m^2(beta1+2 beta2 r+beta3 r^2)=m^2 J=m^2 f2/xi`;
  - `Ztilde=m^2[beta1+beta2(r+Nbar)+beta3 r Nbar]=m^2 Gamma/xi=m^2 f1/xi`.
- Healthy-branch kinematics gives `db/da=xi+y_N=c*xi=Nbar` on Candidate C.
- **Spatial derivative normalization ruling:** Lagos raises spatial indices with each sector's background spatial metric. For a comoving Fourier wave number `k`, `partial_1^2 -> -k^2/a^2` and `partial_2^2 -> -k^2/b^2`. Therefore factors such as `a^2 partial_1^2` and `b^2 partial_2^2` in Eqs. (3.6)-(3.7) cancel the metric scale factors. Do not use the earlier incorrect convention `partial^2 -> -k^2` directly inside those terms.
- With that convention, the complete B-shift interaction terms from Lagos Eqs. (3.6)-(3.8) combine into
  `a M1^2 Z k^2/[2(Nbar+r)] * [r B1-(Nbar/r)B2]^2`.
- The raw velocity Hessian has identically zero rows/columns for `Phi1,B1,Phi2,B2`. The Einstein-Hilbert cross-velocity coefficients are `K(Psi1,E1)=-2 k^2 a^3 M1^2` and `K(Psi2,E2)=-2 k^2 (Nbar b^3 M2^2)/Nbar^2` in the module's Hessian convention.

## RED/GREEN ledger

- A1 RED: `tests/test_lagos_bridge.py` commit `ce5aee2`; reproduced as `ModuleNotFoundError`.
- A1 GREEN core: `numerics/lagos_bridge.py` commit `dca0d52`; standalone bridge checks passed.
- Full repository execution of `tests/test_lagos_bridge.py` remains pending when a complete checkout is locally available.
- A2 initial RED: `tests/test_bigravity_scalar_action.py` commit `917aec5`; module absent.
- A2 first implementation: `numerics/bigravity_scalar_action.py` commit `f0de003`.
- Root-cause audit found the initial test itself used the wrong spatial-derivative normalization. This was a test/specification error, not a physics result.
- Corrected RED test committed as `f56c58f`; it failed against the old implementation on both the shift-square and kinetic cross-term normalization, as expected.
- Corrected implementation committed as `3984612`; the two source-normalized local checks pass. The obsolete earlier scratch assertion remains intentionally invalid and must not be reused.

## Active task list

- [x] **A0 — establish independent source route.**
- [ ] **A1 — close convention map JANUS ↔ Lagos–Ferreira.** CORE MAP COMPLETE / FULL-REPO TEST PENDING.
  - [x] map `a,b,Nbar,r,H,Hb,M1,M2`;
  - [x] map `Z,Ztilde`;
  - [x] encode `numerics/lagos_bridge.py`;
  - [ ] run full `tests/test_lagos_bridge.py` in complete checkout and record output.
- [ ] **A2 — encode the gravity quadratic action independently.** IN PROGRESS.
  - [x] lock scalar perturbation normalization and cosmic-time conventions;
  - [x] lock spatial derivative/Fourier normalization;
  - [x] establish raw field order `Phi1,B1,Psi1,E1,Phi2,B2,Psi2,E2`;
  - [x] TDD slice: auxiliary fields have no velocity Hessian rows/columns;
  - [x] TDD slice: correct relative-shift quadratic block;
  - [x] TDD slice: Einstein-Hilbert Psi/E cross-velocity coefficients;
  - [ ] **A2.4 — encode the remaining raw Einstein-Hilbert scalar blocks from Eqs. (3.6)-(3.7), one independently testable coefficient family at a time.** NEXT.
  - [ ] **A2.5 — encode the dRGT scalar interaction block Eq. (3.8), one coefficient family at a time.**
  - [ ] keep module independent of `comelli_dae`, `comelli_transfer`, `comelli_descriptor`.
- [ ] **A3 — algebraically eliminate auxiliary lapses/shifts.**
  - [ ] eliminate `Phi1,Phi2,B1,B2`;
  - [ ] verify reduced kinetic Hessian loses `Psi2` direction;
  - [ ] eliminate remaining auxiliary scalar;
  - [ ] remove gauge directions / use gauge invariants.
- [ ] **A4 — principal-symbol regression.**
  - [ ] add two barotropic matter action/sound-speed blocks;
  - [ ] derive high-k generalized eigenproblem;
  - [ ] recover matter speeds and De Felice Eq. (86) gravity `c_s^2`;
  - [ ] >=3 `(a,k/H)` points with convergence.
- [ ] **A5 — exact Case-C regression.**
  - [ ] evaluate on `numerics/comelli_case_c.py`;
  - [ ] derive pure-gravity relative scalar equation;
  - [ ] recover B.5 or explicit invertible equivalent.
- [ ] **A6 — compare back to Comelli.**
  - [ ] transform action variables to Comelli gauge invariants;
  - [ ] compare constraints and f-sector spatial interaction term-by-term;
  - [ ] identify exact source of missing `k^2 E` in old reduction.
- [ ] **A7 — replace native solver** only after A1-A6 pass.

## Immediate restart instruction

Resume at **A2.4**.

1. Re-open Lagos–Ferreira Eqs. (3.6)-(3.7) before adding each coefficient family; preserve their spatial-metric derivative convention.
2. Add one failing test for a raw Einstein-Hilbert coefficient family (recommended: `Phi-Psi_dot`, `B-Psi_dot`, and spatial `Psi^2/Phi Psi` terms for sector 1 first).
3. Verify RED against the current module.
4. Implement only that family and verify GREEN before moving to sector 2.
5. Then add Eq. (3.8) dRGT interaction terms by separate RED/GREEN slices.
6. Do not import or compare against Comelli until the independent action has passed A3-A5.
7. Update this file after every hard ruling, corrected test specification, RED/GREEN transition, or restart-point change.
