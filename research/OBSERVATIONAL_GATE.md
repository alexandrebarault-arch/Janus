# Observational gate: void lensing and dynamics

Date: 2026-10-11

Status: `CONSTRAINING_BUT_NOT_YET_A_FORMAL_FIT`

## 1. Current measurements that matter most

### Void CMB lensing

Sartori et al. (A&A 700, A17, 2025) cross-correlate DESI Legacy Survey DR9 LRG voids with the Planck 2018 CMB lensing map. Their spectroscopically calibrated ΛCDM template gives, for the full void sample,

`A_kappa = 1.016 +/- 0.054`,

with a 14-sigma lensing detection. The void-in-void and void-in-cloud subsamples are also consistent with the calibrated ΛCDM mocks.

Interpretation for JANUS-R: current void lensing leaves little room for an arbitrary order-unity distortion of the lensing profile. Any viable Janus-like sector must either produce a modest correction, lie near a response crossover, or alter the galaxy/void profile in a correlated way that must be simulated self-consistently.

### Lensing versus velocities (`E_G`)

Rauhut et al. (Open Journal of Astrophysics, 2025; arXiv:2507.16098) combine DESI DR1/BOSS clustering with KiDS, DES and HSC weak lensing and measure `E_G`, a statistic designed to compare lensing and galaxy velocities sourced by the same large-scale overdensities. They report consistency with the Planck GR+ΛCDM prediction to `z ~ 1`.

Interpretation for JANUS-R: a large universal lensing/dynamics mismatch is not currently indicated by the data. This is directly relevant because such a mismatch is one of the cleanest signatures of the bimetric relative mode.

### Scale-dependent modified gravity with DESI DR1

Gonzalez et al. (2026; arXiv:2604.26915) find no evidence for a Yukawa-like scalar modification in their Hu-Sawicki `f(R)` mapping and constrain its present-day correction scale to `<17.81 Mpc` (95% CL) in that model.

This is **not** a bound on the spin-2 JANUS-R interaction: the tensor structure, screening and matter couplings differ. It is nevertheless a useful warning that DESI full-shape clustering is already sensitive to new gravitational scales in the tens-of-Mpc range, so a `~100 Mpc` JANUS-R effect cannot be assumed observationally invisible.

## 2. Correct linear JANUS-R void kernels

In the equal-Planck-mass unscreened linear diagnostic, define

`x = k^2/(k^2 + a^2 mu^2)`, `0 <= x <= 1`.

For a visible-sector underdensity

`delta_g = -D`, `D > 0`,

and a twin-sector overdensity

`delta_f = R D`, `R >= 0`,

the visible lensing/Weyl source relative to the GR visible-only void source is

`A_lens = (1 + x) - R (1 - x)`.

The slow-matter/dynamical response is

`A_dyn = (1 + 4x/3) - R (1 - 4x/3)`.

These formulas correct a possible misreading of the previously derived `3/4` ratio: that ratio is **lensing divided by dynamics for the pure equal-amplitude relative mode**, not a universal 25% suppression of void lensing versus ΛCDM at fixed visible density.

## 3. Equal anti-correlated mode

For the particularly Janus-like case

`R = 1`, i.e. `delta_f = -delta_g`,

we obtain

`A_lens = 2x`,

`A_dyn = 8x/3`,

and therefore

`A_lens/A_dyn = 3/4`.

Several important consequences follow.

### Same visible void profile

At high `k` (`x -> 1`) the lensing amplitude is **twice** the GR visible-only value, while the dynamical response is `8/3` times GR.

At low `k` (`x -> 0`) both responses vanish because the massless long-range mode sees nearly cancelling weighted positive/negative density contrasts of the two sectors.

At the crossover `x = 1/2`,

`A_lens = 1`,

so the lensing can look exactly GR-like even though

`A_dyn = 4/3`.

Thus a Janus-like mode can hide in a lensing-only comparison near the spin-2 crossover while still predicting substantially altered velocities.

## 4. Toy inversion of the 2025 void-lensing amplitude

This is **not a likelihood fit**. Assume, only as a diagnostic, that:

1. the observed void profile corresponds to the same visible density profile as the ΛCDM mock;
2. `R = 1`;
3. the relevant mode can be represented by a single effective `x`;
4. nonlinear screening/profile-selection effects are negligible.

Then

`A_kappa = 2x`.

Using `A_kappa = 1.016 +/- 0.054` gives

`x = 0.508 +/- 0.027`.

The corresponding dynamical response is forced to be

`A_dyn = (4/3) A_kappa = 1.355 +/- 0.072`.

So the equal anti-correlated toy mode that hides in current void lensing would predict roughly a **35% enhancement in slow-matter/velocity response** for the same effective source.

That is a sharp target for velocity/RSD/`E_G` measurements.

Because current DESI+weak-lensing `E_G` results are reported as consistent with GR, an unscreened equal-amplitude relative mode dominating ordinary large-scale structure is already under pressure. A formal exclusion requires the actual JANUS-R transfer functions, covariance, galaxy bias and selection functions; the abstract consistency statement alone is not sufficient to quote a valid sigma exclusion.

## 5. General degeneracy curve

If lensing is required to stay at its GR value, `A_lens = 1`, then

`R = x/(1-x)`.

Along this curve the dynamical response is

`A_dyn = (3 - 2x)/[3(1-x)]`.

Hence hiding the modification in lensing does not generically hide it dynamically. As `x` increases, the twin overdensity required to maintain standard lensing grows and the velocity deviation becomes increasingly large.

This provides a practical strategy for a future joint fit:

- void lensing constrains a combination of `(x,R)`;
- velocities/RSD constrain an independent combination;
- their intersection can determine or exclude the twin-sector amplitude and spin-2 interaction scale.

## 6. What observations currently say

### Strong conclusion

A large, arbitrary Janus-like modification of late-time void lensing is **not supported** by current data. The 2025 DESI-Legacy/Planck void signal agrees closely with calibrated ΛCDM mocks.

### Moderate conclusion

A specially structured bimetric relative mode is **not yet excluded by the lensing result alone**, because the spin-2 kernels possess crossover/cancellation directions. But such hiding generically produces a dynamics-lensing mismatch, for which current `E_G` measurements show no evidence.

### What cannot yet be claimed

We cannot quote a rigorous bound on the density fraction of the `f` sector or on `m_FP` from these measurements without computing the full two-matter transfer functions and fitting the actual likelihoods.

## 7. Decision

`STRONG_LATE_JANUS_SEGREGATION_AS_DOMINANT_LSS_MODE = DISFAVORED`

`SUBDOMINANT_OR_CROSSOVER_JANUS_R_MODE = STILL_OPEN`

`NEGATIVE_LENSING_BY_ISOLATED_POSITIVE_F_MASS = NOT_A_PREDICTION_OF_THIS_MODEL`

The project should now prioritize a joint lensing+dynamics calculation rather than a lensing-only void profile.
