# Janus Research

> **Active Gate 2B checkpoint (22 Oct 2026 — Step53):** Start with [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), then the [Step53 exact regular-center coefficient U2 and DOP853 outward-shoot audit](research/STEP53_EXACT_CENTER_U2_AND_SHOOTING_AUDIT.md) and [full rational machine report](research/reports/gate2b-step53-report.json). From the original positive-EH spherical HR+two-dust six-pair primary-reduced secondary, the second regular-center coefficient in pLf=r²(U0+U1r²+U2r⁴+...) is **EXACTLY ALGEBRAIC** U2=A2+B2 sqrt(H²) with exact rational inputs; integer-sqrt Fraction enclosure PROVES U2<0 (~ -1.0073853486743828e-5), 4 Laurent truncations 12/14/18/22 match identical exact fractions and bound unknown tails above r⁵. At r_start=.05, including U2 reduces **NUMERICAL** discrepancy against a DOP853 internal reference from 9.27e-15 to ~4.34e-19, not a global rigorous error bound. **9 targeted tests PASS** with three byte-identical new GitHub files. Underlying original Step45/46 formulas in this local session were faithfully reconstructed rather than byte-exact GitHub files; full original-provider re-run PENDING. No continuum dust/ODE proof, secondary time preservation, Dirac rank or lapse fixing. **Gate2B OPEN, JANUS-R NOT VALIDATED.** GitHub still has THREE named branches and default main pending owner UI switch/deletions, though histories preserved in active ancestry and old PR closed. Write science only to `research/gate2b-nonhomothetic-transfer`, Actions disabled.

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
