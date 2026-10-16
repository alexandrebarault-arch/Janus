# Gate 2B — latest restart checkpoint

Date: 2026-10-16
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **Gate 2B OPEN; homothetic six-field action is controlled; non-homothetic time-dependent linear oracle is the active hard block.**

Read first after interruption:

1. `research/NONHOMOTHETIC_LINEAR_BRIDGE_AUDIT.md`;
2. `research/AOKI_COMPACT_METRIC_SCHUR_AUDIT.md`;
3. `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`;
4. `research/GATE2B_CHECKPOINT.md`.

## 1. Closed results — do not redo

Unless contradictory evidence appears, the following are closed at audit level:

- De Felice/Hassan-Rosen scalar action reconstruction;
- time-dependent BD canonicalization;
- Case-C `NG3` and all three Eq. (85) principal modes;
- Candidate-C dust+dust principal gravity branch;
- exact-dust late six-dimensional scalar phase space;
- proof that four late adiabatic density conditions leave two helicity-0 matching data free;
- exact non-homothetic spherical Stückelberg temporal relation;
- finite weak-metric Candidate-C folds;
- homogeneous kinetic-sign warning near fold 1;
- compact-support homothetic Aoki `K_S,c_S^2` oracle;
- compact weak Einstein-Hilbert + HR action with four metric potentials Schur-eliminated;
- finite-mass homothetic static control.

## 2. Candidate-C fold warning retained

Regular nonlinear pair:

- fold 1: `a_1 ~= 0.0301646`, `z_1 ~= 32.151`, `mu_1 ~= -0.768883`;
- fold 2: `a_2 ~= 0.0491246`, `z_2 ~= 19.356`, `mu_2 ~= -0.67015`.

Independent homogeneous kinetic-sign zero:

`a_K ~= 0.030136993`, `z_K ~= 32.18181`, `mu_K ~= -0.76624`.

The near-coincidence is a strong warning, **not** yet a no-go theorem.

## 3. Homothetic six-field action oracle — GREEN

The compact-support action retains

`(pi, phi_g, psi_g, phi_f, psi_f)`

or equivalently the six-field Stückelberg representation before the final scalar projection.

After the four weak metric amplitudes are eliminated, the small-`m^2/H^2` control reproduces the Aoki nonlinear kinetic and gradient coefficients at about the `0.2%` level at the committed compact resolution.

A finite-mass static root is also recovered at about the `0.22%` level.

Thus the homothetic action is no longer the blocker.

## 4. New native non-homothetic background layer

Added:

- `numerics/nonhomothetic_compact_background.py`;
- `tests/test_nonhomothetic_compact_background.py`.

For the two natural conformal charts,

`a'_g = a H`,
`a''_g = a(H^2+H')`,

and, with `b=a xi` and `d eta_f/d eta_g=c`,

`db/d eta_f = b H`,
`d2b/d eta_f2 = b(H^2+H'/c)`.

Targeted reconstructed verification: `3 passed`.

## 5. De Felice ↔ Stückelberg bridge — GREEN

Added:

- `numerics/nonhomothetic_linear_stueckelberg_bridge.py`;
- `tests/test_nonhomothetic_linear_stueckelberg_bridge.py`.

In g-flat gauge,

`E_f = -2 L`,

`psi_f + k^2 E_f/6 = - n H_f T`.

Therefore

`T = - [1/(n H_f)](psi_f+k^2 E_f/6)`.

The bridge also pins the induced f lapse/shift and the pure-Stückelberg Eq. (72) matter variable.

Fresh reconstructed verification after the principal-map extension: `5 passed`.

## 6. Principal non-homothetic pi map — derived independently

An independent reconstruction of the committed exact-dust Candidate-C local DAE was used to recover the gravity eigenvector and then `(T,L)` through the bridge above.

The high-k ratio obeys

`[(T/L)/(-lambda)] -> a^2/c`.

Representative values at `k=3200`:

- `a=0.3`: extracted real `0.1094746`, target `a^2/c=0.1094563`;
- `a=0.5`: extracted real `0.2668165`, target `0.2667849`;
- `a=0.7`: extracted real `0.5033082`, target `0.5032418`.

Hence the principal map is

`delta eta = -(1/(c a^2)) partial_eta pi`,

`delta r = +(1/a^2) partial_r pi`.

It reduces to Aoki when `c -> 1`.

**Important:** this is only the principal/high-frequency map.  Finite-H subleading terms must come from the time-dependent constrained reduction.

## 7. Failed non-homothetic shortcuts — do not repeat

The following have now been explicitly rejected:

- reusing the homothetic `c=1` pi map unchanged;
- reading the Candidate-C speed from a frozen local WKB/Schur system;
- subtracting a reference with `H=0` but unchanged matter/interactions — that reference is off-shell;
- treating one-profile matter amplitudes as if they were ordinary static auxiliaries;
- interpreting a raw local Stückelberg 2x2 symbol before the full constraint reduction.

The corrected principal `1/c` factor by itself does **not** recover the finite-H De Felice speed.  This is expected once the missing `Kdot,Cdot` structure is recognized.

## 8. Time-dependent quadratic reducer restored — GREEN

The generic reducer previously living only on `research/v2-flrw` has been ported to the active branch:

- `numerics/time_dependent_quadratic_reduction.py`;
- `tests/test_time_dependent_quadratic_reduction.py`.

It retains:

- `Cdot` when eliminating a kinetic-null coordinate;
- `Kdot` and `Cdot` in the Euler-Lagrange matrices;
- the `Rdot` term in the De Felice Eq. (72) map.

Fresh reconstructed verification: `4 passed`.

This is the same structural repair that was decisive in DF5e.5.

## 9. Current active calculation

Construct the **local non-homothetic quadratic action before the final scalar reduction** on one strict on-shell Candidate-C dust trajectory,

`L2 = 1/2 qdot^T K qdot + qdot^T C q + 1/2 q^T Q q`.

Then:

1. eliminate only genuine algebraic metric constraints;
2. differentiate the resulting `K,C,Q` along the same on-shell background;
3. perform the time-dependent null/BD reduction with `Cdot` retained;
4. construct the full Euler-Lagrange matrices including `Kdot` and `Cdot`;
5. take `mu -> 0` and require the gravity pair to converge to the independent Candidate-C target

`c_s^2 ~= 0.692071477288` at `a=0.5`.

This oracle must be GREEN before any fold interpretation.

## 10. After the linear oracle

Only after the same native action passes the De Felice `mu -> 0` oracle:

1. promote it to finite nonlinear `mu` on the early regular branch;
2. evaluate the fully constrained kinetic and gradient operators toward `a_1`;
3. test whether the homogeneous kinetic zero survives;
4. integrate a fold-crossing trajectory only if the kinetic/constraint system remains regular;
5. derive `(Y3,Y3_N)` from that trajectory;
6. rerun the late exact-dust transfer;
7. add visible radiation only after the dust path survives.

## 11. Verification limitation

The latest small modules have targeted RED/GREEN verification in reconstructed workspaces.  The De Felice/Stückelberg convergence table is from an independent reconstruction of the committed exact-dust equations.  GitHub Actions remain disabled and the full repository has not been executed in one clean worktree.

`GATE_2B = OPEN`.
