# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **single restart point after any interruption**. Read this file first. Update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The Candidate-C background/convention bridge is under control. The old 12x12 scalar closure is algebraically consistent but removes the physical helicity-0 gradient, so it must not be used for transfer/segregation conclusions.

## Hard facts to preserve

### Convention/background bridge

- JANUS -> Comelli/De Felice: `beta_n=n! a_n`, `f2=yJ`, `f1=Gamma`, `xi=y`, `kappa=alpha^2`, `c=ctilde`.
- De Felice Eq. (27), `2(c-1)W = rho_g - c xi^2 rho_f/kappa`, matches JANUS at ~`2e-14` relative on the dust+dust comparison point.
- De Felice high-k gravity speed agrees with `flrw_two_matter.py::diagnostics()['scalar_cs2']`.

### A.3 / A.18 prime issue — CURRENT RULING

- The PDFs of arXiv:1202.1986 Appendix A.3 and arXiv:1403.5679 A.18 **print** `(calB1-calE)`.
- However the raw gauge-invariant definitions in arXiv:1202.1986 Eqs. (4.6)-(4.7) are:
  - `calE = E1-E2`;
  - `Xi1=B1_raw+E1'`, `Xi2=B2_raw+E2'`;
  - `calB1=B2_raw-c^2 B1_raw+(1-c^2)E1'`.
- Direct substitution gives the exact identity
  `Xi2-c^2 Xi1 = calB1-calE'`.
- Therefore the printed A.3/A.18 is internally inconsistent with the paper's own definitions; the algebraically consistent relation contains **`calE'`**.
- This was pinned by `tests/test_comelli_bridge.py::test_additional_gauge_invariants_follow_raw_definitions_not_a3_typo` and implemented in `numerics/comelli_bridge.py` at branch head `0ade047`.
- Do **not** treat the printed unprimed A.18 as physical merely because it appears in both appendices. Keep it only as a historical/diagnostic variant when checking how the typo affects rank/index.

### Published scalar dynamics

- Comelli A.7-A.16, slips, A.17, and A1/A2 identities were independently re-audited.
- Full A.12/A.16 were checked before slip reduction; no explicit spatial-gradient block was dropped.
- Appendix B.2 proves the helicity-0 gradient exists. For `w1=1/3`, `w2=0`, `a2=a3=0`, `f1=f2`, B.5 reduces sub-horizon to
  `E''+(3/tau)E'-(2/3)k^2E=0`.
- With `E=tau^2 e(x)`, `x=k tau`, the acceptance operator is exactly
  `x^2 e_xx + 7x e_x + 8e - (2/3)x^2 e = 0`.
- The 2014 reduction states that `B1` and `Psi1/2` are nondynamical and can be expressed through `E,Phi1,Phi2`; only those three obey second-order scalar evolution equations.
- Leading Case-C equations already recover the visible-radiation `Phi1` mode and twin-dust `Phi2` mode. The missing mode is specifically the gravitational `E` mode.

### Old JANUS closure failure

- Candidate C at `a=0.5`, `k=0.5 h/Mpc`: radiation pair is exactly `1/sqrt(3)`, but the second pair is only `c~0.0159` versus De Felice `c_s~0.8319`.
- Dust+dust gives the same spurious pair.
- As k increases, faulty frequency tends to `omega~23.894 H0`; apparent speed falls as `1/k`, proving the physical `k^2 E` term is structurally absent.
- Ruled out as fixes: dust/radiation mixture, differentiated g00 vs f00, individual background derivatives, simple A1/A2 typo, isolated f-trace sign flip, floating-point conditioning, De Felice normalization, and merely swapping closure rows.
- The old 12x12 organization promotes `B1'` as an acceleration unknown even though the published reduction treats `B1` as nondynamical. Eliminating `B1'` alone on an oversimplified frozen-leading background did not recover B.5, so this is a contributing structural issue rather than a complete fix.

## Exact dynamically on-shell Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`, `rho1=3/a^4`, `rho2=3/(a xi)^3`.

Exact branch:
`a^4 xi^2 + xi - a - a^4/3 = 0`.

Positive root:
`xi(a)=[-1+sqrt(1+4a^5+(4/3)a^8)]/(2a^4)`.

Early-time conformal series:
- `a=tau+tau^6/12+tau^9/54-5tau^11/132+...`;
- `xi=tau+tau^4/3-11tau^6/12-29tau^9/54+...`;
- `H=1/tau+O(tau^4)`, `H_omega=2/tau+O(tau^2)`, `c=2+tau^3+O(tau^5)`;
- `rho2~tau^-6`, so apparently subleading background corrections can contribute at the same order as induced `Phi2~tau^3`.

