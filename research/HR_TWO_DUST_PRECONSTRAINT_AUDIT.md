# Gate 2B — finite-mu HR + two canonical dust phase pairs (preconstraint)

**Date:** 2026-10-18
**Active branch:** `research/gate2b-nonhomothetic-transfer`
**Status:** `HR_PLUS_TWO_DUST_PRECONSTRAINT=GREEN_AS_PARTIAL_ACTION`; `FULL_EH_HR_DUST=OPEN`; `GATE_2B=OPEN`.

## Question, relevance and scope

The preceding calculations produced a finite-mu, regular-radial **interaction-only** 16-amplitude Hessian, including the full f-native field-sampling inverse Jacobian, and a separate compact spacetime beta4 Ward check. Gate 2B still lacked a controlled matter interface for the actual two dust phase pairs.

This audit connects the **existing** 16-amplitude finite-mu HR interaction to both canonical dust phase pairs, without pretending to have completed Einstein–Hilbert, the time-domain constraint reduction, or the on-shell Candidate-C background. It ensures that neither matter momentum is mistakenly discarded as a static metric auxiliary.

New files:

- `numerics/hr_two_dust_preconstraint.py`
- `tests/test_hr_two_dust_preconstraint.py`

The source is a dimensionless model/audit kernel with independent positive native `rho_g,rho_f` parameters. It is **not** a calibrated cosmological model and does not compute an observable.

## Background chart and phase transformation

Work on a fixed common-time slice of a prescribed non-homothetic background:

```text
T=t+sigma(t)r²/2,
R_f=(1+mu(t))r,
J=d(T,R_f)/d(t,r)
 = [[1+sigma_dot r²/2, sigma r],
    [mu_dot r,        1+mu]],
D=det(J)>0.
```

Use a smooth compact regular scalar profile `F(r)=(1-r²/Rmax²)^4` inside the support. Under the previously established pre-BD phase coordinate transformation, use the **first-order ansatz**

```text
q_g(t,r) = Y_g(t) F(r),
q_f(t,r) = [Y_f(t)-T_amp(t)] F(r).
```

Here `T_amp` is the perturbation of the time chart, **not** the background f time `T`. Its derivative gives the `Y_f_dot - T_amp_dot` combination. The phase variables are normalized as in the previously developed local canonical dust action. The full time-dependent background normalization of this ansatz has **not** yet been tested against an on-shell evolving f fluid; the ansatz must be rechecked during full spacetime assembly.

The native f phase derivatives are computed using `J^{-T}`:

```text
q_T = [(1+mu) q_t-mu_dot*r q_r]/D,
q_R = [-sigma*r q_t+(1+sigma_dot*r²/2) q_r]/D.
```

The native phase p_g and p_f are **independent canonical momenta**. They are not Schur-eliminated.

## Dust action and normalization

The existing pressureless phase action's native spherical density (excluding the angular dOmega, including native `r_native²`) is

```text
L_dust = n a³ r_native² {
  p [q_T + lambda q-Phi]
  +rho Phi²/2
  -(n² rho)/(2a²) [q_R+(a/n)U]²
}.
```

The g background uses `(N,a,r)`; the f background uses `(n,alpha,R_f)` and the additional chart determinant `D`. The radial metric shift ansatz is `U=B_amp F'(r)`. The construction is a quadratic local phase action; all linear background tadpoles and the on-shell matter conservation laws must ultimately be checked in the full action.

The spatial integral is **exactly one** angular factor:

```text
S = 4*pi integral_0^Rmax r² [density per spherical volume] dr.
```

### Witnessed RED-to-GREEN error: duplicated 4*pi

The independent canonical normalization test initially gave `H[p_g,Y_gdot]=0.01916002623` versus the correct `0.00152470644`, precisely an extra factor `4*pi`. In the initial new code the native dust density already had 4*pi while quadrature weights also supplied it. Removing the duplicated factor **in both sectors** restores agreement with direct integration.

This was a new implementation error found by a nontrivial physical-normalization regression, not a revision of the existing dust or HR physics.

## 22x22 preconstraint trial Hessian

The integrated HR interaction uses **16 trial arguments**:

```text
(Phi_g,B_g,psi_g,E_g, Phi_f,B_f,psi_f,E_f,
 T_amp,L_amp,T_amp_dot,L_amp_dot,
 Phi_f_dot,B_f_dot,psi_f_dot,E_f_dot).
```

Add six **dust phase arguments**:

```text
(Y_g,p_g,Y_f,p_f,Y_g_dot,Y_f_dot).
```

The result is a symmetric **22x22 partial-action Hessian** before metric constraints. Its dimension is a trial amplitude/rate count and **must not** be confused with 22 independent physical degrees of freedom. The first 16x16 block is the validated HR interaction and the dust block adds the two canonical pairs; the same time-dependent physical constraints still need to be imposed.

