# V2 nonlinear anti-correlated source gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `ALGEBRAIC_BRANCH_TOPOLOGY_DIAGNOSTIC__PHYSICAL_INTERPRETATION_CORRECTED`

## Purpose

The linear V2 scan exposes a stability–mixing tension: parameter regions that remain healthy to very early epochs tend toward the GR-decoupling regime, suppressing the visible massive-spin-2 response needed for a strong Janus-like signal.

A possible escape is nonlinear dynamics of the relative/Stueckelberg mode. The first diagnostic implemented here asks only:

> At fixed background curvature, does a chosen real scalar root remain connected when an anti-correlated two-matter source is increased?

This is a branch-topology test, **not** a time-dependent cosmology and not a direct bound on a density contrast.

## Implementation

- nonlinear scalar equation: `numerics/aoki_scalar_polynomial.py`
- fixed-background continuation: `numerics/nonlinear_source_continuation.py`
- tests: `tests/test_nonlinear_source_continuation.py`

The source is parameterized as

`source_g = -s`,

`source_f = +s`,

which has the sign structure of a visible-sector underdensity plus a twin-sector overdensity.

## Case A

For the Aoki–Maeda–Namba example

`beta2 = -3`, `beta3 = 3`, `m_g^2 = m_f^2 = 0.5`,

at the illustrative fixed value `H^2 = 0.01`, the nonlinear root near `mu ~= 0.692` remains continuously real in this diagnostic as `s` is increased at least to `s=5`.

Result:

`CASE_A_FIXED_H_ROOT_CONTINUITY = PASS_IN_ALGEBRAIC_DIAGNOSTIC`.

This proves only that a large source does not automatically destroy that particular algebraic nonlinear branch.

## Case B

For

`beta2 = -1`, `beta3 = 0.5`, `m_g^2 = m_f^2 = 0.5`,

starting from the late linear root `mu=0` at fixed `H^2=0.01`, the nearby-root tracker loses the connected algebraic branch near

`s ~= 0.4757`.

Result:

`CASE_B_FIXED_H_ROOT_CONTINUITY = ENDPOINT_AT_FINITE_DIMENSIONAL_SOURCE`.

### Correction to the earlier interpretation

The number `s ~= 0.4757` is **not** a realistic void-density threshold.

The source `s` has dimensions of curvature/mass squared. In a matter-era scaling one expects schematically

`s ~ H^2 delta_rel`.

At the illustrative `H^2=0.01`, interpreting `s=0.4757` as `H^2 delta` would correspond to a contrast of order `delta~48`, far outside the regime of a realistic cosmological void perturbation.

Therefore this fixed-H endpoint must **not** be used to claim that Case B fails for realistic void amplitudes.

The physically more relevant result comes from `numerics/cosmic_branch_path.py`, which evolves `H^2` and the relative source together. That diagnostic still finds that the Case-B adiabatic branch loses continuity around the transition `H^2/m^2 ~ 10^-2`, consistent with the qualitative conclusion of Aoki–Maeda–Namba for `w<1/3`.

## What survives from this gate

The useful conclusions are structural:

1. nonlinear scalar branches can remain real under large anti-correlated sources for selected parameters;
2. other parameter choices contain branch mergers/endpoints;
3. a dimensional source threshold at one fixed `H` cannot be interpreted directly as a cosmological density-contrast bound;
4. the relevant problem is the joint evolution of curvature, matter sources and branch identity through `H~m_eff`.

## Updated decision

`FIXED_H_NONLINEAR_BRANCH_EXISTENCE = PASS_FOR_SELECTED_PARAMETERS`

`FIXED_H_ENDPOINT_AS_VOID_BOUND = RETRACTED`

`GLOBAL_NONLINEAR_TO_LINEAR_COSMIC_TRANSITION = OPEN`

`LOCAL_STATIC_VOID_TRANSITION = SEPARATE_GATE`

The next conclusions must come from the cosmic-transition and static-void diagnostics, not from the raw number `s~=0.4757`.
