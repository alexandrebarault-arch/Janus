# V2 conclusion on JANUS

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `LITERAL_JANUS_REJECTED_AS_ESTABLISHED_THEORY__BIMETRIC_SEGREGATION_IDEA_REMAINS_OPEN`

## Executive verdict

If forced to decide today whether Jean-Pierre Petit's **published Janus cosmological model, literally as formulated**, should be regarded as a correct physical theory of the Universe, the answer of this research program is:

**NO.**

More precisely:

- it is not demonstrated;
- its general nonlinear field theory is not closed;
- several of its characteristic physical claims do not survive reconstruction inside a modern ghost-free bimetric framework;
- no complete global confrontation to the decisive cosmological observables has been produced by Janus itself.

However, this research also rejects the opposite caricature that Petit's core intuition is meaningless. A weaker descendant idea remains scientifically interesting:

> two positive-energy matter sectors associated with two interacting metrics can exhibit a relative gravitational mode, scale-dependent cross-sector repulsion, nonlinear screening, and spatial segregation.

That descendant is **not literal Janus**. In this repository it is called `JANUS-R`.

---

## 1. Fatal issue for literal Janus: the nonlinear theory is not closed

Petit, Margnat & Zejli (EPJC 2024) write an action containing interaction terms / interaction tensors between the two sectors, but do not provide their exact general nonlinear form.

The paper explicitly states, in its strong-field discussion, that one is not obliged to provide the exact source/interaction tensor and that its exact form might be supplied in the future.

That is not enough for a fundamental field theory.

Bianchi identities impose conservation-type differential constraints on a correctly defined source tensor; they do not uniquely manufacture the missing tensor or its constitutive dynamics.

Therefore:

`JANUS_2024_GENERAL_NONLINEAR_THEORY = NOT_CLOSED`.

This conclusion does not depend on community acceptance or citation counts. It follows from the mathematical specification of the model itself.

---

## 2. The 2015 constrained-variation derivation is insufficient

For an action `S[g_plus,g_minus]`, imposing

`delta g_minus = - delta g_plus`

before variation gives only

`delta S = (E_plus - E_minus) delta g_plus`.

Stationarity therefore enforces a relation between the two Euler-Lagrange tensors, not independently

`E_plus = 0` and `E_minus = 0`

without an additional assumption.

Thus the two Janus field equations may be sufficient to satisfy the constrained condition, but they are not uniquely derived from it.

This weakens the claimed Lagrangian foundation of the older formulation.

---

## 3. Exact universal `+G/-G` is not recovered in the healthy two-metric reconstruction

The ideal Janus Newtonian sign matrix

```
[[+1,-1],
 [-1,+1]]
```

is singular.

In the reconstructed ghost-free Hassan-Rosen two-metric model, the linear massless+massive spin-2 propagator instead gives, in the maximally modified short-Compton regime for the symmetric case,

- enhanced self-attraction;
- cross-sector repulsion asymptoting to only about `-G/3` in the normalization used here.

The exact equal-strength Janus law is therefore not reproduced.

Adding more healthy Einstein-Hilbert metric sectors does not trivially restore the exact law in the same linear architecture.

Verdict:

`UNIVERSAL_EXACT_PLUS_G_MINUS_G = NOT_SUPPORTED`.

---

## 4. Petit's negative-lensing claim does not survive JANUS-R

A positive-energy `f`-sector source can repel a slow `g`-sector test particle in the linear ghost-free bimetric solution.

However the photon/Weyl response is different because the helicity-0 trace coupling does not act on a traceless photon stress tensor in the same way.

The direct calculation recorded in `research/CROSS_SECTOR_LENSING.md` gives a cross-sector deflection proportional to

`-[1 - u K_1(u)]`,

which approaches zero at short distance and ordinary convergent lensing at long distance; it does not reverse sign.

Therefore an isolated positive-energy twin mass is **not** a negative/divergent lens in this healthy realization.

The distinctive surviving signal is instead a possible **dynamics-vs-lensing mismatch**.

