# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **single restart point after any interruption**. Read this file first and update it whenever a hard finding, rejected hypothesis, task state, or restart point changes.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

Candidate-C background conventions are under control. The old 12x12 scalar closure is algebraically consistent but removes the physical helicity-0 gradient; do not use it for transfer/segregation physics.

## Hard facts to preserve

### Convention/background bridge

- JANUS -> Comelli/De Felice: `beta_n=n! a_n`, `f2=yJ`, `f1=Gamma`, `xi=y`, `kappa=alpha^2`, `c=ctilde`.
- De Felice Eq. (27), `2(c-1)W = rho_g - c xi^2 rho_f/kappa`, matches JANUS at ~`2e-14` relative on the dust+dust comparison point.
- De Felice high-k gravity speed agrees with `flrw_two_matter.py::diagnostics()['scalar_cs2']`.

### Published equations audit

- Comelli A.7-A.16, slips, A.17, and A1/A2 identities were independently re-audited.
- Full A.12/A.16 were checked before slip reduction; their anisotropic brackets vanish exactly under the JANUS slips. No explicit gradient block was dropped there.
- A.17 is algebraically valid; never delete it merely to improve a determinant.
- **A.18 prime ambiguity is now resolved.** Appendix A of arXiv:1202.1986 prints, in the same consecutive list of useful identities, A.3 with `(B1-E)` and A.4 with `(B1-E')`. The 2014 A.18 again uses `(B1-E)`. Therefore the previous global "prime correction" was wrong; it conflated raw perturbation variables with the gauge-invariant combinations. Physical bookkeeping must use unprimed `E` in A.3/A.18 and primed `E` only in A.1/A.4/A.5-A.6 where printed.
- `numerics/comelli_bridge.py` and `tests/test_comelli_bridge.py` were corrected accordingly in TDD. RED numerical mismatch was `0.08128901146755702`; GREEN identity residuals are <=`3e-17`. Commits: test `65e786c`, implementation `b29270c`.
- The old derived-prime A.18 organization is retained only as historical/debugging evidence. Its rank-6 result must no longer be used as physical justification for declaring `E'` freely dynamical.
- Appendix B.2 proves the missing helicity-0 gradient exists. For `w1=1/3`, `w2=0`, `a2=a3=0`, `f1=f2`, B.5 reduces to `E''+(3/tau)E'-(2/3)k^2E=0` sub-horizon.
- With `E=tau^2 e(x)`, `x=k tau`, the acceptance operator is exactly `x^2 e_xx + 7x e_x + 8e - (2/3)x^2 e = 0`.
- The primary 2014 reduction explicitly states that `B1` and `Psi1/2` are nondynamical and can be expressed in terms of `E`, `Phi1`, `Phi2`; only `E`, `Phi1`, `Phi2` obey the three second-order scalar equations.
- At leading Case-C order the direct equations already reproduce the two matter/metric modes independently: visible-radiation `Phi1` obeys the GR equation and twin-dust `Phi2` obeys Comelli B.4. The missing mode is specifically the gravitational `E` mode governed by B.5.

### Old closure failure

- Candidate C at `a=0.5`, `k=0.5 h/Mpc`: radiation pair is exactly `1/sqrt(3)` but the second pair is only `c~0.0159` versus De Felice `c_s~0.8319`.
- Dust+dust gives the same spurious pair.
- As k increases, the faulty frequency tends to `omega~23.894 H0`; apparent speed falls as `1/k`, so the `k^2 E` gravity gradient is structurally absent.
- Ruled out as fixes: dust/radiation mixture, `d(g00)` vs `d(f00)`, individual background derivatives, simple A1/A2 typo, isolated f-trace sign flip, double precision/conditioning, De Felice normalization, and merely swapping A.18 inside the same old closure.
- The old constraint/acceleration organization was built around the now-rejected derived-prime A.18 and rank-6-at-fixed-`E'` assumption. Its structural interpretation must be redone.
- Promoting `B1'` as an independent acceleration unknown is also inconsistent with the published statement that `B1` is nondynamical; however scratch elimination shows that fixing this alone does not restore B.5. It is a contributing structural issue, not yet a sufficient diagnosis.

