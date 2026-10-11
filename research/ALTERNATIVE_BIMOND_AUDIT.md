# Alternative branch audit — BIMOND

Date: 2026-10-11

Status: `REJECTED_AS_FUNDAMENTAL_REPLACEMENT__RETAINED_AS_NONLINEAR_SEGREGATION_INSPIRATION`

## Why BIMOND was audited

The principal weakness found in Hassan-Rosen JANUS-R is not the absence of cross-sector repulsion. It is the difficulty of generating a *large relative/twin density mode* from near-adiabatic initial conditions.

Mordehai Milgrom's Bimetric MOND (BIMOND) attacks precisely this problem. It contains two metrics and, in matter/twin-matter symmetric versions, predicts attraction within each sector and repulsion between sectors in the MOND regime.

References:

- Milgrom 2009, *Bimetric MOND gravity*, Phys. Rev. D 80, 123536, arXiv:0912.0790.
- Milgrom 2010, *Matter and twin matter in bimetric MOND*, MNRAS 405, 1129, arXiv:1001.4444.
- Milgrom 2010, *Cosmological fluctuation growth in bimetric MOND*, Phys. Rev. D 82, 043523, arXiv:1006.3809.

## The attractive feature

For symmetric matter/twin-matter backgrounds the nonrelativistic fluctuation equations split into:

- a **sum/common** system governed by Newtonian dynamics;
- a **difference/relative** system governed by MOND-like dynamics.

The difference mode is nonlinear even at small perturbation amplitude and experiences stronger effective gravity. Milgrom explicitly finds that this favors matter/twin-matter segregation and interleaving cosmic webs, with overdensities of one sector tending to occupy voids of the other.

This is exactly the dynamical capability missing from the simple linear Hassan-Rosen reference system, where the relative mode grows only mildly (`a^1.186...` in its maximal homothetic limit) and is not sourced at all from an exactly adiabatic common mode.

Therefore BIMOND provides a valuable **mechanism lesson**:

> successful Janus-like segregation probably requires a genuinely nonlinear relative mode rather than merely a slightly enhanced linear eigenvalue.

## Fatal theoretical problem

The original dynamical BIMOND action couples the two metric connections through derivative interactions built from

`C^alpha_{mu nu} = Gamma[g]^alpha_{mu nu} - Gamma[f]^alpha_{mu nu}`.

D'Ambrosio, Garg & Heisenberg (2020) performed a minisuperspace/Hamiltonian and cosmological-perturbation audit and concluded that unconstrained BIMOND generically propagates the Boulware-Der ghost. Their diagnosis is structural:

- derivative kinetic mixing of the two metrics;
- interaction terms outside the known dRGT/Hassan-Rosen ghost-free potential structure;
- extra scalar propagation/strong-coupling pathology in cosmological perturbations.

They find that the constrained limit with the second metric forced flat reduces to an `f(Q)` nonmetricity MOND theory and can avoid the BIMOND ghost, but it then ceases to be the dynamical two-sector bimetric theory needed for Janus-like twin-matter segregation.

Reference:

D'Ambrosio, Garg & Heisenberg, *Non-linear extension of non-metricity scalar for MOND*, Phys. Lett. B 811 (2020) 135970, arXiv:2004.00888.

## Later BIMOND papers do not close this defect

Milgrom's 2022 *Broader view of bimetric MOND* explicitly states that stability and possible ghosts are not addressed and treats BIMOND as, at best, an effective framework that may require additional elements.

His 2026 paper, *Bimetric MOND as a framework for variable-G theories: Local systems and cosmology*, expands the framework but explicitly states that he cannot yet provide a consistent model satisfying all cosmological observations. The paper discusses the possibility of tolerating some local theoretical issues because MOND approaches GR in high-acceleration systems; this is not sufficient for our standard of a fundamental cosmological theory.

References:

- Phys. Rev. D 106, 084010 (2022), arXiv:2208.10882.
- Phys. Rev. D 113, 064014 (2026), arXiv:2512.09353.

## Decision

`BIMOND_AS_FINAL_JANUS_CONTINUATION = REJECTED`

Reason: its most relevant full two-metric implementations do not currently pass the ghost/degree-of-freedom gate.

`BIMOND_SEGREGATION_MECHANISM = RETAINED_AS_R&D_INSPIRATION`

The key idea to transplant, if possible without reintroducing a ghost, is:

**make the relative sector strongly nonlinear in the low-acceleration / transition regime, so that tiny differences can be amplified much more strongly than by a fixed linear `4/3` gravitational eigenvalue.**

## Implication for JANUS-R

Do not graft BIMOND's derivative metric interaction directly onto Hassan-Rosen; that would sacrifice the very ghost-free property for which JANUS-R was adopted.

Instead search within the existing Hassan-Rosen nonlinear helicity-0/Vainshtein dynamics for an analogous amplification of the relative mode during the cosmological transition.

If Hassan-Rosen cannot produce this amplification, the research program should conclude that the Janus segregation intuition cannot presently be implemented in a known complete ghost-free two-metric theory, rather than hiding the defect behind a phenomenologically attractive but ghostly action.
