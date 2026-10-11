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
- The complete primary-source A.12/A.16 spatial equations were checked **before** slip reduction. Each contains an anisotropic block plus a pure-trace block. JANUS slips are exactly the vanishing of those anisotropic brackets, so the post-slip trace equations are not missing an explicit spatial-gradient term.
- Primary Comelli A.16 really has the positive f-sector trace interaction block in Comelli's variables. An opposite sign seen in an independent Lagos-Ferreira formulation is convention-dependent and is not evidence for changing JANUS.
- A.17 is algebraically valid; do not remove it to improve a determinant.
- A.18 has a real notation/typography issue. Raw gauge-invariant definitions give `Xi2-c^2 Xi1 = calB1-calE'`, hence `(calB1-calE')`, while the printed appendix shows `(calB1-calE)`.
- **A.18 changes constraint rank.** On `H_omega=cH`, for variables `[E',Phi1',Phi2',B1,B2,F1,F2]`, the seven constraint/identity equations have rank 6 with derived `(B1-E')`, but rank 7 with printed `(B1-E)` for generic `c!=1`. The printed-form determinant is proportional to `H^3 a^4 c^2 f2^2 m^4 (c-1)/(kappa xi^2)`.
- Therefore declaring `E'` freely dynamical is justified only in the derived-prime organization and must not be assumed while auditing the printed system.
- Comelli Appendix B.2 explicitly contains the missing helicity-0 gradient. For `w1=1/3`, `w2=0`, `a2=a3=0`, `f1=f2`, B.5 reduces sub-horizon to
  `E'' + (3/tau) E' - (2/3) k^2 E = 0`,
  so the benchmark dispersion must contain `q^2=2/3` (`3q^2-2`).

### Old JANUS closure failure

- The old closure is built on the derived-prime A.18 and rank-6-at-fixed-`E'` assumption.
- It passes residual, linearity and held-out `f00` Bianchi tests but fails physical mode content.
- Candidate C at `a=0.5`, `k=0.5 h/Mpc` recovers radiation speed exactly `1/sqrt(3)`, proving k/time normalization.
- Its supposed gravity pair is only `c~0.0159`, versus independent De Felice `c_s~0.8319`.
- Dust+dust Candidate C gives the same spurious pair.
- As k grows, the faulty frequency tends to `omega~23.894 H0`, so speed falls as `1/k`; reconstructed `E''` tends to a constant coefficient ~`-571`, not `-c_s^2 k^2`.
- Swapping differentiated `g00/f00`, varying individual background derivatives, dropping in printed vs derived A.18 inside the same closure, isolated f-trace sign flip, and 80-digit solving do not repair it.

## Dynamically on-shell Comelli Case-C benchmark

Use `8piG=kappa=m^2=a1=1`, `a0=a2=a3=a4=0`, `w1=1/3`, `w2=0`, with

- `rho1 = 3/a^4`,
- `rho2 = 3/(a xi)^3`.

Exact branch relation:

`a^4 xi^2 + xi - a - a^4/3 = 0`,

positive root

`xi(a) = [-1 + sqrt(1 + 4 a^5 + (4/3) a^8)] / (2 a^4)`.

Early-time series:

- `xi(a) = a + a^4/3 - a^6 - (2/3)a^9 + ...`;
- `a' = sqrt(1+a^4 xi)`;
- `tau(a) = a - a^6/12 - a^9/54 + 7a^11/88 + ...`;
- `a(tau) = tau + tau^6/12 + tau^9/54 - 5tau^11/132 + ...`;
- `xi(tau) = tau + tau^4/3 - 11tau^6/12 - 29tau^9/54 + ...`.

Leading physical background:

`a~tau`, `xi~tau`, `H~1/tau`, `H_omega~2/tau`, `rho1~3/tau^4`, `rho2~3/tau^6`, `c->2`.

The older fixed-`xi` family and frozen-`a`, `xi=epsilon` family are diagnostic only; they are not dynamically on-shell Case-C trajectories.

## Descriptor / DAE findings

