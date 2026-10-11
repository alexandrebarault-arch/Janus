# Scientific State

Last updated: 2026-10-11

## Executive status

### JANUS-EXACT

**Status:** `NOT_CLOSED`

The published Janus formulation is not presently accepted here as a fully specified general relativistic bimetric theory. The central issue is not that two metrics or cross-sector repulsion are impossible. It is that the general interaction structure is not fully defined in a way from which all field equations and conservation laws follow uniquely.

### JANUS-R Late

**Status:** `ACTIVE_MAIN_BRANCH`

Current best continuation:

- two Lorentzian metrics `g` and `f`;
- two positive-energy matter sectors;
- ghost-free Hassan-Rosen type interaction potential;
- ordinary baryons + conventional CDM retained in the visible `g` sector for the main branch;
- no explicit cosmological constant term in the visible sector (`beta_0 = 0`) while testing self-acceleration;
- local/galactic deviations must be hidden by nonlinear Vainshtein screening;
- any Janus-like cross-sector effect must emerge outside the screened regime and must be derived, not imposed.

The next decisive target is the metric/lensing response in and around large cosmic voids.

## Established conclusions from the audit

### 1. Constrained variation in the 2015 Janus derivation is insufficient to derive two independent equations

If an action `S[g_+, g_-]` is varied subject to

`delta g_- = - delta g_+`,

then

`delta S = (E_+ - E_-) delta g_+`.

The variational condition therefore enforces only a relation between the two Euler-Lagrange tensors, not independently `E_+ = 0` and `E_- = 0` without an additional assumption.

**Consequence:** the two published field equations can be sufficient to satisfy the constrained variation while not being uniquely derived by it.

### 2. Janus 2024 improves the architecture but still leaves the general interaction incompletely specified

The 2024 action introduces interaction Lagrangian terms, but their complete field dependence/general relativistic form is not supplied sufficiently to reconstruct a unique closed nonlinear theory in all regimes.

**Status:** `OPEN_DEFECT`.

### 3. Exact Newtonian sign matrix is singular

The idealized Janus interaction matrix

```
J = [[ 1, -1],
     [-1,  1]]
```

has

`det(J) = 0`

and eigenvalues `0` and `2`.

This is a structural clue: an exact equal-magnitude attraction/repulsion rule is difficult to realize with two independent canonical metric sectors.

### 4. Cross-sector repulsion itself is not impossible

Ghost-free bimetric theories with two matter sectors can generate an effective repulsive cross interaction in some regimes through the coexistence/mixing of massless and massive spin-2 modes.

Therefore the binary statement "bimetric cross-sector repulsion is impossible" is rejected.

### 5. Fundamental negative energy is not currently required

The research branch no longer assumes that the second sector must have a fundamentally negative Hamiltonian density. Repulsion can arise effectively while both matter sectors have positive energy.

This is currently preferred because it avoids introducing a negative kinetic-energy degree of freedom unless observation or consistency later requires it.

## Rejected / downgraded branches

### A. Minimal `beta_1` self-accelerating model

**Reason:** attractive background expansion, but scalar perturbation instability at early times/small scales.

**Verdict:** `REJECTED_AS_FINAL_MODEL`.

### B. `beta_1-beta_4` infinite branch as primary candidate

Initially considered promising because of gradient-stability properties. Later downgraded because the evolution of the metric ratio conflicts with the healthy/Higuchi requirement on the relevant branch.

**Verdict:** `REJECTED_AS_PRIMARY_BRANCH`.

### C. Constant-mass unified model where the same twin sector is all dark matter and also causes large-scale Janus repulsion

A constant effective graviton mass cannot naturally make the same second sector behave as ordinary attractive dark matter on the required scales while remaining Janus-like repulsive over tens-to-hundreds of Mpc without severe tension between regimes.

**Verdict:** `REJECTED_UNIFIED_CONSTANT_MASS`.

### D. Naive cosmological extrapolation of the linear Yukawa repulsive regime

Choosing a tiny graviton mass solely to extend the linear repulsive Yukawa regime to ~100 Mpc ignores local constraints on the same unscreened linear solution.

**Verdict:** `REJECTED_NAIVE_LINEAR_EXTRAPOLATION`.

**Correction:** any viable large-scale effect must incorporate nonlinear screening (Vainshtein or equivalent) and cannot be inferred by extending the flat-background point-source solution everywhere.

## Active branches

### JANUS-R Late — MAIN

Question:

Can a ghost-free two-metric, two-positive-energy-sector theory be indistinguishable from GR in screened high-density regions, while producing a distinctive late-time large-scale cross-sector response around voids/cosmic-web structures and potentially contributing to cosmic acceleration without an explicit Lambda term?

### JANUS-R2 — HIGH RISK

Allow effective graviton mass/mixing parameters to evolve through the cosmological metric ratio `xi(t)`.

Purpose: test whether early-time and late-time interaction regimes can differ strongly enough to mimic multiple cosmological roles without adding an arbitrary new scalar field.

Status: `EXPLORATORY`; must pass ghost/gradient/lapse/singularity tests.

### JANUS-R3 — EXPLORATORY

Use 3+ metrics in a modern ghost-free multimetric interaction graph to investigate whether an approximate or exact Janus `+G/-G` sign pattern can emerge without pathological kinetic mixing.

Status: `EXPLORATORY_LOW_PRIORITY`.

## Immediate scientific gate

Derive or numerically solve the visible metric response to an extended `f`-sector overdensity associated with a large void environment, including the screened-to-unscreened transition.

Required outputs:

1. `Psi_g(r)` — nonrelativistic potential.
2. `Phi_g(r)` — spatial curvature potential.
3. Weyl/lensing potential `(Phi_g + Psi_g)/2`.
4. Deflection angle `alpha(R)`.
5. Projected convergence `kappa(R)`.
6. Sign and amplitude comparison with a matched Lambda-CDM void profile.

No claim of "negative lensing" is allowed until these quantities are derived.
