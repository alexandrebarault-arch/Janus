# JANUS Gate 2B — Step 35: regular-center rigidity on the FLAT/comoving secondary submanifold
Date: 2026-10-20. Active branch: research/gate2b-nonhomothetic-transfer.

## Scope, prior evidence, and exact mathematical advance

Start from the earlier Step33f restricted Poisson-functional bracket already cross-checked against the full Step33e bracket, **not** an asserted general field-theoretic BD secondary. Assumptions: spherical spatially FLAT Lg=a,Sg=ar,Lf=b,Sf=br; BOTH dust clocks comoving; pL_i=r² P_i(r), pS_i=(r² P_i)' so Dg=Df=0; regular elimination of relative HR radial shift z=0; nonzero m² and J(y).

With y=b/a, J(y)=beta1+2 beta2*y+beta3*y² and
X(r)=Pg(r)/(Mg²*a)-Pf(r)/(Mf²*b), the previously verified K00 is

    C_flat(r) = (m² Mg² a² J(y)/2)*r²*[3 X(r)+r X'(r)]
              = (m² Mg² a² J(y)/2)*d[r³ X(r)]/dr.

The new observation is the **regular-center necessity theorem within this subclass**:
for m²*J(y) != 0, C_flat(r)=0 on (0,R] iff r³X(r)=constant. Since regular spherical canonical data have finite Pg,Pf at r=0, X must remain bounded, the constant is zero and X(r)=0 pointwise. Thus the synchronized gravitational momenta are not just one sufficient example (as noted in Step33f); they are **necessary in the regular subclass**. On a punctured domain C0/r³ is an alternative solution, but pL=r²P then develops a ~1/r singularity and is not regular central data.

This does not establish Dirac time preservation, a physical lapse ratio, or general local ghost removal. The conclusion cannot be promoted to curved spatial slices, moving dust, generic shift z or full 4D perturbations.

## Independent primary reconstruction and positive two-dust witness

The new numerics/hr_regular_secondary_flat.py independently reconstructs original, non-IBP spherical flat primary densities including separate g/f dust momenta, computes the exact polynomial secondary via derivative of r³X, and finds floating-point polynomial extrema over [0,1] by finding stationary roots (not grid-only positivity samples).

At Candidate-C dust-only a=.4, y=.5787707228025044:
- J=+.6763833272458433 (regular).
- Pg=-.76351101*(1+.08r+.032r²) and Pf=(Mf²*b/(Mg²*a))*Pg.
- min_[0,1] pg/r² = +.900000000000 approximately.
- min_[0,1] pf/r² = +.124128183812 approximately.
- The dust momenta are independently positive and NOT identified with each other; metric momenta are nonconstant, while X=0.
- Both direct lapse primaries and both radial momentum primaries vanish at evaluated points at floating-point roundoff.
- A separate small f-momentum perturbation leaves the primary equations satisfied after recomputing BOTH dust densities, but makes the secondary nonzero; this excludes tautologically coding the secondary as zero.
- eps in (-.15,-.08,0,.08,.15) passes positivity for the whole radial [0,1] polynomial extremum check. Smallest recorded lower bounds across those eps: g +.3337014213, f +.1202487014.

The homogeneous differential operator L[X]=3X+rX' has the unique bounded-center solution for a polynomial forcing f(r)=sum f_n*r^n: X(r)=sum f_n*r^n/(n+3). The singular free C/r³ solution is deliberately excluded. Thus the restricted linearized secondary has no bounded-center radial kernel in X at fixed a,b and fixed J!=0.

## Degenerate J gate

For Candidate-C beta values, roots J(y)=0 are approximately y=.15852484 and .46111868; these roots are NOT an alternate proof of a physical secondary: at J=0 the nondegenerate relative-shift elimination used to derive the K00 formula fails, and the present module rejects it explicitly.

Thirty independent dust-only a samples in [.025,1] via positive quartic continuation had min J~+.5218731130. This is a NUMERICAL sampled branch check, not a certified continuous lower bound, not a radiation-era assertion, and not a fold stability test.

## Actual reproducibility

New exact files:
- numerics/hr_regular_secondary_flat.py, Git blob d30281a11d854084270a4f536e24e2dc857d58fc
- tests/test_hr_regular_secondary_flat.py, Git blob 6425b1c36c8d7e4401bfffe6dabf4f9b31f58cc6

Actual local command in a new /mnt/data/janus-step35 isolated workspace:

    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_regular_secondary_flat.py
    11 passed in 0.32s

Both GitHub blob hashes were computed using the exact bytes of the locally executed files and match the uploaded source/test Git blobs. The full repository suite, earlier 33f/g/h, or Step34 checkpoint claims were NOT rerun. No CI, no external independent replication.

## Recovery of Step34 documentation inconsistency

The existing research/STEP34_CHECKPOINT.txt refers to:
research/ORIGINAL_NONIBP_FINITE_VARIATION_STEP34_AUDIT.md,
tests/test_hr_original_discrete_pb.py,
scripts/verify_gate2b_step34.py,
research/reports/gate2b-step34-report.json.
Those four paths are ABSENT from the inspected active-branch tree as of the Step35 start. The actual source numerics/hr_original_discrete_pb.py EXISTS. Do not treat the alleged Step34 seven tests as independently reproducible from this branch until the missing code/report or an explicit retraction is provided. Step35 does NOT resolve this provenance gap.

## NEXT EXACT RED (priority)

1. Extend primary+SECONDARY=0 simultaneously to the curved, NONCOMOVING Step33g/h canonical family over a continuous radial interval. Solve for a freely adjustable smooth radial momentum/metric profile, including derivative of the K01 kernel (C_local=K00-K01'), with both positive dusts and shift regularity. Do NOT tune only one integrated smeared bracket.
2. From such data, calculate {C_local,H_g}, {C_local,H_f} with all canonical pairs and smeared-functional boundary terms, test full Dirac preservation and lapse fixing, and separate the K=0/J=0 degenerate branches.
3. Independently produce genuinely physically nonhomothetic on-shell evolution, not just chart compensation. Reproduce finite-H mu->0 De Felice AND homothetic nonlinear Aoki K_S,c_S² (healthy and unhealthy controls) on the SAME completed reduced action, then investigate Candidate-C first fold a~.0301646.
4. Repair the orphaned Step34 checkpoint references and perform a full repository regression in a coherent worktree.

Status: STEP35_RESTRICTED_CENTER_RIGIDITY=DERIVED_AND_TARGETED_TESTED; GENERAL_LOCAL_SECONDARY=OPEN; DIRAC_LAPSE_FIXING=OPEN; ON_SHELL_NONHOMOTHETIC=OPEN; GATE_2B=OPEN; JANUS-R NOT VALIDATED.
