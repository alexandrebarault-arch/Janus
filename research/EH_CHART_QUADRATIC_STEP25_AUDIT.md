# Gate 2B: Full f Einstein–Hilbert chart quadratic versus relative HR interaction (step 25)

**Date:** 2026-10-18. **Active branch:** research/gate2b-nonhomothetic-transfer.

**Verdict:** Isolated f-EH compact chart Hessian null identity GREEN; complete on-shell EH+HR+two-dust physical action and Gate 2B OPEN.

## What has actually been derived

Step 24 established the compact change-of-variables Ward identity for an isolated f-native Einstein–Hilbert ADM+GHY scalar density containing lapse, radial shift, spatial scalar trace and traceless shear, including their native temporal and spatial derivative jets.

Step 25 now takes the **actual second variation of the finite spacetime-integrated nonlinear action**, in six independent trial amplitudes:

    x=(deltaT, deltaR, Phi_f, U_f, psi_f, E_f).

Two chart perturbations are compact interior coordinate deformations. The remaining four amplitudes are f-native metric perturbations held fixed as native fields under chart reparameterization, including their native derivative samples. The native background is a smooth regular off-shell FLRW polynomial benchmark, NOT the Candidate-C solution.

The exact integral over the common chart is

    S_f(x)=4*pi integral dt dr D(t,r;x_chart)
             rho_EH( X(t,r;x_chart); metric_native(x_fields) ),

where X=(T,R), D=det d(T,R)/d(t,r), and rho_EH is the complete native spherical ADM+GHY density from the independent step-24 nonlinear native calculation. The 6x6 Hessian is computed by centered mixed/diagonal second differences of this full action, rather than by differentiating a postulated quadratic matrix.

### Analytic reason for the chart null directions

For an arbitrary smooth compact coordinate vector xi^A and any smooth scalar density rho of the f-native fields,

    delta[D rho(X)]
       = D (partial_A rho) xi^A
           + rho Cof(J)^mu_A (partial_mu xi^A)
       = partial_mu [rho Cof(J)^mu_A xi^A].

The last equality is the chain rule plus the Piola identity for a coordinate Jacobian. Its spacetime integral is zero for fixed outer boundaries, regular radial origin, and an orientation-preserving chart. Consequently, the isolated f-EH spacetime action does not change under compact chart shifts, off shell, and all of its first and second chart derivatives, including mixed derivatives with f-native field amplitudes, are zero.

This **does not** say that the combined HR+EH+matter action has a null relative-chart block or that the metric/BD constraints have been established. The f-EH identity is about a separately covariant sector expressed in moving coordinates; the HR interaction couples f and g and need not share this isolated-sector chart invariance.

### Actual six-dimensional quadratic result

At time/radial quadrature order 42, chart step 0.003, native metric amplitude step 0.004, on the dimensionless off-shell control:

    max abs(H_EH[chart rows 0:2, all columns]) = 8.673617379884035e-13
    norm_F(H_EH[native metric 4x4 block])        = 11.088651626052187
    abs(first chart derivatives)                 = 0 within numerical precision

Metric 4x4 block is nonzero:

    -0.0768272852  -0.3314061125  -0.3249043174  -5.2193951443
    -0.3314061125  -2.1674174817   0.7879604537   0.1401653057
    -0.3249043174   0.7879604537   0.6467659739   5.2282005676
    -5.2193951443   0.1401653057   5.2282005676  -2.6404757828

Changing the compact chart by (epsT,epsR)=(0.045,-0.035) changes the separately computed native metric 4x4 Hessian by at most 4.63e-12. This tests stronger invariance than a single mixed derivative.

**Discriminating negative control:** artificially freezing all native metric field/derivative samples at the original coordinates, while moving the geometry and Jacobian, gives nonzero mixed 2x4 coefficients approximately

    -0.00028618   -0.00224105   +0.00439288   +0.02914977
    -0.00001104   -0.01224483   +0.01761069   +0.31153045.

