# Janus Research

> **Active Gate 2B checkpoint — Step68a (24 Oct 2026):** Read [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), then [Step68a exact center shift-variation audit](research/STEP68A_CENTER_SHIFT_FUNCTIONAL_VARIATION_AUDIT.md) and [machine report](research/reports/gate2b-step68a-report.json). New center-regular exact algebra for the Frechet response delta(z), delta(z'), delta(z'') of the original relative-shift stationarity on fixed Step55 positive radial benchmark; **21 targeted tests PASS**, source/test SHA Git blobs verified against actually executed files. Important negative control: even though the background shift has z''=0, delta(z') can be NONZERO (center example delta(z')=2). Original historical Step45/55/57–60 sources were NOT reexecuted together in this specific run and complete Hamiltonian X_H substitution remains OPEN. **GATE_2B OPEN, JANUS-R NOT_VALIDATED**; main/v2-flrw untouched, GitHub Actions OFF.

> **Active Gate 2B checkpoint (24 Oct 2026 — Step67b):** Start from [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), then [Step67b authentic original HR center U3 Taylor integer interval audit](research/STEP67B_AUTHENTIC_ORIGINAL_G_U3_CENTER_INTERVAL_AUDIT.md) and [Step67b machine report](research/reports/gate2b-step67b-original-center-u3-report.json). FOUR original Step45/46/55 + Step55 GLOBAL-BARRIER modules are now actually reconstructed BYTE-FOR-BYTE and Git blob verified in one runtime, and the original 256-cell Step55 proof has been RERUN with exact original strict witness margins. A new rigorous order-3 Taylor coefficient of the TRUE physical initial-data radial secondary ODE is enclosed: U3 in [-31325163121998456229/2500000000000000000000000000, -62650326243996887233/5000000000000000000000000000], i.e. U3~-1.25300652488e-8<0, giving the pLf r^8 center coefficient. **16 genuinely executed new tests PASS, both files git-byte-identical.** This Step67b is ADDITIONAL to (not a replacement for) the preceding Step67 shift-jets audit; its report remains intact. **NO original Step57–60 temporal six-pair Dirac in this joint runtime yet; lapse-fixing/rank, BD ghost freedom, full 4D JANUS-R validation remain OPEN.** Work only on `research/gate2b-nonhomothetic-transfer`; keep `main`, `research/v2-flrw`, disabled Actions unchanged.
> **Previous Gate 2B checkpoint (24 Oct 2026 — Step67):** START from [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), then [Step67 exact radial shift jets audit](research/STEP67_CENTER_RADIAL_SHIFT_JETS_AUDIT.md) and [machine report](research/reports/gate2b-step67-report.json). Relative shift z(r)=r/250 on the previously certified positive Step55 radial benchmark implies, through the exact normalized implicit root with COMPLETE s,d,k chain rule, z'=1/250 and z''=0; 20 new targeted tests passed locally, and source/test/report Git blobs were read back and checked identical to local outputs. This is a conditional initial-data algebra result, NOT a temporal Dirac calculation. Full six-pair preservation/rank, independent non-IBP oracle, lapse fixing, ghost freedom and 4D observables remain OPEN. Gate 2B OPEN / JANUS-R NOT VALIDATED. Only research/gate2b-nonhomothetic-transfer modified; main and research/v2-flrw untouched; Actions OFF. **Critical:** z'=1/250 and z''=0 describe the fixed background only; canonical Hamiltonian variations delta z and delta z' generally do NOT vanish, as in Step57/58.

> **Previous Gate 2B checkpoint (24 Oct 2026 — Step66):** Resume FIRST from [00_CURRENT_RESTART.md](00_CURRENT_RESTART.md), read [Step66 exact center-normalized HR relative-shift C² conditioning audit](research/STEP66_CENTER_NORMALIZED_SHIFT_C2_IMPLICIT_CERTIFICATE.md), and [Step66 machine report](research/reports/gate2b-step66-report.json). On the *previously certified* positive exact Step55 radial benchmark, Dg=r³d, K=r²k with k>229/1000, z=r w with w=1/250 and 0<=r<=17/20. The TRUE stationary shift algebra Fz=Dg-Kz/sqrt(1-z²)=0 normalizes to d-k w/sqrt(1-s w²)=0, uniformly invertible at r=0 with |∂_w Fhat|>229/1000; all 5 normalized first/second partial derivatives of w(d,k;s) are algebraically derived and bounded with EXACT fractions globally: |w_d|<22/5, |w_k|<1/50, |w_dd|<1/5, |w_dk|<20, |w_kk|<1/5. **20 new targeted SymPy/Fraction tests PASS**, final source/test Git blobs byte-identical to executed files. Prior original physical Step45/55 certificates were consulted and assumed, NOT reimported or rerun in this standalone Step66 workspace; this is NOT the original physical six-pair temporal lapse-rank calculation. Full on-shell Step55 four-lapse operator, independent original non-IBP temporal oracle, Dirac rank, lapse fixing, and ghost-freedom still OPEN. Gate 2B OPEN, JANUS-R NOT VALIDATED. All GitHub work stays on `research/gate2b-nonhomothetic-transfer`; main/V2 unmodified, user-disabled Actions OFF.

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
