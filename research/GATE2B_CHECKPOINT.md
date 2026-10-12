# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **authoritative restart point after any interruption**. Read this file first and update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The old direct Comelli closure and a correctly index-reduced Comelli reconstruction both fail to recover the physical helicity-0 gradient. The active route is now an **independent scalar quadratic-action reconstruction** from De Felice 1404.0008 and Lagos-Ferreira 1610.00553.

## Closed facts

### Convention bridge

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi*J`, `f1=Gamma`.
- Lagos massive-bigravity: `r=xi`, `Nbar=xi*c`, `Z=m^2 f2/xi=m^2 J`, `Z_tilde=m^2 f1/xi=m^2 Gamma/xi`.
- Massive bigravity has `alpha_L=0`; the helicity-0 gradient is generated only after lapse/shift elimination together with Einstein-Hilbert structure, not by a standalone interaction `E^2` term.

### Independent De Felice principal action

- `numerics/de_felice_action_principal.py` independently implements De Felice Eqs. (80),(82),(86), without calling the historical diagnostics implementation.
- Candidate-C checks agree at `a=1,0.5,0.2`.
- At `a=0.5`: `c_s^2 ~= 0.69207999`, `c_s ~= 0.83191345`.

### Lagos pure metric action — independently reconstructed

- Interaction potential: test `b51940f`; implementation `894b692`; Eq. (3.7) PDF-parsing correction `2de9354`.
- Correct Eq. (3.7) factor is `nu^2*Nbar*r^2`, not `nu^2*Nbar*r/2`.
- Einstein-Hilbert self-actions: test `0996450`; implementation `f1b5cc3`.
- Primary PDF fixes the kinetic mixing factors as `a^2 k^2` and `b^2 k^2/Nbar^2`.
- Pure metric action is exchange-symmetric on proportional equal-Planck controls.
- Algebraic lapse/shift elimination: test `a9d1d8b`; implementation `7fcdd15`.
- `Phi1,Phi2,B1,B2` are eliminated directly from the action; their constraints are never differentiated into evolution equations.
- Post-auxiliary velocity Hessian has rank 1 on proportional controls over scans in H and k.
- Relative/common projection: test/interface `e573916`,`263f9c7`; implementation `35c1a14`.
- In `(Psi+,Psi-,E+,E-)`, only `E-=(E1-E2)/sqrt(2)` has a nonzero kinetic projection.
- One-field relative structural slice: RED test `9f5fd5e`; implementation `fcb240f`.
- `relative_e_slice_coefficients()` now exposes `L = K dot(E-)^2/2 + C E- dot(E-) + P E-^2/2` after auxiliary elimination. Its kinetic coefficient is constructed from the same reduced action and must equal the projected `E-` Hessian coefficient.
- This proportional pure-metric slice is only a structural/gauge control. Its gradient or mass is **not** Candidate-C physics until both matter sectors and their background terms are included.

### Direct Comelli route — closed negative result

- Candidate C recovers radiation speed `1/sqrt(3)` but gives a false gravity pair `c~0.0159` instead of `~0.8319`.
- Dust+dust fails identically; at large k the bad frequency tends to a constant, so the physical gravity `k^2 E` term is absent.
- Correctly making `B1` nondynamical still fails Case-C B.5.
- Ruled out: matter mixture, closure-row choice, isolated derivative errors, A1/A2 typo, A.18 swap inside old closure, f-trace sign flips, conditioning, selected minors, frozen-time PGCD, and eliminating `B1'` alone.

### A.3 / A.18

- Printed A.3/A.18 has `(calB1-calE)`; raw invariants give `(calB1-calE')` exactly.
- Finite-tau Bianchi checks select the derived-prime form. Printed-unprime is only a typo/control branch.

## Exact Case-C acceptance benchmark

`8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`.

- Exact branch: `a^4 xi^2 + xi - a - a^4/3 = 0`.
- `numerics/comelli_case_c.py` supplies exact background/conformal map.
- Required B.5: `E''+(3/tau)E'-(2/3)k^2E=0`.
- Equivalently with `E=tau^2e(x)`: `x^2e_xx+7xe_x+8e-(2/3)x^2e=0`.