Thus the chart-null result does depend on the required transport.

### Relative HR interaction contrast

A separate finite-mu HR beta1–beta3 **interaction-only** compact radial Hessian yields nonzero relative-chart coefficients on its own arbitrary off-shell trial basis:

    Frobenius norm H_HR[chart,chart]  = 0.22018254849636304
    Frobenius norm H_HR[metric,chart] = 0.5121472056324078.

Setting m²=0 makes that HR Hessian vanish. The native EH and HR numerical norms have DIFFERENT compact supports, field profile conventions and integrations. The contrast checks nonzero relative interaction response, not a comparison of propagation rates, energies, kinetic eigenvalues, or equivalent physical modes.

## Files, actual tests and source provenance

New executable source: numerics/hr_eh_full_scalar_quadratic_chart.py
New regression tests: tests/test_hr_eh_full_scalar_quadratic_chart.py
New provenance runner: scripts/verify_gate2b_step25.py

Nine new targeted tests: complete 6x6 EH Hessian and its chart-null rows; nonzero metric block; bad native-sampling control; invariance of the complete metric Hessian under finite chart motion; independent equivalence with the separately calculated native metric Hessian; equality of mixed derivatives with the step-24 Ward oracle; variable compact spacetime supports; finite-difference step convergence and domain guards; nonzero HR relative interaction block and m²=0 decoupling.

Executed locally in /mnt/data/janus-next:

    PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
    41 passed

    python scripts/verify_gate2b_step25.py checkpoint-25-local.json
    tests_passed_count=41, tests_exit_code=0
    workspace_origin=non_git_workspace_reconstruction
    full_repository_regression=false
    physical_stability_oracles: DeFelice NOT_RUN, Aoki NOT_RUN
    gate2b=OPEN

All THREE newly executed files match their live GitHub blob SHA byte-for-byte:

    numerics/hr_eh_full_scalar_quadratic_chart.py
      975eac41ad9acc669335ddb14b5cf1b295d2c0b6
    tests/test_hr_eh_full_scalar_quadratic_chart.py
      dad81da95a883ad8845de5b79a235ac78a91cf79
    scripts/verify_gate2b_step25.py
      dbafd452b2bef6e5037f536b94e05671fb85a66c

IMPORTANT: the local dependencies from the earlier HR/dust code are still some algorithm-preserving reconstructions of GitHub source, not a full exact Git checkout. GitHub clone DNS failed and GitHub Actions were previously disabled. **41 passed** is the focused local suite, NOT the whole repository or third-party reproduction.

## Next scientific RED gates, in order

1. Construct ONE time-dependent common action with exact, coherent f-native spherical Einstein–Hilbert scalar profiles, Jacobian/field transport, the HR interaction and BOTH dust phase pairs. Preserve the new isolated EH chart-null identity as a boundary/Noether guard, but do not delete real HR relative chart couplings.
2. Impose on-shell Candidate-C background functions a(t),n(T),alpha(T),sigma(t),mu(t), with both independently conserved dust fluids. Demand cancellation of tadpoles. Current numerical benchmarks have nonzero tadpoles and are explicitly off shell.
3. Derive and eliminate four true metric scalar auxiliaries, then perform the time-dependent Boulware–Deser null/canonical reduction without Schur-eliminating either of the two dust phase pairs.
4. On THAT SAME reduced action, reproduce the finite-H mu->0 De Felice physical scalar characteristic and the homothetic nonlinear Aoki K_S, c_S² in both stable and unstable controls.
5. Only after both external acceptance limits pass, investigate constrained kinetic/gradient regularity at Candidate-C fold 1 near a≈0.0301646, and reject the hypothesis if a physical obstruction appears. No validated late-time transfer or CMB likelihood exists.

**Scientific statement appropriate for circulation:** a compact nonlinear f-EH action-level coordinate-change Hessian gate passes, and nontrivial HR relative chart couplings are distinguished. This is a consistency result, not a proof of JANUS-R cosmology.
