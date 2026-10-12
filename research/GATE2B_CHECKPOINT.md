# Gate 2B — authoritative restart checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption. Update after every hard finding or task-state change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.** The full De Felice/Hassan-Rosen two-matter action reconstruction correctly reproduces the Boulware–Deser constraint, the scalar degree count, and the Eq. (72) physical-variable basis, but its current reduced physical action still fails the decisive high-k helicity-0 propagation test. Do not proceed to Candidate-C transfer integration yet.

## Closed hard facts

### Background / conventions

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Independent De Felice high-k gravity target on Candidate C at `a=0.5`: `c_s^2 ~= 0.69208`, `c_s ~= 0.83191`.
- Exact Case-C background lives in `numerics/comelli_case_c.py`; asymptotic acceptance remains `E''+(3/tau)E'-(2/3)k^2E=0`.
- Independent `de_felice_action_principal.py` gives the finite-a Case-C gravity target `c_s^2=-0.6665833419871022` at `a=0.05`.

### Historical Comelli closure — rejected for physics

- It recovers visible radiation propagation but replaces the physical gravity pair by `c~0.0159`.
- Dust+dust gives the same failure; the false frequency tends to a constant at high k, proving the helicity-0 `k^2 E` term was projected out.
- Unit conversion, matter mixture, closure-row choice, simple coefficient/sign swaps, conditioning, selected minors and merely eliminating `B1'` were ruled out.

### Lagos route — retained only as audit reference

- Lagos 1610.00553 specializes its final quadratic action to matter coupled to metric 1 and uses those background equations.
- Adding an independent second Eq. (54) matter block to that specialized action produces a spurious fourth kinetic direction linear in `rho_f`.
- Therefore Lagos is useful for convention/cross-check work, but **must not be used as the final two-matter scalar action**.
- Spatial derivative audits L1-L4 are complete (`252a4dd`, `11c9b5a`, `af6b315`, `68e1c17`).
- Lagos -> De Felice lapse convention is `Phi_DF=Phi_L/2`; TDD RED/GREEN `53c9af3` / `2ee436d`.

## Validated De Felice two-matter action reconstruction

### Matter

- `numerics/de_felice_matter_action.py` implements De Felice Eq. (54) for one P(X) sector.
- Metric-off action reproduces the intrinsic matter sound speed.
- Both matter sectors are added independently, each with its own metric/lapse/scale factor.

### Einstein-Hilbert

- `numerics/de_felice_gravity_action.py` directly specializes De Felice Eq. (44) to flat scalar Fourier modes.
- TDD scaffold: RED `bb86701`, initial GREEN `85b008c`.
- A direct contraction audit found three Fourier-sign mistakes: `B E_dot`, `Phi E`, `psi E`. RED `a7d41b3`, fix `256cefd`.

### Hassan-Rosen interaction

- `numerics/hr_scalar_potential.py` contains an exact local standard-beta matrix potential and a perturbative De Felice helper.
- Exact diagonal standard-beta potential matches the independent diagonal implementation at machine precision (`35fcfdb` -> `cfa9e5c`).
- The Fourier relative-shift block is inserted analytically from De Felice Eqs. (45)-(46): `+(m^2 M_g^2/2) N a^3 xi J/(ctilde+1) k^2 (B_g-ctilde B_f)^2`.
- De Felice-sign correction of the standard-beta potential: RED `3f345e7`, fix `9851c3d`.

### DF4 — physical basis and BD removal CLOSED

- Eq. (72) basis transform is implemented as `(Y1,Y2,Y3,Z_BD)` with `Z_BD=Sigma`.
- `Z_BD_dot` has no quadratic kinetic direction on exact Case C.
- `Z_BD` is algebraically eliminated, leaving a 6x6 quadratic Hessian for `(Y1,Y2,Y3,Y1dot,Y2dot,Y3dot)` and a positive 3x3 kinetic matrix on Case-C control points.
- TDD/implementation trail: `9145fe1`, `c7db4d1`, `e1c7ea5`, `2fc77e0`.

### DF5 — physical high-k dispersion: CURRENT FAILURE

- RED Case-C regression `bb43d94`; speed extractor added `3dc45ce`; exact synthetic 3-mode regression committed `18d1fec`.
- `physical_squared_phase_speeds()` is independently validated: on a synthetic quadratic action it recovers `(-2/3,1/3,0.4)` to about `1e-16`.
- The Case-C regression now compares against independent `gravity_principal_action()` rather than forcing the strict asymptotic `-2/3`; commit `0f849c9`.
- A uniform high-k finite-difference step can leave the perturbative metric domain because `k^2 E_f` is the actual small combination. The test step was reduced in `8395e21` so a RED result reflects dispersion rather than a square-root domain failure.
- A focused mini-package was reconstructed and DF5c was executed locally. Uniform small-step runs already showed the wrong third branch. A dimensionally scaled Hessian was then used as a diagnostic, with steps chosen so `k^2 E`, `kB`, velocities and rate variables remain perturbatively small.
- With that scaled diagnostic the two matter branches move toward their expected limits, while the third branch is stable but behaves as a finite-frequency mode:
  - `k=200`: approximately `(0.2633, 0.3315, 487.23)`;
  - `k=400`: approximately `(0.3158, 0.3690, 123.78)`;
  - `k=800`: approximately `(0.3290, 0.3782, 31.09)`;
  - `k=1200`: approximately `(0.3314, 0.3796, 13.84)`.
