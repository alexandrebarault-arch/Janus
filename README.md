# Janus Research

> **Active Gate 2B checkpoint (22 Oct 2026 — Step 50):** Read [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), [Step50 source-preserving branch consolidation and three-solver radial audit](research/STEP50_BRANCH_CONSOLIDATION_AND_SOLVER_CROSSCHECK_AUDIT.md), [machine report](research/reports/gate2b-step50-report.json), and [branch consolidation instructions](research/BRANCH_CONSOLIDATION_2026-10-22.md). The historical `main` and `research/v2-flrw` heads are NOW BOTH ancestors of this active branch, via a two-parent commit `4f7a3a1` with an unchanged tree, so legacy Git history is retained without overwriting scientific files. **However GitHub still displays 3 branches** and the default remains `main`: the GitHub UI must change default, close legacy draft PR#1, and delete both other refs; connected app has no admin delete/default action. Science: three numerical integrators RK45/DOP853/Radau agree at ~4.1e-14 max sampled momentum difference over 2049 radial sites, both normalized dust momenta positive at sampled sites. **29 targeted tests PASSED** (21 Step49+8 Step50), byte-identical NEW files, historical Step45–47 full authentic provider retests PENDING. This is not global continuum ODE certification or Dirac preservation. Gate2B OPEN, JANUS-R NOT VALIDATED. Continue writing ONLY `research/gate2b-nonhomothetic-transfer`, never reactivate Actions.

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
