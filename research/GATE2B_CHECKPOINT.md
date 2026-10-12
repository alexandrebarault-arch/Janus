# Gate 2B — authoritative restart checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption. Update after every hard finding or task-state change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.** The full De Felice/Hassan-Rosen two-matter reconstruction reproduces the BD constraint, scalar degree count and Eq. (72) physical basis, but the current lapse/shift reduction gives the wrong high-k helicity-0 kinetic invariant. Do not proceed to Candidate-C transfer integration.

## Closed hard facts

### Background / targets

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Independent Candidate-C target at `a=0.5`: `c_s^2 ~= 0.69208`, `c_s ~= 0.83191`.
- Exact Case-C background is in `numerics/comelli_case_c.py`; asymptotic acceptance is `E''+(3/tau)E'-(2/3)k^2E=0`.
- Independent `de_felice_action_principal.py` gives finite-a Case-C `c_s^2=-0.6665833419871022` at `a=0.05`.

### Historical Comelli closure — rejected

- Radiation branch is correct but the putative gravity branch has `c~0.0159` and finite high-k frequency, proving loss of the helicity-0 gradient.
- Unit conversion, matter mixture, row choice, individual derivative coefficients, simple sign/factor swaps, conditioning, selected minors and eliminating `B1'` alone were ruled out.

### De Felice action pieces — individually audited

- `de_felice_matter_action.py` matches Eq. (54), including the spatial `-N^2(rho+P)k^2(q+aB/N)^2/(2a^2)` block.
- `de_felice_gravity_action.py` matches the scalar Fourier contractions of Eq. (44), including `B E_dot`, `Phi E`, `psi E`, and the `k^6 E^2/18` term.
- `hr_scalar_potential.py` uses the De Felice sign of the HR potential and the analytic relative-shift block from Eqs. (45)-(46).
- A direct beta1-only Case-C audit of the HR pure-`E_f^2` Hessian reproduces the analytic `xi k^4/6` coefficient to better than `1e-6` relative with an appropriately scaled perturbation step. The separate `Gamma(H-h)^2` spatial block is therefore present.
- Multiplying only the HR relative-shift coefficient over factors `1/8 ... 8` changes amplitudes but never removes the bad `k^2` scaling of the reconstructed kinetic invariant; no single missing shift multiplier is the fix.

### DF4 — degree count / BD basis CLOSED, but not sufficient for principal dynamics

- Eq. (72) basis `(Y1,Y2,Y3,Z_BD)` is implemented and gives the correct null kinetic direction before BD removal.
- `Z_BD` is algebraically eliminable; three scalar kinetic directions remain.
- The old frozen integration-by-parts of linear `Y*Zdot` terms is not a valid standalone derivation of the full high-k equations because Eq. (84) retains time derivatives of the coefficient matrices. However, restoring those derivative/measure terms does **not** repair the bad kinetic scaling described below, so this is not the root cause of `N_G^(3)`.

### DF5 — decisive kinetic-invariant failure

- `physical_squared_phase_speeds()` is independently validated on a synthetic three-mode action; a normalized generalized-QZ calculation gives the same bad Case-C third branch as the original `K^{-1}` extractor. The failure is not caused by ill-conditioned inversion of `K`.
- The published kinetic invariant is
  `NG3 = det(K)/(K11*K22-K12^2)` (De Felice Eq. 77), with exact finite-k Eq. (78) and high-k Eq. (80):
  `NG3 -> (3/8) m^2 a^4 xi J B`.
- On Case C at `a=0.05`, the independent exact Eq. (78) gives approximately:
  - `k=50`: `0.010901`;
  - `k=100`: `0.015890`;
  - `k=200`: `0.017943`;
  - `k=400`: `0.018542`;
  - `k=800`: `0.018698`;
  - asymptotic Eq. (80): `0.0187507871`.
  Thus `k=400` is already ~98.9% asymptotic.
- The reconstructed physical kinetic matrix instead gives, in the paper variable `Y3=S`:
  - `k=50`: `~0.06510`;
  - `k=100`: `~0.26041`;
  - `k=200`: `~1.04162`;
  - `k=400`: `~4.16620`;
  - `k=800`: `~16.6607`;
  - `k=1200`: `~37.47`;
  - `k=2000`: `~103.94`.
  Therefore reconstructed `NG3 ~ k^2` instead of approaching a constant.
