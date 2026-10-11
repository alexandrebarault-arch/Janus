# Gate 2B — persistent checkpoint and restart plan

Date: 2026-10-12
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: **single restart point after any interruption**. Read this file first. Update it after every hard finding, rejected hypothesis, task-state change, or restart-point change.

## Scientific goal

Close Gate 2B: compute the full non-homothetic scalar transfer of Candidate C from published ghost-free bigravity equations. No Candidate-C transfer or segregation result is scientifically interpretable until the implementation independently reproduces the published high-k helicity-0 propagation.

## Current verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The Candidate-C background/convention bridge is under control. The old 12x12 perturbation closure is algebraically consistent but removes the physical helicity-0 gradient and must not be used for physics conclusions.

## Hard facts

### Background / conventions

- JANUS -> Comelli/De Felice: `beta_n=n! a_n`, `f2=yJ`, `f1=Gamma`, `xi=y`, `kappa=alpha^2`, `c=ctilde`.
- `numerics/candidate_c_transfer.py` maps Candidate C to perturbation conventions.
- De Felice background Eq. (27), `2(c-1)W = rho_g - c xi^2 rho_f/kappa`, matches JANUS at ~`2e-14` relative on the dust+dust comparison point.
- The independent De Felice high-k scalar-speed target agrees with `flrw_two_matter.py::diagnostics()['scalar_cs2']`.

### Published scalar equations

- Comelli matter conservation A.7-A.9, Einstein scalar equations A.10-A.16, slips, A.17, and the A1/A2 auxiliary identities have been independently re-audited.
- The complete A.12/A.16 equations were checked before slip reduction. The anisotropic brackets vanish exactly under the JANUS slip relations, so no explicit spatial-gradient block was accidentally dropped there.
- Primary Comelli A.16 has the positive f-sector trace interaction block in Comelli conventions. Flipping only this sign in scratch changes the spurious speed from ~`0.01594` to ~`0.01557`, not to the De Felice value; this is not the fix.
- A.17 is algebraically valid and must not be removed to improve a determinant.
- A.18 has a genuine notation/typography ambiguity. Raw gauge-invariant definitions give `(calB1-calE')`; the printed appendix shows `(calB1-calE)`.
- A.18 changes constraint rank. On `H_omega=cH`, the seven constraint/identity equations have rank 6 with derived-prime A.18 but rank 7 with printed-unprime A.18 for generic `c!=1`.
- Comelli Appendix B.2 explicitly contains the missing helicity-0 gradient. For `w1=1/3`, `w2=0`, `a2=a3=0`, `f1=f2`, B.5 reduces sub-horizon to `E'' + (3/tau)E' - (2/3)k^2 E = 0`.
- With `E=tau^2 e(x)` and `x=k tau`, the exact acceptance operator is `x^2 e_xx + 7x e_x + 8e - (2/3)x^2 e = 0`; only after recovering this should one take the high-x/WKB factor `3q^2-2`.

### Old JANUS closure failure

- The old closure is built on derived-prime A.18 and a rank-6-at-fixed-`E'` organization.
- It passes residual, linearity and held-out Bianchi checks but fails physical mode content.
- Candidate C at `a=0.5`, `k=0.5 h/Mpc` recovers radiation speed exactly `1/sqrt(3)`, proving k/time normalization.
- Its second oscillatory pair is only `c~0.0159`, versus independent De Felice gravity speed `c_s~0.8319`.
- Dust+dust Candidate C gives the same spurious pair.
- As k grows, the faulty frequency tends to `omega~23.894 H0`, so speed falls as `1/k`; reconstructed `E''` approaches a constant coefficient ~`-571`, not `-c_s^2 k^2`.
- Swapping differentiated `g00/f00`, varying individual background derivatives, printed vs derived A.18 inside the same closure, isolated f-trace sign flip, and 80-digit solving do not repair it.

## Dynamically on-shell Comelli Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`, with `rho1=3/a^4`, `rho2=3/(a xi)^3`.

Exact branch:

`a^4 xi^2 + xi - a - a^4/3 = 0`.

Positive root:

`xi(a)=[-1+sqrt(1+4a^5+(4/3)a^8)]/(2a^4)`.

