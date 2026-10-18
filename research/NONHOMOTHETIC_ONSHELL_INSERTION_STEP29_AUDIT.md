# JANUS-R / Gate 2B — Step 29: explicit obstruction to **naively inserting** the on-shell homogeneous Candidate-C solution in the finite-μ chart

**Date:** 2026-10-18. **Branch:** `research/gate2b-nonhomothetic-transfer`.

**Precise scientific status:** `NAIVE_ONSHELL_HOMOGENEOUS_TO_NONHOMOTHETIC_INSERTION=FAIL`; `LOCAL_VISIBLE_LAPSE_EULER_OBSTRUCTION=VERIFIED`; **`FULL_NONHOMOTHETIC_ONSHELL_BACKGROUND=OPEN`**, **`GATE_2B=OPEN`**. This is a definite, falsifiable **negative result for a particular naive substitution**, NOT a general theorem against JANUS-R or against nonhomothetic metric solutions.

## Why this gate was necessary

- **Step 27** established a coherent five-sector nonlinear spacetime *off-shell* trial action: positive g/f Einstein–Hilbert + complete Hassan–Rosen potential + two covariant irrotational dust sources. Its polynomial native g/f scale and lapse backgrounds do **not** solve the coupled field equations.
- **Step 28** independently derived and verified a *homogeneous* on-shell two-dust FRW Routhian for radiation-free Candidate-C. Its lapse/scale first variations vanish. Yet the nonhomothetic relative-coordinate transformation of Step 27 is **not** an arbitrary common gauge transformation of both metrics; treating a nonzero relative radial distortion as a mere coordinate relabelling while leaving native f scale and dust charges fixed changes the relative geometry and HR interaction.
- The first prerequisite for promoting Step 28 into Step 27 is therefore an explicit **local field-equation check**, not diagonalization of an off-shell Hessian or an assertion that the homogeneous branch remains on shell.

## Analytic result at the regular spherical origin

Work at an arbitrary time in common g cosmic coordinates with homogeneous spatially flat metrics before relative displacement:

```
ds_g²=-N_g² dt²+a²(dr²+r²dΩ²),

ds_f,native²=-N_f(T)² dT²+b(T)²(dR²+R²dΩ²),
T=t+σ(t)r²/2,     R=λ(t)r,     λ=1+μ>0.
```

At the regular center `r→0`, the radial relative transformation has the **three equal physical f spatial ratios**

```
y_original=b/a,     y_effective=λ b/a=λ y,
```

while the native f time eigenvalue remains `N_f/N_g` there. Thus the principal square root of `g^{-1}f` has eigenvalues `(N_f/N_g, λy, λy, λy)` at the center. Using the *actual all-beta Hassan–Rosen interaction* gives the g lapse potential

```
V_g(y)=β0+3β1 y+3β2 y²+β3 y³,
J_g(y)=β1+2β2 y+β3 y²,
V'_g(y)=3J_g(y).
```

The g lapse Euler equation per comoving spatial volume, after **proper two-dust canonical Routh reduction** (not premature on-shell covariant dust Lagrangian substitution), is

```
R_g(λ)=3 M_g² a a_dot²/N_g² - C_g - m² M_g² a³ V_g(λ y).
```

On the previously verified Step 28 homogeneous Candidate-C dust-only branch, `R_g(1)=0`. Consequently, if the native f scale `b(T)` and g data are simply inserted without readjustment into a relative radial map `R=λr`,

```
R_g(λ)-R_g(1) = -m² M_g² a³ [V_g(λy)-V_g(y)],
(dR_g/dλ)|λ=1 = -3m² M_g² a³ y J_g(y).
```

This is an **exact center field-equation obstruction** for the specified ansatz; it does not depend on assumed weak scalar potentials, missing perturbation initial data, or the f Planck mass. The `β4` term is correctly absent from the g lapse variation because it represents the f-only volume contribution. A pure `m²=0` model has no such relative HR obstruction.

### Important limitation and counterexample to overclaiming

