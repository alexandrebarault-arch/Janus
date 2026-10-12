# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **authoritative restart point after any interruption**. Read this file first and update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The Candidate-C background bridge is under control. The old direct Comelli 12x12 closure and a later correctly index-reduced Comelli reconstruction both fail to recover the physical helicity-0 gradient, despite reproducing the visible radiation mode. They must not be used for transfer/segregation conclusions.

The active route is now an **independent scalar quadratic-action reconstruction**, primarily from De Felice et al. arXiv:1404.0008 and Lagos & Ferreira arXiv:1610.00553, followed only afterwards by a term-by-term comparison back to Comelli.

## Closed facts

### JANUS / De Felice / Lagos conventions

- JANUS -> Comelli/De Felice: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi*J`, `f1=Gamma`.
- Lagos massive-bigravity variables map as
  - `r = xi`,
  - `Nbar = xi*c`,
  - `Z = m^2 J = m^2 f2/xi`,
  - `Z_tilde = m^2 Gamma/xi = m^2 f1/xi`.
- Therefore `r*Z = m^2 f2` and `r*Z_tilde = m^2 f1` exactly.
- This action-level map is independent of the Comelli scalar field equations.
- Lagos massive bigravity has `alpha_L=0`. Hence there is no direct interaction term of the form `(partial^2 E)^2` from the extra `alpha_L` operator. The helicity-0 spatial gradient must emerge after eliminating the lapse/shift auxiliaries together with the Einstein-Hilbert kinetic structure; it is not expected to be one isolated explicit `k^2 E` interaction block.

### De Felice principal action

- De Felice scalar reduction integrates out nondynamical `B,b,Phi,varphi`, leaving three physical scalar variables and a quadratic action with matrices `K,N,M`.
- Their Eq. (86) contains one gravitational scalar speed plus the two matter sound speeds.
- `numerics/de_felice_action_principal.py` now independently implements Eqs. (80), (82), (86) without calling the historical `flrw_two_matter.diagnostics()` implementation.
- On Candidate C, independent numerical cross-checks give the same `c_s^2` as the historical implementation at `a=1,0.5,0.2`.
- At `a=0.5` (`z=1`): `c_s^2 ~= 0.69207999`, `c_s ~= 0.83191345`.
- The high-k scalar kinetic coefficient is taken from De Felice Eq. (80): `NG3 -> (3/8) m^2 a^4 xi J B` for flat FLRW.

### A.3 / A.18 issue

- Printed Comelli/earlier-paper A.3/A.18 contains `(calB1-calE)`.
- Raw gauge-invariant definitions give `Xi2-c^2 Xi1 = calB1-calE'` exactly.
- Bianchi tests on the exact Case-C background select the derived-prime form at finite tau.
- Printed-unprime remains only a typo/control branch.

### Direct Comelli reconstruction — closed negative result

- Old closure: Candidate C radiation speed is exactly `1/sqrt(3)` but the supposed gravity pair is only `c~0.0159` instead of `~0.8319`.
- Dust+dust gives the same failure.
- At large k the bad frequency approaches a constant rather than scaling with k; the gravity `k^2` term is structurally absent.
- Correctly treating `B1` as nondynamical and index-reducing the direct system reproduces the expected three second-order physical fields but still fails the Case-C gravitational equation.
- Simple fixes already rejected: matter mixture, g00/f00 closure choice, individual background derivatives, A1/A2 typo, A.18 swap inside old closure, f-trace sign flips, numerical conditioning, selected square minors, frozen-time PGCD, and eliminating `B1'` alone.

## Exact Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`.

- `rho1=3/a^4`, `rho2=3/(a xi)^3`.
- Exact branch: `a^4 xi^2 + xi - a - a^4/3 = 0`.
- `numerics/comelli_case_c.py` implements the exact branch, conformal map `tau(a)`, inverse `a(tau)`, background derivatives and scaled `D_tau` operator.
- Published acceptance equation (Comelli B.5 in this specialization):
  `E'' + (3/tau) E' - (2/3) k^2 E = 0`.
- With `E=tau^2 e(x)`, `x=k tau`, equivalent target:
  `x^2 e_xx + 7 x e_x + 8 e - (2/3) x^2 e = 0`.
- High-x factor: `3 q^2 - 2`.

## New files / commits for the action route

- `tests/test_lagos_action_bridge.py`
  - RED commit: `85ede8f`
- `numerics/lagos_action_bridge.py`
  - implementation commit: `89c1482`
- `tests/test_de_felice_action_principal.py`
  - RED commit: `c761e4c`
