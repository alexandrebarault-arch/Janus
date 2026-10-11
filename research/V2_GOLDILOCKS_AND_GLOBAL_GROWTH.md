# V2 Goldilocks sign-flip window and global-growth tension

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `POSITIVE_MECHANISM_FOUND__UNIVERSAL_LINEAR_VERSION_STRONGLY_DISFAVORED`

## 1. Why this calculation was needed

Earlier V2 work produced two apparently conflicting requirements:

1. the early Universe must be GR-like / nonlinearly screened while `H >> m_eff`;
2. a sizeable relative mode must exist late enough to generate Janus-like segregation.

A symmetric homothetic system cannot generate a relative mode from a perfectly common seed at linear order. However, the actual two-fluid system need not have equal background weights.

The toy model in `numerics/asymmetric_twofluid.py` shows that unequal sector weights mix the initially common perturbation into the relative mode once the modified spin-2 kernel becomes active.

This means that a primordial isocurvature seed is **not strictly required** in the reduced model.

## 2. Self-consistent transition model

`numerics/self_consistent_transition.py` couples two ingredients:

- approximate low-energy Higuchi crossing `m_eff^2 ~= 2 H^2`, which sets a transition redshift for a chosen Compton length `lambda_g`;
- time-dependent quasi-static kernel

  `x(k,a) = k^2 / (k^2 + a^2 m_eff^2)`.

Before the transition, the model assumes the nonlinear early phase has kept the two sectors on a common GR-like growing mode.

After the transition, the toy integrates the maximally available linear two-fluid response on an EdS background.

This is deliberately optimistic and therefore acts as an **upper-bound / feasibility** calculation, not a cosmological prediction.

## 3. A genuine sign-flip mechanism exists

Start from a common proto-void:

`delta_g = delta_f < 0` at the transition.

If the visible sector has a sufficiently large effective background weight `f_g`, modified gravity can make the twin perturbation cross zero and become positive by today:

`delta_g < 0`, `delta_f > 0`.

That is a true Janus-like anti-correlation generated from an initially common mode.

### Representative scale-space result

For `H0=70 km/s/Mpc`, `Omega_m0=0.30`, and the maximal two-metric kernel, a Compton length near `100 Mpc` gives a transition around

`z_H ~= 13.5`.

At that transition, the constant-`x` control gives a twin sign flip only if the effective visible background weight is roughly

`f_g > 0.80`

when `x` is essentially maximal.

For `f_g=0.90`, the sign-flip threshold in the constant-`x` control is around

`x_crit ~= 0.892`.

The exact numbers are toy-model dependent; the structural result is that both **background asymmetry** and **strong late unscreening** are required.

## 4. Goldilocks behavior when the mass scale is treated consistently

The same `lambda_g` controls two competing effects:

- shorter `lambda_g` -> larger mass -> earlier Higuchi crossing, giving more time to segregate, but weaker modification on a fixed spatial scale;
- longer `lambda_g` -> stronger modification on a fixed scale, but a later transition, leaving less time to segregate.

Therefore the sign flip occurs only in a finite interval of `lambda_g`.

Using the representative mapping `k ~= pi/R`, for `f_g=0.90` the toy gives approximate sign-flip intervals:

| characteristic structure | sign-flip `lambda_g` band |
|---:|---:|
| 50 Mpc | 11-206 Mpc |
| 100 Mpc | 25-202 Mpc |
| 150 Mpc | 41-194 Mpc |
| 200 Mpc | 62-182 Mpc |

The common intersection across all four scales is about

`lambda_g ~= 62-182 Mpc`.

**Important:** the numerical interval depends on how a real void profile is mapped to a representative Fourier mode. Replacing `k=pi/R` by another convention moves the lower edge significantly. The existence of the competing lower/upper bounds is more robust than the quoted numbers.

## 5. More honest k-space scan

Avoiding the arbitrary `R -> k` mapping, scan directly in Fourier scale.

For `f_g=0.90` the toy sign-flip bands are approximately:

