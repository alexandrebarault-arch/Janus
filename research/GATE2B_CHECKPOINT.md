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
- Lagos massive bigravity has `alpha_L=0`. Hence there is no direct interaction term of the form `(partial^2 E)^2` from the extra `alpha_L` operator. The helicity-0 spatial gradient must emerge after eliminating lapse/shift auxiliaries together with the Einstein-Hilbert kinetic structure; it is not expected to be one isolated explicit `k^2 E` interaction block.

### De Felice principal action

- De Felice scalar reduction integrates out nondynamical `B,b,Phi,varphi`, leaving three physical scalar variables and a quadratic action with matrices `K,N,M`.
- Their Eq. (86) contains one gravitational scalar speed plus the two matter sound speeds.
- `numerics/de_felice_action_principal.py` independently implements Eqs. (80), (82), (86) without calling the historical `flrw_two_matter.diagnostics()` implementation.
- Candidate-C cross-checks reproduce the same `c_s^2` at `a=1,0.5,0.2`.
- At `a=0.5` (`z=1`): `c_s^2 ~= 0.69207999`, `c_s ~= 0.83191345`.
- The flat high-k scalar kinetic coefficient is `NG3 -> (3/8) m^2 a^4 xi J B`.

### Lagos scalar interaction transcription

- `tests/test_lagos_scalar_interaction.py` RED commit: `b51940f`.
- `numerics/lagos_scalar_action.py` initial interaction transcription: `894b692`.
- **Important PDF parsing correction:** in Lagos Eq. (3.7), the coefficient rendered by text extraction as something like `nu 2 Nbar r 2` is `nu^2 * Nbar * r^2`; the final `2` is the exponent of `r`, not a denominator.
- The corrected metric-2 `Z_tilde` coefficient inside Eq. (3.7), for constant `M1`, is `2 nu^2 Nbar r^2 Z_tilde`.
- After the Eq. (3.7) overall prefactor is converted to the common `M1^2 a^3` normalization, the corresponding healthy-branch contribution is `2 Nbar^2 r^5 Z_tilde Psi2(3/2 Psi2 + b^2 k^2 E2)`.
- Correction commit: `2de9354`.
- Independent scratch evaluation on Candidate C with a generic scalar state gives raw and healthy-branch interaction actions equal to ~`5e-16` relative precision after this correction.
- With `alpha_L=0`, a pure `E1/E2` configuration and all lapse/shift/curvature perturbations set to zero has no direct interaction `E^2` term. The physical helicity-0 gradient must arise after auxiliary elimination.

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
- `numerics/comelli_case_c.py` implements exact branch, conformal map `tau(a)`, inverse `a(tau)`, background derivatives and scaled `D_tau` operator.
- Published acceptance equation: `E'' + (3/tau) E' - (2/3) k^2 E = 0`.
- With `E=tau^2 e(x)`, `x=k tau`: `x^2 e_xx + 7 x e_x + 8e - (2/3)x^2 e = 0`.
- High-x factor: `3 q^2 - 2`.

## Action-route files / commits

- `tests/test_lagos_action_bridge.py` — RED `85ede8f`.
- `numerics/lagos_action_bridge.py` — implementation `89c1482`.
- `tests/test_de_felice_action_principal.py` — RED `c761e4c`.
- `numerics/de_felice_action_principal.py` — implementation `e510107`.
- `tests/test_lagos_scalar_interaction.py` — RED `b51940f`.
- `numerics/lagos_scalar_action.py` — implementation `894b692`, corrected Eq. (3.7) prefactor `2de9354`.

Container network cannot clone/download GitHub in this environment, so these new pytest files have not yet been executed as a repository suite. Core algebra has been independently checked in scratch calculations; do not mark the suite green until an executable checkout is available.

## Active task list

