# Gate 2B — independent raw scalar-action reconstruction

Date: 2026-10-12
Canonical branch: `research/v2-flrw`
Status: **ACTIVE — RAW DE FELICE TWO-MATTER ROUTE**
Parent restart ledger: `research/RESTART_TASKS.md`

Purpose: reconstruct the healthy-branch scalar dynamics independently of both the failed Comelli closure and the one-matter Lagos background reduction. The raw action is the oracle; Lagos becomes a later cross-check only after the physical characteristics are recovered.

## Binding acceptance criteria

1. Do not use the old 12x12 Comelli closure as an input.
2. Do not tune coefficients/signs to hit a target.
3. Reproduce the De Felice gravitational high-k `c_s^2` from the independently assembled raw action at Candidate C `a=1,0.5,0.2`.
4. Recover both matter sound speeds independently.
5. Recover exactly three physical scalar modes after gauge/constraint reduction.
6. On exact Case C, recover the known scalar equation or an explicitly invertible equivalent variable map.
7. Only after these pass compare back to Lagos/Comelli and identify the missing/rearranged structure.

## Hard source facts

### De Felice raw action

The required independent ingredients are all in arXiv:1404.0008:

- Eq. (44): quadratic Einstein-Hilbert action for `g`; the `f` contribution follows by the paper's stated replacement.
- Eqs. (45)-(46): exact quadratic Hassan-Rosen mixing action, including determinant pieces, `Delta`, and the `Gamma` spatial-difference term.
- Eq. (54): generic P(X) matter quadratic action; apply separately to g and f.
- Eqs. (13)-(16): background Friedmann/acceleration identities.
- Eqs. (72)-(73): three gauge-invariant physical scalar variables and reduced quadratic action.
- Eq. (80)/(82): gravitational kinetic no-ghost eigenvalue and `B`.
- Eqs. (84)-(86): high-k dispersion relation and the three propagation speeds.

The reduced action contains a real antisymmetric mixed matrix `N` (`qdot*q`). Any spectral diagnostic that omits it is incomplete.

### Background bridge

Use:

- `xi = y`;
- `kappa = alpha^2`;
- `ctilde = c`;
- `n/N = ctilde*xi`;
- `alpha_scale = xi*a` for the f spatial scale factor;
- healthy branch `H = xi H_f`;
- `J = beta1 + 2 beta2 xi + beta3 xi^2` in repository conventions;
- `Gamma = xi J + 0.5 (ctilde-1) xi^2 J'`.

For flat Candidate C and `M_g^2=1`, useful identities that avoid guessing intermediate `U` normalization are

- `m^2 rhohat_m,g = 3 H^2 - rho_g`;
- `m^2 rhohat_m,f = 3 kappa H_f^2 - rho_f`;
- `Hdot/N = 0.5 [m^2 xi J (ctilde-1) - (rho_g+P_g)]`;
- `Hfdot/n = -0.5 [m^2 J (ctilde-1)/(kappa xi^3 ctilde) + (rho_f+P_f)/kappa]`.

### Scalar decomposition

De Felice uses

- `V_i = D_i B`;
- `H_ij = 2 gamma_ij psi + (D_i D_j - gamma_ij Delta/3) E`;
- f analogues `varphi,b,Sigma,S`.

The three gauge invariants are `Y1,Y2,Y3` with `Y3=S-E`. In g-flat gauge `E=psi=0`, the natural raw dynamical coordinates are therefore the f spatial scalars plus the two matter perturbations; after all constraints one of these four coordinates is still nondynamical, leaving three physical modes.

### Matter conventions

De Felice Eq. (54) uses

`g_00 = -N^2 (1 + 2 Phi)`.

The current repository bridge `Phi_DF = Phi_L` is correct. Do not introduce a `/2` patch.

For P(X), the pure-lapse bracket coefficient is

`-P/2 + [(1+c_s^2)/(2 c_s^2)] (rho+P)`.

Do not substitute exact dust (`c_s^2=0`) into the unreduced P(X) action. Take the dust limit only after constrained reduction or use an equivalent dust action.

## Closed diagnostic questions

### 1. Are the five raw Eq. (54) metric-only structures simply missing from Lagos?

**No.** In the one-matter derivation they are absorbed/cancelled through the background equations, with the explicit canonical residual `(rho+P) Phi^2/2` and P(X) generalization `(rho+P) Phi^2/(2c_s^2)`.

Therefore do not add the five raw structures blindly to `lagos_two_matter_action.py`.

### 2. Is `Phi_DF = Phi_L/2` the missing convention?

**No.** The action coefficients independently fix `Phi_DF = Phi_L`.

### 3. Is the quadratic spectral solver missing the antisymmetric mixed term?

A solver that omitted it would indeed be wrong, but this is **not the current hard failure's cause**. The current action was independently reconstructed as

`L = 1/2 qdot^T K qdot + qdot^T C q + 1/2 q^T Q q`,

and solved with `A=C-C^T` included. At Candidate C `a=0.5`, probes `c_g^2=0.4`, `c_f^2=0.3`, the two matter characteristics are correct while the third scalar frequency saturates around `omega ~ 86.6` as k grows. Hence its propagation speed tends to zero instead of the De Felice target `c_grav ~= 0.831913`.

