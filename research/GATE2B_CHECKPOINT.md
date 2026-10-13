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
- Restoring time-derivative/measure terms omitted by frozen integration-by-parts does not repair the bad `N_G^(3)` scaling, so this is not the root cause.

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
- Before the HR shift-volume fix the reconstructed value at `k=400` was about `4.166`, with `NG3 ~ k^2`.
- The bad term is already present before BD Schur elimination. BD removal, intrinsic f-fluid sound speed, finite-difference noise and kinetic-matrix inversion are not the cause.

## HR shift-volume bug — confirmed and fixed, but not sufficient

De Felice Eq. (45) contains
`-sqrt(-g) rhohat_g - sqrt(-f) rhohat_f + (1/2) N a^3 xi J Delta`.
Thus the HR shift Hessian has volume `B_g^2`, volume `B_f^2`, and relative-shift pieces.

The historical helper omitted the first two. A direct Case-C Hessian comparison at `a=0.05,k=400` found approximately `Q_BgBg=+0.3334` historically versus `Q_BgBg=-2.6668` from the complete Eq. (45)-(46) interaction.

- Commit `8637753`: add both missing volume-shift terms.
- Commit `181deda`: test requires the complete Eq. (45)-(46) shift Hessian.

### Post-fix scratch regression

A scratch reconstruction using the same **uniform finite-difference step `h=2e-6`** as the repository RED test reproduces the old failure closely (`NG3~4.15` at `k=400`, versus repo history ~`4.166`), so it is a useful diagnostic replica.

With the shift-volume fix the same scratch gives approximately:
- `k=100`: `NG3=0.10417`;
- `k=200`: `NG3=0.41666`;
- `k=400`: `NG3=1.66666`;
- `k=800`: `NG3=6.66664`.

Therefore the first exact HR bug is dynamically active but **does not fix the root problem**: reconstructed `NG3` still scales as `k^2`, with a smaller coefficient. The exact repository test has not been executed through CI/actions; do not claim it green.

This moves the root-cause search from isolated HR shift coefficients to the **high-k auxiliary Schur structure / variable normalization / sector prefactors**.

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
  - [x] DF5c — integrated Case-C speed regression: FAIL.
  - [x] DF5e.1 — rule out EH block, matter block, finite-difference cancellation, `K^{-1}` conditioning, BD Schur and intrinsic fluid sound as root causes.
  - [x] DF5e.2a — direct NG3 RED regression exists; target at `a=0.05,k=400` is `0.0185421788`.
  - [x] DF5e.2b — first exact HR mismatch found and fixed: missing volume `B_g^2/B_f^2` terms.
  - [x] **DF5e.2c — post-fix scratch rerun: NG3 still scales as `k^2`; fix insufficient.**
  - [ ] **DF5e.3 — derive the high-k auxiliary Schur analytically. NEXT.**
    - [ ] DF5e.3a — extract raw kinetic block `K0`, auxiliary Hessian `A`, and rate-auxiliary cross block `R` before BD transform, with `K_red = K0 - R A^{-1} R^T`.
    - [ ] DF5e.3b — track leading powers of k for the Y3=S rate direction through Eq. (72); identify which cancellation leaves the spurious `O(k^2)` NG3.
    - [ ] DF5e.3c — audit Eq. (72) normalization/signs and f-sector EH/matter prefactors against the primary definitions; do not change coefficients without an exact mismatch.
    - [ ] DF5e.3d — compare remaining HR lapse/trace cross-Hessian entries only if Schur localization points there.
  - [ ] DF5e.4 — make Eq. (78) NG3 green at several k values.
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

- `test_case_c_finite_k_ng3_matches_de_felice_eq78` remains expected RED until DF5e.3 is closed.
- Case-C physical speed regression remains RED/untrusted.
- `tests/test_comelli_native_scalar.py` remains intentionally RED.

## Immediate restart instruction

**Resume at DF5e.3a — high-k auxiliary Schur.**

1. Use the corrected HR shift-volume code (`8637753`) and complete shift regression (`181deda`).
2. At exact Case C `a=0.05`, build the full 12x12 quadratic Hessian and partition it before auxiliary elimination into dynamic/rate block and auxiliaries `(Phi_g,Phi_f,B_g,B_f)`.
3. For the rate block, write the Schur correction explicitly: `K_red = K0 - R A^{-1} R^T`, where `R` is rate-to-auxiliary coupling.
4. Transform the rate directions with Eq. (72) and isolate the Y3=S kinetic invariant before BD removal.
5. Evaluate leading k powers at `k=(100,200,400,800)`; determine which exact entry prevents cancellation of the `O(k^2)` term.
6. Audit Eq. (72) normalization/signs and f-sector prefactors against the primary paper before altering any coefficient.
7. Update this checkpoint immediately after the first exact Schur mismatch/localization.
8. Move to Candidate C only after Case-C NG3 and physical speeds are green.