- `numerics/de_felice_action_principal.py`
  - implementation commit: `e510107`

Container network cannot clone/download GitHub in this environment, so the new pytest files have not yet been executed as a repository suite. Their core algebra was independently evaluated in scratch calculations; do not mark the suite green until an executable checkout is available.

## Active task list

- [x] Convention bridge and exact Candidate-C background.
- [x] Audit old Comelli scalar equations / closure.
- [x] Independent De Felice high-k regression.
- [x] Exact Case-C dynamically on-shell benchmark.
- [x] Resolve internal A.3/A.18 bookkeeping in favor of `E'`.
- [x] Correctly index-reduce `B1` as nondynamical in the direct Comelli route.
- [x] Demonstrate that the correctly index-reduced Comelli transcription still misses B.5.
- [ ] **T1c — replace/validate the scalar reduction independently.** IN PROGRESS.
  - [x] **T1c.6o.1 — Lagos action convention bridge.** `r=xi`, `Nbar=xi*c`, `Z=m^2 f2/xi`, `Z_tilde=m^2 f1/xi`.
  - [x] **T1c.6o.2 — independent De Felice principal action.** Reproduce `c_s^2` without using Comelli or the historical diagnostic implementation.
  - [ ] **T1c.6o.3 — transcribe the Hassan-Rosen specialization of Lagos Eqs. (3.6)-(3.8) into a Fourier-space scalar quadratic action.** Set constant Planck masses and `alpha_L=0`; retain `Phi1,Phi2,B1,B2` as auxiliaries and `Psi1,Psi2,E1,E2` before gauge reduction.
  - [ ] **T1c.6o.4 — integrate out `Phi1,Phi2,B1,B2` symbolically/numerically from the action, then verify that the massive-bigravity metric sector has one scalar physical DoF after gauge removal.**
  - [ ] **T1c.6o.5 — add separately coupled g/f barotropic matter actions (same physical setup as De Felice) and recover Eq. (86) from the reduced high-k action, not by inserting Eq. (86) as an input.**
  - [ ] **T1c.6p — compare the independently action-derived auxiliary constraints and reduced gradient term to Comelli term-by-term; identify exactly where the direct transcription/reduction loses the helicity-0 gradient.**
  - [ ] **T1c.6q — Case-C acceptance:** recover B.5 exactly or an explicitly equivalent action-variable equation.
  - [ ] verify the result is invariant under Bianchi-redundant equation representatives.
- [ ] **T2 — Candidate C full scalar validation:** recover De Felice gravity speed from the new reduced system on dust+dust and visible-radiation backgrounds.
- [ ] **T3 — replace the faulty old scalar closure with the validated action-derived system.**
- [ ] **T4 — implement `numerics/comelli_native_scalar.py` or a clearly named action-based replacement.**
- [ ] **T5 — make `tests/test_comelli_native_scalar.py` green + >=3 additional `(z,k)` high-k regressions.**
- [ ] **T6 — full Gate-2B regression suite.**
- [ ] **T7 — time-domain transfer RHS + fundamental transfer matrix.**
- [ ] **T8 — continuous GR-connected/adiabatic mode tracking.**
- [ ] **T9 — compute `T_gg,T_gf,T_fg,T_ff` and relative-mode growth.**
- [ ] **T10 — Gate-2B verdict with numerical tolerances and domain.**

## Current RED regression

`tests/test_comelli_native_scalar.py` still imports the intentionally absent `numerics/comelli_native_scalar.py`. Do not implement around it until T1c is independently closed.

## Immediate restart instruction

**Resume at T1c.6o.3 — Lagos scalar quadratic action transcription.**

1. Use Lagos & Ferreira arXiv:1610.00553 Eqs. (3.6)-(3.8), massive-bigravity specialization Eqs. (3.13)-(3.15), with the bridge in `numerics/lagos_action_bridge.py`.
2. Work in Fourier space with `partial^2 -> -k^2` and constant `M1,M2`; set `alpha_L=0` only because this is exactly the Hassan-Rosen specialization, not as a fitting choice.
3. Keep `Phi1,Phi2,B1,B2` algebraic. Do **not** differentiate their constraints into new evolution equations.
4. First reproduce the one-scalar DoF count of pure metric massive bigravity after auxiliary elimination and gauge removal.
5. Then add the two separate matter sectors and derive the high-k principal matrix. Acceptance is De Felice Eq. (86) emerging from the action.
6. Apply the same action reduction to exact Case C and require B.5.
7. Only then compare to Comelli to locate the exact lost term/constraint structure.
8. Update this checkpoint immediately after every new hard ruling or completed subtask.