| `k [h/Mpc]` | `lambda_g` sign-flip band |
|---:|---:|
| 0.005 | none found |
| 0.010 | none found |
| 0.020 | 75-172 Mpc |
| 0.030 | 41-194 Mpc |
| 0.050 | 22-203 Mpc |
| 0.100 | 10-206 Mpc |

Thus the mechanism naturally targets intermediate large-scale-structure modes rather than arbitrarily large wavelengths.

For smaller visible weight it becomes harder. Examples:

- `f_g=0.85`: sign flip appears from about `k~0.03 h/Mpc` upward;
- `f_g=0.80`: in this scan it appears only around `k>=0.05 h/Mpc`;
- even `f_g=0.95` did not produce a sign flip at `k<=0.01 h/Mpc` over the scanned mass range.

## 6. Critical problem: global visible growth becomes far too strong

The same coupling that produces the sign flip strongly enhances the visible growing mode.

Representative point:

`f_g=0.90`, `lambda_g=100 Mpc`, `z_H~=13.5`.

The EdS control gives approximately:

| `k [h/Mpc]` | visible transfer `T_g` | twin transfer `T_f` | GR transfer `1+z_H` | visible enhancement |
|---:|---:|---:|---:|---:|
| 0.01 | 42.3 | +4.0 | 14.5 | 2.9x |
| 0.02 | 48.3 | -0.68 | 14.5 | 3.3x |
| 0.03 | 50.1 | -2.11 | 14.5 | 3.45x |
| 0.05 | 51.2 | -2.99 | 14.5 | 3.53x |
| 0.10 | 51.7 | -3.39 | 14.5 | 3.56x |

The sign-flip region is therefore also a region of order-unity modification of global structure growth in this universal linear toy.

## 7. Observational cross-check

This is strongly disfavored as a **universal linear** modification.

DESI DR1 full-shape modified-gravity analyses find no significant deviation from GR. In a common phenomenological parameterization, DESI + CMB + DES analyses reported approximately

`mu_0 = 0.05 +/- 0.22`,

`Sigma_0 = 0.008 +/- 0.045`,

with scale-binned modified-gravity parameters also consistent with GR.

Reference:

- DESI Collaboration / Ishak et al., *Modified Gravity Constraints from the Full Shape Modeling of Clustering Measurements from DESI 2024*, arXiv:2411.12026.

DESI + weak-lensing `E_G` measurements also find the relative lensing/velocity response consistent with GR to `z~1`:

- Rauhut et al., arXiv:2507.16098.

A 2026 DESI scale-dependent-gravity analysis found no evidence for a Yukawa-like scalar fifth force and constrained its range to `<17.81 Mpc` within the tested `f(R)` model:

- Gonzalez et al., arXiv:2604.26915.

That numerical bound **cannot be transferred directly** to a massive spin-2/twin-matter model, but it demonstrates how strongly DESI already constrains universal modifications on the `k` scales relevant here.

## 8. Main conclusion

`UNIVERSAL_LINEAR_JANUS_SIGN_FLIP = STRONGLY_DISFAVORED`

The positive result is not discarded; it changes the architecture of the surviving hypothesis.

The only credible route now is:

> ordinary linear LSS remains close to GR because the extra mode is screened/suppressed in typical environments, while low-density or strongly relative two-sector configurations can move onto a different nonlinear response and generate a void-specific segregation effect.

In other words, JANUS-R must become an **environment-dependent nonlinear theory**, not a universal late-time linear fifth-force model.

## 9. Next decisive gate

Test whether Vainshtein/nonlinear response can provide exactly that selectivity:

1. GR-like response for ordinary/common overdensity modes;
2. stronger response for a visible underdensity coupled to a twin-sector overdensity;
3. self-limiting screening before the void velocity/lensing signal becomes incompatible with DESI and current void data.

The Aoki-Maeda-Namba source structure is encouraging because the nonlinear scalar is driven by the weighted **difference** of the two sector perturbations. But the required environment-selective window has not yet been demonstrated.
