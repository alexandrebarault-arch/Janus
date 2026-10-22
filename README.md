# Janus Research

> **Active Gate 2B checkpoint (22 Oct 2026 — Step49):** Resume from [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), the [Step49 center-analytic and outward-shooting audit](research/STEP49_ANALYTIC_CENTER_AND_OUTWARD_SHOOTING_AUDIT.md), and the [Step49 machine report](research/reports/gate2b-step49-report.json). From the original spherical six-pair ADM/HR/two-dust primary-reduced secondary, the normalized C/r² has exact even parity and a nonzero implicit derivative, yielding a CONDITIONAL local unique analytic regular-center secondary solution for prescribed analytic g/metric/phase profiles. Exact rational arithmetic proves both normalized dusts positive at the center (g=0.8856, f>0.1242). Numerical outward Frobenius shooting with first even correction matches the earlier interior branch near floating roundoff on [.001,.85], with only sampled positivity (129 radii), NOT certified global continuation. **21 new targeted tests PASS with byte-identical NEW sources**; older Step45/46/47 local dependencies are mathematical adapters, NOT full GitHub bytes, and two Step48 historical-provider tests remain pending. Full Dirac secondary time preservation/rank/lapse fixing and JANUS-R validation remain OPEN. Work only on `research/gate2b-nonhomothetic-transfer`; do not enable workflows.

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
