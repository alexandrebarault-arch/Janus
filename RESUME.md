# Janus Research Resume Checklist

Date: 2026-10-11
Active branch: `research/v2-flrw`
Draft PR: `#1`
GitHub Actions / workflows: **disabled by user**. Do not rely on CI. Use local/manual verification and record exact outputs in PR comments or research notes.

## Purpose

This file is the authoritative restart point if the research session is interrupted. Read it before doing new work.

## Current scientific state

1. `JANUS-EXACT` remains **NOT CLOSED** as a complete general-relativistic bimetric theory.
2. Main continuation is `JANUS-R`: ghost-free Hassan-Rosen-type bigravity, two positive-energy matter sectors, no literal negative-mass requirement.
3. Literal universal `+G/-G` and negative-lensing predictions are **not recovered** in the linear ghost-free two-metric mechanism.
4. Linear cross-sector repulsion exists but saturates at a weaker effective coupling; visible-matter dynamics and photon lensing respond differently.
5. A healthy-looking FLRW background can still fail perturbative stability. Background fit alone is not a pass.
6. Exploratory scans show a strong **stability-vs-visible-mixing tension**: pushing the healthy linear regime to high redshift tends to move toward GR-like decoupling.
7. Universal linear JANUS-R strong enough to flip the twin perturbation also over-amplifies visible growth in the toy model and is strongly disfavored as the main mechanism.
8. The only serious surviving route is **environment-dependent nonlinear JANUS-R**: ordinary/common regions remain GR-like while a strong relative two-sector environment can enter a different nonlinear response.
9. Aoki-Maeda-Namba (2015) provides a concrete nonlinear scalar equation with both matter sectors; visible void + twin overdensity adds in the relative source.
10. The fixed-`H` source endpoint near `s~0.476` was dimensionful and must not be interpreted as a realistic void-density threshold. Cosmological trajectory diagnostics supersede that interpretation.
11. Higuchi/Compton scaling implies that a void-scale massive mode (`lambda_g ~ 50-200 Mpc`) naturally requires an early nonlinear phase and only enters a linearly healthy regime around roughly `z~8-22`.
12. Static screening depends on the **weighted relative mass** `|G_g M_g - K^2 G_f M_f|`, not the total mass.
13. For `lambda_g=100 Mpc`, an order-unity relative contrast today has `R_V/R << 1` in the static scaling, while screening can be much stronger near the early transition. A late release of the relative mode is therefore plausible at the scaling level.
14. In the Case-A static positive-source diagnostic (`beta2=-3`, `beta3=3`, equal couplings, `K=1`), branch topology changes with local twin/visible source ratio. The numerical exchange is around `q~1.325` in that normalization. This is environmental selectivity, not a universal constant.
15. For the physically relevant **visible void (`M_g<0`) + twin overdensity (`M_f>0`)** sign choice, the asymptotically homothetic algebraic branch develops a double-root endpoint near `R~2.7 R_V`. This means the algebraic/small-gradient approximation fails and a gradient-resolved transition layer is required; it is not proof of a physical singularity there.
16. Aoki-Mizuno (2016) show that the conventional static Ricci-flat Vainshtein solution is ghost/gradient unstable in their effective analysis, including vector perturbations for their worked spherical background. This is a serious caveat but does not directly exclude a cosmological void on a non-Ricci-flat FLRW background with both matter sectors.
17. The likely danger is concentrated in the **void compensation / branch-transition wall**, where gradients, Weyl curvature and scalar/vector mixing become important.
18. Brizuela-de Cesare-Soler Oficial (2024) provide a general perturbation formalism for arbitrary spherically symmetric bimetric backgrounds. It is the right stability machinery **after** a genuine gradient-resolved background has been constructed. Do not conflate AMN `non-homothetic` with their worked `nonbidiagonal` vacuum subclass.
19. A shortcut based only on a static scalar Stückelberg kinetic matrix was tried conceptually and rejected as insufficient: it does not reproduce the known stable nonlinear cosmological branch, showing that temporal/vector Stückelberg structure matters.

## Mandatory resume order

### Step 1 — Re-read these files

Highest priority:

- `RESUME.md`
- `research/V2_ENVIRONMENTAL_SCREENING.md`
- `research/V2_STATIC_VOID_GATE.md`
- `research/V2_COSMIC_TRANSITION_GATE.md`
- `research/V2_GOLDILOCKS_AND_GLOBAL_GROWTH.md`
- `research/V2_STABILITY_MIXING_TENSION.md`
- `research/NONLINEAR_TWIN_SCREENING.md`

Then background state if needed:

- `research/STATE.md`
- `research/VERDICT_V1.md`
- `research/V2_LINEAR_GATE.md`
- `research/NEXT_TESTS.md`

### Step 2 — Verify branch state

Confirm:

- branch is `research/v2-flrw`;
- PR #1 is still draft/open and unmerged;
- compare branch against `main`;
- read recent commits if the branch advanced after this file;
- never overwrite newer work based only on this checklist.

