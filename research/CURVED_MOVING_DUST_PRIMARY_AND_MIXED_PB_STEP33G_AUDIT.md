# JANUS-R / Gate 2B — Step 33g: curved primary surface, two moving dusts, mixed bracket derivatives

**Date:** 2026-10-19. **Research branch:** `research/gate2b-nonhomothetic-transfer`.
**Scientific verdict:** `CURVED_NONCOMOVING_SPHERICAL_PRIMARY_SURFACE=GREEN`; `RADIAL_MIXED_HAMILTONIAN_KERNEL_CHECK=GREEN` on the specified constrained witness; **`GENERAL_LOCAL_BD_SECONDARY_AND_TIME_PRESERVATION=OPEN`, `GATE_2B=OPEN`**.

## What changed relative to Step 33f

Step33f proved the exact mixed radial Hamiltonian bracket on one primary-constraint submanifold where the spatial 3-geometries were flat, dust clocks comoving, and each radial momentum constraint vanished separately. There only K00 survived.

Step33g gives a **second explicit *exact* nonhomogeneous primary-surface family** in which (a) BOTH spatial 3-geometries are curved and generally different, (b) BOTH dust phase gradients are nonzero and distinct, (c) the relative Hassan–Rosen shift `z(r)` is nonzero, and (d) the separate radial momentum densities are nonzero but cancel in the diagonal momentum constraint.

It then independently calculates the nine local coefficients of the **mixed** canonical bracket using functional derivatives of the complete positive-EH spherical ADM + five-beta HR + TWO canonical dust constraints, with correct curvature boundary integrations by parts. The nonzero derivative coefficients on primary data expose exactly why it was necessary not to extrapolate the flat `K00` formula to the general case.

**Important:** these are *canonical initial data obeying the constraints*, not an evolved, inhomogeneous cosmological solution. This audit does not prove the universal local Boulware–Deser secondary, time preservation or lapse fixing.

## Algebraic construction of primary-satisfying curved moving-dust initial data

For `r>0`, positive `a,b`, two small independent curvatures `c_g,c_f`, choose

```text
u_g(r)=1+c_g r², u_f(r)=1+c_f r²,
L_g=a u_g²,   S_g=a r u_g²,
L_f=b u_f²,   S_f=b r u_f².
theta_g'(r)=k_g r L_g,   theta_f'(r)=k_f r L_f,
z(r)=z_1 r,  |z|<1.
```

Both dust phase gradients are regular (odd in `r`) and independently specified; their clock potentials, defined by integration, are regular and even. The spatial scalar curvature of each conformal 3-slice is exactly

```text
R3_i = -(8/[a_i² u_i^5]) [u_i''+2u_i'/r]
```

and agrees with the original spherical curvature formula `2/S² [1-(S'/L)²-2(S/L)(S'/L)']`. Thus neither sector is assumed spatially flat. Independent smooth momentum profiles are chosen by integrating `pL_i'=2r[u_i+2r u_i'] P_i(r)` with independent `P_g(r),P_f(r)`.

With `ell=S_f/S_g`, the HR relative-shift coefficient and root are

```text
A_tau= beta1*S_g² + 2*beta2*S_g*S_f + beta3*S_f²,
K=m² M_g² L_g L_f A_tau,
D_*(r)=K(r) z(r)/sqrt(1-z(r)²).
```

Impose `D_g=D_*`, `D_f=-D_*` (hence `D_diag=0`), **without setting either momentum or dust gradient to zero**. Solve for the true canonical metric radial momenta

```text
pS_g=(D_* + L_g pL_g' - p_g theta_g')/S_g',
pS_f=(-D_* + L_f pL_f' - p_f theta_f')/S_f'.
```

Substituting these into the ORIGINAL two lapse Hamiltonians