If `λ` is constant and the native f spatial scale is **consistently redefined** as `b_native=b_physical/λ`, then `λ b_native/a=y`; the *central g lapse obstruction disappears*. The f lapse/scale evolution, f dust charge transformation and complete spatial/timing equations still need to be satisfied. For `σ≠0` and/or `λ_dot≠0` the exact pulled-back f geometry also acquires `r`-dependent radial/time cross terms and native-time sampling. A genuine nonhomothetic solution must solve the **full set of equations** with appropriate field backreaction. This result must **never** be reported as "nonhomothetic JANUS is impossible." It establishes that *copying the on-shell homogeneous solution without changing its native f geometry* is not sufficient.

## Independent computation from the exact nonlinear HR square root

New source `numerics/hr_nonhomothetic_center_obstruction.py` computes the above analytic center formula and **independently** forms the *exact* pulled-back spherical f radial/time `2×2` metric at finite radius:

```
f_tt = -n(T)² T_t² + b(T)² R_t²,
f_tr = -n(T)² T_t T_r + b(T)² R_t R_r,
f_rr = -n(T)² T_r² + b(T)² R_r²,
f_ΩΩ = b(T)² R².
```

Using `s=sqrt(det f_2 / det g_2)`, `τ=sqrt(tr(g_2^{-1} f_2)+2s)`, and `ℓ=sqrt(f_ΩΩ/g_ΩΩ)`, it recomputes `e0..e4` and the full HR density with no reference to the analytic central `V_g` function. A centered **partial g lapse derivative** of this exact interaction density is normalized by `r²` and compared with the independent center formula as `r→0`. This avoids just testing an algebraic function against a rearrangement of itself.

The same source numerically varies a **compactly supported g lapse** in a radial action containing the g Einstein–Hilbert homogeneous lapse term, the correct canonical g dust charge `-N_g C_g`, and the **nonlinear HR potential**. The f Einstein–Hilbert and f dust actions have zero *direct* partial derivative with respect to `N_g` when the f metric and its chart are held fixed, so they cannot cancel a nonzero g-lapse Euler residual. The normalized radial bump is independently known exactly:

```
F(r)=(1-r²/Rmax²)^4,
4π∫_0^Rmax dr r² F(r)=2π Rmax³ B(3/2,5).
```

This tests an **actual first action variation** of a necessary equation at the instant, but it is **not** yet the full five-sector time-integrated nonhomothetic Euler system or a demonstration of the f constraints.

## Measured reproducible values: radiation-free Candidate C

Use `β=(0, 1, -4.2383993109, 13.6801214252, -38.5117901844)`, `m²=23.3348939346`, `M_g²=1`, `C_g=0.9`; homogeneous `y(a)` and `N_f(a)` from the Step28 **dust-only** variant, with original homogeneous `g` lapse `N_g=1`. The inputs were independently revalidated in the new tests against the original dust branch quartic and its implicit derivative (`N_f=y+y_N`). All numbers are dimensionless code diagnostics, not direct observations.

| `a` | original `y=b/a` | radial relative `λ=1+μ` | original `R_g(1)` | **naively mapped** `R_g(λ)` |
|---:|---:|---:|---:|---:|
| 1.0 | 0.556882559187 | 0.78 | ≈0 | **+1.51155110041** |
| 0.4 | 0.578770722803 | 0.78 | ≈0 | **+0.160780603696** |
| 0.05 | 1.360739478178 | 0.78 | ≈0 | **+0.028554624135** |
| 0.03 | 1.979545244855 | 0.231117 | ≈0 | **+0.03919434056** |

At `a=0.4`, `λ=0.78`, the **independent nonlinear square-root partial g lapse difference** at `r=10^-4` returns the same `+0.1607806037` within finite-difference precision. The exact derivative at `λ=1` is `-1.7539067836`, reproduced by centered finite differences of the mapped residual.

For the compact radial profile of radius `0.035`, the directly differentiated integrated lapse action yields `+3.20003248×10^-6`, in agreement with the analytic center residual times the exact radial bump norm. For `λ=1` and no tilt, the same compact variation is numerically zero. With nonzero `σ, σ_dot` and `λ_dot`, even a chart with `λ=1` can produce a nonzero finite-`r` g lapse source (for the chosen independently Taylor-sampled native f lapse/scale), despite the center being unchanged. Such finite-radius values diagnose inhomogeneous **off-shell** terms, not an unavoidable physical obstruction.

