# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main`
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc`

Purpose: **first file to read after any interruption**. Update after every hard result, blocker, branch-policy change, or verified diagnostic.

## 0 — Resume in one minute

1. Work only from `research/v2-flrw`.
2. Read this file, then `research/GATE2B_ACTION_RECONSTRUCTION.md`, `research/GATE2B_CHECKPOINT.md`, and `LATEST.md`.
3. Do **not** return to literal published JANUS, the failed direct Comelli closure, coefficient/sign tuning, or blind root scans.
4. The apparent five missing metric-only De Felice Eq. (54) structures are **not** an add-back patch: Lagos' one-matter background reduction absorbs/cancels them.
5. The full frozen quadratic spectral problem including the antisymmetric `qdot*q` matrix was independently reconstructed and still gives the same hard failure: both matter modes propagate correctly but the third scalar frequency saturates instead of `omega ~ k`. The spectral solver is cleared as leading cause.
6. The authoritative route is now the independent raw De Felice two-matter action, not the Lagos one-matter reduced metric block.
7. A2.4d now has source-level raw building blocks and a complete g-flat two-matter density in `numerics/de_felice_raw_scalar_action.py`.
8. Resume at **A3: simultaneous auxiliary elimination**, then measure the rank and high-k characteristics before any production correction.

## 1 — Git / repository state

- `main` — `aead63f4098f0d15a849e579105af034b6317b30`; stable pre-V2 baseline; keep untouched.
- `research/v2-flrw` — canonical active research line; keep.
- `research/gate2b-nonhomothetic-transfer` — `fd430d73ed7e8c4638b6d94ba1c46f54fba3f5b5`; redundant historical branch, fully absorbed by merge `35f5edc19443a059308e8c2710deb656bfdd8fbc`; freeze and delete only when ref deletion is available.
- PR #1 remains draft (`research/v2-flrw` -> `main`). Do not merge as housekeeping and do not interpret it as validation.
- GitHub Actions/workflows remain intentionally disabled.

Latest A2.4d implementation lineage:

- `161ccd7530c844e16de6ecb22e678a29efe102f0` — RED stub for raw Eq. (44) block.
- `0002c9abf44d8d56f1cc787e44c37b6141c28a65` — RED Eq. (44) scalar tests.
- `f3c00a1d255f39e7c9aa18cea97c70dc522ac0da` — GREEN source-level EH scalar contraction.
- `3e589a8acf962ba989a84cfc1d735dd83599c94c` — RED HR Eq. (45)-(46) slices.
- `22d0f59dd62eb077f428f84d17dcda53cff7bce5` — GREEN raw HR quadratic block.
- `eca2b267a9f27943c4614c81a3d2373c504f2941` — RED stub for full raw two-matter assembly.
- `eaf1037823a484835d45f7097542f6953935e38c` — RED g/f volume-normalization tests.
- `731fe693ad6cd4c9eaf0677b8ba06d8888e30f0d` — GREEN full raw g-flat density `EH(g)+EH(f)+HR+matter(g)+matter(f)`.

## 2 — Scientific status

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN / FALSIFICATION-DRIVEN`

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / NOT VALIDATED`

Current blocker: the old Lagos-based two-matter assembly reproduces the two matter characteristics but not the known Hassan-Rosen helicity-0 high-k gravity characteristic.

Independent Candidate-C benchmark at `a=0.5`:

- `c_grav^2 ~= 0.6920799927`
- `c_grav ~= 0.83191345`

## 3 — Established results not to redo

Historical TDD already completed before the raw route:

- RED `b12ad1d95cde5926bdbc4896454cdc4f352274cd` -> GREEN `0448eef3ad05f6937aca8fadcab9a04d4916c712`: scalar P(X) matter action.
- RED `3e13f971447213d3510c940303330355383c7eff` -> GREEN `d26017a1b65e391d9cb80edc75ca308829819d20`: g/f lapse, scale and volume normalization.
- RED `b44f8305af9b501076629a033214e8e00523eb87` -> GREEN `6057075a9f3bf64763a05d4cd796ce7cf7da9e09`: first Lagos metric + two-matter assembly.
- RED `4f32b85f9bee546910568cfcaa7051baf06ac726` -> GREEN `796662db13fc3aec595bbcd99fec87e164a13122`: remove obvious metric-only matter double counting and recover rank-3 kinetic structure on proportional control.
- RED `0a75660a0048edb433a23a8ef8b83164e0bb3cfe` -> GREEN `af50032a23acaf58d134df16ed2e599cdbe087d9`: correct Lagos interaction coefficients.

Last targeted repository verification before the present raw-action pass: `15 passed`; **not** a full-suite result.

## 4 — Closed diagnostic branches

### P1c.1 — five raw Eq. (54) structures

Closed. Do not add them back individually. Lagos' one-matter derivation uses background equations to absorb/cancel the metric-only matter pieces; the canonical explicit lapse residual is `(rho+P) Phi^2/2`, generalized for P(X) to `(rho+P) Phi^2/(2 c_s^2)`.

### P1c.2 — lapse convention

Closed. `Phi_DF = Phi_L`; do not introduce `Phi_L/2`.

### P1c.3 — quadratic spectral solver

Closed as leading cause. Including `A=C-C^T` in

`det(-omega^2 K + i omega A + Q)=0`

still yields, at Candidate C `a=0.5`, correct g/f matter branches while the third scalar `omega` saturates near a finite scale as `k` grows. Do not tune the solver to force Eq. (86).

## 5 — A2.4d raw action result

Primary source: De Felice et al. arXiv:1404.0008.

New file: `numerics/de_felice_raw_scalar_action.py`.

Implemented directly from source, with **no background equations inside the raw helpers**:

1. `eh_scalar_quadratic_density_flat` — scalar contraction of Eq. (44), `K=0`, before the overall `(M^2/2) N a^3` factor.
2. `hr_scalar_quadratic_density_g_flat` — Eqs. (45)-(46) in g-flat gauge, normalized by `M_g^2 N a^3`, parameterized by source-transparent combinations:
   - `mu_g = m^2 rhohat_m,g`
   - `mu_f = m^2 rhohat_m,f`
   - `zeta = m^2 xi J`
   - `gamma_m = m^2 Gamma`.
3. `RawBimetricBackground` — carries local g/f lapses/scales and the raw interaction/background coefficients.
4. `raw_two_matter_scalar_density_g_flat` — complete raw quadratic density

   `EH(g) + EH(f) + HR + P(X)_g + P(X)_f`

   divided by the common `M_g^2 N a^3`.

Normalization controls:

- `n/N = ctilde*xi`;
- `alpha/a = xi`;
- f volume relative to g is `ctilde*xi^4`;
- f EH relative weight is `kappa*ctilde*xi^4`;
- matter f carries `ctilde*xi^4` with **no extra ad hoc `1/kappa`**.

A reconstructed local targeted run on the exact source formulas gave:

`python -m pytest -q tests/test_de_felice_raw_scalar_action.py`

`9 passed in 0.04s`

This is **not a clean checkout/full repository-suite run**. It validates the targeted raw Eq. (44), HR slices, and g/f normalization only.

## 6 — Source/background identities for Candidate C

For flat `K=0`, `M_g^2=1`:

- `mu_g = m^2 rhohat_m,g = 3 H^2 - rho_g`;
- `mu_f = m^2 rhohat_m,f = 3 kappa H_f^2 - rho_f`;
- `Hdot/N = 0.5 [m^2 xi J (ctilde-1) - (rho_g+P_g)]`;
- `Hfdot/n = -0.5 [m^2 J (ctilde-1)/(kappa xi^3 ctilde) + (rho_f+P_f)/kappa]`;
- `zeta = m^2 xi J`;
- `gamma_m = m^2 Gamma`.

Apply these only when constructing the benchmark background, after the raw terms have been independently defined.

## 7 — Ordered task queue

### P0 — repository/restart hygiene

- [x] audit branches/PRs; freeze redundant historical branch.
- [x] maintain authoritative restart ledger.
- [ ] delete historical branch only when ref-delete capability exists.

### P1 / A2 — exact raw two-matter action

- [x] P(X) matter Eq. (54) for arbitrary lapse/scale.
- [x] g/f local normalization.
- [x] P1c.1 five-term audit.
- [x] P1c.2 lapse convention audit.
- [x] P1c.3 full spectral solver audit.
- [x] A2.4d source-level Eq. (44) g/f scalar contraction.
- [x] A2.4d raw HR Eqs. (45)-(46) g-flat block.
- [x] A2.4d full raw two-matter g-flat density.

### A3 — ACTIVE: constraints and physical 3x3 system

- [ ] construct the quadratic Hessians of the raw density in variables
  `x_aux=(Phi,B,varphi,b)` and `q=(Sigma,S,u_g,u_f)`;
- [ ] verify the 4x4 auxiliary Hessian is nonsingular on Candidate C for finite `k` away from singular limits;
- [ ] eliminate all four auxiliaries by exact/numerical Schur complement at the Lagrangian level, retaining velocity couplings;
- [ ] measure the reduced 4x4 velocity Hessian rank; healthy expectation is rank 3;
- [ ] identify/eliminate the remaining nondynamical scalar without imposing a target dispersion;
- [ ] construct physical `K,N,M` (or equivalent quadratic pencil) for the 3 propagating scalars.

### A4 — high-k falsification gate

- [ ] RED: raw oracle does not yet have a validated Candidate-C 3-mode speed regression.
- [ ] recover g matter speed.
- [ ] recover f matter speed.
- [ ] recover gravity speed `c_grav^2 ~= 0.6920799927` at `a=0.5`.
- [ ] repeat at `a=1` and `a=0.2`.
- [ ] verify gravitational kinetic sign against De Felice Eq. (80)/(82).

If the independent raw action fails Eq. (86), stop transfer phenomenology and audit raw transcription/conventions. Do not repair Lagos until the raw oracle passes.

### A5/A6

- [ ] exact Case-C regression.
- [ ] compare validated raw reduction back to Lagos/Comelli and localize the missing/rearranged structure.
- [ ] only then repair production transfer code.

## 8 — Interruption protocol

Before any pause/context loss:

1. update this file;
2. record exact commit SHAs;
3. record exact targeted command/result or explicitly mark unexecuted/full-suite unavailable;
4. state the active hypothesis and rejected alternatives;
5. end with a single `NEXT:` instruction.

**NEXT:** implement A3 on top of `731fe693ad6cd4c9eaf0677b8ba06d8888e30f0d`: build the raw quadratic Hessian for `x_aux=(Phi,B,varphi,b)` and `q=(Sigma,S,u_g,u_f)`, eliminate the four auxiliaries by Schur complement while retaining all velocity cross terms, verify reduced kinetic rank 3 at Candidate C `a=0.5`, then extract the 3-mode high-k quadratic pencil before touching any Lagos production code.
