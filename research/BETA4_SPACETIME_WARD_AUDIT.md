# Gate 2B — full compact spacetime beta4 Ward identity audit

Date: 2026-10-18
Branch: research/gate2b-nonhomothetic-transfer
Scientific status: BETA4_SPACETIME_WARD_GREEN; GATE_2B_OPEN.

## Question and exact identity

Can the existing 14x14 exact native Hassan–Rosen interaction jet, extended by the f-field sampling correction to 22x22, reproduce a true integrated change-of-coordinates identity, not merely a pointwise algebraic check?

Yes, for the beta4 f-volume term on the specified regular off-shell polynomial background and compact spacetime support, by two independent numerical routes.

For the real principal metric square root,
sqrt(-g) e4(sqrt(g^-1 f)) = sqrt(-f).

With f-native spherical variables (T,R) pulled back into common coordinates (t,r),

I = 4 pi integral dt dr [D n(T) alpha(T)^3 R^2 (1 + v q(T,R))],
D = det[d(T,R)/d(t,r)] > 0.

Use T0=t+sigma(t)r^2/2, R0=(1+mu(t))r, and independently vary
deltaT=eps_T A(t)F(r), deltaR=eps_R r A(t)F(r),
A(t)=[1-(t/Tmax)^2]^4, F(r)=[1-(r/Rmax)^2]^4
on the compact supports. Displacements vanish at outer boundaries.

The exact mixed chart/native-f-lapse perturbation variation is

d²I/(d eps d v) = 4 pi integral dt dr {
 D [partial_T(rho1) deltaT + partial_R(rho1) deltaR]
 + rho1 deltaD
} = 0,

where rho1=n(T)alpha(T)^3 R^2 q(T,R).

This is a total divergence. Omitting native field sampling q_T deltaT + q_R deltaR destroys the cancellation.

Control background: n(T)=1+.05T+.03T², alpha(T)=1+.02T+.015T²,
sigma(t)=.08+.025t, mu(t)=-.22+.05t,
q(T,R)=1+.45T+.30R²+.20TR².
These are smooth positive polynomial controls, NOT an on-shell Candidate-C solution.

## Independently implemented checks

A. numerics/hr_beta4_spacetime_ward.py computes the exact finite-amplitude native f volume, plus its independently differentiated mixed coefficient. At amplitude v=.1 the common-domain f volume is approximately 0.3828932717508013 both with zero chart displacement and with eps_T=.05, eps_R=-.04.

B. numerics/hr_beta4_native_jet_ward.py instead projects the EXISTING
numerics/hr_native_stueckelberg_jet.py plus
numerics/hr_native_field_sampling.py onto compact time/radial chart modes and a native f-field perturbation. It contracts the actual 22x22 Hessian and integrates with 4 pi r² dr dt. The interaction sign is negative, so result B matches minus result A.

At quadrature order 24, the f-lapse tests yield:

| Diagnostic | Time displacement | Radial displacement |
|---|---:|---:|
| Analytic complete mixed coefficient | ~-2.8e-17 | ~8.2e-18 |
| Actual native HR 22-jet mixed coefficient | ~2.7e-17 | ~-6.5e-18 |
| Actual native HR jet WITHOUT field sampling | +7.13598e-3 | +6.0751e-4 |
| Analytic coefficient WITHOUT field sampling | -7.13598e-3 | -6.0751e-4 |

The truncated residuals are negative implementation controls, not physical predictions. Radial integration MUST multiply the native HR jet density by r² only: the quadrature weights already contain 4 pi dt dr.

Extended beta4 tests cover all four native f scalar modes:
- lapse Phi_f: linear f-volume weight 1;
- isotropic spatial trace psi_f: linear f-volume weight 3, so omitted-transport residual exactly triples;
- shift B_f and traceless shear E_f: zero linear f-volume source on the diagonal native test background;
- the full integrated mixed variation vanishes in all four channels.

## Code, tests, provenance and unexpected failure

Committed:
- numerics/hr_beta4_spacetime_ward.py
- numerics/hr_beta4_native_jet_ward.py
- tests/test_hr_beta4_spacetime_ward.py
- tests/test_hr_beta4_native_jet_ward.py

Actual local targeted command in /mnt/data/janus-check:

PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
=> 27 passed (2026-10-18).

This reconstructed test workspace contains 6 new independent volume tests, 7 new native-jet Ward tests, 10 earlier inverse-chart tests, and 4 independent external-JHR manuscript audit tests. It is NOT a full repository regression.

To check exact source provenance, six files were compared by git hash-object to the live GitHub blob SHA, and their hashes MATCH:

- numerics/hr_native_stueckelberg_jet.py: affd900ffeded8f7de0d87b8c42b14b056b10a7a
- numerics/hr_native_field_sampling.py: 5203c1d515ad13e35ee547094dce60a61d5e8588
- numerics/hr_beta4_spacetime_ward.py: 8062b73748a8a1eca0db84cd30ca78488c4bebae
- numerics/hr_beta4_native_jet_ward.py: 2c959cc5ff5d1f39b604146442b3b2dc9419fe41
- tests/test_hr_beta4_spacetime_ward.py: f10a1f77c345971f649a92d579b25cefe5bdb799
- tests/test_hr_beta4_native_jet_ward.py: 49421a5e06aec324f8a6aea56b7e96a911233ed5

During extension from one to four native metric modes, four tests initially failed because a native field index was accidentally reused as the loop index for chart modes in the NEW audit helper. Renaming that variable to mode_index corrected the test-harness issue and the clean targeted rerun passed 27/27. It was not a discovered instability of the physical theory. The regression tests now protect against recurrence.

GitHub Actions remain disabled, and DNS prevents a clean clone in the current local runtime. No repository-wide suite or independent external verification is claimed.

## Limits and next RED gates

- This is an off-shell beta4 geometric/coordinate Ward check, NOT a proof of every beta1-beta3 interaction equation, Bianchi identity or material conservation law.
- It does not assemble Einstein–Hilbert gravity or the two dust canonical phase pairs. It has no physical kinetic/gradient operator, on-shell background, cosmological scalar spectrum, CMB calculation, or likelihood.
- Beta4 Ward cancellation does not imply a regular Candidate-C fold crossing.
- The finite-H mu->0 De Felice principal scalar and nonlinear homothetic Aoki K_S,c_S² must still be reproduced by ONE fully assembled finite-mu action before any physical stability verdict.

Immediate steps:
1. Construct compact spacetime EH + native HR + TWO dust phase action with identical profiles, native field sampling, background drift and correct measure.
2. Preserve this beta4 Ward test as a mandatory acceptance control while auditing boundary terms, tadpoles and the four metric auxiliary constraints.
3. Perform time-dependent BD/null canonicalization without Schur-eliminating either dust canonical phase pair.
4. Pass both independent De Felice and Aoki physical oracles on the same action.
5. ONLY THEN compute the Candidate-C first fold near a=0.0301646, and accept failure if the physical constraints become singular/unstable.

Verdict: BETA4_SPACETIME_WARD=GREEN; GATE_2B=OPEN; JANUS_R_LATE=NOT_VALIDATED.
