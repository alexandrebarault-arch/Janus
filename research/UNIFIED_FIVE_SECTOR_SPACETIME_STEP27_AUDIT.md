# JANUS Gate 2B — Step 27: one five-sector, native-consistent spacetime action

**Research branch:** `research/gate2b-nonhomothetic-transfer`  
**Date:** 2026-10-18  
**Verdict:** `ONE_FIVE_SECTOR_OFFSHELL_SPACETIME_ACTION=GREEN_AS_CONSISTENCY_TEST`; `PHYSICAL_ONSHELL_SCALAR_ACTION=OPEN`; **`GATE_2B=OPEN`**.

## Scientific advance and exact scope

The previous Step 26 controlled the coupled **Hassan–Rosen** potential, and Step 25 separately controlled the f Einstein–Hilbert (EH) coordinate Ward. The previous matter interface instead used frozen-time, radially projected **canonical dust phase pairs**. These did NOT yet constitute one fully shared five-term spacetime action.

This step constructs an explicit **native-consistent, nonlinear time-and-radius spacetime integral** with five simultaneous sectors on identical metric functions and the same positive, orientation-preserving nonhomothetic background chart:

1. Positive-sign native Einstein–Hilbert **g** ADM + GHY representative;
2. Positive-sign native Einstein–Hilbert **f** ADM + GHY representative;
3. The exact spherical principal-square-root Hassan–Rosen interaction including **all beta0..beta4**;
4. Irrotational pressureless covariant **g dust**;
5. Irrotational pressureless covariant **f dust**.

**This is a nonlinear off-shell trial action and a kinematic integration/normalization gate; it is NOT the on-shell Candidate-C solution, the complete constrained physical perturbation action, or a stability result.** In particular the native matter action is now a covariant irrotational dust Lagrange-multiplier formulation. It is **not yet proved equivalent on the common time-dependent bimetric perturbation basis** to the previously developed finite-radius canonical dust kernel. That conversion remains a precise RED task.

## Single native metric and five action pieces

In either native (time, radius) sector, choose scalar lapse `Phi`, radial shift `U`, spatial trace `psi` and shear `E`:

```text
metric_00 = -n(T)^2 [1+2 Phi(T,R)]
metric_0R = n(T) a(T) U(T,R)
metric_RR = a(T)^2 Qr(T,R)
metric_Omega = a(T)^2 R^2 Qt(T,R)
Qr = 1+2psi-(2/3)k^2 E
Qt = 1+2psi+(1/3)k^2 E.
```

The exact same source of `n,a,Phi,U,psi,E,Qr,Qt` is used by the EH, HR **and dust** densities. Trial amplitudes use polynomial radial functions with proper center parity (`U=O(R)`, `E=O(R^2)`). Both sector backgrounds are smooth positive polynomials. Their choice here is for numeric falsification only; they are NOT derived from the JANUS Friedmann equations. The homogeneous dust background satisfies native continuity `rho_0 a^3=constant`, and its proper-time clock obeys `theta_0,T=n(T)`.

For a native spherical metric, define

```text
N = n sqrt(1+2Phi+U^2/Qr),
L = a sqrt(Qr), S = a R sqrt(Qt),
N^R = metric_0R / metric_RR,
W = S_R/L,
R(3) = 2/S^2 [1-W^2-2(S/L) W_R].
```

Let `Kr,Kt` be the exact radial/angle ADM extrinsic curvature eigenvalues from the previous independently audited six-scalar geometry; they are evaluated with *this* native metric and its native time/radius derivatives. Then

```text
L_EH = (M^2/2) N L S^2 [ R(3)-4 Kr Kt-2 Kt^2 ].
```

The covariant irrotational dust Lagrange-multiplier density is

```text
L_dust = -rho/2 * sqrt(-det metric_2x2) * metric_Omega
               * (metric^(AB) theta_A theta_B + 1).
```

