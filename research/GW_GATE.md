# Gravitational-wave gate for Candidate C

Date: 2026-10-11

Status: `NO_OBVIOUS_CURRENT_GW_EXCLUSION__NOT_A_FULL_WAVEFORM_LIKELIHOOD`

## Why this gate was checked now

Candidate C has a present relative lapse / auxiliary tensor-cone parameter

`ctilde_0 ~= 0.99042`, 

which is visibly different from unity. Because GW170817 constrains the speed of the observed gravitational-wave signal extremely tightly, this could have killed the candidate before a costly scalar-transfer calculation.

It does not, for the model architecture presently used.

## Important model distinction

Akrami et al. (2018) showed that **doubly coupled** bigravity, where the same visible matter sector couples to a composite metric built from both `g` and `f`, is forced by GW170817 either toward proportional backgrounds or toward a singly-coupled limit.

JANUS-R does **not** use that composite visible-matter coupling. Visible matter and detectors couple to `g`; the separate twin matter sector couples to `f`.

Therefore the Akrami et al. exclusion cannot simply be copied onto JANUS-R.

Reference:
https://arxiv.org/abs/1803.09726

## Candidate-C mass scale

From `numerics/flrw_two_matter.py`,

`m_eff,0/H0 ~= 42.31`.

For `H0=70 km/s/Mpc`,

`H0 ~= 2.27e-18 s^-1`,

and with `hbar = 6.582e-16 eV s`,

`hbar H0 ~= 1.49e-33 eV`.

Hence

`m_eff,0 c^2 ~= 6.3e-32 eV`.

This is roughly ten orders of magnitude below the usual LVK massive-graviton dispersion bounds of order `10^-22 eV` and far below even prospective LISA mass reach quoted in modern reviews.

Thus the ordinary dispersion bound on a massive graviton does not exclude Candidate C.

## Oscillation parameter

In the De-Felice/Narikawa tensor phenomenology, the frequency-dependent mixing contains a parameter schematically

`x = 2 omega^2 (ctilde-1) / mu^2`.

At `f=100 Hz`, Candidate C has

`omega/mu ~ 6e18`,

and therefore

`|x| ~ O(10^36)`

for `|ctilde-1|~10^-2`.

The bimetric oscillation literature shows that observable flavor oscillations are largest around `x~1` and are suppressed in both asymptotic limits `x<<1` and `x>>1`. In the enormous-`|x|` regime the propagation basis becomes nearly aligned with the metric/flavor basis, so a visible `g`-metric wave predominantly follows the luminal `g` tensor cone.

Reference review:
https://doi.org/10.1007/s41114-024-00054-9

Earlier waveform analysis:
https://doi.org/10.1103/PhysRevD.91.062007

## What this does and does not prove

This is enough to reject the simple claim

`ctilde_0 != 1 => Candidate C is immediately ruled out by GW170817`.

That claim is false for the present separate-sector/superlight-mass architecture.

It does **not** constitute a dedicated JANUS-R gravitational-wave likelihood. A complete test would propagate both tensor fields on the actual time-dependent Candidate-C background and compare the visible strain to LVK events.

## Decision

`GW_FATALITY_CHECK = PASS`

Candidate C remains worth testing in the scalar sector.

Do not confuse this result with the doubly-coupled-composite-metric model excluded by GW170817.
