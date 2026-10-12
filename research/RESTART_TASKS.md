# JANUS-R — Authoritative restart tasks

Date: 2026-10-12
Canonical active branch: `research/v2-flrw`
Stable baseline: `main` (`aead63f4098f0d15a849e579105af034b6317b30`)
Gate 2B consolidation merge: `35f5edc19443a059308e8c2710deb656bfdd8fbc`

Purpose: **first file to read after any interruption**.

## 0 — Resume in one minute

1. Work only from `research/v2-flrw`; keep `main` untouched.
2. Literal published JANUS remains rejected as an established theory. The surviving program is JANUS-R: a healthy Hassan-Rosen two-sector descendant tested by falsification gates.
3. The authoritative scalar oracle is the independent raw De Felice two-matter action plus the **time-dependent physical-variable / BD reduction**.
4. Correct quadratic equations are
   `K qddot + (Kdot + C - C^T) qdot + (Cdot - Q) q = 0`.
5. Physical f-sector variable in g-flat gauge:
   `Y2hat = u_f - (Sigma + k^2 S/6)/(n H_f)` with the full `Rdot` contribution retained.
6. A4 is now closed: `a=1`, `a=0.5`, and the corrected `a=0.2` conditioning gate pass; kinetic signs are positive and the high-k extraction is stable to derivative-step changes.
7. The exact Eq. (86) gravity-speed oracle must be tested on a **self-consistent P(X) background**, not on the arbitrary Candidate-C probe sound speeds.
8. Lagos vs raw De Felice has now been checked directly at the **action level** on self-consistent P(X) backgrounds: they agree numerically to ~`1e-11` in a common gauge.
9. Therefore the old missing-helicity-0 failure is **not an action-assembly failure**. It lives downstream in the historical Lagos reduction/dispersion path, which freezes the background and does not carry the full `K,C,Q`, `Kdot,Cdot`, and time-dependent null-coordinate reduction.
10. NEXT: implement a Lagos physical-reduction path that mirrors the validated raw De Felice pipeline, starting with a RED regression that requires the Lagos route to reproduce the same three physical scalar characteristics on the self-consistent P(X) controls. Do not alter action coefficients unless that equivalence test fails first.

## 1 — Git / repository state

- `main` — stable pre-V2 baseline; untouched.
- `research/v2-flrw` — canonical active research line.
- `research/gate2b-nonhomothetic-transfer` — historical/redundant; fully absorbed and frozen until ref deletion is available.
- PR #1 remains draft (`research/v2-flrw` -> `main`); do not merge as model validation.
- GitHub Actions/workflows remain intentionally disabled.

Latest relevant lineage:

- `64bfd19a184a7df39b9d075822f9a621c62fd59f` — RED Eq. (44) Fourier shift-cancellation regression.
- `7d9f57d8a892cf51c1c9823b9c74655f2e914e71` — GREEN Eq. (44) `B*E_dot` sign fix.
- `0ba69ef36b0396fc5eb7457f6fda52e21a95a445` — RED generic time-dependent BD reduction.
- `a2e47995bec88d61501e36da8c02b83333420edf` — GREEN generic null-coordinate reduction + `Y2hat` map.
- `afce1faaf404393b03f89e1d33534e37f81be737` — RED null-Schur conditioning regression.
- `e865ccf3e1fc4eb6c7191cec3aebc7cc814d0ea5` — GREEN local conditioning fix.
- `2553b53bd8a2a9aac8482300651602d3ad0360c2` — RED Candidate-C physical 3-mode regression.
- `cebd1e2b04c7a7b0ae1c2deb9d8dcc7246efae7e` — GREEN Candidate-C `a=0.5` benchmark.
- `e3fcdcd6f8315c6438c7df952b45e283887fe146` — RED self-consistent P(X) control.
- `d334a89031949fa6f19ef38275fce0dce25b00af` — GREEN self-consistent P(X) control.
- `fc91cde90609c2e860cd82cb3bb4636e9604a79f` — corrected `a=0.2` RED: finite/mode-complete gate only.
- `a3f0b13ef8e80c1da6449b771d2be0a3a2232bb4` — GREEN stabilized Candidate-C reduction (joint Hessian + Schur + explicit null-Schur derivatives).
- `25e76fd1c1725dcb86e179a8a10a4f0f373c887d` — freeze `a=1` high-k and kinetic-sign gates.
- `c3a7212b44ad07f2bde6659dcec63ed68552fbdb` — freeze derivative-step robustness.
- `ba476c220c057919de759f27ba0d2b040f2056ce` — freeze Lagos/raw action equivalence on self-consistent P(X) backgrounds.

