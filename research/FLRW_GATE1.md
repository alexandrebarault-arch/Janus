# Gate 1 — two-matter FLRW background and high-k stability

Date: 2026-10-11

Status: `BACKGROUND_PASS__LINEAR_STABILITY_REQUIRES_PARAMETER_SELECTION_AND_EARLY_NONLINEAR_MATCHING`

## Purpose

Construct an explicit, reproducible JANUS-R background on the dynamical FLRW branch of ghost-free Hassan-Rosen bigravity with:

- two metrics `g` and `f`;
- separately coupled positive-energy matter sectors;
- `beta_0 = 0` (no explicit visible-sector cosmological constant);
- ordinary visible matter + radiation retained in `g`;
- twin dust in `f`;
- late self-acceleration from the interaction potential.

Background equations: Aoki & Maeda, arXiv:1312.7040.
High-k perturbative diagnostics: De Felice et al., arXiv:1404.0008.
Early nonlinear reference: Aoki, Maeda & Namba, arXiv:1506.04543.

Implementation: `numerics/flrw_two_matter.py`.

## Background equations

For flat FLRW,

`y = a_f/a_g`.

On the dynamical Bianchi branch,

`H_g = y H_f`.

With `M_f/M_g = alpha`, `beta_0=0`, and `H0=M_g=1`,

`E^2 = Omega_g(a) + (m^2/3) U_g(y)`,

`U_g = 3 beta_1 y + 3 beta_2 y^2 + beta_3 y^3`.

Combining the second Friedmann equation with the Bianchi relation gives

`Omega_g + (m^2/3)U_g - y^2 Omega_f/alpha^2 - (m^2 y^2/3 alpha^2)U_f = 0`,

where

`U_f = beta_4 + 3 beta_3/y + 3 beta_2/y^2 + beta_1/y^3`.

For f-sector dust this reduces exactly to a quartic in `y`; the code follows the continuous positive real root.

The relative lapse is

`n/N = y + d y/d ln a`,

and the De-Felice variable is

`ctilde = n a_g/(N a_f) = 1 + d ln y/d ln a`.

## Correction to the first Gate-1 analysis

An earlier version of this file treated

`m_eff^2 > 2 H^2`

as the general high-redshift Higuchi/no-ghost test. That was too strong and is **corrected here**.

For the two-fluid healthy branch, De Felice et al. derive the relevant high-k scalar kinetic condition in terms of

`B = 2 W + y^2 (rho_f + P_f)/(kappa M_g^2)`,

with `kappa=alpha^2`. The simple `m_eff^2-2H^2` expression is recovered only in an appropriate low-energy / pure-gravity limit. Therefore a zero of `W` or of the naive de-Sitter inequality is not by itself a demonstrated ghost in the two-fluid cosmology.

The code now evaluates explicitly:

- `J` — vector kinetic sign;
- `Gamma` and the exact background-dependent `m_eff`;
- `B` — scalar high-k no-ghost quantity;
- scalar high-k `c_s^2`;
- vector high-k `c_V^2`.

## Baseline A — clean background existence point

```text
beta_0 = 0
beta_1 = 1
beta_2 = -1.75
beta_3 = 0
beta_4 = 1.8160193651823988
alpha = 1
Omega_g,m0 = 0.30
Omega_g,r0 = 9e-5
Omega_f,m0 = 0.03
y0 = 0.175
m^2/H0^2 = 5.765024453024453
```

Background properties:

- regular continuous positive branch;
- positive lapse;
- `J>0`;
- self-acceleration with `beta_0=0`;
- `q0 ~= -0.566`, `z_acc ~= 0.70`;
- maximum `|H/H_LCDM-1|` over `0<=z<=2` about 1.3%;
- regular future de Sitter solution;
- exact `m_eff,0/H0 ~= 3.510` using the De-Felice `Gamma`, not the earlier simplified estimate.

### Exact high-k diagnosis

For Baseline A:

- `B>0` throughout the sampled history: **no scalar high-k ghost detected**;
- `c_V^2>0` throughout the sampled interval: **no vector gradient instability detected** there;
- scalar `c_s^2(0) ~= 0.903`;
- scalar `c_s^2` crosses zero at

