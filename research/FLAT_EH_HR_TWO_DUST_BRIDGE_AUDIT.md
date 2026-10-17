# Gate 2B — restricted Einstein–Hilbert/HR/two-dust bridge

Date: 2026-10-18
Branch: research/gate2b-nonhomothetic-transfer
Status: FLAT_GAUGE_EH_SUBBLOCK_GREEN; FULL_SCALAR_EH_OPEN; GATE_2B_OPEN.

## Purpose and strict scope

The prior finite-mu, 22-amplitude *partial* HR interaction + two canonical dust phase-pair Hessian is now extended with analytically differentiated native Einstein–Hilbert lapse and radial shift blocks from BOTH metrics, on the SAME compact radial control profile and non-homothetic background chart.

Code: numerics/hr_flat_eh_two_dust_bridge.py
Tests: tests/test_hr_flat_eh_two_dust_bridge.py

This is a meaningful, restricted gravitational interface. It is NOT the complete scalar EH action: native scalar spatial traces and traceless shears, their derivatives, relative-chart perturbation dependence of EH, full time-supported integration, background on-shell constraints and time-dependent BD reduction are still MISSING. No physical ghost, gradient, fold-crossing or observational claim is made.

## Analytic restricted EH Hessian

In one native flat-spatial spherical chart:

    g_tt = -n² (1+2 Phi), g_tr = n a U,
    gamma_ij = a² diag(1,r²,r² sin²theta).
    N_ADM = n sqrt(1+2 Phi+U²).
    h = a_dot/a; b = n/a.
    K_r = (h-b U_r)/N_ADM,
    K_t = (h-b U/r)/N_ADM.

Because the native spatial curvature R^(3) is zero in this RESTRICTED metric, the ADM EH density before overall M²/2 and angular measure is:

    L_EH = N_ADM a³ r² (-4 K_r K_t -2 K_t²).

For linear Phi,U,U_r amplitude forms, the exact quadratic contribution is:

    L_EH^(2) = (a³ r²/n) [
      -9 h² Phi² -4 h b Phi U_r -8 h b Phi U/r
      -4 b² U_r U/r -2 b² U²/r² +3 h² U²
    ].

The implementation differentiates this exact polynomial analytically. The test comparator computes the nonlinear ADM density independently, then finite-differences its amplitude Hessian.

## Common/f-native interface and new tilt term

For a common compact radius Rmax, choose F(r)=(1-r²/Rmax²)^4. Set Phi_g/f=amplitude*F and native radial shift U_g/f=amplitude*F'(r). This matches the shift convention k B from the existing native HR local jet.

Background f map:
    T=t+sigma(t)r²/2;
    R_f=(1+mu(t))r;
    J=[[1+sigma_dot r²/2,sigma r],[mu_dot r,1+mu]];
    D=det J>0.

