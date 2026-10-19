# JANUS / Gate 2B — Step 31: one spherical EH + HR + two-dust action, 12 homogeneous-on-shell scalar tadpoles

**Checkpoint:** 2026-10-19. **Branch:** `research/gate2b-nonhomothetic-transfer`.

**Verdict:** `HOMOGENEOUS_COMMON_CHART_12_FIELD_TADPOLES=GREEN`; `INDEPENDENT_RELATIVE_F_METRIC_RESPONSE=NONZERO`; `GENUINELY_NONHOMOTHETIC_ONSHELL_BACKGROUND=NOT_FOUND`; `BD_REDUCTION=NOT_PERFORMED`; **`GATE_2B=OPEN`**.

## Actual advance and distinction from step 30

Step 30 constructed the *exact inverse coordinate pullback* of a dust-only homogeneous on-shell Candidate-C f metric, dust phase and current into a tilted (T,R) native f chart. Its verified g-lapse variation was **one** necessary first-order Euler direction, and the compensated solution was *the same homogeneous geometry*, not a physical nonhomothetic branch.

Step 31 builds and differentiates an independent **single, exact nonlinear, spherically symmetric, common-coordinate action** containing both positive-Einstein–Hilbert ADM+GHY sectors, all five Hassan–Rosen betas, and both original off-shell irrotational-pressureless dust Lagrange-multiplier actions. All five sectors use **the same actual g and f metric perturbations**, not separately tuned Hessian bases. It checks the on-shell homogeneous Candidate-C baseline in **12 distinct compact field directions**. The f perturbations are independent physical *trial field variations* beyond the inverse-chart compensation; their quadratic responses are nonzero. This is a step toward extracting a dynamical perturbation action, **not** the discovery of a new on-shell physical finite-μ background or of reduced scalar eigenmodes.

### Exact fields and ADM density

On a common `(t,r)` chart with spherical line element

```
  ds_i² = -n_i(t)²(1+2Φ_i)dt² + 2 n_i(t)a_i(t)U_i dt dr
          +a_i(t)²Q_ri dr² +a_i(t)² Q_ti r²dΩ²,
  Q_ri=1+2ψ_i-2k²E_i/3, Q_ti=1+2ψ_i+k²E_i/3,
  N_ADM,i = n_i sqrt(1+2Φ_i+U_i²/Q_ri),
  (N^r)_i = n_i U_i/(a_i Q_ri),
  L_i=a_i sqrt(Q_ri), S_i=a_i r sqrt(Q_ti).
```

Define `W_i=S_{i,r}/L_i`. Then **for each sector**, with `K^r_r=(Ldot/L-(N^r)_r-N^r L_r/L)/N_ADM`, `K^θ_θ=(Sdot/S-N^r S_r/S)/N_ADM`,

```
  (3)R_i = (2/S_i²)[1-W_i²-2(S_i/L_i) W_i,r],
  L_EH,i=(M_i²/2) N_ADM,i L_i S_i²
           [(3)R_i-4 K^r_r K^θ_θ-2 (K^θ_θ)²].
```

This is the ADM+spatial/time-boundary representative, not the unreduced 4D scalar-curvature density at a fixed finite-boundary prescription. Compact trial variations vanish with sufficient derivatives at time/radial boundaries. The real square-root HR potential is independently computed from the two temporal/radial 2×2 blocks plus angular eigenvalue `ell=sqrt(f_ang/g_ang)`, with all `β0...β4` coefficients and strictly positive g/f Einstein–Hilbert signs.

Before varying, retain **both** covariant dust actions:

```
  L_dust,i = (ρ_i/2) N_i L_i S_i²
     { [ (θdot_i-N_i^r θ'_i)/N_i ]²
        -(θ'_i/L_i)²-1 }.
```

Background dust densities `ρ_g=Cg/a³` and `ρ_f=Cf/b³`, and background clocks `θdot_g=1`, `θdot_f=N_f`, with **independent** phase and multiplier variation. At the background both dust Lagrangian **values** vanish, but their partial g/f-lapse variations are nonzero; substituting the normalization before variation would invalidate the result. A separate two-sector local Legendre transform is checked in tests, but a global common-time canonical/BD reduction is **not** yet done.

