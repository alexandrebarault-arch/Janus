# V2 Initial Lapse Admissibility Basin

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `FINITE_SAFE_BASIN_FOUND__LAPSE_GATE_IS_NONTRIVIAL`

## Purpose

After the reference wall passed the time-symmetric secondary-constraint lapse gate, determine whether it is

1. an isolated fine-tuned point, or
2. part of a finite basin of regular initial data.

This remains an **initial-slice** study. No time evolution is inferred.

Reproducible evaluator:

`numerics/initial_lapse_family_scan.py`

Regression tests:

`tests/test_initial_lapse_family_scan.py`.

Local verification after implementation:

`6 passed in 0.65s`

for the combined initial-lapse + family-scan tests.

## 1. Independent matter-amplitude scan

Hold the reference interaction parameters fixed:

- `beta1=1`;
- `beta2=-0.2`;
- `beta3=0`;
- interaction scale `0.02`;
- f Gaussian width `2`;
- g shell radius `5`, width `1`.

Vary independently the f-centre amplitude and g-shell amplitude by multipliers

`0.25, 0.5, 1, 2, 4, 8`.

All **36/36** combinations

- solved the nonlinear Hamiltonian constraints;
- kept positive conformal factors;
- had finite `W`;
- retained `W>0` over the full radial domain.

Across this grid the smallest lapse ratio encountered was about `0.70`.

Therefore the reference is not a narrow amplitude fine tuning.

## 2. Extreme one-sector amplitude probes

### Increase only the g shell

With the reference f centre fixed, increasing the g-shell amplitude through multipliers

`0, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 128`

kept the initial lapse branch admissible throughout the tested range.

This does **not** establish physical relevance at huge amplitudes; it only shows that the lapse branch is not fragile to a much stronger g shell in this family.

### Increase only the f centre

With the reference g shell fixed, the f-centre branch behaved differently:

- multipliers through `~12` remained on the positive lapse branch;
- shortly above that, `W_g` develops radial zeros and a finite interval with `W<0` appears;
- by `16x` the configuration is clearly outside the selected same-time-orientation branch.

A numerical bisection places the onset close to `~12.08x` in the current regularized setup, but **this should not be quoted as a universal physical threshold**.

Near onset one zero lies very close to the origin and is sensitive to the numerical inner radius. However a second zero remains at a finite radius under changes in `r_min`, showing that the forbidden interval itself is not merely an origin artifact.

Examples:

- at `12.08x`, a stable outer zero remains around `r≈0.063–0.070` while `r_min` is varied from `1e-6` to `1e-3`;
- at `12.1x`, the outer zero is around `r≈0.17–0.19` over the same check.

Scientific interpretation:

`VERY_STRONG_TWIN_CENTRE_CAN_EXIT_LAPSE_BRANCH = YES`.

## 3. Interaction-parameter map

Keep the reference matter profiles and scan

- `beta1=1` fixed;
- `beta2` from `-0.40` to `+0.05` in steps of `0.025`;
- `beta3` from `-0.25` to `+0.25` in steps of `0.025`;
- flat asymptotic completion of `beta0,beta4`;
- interaction scale `0.02`.

Total points:

`399`.

Results:

- nonlinear Hamiltonian BVP converged at **399/399** points;
- lapse branch remained admissible at **351/399** points;
- **48/399** points developed `W<=0` somewhere despite regular constraint data.

Thus the lapse gate adds genuine information that is absent from the Hamiltonian constraints alone.

### Unsafe coarse/fine-grid structure

The forbidden points form a structured band concentrated at more negative `beta2/beta3` combinations. On the `0.025` grid, unsafe `beta3` values occur for:

- `beta2=-0.400`: `-0.250,-0.225,-0.050,-0.025,0,0.025,0.050,0.075,0.100`;
- `beta2=-0.375`: `-0.100,-0.075,-0.025,0,0.025,0.050`;
- `beta2=-0.350`: `-0.150,-0.125,-0.100,-0.075,-0.050,-0.025,0`;
- `beta2=-0.325`: `-0.200,-0.175,-0.150,-0.125,-0.100,-0.075,-0.050`;
- `beta2=-0.300`: `-0.225,-0.200,-0.175,-0.150,-0.125,-0.100,-0.075`;
- `beta2=-0.275`: `-0.250,-0.225,-0.200,-0.175,-0.150,-0.125`;
- `beta2=-0.250`: `-0.250,-0.225,-0.200,-0.175`;
- `beta2=-0.225`: `-0.250,-0.225`.

No forbidden points were found on this grid for `beta2>=-0.200`.

This last statement is only about the scanned rectangle/profile; it is not a theorem for all data.

## 4. Resolution check of representative points

Representative safe/unsafe classifications were repeated at `260` and `600` initial radial points with tighter BVP tolerances.

Examples:

- `(-0.35,+0.10)`: safe at both resolutions, `W_min≈0.7861`;
- `(-0.30,-0.05)`: safe at both, `W_min≈0.8097`;
- `(-0.25,-0.15)`: safe at both, `W_min≈0.8195`;
- `(-0.35,-0.10)`: unsafe at both, with two `W_g` and two `W_f` sign changes;
- `(-0.35,0)`: unsafe at both, with two `W_g` zeros;
- `(-0.30,-0.15)`: unsafe at both;
- `(-0.25,-0.20)`: unsafe at both;
- `(-0.225,-0.225)`: unsafe at both.

The divergence magnitude near a zero is grid-sensitive, as expected; the **classification and finite radial zero structure** are stable.

## 5. The failure lives in the compensation wall

For representative unsafe parameter points, the forbidden interval is centred on the g-shell / transition region, not at the outer boundary.

Examples at higher radial resolution:

### `beta2=-0.35, beta3=-0.10`

- first `W_g` zero near `r≈4.53`;
- second `W_g` zero near `r≈6.66`;
- `W<0` through most of that interval.

### `beta2=-0.35, beta3=0`

- `W_g` zeros near `r≈5.15` and `r≈5.91`;
- `W_f` need not cross in this example;
- the ratio therefore flips sign inside the shell.

### `beta2=-0.275, beta3=-0.20`

- `W_g` zeros near `r≈4.70` and `r≈6.41`;
- `W_f` zeros lie slightly inside those radii;
- the mismatch creates a finite `W<0` band.

This independently reinforces the earlier conclusion that the **transition/compensation wall is the decisive region** of JANUS-R.

## 6. Not a simple beta-polynomial zero

At representative radial zeros, the basic interaction combinations such as

`P = beta1 + 2 beta2 R + beta3 R^2`

remain clearly nonzero.

The branch loss is therefore not explained by a trivial zero of a single interaction polynomial. It is produced by the full radial combination of

- both metric factors;
- their radial gradients;
- the two matter profiles;
- interaction coefficients.

Practical consequence:

**keep `W_g(r),W_f(r),W(r)` as explicit numerical gates in all future wall calculations.**

Do not replace them by a one-line beta inequality inferred from this scan.

## Current verdict

`REFERENCE_WALL_FINE_TUNED_IN_AMPLITUDE = NO`

`FINITE_INITIAL_LAPSE_BASIN = YES`

`LAPSE_BRANCH_FILTER_NONTRIVIAL = YES`

`TRANSITION_WALL_REMAINS_DECISIVE = YES`

`DYNAMIC_WALL = STILL OPEN`

The scan strengthens the case for performing a real standard-3+1 evolution: a sizeable initial-data basin survives, while the lapse condition is selective enough to provide a meaningful falsification criterion rather than automatically passing every regular constraint solution.