Early time:

- `xi(a)=a+a^4/3-a^6-(2/3)a^9+...`;
- `a'=sqrt(1+a^4 xi)`;
- `a~tau`, `xi~tau`, `H~1/tau`, `H_omega~2/tau`, `rho1~3/tau^4`, `rho2~3/tau^6`, `c->2`.

### Executable benchmark added

- `numerics/comelli_case_c.py` now codifies the exact positive root, implicit first/second derivatives, exact on-shell background coefficients, and the scaled derivative identity for `tau^p f(k tau)`.
- `tests/test_comelli_case_c.py` pins the exact branch residual, the early-time `c->2`, `H a->1` behavior, `f1=f2=xi`, dimensionless `k`, and the operator formulas
  `D_tau[tau^p f]=tau^(p-1)(p+x d_x)f` and
  `D_tau^2[tau^p f]=tau^(p-2)(p-1+x d_x)(p+x d_x)f`.
- Targeted local reconstruction/run: **3 tests passed**.
- Commit trail: RED test `0e9de06`, interface correction `40a270f`, GREEN implementation `e33a376`.

## Descriptor / DAE findings

- `numerics/comelli_descriptor.py` represents the direct scalar problem as a rectangular `13 equations x 11 variables` quadratic frozen-coefficient polynomial audit tool; no variable is declared dynamical a priori.
- `tests/test_comelli_descriptor.py` verifies exact reconstruction and keeps both A.18 variants distinct.
- Arbitrary square 11-row subsets are not physical evidence. Some minors can show `q~sqrt(2/3)` while their null vectors fail the full 13-row system.
- Frozen-time replacement `D_tau->s` before elimination is insufficient because variable-coefficient Bianchi identities are differential-operator identities; operator ordering and hidden constraints are lost.
- The correct asymptotic variable is `x=k tau`. Preserve `D_tau=partial_tau+(x/tau)partial_x` through elimination.
- Natural first weights: `E=tau^2 e(x)`, shifts/velocity potentials `~tau`, `Phi/F/density contrasts~O(1)`.
- The leading normalized 13-equation hierarchy has a gravitational kernel; E dynamics appears only through higher-order Fredholm compatibility.
- A previous hand elimination that set homogeneous matter/metric kernel amplitudes to zero too early produced the wrong equation. This is rejected; all kernel amplitudes must survive until compatibility fixes them.
- Printed-unprime and derived-prime A.18 enter at different orders, so they must be treated as separate descriptor-index chains.

## Rejected / resolved hypotheses

- k/time normalization error — rejected by exact radiation speed.
- visible dust+radiation mixture — rejected by dust+dust comparison.
- differentiated `g00` vs `f00` choice — rejected.
- one bad background derivative — rejected.
- De Felice normalization/transcription error — rejected.
- simple A1/A2 typo — rejected by primary-source audit.
- omitted anisotropic gradient block after slip — rejected.
- isolated f-trace interaction-sign flip — rejected.
- floating-point conditioning — rejected by high-precision solve.
- Bianchi residuals as proof of physical mode content — rejected.
- selected square minor as dispersion relation — rejected.
- frozen-time commuting-PGCD as full descriptor criterion — rejected.
- A.18 prime/unprime as a simple drop-in fix — rejected; structural ambiguity remains because rank/index changes.
- fixed-xi/frozen-a Case-C trajectories — rejected as off-shell.
- setting non-gravity homogeneous kernel amplitudes to zero before Fredholm compatibility — rejected.

## Active task list

