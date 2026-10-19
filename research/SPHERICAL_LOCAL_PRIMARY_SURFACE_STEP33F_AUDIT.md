# JANUS Gate 2B — Step 33f: local radial mixed bracket on an explicit primary-constraint surface

**Date:** 2026-10-19. **Branch:** `research/gate2b-nonhomothetic-transfer`. **Status:** `LOCAL_RADIAL_MIXED_KERNEL_GREEN`, `EXPLICIT_RESTRICTED_RADIAL_PRIMARY_SURFACE_GREEN`, **`GENERAL_LOCAL_HR_BD_SECONDARY_OPEN`, `GATE_2B=OPEN`**.

## Question and result

Step 33e evaluated the *fully radially smeared* mixed canonical functional bracket `{H_g[N],H_f[M]}` of positive Einstein–Hilbert g/f + five-beta Hassan–Rosen + TWO irrotational canonical dust pairs on an arbitrary radially varying, **off-shell** test family. Its nonzero result did not, by itself, demonstrate a secondary constraint.

Step 33f addresses two concrete gaps **without claiming general BD closure**:

1. Extract a **pointwise differential bilinear kernel** for the arbitrary lapse smearings `N(r),M(r)`, retaining every radial gradient, instead of only one number for one pair of smearings.
2. Construct a **genuinely radially varying canonical phase-space family satisfying both lapse primaries and the diagonal momentum primary pointwise**, with two independently positive dust momenta. Evaluate the mixed kernel there, not only on off-shell polynomials. The family is deliberately restricted to flat spatial slices (a useful necessary witness, not a generic nonhomothetic solution).

In the first task the local kernel reconstructs the independently computed integrated Step33e bracket. In the second, all local primary residuals are near numerical zero and the kernel reduces on the chosen restricted family to `N M` times an additional condition involving **radial derivatives of gravitational momentum**. Its spatially constant limit reproduces Step33b's homogeneous secondary bracket **exactly**. It is **NOT** a universal derivation of the local Hassan–Rosen BD secondary, its secondary time preservation or lapse fixing.

## Full off-shell local smearing differential operator

Let the exact original radially smeared Hamiltonian coefficients be those in `numerics/hr_spherical_mixed_hamiltonian_bracket.py`, where the regular relative shift `z_*(r)` has been eliminated only on its nondegenerate `K(r)≠0` branch and both complete dust canonical phase/momentum pairs are retained. Exact spatial-curvature and `p_L'` terms were already integrated by parts before functional differentiation.

For arbitrary smooth, independently varied canonical radial data, the **integrand** of the mixed functional bracket is bilinear in jets of the two smearings through order two:

```
{H_g[N],H_f[M]} = integral dr sum_{i,j=0}^2 K_ij(r) N^(i)(r) M^(j)(r).
```

`numerics/hr_spherical_local_mixed_kernel.py` constructs all nine `K_ij` without a huge symbolic expansion: at each fixed radius `r0` evaluate the **functional Euler derivatives** of each primary separately using the three centered smearing polynomials `1`, `(r-r0)` and `(r-r0)^2/2`. These probe the unit zeroth/first/second smearing jets. Contract the **six complete canonical pairs** with the exact Poisson symplectic signs. Thus the 3×3 matrix represents the differential smearing dependence; no assumption that `N=M` or `N'=M'=0` enters.

On the original off-shell Step33e radial data at `r=0.43` with beta `(0.2,1.3,-0.35,0.4,-0.17)`, `m²=.91`, `Mg²=1.7`, `Mf²=.63`, the explicit kernel is

```
K = [[ +0.7567188355958618, -0.0286924000547916, 0.0],
     [ -0.2146033230521444, +0.2648947092957616, 0.0],
     [ +0.2648947092957616,  0.0,                0.0]].
```

Across multiple radii and both eliminated-`z` and externally fixed-`z` controls, `K_02=K_12=K_22=K_21=0` and `K_20=K_11` to numerical roundoff. **Do not drop the nonzero N′, M′ or N″ terms before radial IBP.** In fact these derivative terms individually contribute far more than the final residual and cancel substantially. Integrating this local kernel against the ORIGINAL compact arbitrary smearings at 40-point quadrature gives `+1.2437914369613253e-6`, versus the original independent Step33e full bracket `~+1.2437914369615e-6`. Exchanging the two lapse smearings is independently tested and does not give the same number.

