# Gate 2B — inverse-chart native-field transport and compact HR quadratic audit

**Date:** 2026-10-18  
**Branch:** `research/gate2b-nonhomothetic-transfer`  
**Scientific status:** GEOMETRIC TRANSPORT/QUADRATURE CONTROL PASSES; PHYSICAL FINITE-MU SCALAR ACTION AND FOLD CROSSING REMAIN OPEN.

## Research question and previous obstruction

The previous finite-mu local native Hassan–Rosen (HR) interaction was computed first as an exact 14x14 quadratic jet for eight native metric fields and six local Stückelberg/chart derivatives, then promoted to a 22x22 *local jet* by including derivatives of four f-native metric perturbations sampled at displaced coordinates. The crucial issue was to map those eight sampling-derivative slots back to **coherent fields on the same spacetime chart**, before integrating or eliminating constraints.

We now supply an explicit **22x16 kinematic projection and compact radial interaction integral**. This is NOT the complete 16-dimensional `(Y1,Y2,L,T,p_g,p_f)` pre-metric EH+dust augmented Hessian (whose 16 coordinates have different meanings).

## Exact background coordinate differential

At fixed common coordinates `(t,r)`, the prescribed f-native chart is

```text
T0(t,r) = t + sigma(t) r^2 / 2
R0(t,r) = [1+mu(t)] r

J = d(T0,R0)/d(t,r)
  = [[1 + sigma_dot r^2/2,  sigma r],
     [mu_dot r,              1+mu   ]]

D = det(J) = (1+sigma_dot r^2/2)(1+mu) - sigma*mu_dot*r^2 > 0.
```

The names `sigma_r` and `sigma_dot` in the native-jet API mean the instantaneous background `sigma` and its supplied time derivative. The values must eventually come from one on-shell background trajectory; the kinematic gate does not enforce that differential relation.

For each f-native scalar metric component `q_i(T,R)`, evaluated in the common chart,

```text
q_t = T_t q_T + R_t q_R,
q_r = T_r q_T + R_r q_R,

q_T = ((1+mu) q_t - mu_dot*r*q_r)/D,
q_R = (-sigma*r*q_t + (1+sigma_dot*r^2/2)*q_r)/D.
```

This is an *exact* inverse Jacobian identity for the displayed background map, not a derivative expansion in `mu`.

## Compact radial ansatz and profile derivatives

For a fixed-radius common-chart control profile, let `q_i(t,r)=A_i(t)P_i(r)` and `q_t=A_i_dot P_i`, `q_r=A_i P_i'`. The support is `0 <= r < R` with

```text
F(r) = [1 - (r/R)^2]^4,
P_Phi = P_psi = F,
P_B = F'/k,
P_E = -2 [F''-F'/r]/k^2.
```

The derivation holds the *common-coordinate* support radius R and k fixed at a background instant; a moving native f-coordinate profile is handled by the inverse Jacobian, including the advection `-mu_dot*r A_i P_i'` in `q_T`.

At the regular center, `P_B(0)=P_E(0)=0`, `P'_B(0)=-8/(R^2 k)`, and the metric shear profile derivative is regular. During local verification the independent profile-derivative test exposed an omitted `1/k` in `P'_B`; the source was corrected before publication. This is a genuine witnessed RED-to-GREEN test, not tuning a physical coefficient.

## 22x16 pullback

Define a 16-component *trial action* argument

```text
x = (Phi_g,B_g,psi_g,E_g,
     Phi_f,B_f,psi_f,E_f,
     T,L,Tdot,Ldot,
     Phi_f_dot,B_f_dot,psi_f_dot,E_f_dot).
```

For each r, construct a 22x16 map `Q(r)`:

- first 14 rows: the previously validated regular radial metric/Stückelberg map;
- rows 14..17: four f-native `q_{i,T}` from the inverse Jacobian;
- rows 18..21: four f-native `q_{i,R}` from the same inverse Jacobian.

The four field `A_i_dot` slots are the temporal derivatives of `A_i`; they are NOT four new propagating degrees of freedom. In particular, the actual physical reduced phase-space dimension is NOT 16 simply because the *trial action* has 16 entries.

The local 22x22 HR matrix including the quadratic terms from field sampling is projected as

```text
H16(r) = Q(r)^T H22(r) Q(r),
g16(r) = Q(r)^T g22(r).
```

Integrate **before** any metric Schur or BD reduction:

```text
H_compact = 4*pi * integral_0^R r^2 H16(r) dr,
g_compact = 4*pi * integral_0^R r^2 g16(r) dr.
```