A stronger **finite-radius negative control after center compensation** uses `b_native=b_hom/0.78`, `σ=0.08`, `λ_dot=0.04`, and native Taylor samples of `b(T)` and `n(T)`. The center g-lapse equation now vanishes, but at `r=0.2` the independently differentiated HR/g-EH/dust local lapse residual is approximately `-0.0017545` (dimensionless); with `σ=0` and the same radial-rate settings its magnitude is below `5×10^-6`. On common-time slices, the exact f spatial component difference obeys

```
f_rr - f_theta_theta/r² = -n(T)² σ² r².
```

This is a **slicing-dependent metric component identity**, not a spacetime curvature invariant and not evidence for physical anisotropic stress. It proves that fixing the center ratio alone does not algebraically restore the homogeneous *common-slice metric components*. The full f/g Euler equations and native shift backreaction remain to be determined.

The fifth coefficient `β4` can be altered arbitrarily without changing the g lapse variation; zeroing `m²` removes the relative-source difference. A constant radial dilation compensated by the correct native f scale restores the *central* g lapse equation, proving the test is not a universal no-go claim.

## Falsification and quality controls

New targeted test source `tests/test_hr_nonhomothetic_center_obstruction.py`:

- 21 actually executed pytest tests, including five separate real Candidate-C epochs/chart values for the independent exact HR square-root derivative;
- independent reproduction of the old dust-only quartic `y(a)` and f lapse `N_f=y+y_N` for four recorded epochs;
- center limit as `r→0`, direct finite-radius tilted relative map, proper orientation/metric-domain guards;
- independently integrated compact g lapse action variation and analytic radial bump norm, quadrature and finite-difference refinement;
- linearized `J_g` obstruction slope, `β4`-independence, `m²=0` decoupling;
- explicit **coordinate-compensated native f scale counterexample** to an overbroad exclusion, and a new finite-radius negative control demonstrating that an inclined native f time slicing remains nonhomogeneous even after central scale compensation;
- off-shell invalid-chart negative controls.

Actual standalone focused local run:

```
cd /mnt/data/janus29
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_nonhomothetic_center_obstruction.py
# 21 passed
python scripts/verify_gate2b_step29.py /mnt/data/janus29/gate2b-step29-report.json
# 21 passed; gate2b OPEN; standalone_focused_workspace
```

The full Step27 75-test collection and Step28 17-test collection were **not** rerun together in this session; never say "111 tests passed". GitHub CI has remained disabled and direct git clone fails DNS. The two new source/test modules are self-contained and deliberately use independently recomputed Step28 data rather than a clean-checkout import; their provenance should be checked by exact file hashes after publication. Reproducing these local tests on an actual complete Git worktree remains a separate acceptance criterion.

## NEXT PRECISE RED / restart contract

1. Introduce this on-shell homogeneous Candidate-C branch into the full native g/f action **with an explicit choice of compensated f native scale/chart**; correctly transform **both dust charges and native phase variables**, and enforce orientation-positive Jacobians. Do NOT claim it is on shell merely because the center g lapse obstruction can be repaired.
2. Derive and evaluate **all** radial and time-dependent g/f Einstein equations, their dust clock equations, and the HR/Stückelberg relative-coordinate variation; impose their constraints across the radial support and demonstrate full tadpole cancellation on a single common time/radius action. If impossible, log the actual residuals and a negative result for the specified ansatz.
3. Only after those first variations vanish, construct the common finite-time quadratic scalar action and eliminate four metric auxiliaries and time-dependent BD-null constraint while preserving both independent dust canonical phase pairs.
4. From **that same reduced action** reproduce De Felice finite-H `μ→0` and Aoki nonlinear homothetic `K_S,c_S²` (stable and unstable roots), then test regular physical crossing of the Candidate-C local relative-μ fold near `a≈0.0301646`. Ghost/gradient/fold or observational viability is NOT established by Step29.

**Disposition:** The naive Step28→Step27 on-shell insertion is **falsified** by a nonzero necessary field equation. The route to a corrected nonhomothetic on-shell background remains open, as does Gate 2B. This is appropriate for a scientifically honest audit and subsequent peer reproduction.
