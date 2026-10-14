# Candidate C — full Aoki polynomial instantaneous-proxy audit

Date: 2026-10-14
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **EARLY NONLINEAR ALGEBRAIC BRANCH DOES NOT ADIABATICALLY JOIN `mu=0` IN THE INSTANTANEOUS PROXY**

## Purpose

The earlier `candidate_c_aoki_proxy.py` used only the `H >> m_eff` early-root formulas of Aoki, Maeda & Namba (2015).  That established that Candidate-C couplings are not excluded from the class that admits a stable screened early branch, but it did not test how that branch behaves as `H/m_eff` falls through order unity.

The next discriminating test is therefore the complete algebraic Aoki equation, Eqs. (5.8)-(5.11), retaining the `m_g^2`, `m_f^2`, `H^2` and matter-source pieces.

This remains an **instantaneous non-homothetic proxy**, not an exact Candidate-C nonlinear solution.  Aoki's derivation does not contain Candidate C's fully time-dependent `xi(a)` / lapse structure as a dynamical transition system.

## Numerical conditioning improvement

The historical repository helper `aoki_scalar_polynomial.py` reconstructs degree-seven coefficients by Vandermonde interpolation of the equation values.  That is adequate for quoted-root regressions, but branch separation itself is the observable here.

The new helper

- `numerics/candidate_c_aoki_full_proxy.py`

constructs every polynomial term algebraically with `numpy.polynomial.Polynomial`, then solves the resulting coefficients directly.  No coefficient fitting/interpolation is used.

The instantaneous split of the independently known Candidate-C effective mass is

`m_g^2 / m_f^2 = alpha^2 xi^2`,

so

`m_g^2 = m_eff^2 alpha^2 xi^2 / (1 + alpha^2 xi^2)`,

`m_f^2 = m_eff^2 / (1 + alpha^2 xi^2)`.

The instantaneous effective equation-of-state input is reconstructed from the strict dust benchmark deceleration,

`w_eff = (2 q - 1)/3`.

## Source-free branch tracking

Start on the admissible negative branch continuously connected to the stable early Aoki root.  Track it by nearest-root continuation on a dense logarithmic grid from `a=0.01` to `a=1`.

Representative values are:

| a | tracked mu | nearest-root separation |
|---:|---:|---:|
| ~0.0200 | -0.88444 | 0.1102 |
| ~0.05785 | -0.74292 | 0.2102 |
| ~0.10174 | -0.66686 | 0.2133 |
| ~0.12001 | -0.65184 | 0.2037 |
| ~0.20002 | -0.58077 | 0.2166 |
| ~0.50090 | -0.45360 | 0.2269 |
| 1.0 | -0.43030 | 0.2223 |

Across the full sampled interval:

- the tracked root remains real;
- the minimum root separation is about `0.0652`, occurring at the earliest endpoint;
- the normalized polynomial slope never approaches zero;
- at the independently determined late linear principal-stability boundary `a ~= 0.10165`, the branch is still `mu ~= -0.667`.

Therefore there is no evidence that the stable early nonlinear algebraic branch is approaching or merging smoothly into the late linear `mu=0` solution.

## Small source sensitivity

As a limited robustness probe only, set both Aoki matter-source terms to

`source_g = source_f = epsilon H^2`

with `epsilon = 1e-4, 1e-3, 1e-2`.

Near `a ~= 0.10165` the tracked values remain approximately

- `epsilon=1e-4`: `mu ~= -0.66696`;
- `epsilon=1e-3`: `mu ~= -0.66695`;
- `epsilon=1e-2`: `mu ~= -0.66685`;

with nearest-root separation still about `0.213`.

This equal-source prescription is not a physical nonlinear perturbation history; it is only a sensitivity test.  It shows that the branch gap is not a zero-source numerical accident.

## Interpretation

Within this instantaneous projection, the screened early branch and the late linear branch are distinct algebraic branches.  The early branch stays order-unity away from `mu=0` even after the exact-dust linear principal scalar becomes healthy.

This sharpens the transition problem:

- an **adiabatic algebraic continuation** of the early Aoki branch does not deliver the late linear state;
- a branch-changing / non-adiabatic dynamical episode is therefore required if Candidate C is to connect the screened early regime to the healthy late linear regime;
- such an episode is exactly where the omitted scalar-graviton oscillation degree of freedom can matter, and exactly where the two late helicity-0 matching data must be generated.

This is consistent with Aoki et al.'s warning that the `H ~ m_eff` transition may invalidate the adiabatic approximation and require a numerical dynamical treatment.  It does **not** prove that a regular non-homothetic transition exists.

## Scientific ruling

- `EARLY_SCREENED_ALGEBRAIC_BRANCH_EXISTS_IN_PROXY = YES`.
- `EARLY_BRANCH_ADIABATICALLY_APPROACHES_MU_ZERO = NO` in the instantaneous full-polynomial proxy.
- `SMALL_EQUAL_SOURCE_PROBE_CLOSES_BRANCH_GAP = NO`.
- `NONADIABATIC_DYNAMICAL_TRANSITION_REQUIRED_IF_CANDIDATE_C_SURVIVES = YES`.
- `REGULAR_NONHOMOTHETIC_TRANSITION_DERIVED = NO`.

## Regression

`tests/test_candidate_c_aoki_full_proxy.py` pins:

1. representative exact-polynomial roots;
2. reality and finite separation of the tracked early branch;
3. failure to approach `mu=0` at the late principal-stability boundary;
4. robustness against small equal-source sensitivity probes.

Targeted reconstructed-workspace result on 2026-10-14: `3 passed`.  This is not a full-repository test-suite claim.

## Next step

Do not tune `(Y3,Y3_N)` and do not force an algebraic root switch.

The next calculation must supply dynamics: derive the weak-metric / nonlinear-Stueckelberg action or equations on the actual non-homothetic Candidate-C background, retaining the scalar-graviton time derivative.  The first acceptance test is whether a regular trajectory can cross from the early screened branch to a principal-stable late state without a kinetic zero, singular lapse/coordinate map, or divergent `d mu/dN`.
