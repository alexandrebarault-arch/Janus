# Janus Research

> **Active Gate 2B checkpoint (22 Oct 2026 — Step52):** Read [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), [Step52 exact rational Laurent-jet U1 audit](research/STEP52_EXACT_CENTER_U1_RATIONAL_TAYLOR_AUDIT.md) and [Step52 machine certificate](research/reports/gate2b-step52-report.json). NEW EXACT RESULT: using the original SHA-pinned Step45/46 positive-EH spherical HR+two-dust Hamiltonian, regular-center coefficient U1 in pLf=r²(U0+U1 r²+...) is algebraic U1=A+B*sqrt(H²) with A,B,H² exact rational benchmark constants, certified by integer-sqrt outward fraction enclosure **0.0007897451667202464909325108904961683602148118201690 < U1 < 0.0007897451667202464909325108904961683602148118201692**. Jets at orders 14/20/26 reproduce identical exact A,B and conservatively exclude unknown tails below r^9; 8 targeted tests PASS with byte-identical uploaded code/tests and historical Step45/46 sources. **NOT** global ODE continuation/continuous two-dust positivity or Dirac secondary preservation/lapse fixing: Gate2B OPEN, JANUS-R NOT VALIDATED. Previous Git branch history consolidation is ancestry-safe and legacy PR#1 closed unmerged, but GitHub STILL has 3 refs with main default pending owner UI switch/delete. Only scientific writing to `research/gate2b-nonhomothetic-transfer` and do not reenable CI.

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
