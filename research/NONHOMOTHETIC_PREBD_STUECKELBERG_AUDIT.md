# Candidate C — pre-BD Stueckelberg finite-H bridge audit

Date: 2026-10-16
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **FINITE-H LINEAR STUECKELBERG REPRESENTATION CLOSED; PRE-METRIC NONLINEAR INSERTION POINT IDENTIFIED; FINITE-MU NATIVE ACTION STILL OPEN**

## Purpose

The homothetic compact action already reproduces the Aoki nonlinear helicity-0 oracle.  The remaining issue was how to represent the actual non-homothetic Candidate-C scalar at finite H without inventing a subleading one-field `pi` map.

The correct construction is to change variables **before** the time-dependent BD/null reduction.

## 1. Exact pre-BD bridge

In the De Felice Eq. (72) basis, before the BD scalar is eliminated, use state order

`(Y1,Y2,Y3,Z,p_g,p_f)`.

Introduce relative Stueckelberg variables

`(Y1,Y2,L,T,p_g,p_f)`

through

`Y3 = -2 L`,

`Z = - n H_f T + k^2 L/3`.

Equivalently,

`T = - [1/(n H_f)] (Z + k^2 Y3/6)`.

On the strict Candidate-C dust background,

`n H_f = H_omega/a`,

and its g-cosmic-time derivative is

`d(n H_f)/dt_g = (H_omega' - H_omega H)/a^2`.

This rate formula was independently checked by differentiating along the on-shell branch at `a=0.3,0.5,0.7`, with agreement at approximately `1e-10...1e-11`.

## 2. Why T is the correct algebraic coordinate

The validated pre-BD action has a kinetic-null `Zdot` direction.

Under the full time-dependent state/rate transformation

`q_old = R q_new`,

`qdot_old = Rdot q_new + R qdot_new`,

the `Zdot` kinetic null maps exactly to the `Tdot` direction.

Therefore the temporal relative displacement `T` is the time-dependent algebraic/BD coordinate, while `L` remains the physical spatial helicity-0 coordinate.

This avoids constructing an ad hoc finite-H one-field `pi` map.

Implementation:

- `numerics/prebd_stueckelberg_transform.py`;
- `tests/test_prebd_stueckelberg_transform.py`;
- `tests/test_prebd_stueckelberg_el_equivalence.py`.

A synthetic time-dependent control verifies that, after null-coordinate integration by parts and elimination, the **Euler-Lagrange matrices** agree under the residual `Y3=-2L` coordinate change.  Raw reduced Hessians need not agree because the two routes may differ by total time derivatives.

## 3. Direct map before metric constraints

The same bridge can be written directly in the original g-flat reduced variables:

`psi_f = k^2 L/3 - n H_f T`,

`E_f = -2 L`,

`q_g = Y1`,

`q_f = Y2 - T`.

The time derivatives are

`psi_f_dot = k^2 Ldot/3 - n H_f Tdot - [d(nH_f)/dt] T`,

`E_f_dot = -2 Ldot`,

`q_g_dot = Y1dot`,

`q_f_dot = Y2dot - Tdot`.

The direct map agrees with the exact composition

`Eq. (72) transform -> pre-BD (Y3,Z) to (L,T)`

to machine precision in the regression.

## 4. Candidate-C finite-H linear oracle

A new reducer applies the time-dependent bridge on the strict on-shell Candidate-C dust trajectory, canonicalizes `Tdot`, eliminates `T`, and then uses the existing exact-dust DAE machinery.

Implementation:

- `numerics/candidate_c_linear_stueckelberg_action.py`;
- `tests/test_candidate_c_linear_stueckelberg_action.py`.

At `a=0.5`, `k=0.2 h/Mpc`, an independent reconstructed calculation gives approximately

- Stueckelberg-basis gravity `c_s^2 = 0.69092747`;
- original De Felice-basis gravity `c_s^2 = 0.69092766`.

The difference is about `2e-7` in absolute `c_s^2` and decreases with the trajectory-derivative step.  Both lie within the already committed finite-k/double-precision tolerance against the independent asymptotic target

`c_s^2 = 0.692071477288...`.

The purpose of this result is basis equivalence at finite H; it is not a claim that the finite-k double-precision point itself equals the asymptotic target to high precision.

## 5. Dust matter feedback is not negligible

