# Gate 2B — authoritative restart checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption. Update after every hard finding or task-state change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.** The De Felice/Hassan-Rosen two-matter reconstruction has the correct scalar degree count and BD basis, but the reconstructed helicity-0 kinetic invariant is still wrong. Do not proceed to Candidate-C transfer integration.

## Closed hard facts

### Background / targets

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Candidate-C target at `a=0.5`: `c_s^2 ~= 0.69208`, `c_s ~= 0.83191`.
- Exact Case-C background is in `numerics/comelli_case_c.py`.
- Case-C asymptotic acceptance remains `E''+(3/tau)E'-(2/3)k^2E=0`.
- Independent De Felice principal action gives Case-C `c_s^2=-0.6665833419871022` at `a=0.05`.

### Historical Comelli closure — rejected

- Radiation branch is correct but the putative gravity branch has `c~0.0159` and finite high-k frequency, proving loss of the helicity-0 gradient.
- Unit conversion, matter mixture, row choice, individual derivative coefficients, simple sign/factor swaps, conditioning, selected minors and eliminating `B1'` alone were ruled out.

### De Felice action pieces

- `de_felice_matter_action.py` matches Eq. (54), including the spatial `-N^2(rho+P)k^2(q+aB/N)^2/(2a^2)` block.
- `de_felice_gravity_action.py` matches the scalar Fourier contractions of Eq. (44), including `B E_dot`, `Phi E`, `psi E`, and `k^6 E^2/18`.
- `hr_scalar_quadratic_action_density_de_felice()` directly implements the O(delta^2) HR interaction of Eqs. (45)-(46).
- Direct beta1 audits of the HR pure spatial/lapse Hessian and the `Gamma(H-h)^2` block pass.

### DF4 — degree count / BD basis CLOSED

- Eq. (72) basis `(Y1,Y2,Y3,Z_BD)` gives the correct null kinetic direction before BD removal.
- `Z_BD` is algebraically eliminable; three scalar kinetic directions remain.
- Restoring time-derivative/measure terms omitted by the frozen integration-by-parts does not repair the bad `N_G^(3)` scaling, so this is not the root cause.

### DF5 — kinetic invariant failure

- `physical_squared_phase_speeds()` is independently validated on a synthetic three-mode action; generalized-QZ gives the same bad third branch. The extractor is not the cause.
- De Felice Eq. (77): `NG3 = det(K)/(K11*K22-K12^2)`.
- Exact finite-k Eq. (78), Case C at `a=0.05`:
  - `k=50`: `0.010901`;
  - `k=100`: `0.015890`;
  - `k=200`: `0.017943`;
  - `k=400`: `0.0185421788`;
  - `k=800`: `0.018698`;
  - asymptotic Eq. (80): `0.0187507871`.
- Old reconstructed value at `k=400` was about `4.166`, with reconstructed `NG3 ~ k^2` instead of approaching a constant.
- The bad term is already present before BD Schur elimination. BD removal, intrinsic f-fluid sound speed, finite-difference noise and kinetic-matrix inversion are not the cause.

## NEW hard finding — HR shift-volume bug

De Felice Eq. (45) contains

`-sqrt(-g) rhohat_g - sqrt(-f) rhohat_f + (1/2) N a^3 xi J Delta`

at quadratic order. Therefore the HR auxiliary shift Hessian contains **three** pieces:

1. `-sqrt(-g) rhohat_g` contributes a `B_g^2` term;
2. `-sqrt(-f) rhohat_f` contributes a `B_f^2` term;
3. `Delta` contributes the familiar relative-shift square `(B_g-ctilde B_f)^2/(ctilde+1)`.

The historical helper `hr_scalar_quadratic_potential_density_de_felice()` previously set `B_g=B_f=0` inside the exact determinant pieces and then added only item 3. Thus items 1 and 2 were missing from the action used in `de_felice_two_matter_action.py`.

A direct Hessian comparison at Case C `a=0.05,k=400` found a large exact mismatch in the HR shift block. In particular, the historical helper gave approximately `Q_BgBg=+0.3334` for the HR contribution where the complete Eq. (45)-(46) expression gives approximately `Q_BgBg=-2.6668` (same local normalization), an error of about `3.0002` before the auxiliary Schur.

This is the **first exact mismatched Hessian entry** found in DF5e.2.

### Implemented fix

