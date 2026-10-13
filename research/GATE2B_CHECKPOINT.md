# Gate 2B — authoritative restart checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption. Update after every hard finding or task-state change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.** The De Felice/Hassan-Rosen two-matter reconstruction has the correct scalar degree count and matter kinetic invariants, but the helicity-0 invariant `NG3` is still wrong. Do not proceed to Candidate-C transfer integration.

## Closed hard facts

### Background / targets

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Candidate-C target at `a=0.5`: `c_s^2 ~= 0.69208`, `c_s ~= 0.83191`.
- Exact Case-C background is in `numerics/comelli_case_c.py`.
- Case-C asymptotic acceptance remains `E''+(3/tau)E'-(2/3)k^2E=0`.
- Independent De Felice principal action gives Case-C `c_s^2=-0.6665833419871022` at `a=0.05`.
- The four De Felice background equations (both Friedmann and both acceleration equations) close on this Case-C point at ~`1e-16` relative. The action is not being evaluated on an off-shell background.

### Historical Comelli closure — rejected

- Radiation branch is correct but the putative gravity branch has `c~0.0159` and finite high-k frequency, proving loss of the helicity-0 gradient.
- Unit conversion, matter mixture, row choice, individual derivative coefficients, simple sign/factor swaps, conditioning, selected minors and eliminating `B1'` alone were ruled out.

### De Felice action pieces

- `de_felice_matter_action.py` matches Eq. (54), including the spatial `-N^2(rho+P)k^2(q+aB/N)^2/(2a^2)` block.
- `de_felice_gravity_action.py` matches the scalar Fourier contractions of Eq. (44), including `B E_dot`, `Phi E`, `psi E`, and `k^6 E^2/18`.
- `hr_scalar_quadratic_action_density_de_felice()` directly implements the O(delta^2) HR interaction of Eqs. (45)-(46).
- Direct beta1 audits of the HR pure spatial/lapse Hessian and the `Gamma(H-h)^2` block pass.
- The Eq. (72) coefficient used in the basis transform is correct: in g-flat gauge `q_f=Y2 + [1/(n H_f)](Z+k^2Y3/6)`, and `1/(nH_f)=a/H_omega`.

### DF4 — degree count / BD basis CLOSED

- Eq. (72) basis `(Y1,Y2,Y3,Z_BD)` gives the correct null kinetic direction before BD removal.
- `Z_BD` is algebraically eliminable; three scalar kinetic directions remain.
- The first two physical kinetic invariants are correct. In particular, finite-k `NG2` reconstructed from the action matches De Felice Eq. (78) to roughly `1e-8 ... 1e-9` relative over `k=100...800`. Thus the fluid normalization and the main auxiliary denominator are not globally wrong.

### DF5 — published NG3 target

- `physical_squared_phase_speeds()` is independently validated on a synthetic three-mode action; generalized-QZ gives the same bad third branch. The extractor is not the cause.
- De Felice Eq. (77): `NG3 = det(K)/(K11*K22-K12^2)`.
- Exact finite-k Eq. (78), Case C at `a=0.05`:
  - `k=50`: `0.010901`;
  - `k=100`: `0.015890`;
  - `k=200`: `0.017943`;
  - `k=400`: `0.0185421788`;
  - `k=800`: `0.018698`;
  - asymptotic Eq. (80): `0.0187507871`.
- The target values were independently recomputed directly from De Felice `A,B,C`, not only from a repository helper.

## HR shift-volume bug — confirmed and fixed, but not sufficient

De Felice Eq. (45) contains
`-sqrt(-g) rhohat_g - sqrt(-f) rhohat_f + (1/2) N a^3 xi J Delta`.
Thus the HR shift Hessian has volume `B_g^2`, volume `B_f^2`, and relative-shift pieces.

The historical helper omitted the first two. A direct Case-C Hessian comparison at `a=0.05,k=400` found approximately `Q_BgBg=+0.3334` historically versus `Q_BgBg=-2.6668` from the complete Eq. (45)-(46) interaction.

- Commit `8637753`: add both missing volume-shift terms.
- Commit `181deda`: test requires the complete Eq. (45)-(46) shift Hessian.
- Using the f Friedmann equation, EH + matter + HR-volume contributions to `B_f^2` cancel exactly, leaving the relative-shift coefficient `Q_BfBf/k^2 = m^2 xi J c^2/(c+1)`. This independently confirms the fix.

## DF5e.3 — high-k Schur localization

With the corrected HR shift-volume terms, a scratch action reconstruction using the same uniform finite-difference step `h=2e-6` as the repository regression gives approximately:
- `k=100`: `NG3=0.10417`;
- `k=200`: `0.41666`;
- `k=400`: `1.66666`;
- `k=800`: `6.66664`.
So the first HR bug reduced the coefficient but did not remove `NG3~k^2`.

### Exact rate/auxiliary Schur result

Before the BD scalar is eliminated, transform the auxiliary-reduced rate block to Eq. (72). The `Y3=S` kinetic coefficient is already
`~0.10417,0.41667,1.66667,6.66667` for `k=100,200,400,800`.

For the f-sector alone, the relevant raw coefficients have been rederived independently from Eqs. (44), (45), (54):
- `K_EE = kappa xi^3 k^4/(6 n)`;
- `K_qq = n xi^3 (rho_f+P_f)/c_sf^2`;
- `R_(E,Bf) = -kappa xi^3 k^4/(3 alpha)`;
- `R_(q,Phi_f) = -n xi^3 (rho_f+P_f)/c_sf^2`;
- the full `(Phi_f,B_f)` Hessian agrees with the assembled action.