```text
H_g=C_EH,g+p_g sqrt(1+theta_g'²/L_g²)+z D_*/L_g+W_g,
H_f=C_EH,f+p_f sqrt(1+theta_f'²/L_f²)+z D_*/L_f+W_f,
C_EH,i=L_i pL_i²/(4M_i² S_i²)-pL_i pS_i/(2M_i² S_i)
       -(M_i²/2)L_i S_i² R3_i,
```

leaves **two separate scalar equations linear in `p_g` and `p_f`**. The code solves them analytically, without clipping or taking absolute values. This construction ensures `H_g=H_f=D_diag=F_z=0` identically wherever `p_g,p_f>0`, `S_g',S_f'` and `K` are regular. It uses the same five-beta principal-root potential as earlier steps.

At the dust-only Candidate-C control point `a=.4`, `b/a=.5787707228025044`, with `c_g=.015`, `c_f=-.012`, `z_1=.04`, `k_g=.012`, `k_f=-.016`, and two distinct nonconstant gravitational momenta, the 11-point radial sample `r∈[.12,.88]` satisfies:

- `max |(H_g,H_f,D_diag,F_z)| ≈ 2.8×10^-16` (direct analytic source evaluation);
- `p_g>0` and `p_f>0` on the entire tested interval; both spatial curvatures and both matter gradients are nonzero;
- `D_g=-D_f` is nonzero, and `z(r)` is nonzero.

The independent tests also rebuild the **original, unsimplified** gravitational ADM constraints, their curvature, radial momenta, both matter square-root Hamiltonians, and the HR 2×2 principal-square-root metric potential. All primary constraints are checked *after* that independent reconstruction. A deliberately oversized spatial curvature caused an actually **negative** f-dust density and was rejected rather than hidden: this fixes the admissible parameter neighborhood honestly. The curved construction reduces to Step33f's exact dust source formula as `c_i,k_i,z_1 →0`.

## Mixed local bracket *on* these curved/moving constrained initial data

The extra source `hr_curved_primary_mixed_kernel.py` independently constructs symbolic canonical Euler partials of the radially integrated-by-parts Hamiltonian densities. As Step33e, 3-curvature is integrated by parts so lapse jets `N,N'`, `M,M'` are retained. The six canonical pairs are

`(L_g,pL_g),(S_g,pS_g),(theta_g,p_g),(L_f,pL_f),(S_f,pS_f),(theta_f,p_f)`.

The local mixed bracket can be expanded before further IBP as

```text
{H_g[N],H_f[M]}=integral dr sum_{i,j=0}² K_ij N^(i) M^(j).
```

Analytic `∂F/∂q`, `∂F/∂q'` are differentiated symbolically and the radial total derivative in the Euler functional derivative is evaluated through complex step on the *curved, noncomoving* fields and their exact derivatives. At `r=.43` on the primary surface:

```text
K_00 ≈ +0.4111349651, K_01 ≈ -0.0089443716,
K_10 ≈ +0.1149851368, K_11 = K_20 ≈ +0.0260995945.
K_02=K_12=K_21=K_22=0.
```

These are off-evolution *dimensionless numerical regression coefficients* of the mixed bracket, NOT physical propagation coefficients. Contrary to the Step33f flat/comoving subfamily, derivative-of-lapse terms do not individually vanish. Yet on this constrained curved witness the mixed differential coefficients satisfy (to radial differentiation precision)

```text
K_20=K_11,
K_01-K_10+(K_20)'=0.
```

For compact N,M, integrate by parts:

```text
∫dr [K_20 N'' M + K_11 N'M'] = -∫dr K_20' N'M,
∫dr [K_10-K_20'] N'M = -∫dr N [(K_10-K_20')' M
                                       +(K_10-K_20') M'].
```

The coefficient of `N M'` therefore cancels *on this primary-surface witness*, leaving the **necessary local scalar secondary candidate**

```text
C_local = K_00 - (K_01)'   [on the tested curved/moving primary family].
```

At the sample point it is approximately `+0.47`, different from the raw `K_00≈0.411`. Neglecting smearing derivatives would give the wrong local candidate. A separate special-case test reduces all curved/moving gradients to zero and reproduces the **previous independent Step33f analytical** `K00=(m²Mg²a²/2)J r²(3X+rX')`, with every other Kij zero.

