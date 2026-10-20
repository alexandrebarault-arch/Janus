# JANUS Gate 2B — Step37: curved, noncomoving two-dust APPROXIMATE local-secondary continuation

Date: 2026-10-20. Work branch: \`research/gate2b-nonhomothetic-transfer\`. **Scientific verdict:** restricted curved noncomoving two-dust **numerical near-secondary witness achieved**, not a continuum exact solution or completed Boulware–Deser Dirac algorithm. \`GATE_2B=OPEN\`; \`JANUS-R NOT VALIDATED\`.

## 1. Exact hard question addressed

Previously Step33g found *curved*, *noncomoving*, nonzero-relative-shift spherical ADM data satisfying both lapse primaries, the diagonal radial momentum primary, and the algebraic shift equation pointwise, with both canonical dust momenta positive. However the mixed Hamiltonian functional Poisson bracket yielded a necessary local secondary coefficient \`C_local=K00-(K01)'\` around +0.47 at r=.43: the primary witness alone fails secondary consistency. Step35 derived a flat/comoving, bounded-center inverse \`A(r³X)'\`; Step36 proved nonzero J on the particular dust-only homogeneous Candidate-C background.

Step37 retains a REAL curved/inhomogeneous two-dust primary family and seeks numerical \`C_local≈0\` over an interval, not only an integrated bracket or one radius. This is a finite-dimensional **collocation approximation**, not a proof that an exact continuum local secondary solution exists.

## 2. Starting data, primary equations and regular parities

The exact previously derived Step33g primary generator retains all five HR betas and both *independent* canonical dust fields (phases/momenta). At Candidate-C dust-only a=.4, y=b/a=.5787707228025044, use the small deformed nonproportional 3-geometries

    Lg=a(1+0.0015 r²)^2, Sg=r Lg
    Lf=b(1-0.0012 r²)^2, Sf=r Lf
    theta'_g = 0.0012 r Lg, theta'_f = -0.0016 r Lf
    z(r) = 0.004 r

The two curvatures are nonzero, distinct; the dust clocks are moving with different gradients and the relative shift is nonzero. Radial momenta \`pL_i\` are generated as \`pL_i'=2r(u_i+2ru_i')Q_i(r)\`, with g generator \`Q_g=pa/3\` and the f generator \`Q_f=pb/3+sum_{k=0}^4 c_{2k}r^{2k}\`. The even polynomial, even conformal factors, even dust phases, and odd radial shift/phase-gradient profiles are **consistent with** smooth spherical parity near the center; tests do not certify all 4D origin regularity or boundary evolution. Independently algebraically solving Hg=Hf=0 for positive dust momenta and Ddiag=Fz=0 for the shear/radial momenta preserves ALL exact primary constraints on the selected family by construction; this is not a solved time-dependent spacetime.

### Actual RED -> GREEN: correctly map the free momentum GENERATOR

An initial perturbative correction reduced C by only ~50% and DID NOT scale as a second-order remainder. The independently checked cause was a numerical representation error, not physics: Step35's X is formed from \`pLf/r²\`, whereas the curved builder's independent polynomial \`Q_f\` parametrizes \`(pLf)'/(2r)\`. At flat geometry a coefficient \`Q_{f,n}r^n\` produces **\`(2/(n+2)) Q_{f,n}r^n\`** in \`pLf/r²\`. The missing inverse \`(n+2)/2\` explains residual factors exactly 1, 2/3 and 1/2 for n=0,1,2, independently tested. Correcting this coefficient gives O(scale²) first-order residuals and rapid iteration. This is protected by \`test_flat_momentum_generator_is_not_pL_div_r2\`.

## 3. Independent mixed bracket / local secondary

Use six canonical pairs \`(Lg,pLg),(Sg,pSg),(theta_g,pg),(Lf,pLf),(Sf,pSf),(theta_f,pf)\`. The original Step33g exact symbolic Euler partials of the two *separately smeared* EH+HR+two-dust primaries are cached and sampled by complex-step radial differentiation, with independent N,N',N'' and M,M',M'' probes. The resulting K_ij reproduces the PREVIOUS Step33g numerical K00=.41113496513668, K01=-.00894437157808, K10=.11498513679744, K11=K20=.02609959454418 at r=.43, along with K02=K12=K21=K22≈0.

On the primary test family the smear-derivative Ward consistency \`K01-K10+(K20)'≈0\` is checked with changing finite-difference h, so the necessary local scalar is \`C_local(r)=K00(r)-(K01)'(r)\`, NOT just K00. Finite h derivative steps have O(h²) error; the limiting exact derivative and the full Dirac Hamiltonian algebra have not been computed analytically.

The background assembly uses the same nominal positive-EH spherical canonical equations as Step33g. The new \`kernel_fast\` caches lambdified radial profiles so that the full six-pair calculation is tractable for numerical iteration, without eliminating either dust phase pair.

## 4. Regular-center leading inverse and nonlinear collocation

For each iteration, compute the **actual curved** source \`C_local(r)\` on 18 radii between r=.05 and .85, fit \`C_local/r²\` to a fourth-degree polynomial in \`s=r²\`, then solve the flat restricted regular-center leading equation:

    A = (m² Mg² a²/2) J(y) > 0,
    A r² [3 deltaX + r deltaX'] = - C_source,
    deltaX_{2k} = -source_{2k}/[A(2k+3)],
    deltaQf_{2k} = -(Mf² b) deltaX_{2k} (2k+2)/2.

The last factor is the explicitly corrected generator conversion. Resubstitute the independently adjusted \`Q_f\` in the FULL curved primary builder, re-solve both dust momenta and pS_i, then recalculate the **full curved local bracket**. This is a preconditioned fixed-point iteration, not an exact closed-form curved solution.

Nine distinct *out-of-fit* validation radii (.04,.11,.21,.31,.41,.51,.61,.71,.83) show:

| Iteration | max abs local C |
|:--|--:|
| 0 | 0.8017435530 |
| 1 | 0.01594465734 |
| 2 | 0.0003147858816 |
| 3 | 0.000006285254332 |
| 4 | 0.0000002152984402 |
| 5 | 0.00000009584459520 |

Thus max |C| drops by > 8 million-fold on THESE discrete validation sites. At final iteration max |C/r²|≈4.36e-6. This quantity also exposes the finite-radius/origin issue: the unnormalized C is automatically small near r=0. Both dust canonical momenta are strictly positive at the nine validation sites: min pg≈0.00141698 and min pf≈0.000198788. On those sites, max |Hg,Hf,Ddiag,Fz|≈2.22e-16, min |K|≈0.00037415, max |z|≈0.00332. Fifty-one additional radial points were checked (including sampled local J(Sf/Sg)>0.6); an additional test finds the corrected local smear-derivative Ward residual decreases approximately fourfold as radial h is halved. Fifty-one sampled points were checked for positive dust momenta/regular finite K and near-zero primaries. **Do not call this interval-wide certified positivity or an exact C(r)=0 theorem.**

The convergence stalls near an O(1e-7) absolute C level and derivative h refinement changes the O(1e-8) residual. One must not claim machine-exact secondary closure; further spectral order/interval numerical conditioning is needed.

## 5. INDEPENDENT original NON-integrated-by-parts Poisson oracle

To check against self-validation by the same Euler/IBP formula, an independently written second-order radial centered finite difference discretization directly evaluates the **original** spherical EH three-curvature (including S''), pL', all HR beta potentials and TWO square-root dust Hamiltonians. It perturbs ALL twelve canonical nodal fields with complex steps and *re-solves the exact relative shift z* for every nodal perturbation, then contracts all six canonical pairs. There is no symbolic Euler/IBP machinery in this oracle.

For the SAME compact smearings, before and after Step37 correction:

| uniform nodes | uncorrected mixed PB | corrected mixed PB |
|:--|--:|--:|
| 81 | +0.009385071812 | -2.360219974e-6 |
| 161 | +0.009386846507 | -5.855849394e-7 |
| 321 | +0.009387289761 | -1.423468184e-7 |
| 641 | +0.009387400548 | -3.156366751e-8 |

The corrected mixed bracket shrinks approximately as the finite-difference grid error O(dr²); the corresponding original discrete primary residual decreases from ~2.43e-7 (81) to ~3.89e-9 (641). This supports, but cannot PROVE, convergence toward a small continuum mixed bracket. Cancellations inside an integral do not establish pointwise C=0; that is why the separate nine-radius local C test is mandatory.

## 6. Test/provenance boundary — DO NOT OVERCLAIM

- Committed solver: \`numerics/hr_step37_curved_solver.py\`, exact Git blob \`ce627177d7fa97bad21a7689b292ee24a63930cc\`.
- Committed independent oracle: \`numerics/hr_step37_original_nonibp_oracle.py\`, exact Git blob \`005449ade6e3582e3b9a5c3374a881a77e73e3f6\`.
- Committed test module: \`tests/test_hr_step37_curved_solver.py\`, exact Git blob \`01b37200c8c547ff4572dad40a7dd21879160f86\`.
- One backward-compatible extension to \`numerics/hr_curved_moving_dust_primary.py\`: optional polynomial \`f_delta\`, default empty so historical calls remain unchanged. The preexisting \`hr_curved_primary_mixed_kernel.py\` is not modified.
- \`12/12\` actual **targeted tests PASS** in reconstructed \`/mnt/data/janus-step37\`, approximately 8 seconds, using **compatibility wrappers** for the two previous Step33g providers; wrappers calculate the same background and Euler expressions and reproduce the historical K_ij numbers, BUT their blob bytes are NOT identical to the actual committed original Step33g provider files. This provenance limitation is material. NEW solver, oracle, and test Git blobs match the executed local bytes.
- \`scripts/verify_gate2b_step37.py\` is a committed full checkout acceptance runner; its numerical acceptance passed in reconstructed local worktree but a clean FULL GitHub branch checkout with the actual Step33g providers has **NOT** been rerun. No whole repository suite, enabled GitHub Actions, or independent external replication.

Do not aggregate Step33f/g/h/35/36 test counts with these 12 and pretend one giant test suite ran.

## 7. EXACT NEXT RED for Step38

**First**, execute the committed Step37 runner and 10 tests against the REAL, byte-verified historical Step33g provider files in a coherent workspace, then fix only verified regressions, and check pL-integrand/f_delta parameterization plus off-shell envelope-theorem derivatives.

**Second**, improve curved C→0 collocation to an interval-certified or rigorously convergent solution, with center regularity and both dust-positive bounds; vary polynomial degree, derivative h and radial domain independently. Distinguish J(Sf/Sg), K(r), and r→0 coordinate factors.

**Third**, derive the full Hamiltonian Poisson functional preservation \`{C_local,H_T}\` with both dust canonical pairs, the rank of the primary/secondary Dirac matrix, and the actual lapse ratio on this curved initial-data solution. If the preservation fails, REPORT NEGATIVE rather than inferring healthy BD elimination. This is the true hard physics gate.

**Fourth**, only after successful field-theory Dirac constraints: build a physically nonhomothetic on-shell time evolution and recover BOTH finite-H De Felice μ→0 and nonlinear homothetic Aoki KS,cS² (stable AND unstable control) from the SAME reduced action, before a Candidate-C first-fold/no-ghost/gradient/observational verdict.

Keep \`main\` and \`research/v2-flrw\` unchanged. The externally proposed opposite-f Einstein–Hilbert sign JHR manuscript remains a distinct critical audit.

**Final:** \`STEP37_CURVED_APPROX_SECONDARY=NUMERICALLY_GREEN\`; \`GENERAL_LOCAL_BD_SECONDARY_EXACT=OPEN\`; \`TIME_PRESERVATION=OPEN\`; \`LAPSE_FIXING=OPEN\`; \`GATE_2B=OPEN\`, JANUS-R NOT VALIDATED.
