# Gate 2B — RAF / restart ledger

Date: 2026-10-11
Branch: `research/gate2b-nonhomothetic-transfer`

This file is intentionally short. It complements `research/GATE2B_CHECKPOINT.md` and exists so an interrupted session can resume in under one minute.

## Progress estimate

- Diagnostic of the current high-k failure: **~80% complete**.
- Gate 2B as a whole: **~45% complete**.
- RAF (remaining work) for Gate 2B: **~55%**.

These percentages are engineering estimates, not scientific confidence levels.

## Current blocker

The current JANUS 12x12 scalar closure is algebraically/Bianchi consistent but projects out the physical helicity-0 high-k gradient. It recovers the radiation speed exactly but gives a spurious gravity-like speed ~0.0159 instead of De Felice ~0.8319 at the Candidate-C comparison point.

A structural ambiguity in Comelli A.18 changes the scalar constraint rank:

- derived gauge-invariant form `(B1-E')`: rank 6 at fixed `E'`;
- printed form `(B1-E)`: rank 7 for generic non-homothetic `c != 1`.

Therefore do **not** assume `E'` is a freely prescribed state variable while deciding the correct descriptor structure.

## Exact current task

**T1c.6c — build the full scalar descriptor/DAE polynomial system without prescribing `E'`.**

Required outputs:

1. complete variable vector and derivative order bookkeeping;
2. polynomial/descriptor matrix for both A.18 variants;
3. generic rank and hidden algebraic-constraint count;
4. finite generalized mode count / physical scalar DOF count;
5. test on the dynamically on-shell Case-C early-time hierarchy;
6. identify which formulation can reproduce Comelli Appendix B.5 without tuning coefficients.

## Immediate next actions

- [ ] T1c.6c.1 — construct descriptor from the undifferentiated published scalar equations plus gauge identities/slips; no differentiated constraints used merely to square the system.
- [ ] T1c.6c.2 — apply correct Case-C amplitude weights (`E=tau^2 E_N`; induced metric/matter amplitudes with their asymptotic tau powers) before reading the principal rank.
- [ ] T1c.6c.3 — compute row/column rank profile versus polynomial degree for both A.18 variants.
- [ ] T1c.6c.4 — determine finite generalized modes and infinite/algebraic modes (constraint index / Kronecker structure as far as numerically/symbolically feasible).
- [ ] T1c.6c.5 — compare physical scalar mode count against De Felice: one gravitational scalar plus matter acoustic modes.
- [ ] T1c.6d — perform differential elimination with the validated descriptor and reproduce Comelli B.5; benchmark acceptance is `E'' + 3/tau E' - (2/3) k^2 E = 0` and high-k factor `3 q^2 - 2`.
- [ ] T1c.7 — prove invariance under Bianchi-redundant row choices and settle A.18 bookkeeping.
- [ ] T2 — on dust+dust Candidate C, recover independent De Felice scalar speed.
- [ ] T3 — identify the precise structural error in the old 12x12 closure.
- [ ] T4 — implement corrected `numerics/comelli_native_scalar.py`.
- [ ] T5 — make `tests/test_comelli_native_scalar.py` green; add >=3 additional `(z,k)` speed regressions.
- [ ] T6 — rerun all Gate-2B algebraic/constraint/Bianchi tests.
- [ ] T7 — build time-domain transfer RHS and fundamental transfer matrix.
- [ ] T8 — track the GR-connected adiabatic mode continuously.
- [ ] T9 — compute `T_gg`, `T_gf`, `T_fg`, `T_ff` and relative-mode growth.
- [ ] T10 — record Gate-2B pass/fail/inconclusive verdict with numerical tolerances and domain.

## Already ruled out — do not redo unless new evidence appears

- k/time unit conversion;
- visible dust+radiation mixture;
- `d(g00)` vs `d(f00)` closure choice;
- isolated background-derivative error;
- De Felice target normalization;
- simple A1/A2 transcription/sign typo;
- omitted anisotropic `k^2` block after slip reduction;
- A.18 prime/unprime as a simple drop-in fix to the existing closure;
- isolated f-trace interaction-sign flip;
- floating-point conditioning;
- selected high-k minors as the dispersion relation;
- frozen-a / off-shell Case-C backgrounds.

## Restart rule

Read `research/GATE2B_CHECKPOINT.md`, then this file. Resume at the first unchecked T1c.6c item. Do not integrate Candidate C transfer functions until Comelli B.5 and De Felice high-k speed are both reproduced independently.