The two pressureless sectors cannot be removed as static auxiliaries from the helicity-0 mode.

At `a=0.5`, `k=0.2 h/Mpc`:

- full Stueckelberg + two-dust system: `c_s^2 ~= 0.69093`;
- artificial clamp of both dust coordinates/rates, retaining only `(L,Ldot)`: `c_s^2 ~= 0.49432`.

The difference is approximately `0.197`, i.e. order unity for the propagation problem.

The same qualitative mismatch is present over the tested `k` values.

Regression:

- `tests/test_candidate_c_stueckelberg_matter_feedback.py`.

**Ruling:** the finite-mu nonlinear action must retain the two dust phase pairs through the time-dependent constrained reduction.  Treating matter as an instantaneous Schur auxiliary is invalid.

## 6. Pre-metric augmented insertion point

The old exact dust Hessian before metric elimination has order

`(psi_f,E_f,q_g,q_f, rates[4], Phi_g,Phi_f,B_g,B_f,p_g,p_f)`.

A 14x16 transformation now maps it to

- six states `(Y1,Y2,L,T,p_g,p_f)`;
- their six rates (`p_gdot,p_fdot` remain structural zeros);
- four metric auxiliaries `(Phi_g,Phi_f,B_g,B_f)`.

The metric variables are left unchanged.

Transforming the **augmented** Hessian first and only then Schur-eliminating the four metric auxiliaries was independently checked against the historical route

`metric Schur -> Eq.72 -> pre-BD Stueckelberg transform`.

Representative relative infinity-norm discrepancies are

| a | k [h/Mpc] | relative discrepancy |
|---:|---:|---:|
| 0.3 | 0.1 | `4.2e-13` |
| 0.5 | 0.2 | `5.3e-11` |
| 0.7 | 0.1 | `5.8e-13` |

The four-dimensional metric auxiliary block has rank 4 at all three points.  Its condition number is finite (roughly `1.8e4`, `5.9e4`, `1.6e5` respectively).

Implementation/regression:

- `direct_flat_augmented_transform(...)` in `numerics/prebd_stueckelberg_transform.py`;
- `tests/test_candidate_c_stueckelberg_augmented_action.py`.

## 7. Scientific consequence

The finite-H linear bridge is no longer the conceptual blocker.

There is now a well-defined pre-constraint interface at which the nonlinear interaction can be introduced **without changing the already validated Einstein-Hilbert or dust sectors**:

1. retain `(Y1,Y2,L,T,p_g,p_f)` plus four metric auxiliaries;
2. keep the validated EH and dust phase terms;
3. replace/promote only the Hassan-Rosen interaction block from the linear `mu=0` form to the exact finite-`mu` non-homothetic pullback;
4. eliminate the metric auxiliaries;
5. perform the time-dependent `Tdot` null/BD reduction;
6. retain both dust phase pairs;
7. evaluate the full kinetic/gradient operator.

This is the minimal architecture capable of connecting the homothetic Aoki nonlinear oracle to the non-homothetic De Felice linear oracle.

## 8. What is not yet proved

This audit does **not** yet establish an independent finite-`mu` Candidate-C dynamical action.

In particular:

- the exact nonlinear HR pullback has not yet been inserted into the full dust + EH augmented action in the same variable convention;
- the finite-`mu` metric constraint matrix has not yet been evolved dynamically;
- the full kinetic/gradient coefficient at fold 1 is still unknown;
- the near-coincidence between the homogeneous kinetic-sign zero and fold 1 remains a warning, not a no-go theorem.

`GATE_2B = OPEN`.

## 9. Immediate next calculation

Construct a finite-`mu` HR Hessian/correction in the validated augmented interface and require two limits before using it at the fold:

1. `mu -> 0`: recover the augmented linear HR block and the finite-H Candidate-C De Felice/Stueckelberg spectrum;
2. homothetic early-time limit: recover the already GREEN compact Aoki nonlinear `K_S,c_S^2` oracle.

Only a construction that passes both limits may be evaluated along the regular Candidate-C nonlinear branch toward `a_1 ~= 0.0301646`.

## Verification limitation

The new algebraic map and synthetic EL controls were executed directly.  The Candidate-C spectral and pre-metric equivalence numbers were independently reproduced from the committed formulas in a reconstructed local scratch workspace.  GitHub Actions remain disabled and the full repository has not been run in one clean worktree.
