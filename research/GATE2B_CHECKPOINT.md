# Gate 2B — authoritative restart checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The De Felice/Hassan-Rosen reconstruction now has the correct scalar degree count, the first two kinetic invariants, and a pressure-consistent time-dependent BD elimination that recovers the published finite-k `NG3` branch in the executable DF5e.4 subset.  The remaining Case-C blocker is the scalar **dispersion/state sector**, not the kinetic ghost invariant.

Do not proceed to Candidate-C transfer integration yet.

## Closed hard facts

### Background / targets

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Exact Case-C background: `numerics/comelli_case_c.py`.
- Case-C asymptotic acceptance: `E''+(3/tau)E'-(2/3)k^2E=0`.
- Independent De Felice principal action at `a=0.05`: `c_s^2=-0.6665833419871022`.
- Candidate-C target at `a=0.5`: `c_s^2 ~= 0.69208`, `c_s ~= 0.83191`.
- The four De Felice background equations close on the Case-C control point at ~`1e-16` relative.

### Action pieces

- Eq. (44) EH scalar contractions were independently audited.
- Eq. (54) P(X) matter action was independently audited.
- `hr_scalar_quadratic_action_density_de_felice()` directly implements the O(delta^2) interaction of Eqs. (45)-(46).
- Historical missing HR shift-volume terms were found and fixed (`8637753`, regression `181deda`).
- Eq. (72) normalization is correct: `1/(n H_f)=a/H_omega`.
- f-field drift is correct and must remain
  `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2`.

### DF4 — degree count / BD basis CLOSED

- Eq. (72) basis `(Y1,Y2,Y3,Z_BD)` exposes the null BD kinetic direction.
- `Z_BD` is algebraically eliminable and exactly three scalar kinetic directions remain.
- NG2 matches De Felice Eq. (78) to roughly `1e-8...1e-9` relative over `k=100...800` in the audited reconstruction.
- GR one-metric degeneracy is preserved.

## DF5e.3 — old spurious kinetic branch localized

Before proper time-dependent BD elimination, the auxiliary/rate Schur leaves

`K_Y3Y3 -> a^2 xi k^2/[4(c+1)]`

at high k.  On early Case C (`c->2`) this is `a^2 xi k^2/12`, explaining the historical `NG3~k^2` values.

The underlying f-sector rate/auxiliary coefficients were independently rederived from Eqs. (44), (45), (54); the rate sector itself is not to be tuned.

## DF5e.3e — BD algebraic/state audit CLOSED

The apparent `h_ZZ^eff ~ -2.15e3` was caused by differentiating `C_ZZ(a)` while forcing `P_f=0` at neighboring points despite finite diagnostic `c_sf^2`.

For barotropic P(X),

`dot P_f = c_sf^2 dot rho_f = -3 n H_f c_sf^2 (rho_f+P_f)`.

At `a=0.05,k=400,c_sf^2=0.1`:

- `partial C_ZZ/partial P_f ~= 4.6882748e-8`;
- `dot P_f ~= -4.60771344e10`;
- omitted contribution to `dot C_ZZ ~= -2160.22`.

Including it moves the algebraic coefficient to `h_ZZ^eff ~= +6.741...`, consistent with the Eq. (78)/(79) requirement near `6.7418`.

No EH, matter or HR coefficient is changed.

## DF5e.4 — time-dependent BD kinetic canonicalization IMPLEMENTED

### Implementation

- `numerics/bd_time_canonicalization.py`: generic integration-by-parts helper for the complete `C[:,Z] Zdot` column.
- `numerics/de_felice_two_matter_exact_quadratic.py`: stable Hessian backend using the direct O(delta^2) HR action rather than finite-differentiating the nonlinear HR potential and then differentiating that Hessian again.
- `numerics/de_felice_bd_audit.py`: pressure-consistent Case-C derivative and time-dependent BD physical adapter.
- regressions committed for:
  - pressure chain rule;
  - synthetic canonicalization identity;
  - Eq. (78) NG3 at four k values.

For `H=[[M,C],[C.T,K]]`, `z=Z`, `c_i=C[i,z]`, and `mu=d ln(Na^3)/dt`, the canonicalizer applies

- `C_new[z,i]=C[z,i]-c_i` for `i!=z`;
- `C_new[:,z]=0`;
- `M_new[i,z]=M[i,z]-(dot c_i+mu c_i)`;
- `M_new[z,z]=M[z,z]-(dot c_z+mu c_z)`.

At `N=1`, `mu=3 H_cosmic`.

### Fresh executable-subset verification

The full repository cannot be cloned in the current container and GitHub Actions are disabled.  A minimal executable workspace reconstructed from the committed formulas was run freshly:

