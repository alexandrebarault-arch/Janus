# V2 Twin-Matter Lapse Block from Exact Sector Duality

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `F_MATTER_LAPSE_BLOCK_DERIVED__CXX_RUNTIME_VALIDATION_PENDING`

## Purpose

Remove the last unnecessary symbolic obstacle in the twin-fluid lapse implementation without hand-transcribing the full Appendix D of Kocic–Lundkvist–Torsello.

The public one-fluid `bim-solver` already contains the complete geometry and g-matter lapse coefficients. Its explicit matter dependence is localized in the runtime `eq_gW_2` / `eq_fW_2` pair. The published theory has an exact sector duality.

Therefore derive only the **missing f-matter additive blocks** from the existing g-matter blocks.

Pinned upstream:

`nubirel/bim-solver@8852e8e9921edeeedf1a447d3bf27b82ec24433c`

Source:

`include/eom-std/eomLapseRatios.h`.

## 1. Upstream definitions

Use

`R = B_f/B_g`,

`lambda = sqrt(1+p^2)`.

Define the beta polynomials

`P  = beta1 + 2 beta2 R + beta3 R^2`,

`Qg = beta2 + beta3 R`,

`Qf = beta1 + beta2 R`,

`C  = beta1 - beta3 R^2`.

For each Valencia dust sector define

`E_g = D_g - S_g v_g + tau_g`,

`H_g = D_g + S_g v_g + tau_g`,

and the analogous `E_f,H_f`.

## 2. g-matter blocks isolated from upstream

Subtracting the same generated expressions with `D_g=S_g=tau_g=0` gives the exact g-matter contributions to the runtime `W2` coefficients:

`Delta Wg2[g] =`

`- (kappa_g A_g^2 A_f^2 (1+p^2) R^2 P / 2)`

`  * [ -lambda C E_g + 2 A_f Qg (S_g v_g + p^2 H_g) ]`.

And

`Delta Wf2[g] =`

`+ kappa_g A_g^2 A_f^2 (1+p^2) R^2 P Qg (D_g + tau_g)`.

These expressions are not a new ansatz; they are a compact factorization of the explicit terms already present in the pinned C++ source.

## 3. Correct way to apply the duality

The published duality is simultaneous:

`g <-> f`,

`kappa_g <-> kappa_f`,

`beta1 <-> beta3`, `beta2 -> beta2`,

`p -> -p`,

`W_g <-> -W_f`.

The dangerous part is `R=B_f/B_g -> 1/R`.

To avoid a power-of-R mistake, the derivation was performed as follows:

1. replace `R` by the independent ratio `B_f/B_g`;
2. swap `A_g<->A_f`, `B_g<->B_f`, couplings, beta indices and matter states;
3. apply the required overall sign from `W_g<->-W_f`;
4. only then re-eliminate `B_f = R B_g`.

`lambda=sqrt(1+p^2)` is invariant under `p->-p`.

## 4. Missing f-matter additions

The result is

### f matter contribution to `gW_2`

`Delta Wg2[f] =`

`- kappa_f A_g^2 A_f^2 (1+p^2) P Qf (D_f + tau_f) / R^5`.

### f matter contribution to `fW_2`

`Delta Wf2[f] =`

`+ kappa_f A_g^2 A_f^2 (1+p^2) P /(2 R^6)`

`  * [ lambda C E_f`

`      + 2 A_g R Qf (S_f v_f + p^2 H_f) ]`.

These are the only missing dust-matter pieces if the existing one-fluid geometry/g-matter generated coefficients are retained unchanged.

## 5. Why this is enough for the dust extension

The general published lapse relation is linear in the stress-energy contributions from the two separately coupled sectors. The pinned upstream implementation already contains

- all geometry/bimetric terms;
- all g-dust contributions.

The new independent f dust therefore enters additively through the dual matter block above. No new radial derivatives of f matter are introduced into `W0/W1`; the explicit upstream matter dependence is localized in `W2`.

This statement is specific to the same pressureless Valencia matter model used by the pinned solver. A pressureful or anisotropic f fluid would require the corresponding general stress projections, not these dust formulas.

## 6. Verification

A local TDD cycle was run independently of GitHub Actions.

### RED

Tests were written before the module existed:

`ModuleNotFoundError: No module named 'lapse_matter_duality'`.

### GREEN

After implementing the compact blocks:

`3 passed in 0.03s`.

The tests verify:

1. all f-matter additions vanish exactly when the f state is zero;
2. exchanging sectors maps the g-matter contribution into minus the corresponding dual f-matter contribution, as required by `W_g<->-W_f`;
3. time-symmetric rest-dust (`p=S_g=S_f=0`) values remain finite.

An independent SymPy derivation compared the compact formulas to the expressions obtained by the full simultaneous substitution and simplification; all four differences simplified exactly to zero.

Repository files:

- `numerics/lapse_matter_duality.py`
- `tests/test_lapse_matter_duality.py`.

## 7. Implementation consequence

The previous statement

`GENERAL_TWIN_LAPSE = BLOCKED ON FULL AUTHOR SYMBOLIC SOURCE`

is now too pessimistic.

Revised state:

`GENERAL_TWIN_LAPSE_MATTER_EXTENSION = DERIVED`

`GENERAL_TWIN_LAPSE_CXX_REGRESSION = NOT RUN`

`FULL AUTHOR SYMBOLIC SOURCE = DESIRABLE CROSS-CHECK, NOT STRICTLY REQUIRED FOR DUST PATCH`

In a compilable GPL fork, the minimal implementation is now:

1. keep upstream `Wg0,Wg1,Wg2,Wf0,Wf1,Wf2`;
2. add `Delta Wg2[f]` to `Wg2`;
3. add `Delta Wf2[f]` to `Wf2`;
4. run `f-matter=0` exact upstream regression;
5. run sector-duality randomized tests;
6. monitor `W=-W_f/W_g>0` during evolution.

## 8. Remaining caution

The derivation is algebraically strong but has **not** yet been compiled inside `bim-solver` in this environment.

Therefore it removes an analytic implementation ambiguity, not the need for executable regression.

The next hard blocker is now practical rather than theoretical:

> materialize and compile a GPL-compatible upstream fork, then run the one-fluid and duality regression matrix before interpreting any wall evolution.
