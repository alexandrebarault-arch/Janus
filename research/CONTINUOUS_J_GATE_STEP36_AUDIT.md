# JANUS Gate 2B — Step36: rigorous continuous J(y) regularity on Candidate-C DUST-ONLY quartic

Date: 2026-10-20. Active branch: `research/gate2b-nonhomothetic-transfer`.
Result: `DUST_CANDIDATE_C_CONTINUOUS_J_GATE=GREEN_ON_CERTIFIED_INTERVAL`; `GATE_2B=OPEN`, `JANUS-R NOT VALIDATED`.

## Scientific question and discriminant

Step35 had sampled thirty positive quartic roots and reported J(y)>0, but this was not a statement about every intermediate time. Here we replace the finite sample with an EXACT-RATIONAL continuous interval certificate for the supplied decimal-calibrated DUST-ONLY Candidate-C background. This is relevant to Step33f/35's NONDEGENERATE relative shift constraint (J != 0) and the first proposed nonlinear fold a~0.0301646. It is NOT a completion of the curved noncomoving secondary, Dirac constraint algebra, or ghost/gradient dynamics.

## Exact quartic elimination

Write F=Mf²=(0.10879548725)², M=m²=23.3348939346, Cg=0.9,
Cf=3(0.23958426762)(0.5568825591873054)³; beta=(0,1,-4.2383993109,13.6801214252,-38.5117901844).
These supplied decimals are **exact rational inputs in the certificate**, not estimates of unknowable exact physical constants.

The quartic P(y,a)=0 used by the existing dust-only Candidate-C branch rearranges to

    P(y,a) = M*Q(y) + (F*Cg*y-Cf)/(3 a³) = 0
    Q(y) = F*beta3*y^4/3
         + (F*beta2-beta4/3)*y³
         + (F*beta1-beta3)*y²
         - beta2*y - beta1/3.

With t=a^(-3) and D(y)=Cf-F*Cg*y,

    t(y) = 3*M*Q(y)/D(y),
    t'(y) = [3*M / D(y)^2] * [Q'(y)*D(y)+F*Cg*Q(y)].

For EXACT rational y_L=139/250=0.556 and y_U=23/10=2.3:
1. Q's cubic and quartic coefficients q3,q4 are positive, hence Q'''(y)=6q3+24q4*y>0 for ALL y>=y_L.
2. Exact checks give Q''(y_L)>0, Q'(y_L)>0 and Q(y_L)>0; therefore Q,Q',Q'' remain positive on [y_L,y_U] and beyond.
3. D(y_U)>0, so D(y)>0 across the interval.
4. Consequently t'(y)>0 **at every point**, not merely at sampled radii or a values.
5. Exact endpoint inequalities give 0<t(y_L)<1 and t(y_U)>64000=(0.025)^(-3). The intermediate value theorem plus strict monotonicity guarantee **exactly one** root y in (0.556,2.3) for every a∈[0.025,1]; this proof does not rule out additional quartic roots outside the certified interval.
6. Since J(y)=beta1+2beta2*y+beta3*y² has J'(y)=2(beta2+beta3*y)>0 for y>=y_L, and J(y_L)=0.5159179831798272...>1/2, the whole certified branch obeys

    J(y(a)) > 1/2    for every a ∈ [0.025,1].

The proof consists of exact `fractions.Fraction` strict inequalities and rational bisection; no floating point is used to decide the inequalities.

## Independent numerical reporting (display only)

The unique root for a=1 is within (0.55688,0.55689), consistent with the supplied y0 to its calibration precision; y0 itself is NOT an exact root at the last printed digit. Specific bisection midpoints (85 dyadic steps) include:

| a | certified-root midpoint y | J(y) |
| ---: | ---: | ---: |
| 1 | 0.5568825591873056 | 0.521873113004595 |
| 0.4 | 0.5787707228025017 | 0.676383327245824 |
| 0.09 | 0.9399775251263363 | 5.119177085781536 |
| 0.0301646 | 1.971261154528869 | 37.449196983058634 |
| 0.03 | 1.9795452448545103 | 37.82670888284864 |
| 0.025 | 2.279890828005346 | 52.78175765430383 |