Verdict:

`LITERAL_NEGATIVE_LENSING_PREDICTION = NOT_RECOVERED`.

---

## 5. Fundamental negative mass is unnecessary and theoretically costly

JANUS-R obtains effective cross-sector repulsion with positive kinetic signs and positive-energy matter sectors.

Therefore fundamental negative energy is not required to realize the part of Petit's idea that is actually interesting gravitationally.

Introducing a wrong-sign fundamental kinetic sector would create a serious ghost/energy-boundedness problem unless a complete constraint structure removes it.

No such necessity has emerged from this research.

Verdict:

`FUNDAMENTAL_NEGATIVE_MASS = UNNECESSARY_AND_UNPROVEN`.

---

## 6. What survived: real two-sector segregation physics

Several nontrivial pieces of the intuition survive.

### 6.1 Cross-sector repulsion exists in a healthy theory class

Ghost-free Hassan-Rosen bigravity with separate matter sectors can produce an effectively repulsive cross-sector force in part of parameter/scale space.

### 6.2 A relative/segregation mode exists

The two-sector system contains a relative massive spin-2 mode in addition to the common GR-like mode.

In the simplest symmetric unscreened control limit this relative mode grows faster than the common matter mode, although only modestly at linear level.

### 6.3 Nonlinear relative sourcing is real

Aoki-Maeda-Namba's nonlinear scalar equation contains a weighted source difference between the two sectors. A visible underdensity paired with a twin overdensity reinforces the relative nonlinear source rather than cancelling it.

### 6.4 Regular separated initial data exist

The repository now contains independent implementations/checks of the two-sector spherical Hamiltonian constraint problem, including `numerics/two_sector_initial_constraints.py`.

For exchange-symmetric bi-Minkowski interactions and positive matter only:

- central `f` Gaussian core;
- surrounding `g` Gaussian shell;

regular positive solutions exist.

Newest independent check:

- TDD: RED `ModuleNotFoundError` -> GREEN `3 passed in 0.51s`;
- moderate positive-matter core/shell scan: `100/100` converged;
- deliberately strong scan: `47/48` converged.

Thus spatial separation itself is not forbidden by the nonlinear constraints.

### 6.5 The initial secondary/lapse branch has a finite healthy basin

Separate repository work reconstructed the time-symmetric two-matter lapse ratio and scanned the initial wall. The reference wall has a finite positive same-oriented lapse branch, and a broad but not unlimited parameter/amplitude basin survives. Outside that basin the lapse relation develops forbidden sign/zero behavior inside the compensation wall.

Therefore a nontrivial separated two-sector initial slice can pass both Hamiltonian and initial lapse/secondary-constraint gates.

Verdict:

`TWO_POSITIVE_SECTOR_SEGREGATED_INITIAL_DATA = PASS_IN_PRINCIPLE`.

---

## 7. Why JANUS-R is still not a theory of the real Universe

The surviving descendant has a severe stability/observability tension.

Exploratory healthy-branch scans found that pushing linear stability to earlier redshifts tends to suppress visible mixing and drive the model toward the GR-decoupling regime.

Strong linear effects that could rapidly create large segregation are correspondingly easier to observe and harder to reconcile with early cosmology/LSS.

Nonlinear cosmological Vainshtein behavior remains a possible escape: published work shows that nonlinear scalar dynamics can restore a GR-like stable early regime for suitable parameters.

But the decisive problem is now the **transition wall** between a localized relative nonlinear region and the homogeneous exterior.

Known facts:

- the algebraic approximation develops branch endpoints near the wall in Janus-like void sign configurations;
- this signals breakdown of the small-gradient approximation, not automatically a physical singularity;
- a known static Ricci-flat Vainshtein background studied by Aoki-Mizuno suffers ghost/gradient instability, though this is not a theorem for a cosmological non-Ricci-flat two-fluid void;
- Brizuela-de Cesare-Soler Oficial provide the formal perturbation machinery for arbitrary spherical bimetric backgrounds, but a regular two-fluid cosmological wall background must first be evolved.

