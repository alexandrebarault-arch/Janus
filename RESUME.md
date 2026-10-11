# Janus Research — Authoritative Resume Checkpoint

Date: 2026-10-11
Active branch: `research/v2-flrw`
Draft PR: `#1` — keep open/draft and **do not merge yet**
Base: `main`
GitHub Actions/workflows: **disabled by user**. Never infer verification from CI.

## How to resume after any interruption

Read this file first. Then:

1. confirm PR #1 is still draft/open/unmerged;
2. compare `research/v2-flrw` against `main` and inspect commits newer than this file;
3. read the authoritative documents listed below;
4. resume from **NEXT ACTIONS**, not from old chat context;
5. do not repeat superseded algebraic scans or hand-derive the huge lapse formula;
6. record every meaningful correction/result in Git before moving on.

## Authoritative documents

Implementation / dynamic wall:

- `research/V2_TWIN_FLUID_NR_RUNBOOK.md`
- `research/V2_TWIN_FLUID_PATCH_SPEC.md`
- `docs/superpowers/plans/2026-10-11-twin-fluid-nr.md`
- `research/V2_NR_FEASIBILITY_AND_LAPSE_GATE.md`
- `research/V2_MEAN_GAUGE_AND_LAPSE_REPRESENTATION.md`
- `research/V2_FULL_SPHERICAL_GATE.md`
- `research/V2_INITIAL_DATA_GATE.md`

Scientific background / earlier gates:

- `research/V2_ENVIRONMENTAL_SCREENING.md`
- `research/V2_STATIC_VOID_GATE.md`
- `research/V2_COSMIC_TRANSITION_GATE.md`
- `research/V2_GOLDILOCKS_AND_GLOBAL_GROWTH.md`
- `research/V2_STABILITY_MIXING_TENSION.md`
- `research/NONLINEAR_TWIN_SCREENING.md`
- `research/V2_LINEAR_GATE.md`
- `research/STATE.md`
- `research/VERDICT_V1.md`

## Scientific truth — compressed

### Janus exact

1. `JANUS-EXACT = NOT_CLOSED` as a fully specified nonlinear generally covariant bimetric theory.
2. The 2015 constrained variation does not independently derive both published field equations.
3. Janus 2024 improves the structure but does not fully specify the general relativistic interaction sector needed for a closed theory in all regimes.
4. Literal fundamental negative mass is not required by the best surviving continuation.
5. Literal universal `+G/-G` is not recovered in the healthy linear two-metric continuation.
6. An isolated positive-energy twin source does not give negative/divergent photon lensing in the linear ghost-free two-metric mechanism.

### JANUS-R

Main continuation:

- Hassan–Rosen ghost-free bigravity;
- two separately and minimally coupled positive-energy matter sectors;
- ordinary visible sector retained;
- Janus-like behaviour must emerge dynamically, not be inserted as a sign rule;
- nonlinear screening is essential.

Linear results:

- cross-sector slow-matter repulsion exists in part of parameter space;
- symmetric asymptotic cross strength approaches about `-G/3`, not `-G`;
- actual force-sign threshold from the Yukawa potential is `mu r ~= 0.9612787631`;
- cross photon lensing remains non-negative in the corresponding linear solution;
- dynamics and lensing differ, giving a potentially falsifiable signal;
- maximally unscreened symmetric relative mode grows only as `a^1.186...`, too slowly to create dramatic late segregation from an arbitrarily tiny seed.

### Stability-versus-effect tension

A Lambda-CDM-like background `H(z)` is easy to obtain and is **not** evidence of viability.

Exploratory V2 scans show a robust qualitative tension:

- making the linear cosmology healthy farther back in redshift tends to reduce visible mixing of the massive mode;
- strong universal linear JANUS-R then either becomes observationally conspicuous or is driven toward GR-like decoupling.

Decision:

`STRONG_LINEAR_JANUS_R = DOWNGRADED`

The only serious surviving path is:

`ENVIRONMENT_DEPENDENT_NONLINEAR_JANUS_R`.

## Nonlinear two-matter result

Primary source: Aoki–Maeda–Namba 2015.

Their nonlinear scalar equation retains both matter sectors. The weighted relative source is schematically

`S_rel ~ kappa_g^2 rho_g delta_g - K^2 kappa_f^2 rho_f delta_f`.

For a visible underdensity plus twin overdensity the two contributions add coherently.

Important corrections:

- old fixed-`H` source endpoints are dimensionful and must not be read as density-contrast thresholds;
- an algebraic double-root endpoint in the compensation wall marks breakdown of the small-gradient/algebraic approximation, not automatically a physical singularity;
- the decisive region is therefore a **gradient-resolved radial transition wall**.

## Full spherical / numerical-relativity breakthrough

### Static two-matter equations already exist

Aoki–Maeda–Tanabe 2016 derive full static spherical Hassan–Rosen equations with **both matter sectors**, reducible to first-order radial equations plus an algebraic constraint.

### Dynamic spherical architecture already exists

