# Gate 2B — full native spherical scalar EH, untilted chart only

Date: 2026-10-18. Active branch: research/gate2b-nonhomothetic-transfer.

**Status: native full scalar Einstein–Hilbert UNTILTED GREEN; full finite-mu physical scalar/BD reduction OPEN.**

## Question and advance

The previous finite-mu Einstein–Hilbert plus Hassan–Rosen plus two-dust 22-amplitude bridge had ONLY native lapse/shift EH contributions. This new work constructs and tests an exact quadratic spherical ADM EH density for all six native scalar fields/rates (Phi,B,psi,E,psi_dot,E_dot). It includes intrinsic 3-curvature, radial/angular extrinsic curvature, spatial trace and traceless shear.

Scope: two native metrics, common compact radial profile, untilted T=t and R_f=(1+mu)r with constant mu>-1. The new 24x24 spatial, time-local trial interface combines native full scalar EH with the existing 22-slot HR+two-dust blocks by padding the earlier matrix with TWO g spatial scalar-rate columns. The pre-existing f spatial scalar-rate slots are reused. **NO independent physical mode count or stability follows from the size of the 24x24 matrix.**

## Exact native ADM scalar geometry

Use the same LINEAR spatial metric convention as the native HR jet:

- g_tt = -n²(1+2Phi); g_tr=n a U.
- h_rr = a² Qr, h_theta_theta = a² r² Qt.
- Qr=1+2psi-2k² E/3; Qt=1+2psi+k² E/3.
- F(r)=(1-r²/Rmax²)^4, U=B_amp F_r, psi=psi_amp F,
  E=E_amp P_E, P_E=-2(F_rr-F_r/r)/k².
- N_ADM=n sqrt(1+2Phi+U²/Qr).

Let Z=1+r Qt_r/(2Qt), W=sqrt(Qt/Qr)Z, b=n/a, h=a_dot/a. Then

    R3 = 2/(a² r² Qt) [
        1 -(Qt/Qr)Z²
          -2r(Qt/Qr){(Qt_r/Qt-Qr_r/Qr)Z/2
                 +Qt_r/(2Qt)+r(Qt_rr/Qt-(Qt_r/Qt)²)/2}
    ].

The independent extrinsic curvature eigenvalues are

    Kr=[h+Qr_dot/(2Qr)-b(U_r/Qr-U Qr_r/(2Qr²))]/N_ADM
    Kt=[h+Qt_dot/(2Qt)-b(U/Qr)(1/r+Qt_r/(2Qt))]/N_ADM.

The exact EH ADM density per unit solid angle is

    L_EH=N_ADM a³ r² sqrt(Qr) Qt [R3-4KrKt-2Kt²].

The code evaluates exact first/second derivatives with a 6-variable Taylor jet, not a finite-difference Hessian. These formulas reproduce the previously published native flat-spatial ADM lapse/shift Hessian when psi and E vanish.

The trace and traceless shear rates satisfy independent algebraic controls:

    H[psi_dot,psi_dot] = -12 a³r² F²/n
    H[E_dot,E_dot] = +a³r² k^4 P_E²/(3n)
    H[psi_dot,E_dot] = 0.

The negative raw trace sign is a preconstraint gauge feature, **not a physical ghost verdict**.

## Native f coordinate scaling — critical corrective RED-to-GREEN

For m=1+mu, R_f=m r and k_f=k/m. The f-native scalar shear POTENTIAL (two spatial derivatives) must transform as

    E_f,native=m² E_f,common
    E_fdot,native=m² E_fdot,common.

The f native radial shift potential transforms with one power of m:

    B_f,native=m B_f,common.

A preliminary radial rescaling test looked green before the E scaling was included. It did NOT test agreement with the existing HR physical shear. An independent **cross-action f metric matching** test detected the missing m²; the E and E_dot projection columns were repaired. The final controls compare the actual radial AND angular f metric perturbations on the two sides and rerun the f-EH radial coordinate-rescaling test after consistent field redefinition.

