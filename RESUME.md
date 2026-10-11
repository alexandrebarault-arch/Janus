# Janus Research Resume Checklist

Date: 2026-10-11
Active branch: `research/v2-flrw`
Draft PR: `#1` — keep open/draft, do not merge yet
GitHub Actions / workflows: **disabled by user**. Never infer verification from CI.

## Purpose

This is the authoritative restart point after any interruption. Read this file first. Do not restart superseded algebraic scans, dimensional source-threshold arguments or ad-hoc lapse derivations.

## Scientific state — compressed truth

1. `JANUS-EXACT` is **NOT CLOSED** as a complete generally covariant nonlinear bimetric theory.
2. Main continuation is `JANUS-R`: ghost-free Hassan-Rosen bigravity, two positive-energy matter sectors.
3. Literal universal `+G/-G`, fundamental negative mass and isolated negative photon lensing are **not** recovered/required by the healthy two-metric continuation.
4. Linear cross repulsion exists but is weaker (`-G/3` in the symmetric asymptotic normalization), and slow-matter dynamics differs from photon lensing.
5. Linear relative-mode growth (`p≈1.186` maximally unscreened in EdS) is too weak to create dramatic late segregation from an arbitrarily tiny seed by itself.
6. Lambda-CDM-like `H(z)` is not a stability pass. Exploratory scans expose a strong stability-vs-visible-mixing tension: making the theory healthy earlier drives it toward GR-like decoupling.
7. The only serious surviving path is **environment-dependent nonlinear JANUS-R**.
8. Aoki-Maeda-Namba 2015 give the key nonlinear two-matter scalar equation; visible underdensity + twin overdensity adds coherently to its relative source.
9. Fixed-H source thresholds are dimensionful and must not be read as density-contrast thresholds.
10. Algebraic double-root endpoints at a compensation wall are signs that the algebraic/small-gradient approximation fails there, not automatic physical singularities.
11. Aoki-Mizuno static Ricci-flat Vainshtein instabilities are a major warning, not a universal no-go for a non-Ricci-flat cosmological two-matter wall.
12. Brizuela-de Cesare-Soler Oficial 2024 provide general perturbation machinery once a genuine gradient-resolved spherical background exists.

## Full spherical / numerical-relativity breakthrough

### Aoki-Maeda-Tanabe 2016

`Relativistic stars in bigravity theory`, arXiv:1602.02227.

Full static spherical Hassan-Rosen equations already exist **with both matter sectors retained**: radial Einstein equations, both matter conservation laws and the bimetric constraint, reducible to seven first-order ODEs plus an algebraic constraint.

### Kocic-Torsello-Hogas-Mortsell 2020

`Initial data and first evolutions of dust clouds in bimetric relativity`, arXiv:1904.08617.

Correct dynamical architecture already exists:

- full spherical standard `3+1` bigravity;
- nonbidiagonal separation/relative shift;
- Hamiltonian + momentum + secondary constraints;
- short dust-cloud evolutions;
- no simple analytic LTB analogue.

Public code: `nubirel/bim-solver` (GPLv3), pinned for this research at tree/commit:

`8852e8e9921edeeedf1a447d3bf27b82ec24433c`

The current sandbox cannot clone/download it (`Could not resolve host: github.com`). Source inspection is through the GitHub connector only; **the C++ solver has not been compiled here**.

## Gate A0 — constrained Janus-like initial data: PASS

Files:

- `numerics/twin_lane_emden_initial.py`
- `tests/test_twin_lane_emden_initial.py`
- `research/V2_FULL_SPHERICAL_GATE.md`

Time-symmetric conformally-flat constraints were solved for:

- central positive f density;
- regular positive g compensating shell;
- asymptotic bi-Minkowski boundary;
- positive conformal factors.

Manual TDD:

- RED: `ModuleNotFoundError`
- GREEN: `3 passed in 0.48s`

Verdict:

`JANUS_LIKE_INITIAL_DATA_EXISTENCE = PASS`

Meaning only: the desired central twin concentration + visible wall is not forbidden by the time-symmetric elliptic constraints. Formation/evolution/stability/FLRW embedding remain open.

## Important rejected shortcuts

### Ad-hoc expanding CMC Lane-Emden

Rejected. At `K_ij != 0`, momentum and secondary constraints no longer vanish automatically. A radial f/g ratio through the wall requires consistent extrinsic curvature + separation/shift; simply inserting `K=-3H` is invalid.

