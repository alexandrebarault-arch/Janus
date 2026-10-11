# Janus Research Resume Checklist

Date: 2026-10-11
Active branch: `research/v2-flrw`
Draft PR: `#1` — keep open/draft, do not merge yet
GitHub Actions / workflows: **disabled by user**. Never infer verification from CI.

## Purpose

This is the authoritative restart point after any interruption. Read this file first, then follow the exact order below. Do not restart old algebraic scans or reinterpret superseded thresholds.

## Current scientific state

1. `JANUS-EXACT` remains **NOT CLOSED** as a complete generally covariant nonlinear bimetric theory.
2. Main continuation is `JANUS-R`: ghost-free Hassan-Rosen bimetric gravity, two positive-energy matter sectors, no fundamental negative-mass requirement.
3. Literal universal `+G/-G` and isolated negative photon lensing are **not recovered** in the healthy linear two-metric mechanism.
4. Linear cross-sector repulsion exists but asymptotes to a weaker coupling (`-G/3` in the symmetric normalization), while lensing and slow-matter dynamics differ.
5. Linear relative-mode growth is too weak to manufacture dramatic late segregation from an arbitrarily tiny seed unless non-homothetic sourcing or nonlinear evolution matters.
6. A good FLRW `H(z)` is not a stability pass. The first Lambda-CDM-like regression point failed the healthy/Higuchi diagnostic already near low redshift.
7. Exploratory scans show a strong **stability-vs-visible-mixing tension**: pushing the linearly healthy regime earlier drives the theory toward GR-like decoupling.
8. The only serious surviving route is **environment-dependent nonlinear JANUS-R**: common environments remain GR-like while a strong relative two-sector environment can excite a different nonlinear branch.
9. Aoki-Maeda-Namba (2015) provide the key seventh-order nonlinear scalar equation with both matter sectors. A visible underdensity plus twin overdensity adds coherently to its relative source.
10. Fixed-`H` source thresholds are dimensionful and must not be interpreted directly as density-contrast thresholds.
11. Higuchi/Compton scaling for a void-scale massive mode (`lambda_g ~ 50-200 Mpc`) naturally points to an early nonlinear phase and a later release toward a linearly healthy regime.
12. Static screening is controlled by weighted **relative** source/mass, not total visible density alone.
13. Algebraic/static Case-A diagnostics found environment-dependent branch selection; this is not a universal constant of the theory.
14. For the physically relevant visible-under-density / twin-overdensity sign, the algebraic small-gradient approximation develops a double-root endpoint near the compensation/transition wall. Treat this as **breakdown of the algebraic approximation**, not proof of a physical singularity.
15. Aoki-Mizuno (2016) found ghost/gradient problems for their static Ricci-flat Vainshtein background. This is a major warning but not a proof against a non-Ricci-flat cosmological two-matter void.
16. Brizuela-de Cesare-Soler Oficial (2024) provide general perturbation machinery for arbitrary spherical bimetric backgrounds. Use it only after a genuine gradient-resolved background is available.

## New decisive progress: full spherical equations exist

### Aoki-Maeda-Tanabe 2016

`Relativistic stars in bigravity theory`, Phys. Rev. D 93, 064054, arXiv:1602.02227.

They already derive the full static bidiagonal spherical Hassan-Rosen equations **with both matter sectors present**:

- radial Einstein equations for `g` and `f`;
- both matter conservation equations;
- bimetric Bianchi/secondary constraint;
- reduction to seven first-order ODEs plus one algebraic constraint.

Therefore Gate A does **not** require deriving the full radial field equations from scratch.

### Kocic-Torsello-Hogas-Mortsell 2020

`Initial data and first evolutions of dust clouds in bimetric relativity`, CQG 37, 165010, arXiv:1904.08617.

They provide the correct **dynamic** architecture:

- full spherical `3+1` bimetric equations;
- nonbidiagonal relative-shift/separation variable;
- Hamiltonian, momentum and secondary constraints;
- numerical short-time dust evolution;
- no simple analytic LTB analogue in bimetric gravity.

Open-source implementation:

`https://github.com/nubirel/bim-solver`

The solver already implements the gravitational `3+1`/cBSSN machinery and Valencia hydrodynamics for the `g` sector.

## Exact twin-fluid extension point in `bim-solver`

