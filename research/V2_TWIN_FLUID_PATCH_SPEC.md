# V2 Twin-Fluid Standard-3+1 Patch Specification

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `SOURCE_MAP_COMPLETE__LAPSE_SYMBOLIC_BLOCK_EXTERNAL`

## Purpose

This document is the exact source-level patch specification for extending the pinned public `nubirel/bim-solver` standard-3+1 formulation from one Valencia dust fluid coupled to `g` to two independent dust fluids, one minimally coupled to each metric.

Pinned upstream tree/commit:

`8852e8e9921edeeedf1a447d3bf27b82ec24433c`

This repository does **not** vendor or modify the GPLv3 upstream source. The actual implementation belongs in a separate GPL-compatible fork once the solver can be materialized and compiled.

The source audit below is based on the pinned upstream files, not on guessed pseudocode.

---

## 1. New f-fluid state

Keep the existing g-fluid names unchanged for one-fluid regression:

- `pfD`, `pfS`, `pftau`, `pfv`.

Add a genuinely independent f-fluid state, for example:

- `pfFD`, `pfFS`, `pfFtau`, `pfFv`;
- RHS: `pfFD_t`, `pfFS_t`, `pfFtau_t`;
- radial derivatives: `pfFD_r`, `pfFS_r`, `pfFtau_r`, `pfFv_r`.

The exact spelling is implementation-local; the requirement is that no storage is shared between sectors.

### `src/bim-solver-std.cpp` registration points

Add the new state consistently to:

1. `enum bimIndex` state variables;
2. RHS variables;
3. cached radial derivative variables;
4. `bimInput`;
5. `bimEvolvedGF`;
6. `bimOutput`;
7. optional derivative diagnostics;
8. `emitField(...)` declarations;
9. `emitDerivative_r(...)` declarations;
10. `calculateDerivedVariables()`;
11. left-boundary parity;
12. right-boundary extrapolation.

### Spherical parity

Exactly mirror the existing g dust parity:

- `D_f`: even;
- `S_f`: odd;
- `tau_f`: even;
- `v_f`: odd.

No new physical assumption is involved here; this is ordinary regular spherical hydrodynamics.

---

## 2. f-sector Valencia equations

Source reference: pinned `include/eom-std/eomMatter.h`.

The f fluid must be the exact sector-covariant analogue of the existing g fluid. Replace every g geometric quantity by the corresponding f quantity; do **not** use g lapse/metric/shift in the f hydrodynamics.

Using compact names `Df,Sf,tauf,vf`, the required equations are:

```text
Df_t = fBet_r Df + fBet Df_r
     + fAlp [ -fDAlp Df vf - Df_r vf - Df vf_r ]
     + [2 fBet Df - 2 fAlp Df vf]/r
```

```text
Sf_t = 2 fBet_r Sf + fBet Sf_r
     + fAlp [ fDA Sf vf - Sf_r vf - Sf vf_r
              - fDAlp (Df + Sf vf + tauf) ]
     + [2 fBet Sf - 2 fAlp Sf vf]/r
```

```text
tauf_t = fBet_r tauf + fBet tauf_r
       + fAlp [ fK1 Sf vf - fDAlp vf tauf - vf_r tauf
                - vf tauf_r - fDAlp Sf/fA^2 ]
       + [2 fBet tauf - 2 fAlp vf tauf]/r
```

Primitive velocity:

```text
vf = Sf / [ (Df + tauf) fA^2 ]
```

Radial derivative:

```text
vf_r = [ -2 fDA Sf (Df+tauf)
         + Sf_r (Df+tauf)
         - Sf (Df_r+tauf_r) ]
       / [ fA^2 (Df+tauf)^2 ]
```

Dust stress-energy projections:

```text
rho_f^m = (Df + tauf)/(fA fB^2)
j_f^m   = Sf/(fA fB^2)
J1_f^m  = Sf vf/(fA fB^2)
J2_f^m  = 0
```

### Mandatory symmetry test

On a fixed state with

```text
g geometry == f geometry,
Dg == Df,
Sg == Sf,
taug == tauf,
```

the g and f primitive variables and Valencia RHS must agree to machine precision.

This test must be RED before the f equations are added and GREEN afterwards.