Kocic–Torsello–Högås–Mörtsell, arXiv:1904.08617, provide full spherical standard-3+1 bimetric evolution and public GPLv3 code:

`nubirel/bim-solver`

Pinned upstream revision:

`8852e8e9921edeeedf1a447d3bf27b82ec24433c`

The public numerical implementation evolves matter only in `g`, but the bimetric geometry is already fully dynamical.

Current execution environment can inspect that repository through the GitHub connector but cannot clone/compile it locally. **Never claim that upstream C++ has been built or run here.**

## Gate A0 — initial constraints

`INITIAL_DATA_EXISTENCE = PASS`

Time-symmetric conformally-flat two-matter Hamiltonian constraints have regular positive solutions for a central f concentration plus external g shell.

Relevant files include:

- `numerics/twin_lane_emden_initial.py`
- `numerics/two_matter_initial_data.py`
- corresponding tests
- `research/V2_INITIAL_DATA_GATE.md`

Manual TDD evidence includes GREEN `3 passed` for the two-matter initial-data module. Reference conformal factors remained positive and close to unity in the baseline case.

Interpretation only:

- two-sector centre/wall initial geometry is not forbidden by the nonlinear constraints;
- this is **not** yet a cosmological void, evolution, attractor or stability proof.

## Twin-fluid patch is now source-level specified

See:

`research/V2_TWIN_FLUID_PATCH_SPEC.md`

Pinned upstream standard-3+1 files were inspected directly.

### New f Valencia state

Add an independent state such as

`Df,Sf,tauf,vf`

with its own RHS and radial derivatives. Never reuse g-fluid storage.

### Sector-symmetric f hydrodynamics

Use the exact f-geometry dual of the existing g Valencia dust equations.

Matter projections:

`rho_f^m=(Df+tauf)/(fA fB^2)`

`j_f^m=Sf/(fA fB^2)`

`J1_f^m=Sf vf/(fA fB^2)`

`J2_f^m=0`.

### Gravitational source corrections

Add exactly once:

`eq_f_rho += (Df+tauf)/(fA fB^2)`

`eq_f_j += Sf/(fA fB^2)`

`eq_f_JK += fAlp*(3Df-Sf*vf+3tauf)/(2 fA fB^2)`

`eq_f_JKD += fAlp*Sf*vf/(fA fB^2)`.

Do not patch unused `JK1/JK2` in the first implementation.

### Separation / mixed momentum corrections

In upstream conventions:

`base_p_f -> base_p_f - Sf/(fA*gA*gB^2*P_2_1(R))`

and the explicit matter piece of `C_3` becomes

`-k_g*k_f*(Sg+Sf)/(2*gB^2)`.

### Direct fSig matter source

Add

`-k_f*fAlp*Sf/(2*fB^3)`.

### State-machine locations

The independent f state must be added to:

- enum/storage;
- input list;
- evolved-GF list;
- output/diagnostics;
- `emitField`;
- radial derivatives;
- derived primitive velocity;
- origin parity;
- outer extrapolation.

## General twin-matter lapse — decisive implementation block

Primary source:

Kocic–Lundkvist–Torsello, *On the ratio of lapses in bimetric relativity*, arXiv:1903.09646.

With both matter sectors,

`0 = W_g alpha + W_f alpha_f`,

therefore

`W := alpha/alpha_f = -W_f/W_g`.

The published expressions contain both matter stress-energy tensors. Matter coupled to either metric affects the lapse of the other.

Exact duality:

`g <-> f`, `beta_(4-n) <-> beta_n`, `p <-> -p`, `W_g <-> -W_f`.

### Important source-localization result

At the pinned upstream revision, `pfD/pfS/pftau` occur only **four times** in the generated `eomLapseRatios.h`:

- monolithic `eq_gW`;
- monolithic `eq_fW`;
- runtime split `eq_gW_2`;
- runtime split `eq_fW_2`.

The standard solver actually reconstructs

`W = W0 + r(W1+r W2)`.

Thus explicit one-fluid matter dependence used at runtime is localized in the `W2` pair.

This makes a two-fluid extension tractable, but the exact dual transformation also changes powers of `R=fB/gB` and beta ordering. **Do not hand-simplify the generated expression.**

The authors published machine-readable Mathematica ancillary files. Obtain/translate those in the real fork if possible.

## Mean-gauge result

See:

`research/V2_MEAN_GAUGE_AND_LAPSE_REPRESENTATION.md`

The geometric-mean gauge does **not** bypass `W`.

Relations:

`H^2 lambda = alpha alpha_f`

`alpha^2 = H^2 lambda W`

`alpha_f^2 = H^2/(lambda W)`.

Decision:

`MEAN_GAUGE = RECOMMENDED_AFTER_W_IS_KNOWN`

A mean gauge is sector-symmetric and therefore attractive for the eventual wall experiment.

### New explicit branch gate

For a real mean lapse and same time orientation:

`W = -W_f/W_g > 0`.

Therefore monitor as physical/branch warnings:

- `W_g -> 0` with `W_f != 0`;
- `W_f -> 0` with `W_g != 0`;
- `W < 0`;
- simultaneous `W_g,W_f -> 0` as a special degenerate case requiring separate analysis.