The momentum-rate pairs have exact analytic normalization

```text
C_g = H[p_g,Y_g_dot] = 4*pi*N*a³ * integral_0^Rmax r² F² dr,
C_f = H[p_f,Y_f_dot] = 4*pi*n*alpha³*(1+mu)^3
                           * integral_0^Rmax r² F² dr,
H[p_f,T_amp_dot] = -C_f.
```

The `D` in the f measure cancels `1/D` in its **native-time derivative**, giving the exact cubic factor `(1+mu)^3`. For the dimensionless diagnostic point (Rmax=.23, N=1.03, a=.85, n=1.16, alpha=.74, mu=-.24),

```text
C_g = +0.001524706442287953,
C_f = +0.000497377527077860,
H[p_f,T_amp_dot] = -0.000497377527077860.
```

The canonical p_g–p_f to (Y_g_dot,Y_f_dot) submatrix has rank 2. The `Y_f=T_amp` and `Y_f_dot=T_amp_dot` configuration leaves the f matter phase invariant/zero in this quadratic ansatz, as required.

## Important further finding: tilted f foliation creates a rate-square term

The f-native **spatial** derivative also mixes with the common-time rate:

```text
q_R=(-sigma*r*q_t+T_t*q_r)/D.
```

Consequently the spatial gradient term generates a quadratic term in the common-time fluid phase rate even though the native dust phase Lagrangian is first order in `q_T`:

```text
H[Y_f_dot,Y_f_dot] =
 -4*pi*n³*alpha*rho_f*(1+mu)^2
 * integral_0^Rmax dr r² (sigma*r)^2 F(r)^2 / D(r).
```

For the diagnostic: `H[Y_f_dot,Y_f_dot]=-6.14038736657e-8`.

This term is exactly reproduced by an independently integrated formula and vanishes when `sigma=0`. It is **not** valid to delete it to enforce an artificial canonical-looking matrix on common-time slices; nor is its isolated negative sign proof of a physical ghost. The kinetic and constraint classification requires the full EH+HR+dust reduction in a consistent time slicing.

## Verification

The two new files were checked **byte-for-byte by git hash-object** against GitHub blobs:

- `numerics/hr_two_dust_preconstraint.py`: `bbb23d13543c1de5331bedbd5d34ce66a7c1740e`
- `tests/test_hr_two_dust_preconstraint.py`: `97d04cf9a5ef64fb127a41177e6e36902b971fda`

Local reconstructed workspace `/mnt/data/janus-check`, with exact existing relevant HR source files previously matched to GitHub:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_two_dust_preconstraint.py
# 10 passed
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
# 37 passed
```

The ten new tests include independent direct scalar dust density quadrature versus the 22x22 quadratic matrix, canonical normalization in each sector, determinant/positivity guards, finite-quadrature convergence, phase cancellation, exact tilted-rate-square integral, momentum-pair rank and additivity with the existing HR interaction Hessian.

**Limitation:** 37 tests are from the limited reconstructed workspace, not the full GitHub repository. GitHub Actions remain disabled; no clean full-branch run or external independent review is claimed.

## Remaining blockers and publication gate

1. **Einstein–Hilbert missing from THIS shared 22-variable action**: the separately validated EH compact calculators have different gauge/time/profile conventions. They cannot merely be pasted into this matrix without a consistent native-to-common metric map, background derivative/boundary terms and unperturbed volume factors.
2. **Time integration missing**: this is a time-local quadrature of a finite radial trial basis, not the time-domain Euler–Lagrange or canonical system. Its coefficient derivatives and mixed rate integrations by parts still need implementation.
3. **On-shell background/matter normalization missing**: `sigma,mu,n,alpha,lambda_g,lambda_f` were independent numerical audit inputs. They must be obtained consistently from the same Candidate-C solution.
4. **Metric auxiliaries and BD null coordinate not eliminated**: the 22x22 eigenvalues cannot be interpreted as physical ghost or gradient signs.
5. **Physical acceptance oracles not passed** on the same action: finite-H `mu->0` Candidate-C De Felice spectrum, and homothetic nonlinear Aoki `K_S,c_S²`.
6. **No fold or observational result** until all previous gates succeed.

**Next exact RED:** implement a unified native spherical EH term on the SAME compact spatial profile and time-supported chart, with four lapse/shift metric constraints. Audit its variation under the f-native chart, include EH in this partial action, then perform time-dependent constraint elimination while retaining p_g and p_f. Do not infer physical stability from the present partial Hessian.

**Scientific verdict:** `HR_TWO_DUST_PHASE_GATE=GREEN_AT_PARTIAL_ACTION_LEVEL`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`.
