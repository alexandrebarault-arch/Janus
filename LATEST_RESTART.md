# JANUS Gate 2B — point de reprise prioritaire

Date: 2026-10-18
Active branch: research/gate2b-nonhomothetic-transfer
Scientific status: GATE_2B_OPEN

**Read this file first after an interrupted session.** The larger historical journal is research/GATE2B_LATEST_RESTART.md (sections 1–18); the NEW mathematical details are in research/FINITE_MU_NATIVE_TRANSPORT_AUDIT.md.

## Latest commits/results

- numerics/hr_native_sampling_compact.py — 22x16 profile pullback based on the FULL inverse f-native background chart Jacobian, then finite-radius 4*pi*r^2 integration.
- tests/test_hr_native_sampling_compact.py — 10 targeted tests passed in a locally reconstructed environment.
- research/FINITE_MU_NATIVE_TRANSPORT_AUDIT.md — full derivation, assumptions, tests, limitations, ordered next gates.

The inverse-chart identity is

```text
T=t+sigma(t)*r^2/2,   R=(1+mu(t))*r
D=(1+sigma_dot*r^2/2)*(1+mu)-sigma*mu_dot*r^2>0
q_T=((1+mu)*q_t-mu_dot*r*q_r)/D
q_R=(-sigma*r*q_t+(1+sigma_dot*r^2/2)*q_r)/D
```

An actual RED test caught a missing `1/k` in the derivative of the radial metric shift profile; this was corrected. All 10 new targeted tests pass after correction, including finite quadrature convergence and beta0/beta4 sector separation.

**NO physical kinetic or dispersion conclusions follow**: these 16 trial action slots are not the historical 16-dimensional physical pre-metric De Felice state, and the four f-native perturbation amplitude rates are not independent new propagating fields.

## Exact next RED, in order

1. Assemble a coherent time-supported Einstein-Hilbert + native HR + TWO dust canonical phase actions, using this same common/native chart and regular radial support, including all background and perturbation field transports.
2. Check integration by parts, tadpoles, native f-volume/Noether boundary identity and metric auxiliary block rank.
3. Reduce the four metric auxiliaries and the time-dependent BD null coordinate; KEEP both dust canonical phase pairs dynamical.
4. From the SAME completed action reproduce (a) finite-H Candidate-C mu->0 De Felice physical scalar speed, and (b) homothetic Aoki nonlinear kinetic/gradient K_S,c_S^2 including stable AND unstable branches.
5. Only then approach fold 1 (a ~ 0.0301646) and test constrained kinetic/gradient regularity. Continue with transition/late transfer only if healthy.

## Verification and branch rules

- Last targeted local run: `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_native_sampling_compact.py` -> 10 passed. These tests used locally reconstructed prerequisite sources from the committed implementations.
- Whole repository suite NOT run; clone DNS failure and disabled GitHub Actions.
- Keep main and research/v2-flrw untouched; commit on research/gate2b-nonhomothetic-transfer.
- Keep an explicit FAIL/OPEN verdict if the two physical acceptance oracles fail, rather than claiming JANUS validated.

## Parallel audit — external SJHR note, 2026-10-18

**Mandatory reading before external scientific circulation:** `research/JHR_EXTERNAL_PREPUBLICATION_AUDIT_2026_10_18.md`. The corresponding executable tests are `tests/test_jhr_prepublication_gates.py` (4 targeted tests passed in a reconstructed local workspace).

The externally supplied 2026 JHR action is **not** the ongoing positive-kinetic JANUS-R continuation. The source note's *negative* f Einstein–Hilbert sign creates an indefinite common-time TT kinetic form if both couplings are positive. The HR BD constraint does not repair this tensor kinetic sign. The stellar Noether numerical sum cancellation does not establish each separate metric Bianchi constraint, the stated 1 meV strong-coupling scale is incompatible with m~1e-32 eV under the displayed Lambda3 formula, and the apparent CMB third-peak fit is a tunable forced-oscillator output rather than a predicted C_ell.

**Publication gate: external JHR as written FAILS current validation. Do not present as proven.** Keep this audit distinct from Gate 2B, which remains OPEN.