## Exact dynamically on-shell Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`, `rho1=3/a^4`, `rho2=3/(a xi)^3`.

Exact branch:
`a^4 xi^2 + xi - a - a^4/3 = 0`.

Positive root:
`xi(a)=[-1+sqrt(1+4a^5+(4/3)a^8)]/(2a^4)`.

Early-time conformal series retained from the on-shell solution:
- `a=tau+tau^6/12+tau^9/54-5tau^11/132+...`;
- `xi=tau+tau^4/3-11tau^6/12-29tau^9/54+...`;
- hence `H=1/tau+O(tau^4)`, `H_omega=2/tau+O(tau^2)`, and crucially `c=2+tau^3+O(tau^5)`.
- Because `rho2~tau^-6`, these nominally subleading background corrections can enter the same hierarchy order as induced `Phi2~tau^3`. Freezing `a=xi=tau,c=2` while retaining later perturbation terms is therefore inconsistent for B.5.

### Executable benchmark in Git

- `numerics/comelli_case_c.py` implements the exact branch, exact on-shell background derivatives, dimensionless k, conformal time `tau(a)`, monotonic inversion `a(tau)`, and `case_c_background_from_tau`.
- It implements `D_tau[tau^p f(k tau)] = tau^(p-1)(p+x d_x)f` and the corresponding second derivative.
- `tests/test_comelli_case_c.py` pins branch residual, `c->2`, `H a->1`, `f1=f2=xi`, conformal-time inversion and scaled derivatives.
- Verification performed locally: benchmark tests passed; conformal-map inversion error was ~`1.7e-18` at the control point.

## Descriptor / DAE findings

- `numerics/comelli_descriptor.py` keeps the direct system rectangular: 13 equations x 11 variables, quadratic in a frozen commuting derivative only as an audit representation.
- Arbitrary square minors and frozen-time `D_tau->s`/PGCD are rejected as physical mode criteria because variable-coefficient Bianchi identities are differential-operator identities.
- Correct asymptotic variable: `x=k tau`; preserve `D_tau=partial_tau+(x/tau)partial_x` through elimination.
- Natural first weights for the pure gravity mode are `E=tau^2 e(x)`, induced `Phi2~tau^3 q3(x)`, induced `Phi1~tau^5 p5(x)`, shifts/velocity potentials with their constraint-determined weights, and no independent leading matter-mode amplitudes.
- On the oversimplified frozen-leading background `a=xi=tau,c=2`, algebraic elimination with the now-correct printed A.18 produces an extra relation and the wrong gravity ODE. This is **not** accepted as a contradiction with B.5 because the exact Case-C corrections `c-2=O(tau^3)`, `xi-tau=O(tau^4)`, etc. multiply divergent sector-2 densities and contribute at the same order.
- The derived-prime scratch chain happened to preserve a three-equation count but is no longer physically admissible after the primary-source audit; do not use that as evidence.
- The next derivation must use the printed/unprimed A.18 together with the exact on-shell background expansion to the order at which `Phi2~tau^3` and `Phi1~tau^5` feed back into the E equation.

## Rejected hypotheses / superseded rulings

- k/time normalization error.
- visible dust+radiation mixture.
- `d(g00)` vs `d(f00)` closure choice.
- one bad background derivative.
- De Felice normalization/transcription error.
- simple A1/A2 typo.
- omitted anisotropic gradient after slip.
- isolated f-trace interaction-sign flip.
- floating-point conditioning.
- Bianchi residuals as proof of physical mode content.
- selected square minor as dispersion relation.
- frozen-time commuting-PGCD as full descriptor criterion.
- fixed-xi/frozen-a Case-C trajectories.
- setting non-gravity homogeneous kernel amplitudes to zero before Fredholm compatibility.
- **Superseded:** the earlier claim that A.3/A.18 must contain `E'`. Primary source comparison shows A.3/A.18 use unprimed `E`, while A.4 separately uses `E'`.
- **Rejected as sufficient fix:** eliminating `B1'` alone on the frozen-leading background; it does not recover B.5.

