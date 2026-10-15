# Non-homothetic oscillating helicity-0 action — execution plan

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`
Status: NEXT HARD BLOCK

## Goal

Derive a spatially dependent quadratic action/equation for the oscillating helicity-0 mode around the nonlinear non-homothetic Candidate-C branch, with the weak metric constraints retained long enough to decide whether a regular nonadiabatic trajectory can cross the fold interval.

The calculation must determine a genuine kinetic operator and gradient operator.  The homogeneous velocity signature in `NONHOMOTHETIC_OSCILLATION_KINETIC_AUDIT.md` is only a warning/conditioning oracle and is not sufficient by itself.

## Non-negotiable oracles

### Oracle A — homothetic Aoki limit

For `c -> 1`, `xi -> K=const`, `H >> m_eff` and a constant-`w` background, the reduced oscillation system must reproduce Aoki-Maeda-Namba Eqs. (4.50)-(4.56):

- one scalar Stückelberg field `pi` after the constraints;
- `K_S` with the correct sign and normalization up to one global positive action convention;
- `c_S^2`;
- both stable and unstable nonlinear-root controls;
- the separate `mu=0` linear branch.

A local 2x2 principal-symbol determinant before constraint reduction is not an acceptable substitute; it contains the Stückelberg constraint/gauge direction and produced spurious complex characteristics in scratch work.

### Oracle B — Candidate-C linear limit

For `mu -> 0` on the actual non-homothetic Candidate-C dust background, the reduced scalar principal mode must agree with the already validated De Felice/Hassan-Rosen linear principal gravity branch.

This prevents an Aoki-specific nonlinear derivation from silently losing the known linear helicity-0 normalization.

## Required variables

Keep, before reduction,

`(phi_g, psi_g, phi_f, psi_f, delta_eta, delta_r)`

or an exactly equivalent gauge-invariant six-field set.

The nonlinear adiabatic background keeps `mu` finite and the temporal Stückelberg map fixed by the exact non-homothetic relation.  Oscillation amplitudes are weak, but `mu` itself is not expanded.

## Step 1 — homothetic six-field quadratic control

Construct the quadratic action around one homothetic nonlinear root using:

- exact spherical HR pullback already implemented;
- weak metric HR layer already calibrated against Aoki Eqs. (98)-(101);
- Einstein-Hilbert weak scalar operators;
- no matter perturbations, only the background equation of state.

RED acceptance: the unreduced action/constraint system does not yet produce Aoki `K_S,c_S^2`.

GREEN acceptance: after eliminating the four weak metric auxiliaries/constraints and the nondynamical Stückelberg combination, the one-field action reproduces Aoki Eqs. (4.55)-(4.56) on at least three independent nonlinear roots, including opposite kinetic/gradient signs.

## Step 2 — finite `m_eff/H` homothetic control

Do not immediately specialize to `H >> m_eff`.  Retain finite weak metric response and verify that the static/adiabatic zero-frequency sector remains consistent with the already recovered full Aoki `C_H^2+C_m^2=0` roots.

This ties the dynamic reduction to the finite-mass fold machinery already calibrated in `NONHOMOTHETIC_WEAK_METRIC_TRANSITION_AUDIT.md`.

## Step 3 — non-homothetic background promotion

Replace the homothetic constants by the actual on-shell functions

`xi(N), c(N), H(N), xi_N, c_N`

from `candidate_c_dust_background.py`.

No `K -> xi` instantaneous substitution into final Aoki formulas is allowed.  The time-dependent coefficients must enter before the constraints are solved.

## Step 4 — linear `mu -> 0` oracle

Take the new non-homothetic quadratic system to `mu -> 0` and compare its high-k scalar branch with the validated De Felice Candidate-C principal action/speed.

Failure here means the nonlinear weak-metric/Stückelberg normalization is wrong; do not inspect the folds until this is GREEN.

## Step 5 — first-fold kinetic test

Evaluate the fully reduced kinetic eigenvalue along the regular early nonlinear branch approaching

`a_1 ~= 0.0301646`, `mu_1 ~= -0.768883`.

Compare with the independent homogeneous HR-only signature zero

`a_K ~= 0.030136993`.

Important: an algebraic fold does not force a kinetic zero in general.  A homothetic dust counterexample with `B2=3`, `B3=2/3` has a double root `mu=-3/4` but `K_S=375/128>0`.  Therefore any finite-mass Candidate-C kinetic zero must emerge from the actual reduced dynamics, not be assumed from branch topology.

## Step 6 — transition verdict

Only if the full kinetic operator remains finite and nonzero should a dynamical integration through the fold interval be attempted.

Acceptance requires one continuous solution with:

- real HR square root;
- `mu>-1`;
- nonsingular metric/Stückelberg constraint matrix;
- positive kinetic coefficient;
- positive relevant gradient coefficient;
- finite canonical momentum and `dmu/dN`;
- continuous approach to the validated late linear helicity-0 pair.

If such a trajectory exists, project it onto `(Y3,Y3_N)` on a principal-stable late surface and re-run the exact-dust late transfer.  If no such trajectory exists under the two independent oracles above, Candidate C fails Gate 2B rather than being rescued by a chosen late lift.

## Current evidence to retain

- finite weak-metric regular pair absent for approximately `32.15 > z > 19.36`;
- near-singular branch remains close to `mu=-1`, physical regularity unresolved;
- homogeneous nonlinear-branch kinetic oracle calibrated against Aoki dust roots;
- Candidate-C HR-only kinetic signature zero is numerically near fold 1 but is not yet a full kinetic no-go;
- full gradient coefficient has not yet been derived.
