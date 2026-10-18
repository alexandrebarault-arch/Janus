# JANUS-R / Gate 2B — Step 28: two-dust homogeneous on-shell Routhian and compact temporal tadpole gate

**Date:** 2026-10-18. **Research branch:** `research/gate2b-nonhomothetic-transfer`.

**Verdict:** `CANDIDATE_C_DUST_ONLY_MINISUPERSPACE_BACKGROUND=GREEN`, `FOUR_COMPACT_TEMPORAL_TADPOLES=GREEN` **in the strict homogeneous submodel**; `FULL_NONHOMOTHETIC_FIVE_SECTOR_ACTION_ON_SHELL=RED`, `GATE_2B=OPEN`, `JANUS_R_NOT_VALIDATED`.

## Context / why this is the next real gate

Step 27 already integrated five off-shell, covariant action densities (positive Einstein–Hilbert g and f, all-five-beta Hassan–Rosen, two irrotational pressureless dusts) on the same spherical native metrics and compact spacetime domain, but it used **unrelated polynomial time backgrounds** in the two metrics. Consequently that unified action was NOT an on-shell Candidate-C solution and its trial-field Hessians could not be interpreted physically.

Step 28 independently derives the EXACT homogeneous/flat-FLRW positive-EH two-metric **minisuperspace Routhian** with two separately conserved **canonical dust charges**. It tests the radiation-free Candidate-C dust variant across the homogeneous evolution down to and through the *location* of the previous algebraic relative-Stückelberg folds. The prior full nonlinear off-shell Step27 spacetime action HAS NOT been rewritten on this background in Step28: the two constructions are still different stages, and a background minisuperspace check is not the full common scalar perturbation action.

## One single homogeneous five-sector action

Set g cosmic common time `t`, homogeneous scales `a(t),b(t)`, lapses `N_g,N_f`, `y=b/a`, positive masses `M_g²,M_f²`, positive/zero `m²`, and all five interaction coefficients `β_0...β_4`. The FRW interaction square-root eigenvalues are `(N_f/N_g,y,y,y)` and the unique minisuperspace potential is

```
V(y) = β0 + 3β1 y + 3β2 y² + β3 y³
W(y) = β1 + 3β2 y + 3β3 y² + β4 y³

L = -3 M_g² a a_dot²/N_g -3 M_f² b b_dot²/N_f
    -m² M_g² a³ [N_g V(y)+N_f W(y)]
    -N_g C_g-N_f C_f.
```

**Both dust constants** `C_g,C_f` are the two *separate comoving canonical phase momenta*, not densities held fixed independently of the scale factor. Their homogeneous densities are `ρ_g=C_g/a³`, `ρ_f=C_f/b³`.

### Essential RED guard: never impose the dust constraint before varying

For one irrotational homogeneous dust phase `θ`, multiplier density `ρ`, lapse `N` and scale factor `a`:

```
L_dust,cov = (a³ρ/2) [θ_dot²/N - N],
p_θ = a³ρ θ_dot/N.
```

On the proper dust clock `θ_dot=N`, the covariant dust Lagrangian **evaluates to zero**. However its true **partial** derivative `∂L/∂N` at *fixed θ_dot and ρ* equals `-a³ρ=-C`, NOT zero. Canonical Legendre/Routh reduction with fixed conserved `p_θ=C` gives `L_Routh,dust=-N C` and preserves this lapse source. Substituting `θ_dot=N` into the covariant Lagrangian **before** varying would erase the dust energy incorrectly, and could falsely seem to cancel background tadpoles. The new test enforces the correct order for BOTH sectors.

## Exact background equations, directly from the action

Define `A(y)=β0+2β1 y+β2 y²`, `J(y)=β1+2β2 y+β3 y²`, `K(y)=β2+2β3 y+β4 y²`.

The two **lapse constraints** `∂L/∂N_g=0` and `∂L/∂N_f=0` are:

```
R_Ng = 3 M_g² a a_dot²/N_g² - m² M_g² a³ V - C_g = 0,
R_Nf = 3 M_f² b b_dot²/N_f² - m² M_g² a³ W - C_f = 0.
```

The two independent **scale Euler residuals**, `d/dt(∂L/∂a_dot)-∂L/∂a=0` and similarly for b, are