## 2 — Scientific status

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`

`TWO_SECTOR_BIMETRIC_SEGREGATION_IDEA = OPEN / FALSIFICATION-DRIVEN`

`GATE_2B_NONHOMOTHETIC_SCALAR_TRANSFER = OPEN / A4 CLOSED / A5 LAGOS REDUCTION REPAIR ACTIVE`

The healthy Hassan-Rosen two-matter scalar route survives the helicity-0/high-k gate. This does **not** rescue literal JANUS.

## 3 — Raw-action facts closed unless contradicted

- Eq. (54) P(X) matter action independently implemented.
- `Phi_DF = Phi_L`; no `/2` patch.
- f volume relative to g: `ctilde*xi^4`.
- f EH relative weight: `kappa*ctilde*xi^4`.
- no ad hoc f-matter `1/kappa`.
- Eq. (44) Fourier cross coefficient: `-2 k^4 B E_dot/(3 N a)`.
- pure-E `B E_dot` cancellation under the De Felice/Lagos bridge is exact.
- de Sitter EH/background-determinant mapping to Lagos is exact.
- proportional HR relative block maps exactly to the healthy Lagos interaction.
- Minkowski Eq. (44)+Fierz-Pauli gives high-k `c_s^2=1`.
- On self-consistent non-homothetic P(X) backgrounds, the Lagos two-matter action and raw De Felice action agree directly in a common gauge to numerical precision (`~1e-11`).

Important subtlety:

- Eq. (54) uses `delta phi_dot / phi_dot_0`.
- if `u = delta phi / phi_dot_0`, then on an evolving background `delta phi_dot / phi_dot_0 = u_dot + (phi_ddot_0/phi_dot_0)u`.
- Candidate-C's arbitrary probe sound speeds are useful for mode-completeness and conditioning, but are not an exact single-P(X) realization of its dust+radiation / dust background.
- exact Eq. (86) validation therefore lives in `de_felice_consistent_px_control.py`.

## 4 — Root causes already found

Two historical failures are closed:

1. **Frozen-background BD reduction** — eliminating the kinetic-null coordinate after freezing loses `Kdot`, `Cdot`, and `Rdot` terms and creates a false finite-frequency third branch.
2. **Nested finite differences** — differentiating matrices that were themselves obtained by differencing an already reduced Lagrangian causes early-epoch/high-k numerical blow-up.

The validated raw route now:

- builds one joint quadratic Hessian in auxiliaries + coordinates + rates;
- removes lapse/shift by a direct matrix Schur complement;
- differentiates the primary `K,C,Q` matrices in `x=ln a`;
- performs the time-dependent null-coordinate Schur reduction explicitly;
- uses `Kdot` and `Cdot` in the final Euler-Lagrange system;
- rescales the geometric `S` direction by `k^2` only as coordinate conditioning before eigensolution.

## 5 — A4 closed controls

### Self-consistent P(X) Eq. (86) control

Implementation: `numerics/de_felice_consistent_px_control.py`.
Tests: `tests/test_de_felice_consistent_px_control.py`.

Representative checks show the raw route converging to the independent De Felice Eq. (86) gravity speed across non-homothetic epochs, e.g. `a=0.5,0.4,0.3`.

### Candidate-C production diagnostics

- `a=0.5`: three physical high-k modes recovered; historical gravity target recovered within committed tolerance.
- `a=0.2`: three finite oscillatory branches remain present at high k; both imposed matter characteristics are recovered; no spurious blow-up.
- `a=1`: committed three-characteristic regression passes with the stabilized reduction.
- physical 3x3 kinetic eigenvalues are positive at `a=1,0.5,0.2`, matching the independent positive De Felice Eq. (80)/(82) no-ghost sign.
- high-k extrapolation is stable when `diff_step` changes from `2.5e-4` to `2e-3` within the committed `1e-4` absolute criterion.

## 6 — Current verification evidence

Current local reconstructed A4 command:

`python -m pytest -q tests/test_time_dependent_quadratic_reduction.py tests/test_de_felice_raw_scalar_action.py tests/test_de_felice_candidate_c_reduction.py tests/test_de_felice_consistent_px_control.py`

Result on 2026-10-12 after resuming: **`22 passed in 0.58s`**.

This is **not** a clean full-repository-suite result and does not include the newest Lagos/raw equivalence test because the reconstructed local subset does not contain the full Lagos module dependency tree.

Newest repository-level regression added at `ba476c2...`:

`tests/test_lagos_raw_action_equivalence.py`

It asserts Lagos and raw De Felice action values agree on self-consistent P(X) backgrounds at `a=0.5,0.4,0.3` with `rel_tol=abs_tol=2e-11`.

## 7 — Ordered task queue

### A2 — raw action

- [x] Eq. (54) P(X) matter action.
- [x] g/f normalization.
- [x] raw Eq. (44) EH scalar contraction.
- [x] raw Eqs. (45)-(46) HR block.
- [x] full raw g-flat two-matter density.
- [x] Eq. (44) Fourier-sign regression.

### A3 — physical reduction

- [x] eliminate four primary lapse/shift auxiliaries.
- [x] verify reduced rank-3 kinetic structure.
- [x] identify null BD direction.
- [x] time-dependent null-coordinate elimination.
- [x] `Y2hat` + `Rdot`.
- [x] physical 3x3 Euler-Lagrange system.
- [x] remove nested finite-difference conditioning failure.

### A4 — high-k falsification gate

- [x] `a=0.5` three-mode regression.
- [x] `a=0.2` finite/mode-complete high-k regression.
- [x] self-consistent P(X) Eq. (86) gravity control.
- [x] recover both matter characteristics.
- [x] robust `a=1` regression.
- [x] kinetic-sign comparison vs Eq. (80)/(82).
- [x] derivative-step robustness regression.

### A5 — Lagos production reduction repair — ACTIVE

- [x] direct Lagos/raw action-level equivalence in a common gauge.
- [x] establish that no HR/matter coefficient patch is needed before reduction.
- [ ] add RED regression: Lagos time-dependent physical reduction must reproduce the self-consistent P(X) three-mode speeds from the raw route.
- [ ] construct Lagos primary `K,C,Q` from a joint quadratic Hessian, not the old fixed-background velocity-Hessian helper.
- [ ] carry background derivatives and perform time-dependent BD-null reduction before forming the dispersion system.
- [ ] verify Lagos and raw physical `K,D,E` or final characteristic roots agree across `a=0.5,0.4,0.3`.
- [ ] only after these pass, retire/deprecate any frozen-pencil diagnostic that can be mistaken for a physical gravity-speed oracle.

### A6 — only after A5 closes

- [ ] resume JANUS-R phenomenology / nonlinear-wall work.
- [ ] propagate the validated scalar transfer to the nonlinear segregation program.
- [ ] retain literal-JANUS rejection independently of JANUS-R progress.

## 8 — Interruption protocol

Before any pause:

1. update this file;
2. record exact commit SHAs;
3. record exact targeted commands/results or state full-suite execution is unavailable;
4. record rejected experiments as well as accepted ones;
5. end with one explicit `NEXT:` instruction.

**NEXT:** write a failing Lagos physical-reduction regression on the self-consistent P(X) controls, using the raw De Felice three-mode result as the oracle. Then implement the minimum time-dependent Lagos `K,C,Q -> BD Schur -> Kdot/Cdot -> eigensystem` path needed to make that regression pass. Do not touch action coefficients unless the existing action-equivalence regression first fails.
