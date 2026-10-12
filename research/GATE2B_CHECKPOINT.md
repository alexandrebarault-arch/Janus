# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **single restart point after any interruption**. Read this file first. Update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The Candidate-C background/convention bridge is under control. The old 12x12 scalar closure is algebraically consistent but removes the physical helicity-0 gradient, so it must not be used for transfer/segregation conclusions.

The direct Comelli reconstruction has now been index-reduced correctly enough to establish the constraint count and Bianchi structure, but the transcribed system still fails the published Case-C B.5 gravity equation. The active route is therefore an **independent scalar-action reconstruction from De Felice 1404.0008 / Lagos-Ferreira 1610.00553**, followed by a term-by-term comparison back to Comelli.

## Hard facts to preserve

### Convention/background bridge

- JANUS -> Comelli/De Felice: `beta_n=n! a_n`, `f2=yJ`, `f1=Gamma`, `xi=y`, `kappa=alpha^2`, `c=ctilde`.
- De Felice Eq. (27), `2(c-1)W = rho_g - c xi^2 rho_f/kappa`, matches JANUS at ~`2e-14` relative on the dust+dust comparison point.
- De Felice high-k gravity speed agrees with `flrw_two_matter.py::diagnostics()['scalar_cs2']`.

### A.3 / A.18 prime issue — CLOSED FOR INTERNAL BOOKKEEPING

- The PDFs of arXiv:1202.1986 Appendix A.3 and arXiv:1403.5679 A.18 **print** `(calB1-calE)`.
- Raw gauge-invariant definitions in arXiv:1202.1986 Eqs. (4.6)-(4.7) give `calE=E1-E2`, `Xi1=B1_raw+E1'`, `Xi2=B2_raw+E2'`, and `calB1=B2_raw-c^2 B1_raw+(1-c^2)E1'`.
- Direct substitution gives exactly `Xi2-c^2 Xi1 = calB1-calE'`; therefore the printed A.3/A.18 is internally inconsistent with the paper's own definitions.
- `tests/test_comelli_bridge.py::test_additional_gauge_invariants_follow_raw_definitions_not_a3_typo` pins this relation; `numerics/comelli_bridge.py` uses `E'`.
- Independent differential/Bianchi test on the exact Case-C background confirms the same ruling: derived-prime A.18 satisfies the held compatibility at relative ~`1e-11`–`1e-13` on random states, whereas printed-unprime typically violates it at ~`1e-4`–`1e-6` at finite tau. The printed error is asymptotically suppressed as tau->0, which explains earlier apparent equivalence.
- Keep printed-unprime only as a typo/control branch; do not use it as the physical constraint chain.

### Published scalar dynamics

- Comelli A.7-A.16, slips, A.17, and A1/A2 identities were independently re-audited.
- Full A.12/A.16 were checked before slip reduction; no explicit spatial-gradient block was dropped.
- A1/A2 identities were also rederived directly from the raw invariants. With `Q=Xi2-c^2Xi1=calB1-calE'`, they reproduce the implemented A1/A2 sum/difference including B1', E', E'', c', H and H_omega terms.
- Appendix B.2 proves the helicity-0 gradient exists. For `w1=1/3`, `w2=0`, `a2=a3=0`, `f1=f2`, B.5 reduces sub-horizon to `E''+(3/tau)E'-(2/3)k^2E=0`.
- With `E=tau^2 e(x)`, `x=k tau`, the acceptance operator is exactly `x^2 e_xx + 7x e_x + 8e - (2/3)x^2 e = 0`.
- The 2014 reduction states that `B1` and `Psi1/2` are nondynamical and can be expressed through `E,Phi1,Phi2`; only those three obey second-order scalar evolution equations.
- Leading Case-C equations already recover the visible-radiation `Phi1` mode and twin-dust `Phi2` mode. The missing mode is specifically the gravitational `E` mode.

### Old JANUS closure failure

- Candidate C at `a=0.5`, `k=0.5 h/Mpc`: radiation pair is exactly `1/sqrt(3)`, but the second pair is only `c~0.0159` versus De Felice `c_s~0.8319`.
- Dust+dust gives the same spurious pair.
- As k increases, faulty frequency tends to `omega~23.894 H0`; apparent speed falls as `1/k`, proving the physical `k^2 E` term is structurally absent.
- Ruled out as fixes: dust/radiation mixture, differentiated g00 vs f00, individual background derivatives, simple A1/A2 typo, isolated f-trace sign flip, floating-point conditioning, De Felice normalization, and merely swapping closure rows.
- The old 12x12 organization promotes `B1'` as an acceleration unknown even though the published reduction treats `B1` as nondynamical. This is structurally undesirable but is not by itself the whole cause.