The equality `K_20=K_11` eliminates the `N M″` term after *two* integrations by parts moving all derivatives from `N`. That does **not** imply that all derivative-of-smearing pieces vanish off shell; their actual reduced coefficients also involve radial derivatives of `K_ij`.

## Exactly satisfying the radial primary surface on a restricted family

Start from the **radiation-free**, on-shell **homogeneous** Candidate-C dust-only branch of Step33b, with positive `a`, `b=a y(a)`, positive native Planck mass squares, five fixed HR betas and TWO positive dust charge constants. Recompute `y(a)` *independently* by the positive quartic continuation at each `a`.

Choose exactly flat radial three-metrics but freely varying canonical gravitational momenta:

```
L_g=a,       S_g=a r,
L_f=b,       S_f=b r,
p_{L,g}=r² P_g(r),   p_{S,g}=d[p_{L,g}]/dr,
p_{L,f}=r² P_f(r),   p_{S,f}=d[p_{L,f}]/dr,
theta_g'=theta_f'=0.
```

Both sector momentum densities therefore vanish **identically**, not merely after integration:

```
D_g=p_{S,g} S_g' - L_g p_{L,g}'=0,
D_f=p_{S,f} S_f' - L_f p_{L,f}'=0,
D_diag=0,
```

so the regular shift equation gives `z_*=0`. Since the spatial intrinsic curvatures vanish, the full positive-EH gravitational constraints can be evaluated directly from **their original unintegrated spherical ADM form**. Solve the TWO lapse primaries individually for TWO positive, different dust momentum densities:

```
p_g(r) = r² [ (3 P_g²/4 + r P_g P_g'/2)/(Mg² a)
             -m² Mg² a³ V_g(y)],
p_f(r) = r² [ (3 P_f²/4 + r P_f P_f'/2)/(Mf² b)
             -m² Mg² a³ V_f(y)],

V_g=β0+3β1 y+3β2 y²+β3 y³,
V_f=β1+3β2 y+3β3 y²+β4 y³.
```

This ensures **`H_g(r)=H_f(r)=D_g(r)=D_f(r)=0` pointwise** in the tested radial interval for *arbitrary small smooth polynomial variations of `P_g` and `P_f`*, provided both separately reconstructed dust momenta remain positive. These are radially nonconstant momenta/densities even though the spatial 3-geometries are flat. **No full Einstein evolution equations, dust continuity in time, or time-lapse fixing are imposed.** The data are a **canonical primary-constraint surface**, not a nonlinear nonhomothetic on-shell solution.

For this precisely defined family, the newly computed 3×3 mixed-bracket kernel has all entries numerically zero except `K_00`, which matches the compact closed form

```
K_00(r) = [m² Mg² a² J(y)/2] r² [3 X(r)+r X'(r)],
X(r) = P_g(r)/(Mg² a)-P_f(r)/(Mf² b),
J(y) = β1+2β2 y+β3 y².
```

This formula is corroborated by the **independent full Step33e canonical Euler-gradient bracket**, not merely by reconstructing `K_00` from the same formula. It was checked at `a=1,.4,.2,.05,.03`, three radial points each, multiple independent polynomial momentum perturbations, and with different positive g/f matter source profiles.

At `a=.4`, `r=.43`, `y≈.5787707228025044`, the *radially varying* primary-satisfying witness yields

```
Hg = +2.0816681711721685e-17,
Hf = -3.469446951953614e-18,
Ddiag = Dg = Df = 0,
p_g = +0.18951503337809916,
p_f = +0.022872502691009985,
K_00 = -0.11307718948650103,
closed-form formula = -0.11307718948650095,
K_ij other than (0,0) = 0.
```

For the original compact smearings, `∫ K_00 N M dr = -7.916775842392439e-7`; the independently evaluated full Step33e functional bracket gives `-7.916775842392432e-7`. **This nonzero bracket appears despite all THREE primary constraints being exactly satisfied.** It is a *restricted-primary-surface necessary secondary condition*, not a conclusion about arbitrary canonical inhomogeneities.