### ADM sign as repulsion diagnostic

Rejected. A positive f source can give positive long-range ADM mass in both metrics while still producing finite-range cross repulsion through the massive mode. ADM probes the asymptotic massless mode, not the force sign at finite range.

### Upstream maximal-slicing routine as twin-matter kick

Rejected. `include/maximalSlice.h` is specialized to g matter and contains upstream TODO/fixme source/factor notes. Do not infer twin-fluid physics from it.

## Exact twin-fluid extension map in `bim-solver`

**First use standard 3+1 (`bim-solver-STD`), not cBSSN.** It is the published short-evolution formulation and is easier to audit. Only harden to cBSSN after a short standard evolution passes.

The existing single Valencia state is `pfD,pfS,pftau,pfv`. A real twin-fluid extension needs an independent f state and changes at least:

1. `src/bim-solver-std.cpp` — state registration, evolution, derivatives, parity/boundaries.
2. `include/eom-std/eomMatter.h` — f-sector Valencia equations using only f geometry/lapse/shift.
3. `include/eom-std/eomSources.h` — add f matter to `f_rho,f_j,f_JK,f_JKD`.
4. `include/eom-std/eomConstraints.h` — mixed constraint `C_3` currently assumes `S_f=0`.
5. `include/eom-std/eomMiscEquations.h` — `eq_base_p_f` currently assumes `S_f=0`.
6. `include/eom-std/eomEvolution.h` — direct `S_g` source has missing f-sector dual term.
7. `include/eom-std/eomLapseRatios.h` — currently specialized to one-fluid matter.
8. `include/maximalSlice.h` only if maximal slicing is later used; avoid initially.

Exact momentum-sector corrections already derived:

- `base_p_f -> base_p_f - S_f/(A_f A_g B_g^2 P_2_1(R))` in current solver conventions;
- corrected mixed-constraint matter part is proportional to
  `-k_g k_f (S_g + S_f)/(2 B_g^2)`.

These follow from eliminating the separation variable between the two momentum constraints; they are not guessed patches.

## Major new result — general twin-matter lapse ratio already exists

Primary reference:

Kocic, Lundkvist, Torsello, `On the ratio of lapses in bimetric relativity`, arXiv:1903.09646.

This paper is derived with **both matter sectors present**. Preservation of the secondary constraint gives in spherical symmetry

`0 ~= W_g alpha + W_f alpha_f`,

therefore

`alpha = -(W_f/W_g) alpha_f`.

The authors explicitly state that `W_g,W_f` depend on both matter stress-energy tensors: matter coupled to either metric affects the lapse of the other.

Explicit formulas are Eqs. (2.20)-(2.22), coefficients in Appendix D. Under the sector duality `g<->f`, `beta_(4-n)<->beta_n`, `p<->-p`, one has `W_g<->-W_f`.

### Machine-readable source exists

The arXiv record lists ancillary derivation files:

- `src/02-lapse-ratio.nb`
- `src/bimetric-lapses-nr.m`
- `src/bimetric-ss-nr.m`

and arXiv:1904.08617 republishes related machine-readable source.

The current sandbox cannot fetch them because of network/cache restrictions. **When a real fork environment is available, obtain these first. Do not manually transcribe Appendix D into production C++ if the authors' symbolic source is available.**

### Mandatory lapse implementation regression

1. import/translate the authors' general `W_g,W_f` expression;
2. test the `g<->f` duality;
3. set all f-matter variables to zero;
4. require agreement with upstream one-fluid `eomLapseRatios.h` over randomized regular states;
5. only then permit twin-fluid evolution.

This removes the biggest conceptual blocker of Gate A1.

### Gauge

Once `W=-W_f/W_g` is known, only one lapse is gauge freedom. The paper also gives the geometric-mean relation

`H^2 lambda = alpha alpha_f`.

A symmetric geometric-mean gauge is therefore a good research choice for the wall test. Monitor zeros/divergences of `W_g,W_f` as branch warnings.

## Integrator / solver traps

- GitHub Actions/workflows disabled by user.
- Use explicit RK3/RK4 first; DIRK/Jacobian work only if demonstrated stiffness requires it.
- `src/bim-solver-BSSN.cpp` defaults `_TEST_MODE=1`; any future cBSSN physics build must explicitly use `-D_TEST_MODE=0` and verify evolved-field names/count.
- cBSSN full strong hyperbolicity remains less established than in GR; treat it as research-grade.
- Standard-3+1 constraint propagation has been shown to form a first-order symmetric-hyperbolic subsystem; constraint convergence is therefore a meaningful diagnostic even though it does not prove the entire gauge-fixed evolution system is ideal.