```
R_a = -3 M_g² [ (a_dot²+2a a_ddot)/N_g
                 -2a a_dot N_gdot/N_g² ]
      +3m² M_g² a² (N_g A+N_f J) = 0,

R_b = -3 M_f² [ (b_dot²+2b b_ddot)/N_f
                 -2b b_dot N_fdot/N_f² ]
      +3m² M_g² a² (N_g J+N_f K) = 0.
```

On the dynamical branch with `J≠0`, the Bianchi lapse relation is `a_dot/N_g=b_dot/N_f`. In g cosmic time (`N_g=1`), `a_dot=a E`, `b=a y`, and it becomes

```
N_f = y + d y / d ln(a).
```

All four Euler constraints and Bianchi are checked **independently against finite differences of L**, rather than only being substituted back into an algebraic Friedmann function.

## Precise Candidate-C variant and independent quartic

Inputs reproduce `numerics/flrw_two_matter.py:candidate_c()` with `Ω_g,r0=0` **removed intentionally**, exactly as in the existing `numerics/candidate_c_dust_background.py`. This is not the full radiation-era Candidate-C model:

```
β=(0,1,-4.2383993109,13.6801214252,-38.5117901844)
M_g²=1, M_f²=(0.10879548725)², m²/H0²=23.3348939346
C_g=3*(0.30), C_f=3*(0.23958426762)*y0³
resolved dust-only y0=0.5568825591873054
```

The present y0 is resolved self-consistently under both lapse constraints after removing the radiation term, not silently replaced with the earlier radiation-inclusive y0. Here `E(1)=0.9999551638376833`; it is **not 1** because the removed radiation density had `Ω_g,r0=9e-5`.

The branch equation obtained by equating the two Friedmann equations is the same quartic as the existing `flrw_two_matter.polynomial_coefficients`, with `C_f` interpreted as the fixed f dust comoving charge. Derivatives `y_N,y_NN` come from **implicit differentiation of that polynomial**, not from noisy finite differences. Then `E_N`, both scale accelerations and the f lapse rate are constructed consistently; no independently tuned acceleration is inserted.

| a | y=b/a | E=H_g/H0 | N_f (N_g=1) | max absolute 4 EL+lapse+Bianchi residual |
|---:|---:|---:|---:|---:|
| 1.0 | 0.556882559187 | 0.999955163838 | 0.551545778648 | 5.4e-13 |
| 0.4 | 0.578770722803 | 2.385971903909 | 0.518526433828 | 1.2e-13 |
| 0.09 | 0.939977525126 | 20.843350164129 | 0.416922093339 | 1.5e-14 |
| 0.05 | 1.360739478178 | 50.166972485846 | 0.417132659305 | 4.1e-14 |
| 0.03 | 1.979545244855 | 107.680806181894 | 0.461831564933 | 1.3e-13 |

All entries are dimensionless *homogeneous background consistency* controls. They are neither ghost eigenvalues nor observational estimates.

## Additional time-domain test: true compact tadpoles

This is stronger than evaluating a pointwise Friedmann constraint. Independently integrate the background ODE `a_dot=a E(a)` via SciPy `solve_ivp`, in both time directions around `a(t=0)=0.4`. The exact implicit quartic and logarithmic derivatives reconstruct `b(t), N_f(t), a_dot(t), b_dot(t)` at Gauss-Legendre nodes on the time domain. Apply independent compact variations to **each** of `a,b,N_g,N_f`, with `F(t)=(1-(t/T)²)^4`, and also perturb `a_dot,b_dot` by the actual derivative `F_dot(t)`.

Compute the **first derivative of the full integrated Routhian** with respect to each compact amplitude by independently evaluating the finite actions at `±epsilon`. By integration by parts, all four coefficients must vanish for an on-shell background.

At order 26, domain half-width 0.025, finite amplitude 1e-6, the actual computed coefficients for `(a,b,N_g,N_f)` are

```
(-1.80411e-10, +1.38778e-11, 0.0, -6.93889e-12)
```