A future wall is not accepted as regular merely because the metric components stay finite; `W` must remain finite and positive on the selected mean-time branch.

## Numerical-relativity feasibility

See:

`research/V2_NR_FEASIBILITY_AND_LAPSE_GATE.md`.

Search through 2026 found no published spherical Hassan–Rosen numerical evolution with independent dynamical matter fluids in both sectors that supersedes the planned experiment.

No general standard-3+1 no-go was found either.

Kocic 2019 shows the bimetric constraint violations form a first-order symmetric-hyperbolic system (assuming the field/matter equations), with characteristic cone given by the union of the two metric null cones.

Adding separately minimally coupled f matter does not itself introduce a new higher-derivative gravitational principal part.

This is only a **feasibility pass**, not proof that the chosen gauge-fixed wall evolution is stable or globally strongly hyperbolic.

Decision:

`FIRST_DYNAMIC_IMPLEMENTATION = STANDARD_3+1`, not cBSSN.

## Manual verification policy

Actions/workflows are disabled.

For new numerical behaviour:

1. write the failing test first;
2. observe RED;
3. implement minimally;
4. observe GREEN locally when possible;
5. record the exact output;
6. separately verify GitHub content/SHA after writes;
7. never describe a full branch as tested unless it was actually executed.

Previously recorded module-level passes include multiple 3- and 4-test suites, published-root regressions and the initial-data BVP. These are **not** full repository CI.

## NEXT ACTIONS — resume exactly here

### A1. Remove the general-lapse implementation block

Preferred route:

1. obtain the authors' machine-readable `bimetric-lapses-nr.m` / notebook source in a real fork environment;
2. generate the full two-matter `W_g,W_f`;
3. verify exact sector duality;
4. set all f-matter variables to zero and reproduce pinned upstream `eomLapseRatios.h` numerically;
5. set all g-matter variables to zero and verify the dual case;
6. both fluids on: verify secondary-constraint preservation;
7. use mean-lapse gauge only **after** this ratio is correct.

If ancillary source remains unavailable:

- reconstruct only the matter-dependent coefficient block from the compact published `c_i,d_i` equations with symbolic algebra;
- do not hand-copy the full generated C++ expression.

### A2. Materialize a GPL-compatible fork when an executable environment is available

1. pin upstream revision `8852e8e...`;
2. build untouched `bim-solver-STD`;
3. reproduce a one-fluid baseline;
4. write RED tests for f state / sector symmetry / lapse duality;
5. implement the source-level patch specified above;
6. require `T_f=0` regression against upstream.

### A3. Short dynamic wall experiment

Controls:

- vacuum;
- g-only shell;
- f-only centre;
- full twin centre+wall.

Use RK3/RK4, at least three resolutions/Courant factors.

Monitor:

- both Hamiltonian constraints;
- both momentum constraints;
- secondary constraint;
- `W_g,W_f,W`;
- separation `p`;
- metric positivity/determinants;
- square-root branch reality/causal compatibility;
- independent g/f rest masses;
- both fluid velocities.

Classify `DYNAMIC_WALL = PASS/PARTIAL/FAIL` only from resolution-convergent evidence.

### A4. Only if local wall survives

Construct the non-time-symmetric / FLRW exterior problem with consistent extrinsic curvature and separation. Do not return to an ad-hoc `K=-3H` Lane–Emden slice.

### B. Stability

Apply the general spherical perturbation/principal-symbol machinery to the actual evolved wall. Reject unavoidable ghost or gradient instability.

### C. Formation / attractor

Prove ordinary initial conditions can **generate** the anti-correlated state. Existence of tuned initial data is not enough.

### D. Observables

Only after A–C:

- visible velocity profile;
- `Psi_g`, `Phi_g`;
- Weyl/lensing profile;
- joint velocity-vs-lensing prediction;
- DESI/RSD/`E_G`/void lensing/BAO/SNe/CMB comparison.

## Stop / downgrade JANUS-R if

1. no regular gradient-resolved wall evolution exists;
2. every wall evolution has unavoidable ghost/gradient instability;
3. healthy solutions require forbidden early isocurvature;
4. healthy regions decouple the visible massive mode so strongly that the effect is negligible;
5. early screening also kills the desired late effect;
6. all acceptable solutions reduce observationally to GR+LambdaCDM with extra unconstrained parameters.

## Do not redo unless genuinely new mathematics appears

- exact universal `+G/-G` in the same linear two-metric architecture;
- fundamental negative mass as a required mechanism;
- isolated positive twin matter producing divergent negative photon lensing;
- viability judgments from `H(z)` alone;
- dimensional source endpoints interpreted as physical density contrast;
- algebraic root endpoints treated automatically as spacetime singularities;
- static Ricci-flat instability extrapolated blindly to a cosmological wall;
- ad-hoc expanding CMC Lane–Emden initial data;
- a twin lapse that ignores the published `W_g,W_f` relation;
- mean gauge used as if it removed the need for the dynamical lapse ratio.