### Radial and temporal compact independent fields

For each metric separately, six amplitude directions:

```
   (Φ, U, ψ, E, δθ, δρ),
   Φ = p B(t)F(r),
   U = u B(t) r F(r),
   ψ = s B(t)F(r),
   E = e B(t)r²F(r),
   θdot = n(t)+δθ Bdot(t)F(r), θr=δθ B(t)Fr(r),
   ρ = ρ0(t)[1+δρ B(t)F(r)],
   B(t)=[1-(t/T)²]^4,
   F(r)=[1-(r/R)²]^4.
```

The complete native/common scalar field derivative transport `ψ_t, ψ_r, ψ_rr, E_t,E_r,E_rr,U_r` is **explicitly** included in curvature and ADM extrinsic terms. Scalar trace/shear radial regularity at the center holds (`U=O(r)`, `E=O(r²)`). Each single amplitude has an independent finite first variation **before** applying equations. The total action is integrated with `4π dt dr` and one radial `r²` volume factor inside each sector; no angular double counting.

The dynamical-branch on-shell homogeneous background is the same independently established **radiation-free** Candidate-C version as Step 28/30:

```
 β=(0, 1, -4.2383993109, 13.6801214252, -38.5117901844),
 m²=23.3348939346, M_g²=1, M_f²=(0.10879548725)²,
 C_g=0.9, C_f=3*(0.23958426762)*y0³,
 y0=0.5568825591873054;
 a(t=0)=0.4, b(t)=a(t)y(a(t)),
 N_g=1, N_f=y+dy/dln a;
 adot=aH_g(a), bdot=N_f adot.
```

The dust-only homogeneous background is integrated by SciPy `solve_ivp` in both time directions. Its positive `y(a)` is determined from the exact quartic and its derivative via polynomial differentiation. This is NOT a radiation-era observational fit, nor an on-shell *physically* nonhomothetic Stückelberg branch.

## Quantitative witness and actual cancellations

At compact half-time `T=0.027`, radial support `R=0.32`, Gauss–Legendre order 24 per variable, centered amplitude step `2e-5`, the five component action values (arbitrary normalization) are

```
  (EH_g, EH_f, HR, dust_g, dust_f) =
   (-0.00810475501, -0.0000287904612, -0.000985841997,
     0, 0),
  S_total = -0.009119387466617324.
```

The **12 first variations** are ordered `(Φ_g,U_g,ψ_g,E_g,θ_g,ρ_g,Φ_f,U_f,ψ_f,E_f,θ_f,ρ_f)`. The largest actual absolute first variation is **`1.4051260155412136e-11`** (`ψ_g`), with all others smaller. The result is tested for quadrature orders 18/24/26/28/34, changed spacetime supports and finite-difference step refinement; the leading central-difference error scales as `h²`.

More discriminating: the sources cancel **between the action components** rather than being zero individually. Example (approximate derivative per amplitude):

```
  Φ_g:  EH_g +3.64871135e-4,
        HR   -6.44695537e-5,
        dust_g -3.00401582e-4,
        sum ≈ +1.1e-13.

  Φ_f:  EH_f +1.29610824e-6,
        HR   +2.01858490e-5,
        dust_f -2.14819573e-5,
        sum ≈ -3.5e-14.

  ψ_g:  EH_g +1.32476647e-4; HR -1.32476643e-4.
  ψ_f:  EH_f +3.74470798e-7; HR -3.74470756e-7.
```

The matter phase perturbations have vanishing on-shell linear integral by separate clock-current conservation; the multipliers have vanishing linear integral because the clock norm is -1. The **independent local Legendre pairs** are checked in both sectors before constraint elimination.

### Tests proving the new perturbations are not only passive-chart compensation