All three O(k^4) contributions to `K_Y3Y3` cancel almost exactly; the remainder is a clean O(k^2) term. Symbolic elimination on beta1 Case C gives

`K_Y3Y3 = a^2 c_sf^2 k^4 xi^2 (a^3+3) / [6 a^5 c c_sf^2 + 4 a^3(c+1)c_sf^2 k^2 xi + 18 a^2 c c_sf^2 - 9 a^2 c + 12(c+1)c_sf^2 k^2 xi]`,

hence

`K_Y3Y3 -> a^2 xi k^2/[4(c+1)]` as `k->infinity`.

On early Case C `c->2`, this is exactly `a^2 xi k^2/12 = k^2/96000` at `a=0.05`, explaining the observed `1.66667` at `k=400`.

### Important consistency checks

- In the GR one-metric limit (`m^2=0`, HR off) on an on-shell Friedmann background, the same symbolic f-sector Schur gives **exactly zero** for the metric scalar kinetic direction. Thus Eq. (44)+Eq. (54) preserve the expected GR gauge degeneracy.
- g-sector auxiliaries are negligible for this residual: eliminating only `(Phi_f,B_f)` reproduces the same `Y3` coefficient to ~`1e-8` at `k=400`.
- The error is not a finite-difference artifact: using the exactly quadratic HR helper and varying the Hessian step over many decades leaves the residual stable.
- Gauge-fixing g-flat before rather than after auxiliary elimination cannot alter this local f rate/auxiliary Schur at quadratic order; the relevant Hessian entries are evaluated at the background and do not depend on the removed g spatial perturbations.

## BD time-dependent canonicalization — quantified

The frozen `Y Zdot` integration-by-parts is incomplete in principle. Including the measure gives
`h_ZZ^eff = h_ZZ - (dot C_ZZ + 3 H C_ZZ)`.
At Case C `a=0.05,k=400`:
- raw `h_ZZ ~ 1.609e6`;
- `dot C_ZZ + 3H C_ZZ ~ 1.611e6`;
- `h_ZZ^eff ~ -2.15e3`.
This is a real large cancellation, but the resulting finite-k correction to the Y3 kinetic coefficient is only O(`5e-3`), far too small to remove `~1.65` at `k=400`.

To reproduce the exact Eq. (78) target at `k=400`, the effective algebraic BD coefficient would need to be about `+6.74175`, not `-2.15e3`.

A numerical clue (NOT YET A PROOF): this required value is very close to `A_DF/6 + m^2 xi J c^2/(c+1)`, where `A_DF` is De Felice Eq. (79). This points toward the **state/algebraic BD sector** rather than the already-audited rate/auxiliary coefficients.

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
  - [x] DF5e.1 — rule out EH block, matter block, finite-difference cancellation, `K^{-1}` conditioning, intrinsic fluid sound and simple BD Schur as root causes.
  - [x] DF5e.2 — direct NG3 RED + first exact HR bug (missing volume shifts) found/fixed.
  - [x] **DF5e.3a — rate/auxiliary Schur derived and spurious `a^2 xi k^2/[4(c+1)]` localized analytically.**
  - [x] **DF5e.3b — Eq. (72) normalization, background equations, NG2, GR degeneracy and f-sector prefactors audited.**
  - [ ] **DF5e.3e — audit the BD algebraic/state coefficient `h_ZZ^eff`. NEXT.**
    - [ ] decompose transformed `h_ZZ` into `Sigma^2`, `2A Sigma q_f`, `A^2 q_f^2`, auxiliary-Schur and time-dependent canonicalization pieces;
    - [ ] derive each piece from Eqs. (44), (45), (54) with the background field equation for `dot phi_f`;
    - [ ] identify the exact term responsible for the ~`2.16e3` discrepancy between reconstructed `h_ZZ^eff` and the O(1) coefficient required by Eq. (78);
    - [ ] compare the result to De Felice Eq. (79) quantities `A,B,C,D` and the clue `A/6 + m^2 xi J c^2/(c+1)` without fitting coefficients.
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

- `test_case_c_finite_k_ng3_matches_de_felice_eq78` remains RED until the BD algebraic sector is corrected.
- Case-C physical speed regression remains RED/untrusted.
- `tests/test_comelli_native_scalar.py` remains intentionally RED.

## Immediate restart instruction

**Resume at DF5e.3e — BD algebraic/state audit.**

1. Use the corrected HR code (`8637753`) and current exact Case-C background at `a=0.05`.
2. Start from the auxiliary-reduced 8x8 Hessian in old variables `(Sigma,S,q_g,q_f; rates)`.
3. Under Eq. (72), with `Z=Sigma` and `q_f=Y2+A(Z+C Y3)`, decompose the coefficient of `Z^2` before and after time-dependent integration by parts.
4. Separate the raw state contributions `Q_SigmaSigma`, `2A Q_Sigma,qf`, `A^2 Q_qf,qf`, plus the pieces induced by auxiliary Schur and by `dot C_ZZ+3H C_ZZ`.
5. Re-derive those entries from Eq. (44), Eq. (54), Eq. (45), including the background drift `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2`.
6. Find an exact paper mismatch before changing any coefficient. The required physical finite-k value at `k=400` corresponds to `h_ZZ^eff ~ +6.74175`; current reconstruction gives roughly `-2.15e3` after the time-dependent correction.
7. Update this checkpoint immediately after the first exact mismatch or after all state-sector entries are cleared.
8. Move to Candidate C only after Case-C NG3 and physical speeds are green.