Its `rho` variation enforces the future timelike dust clock `metric^(AB) theta_A theta_B=-1`; the dust sector is not a scalar-field potential with invented sound speed. The background `rho_0~a^{-3}` and `theta_0,T=n` satisfy the *separate homogeneous dust conservation/norm requirements*, but the full EH+HR background equations are not imposed.

The exact nonlinear HR density uses the same two native metrics pulled into common `(t,r)` coordinates and the exact spherical 2x2 principal root `e0..e4`, as in Step 26. In this Step 27 code **it is compared directly against the independent pre-existing full HR spacetime integral**, not recalibrated to agree by rescaling.

## Canonical dust Legendre identity: both pairs retained

A second new module independently checks the exact local native ADM Legendre transform. With `gamma=sqrt(gamma_RR)*metric_Omega` (the native spherical spatial measure per `dR dOmega`), shift `N^R`, lapse `N`, and `theta_R`, the covariant dust density equals

```text
L = gamma*rho/(2N) (theta_T - N^R theta_R)^2
        -N*gamma*rho/2 [1+theta_R^2/gamma_RR].

p_theta = (gamma*rho/N) (theta_T-N^R theta_R).

H = N [p_theta^2/(2 gamma rho)
              + gamma rho (1+theta_R^2/gamma_RR)/2]
                  +N^R p_theta theta_R.
```

For future-oriented `p_theta>0`, the algebraic multiplier constraint gives

```text
rho = p_theta / [gamma sqrt(1+theta_R^2/gamma_RR)],
H_reduced = N p_theta sqrt(1+theta_R^2/gamma_RR)
                  + N^R p_theta theta_R.
```

These identities hold independently for `g` and `f`, and the native `dp_theta/d(theta_T)` block is strictly positive and rank 2 across the two sectors. **This is a native local Legendre identity**, NOT the full common-time nonhomothetic canonical transformation with its extra metric/dust constraints. Tests explicitly check that the reduced Hamiltonian is **not** accidentally used away from the density stationary surface.

## Finite native/common spacetime charts and the coupled Ward test

The background is the same time-dependent nonhomothetic chart audited in Step 26:

```text
T=t+sigma(t) r^2/2,
R=(1+mu(t))r,
sigma=.08+.025t, mu=-.22+.05t.
```

Under a **diagonal** compact diffeomorphism of both sectors, native `g` and `f` are pulled back with their full metric Jacobians, and each EH and dust native density is transformed using its own positive native coordinate Jacobian exactly once. The HR term is evaluated on the two common pulled-back metrics. Each of the five separately integrated actions is invariant to quadrature roundoff. Under an **f-only native relative** deformation, `EH_f` and `dust_f` separately remain invariant, `EH_g` and `dust_g` are untouched, but the relative HR interaction changes. This is an off-shell coordinate-change theorem; it does not by itself establish any physical BD constraint.

Illustrative **dimensionless off-shell** values at 48-point quadrature and with the native amplitudes declared in the new source:

| Term | Native-consistent integrated action |
|---|---:|
| EH g | -0.10131100236021987 |
| EH f | -0.05093461223765551 |
| HR interaction | -0.828909268886016 |
| Dust g | -0.00443399410472282 |
| Dust f | +0.00235385235601038 |
| Total | -0.9832350252326039 |

With common compact deformation `(+0.035,-0.023)`, **each of five differences** is `|delta S_i|<6e-17`. With a *relative f-native* deformation `(+0.035,-0.023)`, the relative action difference is `-1.00718622362e-5`, **entirely** due to HR; the other four sectors' changes are at numerical noise level. Setting `m^2=0` identically removes the HR term while retaining nonzero both EH and both dust contributions.

### Independent mathematical controls