The branch now contains a detailed patch specification and runbook for extending the public `nubirel/bim-solver` standard-3+1 spherical evolution code to an independent `f`-sector Valencia dust fluid, including the f-matter contribution to the secondary/lapse relation and control/regression tooling.

The remaining blocker is practical executable evidence: the pinned upstream GPL code has not been materialized/compiled in the current sandbox.

Therefore:

`DYNAMICALLY_GENERATED_STABLE_COSMOLOGICAL_SEGREGATION = OPEN`.

---

## 8. Observational status

Literal Janus has not demonstrated a single global fit simultaneously reproducing the precision observables that a modern cosmological model must face, including at least CMB temperature/polarization/lensing, BAO, supernovae, growth/RSD and large-scale lensing.

Meanwhile current void lensing and lensing-vs-dynamics measurements are broadly compatible with GR/Lambda-CDM, leaving little room for an order-unity late gravitational anomaly unless it is screened or has a specially structured observable signature.

Ordinary ghost-free bimetric cosmology itself is not dead: recent analyses including DESI DR2 find viable backgrounds and modest improvements in some data combinations. This establishes the viability of the mathematical skeleton, not of Janus or the two-matter segregation scenario.

---

## 9. Scores after V2

These are scientific assessment scores, not statistical probabilities.

| Claim / program | Score /20 | V2 conclusion |
|---|---:|---|
| Petit's MHD/plasma work as physics | 16 | strong, separate issue |
| Literal published Janus as a complete fundamental theory | **5** | incomplete; key field structure unspecified |
| Fundamental negative-mass sector | **4** | unneeded and unestablished |
| Exact universal `+G/-G` law | **5** | not recovered in healthy reconstruction |
| Negative gravitational lensing as claimed by Janus | **4** | not recovered by healthy positive-energy two-sector model |
| Core idea: two sectors can gravitationally segregate | **15** | genuinely viable research idea |
| Hassan-Rosen JANUS-R mathematical skeleton | **16** | well-defined ghost-free framework |
| JANUS-R as actual cosmology today | **9** | major stability/formation/observational gates remain |
| Value of one targeted numerical two-fluid wall experiment | **13** | worthwhile R&D, not validation of Janus |

---

## 10. Final decision

### On Jean-Pierre Petit's JANUS

**Reject as an established physical theory.**

If forced into a binary choice `true / false` based on the evidence and mathematics available today, this research chooses:

**LITERAL JANUS: MOST LIKELY FALSE OR AT LEAST FUNDAMENTALLY INCOMPLETE.**

The strongest reason is not sociology or lack of acceptance. It is that the model has not specified the complete nonlinear interaction law needed to define the theory, while several characteristic consequences fail to emerge when the idea is rebuilt in a modern ghost-free bimetric framework.

### On Petit's underlying intuition

**Do not reject it wholesale.**

The scientifically durable residue is:

> A second gravitational sector and a relative massive spin-2 degree of freedom can in principle create environment-dependent segregation while local gravity is screened.

That statement is mathematically meaningful and falsifiable.

But if a future simulation demonstrates a stable version of it, the resulting theory should be described as a **new bimetric/twin-matter model inspired in part by Janus**, not as a proof that Petit's published Janus equations were correct.

### Research stopping rule

There is only one remaining calculation with enough information value to justify a V3:

1. materialize and build the pinned public `bim-solver` revision;
2. reproduce the untouched one-fluid baseline;
3. apply the prepared independent f-fluid source/lapse patch;
4. require exact/numerical zero-f regression and sector-dual controls;
5. evolve the regular segregated two-sector wall at several resolutions/Courant factors;
6. if it survives, test all seven gravitational perturbative degrees of freedom through the resolved wall.

If the wall cannot evolve regularly and stably in any physically interesting parameter region, the remaining JANUS-R segregation program should be stopped.

If it does survive, the next step is an observational void velocity/lensing prediction — **not** a return to negative mass or exact `+G/-G`.
