# Gate 2B — authoritative restart checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption. Update after every hard finding or task-state change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.** The De Felice/Hassan-Rosen two-matter reconstruction has the correct scalar degree count and matter kinetic invariants. The former O(1e3) BD algebraic discrepancy is now explained: the Case-C time derivative of `C_ZZ` froze `P_f=0` despite finite diagnostic `c_sf^2`, omitting the k-essence pressure drift. The production reducer still uses frozen-coefficient BD canonicalization, so `NG3` is not yet green. Do not proceed to Candidate-C transfer integration.

## Closed hard facts

### Background / targets

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Candidate-C target at `a=0.5`: `c_s^2 ~= 0.69208`, `c_s ~= 0.83191`.
- Exact Case-C background is in `numerics/comelli_case_c.py`.
- Case-C asymptotic acceptance remains `E''+(3/tau)E'-(2/3)k^2E=0`.
- Independent De Felice principal action gives Case-C `c_s^2=-0.6665833419871022` at `a=0.05`.
- The four De Felice background equations (both Friedmann and both acceleration equations) close on this Case-C point at ~`1e-16` relative. The action is not being evaluated on an off-shell metric background.

### Historical Comelli closure — rejected

- Radiation branch is correct but the putative gravity branch has `c~0.0159` and finite high-k frequency, proving loss of the helicity-0 gradient.
- Unit conversion, matter mixture, row choice, individual derivative coefficients, simple sign/factor swaps, conditioning, selected minors and eliminating `B1'` alone were ruled out.

### De Felice action pieces

- `de_felice_matter_action.py` matches Eq. (54), including the spatial `-N^2(rho+P)k^2(q+aB/N)^2/(2a^2)` block.
- `de_felice_gravity_action.py` matches the scalar Fourier contractions of Eq. (44), including `B E_dot`, `Phi E`, `psi E`, and `k^6 E^2/18`.
- `hr_scalar_quadratic_action_density_de_felice()` directly implements the O(delta^2) HR interaction of Eqs. (45)-(46).
- Direct beta1 audits of the HR pure spatial/lapse Hessian and the `Gamma(H-h)^2` block pass.
- The Eq. (72) coefficient used in the basis transform is correct: in g-flat gauge `q_f=Y2 + [1/(n H_f)](Z+k^2Y3/6)`, and `1/(nH_f)=a/H_omega`.
- The f k-essence background drift is also correct and must be retained: `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2`, directly from De Felice Eq. (18).

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

## DF5e.3e — BD algebraic/state audit CLOSED

The raw Eq. (72) BD coefficient and `C_ZZ=H[Z,Zdot]` were decomposed independently. The apparent time-corrected result `h_ZZ^eff ~ -2.15e3` was traced to a derivative-path inconsistency, not to Eqs. (44), (45) or (54).

The audit differentiated `C_ZZ(a)` between exact Case-C points while setting `P_f=0` at every neighboring point and simultaneously keeping the diagnostic `c_sf^2=0.1`. For a barotropic k-essence field De Felice Eq. (10) gives `c_s^2=dP/d rho` along the background, and Eq. (18) gives

`dot P_f = c_sf^2 dot rho_f = -3 n H_f c_sf^2 (rho_f+P_f)`.

At `a=0.05,k=400,c_sf^2=0.1`, an independent exact-quadratic scratch audit finds approximately:
- pressure-frozen `h_ZZ^eff = -2153.48`;
- `partial C_ZZ/partial P_f = 4.6882748e-8`;
- `dot P_f = -4.60771344e10`;
- missing `dot C_ZZ` contribution `= -2160.22`;
- pressure-consistent `h_ZZ^eff = +6.7421`.

The value of `h_ZZ^eff` required by the transformed kinetic Schur complement to reproduce Eq. (78) is about `+6.7417` at the same point. The Eq. (79) clue evaluates to

`A_DF/6 + m^2 xi J c^2/(c+1) = 6.741811...`.

Thus the entire O(1e3) discrepancy is accounted for by the omitted pressure-chain-rule contribution. A sound-speed scan confirms the diagnosis: pressure-frozen `h_ZZ^eff` acquires an artificial nearly linear `c_sf^2` term, while adding `dot P_f` leaves the corrected value O(1) and essentially sound-speed independent at the control point.

**Do not remove the `-3 n H_f c_sf^2` term from `dot(phi_f)/phi_f`: it is required by Eq. (18). Do not tune any EH, matter or HR coefficient.**

The remaining production defect is structural: `_canonicalize_linear_zdot_frozen()` intentionally drops `dot C_ZZ+3H C_ZZ`. With the corrected pressure-consistent derivative, that time-dependent canonicalization is precisely large enough to replace the bad `NG3~k^2` branch by the Eq. (78) branch.

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
  - [x] DF5e.3a — rate/auxiliary Schur derived and spurious `a^2 xi k^2/[4(c+1)]` localized analytically.
  - [x] DF5e.3b — Eq. (72) normalization, background equations, NG2, GR degeneracy and f-sector prefactors audited.
  - [x] **DF5e.3e — BD algebraic/state coefficient audited; O(1e3) residual traced to omitted `dot P_f` in the diagnostic derivative path.**
  - [ ] **DF5e.4 — RED first: pressure-consistent time-dependent BD canonicalization; require Eq. (78) NG3 green at `k=100,200,400,800`. NEXT.**
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

- `test_case_c_finite_k_ng3_matches_de_felice_eq78` remains RED until the time-dependent BD canonicalization is implemented.
- Case-C physical speed regression remains RED/untrusted.
- `tests/test_comelli_native_scalar.py` remains intentionally RED.
- The new pressure-trajectory regression required by DF5e.4 has not yet been committed or executed.

## Verification status

The DF5e.3e hard finding was reproduced in an independent scratch reconstruction using the exact quadratic HR interaction. No physical coefficient was changed. Repository tests have not been executed in the current environment because the container cannot clone GitHub and GitHub Actions are disabled. Do not label DF5e.4 green until a real repository worktree executes the RED/GREEN cycle.

## Immediate restart instruction

**Resume at DF5e.4 — pressure-consistent time-dependent BD canonicalization.**

1. Add a RED regression for the local k-essence pressure drift in the Case-C `C_ZZ` derivative: `dot P_f=-3 n H_f c_sf^2(rho_f+P_f)`.
2. Correct the diagnostic derivative path first and verify `h_ZZ^eff` becomes O(1) and agrees with the Eq. (78)-required Schur value.
3. Add a RED finite-k regression for the production reducer that replaces frozen `h_ZZ` by the time-corrected `h_ZZ^eff` while retaining the antisymmetric `Z-Ydot` couplings generated by integrating `Y Zdot` by parts.
4. Implement the minimal general time-dependent canonicalization; do not tune Eq. (44), Eq. (45), Eq. (54), EH, matter, or HR coefficients.
5. Require Eq. (78) `NG3` green at `k=100,200,400,800`, then re-run NG1/NG2, GR degeneracy and the three physical speed branches.
6. Move to Candidate C only after Case C is green.
