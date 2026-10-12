# V2 environmental screening and transition-wall stability gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `ENVIRONMENTAL_SELECTIVITY_PLAUSIBLE__TRANSITION_WALL_STABILITY_OPEN`

## Executive result

The surviving JANUS-R route is no longer a universal late-time linear modification of gravity. Current calculations point to a much narrower possibility:

> the common cosmological mode stays approximately GR-like, while a sufficiently strong **relative two-sector environment** can excite a different nonlinear branch locally, especially around a visible void paired with a twin-sector overdensity.

There is now quantitative evidence for environmental selectivity at the level of nonlinear branch topology and Vainshtein scaling. There is **not yet** a stability proof for the transition layer joining the local branch to the homogeneous exterior.

That transition layer is now the decisive theoretical gate.

---

## 1. Relative rather than total mass controls the scalar screening source

Aoki, Maeda & Namba (2015), Appendix A, obtain for a static twin-matter source approximately

`R_V^3 ~= 2 |G_g M_g - K^2 G_f M_f| / (3 m_eff^2 - 2 Lambda_g)`.

The important structure is the **difference** of weighted sector masses.

Consequences:

- matched/common `g` and `f` sources can partially cancel the massive/relative scalar source;
- a visible underdensity together with a twin overdensity adds in the relative source;
- screening is therefore environment-dependent in a way that is naturally aligned with Janus-like segregation.

For a top-hat relative matter perturbation with negligible `Lambda_g`, the static scaling becomes

`(R_V/R)^3 ~= Omega_m(z) H(z)^2 |delta_rel| / (3 m_eff^2)`.

Equivalently, the contrast needed for `R_V ~= R` is

`|delta_rel|_crit ~= 3 m_eff^2 / [Omega_m(z) H(z)^2]`.

Using matter conservation this can be written

`|delta_rel|_crit ~= 3 (m_eff/H0)^2 / [Omega_m0 (1+z)^3]`.

The implementation is in

`numerics/environmental_screening.py`

with tests in

`tests/test_environmental_screening.py`.

Local RED/GREEN verification for this new module:

- RED: `ModuleNotFoundError` before implementation;
- GREEN: `3 passed in 0.03s` after implementation.

---

## 2. Screening can be much stronger early than today

For `lambda_g = 100 Mpc`, `H0=70 km/s/Mpc`, `Omega_m0=0.30`:

`m_eff/H0 ~= 42.83`.

Today,

`|delta_rel|_crit ~= 1.83e4`.

Thus an order-unity relative contrast gives only

`R_V/R ~= 0.038`.

In this static scaling, an ordinary late-time void-sized relative perturbation is therefore largely **outside** its own Vainshtein radius.

At the matter-era low-energy Higuchi crossing, however,

`m_eff^2 ~= 2 H^2`

and `Omega_m ~= 1`, so

`|delta_rel|_crit ~= 6`.

Thus the same theory can be substantially more nonlinear/screened in the early transition era than at late times.

This provides a concrete version of the qualitative idea

`early GR-like nonlinear phase -> late release of the relative mode`.

It does not prove the release is stable.

---

## 3. Static positive-mass branch selection: a real environmental boundary

The Case-A Aoki-Maeda-Namba parameters are

`beta2=-3`, `beta3=3`, `m_g^2=m_f^2`.

The repository diagnostic

`numerics/static_branch_selection.py`

specializes the Appendix-A algebraic static equation to `K=1`, equal coupling normalization, and defines

`u=(R_V/R)^3`, `q=M_f/M_g`.

The branch topology changes sharply with the local twin/visible source ratio.

Representative results:

- `q=0.001`: the homothetic `mu~0` branch continues deep inside `R_V` and recovers the GR-like behavior;
- `q=10`: the homothetic branch fails before `R_V`, while the nonlinear/non-homothetic branch connected to `mu_infinity~=0.698872` remains real and regular in the algebraic diagnostic;
- in this particular normalization, the exchange occurs around `q ~= 1.325`.

The threshold remained close to this value when the inward continuation range was varied substantially.

### Important limitation

`q~=1.325` is **not a universal constant**. It is specific to the Case-A interaction parameters and the chosen `K=1`/equal-coupling static normalization.

The robust statement is only:

> nonlinear bimetric branch topology can depend qualitatively on the local ratio of the two matter sectors.

This is a real environmental-selection mechanism at the algebraic level.

---

## 4. A Janus-like void is a different sign problem

For an actual visible cosmic void, the perturbation mass relative to the background is negative:

`M_g < 0`,

while a twin overdensity has

`M_f > 0`.

Hence the relevant weighted ratio is anti-correlated (`q<0` in the static-void convention), not the positive-source `q>0` examples above.

The separate diagnostic

`numerics/static_void_transition.py`

therefore treats the correct perturbation signs.

For Case A, the asymptotically homothetic branch connected to `mu=0` reaches a double-root endpoint when moving inward. For equal weighted perturbation magnitudes, the algebraic endpoint occurs near

`R_critical ~= 2.70 R_V`.

Across a broad anti-correlation ratio scan the value stays close to `~2.7 R_V`.

This must **not** be interpreted as a physical singularity at exactly that radius. Aoki-Maeda-Namba explicitly warn that a divergent derivative of the algebraic root signals breakdown of the small-gradient/adiabatic approximation.