The native interaction density already includes `sqrt(-g)`. No extra FLRW volume measure is inserted.

## Reproducible artifacts

- `numerics/hr_native_sampling_compact.py`
- `tests/test_hr_native_sampling_compact.py`
- Prerequisites: `hr_native_stueckelberg_jet.py`, `hr_native_field_sampling.py`, `hr_compact_radial_interaction.py`.

Fresh targeted verification using locally reconstructed prerequisite modules from the committed implementation:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_native_sampling_compact.py
# 10 passed (2026-10-18)
```

Test controls:

1. independently reconstruct common-coordinate derivatives from the projected native derivatives for all four f fields;
2. finite-difference the radial profiles, including the odd-shift `1/k` normalization and regular center;
3. check nonzero native time advection for a changing `mu` even if the common amplitude is frozen;
4. verify the quadratic sampling Hessian against a separately applied Taylor substitution;
5. compare 16-point with 28-point radial Gauss–Legendre quadrature;
6. check beta0 does not couple to f/chart perturbations;
7. check identity-chart (`mu=sigma=mu_dot=sigma_dot=0`) recovery;
8. reject singular/invalid Jacobians and integration domains;
9. check beta4 f-only sector independence from g metric amplitudes;
10. check the pure HR sampling block quadratic in `(Phi_f_dot,B_f_dot,psi_f_dot,E_f_dot)` is identically zero.

At one off-shell diagnostic point `(N,a,n,alpha,k,mu)=(1,.92,1.13,.84,2.2,-.25)`, radius `R=.23`, the 16/28 point **maximum Hessian coefficient difference** was approximately `1.02e-12` in the implemented dimensionless conventions. A nonzero `f-rate x chart` interaction block has Frobenius norm approximately `1.78e-3`; the pure `f-rate x f-rate` HR block is zero. These numbers are numerical regression controls, **not observational predictions** or kinetic signs.

The test environment could not clone the GitHub worktree (DNS unavailable); GitHub Actions are disabled. A complete clean-repository suite has **not** been executed. The locally reconstructed prerequisites and targeted tests were actually run, but this is not equivalent to an independently verified fresh clone.

## Critical scientific limitations

- **Interaction-only, off-shell** control: EH gravity and both dust canonical matter phase pairs remain unassembled; no background tadpole cancellation or integration-by-parts audit is done here.
- **Trial spherical spatial support**, not a physical Aoki eigenfunction nor a Fourier transfer mode.
- **Frozen background instant:** these amplitudes must be embedded in a time-supported, on-shell path and the f-native profile effects followed coherently in time.
- The invertibility condition `D>0` holds for chosen controls; no global nonsingular Candidate-C trajectory is established.
- The 16x16 matrix cannot be directly diagonalized as a physical kinetic or gradient operator because the metric constraints and time-dependent BD-null reduction have not been performed.
- The beta4 local separation is a necessary control but the stronger global f-sector diffeomorphism/Noether Ward identity after full compact spacetime integration is still untested.
- The `mu=0` limit of this interaction gate alone is **not** the De Felice physical scalar spectrum; a homothetic interaction gate alone is **not** Aoki `K_S,c_S^2`.

## Next falsification gates — strict order

1. **Full action assembly:** construct coherent compact-support Einstein–Hilbert + HR + two-dust phase action with the same background chart, temporal profile and boundary terms. Keep both dust phase pairs dynamical.
2. **Metric constraints and BD direction:** eliminate only four metric auxiliaries, then perform the time-dependent null/BD canonicalization. Reject any artificial extra modes or negative kinetic eigenvalues.
3. **Mandatory independent limit A:** `mu -> 0` along the on-shell Candidate-C background must reproduce the already validated finite-H De Felice gravity principal scalar speed (and dust degrees).
4. **Mandatory independent limit B:** the homothetic nonlinear regime must recover the compact Aoki `K_S,c_S^2` coefficients for both stable and unstable roots, after constraints, from the SAME action.
5. **Only then** compute the constrained non-homothetic kinetic/gradient eigenvalues near fold 1 `a ≈ 0.0301646`; attempt a continuous crossing only if the full constraint/kinetic systems stay regular.
6. If that crossing survives, determine the unique late helicity-0 matching data and run late transfer. If it fails, record a negative Gate-2B verdict rather than fitting an arbitrary late lift.

**Current verdict: `GATE_2B = OPEN`. No defensible JANUS cosmological validation, full perturbation theory or fold-crossing conclusion yet.**