- At several spacetime points and for nonzero metric amplitudes, the exact four native spherical metric components in the new five-sector action agree componentwise with the **older Step-26 HR native metric generator**; this cross-check establishes actual common source geometry.
- The entire new HR term (for diagonal and f-relative finite charts) agrees with `0.7` times the older *independently committed HR spacetime action*, because the new independent control chooses `hr_mass2=0.7`. No additional angular/radial Jacobian or f lapse normalization was introduced.
- In the `psi=E=0` restriction, both EH native densities reproduce the **pre-existing exact flat spherical ADM EH primitive** at nontrivial lapse and radial shift amplitudes.
- On zero perturbations, both dust sectors have `rho_0 a^3=constant`, properly normalized native clocks and identically vanishing background dust Lagrangian density; metric variation still sources matter and the full background is **off shell**.
- Both dust sectors pass independent exact Legendre `p_theta theta_T - H = L` and density-constraint tests. Dropping matter density constraints or identifying their momenta would be invalid.
- Numerical radial/time quadrature convergence, invalid branch/orientation/negative density guards, and a nonzero off-shell g gravitational tadpole have been checked.

## Code, tests, reproducibility

New files:

- `numerics/hr_unified_spacetime_offshell.py`
- `numerics/hr_unified_dust_legendre.py`
- `tests/test_hr_unified_spacetime_offshell.py` (**13 new tests**)
- `tests/test_hr_unified_dust_legendre.py` (**5 new tests**)
- `scripts/verify_gate2b_step27.py` (focused JSON provenance runner).

Actual local focused execution in `/mnt/data/janus-next`:

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests
# 75 passed
OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step27.py checkpoint-27-local.json
# tests_exit_code: 0; tests_passed_count: 75
# workspace_origin: non_git_workspace_reconstruction
# full_repository_regression: false
# physical_stability_oracles: DeFelice=NOT_RUN, Aoki=NOT_RUN
# gate2b: OPEN
```

The **four new scientific source/test files** were transferred from the *executed local files* to the active GitHub branch by reading their exact staged UTF-8 file content, and their Git blob SHAs were verified against `git hash-object` in the local runtime. The Step-27 runner and this audit should likewise have their exact GitHub contents verified in the current commit.

Important: older HR/dust prerequisite files in this local reconstructed workspace still do NOT all have identical Git blob SHA to their GitHub sources, and direct `git clone` is unavailable (DNS). This is **75 targeted local tests**, NOT full clean GitHub checkout regression or independent external reproduction. No GitHub Actions run was performed.

## Explicit next scientific RED gates

1. Replace the illustrative off-shell backgrounds by ONE on-shell Candidate-C trajectory simultaneously satisfying **both Einstein background systems, full HR equations and two independent dust conservation laws**; verify the first variation/tadpoles of the *whole common action* vanish.
2. Make the full perturbative field/rate basis genuinely common and time-supported, including full `f` native sampling, chart perturbation jets and integration-by-parts boundary terms. The present nonlinear spacetime action proves same-metric and diagonal-Ward consistency, **not the physical quadratic scalar Hessian** in the old 24 trial-slot basis.
3. Derive the time-dependent canonical equivalence between this new covariant dust action and the earlier finite-radius two-dust **phase-space** kernel; retain **both** canonical phase pairs during reduction.
4. Eliminate the actual four metric scalar auxiliary constraints and the time-dependent Boulware–Deser null direction. Reproduce the finite-H `mu->0` De Felice physical scalar and homothetic nonlinear Aoki `K_S,c_S^2` oracle **on the same fully reduced action** (stable and unstable roots).
5. ONLY if all these pass, test physical kinetic/gradient regularity at Candidate-C first fold `a≈0.0301646`. If they fail, record an explicit negative research gate. No inferred CMB fit or cosmological validation is justified.

**Conclusion:** an actual common five-density spacetime action and independent native two-dust Legendre consistency are now numerically verified. Their utility is to make a future on-shell constrained calculation precise and falsifiable. `GATE_2B=OPEN`, JANUS-R cosmology **NOT VALIDATED**.