`z ~= 1.822`.

Thus the real linear defect of Baseline A is a **scalar gradient instability above z~1.82**, not the previously claimed ghost at `z~17`.

Baseline A remains useful as a background regression test but is **rejected as the main perturbative candidate**.

## Stability–range search

A numerical parameter search was then performed with:

- `beta_0=0`;
- present Friedmann normalization enforced analytically;
- `beta_4` determined by the present second Friedmann constraint;
- continuous positive branch;
- positive lapse, `J`, `B` and late-time vector speed;
- near-LCDM low-redshift background;
- preference for a present spin-2 Compton range of order tens-to-hundreds of Mpc rather than a very short-range force.

A robust tradeoff appears:

**pushing linear scalar stability to very high redshift generally makes the massive spin-2 mode heavier and shortens the Compton range.**

Examples found in the scan include models stable linearly to very high redshift with `lambda_g ~ 10 Mpc`, but that range is too short for the large-void JANUS-R objective. Conversely, keeping `lambda_g ~ 100-150 Mpc` makes a nonlinear early phase difficult to avoid.

This is now considered a central design constraint, not a numerical accident.

## Candidate C — stability-extended Janus-range stress test

The current stress-test candidate is

```text
beta_0 = 0
beta_1 = 1
beta_2 = -4.2383993109
beta_3 = 13.6801214252
beta_4 = -38.5117901844
alpha = 0.10879548725
Omega_g,m0 = 0.30
Omega_g,r0 = 9e-5
Omega_f,m0 = 0.23958426762
y0 = 0.55688253212
m^2/H0^2 = 23.3348939346
```

Diagnostics:

- maximum background deviation from matched LCDM over `0<=z<=2`: about **3%**;
- `q0 ~= -0.517`;
- `m_eff,0/H0 ~= 42.31`;
- corresponding `c/(H0 m_eff/H0)` scale for `H0=70 km/s/Mpc`: about **101 Mpc**;
- `B>0` throughout the tested branch;
- scalar `c_s^2>0` until approximately **z=142.4**;
- vector `c_V^2>0` through that entire scalar-linear regime;
- naive vector high-k sign changes only much deeper in the extrapolated linear branch, around `z~8e4`, where the scalar linear description has already failed badly;
- regular late future.

It also satisfies

`beta_2 < 0`,

and

`beta_2^2 - beta_1 beta_3 > 0`.

Those coefficient signs are sufficient for a healthy nonlinear early branch in the **homothetic/spherical approximation** studied by Aoki-Maeda-Namba. They are **not** a proof for this non-homothetic dynamical Candidate C, so the result is recorded only as encouraging compatibility.

## What Gate 1 now establishes

1. A regular two-matter `beta_0=0` self-accelerating background exists.
2. The generalized two-fluid no-ghost test is less restrictive than the naive de-Sitter Higuchi inequality.
3. Simple moderate-parameter backgrounds can still fail by a scalar gradient instability at low redshift.
4. Parameter choices can postpone that instability by orders of magnitude while keeping a cosmologically interesting ~100 Mpc spin-2 scale.
5. This produces a real **stability–range tradeoff**: demanding linear validity arbitrarily far into the radiation era tends to remove the large-scale Janus effect by making the massive mode too heavy.

## What Gate 1 does NOT establish

It does not prove that Candidate C survives the nonlinear transition around the regime where the linear scalar mode ceases to be trustworthy. The 2023 literature still describes the GR/Vainshtein-to-bigravity transition as unsettled, despite explicit nonlinear solutions and numerical examples without catastrophic instabilities.

Therefore the appropriate status is not `FULL_STABILITY_PASS`.

## Gate-1 decision

- **Baseline A:** background PASS, perturbative candidate FAIL.
- **Candidate C:** retain as the main stability/range stress test.
- **Next decisive problem:** determine whether the nonlinear early GR/Vainshtein phase can connect continuously to Candidate C and, crucially, whether that transition can generate a significant relative `g-f` mode rather than merely suppressing it.

Do not spend effort optimizing the background to sub-percent precision until this segregation/transition gate is passed.