The correct statement is:

`ALGEBRAIC_SMOOTH_MATCHING_FAILS`

and

`GRADIENT_RESOLVED_TRANSITION_LAYER_REQUIRED`.

---

## 5. Serious caveat: static Ricci-flat Vainshtein solutions can be unstable

Aoki & Mizuno (2016), arXiv:1607.00173, study the stability of the Vainshtein solution using the `Lambda_2` nonlinear-sigma-model effective theory.

For scalar perturbations, their quadratic action is governed by a kinetic matrix `Z^{mu nu}` whose trace is proportional to Ricci curvature. On a Ricci-flat background the trace vanishes, so all kinetic eigenvalues cannot have the required sign simultaneously. They conclude that a Ricci-flat Vainshtein solution supported only by the nonlinear scalar necessarily has a ghost and/or gradient instability.

They then include linear vector-graviton perturbations around a specific static spherical bigravity background and still find a ghost and/or gradient instability for all theory parameters **for that background**.

This is a major warning against treating conventional isolated-source Vainshtein screening as automatically healthy.

### Scope limitation of that no-go

Their explicit static analysis:

- focuses outside a compact source where the physical metric is Schwarzschild/Ricci-flat;
- sets the second matter sector to zero for simplicity in the worked solution;
- is therefore not the same background as a cosmological void containing distributed `g` and `f` matter on an FLRW spacetime.

So it is a serious constraint, not a direct theorem excluding JANUS-R voids.

Primary reference:

- K. Aoki & S. Mizuno, *Vainshtein mechanism in massive gravity nonlinear sigma models*, Phys. Rev. D 94, 064054 (2016), arXiv:1607.00173.

---

## 6. Why cosmological void interiors are not covered directly by the Ricci-flat no-go

A uniform spherical top-hat region can be treated, at the separate-universe level, as a local FLRW patch. Such a patch is conformally flat but **not Ricci-flat** when matter/background energy density is present.

Likewise, the homogeneous exterior FLRW region is not Ricci-flat.

Therefore the Aoki-Mizuno scalar trace argument does not automatically force an instability throughout the void interior or homogeneous exterior.

The dangerous region is naturally the **transition/compensation wall**:

- density and Stückelberg gradients become large;
- the algebraic AMN branch develops its endpoint/large derivative;
- Weyl/tidal curvature is non-negligible;
- scalar and vector massive-graviton modes can mix.

This is exactly where the simplified algebraic/static calculations are least reliable.

---

## 7. Modern formalism for the missing calculation

Brizuela, de Cesare & Soler Oficial (2024), arXiv:2402.15327 / Phys. Rev. D 109, 124060, derive linear perturbation equations for **any spherically symmetric bimetric background**, including dynamical backgrounds.

Key features:

- axial and polar sectors are separated with tensor spherical harmonics;
- all seven bimetric propagating degrees of freedom are accounted for;
- the formalism is covariant on the two-dimensional Lorentzian orbit space;
- it can be applied to static or dynamical spherical backgrounds;
- they explicitly derive equations for a class of static nonbidiagonal backgrounds.

They do **not** solve the JANUS-R void stability problem. Their paper supplies the appropriate perturbative machinery.

Two cautions apply before direct use:

1. the AMN `mu != 0` branch is described as non-homothetic; that label must not be assumed identical to the specific nonbidiagonal vacuum class used as the worked example in the 2024 paper;
2. Brizuela et al. assume ordinary matter coupled to the `g` metric in their presentation, whereas JANUS-R keeps separate matter sectors, so the perturbative source sector must be extended accordingly.

---

## 8. Current scientific interpretation

There is now a plausible **environmental architecture**:

1. common/homogeneous regions remain close to the GR-like branch;
2. a strong relative source can drive the nonlinear scalar sector differently;
3. void-like anti-correlation can force a transition layer around the compensation wall;
4. the late Universe can be much less statically screened than the early transition epoch.

But the exact feature that could make JANUS-R observationally distinctive is also the feature most likely to destabilize it:

> the strong-gradient branch-transition wall.

Therefore environmental branch selection is not yet a success claim.

---

## 9. Revised gate

`ENVIRONMENTAL_SOURCE_SELECTIVITY = PASS_AT_SCALING/BRANCH_TOPOLOGY_LEVEL`

`LATE_STATIC_UNSCREENING = PLAUSIBLE_IN_SCALING_LIMIT`

`RICCI_FLAT_LOCAL_VAINSHTEIN_HEALTH = FAIL_FOR_AOKI_MIZUNO_BACKGROUND`

`COSMOLOGICAL_VOID_INTERIOR = NOT_EXCLUDED_BY_THAT_NO_GO`

`VOID_TRANSITION_WALL_FULL_STABILITY = OPEN__DECISIVE`

## 10. Next required calculation

The next high-value task is no longer another root scan. It is a gradient-resolved spherical stability problem:

1. construct a smooth compensated `g`-void + `f`-overdensity background on FLRW;
2. solve the background Stückelberg/metric profiles without dropping the transition gradients;
3. linearize the full axial and polar perturbations around that background;
4. inspect the principal kinetic/gradient matrices for ghosts and imaginary propagation speeds;
5. only if stable, compute the visible peculiar acceleration and Weyl/lensing profile.

A failure at step 4 would remove the main remaining environmental escape route for JANUS-R.
