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
- A.18 is genuinely ambiguous: raw gauge-invariant definitions suggest `(calB1-calE')`, while the printed appendix gives `(calB1-calE)`.
- A.18 changes descriptor rank: derived-prime gives rank 6 for the seven constraint/identity equations at fixed background; printed-unprime gives rank 7 for generic `c!=1`.
- Appendix B.2 proves the missing helicity-0 gradient exists. For `w1=1/3`, `w2=0`, `a2=a3=0`, `f1=f2`, B.5 reduces to `E''+(3/tau)E'-(2/3)k^2E=0` sub-horizon.
- With `E=tau^2 e(x)`, `x=k tau`, the acceptance operator is exactly `x^2 e_xx + 7x e_x + 8e - (2/3)x^2 e = 0`.
- The primary Comelli reduction explicitly states that `B1` and the lapse potentials are **nondynamical** and can be expressed in terms of `E`, `Phi1`, `Phi2`; only `E`, `Phi1`, `Phi2` obey the three second-order scalar equations. This is now a central structural constraint on any JANUS reduction.
- At leading Case-C order the direct equations already reproduce the two matter/metric modes independently: the visible radiation `Phi1` equation agrees with the GR equation, and the twin-dust `Phi2` equation agrees with Comelli B.4. The remaining missing mode is therefore specifically the gravitational `E` mode governed by B.5.

### Old closure failure

- Candidate C at `a=0.5`, `k=0.5 h/Mpc`: radiation pair is exactly `1/sqrt(3)` but the second pair is only `c~0.0159` versus De Felice `c_s~0.8319`.
- Dust+dust gives the same spurious pair.
- As k increases, the faulty frequency tends to `omega~23.894 H0`; apparent speed falls as `1/k`, so the `k^2 E` gravity gradient is structurally absent.
- Ruled out as fixes: dust/radiation mixture, `d(g00)` vs `d(f00)`, individual background derivatives, simple A1/A2 typo, isolated f-trace sign flip, double precision/conditioning, De Felice normalization, and dropping in the alternate A.18 inside the same old closure.
- The old acceleration layer promotes `B1'` to an independent unknown together with `E''`, `Phi1''`, `Phi2''`. This conflicts with the published degree-of-freedom organization in which `B1` is nondynamical. **Promoting `B1` before eliminating the constraints is now the leading structural suspect for why the old closure projects out the helicity-0 gradient.**

## Exact dynamically on-shell Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`, `rho1=3/a^4`, `rho2=3/(a xi)^3`.

Exact branch:
`a^4 xi^2 + xi - a - a^4/3 = 0`.

Positive root:
`xi(a)=[-1+sqrt(1+4a^5+(4/3)a^8)]/(2a^4)`.

Early time:
`a~tau`, `xi~tau`, `H~1/tau`, `H_omega~2/tau`, `rho1~3/tau^4`, `rho2~3/tau^6`, `c->2`.

### Executable benchmark in Git

- `numerics/comelli_case_c.py` implements the exact branch, exact on-shell background derivatives, dimensionless k, conformal time `tau(a)`, monotonic inversion `a(tau)`, and `case_c_background_from_tau`.
- It implements `D_tau[tau^p f(k tau)] = tau^(p-1)(p+x d_x)f` and the corresponding second derivative.
- `tests/test_comelli_case_c.py` pins branch residual, `c->2`, `H a->1`, `f1=f2=xi`, conformal-time inversion and scaled derivatives.
- Verification performed locally: benchmark tests passed; conformal-map inversion error was ~`1.7e-18` at the control point.

## Descriptor / DAE findings