- Commit `8637753`: `hr_scalar_quadratic_potential_density_de_felice()` now adds both volume shift terms plus the relative-shift term.
- Commit `181deda`: `tests/test_hr_scalar_potential.py` now requires the complete Eq. (45)-(46) shift Hessian, not only the rank-one relative-shift square.
- The `B=0` diagonal convention test remains unchanged.
- A scratch reconstruction shows this correction strongly changes the bad gravity kinetic invariant, proving the mismatch is dynamically active. Scratch normalization is not identical to the repository finite-difference path, so **do not declare NG3 green until the repository regression is rerun exactly**.

## Active task list

- [x] Convention bridge / Candidate-C / exact Case-C backgrounds.
- [x] Reject historical Comelli closure for Gate-2B physics.
- [x] Independent De Felice high-k gravity target.
- [x] De Felice Eq. (54) matter action.
- [x] EH scalar Eq. (44) direct audit.
- [x] DF3 degree count exactly 3.
- [x] DF4 Eq. (72) basis + BD algebraic degree removal.
- [ ] **DF5 — recover the three physical high-k speeds. BLOCKED.**
  - [x] DF5a — physical mode extractor + synthetic validation.
  - [x] DF5c — integrated Case-C speed regression: FAIL before latest fix.
  - [x] DF5e.1 — rule out EH block, matter block, finite-difference cancellation, `K^{-1}` conditioning, BD Schur and intrinsic fluid sound as root causes.
  - [x] **DF5e.2a — direct NG3 RED regression exists in `tests/test_de_felice_two_matter_action.py`.** Target at `a=0.05,k=400` is `0.0185421788`.
  - [x] **DF5e.2b — first exact HR auxiliary mismatch found: missing volume `B_g^2/B_f^2` terms. Minimal fix committed.**
  - [ ] **DF5e.2c — rerun the exact repository NG3 regression after commits `8637753` + `181deda`; record the new measured value and k-scaling. NEXT.**
  - [ ] **DF5e.3 — if NG3 remains red, audit remaining HR auxiliary cross-Hessian entries term-by-term, especially `(Phi-ctilde varphi)(TrH-Trh)` and their coupling to `E_f/psi_f`; then derive the high-k auxiliary Schur analytically.**
  - [ ] DF5e.4 — only after every exact mismatch is identified, make NG3 Eq. (78) green over several k values.
  - [ ] DF5d — Candidate-C gravity regression only after Case C is green.
- [ ] DF6 — recover B.5/equivalent reduced action on Case C.
- [ ] T2 — Candidate-C validation at >=3 `(z,k)` points.
- [ ] T3 — identify exactly what old Comelli closure projected out.
- [ ] T4 — native/action-based transfer solver.
- [ ] T5 — green `tests/test_comelli_native_scalar.py` + >=3 regressions.
- [ ] T6 — full Gate-2B regression suite.
- [ ] T7 — time-domain fundamental transfer matrix.
- [ ] T8 — continuous GR-connected/adiabatic mode tracking.
- [ ] T9 — compute `T_gg,T_gf,T_fg,T_ff` and relative growth.
- [ ] T10 — Gate-2B scientific verdict.

## Current intentional RED

- `test_case_c_finite_k_ng3_matches_de_felice_eq78` was RED before the latest HR shift-volume fix and must now be rerun.
- Case-C physical speed regression remains untrusted until NG3 is green.
- `tests/test_comelli_native_scalar.py` remains intentionally RED.

## Immediate restart instruction

**Resume at DF5e.2c.**

1. Run `test_case_c_finite_k_ng3_matches_de_felice_eq78` on the exact branch state containing commits `8637753` and `181deda`.
2. Record measured NG3 at `a=0.05,k=400` versus target `0.0185421788`.
3. Scan at least `k=(100,200,400,800)` to determine whether the reconstructed invariant now approaches a constant or still scales as a power of k.
4. If still red, compare every remaining HR cross-Hessian entry from `hr_scalar_quadratic_action_density_de_felice()` against the helper used by the assembled action, especially lapse/trace entries involving `Phi_g`, `Phi_f`, `psi_f`, `E_f`.
5. Do not change any physical coefficient without an exact Hessian mismatch.
6. Update this checkpoint immediately after the NG3 rerun and after every further exact mismatch.
7. Move to Candidate C only after Case-C NG3 and physical speeds are green.
