# Janus Research Resume Checklist

Date: 2026-10-11
Active branch: `research/v2-flrw`
Draft PR: `#1`
GitHub Actions / workflows: **disabled by user**. Do not rely on CI. Use local/manual verification and record exact outputs in PR comments or research notes.

## Purpose

This file is the restart point if the research session is interrupted. Resume from this file before doing new work.

## Current scientific state

1. `JANUS-EXACT` remains **NOT CLOSED** as a complete general-relativistic bimetric theory.
2. Main continuation is `JANUS-R`: ghost-free Hassan-Rosen-type bigravity, two positive-energy matter sectors, no literal negative-mass requirement.
3. Literal universal `+G/-G` and negative-lensing predictions are **not recovered** in the linear ghost-free two-metric mechanism.
4. Linear cross-sector repulsion exists but saturates at a weaker effective coupling; visible-matter dynamics and photon lensing respond differently.
5. A healthy-looking FLRW background can still fail perturbative stability. Background fit alone is not a pass.
6. The first FLRW regression point failed the `W>0` healthy/Higuchi diagnostic by about `z ~ 0.06`.
7. Exploratory scans show a strong **stability-vs-visible-mixing tension**: pushing the healthy regime to high redshift tends to move toward GR-like decoupling.
8. The nonlinear Aoki-Maeda-Namba scalar equation provides a real possible escape: early nonlinear/Vainshtein behavior can restore a GR-like phase in parameter regions where linear theory is unhealthy.
9. Previous fixed-`H` source-threshold interpretation was too pessimistic physically: the source variable has dimensions. A failure around `s ~ 0.476` at `H^2=0.01` corresponds to an order-`delta ~ tens` source, far beyond ordinary void contrast. This must be retested on a cosmological trajectory.

## Mandatory resume order

### Step 1 — Re-read these files

- `research/STATE.md`
- `research/VERDICT_V1.md`
- `research/V2_LINEAR_GATE.md`
- `research/V2_STABILITY_MIXING_TENSION.md`
- `research/V2_NONLINEAR_SOURCE_GATE.md`
- `research/NONLINEAR_TWIN_SCREENING.md`
- `research/NEXT_TESTS.md`

### Step 2 — Verify branch state

Confirm:

- branch is `research/v2-flrw`;
- PR #1 is still draft/open;
- branch has not been merged to `main`;
- no newer commit invalidates this checklist.

### Step 3 — Manual test policy

Because GitHub Actions/workflows are disabled:

- write tests first for new numerical behavior;
- run them locally in the available Python environment when possible;
- record exact pass/fail output;
- do **not** claim full-branch verification if the repository cannot be cloned/executed directly;
- verify GitHub file contents and SHAs separately after writes.

Known local verification already performed in this research line:

- asymmetric two-fluid control: RED before implementation, then `3 passed` after implementation;
- published Aoki-Maeda-Namba scalar roots reproduced in the diagnostic code.

## Immediate next scientific action

### Gate A — Cosmological nonlinear trajectory

Replace the fixed-`H`, fixed-dimensional-source continuation test with a trajectory parameterized by scale factor `a`:

1. choose a controlled matter-era background first;
2. evolve `H^2(a)` consistently (initially EdS-like `H^2 \propto a^-3`, then use the FLRW solver candidate);
3. evolve physical source terms as
   `source_g = kappa_g^2 rho_g delta_g`,
   `source_f = K^2 kappa_f^2 rho_f delta_f`;
4. use realistic contrasts, respecting `delta_g >= -1` for a visible void;
5. track the same real nonlinear root continuously as both `H/m` and the relative source change;
6. detect root mergers, singular jumps, and branch loss;
7. compare Case A and Case B and then scan nearby parameters.

Primary question:

> Does a continuous real branch exist from an early GR-like nonlinear phase to a late Janus-like anti-correlated configuration for physically realistic density contrasts?

### Gate B — Stability along that trajectory

For any branch surviving Gate A, evaluate or derive the available kinetic/gradient diagnostics along the path. A real algebraic root alone is not enough.

Reject a trajectory if it necessarily crosses:

- ghost / wrong kinetic sign;
- `c_s^2 < 0` gradient instability;
- lapse singularity;
- disconnected branch / unavoidable complexification.

### Gate C — Dynamical generation

If a stable path exists, test whether ordinary initial conditions can actually generate the anti-correlated mode, rather than merely permit it.

Required distinction:

- `existence of a nonlinear solution` != `cosmological attraction toward that solution`.

Build the minimal time-dependent perturbation reduction only after Gate A shows a physically relevant continuous branch.

### Gate D — Observable consequence

Only after A-C:

- compute visible peculiar velocities;
- compute `Psi_g`, `Phi_g`, Weyl potential;
- derive lensing/dynamics mismatch;
- compare to DESI / void lensing / `E_G` constraints.

## Stop / downgrade conditions

Strongly downgrade or reject JANUS-R as a continuation of Petit's segregation idea if:

1. every physically realistic anti-correlated trajectory loses the stable branch;
2. surviving branches require early relative/isocurvature amplitudes already incompatible with observations;
3. all cosmologically healthy regions suppress visible mixing so strongly that the late effect is negligible;
4. nonlinear screening protects early cosmology only by also suppressing the desired late segregation;
5. the only acceptable parameter regions reduce observationally to GR + LambdaCDM with extra unconstrained parameters.

## Things NOT to redo unless new mathematics appears

- do not spend time trying to restore literal universal `+G/-G` in the same linear two-metric setup;
- do not assume fundamental negative mass is required;
- do not claim isolated positive-energy twin matter gives divergent/negative photon lensing;
- do not judge viability from `H(z)` alone;
- do not interpret dimensionful source thresholds as density contrasts without dividing by the appropriate background gravitational scale.

## Repository discipline

For every meaningful new result:

1. add or update a research Markdown note;
2. add numerical code only when it answers a falsification question;
3. add a regression test before implementation when changing behavior;
4. record corrections to previous conclusions explicitly;
5. keep PR #1 draft until a real stable parameter map exists.