## Test execution caveat

Container network cannot clone/download the GitHub repository, so newly added pytest files have not been executed as a repository suite. Core algebra, symmetry, auxiliary-stationarity, rank and projection checks were independently evaluated in scratch. Do not call the suite green until executable checkout becomes available.

## Active task list

- [x] Convention bridge / exact Candidate-C and Case-C backgrounds.
- [x] Audit and reject direct Comelli closure for Gate-2B physics.
- [x] Independent De Felice principal-action regression.
- [ ] **T1c — independently reconstruct and validate the scalar action.** IN PROGRESS.
  - [x] **T1c.6o.1 — Lagos action convention bridge.**
  - [x] **T1c.6o.2 — independent De Felice principal action.**
  - [x] **T1c.6o.3 — pure metric Lagos quadratic action:** interaction + EH + exchange-symmetry controls.
  - [x] **T1c.6o.4a — algebraically eliminate `Phi1,Phi2,B1,B2`.**
  - [x] **T1c.6o.4b — proportional-control kinetic rank = 1.**
  - [x] **T1c.6o.4c — explicit relative/common reduction:** only `E-` kinetic; one-field relative structural Lagrangian encoded.
  - [ ] **T1c.6o.5 — add two separately coupled matter sectors and derive the full high-k principal action.**
    - [ ] **6o.5a — transcribe a barotropic matter quadratic action for a fluid minimally coupled to one metric, in variables suited to algebraic lapse/shift elimination.**
    - [ ] **6o.5b — duplicate it independently for g and f sectors with the correct `a` vs `b,Nbar` normalization.**
    - [ ] **6o.5c — assemble metric + two-fluid quadratic action and integrate all nondynamical variables.**
    - [ ] **6o.5d — derive the principal kinetic/gradient matrix and recover three high-k speeds: g-fluid, f-fluid, gravity. Acceptance: gravity speed equals De Felice Eq. (86) without inserting Eq. (86) into the derivation.**
  - [ ] **T1c.6p — compare action-derived reduced constraints/gradient to Comelli and identify the lost interaction structure.**
  - [ ] **T1c.6q — Case-C acceptance:** recover B.5 exactly or an explicitly equivalent action-variable equation.
- [ ] **T2 — Candidate-C full scalar validation from the new action.**
- [ ] **T3 — replace faulty old scalar closure.**
- [ ] **T4 — implement native/action-based transfer solver.**
- [ ] **T5 — make `tests/test_comelli_native_scalar.py` green + >=3 extra `(z,k)` regressions.**
- [ ] **T6 — full Gate-2B regression suite.**
- [ ] **T7 — time-domain transfer RHS + fundamental matrix.**
- [ ] **T8 — continuous GR-connected/adiabatic mode tracking.**
- [ ] **T9 — compute `T_gg,T_gf,T_fg,T_ff` and relative-mode growth.**
- [ ] **T10 — Gate-2B verdict with tolerances/domain.**

## Current RED regression

`tests/test_comelli_native_scalar.py` remains intentionally RED until T1c is closed.

## Immediate restart instruction

**Resume at T1c.6o.5a — independent barotropic matter quadratic action.**

1. Do not return to the direct Comelli closure.
2. Start from a minimally coupled perfect-fluid / k-essence quadratic action whose sound speed is explicit and whose lapse/shift couplings are algebraic.
3. First validate a single-fluid GR control: after lapse/shift elimination the high-k matter scalar must propagate at its intrinsic `c_s` (`1/sqrt(3)` for radiation, zero intrinsic sound speed for dust).
4. Duplicate the construction for metric 2 with scale factor `b=a*r` and lapse `Nbar=r*c`; check the local speed becomes the expected lapse-rescaled f-sector matter speed.
5. Assemble both matter sectors with the already validated Lagos metric action, integrate nondynamical variables, and derive—not insert—the three high-k propagation eigenvalues.
6. Acceptance: the gravitational eigenvalue equals the independently implemented De Felice Eq. (86), while the two matter eigenvalues equal their intrinsic sector speeds.
7. Then apply the same reduced action to exact Case C and require B.5.
8. Update this checkpoint after every hard finding or completed subtask.