## Authoritative implementation documents

Read before any twin-fluid code:

- `research/V2_TWIN_FLUID_NR_RUNBOOK.md`
- `docs/superpowers/plans/2026-10-11-twin-fluid-nr.md`
- `research/V2_FULL_SPHERICAL_GATE.md`

The runbook contains the exact source map and corrections.

## Mandatory resume order

1. Read `RESUME.md`.
2. Read the three implementation documents immediately above.
3. Confirm branch `research/v2-flrw` and PR #1 draft/unmerged.
4. Inspect commits newer than this file before writing.
5. Do not return to old algebraic root scans unless new mathematics directly requires it.

## Verification policy while Actions are disabled

- TDD for behavioral/numerical code where feasible.
- Record exact RED and GREEN output.
- Verify GitHub file SHA/content after writes.
- Never claim full-repository verification unless actually executed.
- No C++ build/run claim until a real local upstream fork has been materialized and compiled.

Known module-level evidence includes:

- asymmetric two-fluid control: `3 passed`;
- cosmological nonlinear trajectory: `3 passed`;
- Higuchi scale window: `3 passed`;
- self-consistent transition: `4 passed`;
- static Case-A branch selection: `4 passed in 0.75s`;
- environmental screening: RED `ModuleNotFoundError` -> GREEN `3 passed in 0.03s`;
- twin Lane-Emden data: RED `ModuleNotFoundError` -> GREEN `3 passed in 0.48s`;
- published Aoki-Maeda-Namba roots reproduced.

These are not full branch CI.

## Immediate next actions

### Gate A1 — general twin-fluid 3+1 state

When the upstream fork can be materialized:

1. compile untouched `bim-solver-STD` and reproduce a one-fluid baseline;
2. obtain arXiv ancillary `bimetric-lapses-nr.m` / notebook source;
3. add independent `D_f,S_f,tau_f,v_f` state;
4. implement sector-symmetric f Valencia equations;
5. add f matter to all source/constraint/separation/evolution locations listed above;
6. implement general published `W_g,W_f`;
7. prove `T_f=0` regression against upstream lapse/source equations;
8. map the Python Lane-Emden profile into 3+1 fields and verify all constraints.

### Gate A2 — short-time wall evolution

Only after A1:

- vacuum / g-only / f-only / full twin controls;
- RK3/RK4 at >=3 resolutions/Courant factors;
- monitor both Hamiltonian + momentum constraints, secondary constraint, `W_g,W_f`, lapse ratio, separation, metric positivity, both rest masses and velocities;
- classify wall as regular/dispersing/collapsing/branch-failing only from convergent evidence.

### Gate A3 — expanding cosmological embedding

Only after local A2 passes:

- solve full non-time-symmetric constraints;
- include extrinsic curvature and separation consistently;
- FLRW exterior, not asymptotic Minkowski;
- then evolve compensated cosmic void.

### Gate B/C/D

B: perturbative/principal-symbol stability of the evolved wall.

C: test whether ordinary initial conditions generate the anti-correlated state rather than merely allow tuned initial data.

D: only then compute velocity/lensing profiles and fit DESI/RSD/`E_G`/void lensing/BAO/SNe/CMB.

## Stop / downgrade conditions

Strongly downgrade/reject JANUS-R if:

1. no regular gradient-resolved wall evolution exists;
2. every wall evolution has unavoidable ghost/gradient instability;
3. healthy solutions require forbidden early isocurvature;
4. healthy regions decouple the visible massive mode so strongly that the effect is negligible;
5. early screening also kills the late effect;
6. viable solutions reduce observationally to GR+LambdaCDM with extra unconstrained parameters.

## Do not redo unless new mathematics appears

- exact universal `+G/-G` in the same linear two-metric architecture;
- fundamental negative mass as required mechanism;
- isolated positive twin matter giving divergent negative photon lensing;
- viability from `H(z)` alone;
- dimensional source thresholds interpreted as density contrast;
- algebraic root endpoints treated automatically as physical singularities;
- static Ricci-flat no-go extrapolated blindly to cosmological wall;
- ad-hoc expanding CMC Lane-Emden data;
- hand-written twin lapse that ignores the published general `W_g,W_f` result.
