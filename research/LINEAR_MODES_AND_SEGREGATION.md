# Linear unscreened modes and segregation strength

Date: 2026-10-11

Status: `DERIVED_TOY_LIMIT`

Scope: proportional-Minkowski / subhorizon quasi-static intuition for ghost-free bimetric gravity with two separately coupled pressureless matter sectors. Equal Planck masses are used for the cleanest symmetric formulas. This is a diagnostic, not yet the full FLRW perturbation system.

## 1. Fourier-space kernels

For equal Planck masses, normalize all gravitational responses to the long-wavelength cross/self Newton coupling `G_inf`.

Let

`x(k) = k^2 / (k^2 + a^2 mu^2)`, with `0 <= x <= 1`.

The slow-matter (Newtonian/dynamical) response inferred from the Hohmann point-source solution is

`Q_dyn,self = 1 + (4/3) x`,

`Q_dyn,cross = 1 - (4/3) x`.

Thus:

- `k << a mu`: both sectors attract each other like ordinary gravity (`Q -> 1`);
- `k >> a mu`: self-attraction becomes `7/3`, while cross interaction becomes `-1/3`.

The cross repulsion therefore never approaches `-G_inf`; in this linear two-metric realization its asymptotic value is only `-G_inf/3`.

## 2. Lensing kernels

Because photons have traceless stress-energy, the helicity-0 trace coupling responsible for the `4/3` vDVZ enhancement of slow-matter forces does not contribute in the same way.

The corresponding lensing/Weyl kernels are

`Q_lens,self = 1 + x`,

`Q_lens,cross = 1 - x`.

Consequences:

- cross-sector lensing is always non-negative;
- for `k >> a mu`, an `f` source can repel a slow `g` test mass while its direct contribution to `g`-photon lensing tends to zero;
- the difference between dynamical and lensing response is a potential observable.

## 3. Eigenmodes for symmetric twin backgrounds

For equal background densities and equal Planck masses, define

`delta_plus = delta_g + delta_f`  (common/adiabatic mode),

`delta_minus = delta_g - delta_f` (relative/segregation mode).

The dynamical coupling matrix is

```
Q_dyn = [[1 + 4x/3, 1 - 4x/3],
         [1 - 4x/3, 1 + 4x/3]].
```

Its eigenvalues are

`lambda_plus = 2`,

`lambda_minus = 8x/3`.

After including the factor `rho_total/2` carried by each equal background fluid, the common mode has the usual GR effective strength `mu_plus = 1`, while the relative mode has

`mu_minus = 4x/3`.

Thus the new physics acts primarily on relative/isocurvature perturbations while leaving the common mode unchanged in this idealized limit.

## 4. Linear growth rate

In an Einstein-de Sitter approximation, for

`delta ~ a^p`, with effective gravitational strength `mu_eff`,

`p = [-1 + sqrt(1 + 24 mu_eff)] / 4`.

For the maximally unscreened relative mode (`x -> 1`):

`mu_minus = 4/3`,

`p_minus = [-1 + sqrt(33)]/4 ~= 1.186`.

The common mode has `p_plus = 1`.

Therefore the segregation mode grows faster than the common density mode, but only modestly:

`delta_minus/delta_plus ~ a^0.186`.

Examples if the unscreened phase begins with comparable mode amplitudes:

- from `z=1` to today: relative advantage `~2^0.186 ~= 1.14`;
- from `z=10` to today: `~11^0.186 ~= 1.56`;
- from `z=20` to today: `~21^0.186 ~= 1.76`.

Hence the linear two-metric mechanism alone cannot generate an enormous matter-sector segregation from an initially tiny relative perturbation during only the late Universe.

## 5. Pure segregation-mode lensing/dynamics mismatch

For `delta_f = -delta_g`, the visible-sector responses are proportional to

`Dynamical source ~ (8x/3) delta_g`,

`Weyl/lensing source ~ 2x delta_g`.

Therefore, in the unscreened linear relative mode,

`Weyl response / dynamical response = 3/4`.

This is the same spin-2 trace-structure origin as the vDVZ `3/4` light-bending relation.

For a visible void (`delta_g < 0`) accompanied by an `f` overdensity (`delta_f > 0`), the combined lensing can still be void-like (negative convergence), but this comes from the anti-correlated density mode; it is **not** negative lensing by an isolated positive-energy `f` mass.

## 6. Research consequence

`JANUS-R Late` remains mathematically interesting, but its linear two-metric sector is too weak to reproduce the exact strong `+G/-G` Janus segregation by itself.

The project therefore has three possibilities:

1. nonlinear late-time dynamics substantially amplifies the relative mode;
2. a non-negligible primordial/early relative mode survives cosmological screening and is later amplified;
3. a ghost-free multimetric (`N >= 3`) architecture is required for stronger/exact cross-repulsion.

The next two gates are therefore:

- determine whether nonlinear/Vainshtein cosmological evolution enhances or suppresses the relative mode in voids;
- independently investigate modern ghost-free multimetric interaction graphs for stronger Janus-like sign matrices.
