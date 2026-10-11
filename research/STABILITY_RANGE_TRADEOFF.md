# Stability–range tradeoff in JANUS-R

Date: 2026-10-11

Status: `RESULT_NUMERICAL_SCAN__NOT_A_THEOREM`

## Question

Can the same ghost-free two-metric model simultaneously provide:

1. a long spin-2 Compton range, of order `~100 Mpc`, so that cross-sector effects remain relevant on large void/cosmic-web scales;
2. a near-LCDM late background with `beta_0=0`;
3. a sizable twin matter density;
4. a linear scalar sector stable arbitrarily far into the early universe?

## Result

A parameter scan of the two-matter finite/dynamical branch reveals a strong practical tradeoff:

**the farther the linear gradient-stable regime is pushed into the past, the heavier the massive spin-2 mode tends to become and the shorter its present Compton range becomes.**

This is physically reasonable. Linear stability in the early universe is easiest when the massive spin-2 scale is already large compared with the cosmological expansion scale. But the JANUS-R large-void mechanism wants the opposite phenomenology today: a sufficiently light massive mode that its scale dependence is still visible over tens-to-hundreds of Mpc.

## Reference points

### Baseline A

- `alpha = 1`
- `Omega_f0 = 0.03`
- `m_eff,0/H0 ~= 3.51`
- very long Compton scale;
- background within ~1.3% of matched LCDM over `z<=2`;
- high-k scalar gradient instability appears already at `z ~= 1.822`.

This is unacceptable as a purely linear cosmology but remains a background regression test.

### Candidate C

```text
beta1 = 1
beta2 = -4.2383993109
beta3 = 13.6801214252
beta4 = -38.5117901844
alpha = 0.10879548725
y0 = 0.55688253212
Omega_f0 = 0.23958426762
m^2/H0^2 = 23.3348939346
```

- `m_eff,0/H0 ~= 42.31`;
- reference Compton scale `c/(H0 m_eff/H0) ~= 101 Mpc` for `H0=70 km/s/Mpc`;
- background deviation from matched LCDM over `z<=2` about 3%;
- generalized scalar kinetic quantity `B>0`;
- scalar `c_s^2>0` until `z ~= 142.4`;
- vector `c_V^2>0` throughout that entire scalar-linear interval;
- satisfies `beta2<0` and `beta2^2-beta1 beta3>0`, the coefficient-sign condition used as a sufficient nonlinear-stability criterion in the homothetic/spherical analysis of Aoki-Maeda-Namba.

This does **not** prove Candidate C is fully stable: the Aoki nonlinear criterion was derived in a more restricted background than Candidate C.

### Very-high-redshift linear candidates

The scan also finds points for which scalar linear stability can be pushed much further back, including into or beyond recombination. In general those points require a significantly heavier spin-2 mode, with representative present Compton ranges of only tens of Mpc or less. Extreme examples reach ~10 Mpc.

Such points are less useful for the JANUS-R goal because they erase the desired long-range cross-sector effect.

## Literature cross-check

This numerical tradeoff is consistent with the known cosmological Vainshtein picture.

Lüben, Schmidt-May & Smirnov (Phys. Rev. D 102, 123529, 2020; arXiv:1912.09449) identify the spin-2 mass as the cosmological Vainshtein scale: at early times/large densities the massive interaction is screened and GR-like evolution is restored; modifications emerge once the cosmic energy scale falls toward the spin-2 scale.

The 2023 review/phenomenology analysis by Bassi et al. likewise treats the early linear instability as a regime where nonlinear effects are required and explicitly notes that the detailed transition remains an open issue.

Relevant sources:

- https://arxiv.org/abs/1912.09449
- https://doi.org/10.1103/PhysRevD.102.123529
- https://doi.org/10.1140/epjc/s10052-023-11707-4

## Interpretation

The correct requirement is therefore **not** “force the model to stay linear all the way to the Big Bang.” Doing so tends to destroy the long-range phenomenology we are trying to test.

The physically motivated architecture is instead:

1. early high-density epoch: nonlinear/Vainshtein-screened, approximately GR;
2. transition when the cosmological scale approaches the relevant spin-2 scale;
3. late epoch: linear or weakly nonlinear bimetric regime with observable scale dependence.

The difficult question is no longer whether an early nonlinear phase can exist — there is substantial evidence it can — but whether the transition can be **continuous, stable and capable of exciting the relative twin mode strongly enough** for Janus-like segregation.

## Decision

Candidate C is retained as the principal `~100 Mpc` stress-test point.

Do not replace it by a very-heavy, fully linear early-universe point merely to avoid nonlinear physics: that would solve the stability issue by removing the large-scale Janus phenomenology.

Next file: `SEGREGATION_GATE.md`.
