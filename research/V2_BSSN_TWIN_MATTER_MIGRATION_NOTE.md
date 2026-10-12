# V2 — BSSN twin-matter migration note

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `DEFERRED_BUT_HIGH_VALUE`

## Finding

The pinned upstream BSSN implementation already contains explicit f-sector matter projection hooks:

- `eq_pf_frho`
- `eq_pf_fj`
- `eq_pf_fJ11`
- `eq_pf_fJ22`

They currently return zero in `include/eom-BSSN/eomBSSNMatterReg.h`.

Crucially, the generated BSSN lapse-ratio expressions already reference these f-matter projections (for example `eq_pf_frho` appears inside `eomBSSNLapseRatiosReg.h`).

Therefore a future BSSN twin-fluid extension should not require re-deriving the lapse matter block in the same way as the historical standard-3+1 source. The symbolic BSSN equations already expose the relevant matter interface; the missing work is primarily the independent f-fluid state/evolution and nonzero projections.

## Why BSSN is not promoted to the first executable gate yet

The covariant BSSN formulation is theoretically preferable to raw standard 3+1 for long evolutions, but the bimetric system is not simply the GR BSSN system twice.

The original formulation paper explicitly states that strong hyperbolicity cannot yet be claimed under the same assumptions as in GR because the interaction and dependent lapses alter the principal structure.

The 2020 spherical dust-evolution paper used the standard 3+1 code for the published short-time simulations and described BSSN implementation as work in progress toward more stable long-time runs.

No later primary source located in the current 2020–2026 literature search demonstrated a mature long-time spherical two-metric BSSN evolution that would justify skipping the published STD baseline gate.

## Decision

Keep the current order:

1. compile and reproduce the pinned STD one-fluid baseline;
2. apply the fully prepared twin-fluid STD patch;
3. demand zero-f regression;
4. attempt a short twin-wall evolution only long enough to distinguish a regular physical response from immediate branch/lapse failure;
5. if a localized wall response exists but STD then runs into its known center/boundary limitations, migrate promptly to BSSN rather than spending effort extending STD longevity.

## Migration advantage

If migration is triggered, audit these upstream BSSN elements first:

- f-sector projection placeholders in `eomBSSNMatterReg.h`;
- f-matter appearances in `eomBSSNLapseRatiosReg.h`;
- field registration in `src/bim-solver-BSSN.cpp`;
- regularized parity/source conventions;
- gauge choice / mean-gauge compatibility;
- any generated DIRK Jacobians if an implicit integrator is retained.

The standard twin-fluid Valencia mapping already derived in this repository provides the sector-dual matter equations, but the BSSN conserved-variable normalization must be checked against the regularized BSSN definitions rather than copied blindly.

## Scientific implication

A failure of the historical STD code after the wall has shown regular short-time evolution is not a reason to reject JANUS-R. At that point the correct next test is formulation migration.

Conversely, the existence of BSSN matter hooks is not evidence that a stable twin-wall solution exists. It only lowers the engineering cost of the next formulation if the physical gate survives.
