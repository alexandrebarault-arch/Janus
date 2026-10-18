# JANUS Gate 2B — real-provider integration and f Einstein–Hilbert Ward audit

Date: 2026-10-18. Branch: research/gate2b-nonhomothetic-transfer.

**Status:** `UNTILTED_REAL_PROVIDER_PARTIAL_ACTION=GREEN_IN_FOCUSED_WORKSPACE`; `FLRW_F_EH_CHART_WARD=GREEN`; `FULL_NONHOMOTHETIC_EH=RED`; `GATE_2B=OPEN`.

## Result A — run the previously PENDING real-provider test

Prior checkpoint 22.1 left `tests/test_hr_full_scalar_eh_two_dust_real.py` only syntax-compiled. The new session reconstructed the ACTUAL computational dependency path:

```text
numerics/hr_full_scalar_eh_two_dust_untilted.py
  ├── numerics/hr_full_scalar_eh_homothetic.py
  └── numerics/hr_two_dust_preconstraint.py
       ├── numerics/hr_native_sampling_compact.py
       │    ├── numerics/hr_compact_radial_interaction.py
       │    ├── numerics/hr_native_stueckelberg_jet.py
       │    └── numerics/hr_native_field_sampling.py
       └── numerics/hr_compact_radial_interaction.py
```

The genuine HR Hessian algorithm and BOTH dust canonical blocks were executed, not a mock or an independently fabricated 22x22 matrix. The previous two tests now run GREEN, asserting that the complete **time-local, untilted** 24x24 amplitude/rate Hessian is the sum of native scalar EH for both metrics, native HR and both dust phase contributions; f Planck scaling affects ONLY the f native EH block.

**Important reproducibility qualification:** the existing prerequisite numerics modules were reconstructed manually from the GitHub connector's source contents, in a new local workspace where GitHub DNS blocked cloning. These files preserve the mathematical source algorithms but are **not byte-identical Git blobs**: many comments, docstrings and source formatting were compacted. This is an execution of the real algorithms and dependencies, **not a cryptographically exact clean checkout** or repository-wide verification. The three previously existing full-scalar EH modules and pending integration test were already byte-identical to GitHub, and the new test/ward files have exact GitHub hashes. Do not describe the focused workspace as a 100% exact clone.

Added two genuine provider-level tests to the already committed file:
- 18/30-point Gauss–Legendre radial quadrature convergence for the complete 24x24 Hessian and tadpole gradient;
- turning m² off removes the HR block identically while retaining nonzero independent EH and dust blocks, including both canonical momentum-rate couplings.

At the dimensionless off-shell diagnostic point, 28-point quadrature yields

```text
H.shape                          (24,24)
max(abs(H-H.T))                  0
H[p_g,Y_g_dot]                   +0.001524706442287953
H[p_f,Y_f_dot]                   +0.0004973775270778598
H[p_f,T_dot]                     -0.0004973775270778598
rank[p_g,p_f] vs [Y_gdot,Y_fdot]  2
norm(gradient)                   ~0.02001780449 (background OFF SHELL)
```

Illustrative unreduced rate-rate entries `H[psi_g_dot,psi_g_dot]` and `H[E_g_dot,E_g_dot]` are approximately -0.00862309 and +142.18578 in these profile conventions. **Their signs are NOT physical ghost/gradient eigenvalues**, and their large differences reflect arbitrary radius/wavenumber/trial profile normalizations and missing constraints. Likewise an off-shell 4x4 lapse/shift subblock rank cannot establish the final metric constraint/BD rank. Most importantly, the nonzero gradient is evidence that the chosen input background is NOT demonstrably an on-shell solution.

## Result B — first independent full-spacetime f Einstein–Hilbert chart Ward oracle

New artifacts:
- `numerics/hr_eh_spacetime_ward.py`
- `tests/test_hr_eh_spacetime_ward.py`

Derive an invariant compact spacetime integral for a flat f-native FLRW metric with lapse `n(T)`, scale `alpha(T)`, and a native lapse perturbation `Phi=v q(T,R)`. The exact ADM+GHY representative from the positive-sign Einstein–Hilbert action is, per solid angle with overall M_f²/2 and M_f² set to 1:

```text
L_f,EH = -3 alpha(T) alpha_T(T)^2 R^2
              / [n(T) sqrt(1+2 v q(T,R))].
```

The `v=0` native background and first perturbation are:

```text
rho0(T,R) = -A(T) R^2,
rho1(T,R) =  A(T) R^2 q(T,R),
A(T)=3 alpha alpha_T^2/n.
```

Pull them into common chart coordinates via `T=t+sigma(t)r²/2`, `R=(1+mu(t))r` with background Jacobian determinant `D>0`. Add compact interior chart variations

```text
deltaT=e_t A_t(t)F(r), deltaR=e_r r A_t(t)F(r),
A_t=[1-(t/Tmax)^2]^4, F=[1-(r/Rmax)^2]^4.
```

For the mixed variation between an interior chart displacement and native f lapse perturbation, the **complete** chain rule gives

