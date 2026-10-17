# Gate 2B — compact radial HR interaction integral audit

Date: 2026-10-18
Branch: research/gate2b-nonhomothetic-transfer
Verdict: **GEOMETRIC INTERACTION-ONLY INTEGRATION GREEN; PHYSICAL FINITE-MU REDUCTION STILL OPEN**

## What changed

The existing finite-mu native 14x14 HR interaction jet and the previous j0 trial-profile pullback were **local** controls. Directly integrating the old pointwise 12x12 interface with all eight native metric variables constant or sharing j0 would be inconsistent with spherical regularity:

- scalar metric lapses and scalar spatial traces are even at r=0;
- radial scalar shifts are odd at the center;
- radial/angular traceless shear must vanish at the spherical center;
- chart Jacobian jets must arise from one pair of coherent functions deltaT(t,r), deltaR(t,r), rather than be integrated as independent local coordinates.

This audit introduces an explicit compact, smooth trial profile and integrates a correctly projected native interaction *before* metric/BD elimination. It does **not** claim to derive the physical eigenprofile.

## New implementation

- numerics/hr_compact_radial_interaction.py
- tests/test_hr_compact_radial_interaction.py

Set F(r)=(1-r²/R²)^4 for 0<=r<R, and zero outside. F is C^3 at R and smooth at r=0.

In the jet conventions (metric radial shift g_tr=N a k B, longitudinal shear g_rr ~ -2 k² E/3 and g_ang ~ +k² E/3), the regular spherical scalar amplitudes map as:

- Phi_(g,f), psi_(g,f): F;
- B_(g,f): F'/k;
- E_(g,f): -2(F''-F'/r)/k²;
- deltaT = T F;
- deltaT_t = Tdot F;
- deltaT_r = T F';
- deltaR_t = r Ldot F;
- deltaR_r = L(F+rF');
- deltaR/r = L F.

The combination F''-F'/r has a finite *zero* central limit, explicitly
48 r²/R^4 (1-r²/R²)^2. Both radial shift and traceless shear vanish at r=0.

Let J(r) be the 14x12 linear amplitude-to-jet map, H_native(r) the exact 14x14 local HR jet Hessian, and g_native its gradient. The implemented integrated quadratic interaction is

    H_compact = 4*pi * integral_0^R r² J(r)^T H_native(r) J(r) dr
    g_compact = 4*pi * integral_0^R r² J(r)^T g_native(r) dr.

Gauss-Legendre quadrature uses the exact spherical Jacobian. The HR potential density already includes sqrt(-g); it must not be multiplied by an additional a³ or N.

The 12 integrated coordinates are:
(Phi_g, B_g, psi_g, E_g, Phi_f, B_f, psi_f, E_f, T, L, Tdot, Ldot).

## Verification

In a reconstructed local test workspace, using the exact native HR jet implementation already committed to this branch:

    PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_compact_radial_interaction.py
    6 passed

The six tests check:

1. F,F',F'' and the center regular limit against finite differences;
2. spherical shift/shear parity and six coherent chart jets;
3. 16/26-point quadrature convergence of Hessian, gradient and value;
4. direct identity of the integrated quadratic form with the sum of local quadratic forms;
5. beta0 and beta4 sector decoupling after radial integration;
6. invalid input guards.

These six tests are **targeted and locally executed**. No GitHub Actions / full-repository test suite execution is claimed.

## What the result DOES and DOES NOT establish

**Established:** a compact, radially regular interaction-only 12x12 amplitude Hessian, formed from the fully nonlinear finite-mu 14x14 geometric HR jet, with the correct radial weights and no pointwise phase-parity shortcut. It is a reusable *geometric* building block.

**NOT established:** a physical kinetic matrix, scalar dispersion relation, eigenmode, stable Boulware-Deser reduction, or any Candidate-C fold crossing. In particular:

- the spatial profile is an arbitrary smooth control bump, not an Aoki or De Felice on-shell mode;
- metric and chart temporal profiles are not yet integrated consistently;
- Einstein-Hilbert gravity and BOTH dust canonical pairs have not been added;
- native f-field perturbations sampled at the displaced time T may require their own perturbation-rate Taylor terms (the 14x14 jet currently includes only native **background** n(T),alpha(T) drift);
- the selected finite-R domain must remain within the validity of background time Taylor expansions;
- background tadpoles and boundary terms have not been canceled against the other action sectors.

Therefore H_compact eigenvalues must **never** be interpreted as physical ghost or gradient indicators.

## Immediate RAF (ordered)

1. Add an independent test for the displaced-time native f-perturbation **rate** pullback and any analogous native spatial sampling, including all quadratic cross terms with deltaT. Do not silently treat these as zero.
2. Extend the same compact profile/time support into the independently established EH and two-dust phase actions; keep native time and radial derivative bookkeeping consistent across all three action sectors.
3. Assemble a single **pre-metric** constrained action. Eliminate only the four metric auxiliaries; preserve the two dust canonical phase pairs and the time-dependent Tdot-null/BD transformation.
4. Recover both mandatory acceptance oracles from the **same fully assembled** action: Candidate-C finite-H mu->0 De Felice spectrum and homothetic Aoki nonlinear K_S,c_S².
5. Only after both pass, approach Candidate-C first fold a≈0.0301646 and test the actual reduced kinetic and gradient operators before trying a crossing trajectory.

Gate 2B remains **OPEN**. This progress must not be conflated with completing the theory.
