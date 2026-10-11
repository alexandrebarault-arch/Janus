# V2 A1 — Twin-fluid source preparation checkpoint

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `SOURCE_PATCH_PREPARED__UPSTREAM_COMPILE_NOT_RUN`

Read `RESUME.md` first. This file records the work completed after the last RESUME checkpoint.

## 1. What is now prepared

The pinned numerical-relativity target remains:

`nubirel/bim-solver@8852e8e9921edeeedf1a447d3bf27b82ec24433c`

The standard 3+1 solver is still the first implementation target. BSSN/cBSSN is deferred until the first wall experiment is reproduced.

Three independent source patchers now cover the minimal twin-dust extension:

1. `tools/apply_twin_fluid_state_patch.py`
   - registers `pfFD,pfFS,pfFtau,pfFv` and derivatives/RHS;
   - adds the f fluid to `bimInput`, `bimEvolvedGF`, outputs and cached fields;
   - computes the f primitive velocity;
   - applies center parity and outer extrapolation;
   - evaluates radial derivatives and f-fluid RHS.

2. `tools/apply_twin_fluid_patch.py`
   - adds f-sector Valencia dust equations;
   - adds direct f matter to `f_rho`, `f_j`, `f_JK`, `f_JKD`;
   - adds f momentum to the mixed momentum constraint and `base_p_f`;
   - adds the direct f momentum source to `fSig_t`.

3. `tools/apply_twin_lapse_patch.py`
   - preserves the complete generated upstream lapse expressions;
   - adds only the previously derived f-dust blocks to `eq_gW_2` and `eq_fW_2`;
   - uses the exact sector-duality formulas documented in `research/V2_TWIN_LAPSE_MATTER_DUALITY.md`.

A one-command coordinator exists:

`tools/prepare_bim_solver_twin.py`

It verifies the exact audited upstream blobs first, then applies the state, equation/source and lapse patches.

## 2. Upstream source manifest

`tools/verify_upstream_manifest.py` pins the Git blob SHA of every file modified by the patch:

- `src/bim-solver-std.cpp`
- `include/eom-std/eomMatter.h`
- `include/eom-std/eomSources.h`
- `include/eom-std/eomConstraints.h`
- `include/eom-std/eomMiscEquations.h`
- `include/eom-std/eomEvolution.h`
- `include/eom-std/eomLapseRatios.h`

The preparer must refuse a checkout whose audited files differ from these blobs.

## 3. Initial-data file interface resolved

The upstream `GridInitialData` reader loads, for every interior radial cell,

`r` followed by the fields in `fld::bimInput` order.

After the twin-fluid state patch this is 25 state columns, hence **26 columns including `r`**.

`numerics/bim_solver_twin_input.py` implements this mapping in readable text form (`input.binary=false`).

For the time-symmetric conformally-flat initial slice:

- cell centers: `r_i=(i+1/2) delta_r`;
- `gA=gB=psi_g^2`, `fA=fB=psi_f^2`;
- `gDA=gDB=2 psi_g'/psi_g`, `fDA=fDB=2 psi_f'/psi_f`;
- `gSig=fSig=0` because the regularized variable is `sigma=(A-B)/r`;
- `gK=gKD=fK=fKD=0`;
- `q=p=0`;
- rest dust: `pfS=pftau=pfFS=pfFtau=0`;
- `pfD=D_g`, `pfFD=D_f`;
- choose the initial gauge `gAlp=1`, `fAlp=1/W`, `gDAlp=0`, where `W=alpha_g/alpha_f` is supplied by the already validated time-symmetric lapse gate.

The paper's regularization definition `sigma=(A-B)/r` and the conserved-density identity `rho=D psi^{-6}` confirm this mapping for conformally-flat rest dust.

## 4. Manual TDD evidence

GitHub Actions/workflows remain disabled. These are local module-level checks, **not a full C++ regression**.

### Equation/source patcher

RED: module absent.

GREEN: `4 passed in 0.03s`.

### State-registration patcher

GREEN after implementation: `2 passed in 0.03s`.

### Lapse patcher

Initial RED: module absent.

First GREEN exposed an insufficient test. A new balanced-delimiter regression was added and correctly failed because the first C++ transcription of `Delta Wf2[f]` contained an extra parenthesis.

After correction:

`4 passed in 0.03s`.

This correction is important: only the corrected version was pushed.

### Upstream manifest verifier

RED: module absent.

GREEN: `2 passed in 0.03s`.

### One-command preparer

RED: module absent.

GREEN: `1 passed in 0.03s`.

### Twin-fluid input exporter

RED: module absent.

GREEN: `3 passed in 0.03s`.

## 5. What has NOT been demonstrated

Do not upgrade the scientific verdict from these patchers.

Still not run in this environment:

- a materialized checkout of the full upstream source;
- untouched upstream `bim-solver-STD` compilation;
- application of the three patchers to the complete real checkout;
- patched C++ compilation/link;
- `f-matter=0` exact numerical regression against upstream;
- twin-sector randomized duality regression inside the compiled code;
- any time evolution of the Janus-like compensation wall.

The network/tool environment currently cannot clone/download the complete upstream repository, and the GitHub connector cannot create/fork repositories. Therefore the present gate is a reproducible **source-preparation pass**, not an executable NR pass.

## 6. Exact restart procedure when a checkout is available

From the `Janus` repository root:

1. obtain `nubirel/bim-solver` at exactly
   `8852e8e9921edeeedf1a447d3bf27b82ec24433c`;
2. compile **untouched** `bim-solver-STD` first;
3. reproduce one published/upstream one-fluid baseline;
4. verify the source manifest with `tools.verify_upstream_manifest`;
5. apply the source patch with `tools.prepare_bim_solver_twin`;
6. compile the patched STD solver;
7. run with `pfFD=pfFS=pfFtau=0` and require regression to the one-fluid baseline;
8. export the reference twin wall as text with `input.binary=false` using `numerics/bim_solver_twin_input.py` plus the existing initial-constraint/lapse modules;
9. evolve only a short interval first;
10. monitor constraints, lapse sign, causal type, `R=fB/gB`, `p`, both densities, and the compensation/transition wall.

## 7. Scientific next gate

The decisive question has not changed:

> Does a regular twin-matter spherical evolution cross the compensation/branch-transition wall while preserving the constraints and a positive same-oriented lapse ratio?

If the patched solver cannot pass the zero-f regression, stop before interpreting physics.

If zero-f passes but every physically relevant twin wall immediately develops a lapse/constraint/causal pathology, strongly downgrade JANUS-R.

If a regular short evolution exists, proceed to convergence/refinement and only then to the stability and cosmological gates in `RESUME.md`.