## Exact dynamically on-shell Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`, `rho1=3/a^4`, `rho2=3/(a xi)^3`.

Exact branch: `a^4 xi^2 + xi - a - a^4/3 = 0`.

Positive root: `xi(a)=[-1+sqrt(1+4a^5+(4/3)a^8)]/(2a^4)`.

Early-time conformal series:
- `a=tau+tau^6/12+tau^9/54-5tau^11/132+...`;
- `xi=tau+tau^4/3-11tau^6/12-29tau^9/54+...`;
- `H=1/tau+O(tau^4)`, `H_omega=2/tau+O(tau^2)`, `c=2+tau^3+O(tau^5)`;
- `rho2~tau^-6`, so apparently subleading background corrections can contribute at the same order as induced `Phi2~tau^3`.

### Executable benchmark

- `numerics/comelli_case_c.py` implements exact `xi(a)`, derivatives, exact conformal map `tau(a)`, inversion `a(tau)`, and `case_c_background_from_tau`.
- It preserves `D_tau[tau^p f(k tau)] = tau^(p-1)(p+x d_x)f`.
- `tests/test_comelli_case_c.py` pins the exact branch, conformal map and derivative identities.

## Descriptor / DAE findings

- `numerics/comelli_descriptor.py` keeps the direct system rectangular: 13 equations x 11 variables. It is an audit representation, not the physical reduced ODE.
- Arbitrary square minors and frozen-time `D_tau->s`/PGCD are rejected as physical mode criteria because Bianchi identities are differential-operator identities.
- Correct asymptotic variable is `x=k tau`; preserve `D_tau=partial_tau+(x/tau)partial_x` during elimination.
- Natural pure-gravity weights are `E=tau^2 e(x)`, induced `Phi2~tau^3`, induced `Phi1~tau^5`, with shifts/matter variables determined by constraints.
- Setting homogeneous kernel amplitudes to zero before Fredholm compatibility produces false reduced equations; do not repeat this.

### Correct index reduction / new hard findings

- A GR radiation control validates the method “solve 00/0i constraints -> differentiate constraint solutions -> impose conservation + trace”: all remaining equations reduce to `Phi''+4 Phi'/tau+(k^2/3)Phi=0` exactly.
- In full Case C, treat `B1` as an algebraic parameter and form the acceleration system only for `(B1',E'',Phi1'',Phi2'')`. Its left-nullspace has dimension 2.
- The two left-null compatibility conditions give the **same algebraic B1** (agreement ~`1e-9` in the numerical checks); the second combination is the expected Bianchi redundancy. This reproduces the published nondynamical count for B1.
- Example scaling on an E-basis state: `B1~6/tau` (`~60` at tau=.1, `~200` at .03, `~600` at .01, `~2000` at .003).
- After this correct index reduction and exact on-shell background, the local six-dimensional physical Jacobian `[E,Phi1,Phi2,E',Phi1',Phi2']` still contains the correct radiation pair but **no** gravitational pair `±sqrt(2/3) k`.
- At fixed `x=k tau=100`, the E equation behaves approximately as `(E''/E)/k^2 ~ -3/x^2` and `E''/(E' k) ~ -6/x`, i.e. power-law/Hubble dynamics rather than B.5's `+(2/3)k^2 E` gradient.
- Similarity-rescaling by the natural asymptotic weights does not change the spectrum. The missing helicity-0 mode is not a conditioning artifact.
- Equation-removal localization shows the g-Euler/g-trace redundancy behaves as Bianchi expects, while removing f-trace changes E'' strongly and leaves a large omitted residual. The f-sector spatial interaction is where the missing gradient is fixed/killed in the transcribed system.
- Decomposing f-trace on a pure-E basis shows large cancellations between `(2 c f1 F2)` and `(f2 A2)`, and separately between `-2 Phi2''` and `2 H_omega Psi2'`, leaving no `k^2 E` term.
- Flipping the signs of `2 c f1 F2`, `f2 A2`, or both, one at a time in scratch, **never** restores the `sqrt(2/3) k` gravity mode. Therefore the fault is not a simple local sign typo in A.16.

## Rejected / superseded hypotheses