## Active task list

- [x] Convention bridge and Candidate-C background.
- [x] Scalar equations / old closure audit.
- [x] Independent De Felice regression and diagnosis of missing gravity pair.
- [x] **T1a** — dust+dust Candidate-C comparison.
- [x] **T1b** — primary-source audit.
- [x] **T1b.1 — resolve A.18 prime ambiguity from the 2012/2014 appendices; physical relation is unprimed.**
- [ ] **T1c — reproduce Comelli Case-C B.5 on the dynamically on-shell branch.** IN PROGRESS.
  - [x] reject off-shell/frozen-a benchmarks;
  - [x] derive exact dynamic `xi(a)` and conformal-time map;
  - [x] establish singular Fredholm structure;
  - [x] audit full spatial equations before slip;
  - [x] build/test direct 13x11 descriptor audit tool;
  - [x] reject selected minors and frozen-time PGCD;
  - [x] verify leading `Phi1` radiation and `Phi2` dust equations;
  - [x] identify induced pure-E scalings `Phi2~tau^3`, `Phi1~tau^5`;
  - [x] show `B1`-algebraic elimination alone on frozen-leading background is insufficient;
  - [ ] **T1c.6h — rebuild the printed-A.18 hierarchy with the exact on-shell background series, retaining `c-2=O(tau^3)`, `xi-tau=O(tau^4)`, and all background terms that survive against `rho2~tau^-6`.**
  - [ ] **T1c.6i — eliminate nondynamical variables order-by-order and recover the reduced three-field (`E,Phi1,Phi2`) system.**
  - [ ] **T1c.6j — pure-E acceptance: recover exactly `E''+(3/tau)E'-(2/3)k^2E=0`, equivalently `x^2e''+7xe'+8e-(2/3)x^2e=0`.**
  - [ ] verify B.5 under Bianchi-redundant row representatives.
- [ ] **T2** — apply validated reduction to dust+dust Candidate C; recover De Felice speed.
- [ ] **T3** — identify exact structural error(s) in old 12x12 closure and replace them.
- [ ] **T4** — implement corrected `numerics/comelli_native_scalar.py`.
- [ ] **T5** — make `tests/test_comelli_native_scalar.py` green + >=3 extra `(z,k)` regressions.
- [ ] **T6** — full Gate-2B regression suite.
- [ ] **T7** — time-domain transfer RHS + fundamental matrix.
- [ ] **T8** — continuous GR-connected/adiabatic mode tracking.
- [ ] **T9** — compute `T_gg,T_gf,T_fg,T_ff` and relative-mode growth.
- [ ] **T10** — Gate-2B verdict with tolerances/domain.

## Current RED regression

`tests/test_comelli_native_scalar.py` still imports the intentionally absent `numerics/comelli_native_scalar.py`. Do not implement around it until T1c is closed.

## Immediate restart instruction

**Resume at T1c.6h — printed A.18 + exact on-shell Case-C series.**

1. Use unprimed `E` in A.3/A.18 and primed `E` in A.1/A.4 exactly as the primary Appendix A states.
2. Use `case_c_background_from_tau` or a symbolic series derived from the exact branch; do not freeze `a=xi=tau,c=2` beyond the strictly leading equations.
3. Keep `x=k tau`, `E=tau^2 e(x)`, induced `Phi2=tau^3 q3(x)+...`, induced `Phi1=tau^5 p5(x)+...`.
4. Retain enough background orders that products with `rho2~tau^-6` are correct through the first E-compatibility order; at minimum include `c=2+tau^3+...`, `xi=tau+tau^4/3+...`, and consistent H/H_omega/rho expansions.
5. Eliminate `Psi1/2`, matter constraints, F1/F2, B1/B2 algebraically/order-by-order; do not promote B1 into a physical state.
6. Acceptance is the exact B.5 benchmark operator, not merely the high-k root.
7. Update this checkpoint after each hard ruling.
8. Move to T2 only after B.5 is recovered.