- Differential/Fredholm work on the dynamic Case-C hierarchy shows a gravitational nullspace and singular compatibility structure; naive local WKB substitution before elimination is not decisive.
- Differential elimination inside the old state organization still fails for both A.18 variants, motivating a descriptor treatment with no prescribed `E'`.
- **New T1c.6c implementation:** `numerics/comelli_descriptor.py` now represents the published scalar problem directly as a rectangular polynomial differential operator
  `P(s)=P0+sP1+s^2P2`, with **13 equations x 11 variables**:
  `[E,Phi1,Phi2,B1,B2,F1,F2,delta_rho1,u1,delta_rho2,u2]`.
- No variable is declared dynamical in this descriptor. Both `derived_prime` and `printed_unprime` A.18 variants are retained explicitly.
- `tests/test_comelli_descriptor.py` was committed before the implementation. Local verification of the implemented polynomial gives `max|P(s)x-direct_residual| = 5.55e-17` on the synthetic regression state. The A.18 variant-difference regression also matches analytically.
- Naive generalized eigenvalues of arbitrary 11-row square submatrices are **not physical evidence**. At very large `k/H`, some minors that omit A.17 approach the expected Case-C root `q~sqrt(2/3)`, but their null vectors develop huge cancelling `F1/F2` amplitudes and do not satisfy the full 13-row system. This reproduces the earlier warning that selected minors can fake the desired dispersion.
- Therefore T1c.6c is only partly complete: the rectangular polynomial is built and algebraically checked, but its **Kronecker/descriptor structure, hidden constraints, normal rank/minimal indices and common finite modes** are still to be determined using the full row space with physically motivated row/column scaling.

## Rejected / resolved hypotheses

- k/time-unit normalization error — rejected.
- visible dust+radiation mixture — rejected.
- differentiated `g00` vs `f00` choice — rejected.
- one bad background derivative — rejected.
- De Felice normalization/transcription error — rejected.
- simple A1/A2 typo — rejected by primary-source audit.
- omitted anisotropic/spatial-gradient block after slip reduction — rejected.
- isolated f-trace interaction-sign flip — rejected as sufficient repair.
- floating-point conditioning — rejected.
- Bianchi residuals as proof of physical mode content — rejected.
- selected high-k minor as dispersion relation — rejected.
- A.18 prime/unprime as a simple drop-in fix to old closure — rejected; structural ambiguity remains open because ranks differ.
- fixed-`xi` or frozen-`a` Case-C asymptotic families as physical trajectories — rejected.

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
    - [ ] **T1c.6c — full descriptor analysis.**
      - [x] build direct 13x11 quadratic polynomial matrix;
      - [x] add regression tests and verify polynomial reconstruction locally;
      - [x] reject isolated square-minor roots as physical modes;
      - [ ] compute robust normal rank / left-right minimal indices / hidden algebraic constraints for both A.18 variants;
      - [ ] extract only finite modes common to the full rectangular system and check physical scalar degree count.
    - [ ] T1c.6d — use validated descriptor structure for differential elimination; acceptance B.5 and `3q^2-2`.
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

**Resume at T1c.6c — descriptor structure.**

1. Read `numerics/comelli_descriptor.py` and `tests/test_comelli_descriptor.py` first.
2. Use the dynamically on-shell Case-C branch above.
3. Analyze the full 13x11 polynomial matrix; do not infer physics from one 11x11 row subset.
4. Introduce physically motivated variable scales (`E~tau^2`, `B/u~tau`, `Phi/F/density-contrast~O(1)`) and corresponding row equilibration before numerical rank judgments.
5. Determine normal rank, left/right minimal indices, hidden algebraic constraints / DAE index, and finite generalized modes for both A.18 variants.
6. A physical formulation must reproduce the expected scalar degree count, Comelli B.5 and later De Felice; do not choose A.18 by desired outcome alone.
7. Only after descriptor structure is fixed perform differential elimination to `E_N=E/tau^2`, then take sub-horizon/WKB limit.
8. Acceptance remains B.5 and `3q^2-2` on Case C.
9. Do not delete A.17, tune coefficients, or change signs to fit the target.
10. Update this file after every hard ruling; then move to T2 only after B.5 is recovered.
