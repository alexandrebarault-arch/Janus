# Janus Research

> **Active Gate 2B checkpoint (22 Oct 2026 — Step48):** Start at [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), read the [Step48 original non-IBP IVP Poisson and exact center Frobenius audit](research/STEP48_ORIGINAL_POISSON_AND_CENTER_FROBENIUS_AUDIT.md) and [machine report](research/reports/gate2b-step48-report.json). For the Step47 interior noncomoving curved two-dust IVP, the ORIGINAL unintegrated six-canonical-pair ADM/HR Poisson oracle was run on two independent compact lapse pairs at 161/321/641/1281 nodes: higher Richardson extrapolations are approximately -8e-15, **NUMERICAL only, not a proof of exact zero**. New symbolic center analysis PROVES the necessary regular branch condition Uf(0)=Mf²*b*(Pg/(Mg²*a)-2*z1); a formal 1/r singular mode explains backward IVP ill conditioning. New GitHub executable files and original non-IBP oracle byte-match tested local sources. **10 Step48 tests PASSED; 2 deselected pending a coherent original-provider worktree**, CI remains disabled. Global center-regular exactly constrained continuation, continuous new-IVP positive dust and full six-pair Dirac time preservation/lapse fixing remain OPEN. Gate2B OPEN, JANUS-R NOT VALIDATED. Work only on branch `research/gate2b-nonhomothetic-transfer`.

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
