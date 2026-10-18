# JANUS-R / Gate 2B — Step 30: exactly compensated native f metric and dust

**Date:** 2026-10-18. **Branch:** `research/gate2b-nonhomothetic-transfer`.

**Strict verdict:** `EXACT_COORDINATE_COMPENSATION_GREEN_AS_BASELINE`; `SCALE_ONLY_NATIVE_COMPENSATION_FAILS_AT_FINITE_R`; **`GENUINE_NONHOMOTHETIC_ONSHELL_BACKGROUND_OPEN`; `GATE_2B=OPEN`**. This is an explicit covariance/field-transport benchmark, **NOT** a new physical Janus solution, independent massive scalar mode, stability proof, or passage of the relative-μ fold.

## Continuity from Steps 28 and 29

- Step 28 derived the genuine on-shell *homogeneous*, radiation-free Candidate-C **two-dust** Routhian and both lapse, scale, and dust equations.
- Step 29 showed that simply replacing the f spatial chart by `R_f=λ r`, while holding the homogeneous *native* f scale unchanged, breaks the necessary g lapse equation: at `a=.4`, `λ=.78`, the lapse residual jumps from approximately zero to `+0.160780603695`.
- Step 29 also observed that `b_native=b_hom/λ` repairs the **central** source but not the general finite-r tilted source. The present calculation determines **all missing compensating f-native geometric and matter components exactly** for a *pure coordinate relabelling* of the homogeneous on-shell solution. The result identifies a calibration baseline against which a genuinely nonhomothetic *physical* deformation can be measured.

## Mathematical construction and coordinate transformation

Work in g common cosmic coordinates `x=(t,r)` with exactly homogeneous physical

```
ds_g²=-N_g(t)²dt²+a(t)²(dr²+r²dΩ²),
ds_f²=-N_f(t)²dt²+b(t)²(dr²+r²dΩ²),
θ_f=θ_f(t),   θdot_f=N_f,   ρ_f=C_f/b³,
ρ_g=C_g/a³,   N_g=1,
```

where `a(t)`, `b(t)=a(t)y(a)`, `N_f=y+y_N` solve the Step28 Candidate-C **radiation-free** homogeneous branch; `y_N` is implicitly differentiated from the exact quartic. Here `C_g=.9` and `C_f=3×.23958426762×y0³`, with `y0=.5568825591873054`. The two-sided real cosmic-time IVP is `a_dot=aH(a)`, `θdot_f=N_f(a)`, integrated by SciPy `solve_ivp` with dense interpolation.

Take an orientation-preserving, explicitly tilted time-dependent f-native chart:

```
T=t+σ(t)r²/2,       R=λ(t)r,
σ(t)=0.08+0.025t,    λ(t)=0.78+0.04t,
J=d(T,R)/d(t,r)=[[T_t,T_r],[R_t,R_r]]
  =[[1+σdot r²/2,σr],[λdot r,λ]],
D=det J>0.
```

At fixed f-native `(T,R)`, solve the inverse map by a safeguarded Newton iteration on `t`, with `r=R/λ(t)` and `dT/dt|R = D/λ`.

The **unique f-native tensor representing exactly the same physical f metric** is not generally native FLRW:

```
f_native = J^{-T} diag(-N_f(t)²,b(t)²) J^{-1},
f_ΩΩ,native = b(t)² r²,

f_TT=(-N_f² λ²+b² λdot² r²)/D²,
f_TR=( N_f² λ σr - b² λdot r T_t)/D²,
f_RR=(-N_f² σ²r² +b² T_t²)/D².
```

This native f metric generally has **a radial shift, non-FLRW radial/angular metric coefficients and native radial dependence**, even though its pulled-back common representation is exactly homogeneous. In particular, holding native `f_TR=0` and `f_RR=(b/λ)²` while still inclining the chart is an inconsistent *restricted metric ansatz*, not a coordinate transformation of the same physical geometry.

The f dust must be compensated simultaneously:

```
θ_native(T,R)=θ_f(t(T,R)),
(θ_T,θ_R)=N_f(t) (t_T,t_R),
ρ_native(T,R)=C_f / b(t(T,R))³.
```

Thus a tilted native chart produces a **nonzero radial phase gradient** `θ_R`, despite the physical dust remaining exactly comoving in common coordinates. Its proper-time constraint is `f_native^{AB}θ_A θ_B=-1`.

The native conserved dust current *density* is computed independently by using the native metric inverse:

```
J_dust^A = sqrt(-det f_native,2D) f_ΩΩ ρ(-f_native^{AB}θ_B)
         = C_f r² [T_t,R_t]^A / D    (per sinθ).
```

The two-dimensional native continuity equation `∂_T J_dust^T + ∂_R J_dust^R=0` was checked by centered finite differences. It is an exact Piola/continuity transformation of the homogeneous conserved `C_f`. For a nonzero *off-shell* native phase perturbation and density perturbation, the complete covariant dust Lagrangian separately obeys `D L_native = L_common` to roundoff: this test is deliberately **nonzero**, rather than a trivial zero-on-dust-clock equality.

## Interaction and partial action-level regressions

The independently coded exact spherical `2×2` principal-square-root Hassan–Rosen density uses both pulled-back metrics and all `β0..β4`. Under the exact compensation, it agrees with the homogeneous expression with square-root eigenvalues `(N_f/N_g, y,y,y)` across multiple times and radii. The angular radii are transported exactly; there is no extra angular `4π` factor inside the local density.

The *necessary g lapse Euler equation* was recomputed by actually finite-differencing one compact time-and-radial action containing:

1. `g` positive Einstein–Hilbert ADM+GHY flat-background lapse density `-3 a a_dot²/N_g`;
2. the canonically reduced `g` dust contribution `-N_g C_g` (not zeroed prematurely on the covariant dust clock);
3. the **fully nonlinear** spherical all-beta HR potential with compensated or scale-only f metric.

The independent `f` EH and `f` dust contributions have zero direct **partial** derivative with respect to the g lapse at fixed f fields/chart. This is only ONE of the eventual full coupled Euler equations, not all five-sector tadpoles. The compact g lapse perturbation uses `F(t,r)=[1-(t/Tmax)²]^4[1-(r/Rmax)²]^4` and both radial and temporal quadratures, with a finite-difference step. The expected on-shell compensation cancellation occurs. For the scale-only restriction a nonzero finite-radius residual survives.

### Numerical witness

At `a=.4`, common `t=0`, `r=.2`, `λ=.78`, `σ=.08`, `λdot=.04`, `σdot=.025`, on the independently integrated Candidate-C dust-only trajectory:

| Control | Value |
|---|---:|
| `y=b/a` | `0.5787707228025044` |
| `N_f` | `0.5185264338279018` |
| `T` | `0.0016` |
| `R` | `0.156` |
| `D=det J` | `0.780262` |
| Correct native f offdiagonal `f_TR` | `+0.00480694489921799` |
| Native f dust `θ_R` | `-0.01063287` |
| Native dust current divergence | about `+5.4e-12` |
| `g` lapse Euler residual, fully compensated | `+2.66e-10` |
| `g` lapse Euler residual, *only* f scale compensated | `+3.11645509e-4` |
| Compact spacetime integrated g lapse first variation, fully compensated | `+1.30104e-13` |
| Same integrated variation, scale-only | `+3.50278834e-8` |

The `g` lapse residual in the fully compensated case is finite-difference cancellation (the on-shell g Friedmann equation is independently solved). The scale-only residual grows approximately like `r²` at sufficiently small radii, as demonstrated by tests: `r=.1` gives `+7.79093e-5`, `r=.2` gives `+3.11646e-4`. The nonzero off-shell covariant f dust action density at the same point is approximately `+7.40597e-6` **in both** common and correctly Jacobian-weighted native charts. Without the `D` measure it differs.

