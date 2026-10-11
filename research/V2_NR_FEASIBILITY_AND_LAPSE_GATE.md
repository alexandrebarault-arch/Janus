# V2 Numerical-Relativity Feasibility and Lapse Gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `NR_EXTENSION_JUSTIFIED__GENERAL_LAPSE_STILL_DECISIVE`

## 1. Question

Before investing in a twin-fluid fork of `bim-solver`, determine whether later work has produced either

1. an existing two-matter spherical numerical evolution we should reuse, or
2. a hyperbolicity / initial-value no-go that would make the proposed evolution scientifically pointless.

## 2. Literature result

A targeted search through 2026 did not identify a published spherical numerical-relativity evolution of Hassan-Rosen bigravity with **independent dynamical matter fluids in both metric sectors**.

The closest relevant pieces remain:

- Aoki & Maeda / Aoki-Maeda-Tanabe: twin-matter cosmology and static spherical solutions;
- Aoki-Maeda-Namba: nonlinear scalar/Vainshtein evolution diagnostics with both matter sectors;
- Kocic-Torsello-Hogas-Mortsell: full spherical 3+1 dust evolution, but matter only in g in the public numerical example/code;
- Brizuela-de Cesare-Soler Oficial (2024): perturbations on arbitrary spherical bimetric backgrounds, including dynamical ones, but not the requested nonlinear twin-fluid background evolution.

Thus the proposed twin-fluid extension is not an obvious duplication of an already-published solver.

## 3. Hyperbolicity / well-posedness status

Kocic, JHEP 10 (2019) 219 / arXiv:1804.03659 proves that, assuming the bimetric evolution equations and matter conservation laws hold, the bimetric constraint violations obey a homogeneous first-order **symmetric hyperbolic** system. Its characteristic cone is the union of the null cones of the two metrics.

The paper also explains why ordinary matter systems that themselves admit symmetric-hyperbolic form can be combined with the two Einstein sectors when the coupling to the metrics is lower differential order. In Hassan-Rosen theory the bimetric stress-energy is algebraic in the metrics.

Adding a separately minimally coupled f-fluid therefore does not, by itself, introduce a new higher-derivative principal part into the gravitational equations.

### Important limitation

This is **not** a proof that the particular gauge-fixed standard-3+1 twin-fluid evolution used in the future wall simulation is globally strongly hyperbolic in every state.

In particular:

- the 2019 covariant-BSSN paper explicitly did not claim general strong hyperbolicity under the same assumptions as GR;
- dust can develop caustics/shell crossing;
- the lapse-ratio denominator can become singular;
- the square-root / causal compatibility conditions of the two metrics must remain valid;
- the specific transition-wall background may have ghost/gradient instabilities even when the IVP architecture is legitimate.

The result is therefore a **feasibility pass**, not a wall-stability pass.

## 4. Why standard 3+1 remains the first implementation target

The pinned public solver already demonstrated short-term spherical bimetric evolution and its standard-3+1 constraint subsystem has the strongest published causal-propagation result relevant to our use case.

Accordingly:

`FIRST_DYNAMIC_IMPLEMENTATION = STANDARD_3+1`

not cBSSN.

cBSSN remains a later cross-check or upgrade after the twin-fluid physics is validated in the simpler standard formulation.

## 5. General lapse ratio is now the decisive implementation gate

The public solver uses a one-fluid specialization of the lapse-preservation condition. Kocic-Lundkvist-Torsello (CQG 36, 225013; arXiv:1903.09646) derive the general spherical result with both matter sectors:

`0 = W_g alpha + W_f alpha_f`

(up to their common normalization).

Therefore the ratio is fixed dynamically; it is not legal to choose both lapses independently.

The paper's compact formula organizes `W_g,W_f` into non-derivative coefficients plus radial-gradient terms. The coefficients are dual under

`g <-> f`, `beta_(4-n) <-> beta_n`, `p <-> -p`,

with

`W_g <-> -W_f`.

### Source-code localization result

Inspection of the pinned upstream `include/eom-std/eomLapseRatios.h` shows that the existing g-fluid variables (`pfD,pfS,pftau`) occur only four times in the entire generated file:

- once in the monolithic `eq_gW` expression;
- once in the monolithic `eq_fW` expression;
- once in the split runtime coefficient `eq_gW_2`;
- once in the split runtime coefficient `eq_fW_2`.

The runtime gauge calculation uses the split

`W = W0 + r (W1 + r W2)`

form. Hence all explicit one-fluid matter dependence relevant to the running lapse ratio is localized in the `W2` pair.

This is encouraging: the second-sector matter correction is structurally local rather than spread through the full generated geometry expression.

### Why it is still not hand-patched

The exact sector duality simultaneously transforms

- `g <-> f`;
- `R=fB/gB -> 1/R`;
- `beta_n <-> beta_(4-n)`;
- `p -> -p`;
- the matter projections and couplings.

A hand simplification of the large `W2` expression risks missing powers of `R` or signs. The authors supplied machine-readable Mathematica ancillary files for exactly this reason.

Therefore the production rule remains:

**do not manually transcribe or simplify the full Appendix-D lapse expression.**

## 6. Future lapse implementation test matrix

Once the symbolic source or a compilable external fork is available:

1. implement the general two-matter `W_g,W_f`;
2. verify the exact published sector duality on randomized regular states;
3. set all f-fluid variables to zero and reproduce the pinned upstream `W_g,W_f` to floating-point tolerance;
4. set all g-fluid variables to zero and verify the dual result;
5. turn on both fluids and verify that `W_g alpha + W_f alpha_f` remains zero numerically;
6. monitor zeros/sign changes of `W_g` and `W_f` during wall evolution;
7. reject any trajectory that requires an uncontrolled lapse divergence or crosses a forbidden square-root branch.

The wall's potentially most informative failure mode is now explicit:

`LAPSE_RATIO_SINGULARITY = W_f -> 0 while W_g != 0` (or the dual depending on gauge choice).

This is a physical/constraint-branch diagnostic, not merely a numerical nuisance.

## 7. Current conclusion

`NUMERICAL_RELATIVITY_ARCHITECTURE = PASS_IN_PRINCIPLE`

`TWIN_FLUID_SOURCE_PATCH = SPECIFIED` (see `V2_TWIN_FLUID_PATCH_SPEC.md`)

`GENERAL_TWIN_LAPSE = NOT YET IMPLEMENTED`

`FULL_DYNAMIC_WALL = NOT YET RUN`

No result in the current literature search removes the need for the planned dynamic experiment, and no general theorem found here rules it out before execution.
