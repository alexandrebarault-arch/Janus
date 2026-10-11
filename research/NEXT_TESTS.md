# Next tests after V1

Date: 2026-10-11

The V1 audit is complete enough that further progress should not consist of adding more qualitative variants. The next phase must be computational and falsification-driven.

## Gate 1 — Full two-matter FLRW background

Implement the finite/healthy Hassan-Rosen cosmological branch with both separately coupled matter densities retained.

Required outputs:

- `a_g(t)`, `a_f(t)`, lapse ratio and metric ratio `xi(t)`;
- effective spin-2 mass and mixing angle as functions of redshift;
- no lapse singularity;
- no Higuchi ghost;
- positive kinetic eigenvalues;
- acceptable radiation/matter eras;
- self-acceleration test with `beta_0=0`.

**Fail condition:** no continuous healthy branch from radiation domination to today in any reasonable parameter region.

## Gate 2 — Linear transfer functions for both sectors

Derive/implement the coupled scalar perturbation system with

- visible baryons/CDM/radiation;
- twin-sector matter;
- both metric scalar potentials;
- finite spin-2 mass/mixing;
- scale dependence.

Compute transfer functions

`T_gg(k,z)`, `T_gf(k,z)`, `T_fg(k,z)`, `T_ff(k,z)`

for density, velocity and Weyl/lensing observables.

**Fail condition:** required relative mode is unstable, excessively large in CMB/LSS, or too weak to have any measurable late-time role.

## Gate 3 — Nonlinear branch continuity

Use the Aoki-Maeda-Namba seventh-order scalar equation as the first nonlinear diagnostic, then replace the adiabatic algebraic treatment with dynamical evolution through `H ~ m_eff`.

Scan at least:

- finite healthy interaction parameters;
- visible underdensity / twin overdensity ratios;
- realistic background densities;
- redshift evolution from early GR-like regime to late bimetric regime.

Track:

- real roots;
- branch mergers;
- kinetic signs;
- sound speeds;
- `d mu/dt` regularity;
- onset and exit of screening.

**Fail condition:** every parameter region producing a meaningful Janus-like relative mode crosses a singular/unstable branch.

## Gate 4 — Spherical void solver

Solve a compensated visible void plus possible twin overdensity on an FLRW background.

Outputs:

- `delta_g(r,z)`, `delta_f(r,z)`;
- visible peculiar velocity profile;
- `Psi_g(r,z)`, `Phi_g(r,z)`;
- Weyl potential;
- projected CMB/galaxy lensing convergence;
- compensation-wall evolution.

Compare to matched ΛCDM mocks.

**Fail condition:** the only stable solutions give either negligible deviations or order-unity profiles already incompatible with current void data.

## Gate 5 — Joint lensing + dynamics likelihood

The model's key signature is not negative lensing. It is a scale-dependent mismatch between slow-matter dynamics and photon lensing.

Fit jointly to:

1. DESI-Legacy/Planck void lensing (`A_kappa` and radial profile);
2. DESI RSD/full-shape growth;
3. `E_G` lensing-vs-velocity measurements;
4. BAO/SNe background;
5. CMB temperature/polarization/lensing once transfer functions are complete.

**Pass requirement:** improvement or at least competitive fit without parameter fine-tuning that collapses JANUS-R back to effectively GR+ΛCDM.

## Gate 6 — Model-selection penalty

If the model survives, compute at minimum

- chi-square / log likelihood;
- AIC;
- BIC;
- ideally Bayesian evidence.

A model that only reproduces ΛCDM after adding multiple unconstrained twin-sector parameters is not a scientific improvement.

## Gate 7 — Distinctive prediction

Before calling JANUS-R a successful continuation, require at least one prediction not inserted by hand, such as:

- a specific scale/redshift dependence of `E_G`;
- a fixed relation between void velocity and lensing profiles;
- a characteristic transition around the spin-2 Compton/Vainshtein scale;
- a measurable twin-sector-induced feature in cosmic-web statistics.

The prediction must be capable of being wrong.

## Priority order

1. full two-matter healthy FLRW solver;
2. coupled linear perturbations;
3. nonlinear relative-mode branch scan;
4. void solver;
5. joint data fit.

Do **not** spend more time polishing the exact `+G/-G` law, negative-mass interpretation or negative-lensing claim unless new mathematics changes the no-go results already recorded.
