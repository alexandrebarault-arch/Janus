# Multimetric linear no-go for exact Janus strength

Date: 2026-10-11

Status: `DERIVED_CLASS_RESULT`

## Scope

Consider a linearization around a proportional Minkowski vacuum of a theory with:

1. `N` spin-2 fields with positive canonical Einstein-Hilbert kinetic terms;
2. ghost-free potential interactions, giving one massless spin-2 eigenmode plus `N-1` massive Fierz-Pauli spin-2 eigenmodes;
3. each matter sector minimally coupled to one original metric;
4. no exotic derivative/kinetic mixing in the matter coupling;
5. momenta below the strong-coupling cutoff and outside any nonlinear screened region.

This includes the standard linear regime of ghost-free bimetric and tree-type multimetric models.

## Mode decomposition

Let `c_{ia}` be the coupling of matter sector `i` to spin-2 mass eigenmode `a`, where `a=0` is the massless mode. Canonical diagonalization gives the completeness relation

`sum_a c_{ia} c_{ja} = delta_ij` (up to the common normalization convention).

For distinct sectors `i != j`,

`sum_{a>0} c_{ia} c_{ja} = - c_{i0} c_{j0}`.

## Photon / traceless probe

For a traceless probe such as a photon, massless and massive spin-2 modes have the same relevant tensor contraction. At momenta much larger than all massive-mode masses,

`A_lens(i,j) ~ c_i0 c_j0 + sum_{a>0} c_ia c_ja = 0`

for `i != j`.

Therefore cross-sector lensing vanishes in the ultraviolet linear limit rather than becoming negative.

## Slow nonrelativistic matter

For conserved nonrelativistic sources, a Fierz-Pauli massive spin-2 exchange has the standard `4/3` Newtonian enhancement relative to the massless spin-2 exchange because of the helicity-0 trace coupling.

Hence, at momenta much larger than all spin-2 masses,

`A_dyn(i,j) ~ c_i0 c_j0 + (4/3) sum_{a>0} c_ia c_ja`

and therefore for `i != j`,

`A_dyn(i,j) = -(1/3) c_i0 c_j0`.

Normalized to the long-range massless cross attraction, the universal asymptote is

`Q_cross,UV = -1/3`.

## Consequence

Increasing the number of ordinary ghost-free metric sectors does **not** by itself recover the exact Janus rule

`same sector: +G`,

`opposite sector: -G`

at all scales.

The high-momentum linear limit remains `-G/3` for slow cross-sector dynamics and zero for cross-sector photon lensing under the assumptions above.

## Relation to older N >= 3 constructions

Older multimetric constructions can algebraically realize exact `+G/-G` Newtonian sign matrices, but they use interaction/kinetic structures outside the canonical modern ghost-free pairwise-potential class. The modern multimetric literature shows that interaction cycles and nonstandard structures can reintroduce Boulware-Deser-like degrees of freedom unless strong structural restrictions are imposed.

This explains why the exact Janus sign law is easy to write as a Newtonian matrix but difficult to embed in a healthy relativistic spin-2 theory.

## What is not ruled out

This result does not exclude:

- transient stronger repulsion at intermediate scales from a nontrivial massive-mode spectrum;
- nonlinear screened/unscreened branches whose effective force differs from the linear propagator result;
- nonminimal but demonstrably ghost-free matter couplings;
- genuinely multifield vielbein interactions with a different effective phenomenology;
- a theory outside the spin-2 potential-interaction framework.

But `JANUS-R3` can no longer be justified merely by the statement that `N >= 3` removes the `-1/3` limitation. It does not.

## Decision

Downgrade `JANUS-R3` from a likely route to exact Janus to `EXPLORATORY_ONLY`.

The main branch remains `JANUS-R Late`, where the target is not exact `-G` but a testable late-time relative-sector force and a characteristic dynamical/lensing mismatch.