---

## 3. Gravitational source functions

Source reference: pinned `include/eom-std/eomSources.h`.

The upstream f-sector source functions contain only bimetric interaction pieces. Add the f matter terms exactly once.

### Hamiltonian and momentum projections

```text
eq_f_rho += (Df + tauf)/(fA fB^2)
eq_f_j   += Sf/(fA fB^2)
```

Because `C_2` already uses `f_rho`, no separate f-density term is added directly to `C_2`.

### Trace source used by fK evolution

The exact sector dual of the existing g matter term in `eq_g_JK` is

```text
eq_f_JK += fAlp * (3 Df - Sf vf + 3 tauf)/(2 fA fB^2)
```

### Anisotropic source used by fKD evolution

The exact sector dual of the existing g matter term in `eq_g_JKD` is

```text
eq_f_JKD += fAlp * Sf vf/(fA fB^2)
```

### `JK1/JK2`

Do **not** modify `eq_f_JK1/eq_f_JK2` in the first patch.

Repository search at the pinned revision finds these auxiliary functions only at their definitions; the standard evolution uses `JK` and `JKD` directly. Altering unused generated auxiliaries in the first patch creates unnecessary risk of inconsistent or double-counted matter terms.

If a later formulation begins to consume `JK1/JK2`, regenerate them from the general stress-energy expressions rather than hand-patching them.

---

## 4. Separation variable from both momentum constraints

Source reference: pinned `include/eom-std/eomMiscEquations.h`.

The existing `eq_base_p_g` already contains the g-fluid momentum source and remains the g constraint solution.

The existing `eq_base_p_f` was generated under `S_f=0`. With an independent f momentum density, add

```text
eq_base_p_f += - Sf/(fA * gA * gB^2 * P_2_1(R))
```

in the upstream conventions.

Equivalently, the correction recorded in the runbook is

```text
base_p_f -> base_p_f
            - S_f/(A_f_metric A_g_metric B_g^2 P_2_1(R)).
```

This term follows by solving the f momentum constraint for the separation variable; it is not a phenomenological patch.

### Regression

When `Sf=0`, `p_f` must be bitwise/algebraically identical to the upstream expression.

---

## 5. Mixed momentum constraint `C_3`

Source reference: pinned `include/eom-std/eomConstraints.h`.

The upstream matter contribution is

```text
- k_g k_f Sg/(2 Bg^2)
```

because the solver assumes `S_f=0`.

After eliminating the separation variable between the two momentum constraints with both fluids retained, the matter contribution becomes

```text
- k_g k_f (Sg + Sf)/(2 Bg^2)
```

in the current solver conventions (`R=Bf/Bg`).

Therefore the only matter change in `eq_C_3` is the addition of the `Sf` term; all geometric terms remain unchanged.

### Required tests

1. `Sf=0` -> exact upstream result.
2. `Sg=0`, `Sf != 0` -> `C_3` changes with the predicted sign.
3. matched opposite momenta `Sf=-Sg` -> explicit matter piece cancels, while geometric/interaction pieces remain.

---

## 6. Direct matter term in `fSig_t`

Source reference: pinned `include/eom-std/eomEvolution.h`.

The existing g equation contains

```text
- k_g gAlp Sg/(2 gB^3).
```

Under the exact sector duality

```text
g <-> f,
p -> -p,
k_g <-> k_f,
S_g <-> S_f,
```

the direct matter term is independent of `p`, hence its sign does not flip.

Add to `eq_fSig_t`:

```text
- k_f fAlp Sf/(2 fB^3)
```

The existing bimetric p-dependent interaction term remains unchanged.

### Symmetry test

For equal geometries, equal lapses/couplings and identical fluid states, with the interaction sector simultaneously dualized, the direct g/f matter contributions to `Sig_t` must match.

---

## 7. General lapse ratio — the only intentionally untranscribed block

Source: Kocic, Lundkvist & Torsello, *On the ratio of lapses in bimetric relativity*, arXiv:1903.09646.

For both matter sectors the secondary-constraint preservation law has the spherical form

```text
0 = W_g alpha + W_f alpha_f
```

(up to the common normalization used by the authors), therefore