### Step 3 — Manual test policy

Because GitHub Actions/workflows are disabled:

- write tests first for new numerical behavior;
- run them locally in the available Python environment when possible;
- record exact RED and GREEN outputs;
- do **not** claim full-branch verification if the repository cannot be cloned/executed directly;
- verify GitHub file contents and SHAs separately after writes.

Known manual verifications already performed in this research line include:

- asymmetric two-fluid control: RED -> GREEN `3 passed`;
- cosmological nonlinear trajectory: RED -> GREEN `3 passed`;
- Higuchi scale window: RED -> GREEN `3 passed`;
- late sign-flip control: RED -> GREEN `3 passed`;
- self-consistent transition: RED -> GREEN `4 passed`;
- static Case-A branch selection: RED -> GREEN `4 passed in 0.75s`;
- environmental screening scaling: RED `ModuleNotFoundError` -> GREEN `3 passed in 0.03s`;
- published Aoki-Maeda-Namba scalar roots reproduced in the diagnostic code.

These are module-level/manual checks, not a verified full repository suite.

## Immediate next scientific action — decisive wall gate

### Gate A — Find/derive the full spherical background equations with gradients

Do **not** add another algebraic root scan.

1. Search primary literature for full static/dynamical spherically symmetric Hassan-Rosen field equations that retain radial gradients, especially:
   - relativistic stars in bigravity;
   - Lemaître/LTB-type bimetric cosmologies;
   - generic spherically symmetric bimetric constraints/Bianchi equations.
2. Prefer adapting a published full ODE/PDE system over deriving everything from scratch.
3. Extend to **two separately coupled matter sectors** if the published system has only `g`-matter.
4. Construct a smooth compensated visible `g`-void plus twin `f`-overdensity with asymptotic FLRW exterior.
5. Resolve the branch-transition wall rather than imposing an algebraic `mu(R)` root through it.

Primary question:

> Does a regular gradient-resolved spherical background exist that connects a Janus-like relative interior/void environment to the homogeneous GR-like exterior?

Fail condition: no regular connection exists for physically relevant void parameters without lapse/metric singularity or branch breakdown.

### Gate B — Full perturbative stability of the resolved wall

Only after Gate A supplies a genuine background:

1. linearize axial and polar perturbations using the general spherical formalism of Brizuela et al. (2024) or an equivalent derivation;
2. include both matter sectors in the source/perturbation system;
3. identify all seven bimetric gravitational degrees of freedom;
4. inspect kinetic signs and principal radial/angular propagation speeds through the wall;
5. reject on any unavoidable ghost or `c_s^2<0` gradient instability.

### Gate C — Dynamical generation / attractor question

If A-B pass:

- show that ordinary initial conditions actually evolve toward the anti-correlated environment;
- distinguish `existence of a solution` from `dynamical attraction toward it`;
- evolve through the early nonlinear phase and transition to the late localized branch.

### Gate D — Observable consequence

Only after A-C:

- compute visible peculiar acceleration/velocity;
- compute `Psi_g`, `Phi_g`, Weyl potential and lensing;
- predict the relation between void velocity and lensing profiles;
- compare to DESI full-shape/RSD, `E_G`, CMB/galaxy void lensing, BAO/SNe/CMB as appropriate.

## Stop / downgrade conditions

Strongly downgrade or reject JANUS-R as a continuation of Petit's segregation idea if any of the following holds:

1. no regular gradient-resolved void/exterior matching exists;
2. every matching solution has a ghost or gradient instability in the transition wall;
3. the only stable solutions require early relative/isocurvature amplitudes already incompatible with observations;
4. all cosmologically healthy regions suppress visible mixing so strongly that the late effect is negligible;
5. nonlinear screening protects early cosmology only by also suppressing the desired late segregation;
6. acceptable parameter regions reduce observationally to GR + LambdaCDM with extra unconstrained parameters.

## Things NOT to redo unless new mathematics appears

- do not spend time trying to restore literal universal `+G/-G` in the same linear two-metric setup;
- do not assume fundamental negative mass is required;
- do not claim isolated positive-energy twin matter gives divergent/negative photon lensing;
- do not judge viability from `H(z)` alone;
- do not interpret dimensional source thresholds as density contrasts without normalization;
- do not use the AMN algebraic endpoint as if it were a physical singularity;
- do not apply the Aoki-Mizuno Ricci-flat no-go indiscriminately to non-Ricci-flat cosmological void interiors;
- do not apply Brizuela's specific nonbidiagonal worked-background results to AMN non-homothetic backgrounds without establishing equivalence.

## Repository discipline

For every meaningful new result:

1. add or update a research Markdown note;
2. add numerical code only when it answers a falsification question;
3. add a regression test before implementation when changing behavior;
4. record corrections to previous conclusions explicitly;
5. keep PR #1 draft until the transition-wall background and stability gates are genuinely addressed;
6. because Actions are disabled, never infer test status from workflow badges/runs.