- `numerics/comelli_descriptor.py` keeps the direct system rectangular: 13 equations x 11 variables, quadratic in a frozen commuting derivative only as an audit representation.
- Arbitrary square minors and frozen-time `D_tau->s`/PGCD are rejected as physical mode criteria because variable-coefficient Bianchi identities are differential-operator identities.
- Correct asymptotic variable: `x=k tau`; preserve `D_tau=partial_tau+(x/tau)partial_x` through elimination.
- Natural first weights: `E=tau^2 e(x)`, shifts/velocity potentials `~tau`, `Phi/F/density contrasts~O(1)`.
- A sparse Laurent/Taylor-jet operator audit confirms that homogeneous kernel amplitudes cannot be either reintroduced freely at every order or set to zero wholesale; both procedures corrupt Fredholm compatibility.
- Local Taylor jets at regular `x0!=0` are preferable to a Laurent basis around `x=0` for diagnosing B.5 because the latter has Frobenius resonance/logarithmic structure.
- Treating `B1` as an independent evolving leading function causes both the derived-prime and printed-unprime A.18 descriptor chains to overconstrain the gravitational jet rather than recover the two-dimensional solution space of B.5.
- This failure, together with the paper's explicit nondynamical status of `B1`, motivates a new elimination order: solve `B1` algebraically from the constraint chain **before** constructing any second-order dynamics.

## Rejected hypotheses

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
- A.18 as a simple drop-in fix to the old closure (structural ambiguity remains because rank/index changes).
- fixed-xi/frozen-a Case-C trajectories.
- setting non-gravity homogeneous kernel amplitudes to zero before Fredholm compatibility.
- promoting `B1'` as though `B1` were an independent physical scalar is now disfavored by the published degree count and failed descriptor chains.

## Active task list

- [x] Convention bridge and Candidate-C background.
- [x] Scalar constraints/identities and old acceleration layer.
- [x] Old 12x12 closure + Bianchi diagnostics.
- [x] Independent De Felice regression and diagnosis of missing gravity pair.
- [x] **T1a** — dust+dust Candidate-C comparison.
- [x] **T1b** — primary-source audit.
- [ ] **T1c — reproduce Comelli Case-C B.5 on the dynamically on-shell branch.** IN PROGRESS.
  - [x] reject off-shell/frozen-a benchmarks;
  - [x] derive exact dynamic `xi(a)` and conformal-time map;
  - [x] establish singular Fredholm structure;
  - [x] audit full spatial equations before slip;
  - [x] establish A.18 rank/index difference;
  - [x] build/test direct 13x11 descriptor audit tool;
  - [x] reject selected minors and frozen-time PGCD;
  - [x] verify leading `Phi1` radiation and `Phi2` dust equations;
  - [x] show descriptor chains with dynamically promoted `B1` do not reproduce the two-dimensional B.5 gravity space;
  - [ ] **T1c.6e — eliminate nondynamical `B1` algebraically before dynamics.** Start with exact Case C and the printed equation organization used in the paper; then repeat with the derived-prime interpretation as a cross-check.
  - [ ] **T1c.6f — derive the reduced three-field system (`E,Phi1,Phi2`) and recover exact B.5 for the pure-E Case-C mode.**
  - [ ] **T1c.6g — choose the physically consistent A.18 bookkeeping by B.5 + three-scalar degree count + Bianchi consistency.**
  - [ ] verify B.5 under Bianchi-redundant row representatives.
- [ ] **T2** — apply validated reduction to dust+dust Candidate C; recover De Felice speed.
- [ ] **T3** — identify exact structural error in old 12x12 closure and replace it.
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

**Resume at T1c.6e — nondynamical `B1` elimination.**

1. Use the exact Case-C background from `numerics/comelli_case_c.py`.
2. Start from the full direct Comelli scalar equations, not the old 12x12 acceleration closure.
3. Treat `B1`, `Psi1`, `Psi2` and matter constraint variables as algebraic/nondynamical whenever the published reduction does; do **not** introduce `B1'` as an independent state.
4. Eliminate matter perturbations through `00/0i` + conservation consistently, then eliminate `F1/F2` with A.17/A.18 and solve `B1` algebraically.
5. Reduce to the three physical scalar fields `E,Phi1,Phi2` and test the pure-E Case-C sector.
6. Acceptance is exactly `E''+(3/tau)E'-(2/3)k^2E=0`, equivalently `x^2e''+7xe'+8e-(2/3)x^2e=0`.
7. Test printed A.18 first because it is the organization used in the published appendix; repeat the derived-prime bookkeeping only as a cross-check.
8. Never tune coefficients or signs merely to hit B.5.
9. Update this checkpoint after every hard ruling.
10. Move to T2 only after B.5 is recovered.