- k/time normalization error.
- visible dust+radiation mixture.
- differentiated g00 vs f00 closure choice.
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
- printed A.18 as physical simply because it appears twice; raw definitions + Bianchi select `E'`.
- eliminating B1' alone as a sufficient repair; correct index reduction still misses B.5.
- simple sign reversal of either/both f-trace interaction subterms as sufficient repair.

## Active task list

- [x] Convention bridge and Candidate-C background.
- [x] Scalar equations / old closure audit.
- [x] Independent De Felice regression and diagnosis of missing gravity pair.
- [x] **T1a** — dust+dust Candidate-C comparison.
- [x] **T1b** — primary-source audit.
- [x] **T1b.1** — derive A.3 from raw gauge invariants; internal identity uses `E'`; printed A.3/A.18 retained only as typo diagnostic.
- [ ] **T1c — reproduce/replace the Comelli Case-C scalar reduction with an independently validated system.** IN PROGRESS.
  - [x] reject off-shell/frozen-a benchmarks;
  - [x] derive exact dynamic `xi(a)` and conformal-time map;
  - [x] establish singular Fredholm structure;
  - [x] audit full spatial equations before slip;
  - [x] build/test direct 13x11 descriptor audit tool;
  - [x] reject selected minors and frozen-time PGCD;
  - [x] verify leading `Phi1` radiation and `Phi2` dust equations;
  - [x] identify induced pure-E scalings `Phi2~tau^3`, `Phi1~tau^5`;
  - [x] **T1c.6k.1** — validate constraint-differentiation reduction against exact GR radiation control;
  - [x] **T1c.6k.2** — show derived-prime A.18 is Bianchi-compatible and printed-unprime is not at finite tau;
  - [x] **T1c.6k.3** — index-reduce B1 algebraically via left-null compatibility; reproduce 3 second-order physical-field count;
  - [x] **T1c.6k.4** — show correctly index-reduced Comelli transcription still misses B.5 while keeping radiation correct;
  - [x] **T1c.6k.5** — reject simple f-trace subterm sign flips;
  - [ ] **T1c.6o — independent quadratic-action reconstruction from De Felice 1404.0008 and/or Lagos-Ferreira 1610.00553.** Extract the scalar constraint-elimination/action matrices without relying on Comelli Appendix A; reproduce the known gravity `c_s^2` first, then retain enough lower-k structure for the native solver.
  - [ ] **T1c.6p — compare the independent action-derived principal/reduced equations term-by-term with Comelli to identify the missing interaction structure.**
  - [ ] **T1c.6q — Case-C acceptance: recover exactly `E''+(3/tau)E'-(2/3)k^2E=0` or demonstrate precisely why the action variables map to an equivalent equation.**
  - [ ] verify result under Bianchi-redundant row representatives.
- [ ] **T2** — apply independently validated reduction to dust+dust Candidate C and recover De Felice speed.
- [ ] **T3** — identify exact structural error(s) in old 12x12 closure and replace them.
- [ ] **T4** — implement corrected `numerics/comelli_native_scalar.py` or a clearly named action-based replacement.
- [ ] **T5** — make `tests/test_comelli_native_scalar.py` green + >=3 extra `(z,k)` regressions.
- [ ] **T6** — full Gate-2B regression suite.
- [ ] **T7** — time-domain transfer RHS + fundamental matrix.
- [ ] **T8** — continuous GR-connected/adiabatic mode tracking.
- [ ] **T9** — compute `T_gg,T_gf,T_fg,T_ff` and relative-mode growth.
- [ ] **T10** — Gate-2B verdict with tolerances/domain.

## Current RED regression

`tests/test_comelli_native_scalar.py` still imports the intentionally absent `numerics/comelli_native_scalar.py`. Do not implement around it until T1c is independently closed.

## Immediate restart instruction

**Resume at T1c.6o — independent scalar action.**

1. Inspect De Felice et al. arXiv:1404.0008 scalar quadratic action, especially the constraint elimination and equations around the kinetic/gradient matrices and Eq. ~86 propagation speeds.
2. If full matrices are not printed, inspect Lagos & Ferreira arXiv:1610.00553 massive-bigravity specialization of the general bimetric quadratic action.
3. Build an independent action-derived scalar principal/reduced system on the JANUS background map; first acceptance is the already-known De Felice gravitational `c_s^2`.
4. Then apply it to exact Case C and require equivalence to B.5 / `sqrt(2/3)k`.
5. Only after this independent system passes should it be compared term-by-term against Comelli to identify the missing structure in the transcribed direct equations.
6. Keep `research/GATE2B_CHECKPOINT.md` updated after each hard finding.
7. Move to T2 only after the action-derived system is validated.