- [x] Convention bridge and exact Candidate-C background.
- [x] Audit old Comelli scalar equations / closure.
- [x] Independent De Felice high-k regression.
- [x] Exact Case-C dynamically on-shell benchmark.
- [x] Resolve A.3/A.18 bookkeeping in favor of `E'`.
- [x] Correctly index-reduce `B1` as nondynamical in the direct Comelli route.
- [x] Demonstrate that the correctly index-reduced Comelli transcription still misses B.5.
- [ ] **T1c — replace/validate the scalar reduction independently.** IN PROGRESS.
  - [x] **T1c.6o.1 — Lagos action convention bridge.**
  - [x] **T1c.6o.2 — independent De Felice principal action.**
  - [ ] **T1c.6o.3 — transcribe the Hassan-Rosen Lagos scalar quadratic action.**
    - [x] **T1c.6o.3a — interaction potential (`Z`,`Z_tilde`, `alpha_L=0`) in Fourier space.** Raw and healthy-branch forms independently cross-checked; Eq. (3.7) `r^2` parsing error corrected.
    - [ ] **T1c.6o.3b — add the Einstein-Hilbert scalar self-actions for metric 1 and metric 2 with constant Planck masses.** Keep `Phi1,Phi2,B1,B2` algebraic.
    - [ ] **T1c.6o.3c — construct the full pure-metric quadratic Hessian / velocity form and test metric-exchange symmetry on a proportional background.**
  - [ ] **T1c.6o.4 — integrate out `Phi1,Phi2,B1,B2`; verify one scalar physical metric DoF after gauge removal.**
  - [ ] **T1c.6o.5 — add separately coupled g/f barotropic matter and derive the high-k principal matrix; recover De Felice Eq. (86) rather than inserting it.**
  - [ ] **T1c.6p — compare action-derived constraints and reduced gradient to Comelli term-by-term; identify exact lost structure.**
  - [ ] **T1c.6q — Case-C acceptance:** recover B.5 exactly or an explicitly equivalent action-variable equation.
  - [ ] verify result under Bianchi-redundant representatives.
- [ ] **T2 — Candidate C full scalar validation:** recover De Felice gravity speed from the new reduced system.
- [ ] **T3 — replace faulty old scalar closure.**
- [ ] **T4 — implement `numerics/comelli_native_scalar.py` or a clearly named action-based replacement.**
- [ ] **T5 — make `tests/test_comelli_native_scalar.py` green + >=3 extra `(z,k)` regressions.**
- [ ] **T6 — full Gate-2B regression suite.**
- [ ] **T7 — time-domain transfer RHS + fundamental matrix.**
- [ ] **T8 — continuous GR-connected/adiabatic mode tracking.**
- [ ] **T9 — compute `T_gg,T_gf,T_fg,T_ff` and relative-mode growth.**
- [ ] **T10 — Gate-2B verdict with tolerances/domain.**

## Current RED regression

`tests/test_comelli_native_scalar.py` still imports the intentionally absent `numerics/comelli_native_scalar.py`. Do not implement around it until T1c is independently closed.

## Immediate restart instruction

**Resume at T1c.6o.3b — Einstein-Hilbert scalar self-actions.**

1. Extend `numerics/lagos_scalar_action.py` with the non-interaction scalar terms of Lagos Eqs. (3.6) and (3.7), constant Planck masses and Fourier `partial^2 -> -k^2`.
2. Preserve the two time normalizations exactly: metric 1 is normalized by `M1^2 a^3`; metric 2 by `Nbar b^3 M2^2`, converted explicitly to the common normalization.
3. Keep `Phi1,Phi2,B1,B2` algebraic and do not differentiate their constraints.
4. Add a RED test before implementation that checks the pure-metric action is quadratic and is symmetric under metric exchange on a proportional background (`r=Nbar=c=1`, equal Planck masses), modulo relabeling 1<->2.
5. After the full pure-metric action is assembled, form its velocity/Hessian matrix and verify auxiliary variables have no own time derivatives.
6. Only then perform algebraic auxiliary elimination (T1c.6o.4).
7. Update this checkpoint immediately after every hard ruling or completed subtask.