**The exact compensated configuration is a diffeomorphic relabelling of the original homogeneous solution.** As a result, `λ` and `σ` in this construction are chart labels, not an independently dynamical `μ` physical helicity-0 mode and not a Candidate-C nonlinear screened branch. This baseline does not bridge the relative Stückelberg folds at `a≈.0301646/.0491246`, nor does it establish that a new native-FLRW nonhomothetic field ansatz can be on shell.

## Test evidence, negative gates and provenance

New files:

- `numerics/hr_compensated_native_chart.py` — exact chart and inverse; on-shell homogeneous two-dust branch time IVP; explicit native f tensor, transformed phase, mass-current; nonlinear HR density; necessary g lapse temporal/radial partial action variation.
- `tests/test_hr_compensated_native_chart.py` — **18 actual pytest tests**: quartic/IVP, Jacobian/orientation/inverse, exact f tensor recovery, native radial shift, dust norm and current/continuity, nonzero off-shell matter scalar-density Jacobian, nonlinear HR eigenvalue potential, on-shell g lapse at four points and integrated in time/radius, negative naive/no-shift ansatz, and domain guards.
- `scripts/verify_gate2b_step30.py` — focused pytest runner and SHA-256 manifests, reconstructable diagnostic witness, truthful checkout/oracle flags.

Run:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_compensated_native_chart.py
# 18 passed
OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step30.py gate2b-step30-report.json
# 18 passed; workspace_origin=standalone_focused_workspace;
# full_repository_regression=false; previous_step29_tests_rerun=false;
# DeFelice/Aoki NOT_RUN; Gate2B=OPEN
```

A first new radius-scaling test incorrectly required the source ratio between radii `.1` and `.2` to exceed `20`; the source actually exhibits the expected **factor near four**, because the leading residual is `O(r²)`. The test assertion was corrected to `3.6<ratio<4.4` **without altering any physics equation**. Similarly, an initially chosen `1e-7` threshold for the compact integrated negative control exceeded the real computed `3.50e-8`, so it was corrected to a discriminating `1e-8`. A new manifest runner needed to add its workspace to `sys.path` for the diagnostic import; that installation-independent path handling is now fixed.

**The previous 21 Step29, 17 Step28, and 75 Step27 tests were executed in DIFFERENT prior environments, NOT rerun in this Step30 workspace. Never add them and claim a single cumulative passing suite.** A full byte-exact clean Git clone is still DNS-blocked in this runtime; GitHub Actions are disabled; independent reproduction remains outstanding. Record exact SHA hashes on publishing and verify via GitHub connector before marking this checkpoint green.

## NEXT HARD RED — physical research program

1. The baseline gauge-diffeomorphic f-native fields are now explicit. Build **genuinely independent native f metric deformations** (not related to the homogeneous physical f metric by an inverse coordinate pullback), including radial shift and non-FLRW spatial geometry, with the two dust phases/densities varied as actual field variables. Keep the exact-compensation baseline as an always-green zero-tadpole/Noether reference and report every introduced physical perturbation source.
2. Evaluate **all** g and f Einstein equations, HR relative-coordinate/Stückelberg Euler equations, and both canonical dust constraints on a common compact time/radial domain. Find a truly on-shell nonhomothetic Candidate-C background or give a concrete negative gate for a specified ansatz, not a chart-coordinate claim.
3. Only for such an on-shell background, derive a single full time-dependent EH+HR+two dust quadratic physical scalar action; eliminate metric auxiliaries and time-dependent BD-null canonical direction retaining both dust phase pairs.
4. Reproduce BOTH physical independent limits from the SAME reduced action: finite-H `μ→0` De Felice and nonlinear homothetic Aoki `K_S,c_S²` (stable and unstable benchmarks). Only after both pass, examine the first relative `μ` fold near `a≈0.0301646` and decide whether a regular canonical dynamical crossing exists.

**Bottom line:** `COMPENSATED_PURE_CHART_BASELINE=GREEN`; `NATIVE_FLRW_SCALE_ONLY_INSERTION=FAIL_AT_FINITE_RADIUS`; `ON_SHELL_NONHOMOTHETIC_RELATIVE_MODE=NOT_DERIVED`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`.
