# V2 Gate A0 — two-matter spherical initial data

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `INITIAL_DATA_EXISTENCE_PASS__DYNAMICAL_WALL_STILL_OPEN`

## Question

Before modifying a full bimetric evolution code, ask a weaker but necessary question:

> Can the time-symmetric spherical constraint equations admit a regular configuration with an f-sector central concentration and a g-sector compensating shell?

A failure here would kill the proposed Janus-like wall before dynamics are even considered.

## Published equations used

Kocic, Torsello, Högås & Mörtsell (arXiv:1904.08617) impose, at the time-symmetric initial hypersurface,

- vanishing extrinsic curvatures in both sectors;
- `p = 0`;
- conformally-flat spatial metrics
  `gamma_g = psi_g^4 delta_ij`, `gamma_f = psi_f^4 delta_ij`.

Their Eqs. (2.20a,b) are

`4 psi_g Delta psi_g + kappa_g m2 V_g(psi_g,psi_f) + kappa_g D_g = 0`,

`4 psi_f Delta psi_f + kappa_f m2 V_f(psi_g,psi_f) = 0`,

where the polynomial interactions are the beta combinations printed in the paper.

The full Hamiltonian constraint Eq. (2.11b) already contains an f-sector matter term `rho_f^m`; the authors subsequently set it to zero because their collapse example couples matter only to g. For JANUS-R we therefore use the direct separately-coupled extension

`4 psi_f Delta psi_f + kappa_f m2 V_f + kappa_f D_f = 0`.

This is not a new interaction ansatz; it is the standard second-sector matter source restored in the Hamiltonian constraint.

## Boundary conditions

For the `R_infinity = 1` asymptotically bi-Minkowski branch, the paper gives

`beta0 + 3 beta1 + 3 beta2 + beta3 = 0`,

`beta1 + 3 beta2 + 3 beta3 + beta4 = 0`.

Regular spherical symmetry requires

`psi_g'(0) = psi_f'(0) = 0`.

The numerical outer boundary uses

`psi_g(r_max) = psi_f(r_max) = 1`.

## Diagnostic profiles

The first JANUS-R wall proxy deliberately uses only positive physical densities:

- f matter: central Gaussian concentration;
- g matter: external Gaussian shell.

This is **not yet a cosmological void**. In asymptotically-vacuum data there is no homogeneous matter background relative to which the central g region can be called a negative density perturbation. The configuration tests only whether a two-sector centre/wall geometry can satisfy the exact nonlinear Hamiltonian constraints without a metric zero or singularity.

Reference numerical point:

- `beta1 = 1`, `beta2 = -0.2`, `beta3 = 0`;
- asymptotic completion `beta0 = -2.4`, `beta4 = -0.4`;
- `m2 = 0.02`;
- `kappa_g = kappa_f = 1`;
- f central profile `amp=0.04`, `sigma=2`;
- g shell `amp=0.025`, `radius=5`, `sigma=1`;
- `r_max=25`.

## Result

The boundary-value solver converges to a regular positive solution:

- `psi_g` in approximately `[1, 1.04845]`;
- `psi_f` in approximately `[1, 1.04572]`;
- central derivatives satisfy the imposed Neumann conditions;
- outer conformal factors return to 1;
- maximum normalized collocation residual `~7.23e-7`.

A crude amplitude stress scan multiplying both matter profiles by

`0.1, 0.3, 1, 3, 10, 30, 100, 300`

also converged from a flat initial guess for this parameter point. At the largest multiplier the conformal factors remain positive, reaching values of order `4.7` before returning to 1 at the outer boundary.

This stress scan is a numerical existence observation, not a stability theorem and not evidence that such high-amplitude data are cosmologically meaningful.

## Verification

A local test-driven cycle was executed because GitHub Actions are disabled:

1. RED: tests written before the module; pytest failed during collection with `ModuleNotFoundError: No module named 'two_matter_initial_data'`.
2. First implementation: 2 tests passed and the sourced case failed only because an external finite-difference residual estimator was stricter/noisier than the BVP collocation error.
3. Residual reporting was corrected to use SciPy `solve_bvp`'s native normalized collocation residual.
4. GREEN: `3 passed in 0.43s`.

This is module-level local verification, not a full-branch test run.

## Scientific interpretation

`INITIAL_CONSTRAINT_EXISTENCE = PASS`.

The previously identified algebraic AMN branch endpoint does **not** imply that no regular two-sector centre/wall initial geometry can exist. A full radial-gradient constraint solution can be perfectly regular.

However, this does not yet answer the decisive question. A true cosmological void is dynamical and should asymptote to FLRW rather than vacuum. The next gate is therefore not another Lane-Emden scan.

## Next gate

Use the public `nubirel/bim-solver` 3+1/cBSSN infrastructure from Kocic/Torsello/Högås/Mörtsell as the reference implementation for radial dynamics.

The source code already evolves a Valencia perfect fluid in g, while the f-sector matter projections are explicitly set to zero. The shortest physically faithful extension is:

1. add a second independent Valencia dust state coupled to f;
2. populate `rho_f`, `j_f`, `J_f11`, `J_f22` from that state instead of zero;
3. construct initial data approximating a compensated relative perturbation;
4. evolve through the wall and monitor both Hamiltonian/momentum constraints and the bimetric lapse relation;
5. only then apply the general spherical perturbative stability machinery to the resulting background.

`GATE_A_FULL_DYNAMIC_WALL = OPEN`.