- This scaling is stable over more than two decades of finite-difference step when variables are perturbatively rescaled (`k^2 E`, `kB`, etc. kept small). It is not cancellation noise.
- The wrong `k^2` kinetic term is already present **before BD Schur elimination**. At `k=400`, raw `K33(Y3dot^2) ~ 4.16624`, while the BD correction is only `~2.8e-5`; final `K33 ~4.16621`.
- Varying the f-fluid intrinsic sound speed from `c_sf^2=0.001` to `1` leaves reconstructed `NG3` essentially unchanged (`~4.166589` at `k=400`). This mirrors the published independence of `NG3` from `c_sf` and rules out the f-fluid sound-speed block as the cause.
- The auxiliary Hessian entries themselves have the expected large-k coefficients. Example on Case C: after dividing the shift block by `k^2`, `Q_BB ~ [[0.16667287,-0.03333540],[-0.03333540,0.16668522]]`; decomposition into EH + matter + HR reproduces the first entry, so the apparent `B_g^2` excess was not an error.
- **Localization:** the error is introduced at or before the Schur elimination of the four auxiliaries `(Phi_g,Phi_f,B_g,B_f)`, specifically through some cross-coupling needed for the high-k cancellation. It is not introduced by the later BD Schur, speed extraction, or the intrinsic fluid sounds.

## Current root-cause priority

The most promising unresolved possibility is **an incorrect HR lapse/spatial cross coupling**, not a pure `E^2` or pure shift term. Eq. (46) contains couplings such as `(Phi-ctilde*varphi)(Tr H-Tr h)` and related trace/traceless combinations. Such cross terms directly control the lapse/shift constraints and can spoil `NG3` while leaving isolated `E^2` and `B^2` audits green.

## Active task list

- [x] Convention bridge / Candidate-C / exact Case-C backgrounds.
- [x] Reject historical Comelli closure for Gate-2B physics.
- [x] Independent De Felice high-k gravity target.
- [x] De Felice Eq. (54) matter action.
- [x] EH scalar Eq. (44) direct audit.
- [x] HR pure spatial and relative-shift audits.
- [x] DF3 degree count exactly 3.
- [x] DF4 Eq. (72) basis + BD algebraic degree removal.
- [ ] **DF5 — recover the three physical high-k speeds. BLOCKED.**
  - [x] DF5a — physical mode extractor + synthetic validation.
  - [x] DF5c — integrated Case-C speed regression: FAIL.
  - [x] DF5e.1 — rule out simple missing `Gamma(H-h)^2`, relative-shift multiplier, EH scalar block, matter Eq. (54), finite-difference cancellation, `K^{-1}` conditioning, and BD Schur as root causes.
  - [ ] **DF5e.2 — add a direct `NG3` RED regression against De Felice Eq. (78), then audit the full HR lapse/spatial cross-Hessian term-by-term before auxiliary elimination.** NEXT.
  - [ ] DF5e.3 — derive/compare the high-k auxiliary Schur analytically and identify the exact cross entry that prevents the Eq. (78) cancellation.
  - [ ] DF5e.4 — only after root cause is identified, implement one minimal physical fix and make the `NG3` regression green.
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

- Case-C physical speed regression remains RED.
- `tests/test_comelli_native_scalar.py` remains RED.
- Next add a more local `NG3` RED test; do not tune its target.

## Immediate restart instruction

**Resume at DF5e.2.**

1. Add a helper/test computing `NG3 = det(K)/(K11*K22-K12^2)` from the reconstructed 3x3 kinetic matrix.
2. At exact Case C `a=0.05,k=400`, compare it to independent De Felice Eq. (78), approximately `0.018542` (not merely the asymptotic limit).
3. Keep the failing reconstructed value visible in the assertion/debug output; expected current value is about `4.166`.
4. Then derive the complete HR scalar quadratic cross-Hessian in g-flat gauge from Eqs. (45)-(46), especially lapse/trace terms, and compare entry-by-entry with `hr_scalar_potential.py` **before** any auxiliary Schur.
5. Do not modify physical coefficients until one exact mismatched Hessian entry is identified.
6. Update this checkpoint immediately after that first exact mismatch or after all HR cross entries are cleared.