The two endpoints of an 85-step rational bracket may appear IDENTICAL if converted to ordinary double-precision display; they remain distinct as exact fractions. The integer-root bracket proof is strict.

## What the result DOES and DOES NOT rule out

On the regular FLAT proportional-slice (S_f/S_g=y) shift branch used in Step33f/35, the interaction factor has J(y) dependence. Hence on the controlled cosmological background interval, a vanishing **background J(y)** is not the mechanism of the proposed first fold a~0.0301646. This is an **exclusion of one possible algebraic degeneracy only**. The full K(r) contains spherical factors that vanish at the coordinate center r=0, and generic curved nonhomothetic profiles require separate K(r), J(Sf/Sg), and lapse checks. Other causes of a fold, kinetic zero, gradient instability, strong coupling, or chart breakdown remain completely possible.

The coefficients are for dust-only Candidate-C; no radiation, no nonlinear evolved Stückelberg field, no full dynamical Einstein solution. The exact-rational interval is CONDITIONAL on the decimal input parameters. The result is not a global theorem for all JANUS parameter choices, the other quartic roots, or the f-metric sign-reversed external JHR paper.

## Exact reproducibility and provenance

- Source: `numerics/candidate_c_continuous_j_certificate.py`, git blob `375e6c3197fb9d82f19b35c66331bab2675cd506`
- Test: `tests/test_candidate_c_continuous_j_certificate.py`, git blob `5b2634d0ac8a99915617ba27785b728f03a1ec00`
- Targeted actual execution in reconstructed `/mnt/data/janus-step36`:

    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_candidate_c_continuous_j_certificate.py
    # 19 passed in 0.15 s

- Independently emitted manifest: `research/reports/gate2b-step36-manifest.json`.
- The two exact GitHub blob SHAs MATCH the locally executed file hashes.
- **New combined run:** the exact Step35 source/test pair and the exact new Step36 source/test pair were placed into ONE reconstructed `/mnt/data/janus-step36` workspace and run with `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_regular_secondary_flat.py tests/test_candidate_c_continuous_j_certificate.py`: **30 passed in 0.35 s**, all FOUR executed files matched their GitHub blob SHA. This is still NOT the full repository, GitHub CI, on-shell evolution or peer reproduction.

## Critical next work (do not skip)

**HARD NEXT RED (Step37):** curved/noncomoving **primary+local-secondary** construction on a full radial interval. Start from Step35's synchronized X=0 regular-center flat data; introduce a controlled nonzero curvature/dust-gradient/shift homotopy and compute the ACTUAL original-action curved C_local(r)=K00-(K01)' using the Step33g and independent Step33h/34 functional Poisson machinery. For infinitesimal continuation, the flat linearized operator is A*d(r³δX)/dr with A=(m²Mg²a²/2)J>0. A curvature source S(r) would require δX(r)=-(1/(A r³))*∫_0^r S(s)ds on the regular branch, **only if** the source and boundary conditions admit a finite-center correction; this formula is a proposed analytic update, not a computed curved secondary solution. Then impose local secondary pointwise, TWO positive dust densities, regular K and the full separate primary/diagonal constraints; test actual full Dirac secondary time preservation and lapse fixing, including degenerate branches.

Only then attempt a genuinely nonhomothetic on-shell background and **both** same-reduced-action De Felice finite-H μ→0 and Aoki nonlinear homothetic K_S,c_S² physical oracles before judging the first fold.

Keep `main` and `research/v2-flrw` untouched. External wrong-EH-sign JHR manuscript critique is a SEPARATE track.

**Verdict: Step36 continuous branch/J nondegeneracy conditional certificate PASS; LOCAL_CURVED_BD_SECONDARY=OPEN; FULL_DIRAC=OPEN; physical JANUS-R unvalidated.**