- The product `k^2 * c_s^2` of the third branch is approximately constant, so its apparent `c_s^2` scales like `1/k^2`. This is a massive/finite-frequency mode, **not** the required helicity-0 gradient branch.
- Therefore DF5c is a genuine structural failure, not a unit-conversion error, speed-extractor bug, or ordinary floating-point-conditioning effect.
- **Do not mark DF5 green and do not advance to Candidate C.** The action/reduction must be re-audited to locate the missing principal spatial contribution.

## Leading suspects for DF5 root cause

1. The frozen-coefficient canonicalization of linear `Y*Z_BD_dot` terms may be invalid for the high-k principal reduction because the Eq. (72) basis contains explicit `k^2` factors. Time derivatives of the transformation/coefficient may therefore survive at principal order instead of being a lower-order mass correction.
2. The perturbative Hassan-Rosen block may not reproduce every scalar spatial term of De Felice Eqs. (45)-(46), especially the `Gamma (H-h)^2` tensor/spatial contribution, even though its diagonal potential and relative-shift pieces pass separate audits.
3. Less likely but still open: one scalar spatial contraction in the Eq. (44) EH specialization is incomplete despite previous sign audits.

## Active task list

- [x] Convention bridge / Candidate-C / exact Case-C backgrounds.
- [x] Reject historical Comelli closure for Gate-2B physics.
- [x] Independent De Felice high-k gravity target.
- [x] De Felice Eq. (54) one-sector P(X) matter action.
- [x] Lagos audits and proof that the Lagos+two-matter hybrid is invalid.
- [ ] **T1c-DF — full De Felice two-matter scalar action.** ACTIVE.
  - [x] **DF1** — transcribe/audit both gravitational EH sectors.
  - [x] **DF2** — combine two P(X) sectors + HR interaction; lapse/shift auxiliaries algebraic.
  - [x] **DF3** — kinetic degree count exactly 3 on Case C.
  - [x] **DF4** — Eq. (72) basis + BD algebraic elimination.
  - [ ] **DF5 — recover the three physical high-k speeds. BLOCKED BY STRUCTURAL FAILURE.**
    - [x] DF5a — frozen Euler-Lagrange speed extractor.
    - [x] DF5b — synthetic exactly-solvable validation.
    - [x] **DF5c — execute integrated Case-C regression: FAIL.** Helicity-0 branch scales as `1/k^2` instead of approaching independent De Felice `c_s^2`.
    - [ ] **DF5e — root-cause audit of the missing principal spatial term.** NEXT.
      - [ ] DF5e.1 — audit De Felice Eq. (45)-(46) scalar spatial/tensor block against `hr_scalar_potential.py` term-by-term;
      - [ ] DF5e.2 — test DF4 without frozen integration-by-parts of `Z_BD_dot`, retaining the full descriptor/DAE including the time-dependent Eq. (72) transform;
      - [ ] DF5e.3 — isolate EH+HR pure-gravity principal block from matter and compare directly to independent De Felice `NG3`/gradient coefficients;
      - [ ] DF5e.4 — only after root cause is identified, add a RED regression and implement one minimal fix.
    - [ ] DF5d — Candidate-C gravity regression only after Case C is green.
  - [ ] **DF6** — Case-C acceptance: recover B.5 or equivalent reduced action/equation.
- [ ] **T2** — Candidate-C validation at >=3 `(z,k)` points.
- [ ] **T3** — identify exactly what the old Comelli 12x12 closure projected out.
- [ ] **T4** — native/action-based transfer solver.
- [ ] **T5** — make `tests/test_comelli_native_scalar.py` green + >=3 regressions.
- [ ] **T6** — full Gate-2B regression suite.
- [ ] **T7** — time-domain fundamental transfer matrix.
- [ ] **T8** — continuous GR-connected/adiabatic mode tracking.
- [ ] **T9** — compute `T_gg,T_gf,T_fg,T_ff` and relative growth.
- [ ] **T10** — Gate-2B scientific verdict.

## Test caveat

The full repository still cannot be cloned from the container. Focused local mini-package reproduction is valid evidence for DF5c, but do not claim the entire pytest suite is green.

## Current intentional RED

- `tests/test_de_felice_two_matter_action.py::test_case_c_high_k_physical_action_recovers_three_scalar_speed_branches` is intentionally RED until DF5e finds and repairs the missing principal gradient.
- `tests/test_comelli_native_scalar.py` remains intentionally RED until DF5/DF6 are closed.

## Immediate restart instruction

**Resume at DF5e.1.**

1. Re-open De Felice arXiv:1404.0008 Eqs. (44)-(46) from the primary PDF and audit every scalar spatial term against `de_felice_gravity_action.py` and `hr_scalar_potential.py`.
2. In particular verify the full `Gamma (H-h)^2` term of Eq. (45)-(46); do not assume the exact diagonal beta potential plus shift block reproduces it automatically.
3. Separately test whether `_canonicalize_linear_zdot_frozen` changes the high-k principal symbol when the `k^2`-dependent Eq. (72) transform is time dependent.
4. Do not tune physical coefficients or the target. The independent finite-a Case-C target is `c_s^2=-0.6665833419871022` at `a=0.05`.
5. Update this checkpoint immediately after the first hard ruling, then continue to the next DF5e subtask.