```text
alpha_f/alpha = - W_g/W_f
```

or equivalently according to which lapse is chosen as gauge.

`W_g` and `W_f` depend on **both** matter stress-energy tensors as well as the metric/extrinsic-curvature variables and their radial derivatives.

### Do not hand-transcribe Appendix D

The authors publish symbolic ancillary sources including:

- `src/02-lapse-ratio.nb`;
- `src/bimetric-lapses-nr.m`;
- `src/bimetric-ss-nr.m`.

Those files are not materializable in the current execution environment. The full Appendix-D expression is deliberately **not** copied manually here because a single sign/factor error would contaminate every subsequent dynamical conclusion.

### Mandatory future implementation gate

When a compilable external fork is available:

1. obtain the authors' machine-readable expression;
2. translate it into the standard solver variables;
3. verify the published duality
   `g<->f`, `beta_(4-n)<->beta_n`, `p<->-p`, `W_g<->-W_f`;
4. set all f-fluid variables to zero;
5. compare the new `W_g,W_f` and lapse ratio against the pinned upstream one-fluid `eomLapseRatios.h` on randomized regular states;
6. require numerical agreement to floating-point tolerance before any twin-fluid evolution.

No wall evolution is scientifically interpretable before this gate passes.

---

## 8. State-machine changes in `bim-solver-std.cpp`

The pinned source explicitly shows all integration hooks. The new f state must appear in every corresponding location.

### Enum / storage

Add:

```text
pfFD, pfFS, pfFtau,
pfFv,
pfFD_t, pfFS_t, pfFtau_t,
pfFD_r, pfFS_r, pfFtau_r, pfFv_r.
```

### Input

Append `pfFD,pfFS,pfFtau` to `bimInput`.

### Evolution

Append

```text
{pfFD,pfFD_t}, {pfFS,pfFS_t}, {pfFtau,pfFtau_t}
```

to `bimEvolvedGF`.

### Derived variables

`calculateDerivedVariables()` must independently compute

```text
pfv  = eq_pf_v(...g...)
pfFv = eq_pf_Fv(...f...)
```

with the same zero-momentum guard used upstream.

### Derivatives

Register radial derivatives for all new conserved variables and `pfFv`.

### Left boundary parity

```text
pfFD   even
pfFS   odd
pfFtau even
pfFv   odd
```

### Right boundary

Extrapolate all three f conserved variables consistently with the g ones; calculate/extrapolate the f primitive velocity exactly as upstream does for `pfv`.

### Output

Expose at minimum

```text
Df,Sf,tauf,vf,
Df_t,Sf_t,tauf_t,
```

so rest-mass conservation and fluid velocity can be monitored independently.

---

## 9. Required one-fluid regression matrix

Before running a Janus-like wall, test four source states on identical geometry:

| g fluid | f fluid | required behavior |
|---|---|---|
| zero | zero | vacuum baseline |
| nonzero | zero | reproduce pinned upstream one-fluid solver |
| zero | nonzero | exact sector-dual response |
| nonzero | nonzero | both source sets active exactly once |

For the critical `f=0` regression require:

- same g/f geometric RHS as upstream to numerical tolerance;
- same `p_g,p_f,C_1..C_4`;
- same lapse ratio;
- same g-fluid RHS;
- no nonzero f-fluid RHS generated from zero f matter except numerical roundoff.

---

## 10. Scientific stop gate

Do not proceed to interpreting a dynamic wall if any of these fail:

1. sector-symmetry hydrodynamic tests;
2. `f=0` upstream regression;
3. mixed momentum-constraint regression;
4. published `W_g,W_f` duality;
5. upstream one-fluid lapse regression;
6. independent g/f rest-mass conservation in controls;
7. resolution-convergent bimetric constraints.

A failure here is a code/derivation problem, not evidence for or against JANUS-R.

Only after these pass does a regular or failing wall evolution become scientific evidence.

## Current decision

`TWIN_FLUID_PATCH_ARCHITECTURE = SPECIFIED`

`GENERAL_LAPSE_IMPLEMENTATION = BLOCKED_ON_AUTHOR_SYMBOLIC_SOURCE / COMPILABLE_FORK`

`DYNAMIC_WALL = NOT_RUN`