Fetched upstream file:

`include/eom-BSSN/eomBSSNMatterReg.h`

The `g`-fluid Valencia equations are implemented, while the current `f`-matter source functions explicitly return zero:

- `eq_pf_frho`
- `eq_pf_fj`
- `eq_pf_fJ11`
- `eq_pf_fJ22`

However, **do not make a fake four-line patch**. The existing single-fluid variables (`pfD`, `pfS`, `pftau`, `pfv`) also enter:

- radial derivative descriptors;
- lapse-ratio expressions;
- standard and cBSSN evolution code;
- generated DIRK Jacobians;
- initial-data paths.

A real twin-fluid implementation requires a second conserved-variable set and consistent updates to all generated/implicit-solver dependencies.

The upstream code is GPLv3. Do not vendor/copy it wholesale into this research repository without making the licensing consequence explicit. Prefer a separate fork when implementation starts.

## Gate A0 — constrained Janus-like initial data: PASS

New files on this branch:

- `numerics/twin_lane_emden_initial.py`
- `tests/test_twin_lane_emden_initial.py`
- `research/V2_FULL_SPHERICAL_GATE.md`

Using the time-symmetric conformally-flat constraint reduction of Kocic et al. and adding the symmetric `f`-matter term to the second Hamiltonian constraint, we solved coupled generalized Lane-Emden equations for:

- positive central `f`-matter concentration;
- positive compensating `g` shell;
- asymptotic bi-Minkowski boundary;
- positive regular conformal factors `psi_g`, `psi_f`.

Manual TDD verification:

- RED before implementation: `ModuleNotFoundError`
- GREEN after implementation: `3 passed in 0.48s`

Result:

`JANUS_LIKE_INITIAL_DATA_EXISTENCE = PASS`

Interpretation: the desired central twin concentration + visible wall is **not forbidden by the time-symmetric elliptic constraints**.

This does **not** prove formation, evolution, stability, FLRW embedding or phenomenological viability.

## Why an ad-hoc expanding CMC shortcut is rejected

At time symmetry (`K_ij=0`, zero fluid velocity, separation parameter `p=0`), momentum constraints and the secondary bimetric constraint vanish automatically.

For an expanding slice (`K_ij != 0`) they do not. If the local spatial ratio `f/g` varies through the wall, simply imposing homogeneous `K=-3H` independently in both metrics generally fails the coupled momentum/secondary constraints.

Therefore do **not** manufacture a pseudo-FLRW initial slice by inserting constant extrinsic curvature into the Lane-Emden equations alone. Expanding initial data require the full 3+1 constraint system, including relative shift/separation and extrinsic-curvature profiles.

## Solver-status caveat

The published 2020 evolutions were short-time evolutions in standard 3+1. The authors explicitly treated long-term stable bimetric evolution as ongoing work and pointed to cBSSN as the more promising formulation.

The public `bim-solver` is a research codebase, not a production numerical-relativity package. The strong-hyperbolicity/well-posedness status of full bimetric cBSSN is not as settled as in GR. Treat any future evolution as an R&D diagnostic requiring aggressive constraint monitoring.

## Mandatory resume order

### Step 1 — Read these files

Highest priority:

- `RESUME.md`
- `research/V2_FULL_SPHERICAL_GATE.md`
- `research/V2_ENVIRONMENTAL_SCREENING.md`
- `research/V2_STATIC_VOID_GATE.md`
- `research/V2_COSMIC_TRANSITION_GATE.md`
- `research/V2_GOLDILOCKS_AND_GLOBAL_GROWTH.md`
- `research/V2_STABILITY_MIXING_TENSION.md`
- `research/NONLINEAR_TWIN_SCREENING.md`

Then if needed:

- `research/V2_LINEAR_GATE.md`
- `research/STATE.md`
- `research/VERDICT_V1.md`
- `research/NEXT_TESTS.md`

### Step 2 — Verify repository state

- confirm active branch `research/v2-flrw`;
- confirm PR #1 remains draft/open/unmerged;
- compare against `main`;
- inspect commits newer than this file before writing;
- never overwrite newer work based on an older checkpoint.

### Step 3 — Verification policy

Because GitHub Actions/workflows are disabled:

- TDD for new numerical behavior where feasible;
- run module tests locally in the available Python environment;
- record exact RED/GREEN outputs;
- verify GitHub file content/SHA after writes;
- never claim full-repository verification unless it was actually executed.

Known manual checks include:

- asymmetric two-fluid control: `3 passed`;
- cosmological nonlinear trajectory: `3 passed`;
- Higuchi scale window: `3 passed`;
- late sign-flip control: `3 passed`;
- self-consistent transition: `4 passed`;
- static Case-A branch selection: `4 passed in 0.75s`;
- environmental screening scaling: RED `ModuleNotFoundError` -> GREEN `3 passed in 0.03s`;
- twin Lane-Emden initial data: RED `ModuleNotFoundError` -> GREEN `3 passed in 0.48s`;
- published Aoki-Maeda-Namba scalar roots reproduced.

These are module-level checks, not a full branch CI pass.

## Immediate next action — Gate A1/A2

### Gate A1 — twin-fluid full 3+1 initial state

Do **not** return to algebraic root scans.

1. Map `twin_lane_emden_initial.py` output to the 3+1 variables of `bim-solver`.
2. Specify a genuinely independent `f` Valencia dust state (`D_f, S_f, tau_f, v_f`) alongside the existing `g` state.
3. Enumerate every upstream file / generated Jacobian / lapse expression touched by the second-fluid state.
4. At first keep the initial slice time-symmetric so momentum and secondary constraints are analytically controlled.
5. Verify both Hamiltonian constraints against the Python BVP and verify all other constraints are numerically zero to tolerance.

### Gate A2 — short-time wall evolution

Only after A1:

- evolve the regular time-symmetric central-`f` / `g`-shell data for a short interval;
- compare to a one-fluid/GR control;
- monitor Hamiltonian + momentum + secondary constraints;
- monitor lapse ratio, metric determinants, null-cone configuration and matter conservation;
- detect shell crossing, zero lapse, branch loss or explosive constraint growth.

### Gate A3 — expanding cosmological embedding

Only after the local wall survives A2:

- solve full non-time-symmetric 3+1 constraints for an expanding exterior;
- include nonzero extrinsic curvature and separation/shift consistently;
- approach an FLRW exterior instead of asymptotic Minkowski;
- then evolve a compensated cosmic-void profile.

### Gate B — stability of the evolved wall

After a regular background exists:

- apply Brizuela et al. general spherical perturbation formalism or extract the principal symbol around the numerical background;
- track all seven bimetric gravitational degrees of freedom;
- reject unavoidable ghost or gradient instability.

### Gate C — attractor/generation

If A-B pass, test whether ordinary initial conditions **generate** the anti-correlated state rather than merely allowing it as fine-tuned initial data.

### Gate D — observations

Only after A-C:

- visible velocity/acceleration profile;
- `Psi_g`, `Phi_g`, Weyl/lensing profile;
- DESI RSD/full-shape, `E_G`, void lensing, BAO/SNe/CMB.

## Stop / downgrade conditions

Strongly downgrade/reject JANUS-R as a continuation of Petit's segregation idea if:

1. no regular gradient-resolved wall evolution exists;
2. every wall evolution has unavoidable ghost/gradient instability;
3. healthy solutions require forbidden early isocurvature;
4. healthy parameter regions decouple the visible massive mode so strongly that the effect is negligible;
5. early screening also kills the desired late effect;
6. viable solutions reduce observationally to GR + LambdaCDM with extra unconstrained parameters.

## Do not redo unless new mathematics appears

- literal universal `+G/-G` in the same linear two-metric architecture;
- fundamental negative mass as a required mechanism;
- isolated positive twin matter giving negative/divergent photon lensing;
- viability from `H(z)` alone;
- dimensional-source thresholds interpreted as density contrasts;
- algebraic root endpoints treated as physical singularities;
- static Ricci-flat no-go extrapolated blindly to a cosmological wall;
- ad-hoc constant-mean-curvature expanding Lane-Emden data that ignore momentum/secondary constraints.

## Repository discipline

For every meaningful result:

1. update a research Markdown note;
2. add code only when it answers a falsification question;
3. write a regression test before behavioral code changes when feasible;
4. explicitly record corrections to earlier conclusions;
5. keep PR #1 draft until dynamic wall + stability gates are genuinely passed;
6. do not rely on GitHub Actions while disabled.
