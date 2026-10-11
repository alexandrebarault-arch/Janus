# V2 cosmic transition gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `MAIN_THEORETICAL_BOTTLENECK_IDENTIFIED`

Primary source: K. Aoki, K.-i. Maeda, R. Namba, *Stability of the Early Universe in Bigravity Theory*, Phys. Rev. D 92, 044054 (2015), arXiv:1506.04543.

## Question

Can a realistic cosmic history begin in the nonlinear GR-like/cosmological-Vainshtein phase at `H >> m_eff`, then evolve into the late homogeneous linear bigravity branch `mu -> 0` without hitting an unstable, complex or singular transition?

This is more important than merely finding a real nonlinear root.

## Reproducible proxy trajectory

`numerics/cosmic_branch_path.py` tracks the Aoki-Maeda-Namba seventh-order algebraic root while both background curvature and an anti-correlated relative source evolve.

Matter-era proxy assumptions:

- `H^2 ~ a^-3`;
- `delta_rel ~ a^p`;
- `source_g = -s`, `source_f = +s`;
- `s ~ H^2 delta_rel`.

Tests are in `tests/test_cosmic_branch_path.py`.

A local TDD run gave `2 passed` after the implementation was added.

## Case A

Parameters:

`beta2=-3`, `beta3=3`, `m_g^2=m_f^2`.

The early matter-era root near

`mu ~= 0.3964`

can be followed continuously through the adiabatic proxy down to the late nonlinear root near

`mu ~= 0.6989`.

This reproduces the qualitative Case-A path described by Aoki-Maeda-Namba.

### Critical interpretation

This is **not** the desired global cosmology.

The paper explicitly distinguishes the late linear/homothetic branch `mu_infinity=0` from nonlinear/non-homothetic branches. For Case A, the stable nonlinear asymptote is

`mu_infinity = 0.698872` at `Lambda_g=0`.

In the static analysis, this non-homothetic branch gives large departures from GR beyond the Vainshtein radius and an inhomogeneous large-scale spacetime. The authors state that because the observed Universe is homogeneous on large scales, the Stueckelberg variables should ultimately reach the **linear bigravity phase** as the Universe expands.

Therefore:

`CASE_A_CONTINUOUS_ROOT = MATHEMATICALLY_REAL`

but

`CASE_A_MU~0.7_AS_GLOBAL_LATE_UNIVERSE = NOT_ACCEPTABLE_AS_TARGET`.

It may still be useful as a *local nonlinear patch* around structures, provided it can be matched to `mu -> 0` asymptotically.

## Case B

Parameters:

`beta2=-1`, `beta3=0.5`, `m_g^2=m_f^2`.

The early stable matter-era root is near

`mu ~= 1.095`.

The only stable late branch at `Lambda_g=0` is the linear branch `mu_infinity=0`.

Aoki-Maeda-Namba find no stable **adiabatic** `w=0` solution connecting the early branch to the late linear branch. Our proxy root tracker likewise loses nearby-root continuity around the transition region, with the failure occurring around `H^2/m^2` of order `10^-2` for the chosen normalization.

The paper emphasizes that for `w<1/3` the desired transition may be faster than a Hubble time, invalidating the adiabatic approximation. A full nonlinear time-dependent calculation is required.

Thus:

`CASE_B_ADIABATIC_TRANSITION = FAIL`

but

`CASE_B_FULL_NONADIABATIC_TRANSITION = UNRESOLVED`.

## Literature follow-up check

A targeted search through later primary literature did not reveal a 2016–2026 paper that completes this exact two-separately-coupled-matter, fully nonlinear time-dependent transition through `H~m_eff` and then follows structure formation to late times.

This statement is deliberately limited: absence from the search is not a theorem that no such work exists. But the 2015 transition problem remains the operative unresolved reference in the material found.

## Scientific consequence for JANUS-R

The main theoretical bottleneck is now precise:

> A viable JANUS-R cannot simply remain on the Case-A nonlinear branch everywhere. It needs an early nonlinear GR-like phase, a late globally homogeneous near-linear phase, and—if a Janus-like signal is to survive—localized nonlinear relative-mode regions associated with structures such as voids.

This suggests a two-scale architecture:

1. **global background:** asymptotically homogeneous, near `mu=0`;
2. **localized structures:** potentially nonlinear `mu=O(1)` patches, if regular matching exists.

The next gate is therefore the static/local matching problem rather than additional homogeneous root scans.

## Fail criterion

JANUS-R should be strongly downgraded if no regular solution can match

`mu ~ O(1)` in a Janus-like structure

to

`mu -> 0` on the homogeneous exterior,

without a ghost/gradient instability or a singular gradient layer.