The **nonzero** local candidate means the current test initial data, while satisfying all primaries, *do not satisfy the prospective secondary*. The next test is to find initial data satisfying **both** the primary surface and local secondary, then calculate its **Dirac time preservation and lapse fixing**. Nothing here proves that universal closure is valid off the restricted family, or that the BD degree of freedom has been removed.

## Testing and actual resource limitations

- `numerics/hr_curved_moving_dust_primary.py` — exact analytic genuinely curved/noncomoving primary-satisfying data generator.
- `numerics/hr_curved_primary_mixed_kernel.py` — exact partial symbolic/complex-step local Poisson kernel, with six canonical pairs.
- `tests/test_hr_curved_moving_dust_primary.py` — 21 independent positive and negative numerical tests, including direct original metric principal root.
- `tests/test_hr_curved_primary_mixed_kernel.py` — 3 local Poisson/IBP derivative-coefficient regressions.
- `tests/test_hr_curved_flat_reference.py` — 1 independent Step33f flat/comoving closed-form Poisson limit regression.
- `scripts/verify_gate2b_step33g.py` — execute separately as `primary` (21+1 tests) and `bracket` (3 expensive tests). Every test module runs in a fresh subprocess; each invocation writes a separate JSON with SHA-256 and Git blob provenance.

The complete collection **did NOT finish within timeout when evaluated as one Pytest process or as one top-level runner invocation**, because successive symbolic expressions exceeded this hosted environment's processing budget. Neither failure is reported as a physics error. Final reproducible arrangement:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step33g.py primary gate2b-step33g-primary-report.json
# SUCCESS: 21 original primary + 1 flat reference = 22 tests, two fresh workers

PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step33g.py bracket gate2b-step33g-bracket-report.json
# SUCCESS: 3 symbolic kernel tests in one fresh worker (which internally
# uses one separate subprocess to compute the three expensive radial kernels)
```

**Both top-level invocations independently returned exit code 0.** The total is **25 tests across two independently verified runs**, NOT a single completed 25-test run; the prior Step33f 52 tests were not rerun. This preserves the original equations while avoiding misleading timeout claims. This is **not** a complete Git worktree test, no CI, and the older Step33f 52 tests were not rerun in this workspace.

The new local Poisson code independently reproduces the old Step33f analytic flat/comoving limit, which reduces self-consistency-only checking. But the curved local scalar candidate has **not** been checked via a full independent non-IBP radial functional variation of the original action on this new exact curved primary family; that is another explicit required validation before a general BD secondary is published.

## Next exact research gates

1. Reproduce the new local curved/moving bracket via **independent numerical variations of the ORIGINAL, non-IBP spherical EH+HR+two-dust action** with arbitrary compact lapse smearing functions. Confirm `K_01-K_10+K_20'=0` beyond the one explicit primary family, on radial geometry with varying angular eigenvalue and dust currents.
2. Find a primary+secondary-satisfying family, then evaluate **time preservation**, Poisson matrix rank, and radial lapse-fixing equations with two independent dust pairs. Handle `K(r)=0`, `J(ell)=0`, dust positivity and boundary conditions separately. Do not elevate a necessary local scalar to a proven HR-BD secondary without this Dirac test.
3. Connect the full local result to Step32e's coherent time-integrable perturbation action, independently solve a genuinely physically nonhomothetic on-shell g/f+dust background rather than passive coordinate compensation, and pass both *same-reduced-action* De Felice finite-H `mu→0` and nonlinear homothetic Aoki `K_S,c_S²` stable/unstable controls before Candidate-C relative `mu` fold at `a≈.0301646`.

**Verdict: new generality of primary-satisfying initial data and necessary mixed-bracket cancellation verified; general local BD constraint, its secondary preservation, physical scalar stability and JANUS-R cosmology remain UNPROVEN. `GATE_2B=OPEN`.**