At the frozen slice, n(T) and alpha(T) are Taylor-sampled through their supplied background second rates. The native f shift must be differentiated at fixed f-native T, not fixed common t:

    U_f,R = [T_t B_f F''(r)-T_r B_f_dot F'(r)] / D.

Thus the EH action acquires a nonzero B_f / B_f_dot mixed coupling when sigma!=0. That coupling vanishes in the untilted sigma=0 control. The old HR 16-amplitude time/radius sampling interface already contains the B_f_dot coordinate (index 13), so there is no invented new physical degree of freedom.

The f native EH density is multiplied by D when integrated in the common coordinate chart. Gauss–Legendre weights supply the sole 4*pi angular factor. Both sectors receive positive M_g²/2 and M_f²/2 weighting; the second Planck ratio must be positive.

## Combined 22x22 PARTIAL quadratic action

    H_partial = H_HR + H_dust_g + H_dust_f
                + H_EH_g_flat + H_EH_f_flat.

H_HR includes finite-mu nonlinear interaction and native f sampling; dust momenta p_g,p_f remain independent canonical variables. Because EH is limited to a flat-spatial native metric and its background chart is held fixed, this H cannot be Schur-reduced as the physical helicity-0 system. The 4x4 block restricted to (Phi_g,B_g,Phi_f,B_f) has rank 4 at the off-shell numerical control, but this is NOT an acceptance test of the complete four-metric scalar constraint system.

## Regressions and numerical benchmark

Tested independently:
1. Local analytic EH Hessian vs centered finite differences of the exact nonlinear ADM density.
2. g-native integrated Phi_g/B_g block vs direct ADM density quadrature.
3. f-native Phi_f/B_f/B_f_dot block vs direct ADM density quadrature including the inverse chart derivative.
4. Native flat static g sector radial shift term integrates to a boundary: r²[-4 U_r U/r-2 U²/r²]=-2 d(r U²)/dr.
5. A nonzero f B_f/B_f_dot coupling occurs if sigma!=0 but not for sigma=0.
6. No artificially added EH dust momenta, f scalar shear/trace, or Stueckelberg chart columns.
7. 18/32-point radial quadrature convergence and positive f Planck ratio scaling.
8. Combined EH+HR+dust matrix additivity and preservation of p_g/Y_gdot, p_f/Y_fdot, p_f/Tdot canonical channels.
9. Invalid/singular background chart and scale domain guards.
10. Direct f native density independent second-variation regression and g static boundary cancellation.

A g-direct-density centered finite-difference regression at step 2e-4 initially disagreed by 1.71e-5 for a compact shift second derivative. The discrepancy scaled approximately as h² and disappeared under refinement to 2e-5. This was finite-step error in the independent regression, NOT physical coefficient fitting.

Dimensionless OFF-SHELL regression control:
- radius 0.23, a=0.85, N=1.03, n=1.16, alpha=0.74;
- mu=-0.24, sigma=0.08, mu_dot=0.11, sigma_dot=0.025;
- k=2.2, m²=0.7, positive f Planck ratio 1.2, g scale rate 0.04.

Selected entries, with index positions in the 22-variable partial amplitude basis:

| Entry | Restricted EH only | Combined partial action |
|---|---:|---:|
| H[Phi_g,B_g] | +0.0504605855 | +0.0504762766 |
| H[Phi_f,B_f] | -0.0532842784 | -0.0532779368 |
| H[B_f,B_f_dot] | +0.0929488001 | +0.0929488001 |
| H[p_g,Y_gdot] | 0 | +0.0015247064 |
| H[p_f,Y_fdot] | 0 | +0.0004973775 |
| H[p_f,Tdot] | 0 | -0.0004973775 |

The *restricted* 4x4 lapse/shift block has rank 4 and condition ~183.46. These dimensionless numbers are regression checks, not physical kinetic eigenvalues, CMB predictions or fit parameters.

## Reproducibility

Actual local reconstructed workspace /mnt/data/janus-check, using existing targeted GitHub-verified modules:

    PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_flat_eh_two_dust_bridge.py
    10 passed
    PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
    47 passed

The two NEW local source/test files are byte-identical to live GitHub blobs:
    numerics/hr_flat_eh_two_dust_bridge.py
    git blob 447e418ab44a55b864485538ce5e4892fbc66cef

    tests/test_hr_flat_eh_two_dust_bridge.py
    git blob 62307024098b6689f085c49589fbb6b495944a1c

This is a targeted reconstructed workspace run, NOT the full repository suite. GitHub Actions disabled, clean clone blocked by DNS, no external independent referee reproducibility.

## Exact next RED gates

1. Promote native spatial scalar trace and traceless shear (psi and E) into the EH action, including their spatial/time derivatives, within one regular common/f chart.
2. Include EH relative time/radius chart variation and f-native metric perturbation sampling. Verify a full compact EH diffeomorphism/Noether Ward identity analogous to the beta4-volume control.
3. Impose one on-shell Candidate-C trajectory for n,alpha,sigma,mu and both fluid background normalizations, and construct full spacetime time-dependent quadratic action.
4. Only then perform the four metric auxiliary constraints and the time-dependent BD-null reduction, leaving BOTH canonical matter phase pairs dynamical.
5. Require two independent physical limits on THAT SAME reduced action: finite-H mu->0 De Felice scalar, and homothetic nonlinear Aoki K_S,c_S².
6. Only after both pass, test the physical kinetic and gradient matrices near fold 1 a≈0.0301646. An algebraic fold or a restricted matrix sign is NOT a theorem about regular crossing.

Final gate: EH_FLAT_INTERFACE_GREEN, FULL_EH_HR_TWO_DUST_OPEN, GATE_2B_OPEN.
