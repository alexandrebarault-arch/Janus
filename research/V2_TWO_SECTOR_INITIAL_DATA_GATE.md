# V2 two-sector spherical initial-data gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `INITIAL_DATA_EXISTENCE_PASS__EVOLUTION_STABILITY_OPEN`

## Question

Before attempting a full dynamical two-fluid bimetric simulation, ask the cheapest decisive question:

> Can regular time-symmetric spherical initial data exist for a spatially segregated configuration consisting of a central `f`-sector concentration and a surrounding `g`-sector shell, with both matter densities positive and an asymptotically bi-Minkowski exterior?

This is a necessary but not sufficient condition for a Janus-like environment.

## Published equations used

Kocic, Torsello, Högås & Mörtsell, *Spherical dust collapse in bimetric relativity: Bimetric polytropes* (2019/2020), derive the full spherical bimetric Hamiltonian constraints. Their Eq. (2.11b) explicitly contains an `f`-sector matter density term, although the paper later sets it to zero because they choose matter coupled only to `g`.

For time symmetry, conformally flat spatial metrics and `p=0`, their Eqs. (2.20) become generalized Lane-Emden equations for conformal factors `psi_g` and `psi_f`.

The repository module

`numerics/two_sector_initial_constraints.py`

implements those equations and restores the `f`-matter contribution in the second Hamiltonian constraint.

No negative fundamental matter density is introduced.

## Interaction used for the regression gate

A simple exchange-symmetric asymptotically bi-Minkowski point was chosen:

- `beta1 = beta3 = 1`,
- `beta2 = 0`,
- `beta0 = beta4 = -4`,
- equal gravitational couplings,
- positive interaction mass squared.

The values of `beta0` and `beta4` satisfy the two `R_infinity=1` Minkowski conditions from Eq. (2.21).

This point is a numerical existence test, not a claim that these beta parameters are observationally viable.

## Matter profiles

The segregated diagnostic uses only positive matter densities:

- `f` sector: central Gaussian core;
- `g` sector: positive Gaussian shell at finite radius.

This is deliberately more physical than modeling a cosmological void by assigning a negative absolute matter density. A real void is an underdensity relative to a cosmological background, not negative matter.

## TDD verification

Before implementation, the new tests failed during collection with

`ModuleNotFoundError: No module named 'numerics.two_sector_initial_constraints'`.

After implementing the solver, the exact same local tests gave:

`3 passed in 0.51s`.

The tests verify:

1. vacuum gives the exact bi-Minkowski solution `psi_g = psi_f = 1`;
2. a central `f` core plus `g` shell produces a regular positive solution with small constraint residual;
3. for the exchange-symmetric theory, swapping the two matter profiles swaps the two metric solutions.

GitHub Actions are disabled; this is a local/manual module-level verification, not CI.

## Exploratory scan

A moderate grid was scanned over

- `mass2 = 0.005, 0.02, 0.05, 0.1`,
- `g` shell amplitudes `0.02 ... 0.4`,
- `f` core amplitudes `0.02 ... 0.4`.

Result:

`100 / 100` configurations converged.

All returned positive conformal factors and the largest first-order ODE residual was approximately machine precision (`~6.7e-17`) in the evaluated solution representation.

A deliberately much stronger grid using amplitudes up to `5` and `mass2` up to `1` gave

`47 / 48` converged configurations.

The one non-convergent point was

`mass2=1, g_shell_amplitude=5, f_core_amplitude=2`.

This strong-grid failure is not interpreted as a physical singularity because solver failure can be branch/initial-guess dependent. It only shows that regularity is not automatic at arbitrarily strong sources.

## Verdict

`SPATIALLY_SEGREGATED_POSITIVE_MATTER_INITIAL_DATA = PASS_IN_PRINCIPLE`.

Therefore the Hamiltonian constraints do **not** provide a no-go against a Janus-like separated environment.

However:

`DYNAMICAL_GENERATION = NOT_PROVEN`

`LONG_TIME_EVOLUTION = NOT_PROVEN`

`TRANSITION_WALL_STABILITY = NOT_PROVEN`

`COSMOLOGICAL_MATCHING = NOT_PROVEN`.

## Importance for the global Janus verdict

This gate removes one possible fatal objection: a separated two-sector configuration is not forbidden merely because the nonlinear bimetric constraints cannot be solved.

It does **not** rescue Petit's published Janus theory. The calculation is performed in ghost-free Hassan-Rosen bigravity with positive matter in both sectors, not with fundamental negative mass and not with Petit's exact `+G/-G` law.

The decisive remaining issue is whether a regular segregated initial state can evolve through the radial/cosmological transition layer without developing ghost, gradient, lapse or branch instabilities, and whether such a state is dynamically generated from acceptable cosmological initial conditions.
