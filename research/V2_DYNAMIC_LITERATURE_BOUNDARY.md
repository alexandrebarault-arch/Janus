# V2 — Dynamic literature boundary before the twin-wall run

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `NO_PUBLISHED_SUBSTITUTE_FOR_A1_RUN_FOUND`

## Question

Before spending effort on the executable twin-fluid wall experiment, does the modern literature already contain either:

1. a full nonlinear spherical Hassan-Rosen evolution with **two separately coupled matter sectors**, or
2. a theorem that already rules out the required dynamic wall?

A targeted 2021–2026 search found neither.

## What is established

### Kocic, Torsello, Högås & Mörtsell — spherical bimetric dust evolution

Their spherical dust-collapse work constructs bimetric initial data and performs short-time numerical evolution with the same public standard-3+1/BSSN solver architecture we are adapting.

The published one-matter-sector simulations show:

- genuinely nonbidiagonal dynamics;
- interwoven/oscillating null cones;
- short-term collapse qualitatively close to GR in the tested strong-field regime;
- no immediate numerical/physical instability in those particular runs.

This is evidence that the numerical architecture can evolve nontrivial spherical Hassan-Rosen backgrounds. It is **not** evidence that a twin-matter relative wall is stable.

### Brizuela, de Cesare & Soler Oficial (2024)

They provide a covariant perturbation formalism for the most general spherically symmetric bimetric background, including dynamical spacetimes, and track the seven physical gravitational degrees of freedom through axial/polar sectors.

This is the correct machinery for the perturbative stability gate **after** a genuine nonlinear twin-wall background exists.

It does not supply that background and therefore cannot replace Gate A1/A2.

## What is still missing in the literature found

No primary source found in the targeted search performs all of the following together:

- ghost-free Hassan-Rosen bimetric gravity;
- two positive-energy matter sectors separately/minimally coupled to their own metrics;
- a localized anti-correlated configuration (visible underdensity / twin overdensity or equivalent relative wall);
- full radial-gradient evolution through the wall;
- simultaneous monitoring of both matter conservations, both metric constraints, lapse orientation and separation mode;
- subsequent seven-DOF stability analysis of that dynamically generated wall.

Therefore the planned A1 experiment is not a duplicate of an already published calculation.

## Important non-result

Absence of a located paper is not a theorem of novelty. The statement above is deliberately limited to the targeted primary-literature search performed for this project.

Likewise, the existence of successful one-sector dust evolutions does not make the twin-wall likely to pass. The second matter sector enters precisely the relative mode and lapse/secondary-constraint structure that forms the scientific risk.

## Decision

`A1_DYNAMIC_TWIN_WALL_STILL_REQUIRED = YES`

`PUBLISHED_NO_GO_FOR_OUR_EXACT_WALL = NOT_FOUND`

`PUBLISHED_PROOF_OF_STABILITY_FOR_OUR_EXACT_WALL = NOT_FOUND`

The research therefore remains correctly staged:

1. executable zero-f regression;
2. sector-dual f-only control;
3. short twin-wall evolution;
4. resolution/Courant convergence;
5. only if the background survives, apply the general spherical perturbation formalism to the resolved wall.