Independent controls with quadrature order 18 / 32 and different compact widths and finite steps reproduce residuals smaller than `1e-9`. The previous first numerical comparator used an excessively large variation step (2e-5/1e-5) and produced an `O(epsilon²)` truncation residual around 1e-7/1e-8. Refining the step to 1e-6 resolved the discrepancy; it was a **finite-difference test defect**, not a change in background equations.

Deliberately increasing `N_f` by 2% while holding the other background data fixed yields a nonzero f lapse constraint `-0.00029076439058473014` at a=0.4, matching the independently predicted inverse-lapse-square scaling; the f Bianchi residual also becomes nonzero. Increasing conserved `C_f` by 1% changes the f lapse residual by exactly `-0.01 C_f`, leaving the g lapse source unchanged. This is a falsifiable negative control.

## Clarifying the former two folds

The localized folds at `a≈0.0301646` and `a≈0.0491246` in `research/NONHOMOTHETIC_FOLD_AUDIT.md` concern the **nonlinear local relative Stückelberg radial μ equation**. The present homogeneous quartic `y(a)` remains numerically smooth and has positive f lapse on both sides of these values. This is NOT evidence that an oscillating helicity-0 solution crosses either μ fold; the physical scalar action and initial matching data are still missing. Distinguish **background y** from **relative Stückelberg μ**.

## Verification, provenance and remaining RED

Files added:

- `numerics/hr_minisuperspace_onshell.py` — exact homogeneous Routhian, four algebraic/acceleration residuals, on-shell Candidate-C dust-only implicit branch, compact temporal action variations.
- `tests/test_hr_minisuperspace_onshell.py` — **17 executed tests**: both lapse variations, independent scale Euler finite differences, homogeneous Friedmann comparison, Bianchi, double dust continuity/Routh, off-shell negative perturbations, time-domain compact cancellation and finite-step convergence, fold-location differentiation, guards.
- `scripts/verify_gate2b_step28.py` — one-command reproducibility, exact SHA-256 source/test hashes and checkout provenance with explicit physics-gate warnings.

Actual local focused workspace `/mnt/data/janus28`, not a Git worktree:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_minisuperspace_onshell.py
# 17 passed
python scripts/verify_gate2b_step28.py gate2b-step28-report.json
# 17 passed; workspace_origin=standalone_focused_workspace; Gate2B=OPEN
```

The TWO source/test files were published on the active GitHub branch byte-for-byte from the actual executed local files, Git blob hashes:

```
numerics/hr_minisuperspace_onshell.py 6e456921cf094f4afb8f490d01b2d87f426f82b3
tests/test_hr_minisuperspace_onshell.py 40ba78c066c197d230915ba3179d78d76f16e545
```

**The 17 new focused tests are NOT to be added to the 75 historical Step27 tests and described as a single executed 92-test suite.** The original repository still cannot be cloned in the current networked workspace, and CI is disabled. Peer reproduction and full suite remain outstanding. No automatic claim of independent validation.

### Next exact RED — crucial for full JANUS physics

1. **Promote the actual nonlinear Step27 five-sector spacetime action to the derived on-shell, dust-only Candidate-C trajectory**, making all g/f native scale/lapse functions and derivatives consistent under the common/nonhomothetic chart rather than polynomial controls. Reevaluate all common compact lapse/scale/matter variations; reproduce the minisuperspace four equations without prematurely setting the covariant dust clock on shell.
2. Build the **single full time-dependent physical quadratic scalar action**, including the native f metric derivative transport, both dust canonical phase pairs, compact boundary terms, actual chart variations and homogeneous tadpoles. Do not mix scalar trial functions/modes with distinct normalizations.
3. Perform the full metric auxiliary constraints plus time-dependent Boulware–Deser null canonical reduction, retaining BOTH dust phase pairs.
4. Verify **both independent physical scalar** acceptance oracles on that SAME action: finite-H μ→0 De Felice and nonlinear homothetic Aoki `K_S,c_S²` (stable and unstable branches).
5. Only then test constrained kinetic/gradient regularity through the first relative μ fold near a≈0.0301646. A perfectly regular homogeneous background cannot establish a physical fold crossing. No observational/CMB claims.

**Conclusion:** the homogeneous background/on-shell tadpole sub-gate is GREEN, the previously combined full nonhomothetic perturbation and stability gate is STILL RED/OPEN. No validation of JANUS-R has been established.