- pressure-chain + canonicalizer: `2 passed`;
- Eq. (78) NG3:
  - `k=100`: `0.0158886855` vs `0.015890` (`-0.008%`);
  - `k=200`: `0.0179238512` vs `0.017943` (`-0.107%`);
  - `k=400`: `0.0184631480` vs `0.0185421788` (`-0.426%`);
  - `k=800`: `0.0191642249` vs `0.018698` (`+2.493%`).

All four satisfy the existing 3% Eq. (78) tolerance.

**This is not a claim that the full repository suite is green.**

## New blocker — DF5e.5: use De Felice Eq. (85), not the frozen Hessian speed equation

The three-speed Case-C regression remains RED.

The historical `physical_squared_phase_speeds()` freezes the reduced matrices and solves

`K Yddot + (C.T-C) Ydot - M Y = 0`.

This is not the scalar dispersion equation used in De Felice on a time-dependent FLRW background.

From Eq. (73), De Felice Eq. (84) gives for `N=1`

`K Yddot + (dot K + 3 H K + 2 Nmat) Ydot + (dot Nmat + 3 H Nmat + M_DF)Y = 0`.

In repository Hessian conventions (`C=-Nmat`, `M_hessian=-M_DF`):

`K Yddot + (dot K + 3 H K + C.T-C) Ydot + (dot C.T + 3 H C.T - M_hessian)Y = 0`.

Eq. (85), not the frozen equation, is therefore the correct high-frequency characteristic equation. Eq. (86) gives the three principal sound speeds.

A first direct numerical differentiation of the already-reduced physical matrices is ill-conditioned: the gravity state coefficient requires cancellation of terms differing by roughly nine orders of magnitude.  The two matter branches stay near their expected principal values, but the gravity root is unstable under the outer derivative step.  Do not interpret that unstable numerical root as a physical instability or as evidence for changing the action coefficients.

The independent module `numerics/de_felice_action_principal.py` already implements Eqs. (80), (82), (86) and returns the correct gravity target.  DF5e.5 must bridge the reconstructed action to that principal result without catastrophic cancellation.

## Active task list

- [x] convention bridge / exact Case-C background.
- [x] reject historical Comelli closure for Gate-2B physics.
- [x] independent De Felice high-k gravity target.
- [x] Eq. (54) matter action.
- [x] Eq. (44) EH scalar audit.
- [x] DF3 — exactly three scalar DOF.
- [x] DF4 — Eq. (72) basis + algebraic BD removal.
- [ ] **DF5 — recover all three physical high-k speeds.**
  - [x] DF5a — synthetic frozen-mode extractor validation.
  - [x] DF5e.2 — HR shift-volume bug found/fixed.
  - [x] DF5e.3a/b — rate/auxiliary Schur, basis normalization, NG2, GR degeneracy audited.
  - [x] DF5e.3e — pressure-chain cause of O(1e3) algebraic residual found.
  - [x] **DF5e.4 — pressure-consistent time-dependent BD canonicalization; NG3 four-k branch recovered in executable subset.**
  - [ ] **DF5e.5 — reconstruct Eq. (85) dispersion robustly and recover Eq. (86) gravity speed. NEXT.**
  - [ ] DF5d — Candidate-C gravity regression only after Case C speed branch is closed.
- [ ] DF6 — recover B.5/equivalent reduced action on Case C.
- [ ] T2 — Candidate-C validation at >=3 `(z,k)` points.
- [ ] T3 — identify exactly what the old Comelli closure projected out.
- [ ] T4 — native/action-based transfer solver.
- [ ] T5 — `tests/test_comelli_native_scalar.py` + >=3 regressions green.
- [ ] T6 — full Gate-2B regression suite.
- [ ] T7 — time-domain fundamental transfer matrix.
- [ ] T8 — continuous GR-connected/adiabatic mode tracking.
- [ ] T9 — compute `T_gg,T_gf,T_fg,T_ff` and relative growth.
- [ ] T10 — Gate-2B scientific verdict.

## Intentional RED / unverified

- Case-C full physical speed regression remains RED and now must be reformulated around Eq. (85).
- `tests/test_comelli_native_scalar.py` remains intentionally RED.
- Full-repository tests are unexecuted in this environment.

## Immediate restart instruction

**Resume at DF5e.5 — Eq. (85) dispersion audit.**

1. Keep DF5e.4 and the four-k NG3 regression fixed.
2. Derive a conditioned representation of `dot K` and `dot Nmat` from the exact-quadratic reduced action; avoid nested subtraction of O(1e15) state terms.
3. Prefer analytic differentiation of the Schur complement / basis transform or an equivalent high-k principal reduction.
4. Compare term-by-term with De Felice Eq. (86), not with the old frozen extractor.
5. Require `c_s^2=-0.6665833419871022` on Case C plus the two matter principal branches.
6. Only after that move to Candidate C.