- Add **only** an `f` spatial trace perturbation: its common-slice intrinsic spatial curvature changes (`(3)R_f≈-1.2485` at a diagnostic point for amplitude .003), while `g` remains unperturbed and its intrinsic spatial curvature remains zero. The angular relative eigenvalue changes from homogeneous `y` to `~0.57907577`. This is a real trial-field deformation of the common metric pair, NOT the Step 30 *exactly compensated* f-native diffeomorphic baseline. **A slicing-dependent 3-curvature by itself is not a gauge-invariant physical particle diagnosis.**
- The exact action has a nonzero quadratic response in f lapse, shift, trace, shear and phase directions, despite zero linear variation. **These are raw off-shell/before-constraint quadratic entries, NOT ghost or sound-speed measurements.**
- The **mixed** Hessian `∂²S/(∂Φ_g ∂ψ_f)` is about `-1.84236013e-4`; when the HR mass is set to zero, that cross-metric block vanishes to numerical accuracy. This is an independent physically relative-interaction regression and checks the bimetric coupling is not inadvertently lost.
- Removing HR **without adjusting the homogeneous background** produces g/f lapse tadpoles `+6.447e-5` and `-2.019e-5`; the falsely "still on shell" model is rejected.
- A pure β4 interaction is strictly independent of the g lapse, as expected from the f-only volume identity.
- Exactly transformed tilted f-native tensors are recovered under `Jᵀ f_native J` even **after** an independent f perturbation; the perturbed native tensor acquires the required shift. Only this tensor-level covariance is tested: a new native time-dependent on-shell nonlinear branch has not been solved.

## Reproducibility and the precise limitation

New files:

- `numerics/hr_full_onshell_tadpole.py`
- `tests/test_hr_full_onshell_tadpole.py`
- `scripts/verify_gate2b_step31.py`

Actually run in a NEW standalone focused workspace `/mnt/data/janus31`:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_full_onshell_tadpole.py
# 29 passed
OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step31.py gate2b-step31-report.json
# 29 passed, tests_exit_code=0, max_abs_tadpole=1.40512601554e-11
```

Source files have been directly executed locally. On publishing, verify their exact git blob SHA against GitHub; the command runner writes SHA-256 of program, tests and its own source, and explicitly records `workspace_origin=standalone_focused_workspace`, `full_repo_test_suite=false`, `historical_test_suites_rerun=false`, `DeFelice/Aoki=NOT_RUN`, `bd_constraint_reduced=NO`, `GATE_2B_OPEN`. **Do not claim any of the earlier 18/21/17/75 test suites were rerun** and do not silently add those historical counts. No full fresh exact-source GitHub clone or CI is available in this environment.

**Core scientific limitation:** the metric background is still homogeneous physical Candidate-C, expressed directly in a *common* chart. The exact inverse-native chart from step 30 is a passive relabelling only. The 12 independent field variations now pass their first-variation controls, but they do **NOT** supply a new on-shell, genuinely nonhomothetic background. No metric auxiliary/BD-null canonical reduction has been executed on the same full scalar action, and no De Felice finite-H μ→0 or Aoki homothetic nonlinear physical scalar limit has been passed. Gauge elimination, constraints, principal characteristics, first μ-fold and any cosmological likelihood are still **RED/OPEN**.

## Next precise RED gate

1. Use this one common spherical action as the **single field space** for a time-dependent quadratic Hessian retaining both dust phases and multipliers, with explicit first spatial/time jets, compact boundary bookkeeping and no early density elimination.
2. Independently decompose the quadratic operator into diagonal gauge/null components, true lapse/shift constraints and relative bimetric sector **on an on-shell background**, testing the exact covariant Noether/Bianchi identities. Reduce both dust phase/momentum pairs canonically; identify the BD-null direction only after full constraints.
3. Derive or falsify a *genuinely* nonhomothetic on-shell finite-μ background via time/radial field equations, not by inverse-chart compensation or forcing f-native FLRW after a tilt; only then can the Candidate-C relative μ-fold question be decided.
4. From the **same** constrained physical action, reproduce both required independent physical controls (De Felice finite-H μ→0 and Aoki nonlinear homothetic K_S,c_S², stable/unstable), or report an explicit negative gate with the failed equation. **GATE_2B stays OPEN** until all these succeed.