```text
delta_e delta_v S_f,EH =
  4pi int dt dr {
     D [rho1,T deltaT + rho1,R deltaR]
      +rho1 deltaD
  } = 0.
```

This is a compact-support total-divergence identity for the native scalar-density change of variables. It holds **off shell** for positive smooth background and regular, orientation-preserving chart; it does not establish the on-shell f Einstein equation or the gravitational constraint algebra.

**Missing-sampling negative control:** artificially freezing `q(T,R)` under the chart variation drops `q_T deltaT+q_R deltaR` and leaves a nonzero mixed coefficient. At 40-point quadrature:

| Mixed variation | Time-chart displacement | Radial-chart displacement |
|---|---:|---:|
| Exact complete | -8.67e-19 | -2.20e-19 |
| Frozen native lapse q | -3.22107248e-4 | -2.77619145e-5 |
| Restored field-sampling transport | +3.22107248e-4 | +2.77619145e-5 |

A **second independent check** evaluates the exact finite-amplitude common chart integral at multiple nonzero compact deformations (both temporal and radial): it is invariant to the quadrature precision. For v=.04, the reference action and displaced action both evaluate to approximately -0.02309696873988991 in the arbitrary normalized control.

The native ADM density itself was independently compared at three nontrivial lapse amplitudes to the existing repository function `flat_spherical_adm_eh_density`. Its GitHub blob hash `7d4794e41e355d5f3ac7f212898e5f4a59503460` matches the local file byte-for-byte. This prevents the Ward oracle from solely self-validating a newly invented density.

**Critical limitation:** this Ward identity covers a native FLRW geometry and **one lapse perturbation**, using the ADM+boundary representative. It is NOT yet a full f-EH chart variation of all native scalar shift, trace and shear perturbations, nor a coupled Einstein–Hilbert plus HR plus dust Noether identity. It identifies a correct necessary condition and a future regression oracle for the full calculation, not its completion.

## Focused test evidence and provenance

Actually executed in local working folder `/mnt/data/janus-next`:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
24 passed
```

Test breakdown: **11 direct native spherical EH tests, 2 mock-assisted EH/interface structural tests, 4 real-algorithm EH+HR+two-dust assembly tests, 7 independent f-EH Ward tests.**

Exact local/GitHub content hashes confirmed for the new files:

```text
numerics/hr_eh_spacetime_ward.py       e93f3de271be35eaeb629f76196cc7d3fa123fea
tests/test_hr_eh_spacetime_ward.py     bcc6ec74fda3ae09fcf5aca455a58f4df9d81c67
tests/test_hr_full_scalar_eh_two_dust_real.py
                                      2fbff39f7f154ccebd67b32e37de0909bc23c908
```

This is **NOT** a repository-wide passing suite and **NOT** a full clean Git checkout. Actions disabled, direct clone DNS blocked.

## Strict ordered next RED gates

1. Extend the full f-native spherical Einstein–Hilbert ADM action (not only FLRW lapse) to fully coherent `T(t,r),R(t,r)` chart displacements and sampling of `Phi_f,B_f,psi_f,E_f` and all first/second derivatives; integrate on compact time/radial support and require the **entire** f-EH diffeomorphism Ward identity.
2. Unify its 24-amplitude/rate output with the already real-algorithm-exercised HR+two-dust action on a consistent **time-dependent** basis. No physically meaningful Schur or BD reduction before this.
3. Impose ONE nonhomothetic on-shell Candidate-C background, satisfy both matter conservation equations and tadpole cancellation, track metric auxiliary rank and time-dependent BD-null direction.
4. Require from the same reduced action BOTH independently derived physical oracle limits: finite-H mu->0 De Felice and nonlinear homothetic Aoki `K_S,c_S²`.
5. Only then test the first fold near a≈0.0301646 for continuous healthy scalar kinetic and gradient evolution. If an obstruction is found, record an explicit negative Gate-2B verdict instead of fitting arbitrary matching data.

**Scientific verdict:** UNTILTED 24x24 PARTIAL ACTION REAL-ALGORITHM TEST GREEN; f-EH FLRW Lapse WARD GREEN; FULL NONHOMOTHETIC PHYSICAL ACTION OPEN; JANUS-R NOT VALIDATED.

## One-command verification report (added after audit)

`scripts/verify_gate2b_step23.py` runs the four relevant focused pytest files and produces a JSON provenance manifest with SHA-256 digests, test status/count, Python version and whether it is a real Git checkout. On the reconstructed workspace, the script actually returned exit code 0, **24 passed**, with `workspace_origin=non_git_workspace_reconstruction` and null Git HEAD. Its source hash matches GitHub blob `17c7a7693dfd2ed7f0191d8d22b65345da8f952e` exactly. Researchers should run the same command on a clean Git clone, submit the resulting JSON and separately run a full-repository regression. A passing local reconstructed report is not an independent reproduction.

Command: `python scripts/verify_gate2b_step23.py gate2b-step23-report.json`.
