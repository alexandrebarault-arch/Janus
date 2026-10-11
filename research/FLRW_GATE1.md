# Gate 1 — two-matter FLRW background

Date: 2026-10-11

Status: `BACKGROUND_PASS_WITH_EARLY_NONLINEAR_CONDITION`

## Purpose

Construct an explicit, reproducible JANUS-R background on the dynamical FLRW branch of ghost-free Hassan-Rosen bigravity with:

- two metrics `g` and `f`;
- separately coupled positive-energy matter sectors;
- `beta_0 = 0` (no explicit visible-sector cosmological constant);
- ordinary visible matter + radiation retained in `g`;
- a subdominant twin dust background in `f`;
- late self-acceleration from the interaction potential.

Primary equations: Aoki & Maeda, *Cosmology in ghost-free bigravity theory with twin matter fluids* (arXiv:1312.7040), especially Eqs. (42), (44), (48)-(53):
https://arxiv.org/abs/1312.7040

Implementation: `numerics/flrw_two_matter.py`.

## Equations used

For flat FLRW,

`y = a_f / a_g`.

On the dynamical Bianchi branch,

`H_g = y H_f`.

With `M_f/M_g = alpha`, `beta_0=0`, and `H0=M_g=1`, the visible Friedmann equation is

`E^2 = Omega_g(a) + (m^2/3) U_g(y)`,

with

`U_g = 3 beta_1 y + 3 beta_2 y^2 + beta_3 y^3`.

The second Friedmann equation combined with `H_g=y H_f` gives the algebraic constraint

`Omega_g + (m^2/3) U_g - y^2 Omega_f/alpha^2 - (m^2 y^2/3 alpha^2) U_f = 0`,

where

`U_f = beta_4 + 3 beta_3/y + 3 beta_2/y^2 + beta_1/y^3`.

For f-sector dust only, multiplying by `alpha^2 y` reduces this exactly to a quartic in `y`. The solver follows the continuous positive real root rather than integrating two independent scale factors.

The lapse ratio is derived from Bianchi rather than guessed:

`N_f/N_g = y + d y / d ln a`.

## Explicit benchmark

The first simple benchmark retained for V2 is

```text
beta_0 = 0
beta_1 = 1
beta_2 = -1.75
beta_3 = 0
beta_4 = 1.8160193651823988
alpha = M_f/M_g = 1
Omega_g,m0 = 0.30
Omega_g,r0 = 9e-5
Omega_f,m0 = 0.03   # normalized to 3 M_g^2 H0^2
y0 = 0.175
m^2/H0^2 = 5.765024453024453
```

This is **not** claimed to be a best fit. It is a clean existence benchmark with moderate interaction coefficients and a non-negligible twin sector.

## Reproducible checks

The code verifies:

- present visible Friedmann normalization `E(0)=1`;
- the second Friedmann/branch constraint to numerical precision;
- one continuous positive root from `a=1e-8` through today;
- positive lapse ratio throughout every finite sampled epoch;
- `J(y)=beta_1+2 beta_2 y+beta_3 y^2 > 0` throughout the sampled history;
- positive `H^2`;
- continuation from today to `a=100` without branch loss;
- future approach to de Sitter (`q -> -1`);
- late de Sitter massive-spin-2 mass well above the de Sitter Higuchi bound.

## Background numbers

For the benchmark:

- `m_eff/H0(today) = 3.62717`;
- acceleration begins at `z_acc ~= 0.70`;
- `q0 ~= -0.566` (analytic implicit derivative; not a one-sided finite-difference estimate);
- maximum `|H/H_LCDM - 1|` over `0 <= z <= 2` is about **1.3%**;
- comoving-distance difference relative to matched `Omega_m=0.30` flat LCDM is about **+0.36% at z=0.5**, **+0.61% at z=1**, **+0.84% at z=2**;
- dimensionless age differs from matched LCDM by about **+0.7%**;
- future asymptote: `y -> 0.179824...`, `E^2 -> 0.71045...`, `q -> -1`.

Representative expansion values:

| z | H/H0 JANUS-R | H/H0 matched LCDM | fractional difference |
|---:|---:|---:|---:|
| 0 | 1.0000 | 1.0000 | 0 |
| 0.5 | 1.2994 | 1.3088 | -0.72% |
| 1 | 1.7413 | 1.7611 | -1.12% |
| 2 | 2.9317 | 2.9677 | -1.21% |
| 5 | 8.0660 | 8.1004 | -0.42% |
| 10 | 20.0162 | 20.0329 | -0.083% |

The interaction therefore becomes practically invisible in the background at high redshift even though the two metrics are not identical.

## Important early-time caveat

The benchmark is a **finite branch**. Deep in radiation domination,

`y ~ 1.786 a`,

so the lapse ratio tends to zero only asymptotically at the big-bang boundary and remains positive at every finite sampled scale factor.

However,

`m_eff^2 / H^2`

becomes very small at high redshift. The naive *linear* de Sitter-like Higuchi criterion `m_eff^2 > 2 H^2` stops being satisfied at approximately

`z ~ 17`.

This is not hidden or counted as a linear-stability pass. It is precisely the regime in which Aoki, Maeda & Namba showed that linear bimetric perturbation theory becomes unreliable and nonlinear scalar/Vainshtein effects can restore a GR-like stable early universe for suitable interaction parameters:
https://arxiv.org/abs/1506.04543

Therefore the current verdict is:

`BACKGROUND_PASS_WITH_EARLY_NONLINEAR_CONDITION`

not `FULL_STABILITY_PASS`.

## What this result establishes

It falsifies a possible objection that a JANUS-R continuation necessarily fails already at homogeneous background level once `beta_0=0`, a twin matter density, a positive lapse and a regular future are required.

At least one simple parameter point gives:

- radiation era;
- matter era;
- late acceleration without explicit Lambda;
- background expansion close to LCDM;
- no background branch singularity;
- no sign change of `J`;
- a regular de Sitter future.

## What it does NOT establish

It does not yet prove:

- scalar/vector/tensor perturbative stability over the full history;
- successful CMB transfer functions;
- a viable twin-sector initial spectrum;
- nonlinear branch continuity for this exact beta point;
- observational superiority over LCDM.

These are Gates 2 and 3.

## Gate-1 decision

**Retain benchmark for the next calculations.**

Do not optimize its background fit further yet. A 1% background improvement is scientifically irrelevant if the perturbations later fail.