- [x] Map JANUS conventions to Comelli/De Felice.
- [x] Implement/test scalar constraints and identities.
- [x] Establish rank-6 constraint manifold for derived-prime A.18.
- [x] Implement/test metric acceleration layer.
- [x] Implement exact Candidate-C background adapter.
- [x] Implement/test old 12x12 closure plus held-out Bianchi diagnostic.
- [x] Add independent De Felice high-k regression.
- [x] Diagnose local 8D modes: radiation correct, helicity-0 missing.
- [x] **T1a** — self-consistent dust+dust Candidate-C comparison.
- [x] **T1b** — primary-source audit of equations and De Felice target.
- [ ] **T1c — Reproduce Comelli Case-C B.5 from direct equations on a dynamically on-shell background.** IN PROGRESS.
  - [x] T1c.1 — reject off-shell/frozen-a asymptotic families.
  - [x] T1c.2 — derive exact dynamic `xi(a)` and early-time series.
  - [x] T1c.3 — verify dynamic background conservation and gravitational kernel.
  - [x] T1c.4 — establish singular Fredholm compatibility structure.
  - [x] T1c.5 — audit full A.12/A.16 before slip; no missing gradient block.
  - [ ] **T1c.6 — recover correct scalar descriptor/DAE structure and derive B.5.**
    - [x] T1c.6a — old-organization differential elimination fails for both A.18 variants.
    - [x] T1c.6b — rank difference: derived-prime 6 vs printed-unprime 7.
    - [ ] **T1c.6c — differential descriptor hierarchy.**
      - [x] direct 13x11 descriptor audit tool + tests;
      - [x] reject isolated square-minor roots;
      - [x] reject frozen-time commuting-PGCD criterion;
      - [x] identify `x=k tau`, `E=tau^2 e(x)` and natural weights;
      - [x] codify/test the dynamically on-shell Case-C background and scaled derivative operator (`comelli_case_c.py`);
      - [ ] retain all leading kernel amplitudes and compute Laurent/operator left-right compatibility order by order for derived-prime A.18;
      - [ ] repeat descriptor-index/compatibility chain for printed-unprime A.18;
      - [ ] select the physically consistent chain only by B.5 + degree count + Bianchi consistency.
    - [ ] T1c.6d — eliminate to `e(x)` with validated chain. Acceptance: `x^2 e''+7xe'+8e-(2/3)x^2e=0`.
  - [ ] T1c.7 — verify B.5 under Bianchi-redundant row representatives and consistent A.18 bookkeeping.
- [ ] **T2 — Apply validated reduction to dust+dust Candidate C and recover De Felice gravity speed.**
- [ ] **T3 — Identify exact structural mistake in old 12x12 closure.**
- [ ] **T4 — Implement corrected `numerics/comelli_native_scalar.py`.**
- [ ] **T5 — Make `tests/test_comelli_native_scalar.py` green and add >=3 `(z,k)` regressions.**
- [ ] **T6 — Re-run all Gate-2B tests; no regression allowed.**
- [ ] **T7 — Build time-domain transfer RHS and fundamental transfer matrix only after T1-T6 pass.**
- [ ] **T8 — Track GR-connected/adiabatic mode continuously.**
- [ ] **T9 — Compute `T_gg,T_gf,T_fg,T_ff` and relative-mode growth.**
- [ ] **T10 — Record Gate-2B pass/fail/inconclusive verdict with tolerances/domain.**

## Current RED regression

`tests/test_comelli_native_scalar.py` still requires the not-yet-created `numerics/comelli_native_scalar.py` and a gravity pair matching De Felice. Do not implement around it until T1c is closed.

## Immediate restart instruction

**Resume at T1c.6c — differential descriptor hierarchy.**

1. Use `numerics/comelli_case_c.py` for the dynamically on-shell benchmark; do not rebuild an approximate/frozen background.
2. Work in `x=k tau` and preserve `D_tau=partial_tau+(x/tau)partial_x`; do not freeze `D_tau->s` before eliminating constraints.
3. Keep all leading right-kernel amplitudes until left-kernel/Fredholm compatibility fixes them. Do not set them to zero by hand.
4. Build coefficient operators order by order in tau with `E=tau^2 e(x)`, `B/u~tau`, `Phi/F/density contrasts~O(1)` and allow correction orders demanded by the equations.
5. Do this separately for derived-prime and printed-unprime A.18 because their constraint chains differ.
6. Acceptance is exactly `x^2 e_xx + 7x e_x + 8e - (2/3)x^2 e = 0` on Case C, then `3q^2-2` at high x.
7. Do not delete A.17, tune coefficients, or change signs to fit the target.
8. Update this file after every hard ruling.
9. Move to T2 Candidate C only after B.5 is recovered.
