# Janus Research

> **Active Gate 2B checkpoint (23 Oct 2026 — Step61):** Start from [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), read [Step61 exact constrained normalized radial higher-jet and shift consistency audit](research/STEP61_NORMALIZED_RADIAL_ODE_JETS_AND_SHIFT_CONSISTENCY_AUDIT.md) and [Step61 machine report](research/reports/gate2b-step61-report.json). On the REAL documented Step55 radial ODE 2s U_s=G(s,U)-2U with P=r²U, exact independent symbolic ODE chain gives P'=rG, P''=G+2s G_s+(G−2U)G_U and P'''=2r(H_s+H_U*(G−2U)/(2s)); center nonresonant recursion follows from G(0,U)=3U0−U. The actual certified Step55 U,V bounds imply |P−Pstar|<=0.00007225 and |P'−Pstar'|<0.0017425, NOT certified P'',P''' without G derivatives. **New exact Step60 consistency gate:** before evaluating lower-order Dirac coefficients, replace external zr by physical Z1 in z''; otherwise Δz''=(zr−Z1)*[-3z sqrt(1−z²) Dg'+(3z²−1) K']/K, which is generally nonzero. **15 NEW stand-alone symbolic tests PASS**, both new GitHub blobs byte-identical to tested local files. The authentic Step55 G compiler and physical six-pair Step60 temporal operator were NOT imported or rerun in Step61; historical Step57–60 passes remain previous separate evidence. Full Dirac rank/lapse fixing, ghost freedom, true 4D evolution all OPEN; Gate2B OPEN, JANUS-R NOT VALIDATED. Write ONLY on `research/gate2b-nonhomothetic-transfer`; keep disabled Actions OFF.

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
