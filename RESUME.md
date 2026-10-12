# Janus Research — Authoritative Resume Checkpoint

Date: 2026-10-11
Active branch: `research/v2-flrw`
Draft PR: `#1` — keep open/draft and **do not merge yet**
Base: `main`
GitHub Actions/workflows: **disabled by user**. Never infer verification from CI.

## Resume protocol

After any interruption:

1. read this file first;
2. confirm PR #1 is still draft/open/unmerged;
3. compare `research/v2-flrw` against `main` and inspect commits newer than this file;
4. read `LATEST.md` and `research/VERDICT_V2_JANUS.md`;
5. read the authoritative notes listed below as needed;
6. resume from **NEXT ACTIONS**;
7. never overwrite newer branch work from chat memory;
8. record every meaningful correction/result in Git before moving on.

## Current headline verdict

### Literal Jean-Pierre Petit Janus

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`.

If forced into a binary true/false decision today, this research selects:

**MOST LIKELY FALSE OR FUNDAMENTALLY INCOMPLETE AS WRITTEN.**

Reason: Janus 2024 still leaves the exact general nonlinear cross-sector interaction tensor unspecified; several characteristic claims (fundamental negative mass, exact universal `+G/-G`, isolated negative photon lensing) are not recovered when the idea is rebuilt inside a modern ghost-free bimetric framework.

Authoritative conclusion:

- `research/VERDICT_V2_JANUS.md`

Do **not** spend further time trying to rescue literal negative-mass Janus unless genuinely new mathematics closes the nonlinear theory.

### Surviving R&D continuation

The only serious continuation is

`ENVIRONMENT_DEPENDENT_NONLINEAR_JANUS_R`:

- ghost-free Hassan–Rosen bigravity;
- two separately/minimally coupled positive-energy matter sectors;
- no required fundamental negative mass;
- no imposed universal `+G/-G` law;
- nonlinear screening required;
- decisive object = the radial compensation / transition wall.

Strong universal linear JANUS-R is downgraded because stability at early times tends to drive the visible massive-mode coupling toward a GR-like decoupling regime, while strong unscreened mixing is observationally conspicuous.

## Results not to redo

- constrained 2015 Janus variation does not uniquely derive two independent equations;
- Janus 2024 remains under-specified as a complete nonlinear theory;
- linear two-metric cross repulsion exists but approaches about `-G/3`, not `-G`;
- physical force-sign threshold is `mu r ~= 0.9612787631`;
- isolated positive twin matter does not produce negative/divergent photon lensing in the linear ghost-free mechanism;
- maximally unscreened symmetric relative mode grows only as `a^1.186...`;
- dynamics and photon lensing respond differently — potential observable;
- Lambda-CDM-like `H(z)` is easy and is not a viability test;
- fixed-H dimensional source endpoints are not density-contrast thresholds;
- algebraic branch endpoints are not automatically spacetime singularities.

## Nonlinear two-matter gate

Aoki–Maeda–Namba 2015 provide a concrete nonlinear scalar equation with both matter sectors.

Weighted relative source:

`S_rel ~ kappa_g^2 rho_g delta_g - K^2 kappa_f^2 rho_f delta_f`.

Visible underdensity + twin overdensity adds coherently.

The algebraic approximation can lose a root in the compensation wall, so the decisive next physical system requires **full radial gradients**.

## Full spherical architecture

### Static

Aoki–Maeda–Tanabe 2016 derive full static spherical Hassan–Rosen equations with both matter sectors.

### Dynamic

Kocic–Torsello–Högås–Mörtsell provide a full spherical standard-3+1 evolution architecture and public GPLv3 code:

`nubirel/bim-solver`

Pinned upstream revision:

`8852e8e9921edeeedf1a447d3bf27b82ec24433c`

The public implementation evolves matter only in `g`; the bimetric geometry is already dynamical.

Current environment can inspect upstream source through GitHub but cannot materialize/compile the entire GPL repository. **Never claim the upstream C++ has been built or run here.**

`FIRST_DYNAMIC_IMPLEMENTATION = STANDARD_3+1`.

## Gate A0 — initial constraints

`INITIAL_DATA_EXISTENCE = PASS`.

Regular time-symmetric conformally-flat two-matter constraints exist for

- central f concentration;
- external g shell;
- asymptotically flat exterior.

Two independent implementations/checks now exist in the branch, including `numerics/two_sector_initial_constraints.py`.

Newest local TDD check for that independent solver:

- RED: `ModuleNotFoundError` before implementation;
- GREEN: `3 passed in 0.51s`.

Exploratory positive-matter core/shell scan:

- moderate grid: `100/100` converged;
- deliberately strong grid: `47/48` converged.

This is **not** yet a cosmological void, an attractor, or a dynamical stability result.

## Twin-fluid standard-3+1 source patch

Authoritative spec:

`research/V2_TWIN_FLUID_PATCH_SPEC.md`.

Independent f Valencia state:

`Df,Sf,tauf,vf` + RHS and derivatives.

Matter projections:

`rho_f=(Df+tauf)/(fA fB^2)`

`j_f=Sf/(fA fB^2)`

`J1_f=Sf vf/(fA fB^2)`

`J2_f=0`.

Required gravitational source additions:

`eq_f_rho += (Df+tauf)/(fA fB^2)`

`eq_f_j += Sf/(fA fB^2)`

`eq_f_JK += fAlp*(3Df-Sf*vf+3tauf)/(2 fA fB^2)`

`eq_f_JKD += fAlp*Sf*vf/(fA fB^2)`.

Separation/momentum additions:

`base_p_f -> base_p_f - Sf/(fA*gA*gB^2*P_2_1(R))`

and matter part of `C_3` becomes

`-k_g*k_f*(Sg+Sf)/(2*gB^2)`.

Direct fSigma source:

`-k_f*fAlp*Sf/(2*fB^3)`.

Do not patch unused `JK1/JK2` in first implementation.

## General twin-matter lapse — analytic block now resolved for dust

Primary relation:

`0 = W_g alpha + W_f alpha_f`

therefore

`W := alpha/alpha_f = -W_f/W_g`.

Mean gauge does **not** bypass this ratio.

For same time orientation require

`W>0`.

### Exact f-dust matter additions derived

Authoritative note:

`research/V2_TWIN_LAPSE_MATTER_DUALITY.md`.

Code/tests:

- `numerics/lapse_matter_duality.py`
- `tests/test_lapse_matter_duality.py`.

Define

`R=Bf/Bg`,

`P=b1+2 b2 R+b3 R^2`,

`Qf=b1+b2 R`,

`C=b1-b3 R^2`.

Missing f-dust runtime W2 additions are

`Delta Wg2[f] = - k_f Ag^2 Af^2 (1+p^2) P Qf (Df+tauf)/R^5`

and

`Delta Wf2[f] = k_f Ag^2 Af^2 (1+p^2) P/(2R^6)`

` * [lambda C (Df-Sf vf+tauf) + 2 Ag R Qf (Sf vf + p^2(Df+Sf vf+tauf))]`.

These were obtained by applying exact published sector duality to the isolated upstream g-matter block with `Bg,Bf` kept independent before reintroducing `R`.

Verification:

- independent symbolic differences simplify to zero;
- TDD GREEN: `3 passed in 0.03s`.

Updated status:

`GENERAL_TWIN_LAPSE_MATTER_EXTENSION = DERIVED`

`GENERAL_TWIN_LAPSE_CXX_REGRESSION = NOT RUN`.

The authors' ancillary symbolic source is now a desirable cross-check, not a strict analytic blocker for pressureless twin dust.

## Gate A0+ — initial lapse branch

Authoritative notes/code:

- `research/V2_INITIAL_LAPSE_GATE.md`
- `numerics/time_symmetric_lapse_gate.py`
- `tests/test_time_symmetric_lapse_gate.py`.

At time symmetry/rest dust:

`p=K=KD=S=tau=0`,

so the pinned upstream reconstruction reduces to

`Wg=Wg0+r^2 Wg2`,

`Wf=Wf0+r^2 Wf2`.

A source-transcription bug was caught by TDD: upstream `eq_gW_2` is `-A-B+...`, not `-(A-B+...)`.

After the single sign correction:

`3 passed in 0.52s`.

Reference initial wall:

`W_min ~= 0.795`

`W_max ~= 1.178`

`W_outer ~= 1.000000003`.

Refinement from 300 to 800 radial points preserves these values.

Decision:

`REFERENCE_INITIAL_LAPSE_BRANCH = PASS_PRE_EVOLUTION`.

This means the reference wall does not begin on an obviously forbidden lapse/secondary-constraint branch. It says nothing yet about later evolution.

## Initial lapse basin map

Authoritative note/code:

- `research/V2_INITIAL_LAPSE_BASIN.md`
- `numerics/initial_lapse_family_scan.py`
- `tests/test_initial_lapse_family_scan.py`.

Combined local initial-lapse tests:

`6 passed in 0.65s`.

### Amplitude basin

Independent f-centre and g-shell multipliers `0.25..8`:

- `36/36` constraint solutions converged;
- `36/36` kept `W>0`;
- minimum W in grid about `0.70`.

With f centre fixed, increasing the g shell as high as `128x` remained on the positive initial lapse branch in this diagnostic.

With g shell fixed, increasing the f centre eventually exits the branch:

- safe through about `12x` reference f amplitude;
- shortly above, `W_g` develops radial zeros and a finite `W<0` interval;
- clearly forbidden by `16x`.

The exact onset is not promoted as a universal physical threshold because one near-origin zero is inner-grid sensitive. A second finite-radius zero is stable under `r_min` variation, so the forbidden interval itself is real in the diagnostic.

### Beta map

Reference matter profiles; `beta1=1`; interaction `0.02`.

Grid:

- `beta2=-0.40..+0.05` step `0.025`;
- `beta3=-0.25..+0.25` step `0.025`.

Results:

- Hamiltonian BVP converged: `399/399`;
- positive lapse branch: `351/399`;
- forbidden initial lapse branch: `48/399`.

Unsafe points form a structured band at more negative beta combinations. Representative classifications survive 260->600 radial-point refinement.

The failures occur inside the compensation wall. They are not explained by a trivial zero of `P=beta1+2 beta2 R+beta3 R^2`.

Decision:

`FINITE_INITIAL_LAPSE_BASIN = YES`

`LAPSE_BRANCH_FILTER_NONTRIVIAL = YES`

`TRANSITION_WALL_REMAINS_DECISIVE = YES`.

## Numerical-relativity feasibility

`research/V2_NR_FEASIBILITY_AND_LAPSE_GATE.md`.

No published spherical Hassan–Rosen numerical evolution with independent dynamical matter in both sectors was found through 2026 that supersedes this planned experiment.

No general standard-3+1 no-go was found either.

The bimetric constraint-propagation system is known to admit a symmetric-hyperbolic formulation under the field/matter equations. Adding separately minimally coupled f matter does not itself add a higher-derivative gravitational principal part.

This is only a feasibility result, not proof of wall stability.

## Manual verification policy

GitHub Actions/workflows are disabled.

For new numerical behaviour:

1. write a failing test first;
2. observe RED;
3. implement minimally;
4. observe GREEN locally when possible;
5. record exact output;
6. verify GitHub content/SHA separately;
7. never claim full-branch CI.

## NEXT ACTIONS — resume exactly here

### A1. Practical GPL fork / compile gate

Current blocker is now **practical, not analytic**.

Need a materialized GPL-compatible copy of pinned upstream `bim-solver` in an executable environment.

Then:

1. build untouched `bim-solver-STD`;
2. reproduce a one-fluid baseline;
3. write RED tests for independent f state, sector symmetry and lapse duality;
4. implement the patch from `V2_TWIN_FLUID_PATCH_SPEC.md`;
5. inject the derived f-dust W2 lapse additions;
6. demand exact/numerical `T_f=0` regression against upstream;
7. test sector-dual `T_g=0` case;
8. only then enable a two-fluid wall.

The current sandbox cannot download/compile the complete upstream repository; do not fake this step.

### A2. Short dynamic wall experiment

Controls:

- vacuum;
- g-only shell;
- f-only centre;
- full twin centre+wall.

Use at least three resolutions/Courant factors.

Monitor:

- both Hamiltonian constraints;
- both momentum constraints;
- secondary constraint;
- `W_g,W_f,W=-W_f/W_g`;
- require finite `W>0` on selected mean-time branch;
- separation `p`;
- metric positivity/determinants;
- square-root branch reality/causal compatibility;
- independent g/f rest masses;
- both fluid velocities.

Classify `DYNAMIC_WALL = PASS/PARTIAL/FAIL` only from resolution-convergent evidence.

### A3. Only if local wall survives

Construct a non-time-symmetric / FLRW exterior with consistent extrinsic curvature and separation. Do not return to an ad-hoc `K=-3H` Lane–Emden slice.

### B. Stability

Apply general spherical perturbation/principal-symbol machinery to the actual evolved wall. Reject unavoidable ghost or gradient instability.

### C. Formation / attractor

Show ordinary cosmological initial conditions can generate the anti-correlated state. Existence of tuned initial data is insufficient.

### D. Observables

Only after A–C:

- visible velocity profile;
- `Psi_g`, `Phi_g`;
- Weyl/lensing profile;
- joint velocity-vs-lensing prediction;
- DESI/RSD/`E_G`/void lensing/BAO/SNe/CMB comparison.

## Stop / downgrade JANUS-R if

1. no regular gradient-resolved dynamic wall exists;
2. every wall has unavoidable ghost/gradient instability;
3. healthy solutions require forbidden early isocurvature;
4. healthy regions suppress visible mixing until the effect is negligible;
5. early screening also kills the desired late segregation;
6. all acceptable solutions collapse observationally to GR+LambdaCDM with extra unconstrained parameters.
