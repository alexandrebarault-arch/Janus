# Gate 2B — persistent checkpoint

Date: 2026-10-12
Canonical branch: `research/v2-flrw`
Global first restart file: `research/RESTART_TASKS.md`

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The direct Comelli closure, including the corrected-index reconstruction, fails to recover the physical helicity-0 gradient. The active route is an independent scalar quadratic-action reconstruction from De Felice et al. 1404.0008 and Lagos & Ferreira 1610.00553.

## Closed facts

### Convention bridge

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi*J`, `f1=Gamma`.
- Lagos massive bigravity: `r=xi`, `Nbar=xi*c`, `Z=m^2 f2/xi=m^2 J`, `Z_tilde=m^2 f1/xi=m^2 Gamma/xi`.
- Massive bigravity has `alpha_L=0`; the helicity-0 gradient appears only after lapse/shift elimination together with the Einstein-Hilbert structure.

### Independent De Felice principal action

- `numerics/de_felice_action_principal.py` independently implements the relevant high-k coefficients.
- Candidate-C checks agree at `a=1,0.5,0.2`.
- At `a=0.5`: `c_s^2 ~= 0.69207999`, `c_s ~= 0.83191345`.

### Lagos pure-metric action

- interaction potential and EH scalar self-actions independently reconstructed;
- pure metric action exchange-symmetric on proportional equal-Planck controls;
- `Phi1,Phi2,B1,B2` eliminated algebraically at action level;
- post-auxiliary velocity Hessian rank = 1 on proportional controls;
- in the relative/common basis only `E-=(E1-E2)/sqrt(2)` carries the pure-metric kinetic projection;
- the one-field relative slice is structural only, not Candidate-C physics without matter/background terms.

### Direct Comelli route — closed negative result

- radiation mode is recovered at `1/sqrt(3)`;
- the supposed gravity pair gives `c~0.0159` instead of the independent `~0.8319` benchmark;
- dust+dust fails identically and the bad high-k frequency saturates instead of scaling with k;
- the physical gravity `k^2 E` structure is absent from that closure;
- changing matter mixture, closure rows, selected signs/minors, or making `B1` nondynamical does not repair it.

### A.3 / A.18

Raw invariants select `(calB1-calE')`; the printed `(calB1-calE)` form is retained only as a typo/control branch.

## Exact Case-C acceptance benchmark

`8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`.

- branch: `a^4 xi^2 + xi - a - a^4/3 = 0`;
- required B.5: `E''+(3/tau)E'-(2/3)k^2 E=0`.

## New matter-action result

`numerics/de_felice_matter_action.py` now contains the full flat-Fourier scalar specialization of the P(X) quadratic matter action, including lapse, shift, scalar spatial metric, matter-field velocity and gradient terms.

TDD history:

- RED `b12ad1d95cde5926bdbc4896454cdc4f352274cd` -> GREEN `0448eef3ad05f6937aca8fadcab9a04d4916c712`;
- RED `3e13f971447213d3510c940303330355383c7eff` -> GREEN `d26017a1b65e391d9cb80edc75ca308829819d20`.

Focused reconstructed local run: `8 passed`.

Hard checks now pinned:

- free P(X): `omega^2=c_s^2 N^2 k^2/a^2`;
- pure-lapse limit reproduces the earlier Eq. (54) coefficient exactly;
- shift appears through `delta_phi/phi_dot_0 + a B/N`;
- `Tr(H)=6 psi` and `H_ij H^ij=12 psi^2+(2/3)k^4 E^2`;
- multiplying by `N a^3` gives the explicit background volume normalization;
- with `b=a*r`, `Nbar=r*c`, the free f-sector mode has `omega_f^2=c_s,f^2 c^2 k^2/a^2` in common coordinate time.

The unreduced P(X) representation remains singular at exact `c_s^2=0`; take the dust limit only after the constrained action has been reduced.

## Test execution caveat

A clean repository checkout/full pytest suite is still unavailable from the local compiler sandbox. Focused reconstructed tests were executed locally. Do not describe the whole repository suite as green.

## Active task list

- [x] Convention bridge / exact Candidate-C and Case-C backgrounds.
- [x] Reject direct Comelli closure for Gate-2B physics.
- [x] Independent De Felice principal-action regression.
- [ ] **T1c — independently reconstruct and validate scalar action.** IN PROGRESS.
  - [x] Lagos action convention bridge.
  - [x] independent De Felice principal action.
  - [x] pure-metric Lagos quadratic action + exchange controls.
  - [x] algebraic elimination of `Phi1,Phi2,B1,B2`.
  - [x] proportional-control kinetic rank = 1 and explicit relative/common reduction.
  - [x] **T1c.6o.5a:** one-sector barotropic/P(X) scalar matter action.
  - [x] **T1c.6o.5b:** g/f lapse, scale-factor and `N a^3` volume normalization.
  - [ ] **T1c.6o.5c — ACTIVE:** assemble metric + g fluid + f fluid in the common `M1^2 a^3` normalization and eliminate all nondynamical variables.
  - [ ] **T1c.6o.5d:** derive high-k kinetic/gradient matrix and recover three physical speeds without inserting the De Felice result.
  - [ ] compare the action-derived reduced structure to Comelli and identify the lost term.
  - [ ] Case-C acceptance: recover B.5 or an explicitly equivalent action-variable equation.
- [ ] Candidate-C full scalar validation from the new action.
- [ ] native/action-based transfer solver and continuous mode tracking.
- [ ] compute `T_gg,T_gf,T_fg,T_ff` and relative-mode growth.
- [ ] final Gate-2B verdict with tolerances/domain.

## Immediate restart instruction

**Resume at T1c.6o.5c.**

1. Use `pure_metric_lagrangian_healthy()` as the gravitational block; do not import the failed Comelli closure.
2. Add the g-sector Eq. (54) action with background `(N,a)=(1,a)`.
3. Add the f-sector Eq. (54) action with `(Nbar,b)=(r*c,a*r)`.
4. Divide both matter actions by the same pure-metric normalization `M1^2 a^3`; with `M1^-2=8piG`, this means the g and f matter weights must be derived explicitly rather than guessed.
5. First RED test: zero matter must reduce exactly to `pure_metric_lagrangian_healthy()`.
6. Second RED test: proportional equal-Planck/equal-matter data must be exchange symmetric.
7. Only then extend auxiliary elimination to include matter variables and derive the principal matrix.
8. Update `research/RESTART_TASKS.md` and this file at the next hard result.