### Executable benchmark

- `numerics/comelli_case_c.py` implements exact `xi(a)`, derivatives, exact conformal map `tau(a)`, inversion `a(tau)`, and `case_c_background_from_tau`.
- It preserves the scaled derivative operator
  `D_tau[tau^p f(k tau)] = tau^(p-1)(p+x d_x)f`.
- `tests/test_comelli_case_c.py` pins the exact branch, conformal map and derivative identities.

## Descriptor / DAE findings

- `numerics/comelli_descriptor.py` keeps the direct system rectangular: 13 equations x 11 variables. It is an audit representation, not yet the physical reduced ODE.
- Arbitrary square minors and frozen-time `D_tau->s`/PGCD are rejected as physical mode criteria because Bianchi identities are differential-operator identities.
- Correct asymptotic variable: `x=k tau`; preserve `D_tau=partial_tau+(x/tau)partial_x` during elimination.
- Natural pure-gravity weights: `E=tau^2 e(x)`, induced `Phi2~tau^3`, induced `Phi1~tau^5`, with shifts/matter variables determined by constraints.
- Setting homogeneous kernel amplitudes to zero before Fredholm compatibility was shown to produce false reduced equations; do not repeat this.
- The physical hierarchy must use the **derived-prime A.18 from raw definitions**, while the printed-unprime variant may be run only as a typo/control branch.

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
- **Superseded:** "A.3/A.18 physically uses unprimed E because the appendix prints it." Raw definitions prove the internally consistent identity uses `E'`; the printed form is treated as a repeated typo.

## Active task list

- [x] Convention bridge and Candidate-C background.
- [x] Scalar equations / old closure audit.
- [x] Independent De Felice regression and diagnosis of missing gravity pair.
- [x] **T1a** — dust+dust Candidate-C comparison.
- [x] **T1b** — primary-source audit.
- [x] **T1b.1** — derive A.3 from raw gauge invariants; physical/internal identity uses `E'`; printed A.3/A.18 retained only as typo diagnostic.
- [ ] **T1c — reproduce Comelli Case-C B.5 on the dynamically on-shell branch.** IN PROGRESS.
  - [x] reject off-shell/frozen-a benchmarks;
  - [x] derive exact dynamic `xi(a)` and conformal-time map;
  - [x] establish singular Fredholm structure;
  - [x] audit full spatial equations before slip;
  - [x] build/test direct 13x11 descriptor audit tool;
  - [x] reject selected minors and frozen-time PGCD;
  - [x] verify leading `Phi1` radiation and `Phi2` dust equations;
  - [x] identify induced pure-E scalings `Phi2~tau^3`, `Phi1~tau^5`;
  - [ ] **T1c.6k — rebuild the exact-on-shell hierarchy with derived-prime A.18 and eliminate all nondynamical variables (`Psi1/2`, `B1/B2`, `F1/F2`, matter constraints) before introducing any acceleration state.**
  - [ ] **T1c.6l — run the printed-unprime A.18 only as a control branch and record where its rank/index diverges.**
  - [ ] **T1c.6m — reduced three-field acceptance: obtain second-order equations only for `E,Phi1,Phi2`.**
  - [ ] **T1c.6n — pure-E acceptance: recover exactly `E''+(3/tau)E'-(2/3)k^2E=0`, equivalently `x^2e''+7xe'+8e-(2/3)x^2e=0`.**
  - [ ] verify B.5 under Bianchi-redundant row representatives.
- [ ] **T2** — apply validated reduction to dust+dust Candidate C and recover De Felice speed.
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

**Resume at T1c.6k.**

1. Use `case_c_background_from_tau` or exact symbolic series from the same branch.
2. Use the raw-definition-consistent A.18 with `(B1-E')`; keep printed `(B1-E)` only as a control branch.
3. Preserve `x=k tau` and the non-commuting scaled derivative operator during elimination.
4. Eliminate `Psi1/2`, `B1/B2`, `F1/F2`, and matter constraints algebraically/order-by-order before defining the dynamical state.
5. The reduced system must have exactly three second-order scalar equations for `E,Phi1,Phi2`.
6. Pure-E Case-C acceptance is the exact B.5 operator, not only its high-k root.
7. Update this file immediately after every new hard ruling.
8. Move to T2 only after B.5 is recovered.
