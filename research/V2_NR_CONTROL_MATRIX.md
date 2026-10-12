# V2 numerical-relativity control matrix

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `MANDATORY_BEFORE_PHYSICS_INTERPRETATION`

## Purpose

The pinned `bim-solver` standard-3+1 implementation is useful for the first short-time wall gate, but the authors explicitly reported limited long-time evolution, origin regularization/lapse-ratio noise and outer-boundary problems in their original one-fluid simulations.

Therefore a failed twin-wall evolution is **not automatically a physical failure of JANUS-R**. It must be classified against controls run with the same executable, grid, gauge and numerical method.

## Control A — untouched upstream one-fluid baseline

Compile and run the pinned upstream source without any JANUS-R changes.

Use one of the published one-fluid initial-data families or an equivalent regular rest-dust profile.

Record:

- maximum evolution time reached;
- Hamiltonian/momentum/bimetric-constraint norms;
- minimum/maximum lapse ratio;
- center regularity errors;
- outer-boundary reflection/error onset;
- causal type / null-cone diagnostics if available.

This establishes the numerical floor of the historical STD code.

## Control B — patched code with exactly zero f matter

Apply the complete twin-fluid source patch, but set

`pfFD=pfFS=pfFtau=0`

at every grid point.

Requirements:

1. initial metric/matter state equals Control A;
2. new f-fluid RHS remains identically zero up to round-off;
3. metric and g-fluid trajectories agree with Control A to the tolerance expected from source-code ordering;
4. lapse ratio agrees with Control A because all new `Delta W2[f]` terms vanish exactly.

**Hard fail:** any systematic difference from A before the upstream numerical error floor is reached.

A B mismatch is a patch/regression failure, not new physics.

## Control C — sector-dual f-only regression

Construct the dual of a simple g-only rest-dust setup:

- matter moved to the f sector;
- `g <-> f` metric variables;
- `kappa_g <-> kappa_f`;
- interaction coefficients reversed according to the Hassan-Rosen sector duality (`beta_n <-> beta_{4-n}`);
- separation sign transformed consistently.

This run does not need to reproduce Control A variable-by-variable in the same coordinate gauge. It must reproduce the dual constraint/source identities and the corresponding transformed observables.

Purpose: catch asymmetric implementation mistakes that the zero-f test cannot see.

## Experiment D — reference twin wall

Only after A-C pass:

- central positive f overdensity;
- positive g compensation shell / wall proxy;
- both rest fluids initially time symmetric;
- constraint-solved conformal factors;
- positive same-oriented lapse ratio from the exact initial lapse gate.

This is the first actual JANUS-R wall experiment.

## Required comparison logic

A numerical pathology in D counts against JANUS-R only if at least one of the following is true:

1. it occurs substantially earlier than the same numerical pathology in A/B at matched resolution;
2. its location tracks the physical compensation/transition wall rather than the known center or outer boundary;
3. it converges toward a finite physical time/radius under grid refinement;
4. it is preceded by a physical diagnostic crossing such as `W -> 0`, metric determinant loss, square-root/causal incompatibility, or constraint blow-up localized to the wall;
5. the same pathology survives migration to the better-posed BSSN/cBSSN formulation.

Conversely, a failure that shifts with the numerical boundary, finite-difference order or known upstream center problem is **not** a physical no-go.

## Minimal refinement matrix

For each A/B/D run use at least three radial spacings with the same physical domain, e.g.

`dr`, `dr/2`, `dr/4`.

Compare constraint norms at common physical radii/times before any failure.

The first goal is not a production cosmological simulation. It is to establish whether the twin compensation wall has a short-time regular development distinguishable from the numerical error floor.

## Promotion criterion to BSSN

Move the wall experiment to the upstream BSSN/cBSSN implementation if:

- A and B pass;
- D survives long enough to show a localized wall response;
- STD evolution then terminates because of the same origin/boundary/gauge limitations already present in A/B.

Do **not** spend time extending the historical STD code to long times when the better-posed formulation already exists.

## Scientific interpretation

This matrix prevents two opposite errors:

- falsely rejecting JANUS-R because an old numerical scheme fails generically;
- falsely accepting JANUS-R because a short noisy trajectory merely exists.

A physical wall verdict requires controlled differential behavior relative to A/B and convergence with resolution.
