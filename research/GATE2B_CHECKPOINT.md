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
- A.18 is genuinely ambiguous: raw gauge-invariant definitions give `(calB1-calE')`, printed appendix gives `(calB1-calE)`.
- A.18 changes descriptor rank: derived-prime gives rank 6 for the seven constraint/identity equations at fixed background; printed-unprime gives rank 7 for generic `c!=1`.
- Appendix B.2 proves the missing helicity-0 gradient exists. For `w1=1/3`, `w2=0`, `a2=a3=0`, `f1=f2`, B.5 reduces to `E''+(3/tau)E'-(2/3)k^2E=0` sub-horizon.
- With `E=tau^2 e(x)`, `x=k tau`, the acceptance operator is exactly
  `x^2 e_xx + 7x e_x + 8e - (2/3)x^2 e = 0`.
  Only after recovering this may one take high-x/WKB and read `3q^2-2`.

### Old closure failure

- Candidate C at `a=0.5`, `k=0.5 h/Mpc`: radiation pair is exactly `1/sqrt(3)` but the second pair is only `c~0.0159` versus De Felice `c_s~0.8319`.
- Dust+dust gives the same spurious pair.
- As k increases, the faulty frequency tends to `omega~23.894 H0`; apparent speed falls as `1/k`, so the `k^2 E` gravity gradient is structurally absent.
- Ruled out as fixes: dust/radiation mixture, `d(g00)` vs `d(f00)`, individual background derivatives, simple A1/A2 typo, isolated f-trace sign flip, double precision/conditioning, De Felice normalization, and dropping in the alternate A.18 inside the same old closure.

## Exact dynamically on-shell Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`, `rho1=3/a^4`, `rho2=3/(a xi)^3`.

Exact branch:
`a^4 xi^2 + xi - a - a^4/3 = 0`.

Positive root:
`xi(a)=[-1+sqrt(1+4a^5+(4/3)a^8)]/(2a^4)`.

Early time:
`a~tau`, `xi~tau`, `H~1/tau`, `H_omega~2/tau`, `rho1~3/tau^4`, `rho2~3/tau^6`, `c->2`.

### Executable benchmark now in Git

- `numerics/comelli_case_c.py` implements the exact branch, implicit `xi_a/xi_aa`, exact on-shell background derivatives, and dimensionless k.
- It now also implements exact conformal time
  `tau(a)=integral_0^a da/sqrt(1+a^4 xi(a))`
  by Gauss-Legendre quadrature, monotonic inversion `a(tau)`, and `case_c_background_from_tau`.
- It implements the scaled derivative identities
  `D_tau[tau^p f(k tau)] = tau^(p-1)(p+x d_x)f` and
  `D_tau^2[tau^p f] = tau^(p-2)(p-1+x d_x)(p+x d_x)f`.
- `tests/test_comelli_case_c.py` pins branch residual, `c->2`, `H a->1`, `f1=f2=xi`, dimensionless k, conformal-time series/inversion, and scaled derivatives.
- Verification performed locally: original benchmark tests **3/3 passed**; conformal-map test gives zero displayed series error at `a=1e-2` and inversion error `~1.7e-18`.
- Commit trail: test `0e9de06`, k-interface correction `40a270f`, benchmark implementation `e33a376`, conformal-map RED `036381c`, conformal-map implementation `3ddf3f5`.

## Descriptor / DAE findings

- `numerics/comelli_descriptor.py` keeps the direct system rectangular: 13 equations x 11 variables, quadratic in a frozen commuting derivative only as an audit representation.
- `tests/test_comelli_descriptor.py` verifies exact reconstruction and keeps both A.18 variants distinct.
- Arbitrary 11-row minors are not physical evidence; some show `q~sqrt(2/3)` while their null vectors fail the full 13-row system.
- Frozen-time `D_tau->s`/PGCD is insufficient because variable-coefficient Bianchi identities are differential-operator identities; freezing before elimination destroys ordering/hidden constraints.
- Correct asymptotic variable: `x=k tau`. Preserve `D_tau=partial_tau+(x/tau)partial_x` through elimination.
- Natural first weights: `E=tau^2 e(x)`, shifts/velocity potentials `~tau`, `Phi/F/density contrasts~O(1)`.
- The leading normalized hierarchy has a gravitational right kernel. E dynamics appears only through higher-order Fredholm compatibility.
- A previous hand reduction set homogeneous kernel amplitudes to zero too early and produced the wrong ODE. Reject that procedure.
- Derived-prime and printed-unprime A.18 enter at different hierarchy orders and must be treated as separate descriptor-index chains.

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

## Active task list

- [x] Convention bridge and Candidate-C background.
- [x] Scalar constraints/identities and acceleration layer.
- [x] Old 12x12 closure + Bianchi diagnostics.
- [x] Independent De Felice regression and diagnosis of missing gravity pair.
- [x] **T1a** — dust+dust Candidate-C comparison.
- [x] **T1b** — primary-source audit.
- [ ] **T1c — reproduce Comelli Case-C B.5 on the dynamically on-shell branch.** IN PROGRESS.
  - [x] reject off-shell/frozen-a benchmarks;
  - [x] derive exact dynamic `xi(a)` and early-time series;
  - [x] establish singular Fredholm structure;
  - [x] audit full spatial equations before slip;
  - [x] establish A.18 rank/index difference;
  - [x] build/test direct 13x11 descriptor audit tool;
  - [x] reject selected minors and frozen-time PGCD;
  - [x] identify `x=k tau`, `E=tau^2e(x)`, natural weights;
  - [x] codify/test exact Case-C branch, `tau(a)`, `a(tau)`, and scaled derivative operator;
  - [ ] **T1c.6c-derived** — retain all leading kernel amplitudes and compute Laurent/operator left-right compatibility order by order for derived-prime A.18;
  - [ ] **T1c.6c-printed** — repeat for printed-unprime A.18;
  - [ ] choose physical descriptor chain only by B.5 + degree count + Bianchi consistency;
  - [ ] **T1c.6d** — eliminate to `e(x)` and recover exactly `x^2e''+7xe'+8e-(2/3)x^2e=0`;
  - [ ] verify under Bianchi-redundant row representatives.
- [ ] **T2** — apply validated reduction to dust+dust Candidate C; recover De Felice speed.
- [ ] **T3** — identify exact structural error in old 12x12 closure.
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

**Resume at T1c.6c-derived.**

1. Use `case_c_background_from_tau`; do not approximate `a=tau` inside the operator hierarchy.
2. Keep `x=k tau` and the non-commuting scaled derivative operator explicit.
3. Retain every leading right-kernel amplitude until left-kernel/Fredholm compatibility fixes it.
4. Build Laurent/operator coefficients order by order in tau; allow correction orders demanded by the equations.
5. Finish derived-prime A.18 first, then repeat printed-unprime separately.
6. Acceptance is the exact normalized B.5 operator, then `3q^2-2` at high x.
7. Never delete A.17, tune coefficients, or change physical signs merely to hit the target.
8. Update this checkpoint after each hard ruling.
9. Move to T2 only after B.5 is recovered.