The native f EH integral uses exactly one f radial Jacobian m and exactly one angular factor 4pi. The native f r_f² volume factor is already included in the ADM density.

## Reproducible files

- numerics/hr_full_scalar_eh_homothetic.py — standalone native 6-field ADM exact Hessian and two-metric spatial integration.
- tests/test_hr_full_scalar_eh_homothetic.py — 11 direct independent tests (finite differences of a separately implemented nonlinear spherical ADM expression, closed-form kinetic controls, flat-spatial limit, radial-coordinate covariance, f shear agreement, domain guards).
- numerics/hr_full_scalar_eh_two_dust_untilted.py — strict untilted 24-slot composition wrapper with existing HR+two-dust action; it rejects sigma, sigma_dot, mu_dot nonzero.
- tests/test_hr_full_scalar_eh_two_dust_untilted.py — 2 composition guard/index tests using a LOCAL MOCK of the pre-existing HR provider.

Actual fresh LOCAL focused run:

    cd /mnt/data/janus-next
    PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
    13 passed

**Exactly 11 native EH geometry tests were direct. The 2 new interface tests use a mock to verify block addition/guards and do NOT demonstrate that the real full combined EH+HR+dust provider passed.** The earlier 47 targeted tests are historical from another workspace and were not rerun in this fresh focused session; DO NOT claim 60 passed.

Source blobs verified byte-for-byte against the active GitHub files:

- EH source: aa2662933fea9bb09ed8bdd209c33a1464a9fa74
- EH tests: 51a686a3f0cfe21e59d6c13eef095980780ff313
- Strict wrapper source: 455ede0361189c0ec072413f98a66feb8e2cedad
- Strict wrapper tests: 522f014d2ed42cc84ffd1440f4e24f5c9fcee5f8

Temporary development failures were due to the finite-difference comparison tolerance and an incorrect expectation that the trace/shear kinetic cross was nonzero; these were corrected on independent exact algebraic grounds. The important physical HR/E potential scaling mismatch at m != 1 was then found and corrected with a distinct cross-action metric matching test.

## Still open / strict next work

1. **Extend native full scalar EH to fully nonhomothetic inclinations:** sigma(t), mu_dot, sigma_dot, chart displacement deltaT/deltaR and all f-native derivative transport. Include temporal integration and boundary terms. Demand f EH full-spacetime diffeomorphism Ward check in addition to the existing beta4 HR Ward.
2. **Execute the actual combined 24-slot EH+HR+two-dust integration** on one exact-source workspace; currently only direct EH + MOCK structural wrapper tests were run. Preserve the two canonical dust phase pairs.
3. Impose one on-shell Candidate-C background with native lapse/scale derivatives, dust evolution, tadpole cancellation.
4. Reduce four metric auxiliaries and the time-dependent BD-null mode, keeping BOTH dust canonical phase pairs.
5. From the SAME fully reduced action, pass finite-H mu->0 De Felice scalar and homothetic nonlinear Aoki K_S,c_S² controls, stable and unstable roots.
6. Only then evaluate the first Candidate-C fold a≈0.0301646 and declare a pass or physically meaningful failure. No CMB observational claim until subsequent transfer and likelihood.

**Verdict: full native EH scalar jet GREEN on UNTILTED background only; Gate2B OPEN; JANUS-R cosmological validation NOT demonstrated.**

## Additional executable RED gate

**NEXT UNEXECUTED FULL-PROVIDER TEST:** tests/test_hr_full_scalar_eh_two_dust_real.py has now been committed. It imports the REAL hr_two_dust_preconstraint module and the new native scalar EH assembly and checks 24x24 block addition, both canonical dust momentum-rate entries, the two new g trace/shear rate channels and positive f Planck scaling. Its exact GitHub blob SHA is 3ecbf81ea429d5475e902cde2b24fd7441204126. This test has been syntax-compiled locally, but NOT executed because the full prerequisite GitHub worktree cannot be cloned in this environment; do not count it among the 13 passed tests. **Immediate resume action: reconstruct/fetch all real provider modules, RUN this test, fix any actual failure, and record full evidence before extending the chart.**

