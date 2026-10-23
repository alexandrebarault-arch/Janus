# Janus Research

> **Active Gate 2B checkpoint (23 Oct 2026 — Step56):** Resume FIRST from [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), the [Step56 exact shift Frechet, spatial-jet, smeared-boundary and time-stationarity audit](research/STEP56_SHIFT_RESPONSE_AND_TEMPORAL_DIRAC_JETS_AUDIT.md), and [Step56 machine report](research/reports/gate2b-step56-report.json). Physical six-pair spherical Step45 positive-EH HR + two moving dusts has algebraic relative-shift stationarity Fz=Dg-K*z/sqrt(1-z²)=0 with K>0, so z=Dg/sqrt(Dg²+K²) and delta_z=[K² delta_Dg-Dg K delta_K]/(Dg²+K²)^(3/2). Crucially Dg contains -Lg*pLg_prime, and for a compact test function eta, the exact smeared functional derivative delta integral eta*z /delta pLg = +partial_r(eta Lg Z_D); lapse derivatives and noncompact boundary traces must NOT be dropped in temporal Dirac. Dot Fz=0 yields exact dot_z; normalized z/r center response has certified rational finite sensitivity using previous Step55 K/r²>0.229. A separate six-pair TOY demonstrates frozen-z error; **NOT** the physical temporal Dirac bracket. **14 new targeted tests PASS; 2 new Python files byte-exact to tested local versions**. Historic physical Step45/46 source formulas were consulted on GitHub but were not locally re-imported in Step56 standalone symbolic test. **Actual {C,Htotal}, lapse fixing, Dirac rank, BD-ghost freedom and 4D temporal dynamics UNCOMPUTED; Gate2B OPEN, JANUS-R NOT VALIDATED.** Earlier Step55 radial positive constrained initial-data result remains the previous restricted benchmark claim. Historical branch ancestors safely preserved, old PR closed unmerged; still 3 named GitHub refs/default main pending owner UI admin. All research writing on `research/gate2b-nonhomothetic-transfer`; don't re-enable Actions.

Independent technical audit and continuation of Jean-Pierre Petit's Janus cosmology.

## Objective

Do not assume Janus is true or false. Reconstruct the published model, separate mathematics from physical interpretation, attempt falsification, and explore whether a more rigorous theory can preserve the useful intuition.

## Current branches

- **JANUS-EXACT** — audit of published Janus. Current status: `NOT_CLOSED` as a general relativistic bimetric theory.
- **JANUS-R Late** — main research branch. Ghost-free bimetric gravity, two positive-energy matter sectors, conventional CDM retained in the visible sector, late-time large-scale cross-sector effects with Vainshtein screening.
- **JANUS-R2** — exploratory branch with cosmologically evolving effective graviton mass. High risk.
- **JANUS-R3** — exploratory multimetrics branch (`N >= 3`) investigating whether the exact `+G/-G` interaction pattern can emerge in a ghost-free construction.

## Research rules

1. Mathematical consistency before phenomenology.
2. A fit to data is not a derivation.
3. A mathematical solution is not evidence that the corresponding physical object exists.
4. Every result must state its assumptions.
5. Rejected branches remain documented with the reason for rejection.
6. Prefer falsifiable predictions over post-hoc explanations.
7. Lambda-CDM is a benchmark, not an enemy.
8. When a previous conclusion is found incorrect or too strong, correct it immediately and preserve the correction history.

## Repository map

- `research/STATE.md` — current scientific truth and status.
- `research/DECISIONS.md` — chronological decision log.
- `research/JANUS_EXACT_AUDIT.md` — audit of the published Janus formulation.
- `research/JANUS_R.md` — reconstructed research branch.
- `research/NEXT_TESTS.md` — ordered falsification gates.
- `sources/BIBLIOGRAPHY.md` — references and what each one establishes.

## Current headline conclusion

The strongest surviving idea is not fundamental negative mass. It is the possibility that two positive-energy matter sectors coupled to different metrics can experience scale-dependent effective cross-sector interactions through the mixing of massless and massive spin-2 modes. The current main branch requires Vainshtein screening and must now pass a lensing-and-void-profile test before it deserves further cosmological fitting.