The action/background reduction remains the failing layer.

## Existing implementation pieces worth reusing

- `numerics/de_felice_matter_action.py`: Eq. (54) P(X) matter action.
- `numerics/de_felice_action_principal.py`: independent Eq. (86) gravitational benchmark.
- `numerics/candidate_c_transfer.py`: exact Candidate-C background adapter.
- `numerics/flrw_two_matter.py`: Candidate-C branch/background diagnostics.
- `numerics/bigravity_scalar_action.py`: historical raw EH/HR building blocks and useful regression history.

Caution: the historical exact-HR diagonal evaluator in `bigravity_scalar_action.py` contains old comments/code written with `1+Phi` lapse factors. Treat it as a historical implementation to audit, not as an unquestioned normalization oracle; the canonical De Felice lapse convention for the raw reconstruction is `1+2Phi`.

## Historical RED/GREEN ledger preserved

- A1 bridge RED `ce5aee2` -> implementation `dca0d52`.
- A2 base RED `917aec5` -> implementation `f0de003`.
- Corrected spatial-derivative RED `f56c58f` -> `3984612`.
- sector-1 EH velocity RED `ee97d21` -> GREEN `fefab2d`.
- sector-2 EH velocity RED `e3a70e5` -> GREEN `bc16893`.
- exact HR spatial-cross RED `b461763` -> GREEN `10781fc`.
- HR lapse RED `dec47a8` -> GREEN `357701e`.
- sector-1 EH spatial RED `cfda8a1` -> GREEN `334ebb8`.
- sector-2 EH spatial RED `b28f867` -> GREEN `d32b762`.
- De Felice P(X) matter RED `8f94c83` -> implementation lineage leading to current `numerics/de_felice_matter_action.py`.

These historical tests establish useful pieces but **do not constitute a completed raw two-matter action or A4 validation**.

## Active task list

- [x] **A0 — independent source route established.**
- [x] **A1 — background/convention bridge established sufficiently for Candidate-C raw benchmark.**
- [ ] **A2 — raw gravity + two-matter quadratic action. ACTIVE.**
  - [x] P(X) matter action for an arbitrary lapse/scale factor;
  - [x] g/f local matter volume/lapse/scale normalization;
  - [x] historical EH velocity/spatial building blocks available;
  - [x] historical HR spatial/lapse building blocks available;
  - [ ] **A2.4d — CURRENT:** write one canonical De Felice-normalized raw scalar Lagrangian in g-flat gauge from Eq. (44) + f analogue + Eqs. (45)-(46) + two copies of Eq. (54);
  - [ ] enforce the background identities only after summing all raw pieces;
  - [ ] audit the historical HR evaluator's lapse-factor convention against `1+2Phi` before reuse;
  - [ ] keep exact dust out of the unreduced P(X) action.
- [ ] **A3 — eliminate constraints.**
  - [ ] eliminate `Phi,varphi,B,b` simultaneously;
  - [ ] identify and eliminate the remaining nondynamical scalar after g-flat gauge;
  - [ ] construct the physical 3x3 `K,N,M` system.
- [ ] **A4 — high-k regression.**
  - [ ] RED first: current/empty raw oracle must fail to return De Felice gravity speed;
  - [ ] GREEN: recover g matter, f matter, and gravity speeds at `a=0.5`;
  - [ ] repeat at `a=1` and `a=0.2`;
  - [ ] verify gravitational kinetic sign against Eq. (80)/(82).
- [ ] **A5 — exact Case-C regression.**
- [ ] **A6 — compare validated raw reduction back to Lagos/Comelli** and localize the missing structure.
- [ ] **A7 — replace/repair production transfer solver only if A4-A6 establish the correct reduction.**

## TDD rule for the next implementation

No production correction to the Lagos bridge is allowed before an observed failing test.

The first useful RED test should be a Candidate-C high-k action regression that expects three physical characteristics and checks the gravitational one against `numerics/de_felice_action_principal.py`. It must fail because the raw two-matter oracle is not yet implemented or does not yet recover the benchmark — not because of a typo/import error.

A reconstructed local test run is acceptable as RED/GREEN evidence only if the exact code and command are recorded; it is still not a full repository-suite result.

## Immediate restart instruction

**Resume at A2.4d.**

1. Work in De Felice variables and g-flat gauge.
2. Assemble the raw EH, HR, g matter, and f matter quadratic terms without importing the Lagos one-matter background-reduced metric block.
3. Use Candidate-C background equations to cancel/rewrite background coefficients only after raw assembly.
4. Build/eliminate the four lapse/shift auxiliaries.
5. Reduce the remaining four coordinates to the three physical scalars.
6. Extract the full `K,N,M` matrices and high-k roots.
7. Require `c_grav^2 ~= 0.6920799927` at `a=0.5` before touching production transfer code.

**NEXT:** derive and locally verify the De Felice Eq. (44) scalar contraction in g-flat gauge and the f analogue, then combine them with the already-implemented Eq. (54) matter sector and the exact HR quadratic terms under a RED Candidate-C speed regression.