**Discriminating negative control:** replacing `3 X+r X'` by the naively extrapolated homogeneous `3 X` is WRONG: at `r=.43` the correct value is `-0.11307718949`, the incorrect value `-0.08394271077`, a difference of `-0.02913448`. The real radial derivative cannot be omitted. If, instead, `P_f=(Mf² b/(Mg² a)) P_g` identically, then `X=0`, the restricted secondary condition vanishes and both dust densities can remain positive and independent. This is a *test of the condition*, not a proof that the full Dirac algorithm closes.

In the homogeneous limit `P_g=p_a/3`, `P_f=p_b/3`, `X=chi/3`, giving exactly

```
K_00/r² = (m² Mg² a²/2) J(y) chi,
chi=p_a/(Mg² a)-p_b/(Mf² b),
```

which is Step33b's already validated homogeneous Poisson secondary relation. For the unperturbed Candidate-C background, the bracket vanishes over the controlled epochs because `chi=0`, not because the HR interaction was deleted.

## Tests, exact-source provenance and real bug fixes

New files:

- `numerics/hr_spherical_local_mixed_kernel.py` — 3×3 full local mixed differential kernel and global quadrature reconstruction.
- `numerics/hr_spherical_radial_primary_surface.py` — separate polynomial radial positive-two-dust primary-surface construction, direct original EH/HR primary residuals, restricted secondary formula.
- `tests/test_hr_spherical_local_primary_kernel.py` — 21 additional pytest parametrized controls (including tests across multiple radii/epochs), two formerly published Step33e files unchanged.
- `scripts/verify_gate2b_step33f.py` — test runner, SHA-256/Git blob provenance and independent numerical witness, flags for all unresolved physics gates.

**Executed together in the SAME `/mnt/data/janus33e` focused workspace:**

```
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests
# 52 passed in ~17 s (31 original Step33e + 21 NEW Step33f)

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33f.py gate2b-step33f-report.json
# exit 0, 52 passed in ~20 s; report carries all source digests
```

The runner refuses to execute if either original Step33e source/test Git blob differs from the verified live GitHub record. Newly committed Step33f files must be SHA-verified against the **executed** local bytes. There is **no complete git checkout, no GitHub Actions/CI execution and no independent external reproduction**. The preceding Step33d 95-test focused suite and Step32e 93-test focused suite were **not rerun here**; do not add their counts.

An actual initial Python syntax mistake while constructing the positive-momentum guard (`min` around a generator with the wrong parentheses) was caught by the FIRST execution and corrected before the tests passed. No physical equation was modified to force test success. Earlier Step33e's independent canonical-variable unpacking bug remains protected by its complete 31-test regression.

## Next RED — do NOT close Gate 2B prematurely

1. **Extend the primary-surface calculation beyond flat 3-geometries, comoving dust, and separately vanishing radial momenta.** Determine the general local mixed bracket after eliminating `z`, including gradient-dependent pieces and diagonal momentum-constraint contributions. Impose `H_g=H_f=D_diag=0` genuinely on nonhomothetic spatial geometry, not just on this exact solvable subclass. A numerical extension must solve the constraints accurately and track functional derivatives of the unsimplified action; avoid assuming this subclass formula generally.
2. Run the actual **Dirac preservation algorithm**, including both primary lapse constraints, diagonal diffeomorphism constraints, any secondary, the rank of its Poisson brackets, and **lapse fixing**, retaining BOTH canonical dust pairs. Evaluate degenerate `J(y)=0` and `K(r)=0` branches separately. These operations could reject the model or demonstrate the expected BD elimination.
3. On the same physically reduced action recover both De Felice finite-H `mu→0` and nonlinear homothetic Aoki `K_S,c_S²` stable/unstable scalar oracles. Independently find a genuinely **nonhomothetic on-shell** two-dust Einstein–Hassan–Rosen background beyond Step30 passive chart compensation. Only then test the first relative `mu` fold near `a≈0.0301646`.

**Scientific disposition:** a radially varying primary-surface witness and its derivative-dependent necessary bracket condition are verified; neither general spherical BD secondary nor four-dimensional JANUS-R cosmological viability is established. **`GATE_2B=OPEN`.**
