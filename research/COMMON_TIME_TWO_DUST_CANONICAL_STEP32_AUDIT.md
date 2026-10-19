# JANUS Gate 2B — Step 32: exact common-time two-dust canonical bridge, before metric/BD reduction

**Date:** 2026-10-19. **Research branch:** `research/gate2b-nonhomothetic-transfer`.

**Verdict:** `TWO_INDEPENDENT_DUST_CANONICAL_PAIRS=GREEN` in the same five-sector, common-time compact trial action on the *homogeneous radiation-free Candidate-C on-shell background*. `FULL_METRIC_VELOCITY_AND_BD_REDUCTION=OPEN`; `GENUINE_NONHOMOTHETIC_ONSHELL_BACKGROUND=OPEN`; **`GATE_2B=OPEN`**. No physical scalar ghost, speed, nonlinear transition or CMB verdict.

## Problem and result

Step 31 constructed one common-chart positive-Einstein–Hilbert g/f + all-beta Hassan–Rosen + two *covariant* irrotational dust compact spacetime action and independently showed all 12 on-shell compact field tadpoles vanish. However, an explicit physical canonical reduction cannot proceed safely while the two dust momenta remain hidden behind multiplier fields. Step 32 carries out the **exact local Legendre transformation** for each dust in ADM variables derived from the **same** Step 31 spherical metrics. The dust multipliers are eliminated *after* Legendre transformation, and the phase velocities and canonical momenta of both dusts are retained explicitly.

The 14-amplitude action is genuine five-sector common-time EH_g+EH_f+HR+two reduced dust phase-space, with all EH/HR metric profiles and quadrature/normalizations unchanged from Step 31. The original 12 compact field directions (8 metric scalars plus two dust phases plus two dust momenta) still have vanishing first variations on the homogeneous Candidate-C trajectory. Two additional independent local phase-time-rate jet amplitudes are used to audit the symplectic structure. **The phase-rate jets are NOT independently admissible compact field variations and have nonzero first derivatives.** This is expected for a first-order phase-space action, not a failed on-shell solution.

## Exact matter Legendre transform, both signs and density factors verified

For each native/common-time sector, from the exact spherical ADM metric:

- `N = sqrt(-g_tt + g_tr^2/g_rr)`;
- `N^r=g_tr/g_rr`, `gamma_rr=g_rr`, `sqrt(gamma)=sqrt(g_rr)*g_angular` per solid angle;
- irrotational dust phase `theta` and positive density multiplier `rho`.

The original covariant matter density is

\[
\mathcal L_{\rm dust}=\frac{\sqrt\gamma\rho}{2N}
 [ (\dot\theta-N^r\theta_r)^2-N^2(1+\theta_r^2/\gamma_{rr})].
\]

Its exact canonical momentum and Hamiltonian density are

\[
 p=\frac{\sqrt\gamma\rho}{N}(\dot\theta-N^r\theta_r),\qquad
 \mathcal H_\rho=N\left[\frac{p^2}{2\sqrt\gamma\rho}
 +\frac{\sqrt\gamma\rho}{2}(1+\theta_r^2/\gamma_{rr})\right]
 +N^r p\theta_r.
\]

**Independent off-shell check:** evaluate the *nonzero* Step 31 covariant dust Lagrangian for arbitrary nonzero scalar metric, phase, and density perturbations in both sectors. Substitute the independently calculated momentum into `p*theta_dot-H_rho`; the equality holds to ~`1e-17` at explicit nonzero test samples. Never evaluate the normalized covariant dust clock **before** taking the original lapse derivative: that would erase its dust Friedmann source (Step 28 regression).

At fixed positive p, the multiplier stationary point is

\[
 \rho_* = \frac{p}{\sqrt\gamma\sqrt{1+\theta_r^2/\gamma_{rr}}},
 \qquad \mathcal H_{\rm red}
 = N p\sqrt{1+\theta_r^2/\gamma_{rr}} + N^r p\theta_r.
\]

The canonical action is exactly

\[
 \mathcal L_{\rm red}= p\dot\theta -N p\sqrt{1+\theta_r^2/\gamma_{rr}}-N^r p\theta_r.
\]

**Important constraint-interface fact:** in true ADM variables and with fixed p, phase gradient and spatial metric, this Hamiltonian is **affine in lapse N and radial shift N^r**. Its second derivatives with respect to those ADM auxiliaries vanish identically. This does **NOT** mean the EH+HR+matter lapse/shift constraints, or the physical BD-null constraint, have already been solved. The existing Step 31 variables `Phi` and `U` are nonlinear functions of ADM N and N^r; do not confuse their Hessians.

## Same-action 14-variable compact trial jet and results

Ordering, seven per sector:

`(Phi_g,U_g,psi_g,E_g,theta_g,p_g,theta_rate_g, Phi_f,U_f,psi_f,E_f,theta_f,p_f,theta_rate_f)`.

Each dust momentum density per unit angular solid angle is

\[
 p_g=C_g r^2[1+\delta p_g T(t)F(r)], \quad
 p_f=C_f r^2[1+\delta p_f T(t)F(r)],
\]

and phase rate is `theta_dot = N_background + theta_amp * d_t(TF) + theta_rate_amp * TF`, while `theta_r = theta_amp * d_r(TF)`. The two **rate amplitudes** are separate local jets for testing the canonical symplectic structure, not additional dynamical propagating fields.

The exact off-shell phase-momentum-rate mixed second derivatives follow directly from `p*theta_dot`:

\[
 H_{p_i,\dot\theta_j}^{\rm compact}
 =\delta_{ij}4\pi C_i\int dt\,dr\, r^2[T(t)F(r)]^2.
\]

Numerically, at time support `0.027`, radial support `0.32`, quadrature 20–28:

```
H[p_g,theta_rate_g] = +9.45033909e-05
H[p_f,theta_rate_f] = +1.30339270e-05
H[p_g,theta_rate_f] = 0
H[p_f,theta_rate_g] = 0
canonical pair block rank = 2
max absolute derivative of twelve legitimate compact field directions ≈ 3.73e-12
```

A complete **14×14 compact space-time preconstraint Hessian** was also actually evaluated by finite differences of the common five-sector action. Its two phase-rate rows are zero except for their own respective positive dust momentum couplings (within ~`4e-12`). The momentum–momentum and rate–rate second-derivative blocks vanish in this reduced first-order dust representation, and the old mixed HR metric coefficient remains nonzero:

`H[Phi_g,psi_f] ≈ −0.0001842360821`; setting the HR interaction mass to zero removes this cross-metric coefficient but breaks both lapse first variations on the original on-shell background. These are **preconstraint compact profile coefficients**, not physical kinetic eigenvalues, ghost diagnostics or mode dispersion relations.

## Reproducibility and RED→GREEN record

New files:

- `numerics/hr_two_dust_common_time_canonical.py` — exact ADM extraction, off-shell covariant↔canonical Legendre identity, multiplier stationarity, reduced canonical 14-amplitude action, 2×2 analytic/finite-difference symplectic block and full 14×14 preconstraint compact Hessian.
- `tests/test_hr_two_dust_common_time_canonical.py` — **20 new independent focused tests** (local exact Legendre, nonzero covariant dust, multiplier stationary check, ADM lapse/shift linearity, Step31 common-action baseline, 12 valid on-shell tadpoles, two independent canonical pair coefficients/rank, quadrature, analytic normalization, f/g no mixing, preconstraint 14×14 sparse rate rows and refinement, interaction cross, negative controls/domain checks).
- `scripts/verify_gate2b_step32.py` — exact-source SHA-256 manifest, local focused 29+20 test run and explicit unfinished physics flags.

Actual tested workspace `/mnt/data/janus32` uses the **exact Git blob bytes** of the two Step 31 original modules (source and tests):

```
numerics/hr_full_onshell_tadpole.py  e05d8f54cf4eff76a92c278ffdd971612d1ec56b
tests/test_hr_full_onshell_tadpole.py 68fb2302ae57c350db087ea3caf5898ca31661af
```

Both are identical to live GitHub Step31 files. The new tests initially failed in **two controls**, not in the Legendre formulas: (i) an excessively large off-shell phase amplitude on a narrow time bump produced a **negative p**, outside the explicitly chosen positive-p dust branch; the amplitude was reduced to keep p>0; (ii) a new test omitted the import of the known HR mass constant `M2`. Both were repaired and the exact off-shell sign/branch domain preserved. No physical equation was changed to force a pass.

Actual unified focused run:

```bash
cd /mnt/data/janus32
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests
# 49 passed (29 exact Step31 + 20 new Step32)

OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step32.py gate2b-step32-report.json
# expected gate2b OPEN, two canonical pairs GREEN; no De Felice/Aoki
```

This IS an actual **combined** Step31+Step32 run with byte-exact Step31 inputs, unlike earlier disjoint workspace totals. However it is NOT a clean clone of the whole repository, full GitHub test suite, CI run or independent peer replication. The new files should be pushed and GitHub SHA checked against local `git hash-object`, and this audit/restart updated before claiming persisted success.

## The hard RED still ahead

1. **Metric velocities absent as independent jets:** the Step31 spatial trace/shear temporal derivatives are linked to the chosen compact profiles, rather than independently varied `psi_dot_g,E_dot_g,psi_dot_f,E_dot_f`. Add all four independent metric velocities and a common time-supported action, verify the EH+HR+dust metric rate operator and lapse/shift ADM basis constraints. Neither the 14×14 Hessian nor the two-pair symplectic rank is the physical scalar kinetic rank.
2. Identify and solve all true scalar metric lapse/radial-shift auxiliaries, respecting the diagonal diffeomorphism Ward identity **after imposing on-shell field equations**, and the time-dependent HR Boulware–Deser null/canonical constraint; preserve BOTH `(theta_i,p_i)` pairs through reduction.
3. In parallel, solve the full radial/time background Einstein+HR+two-matter equations for an independently **genuinely nonhomothetic** on-shell Candidate-C branch. The present background remains homogeneous and merely admits passive f chart relabelling. The dust-only radiation-free restriction remains explicit.
4. Only from ONE complete physical reduced action reproduce BOTH independent finite-H `mu→0` De Felice scalar and nonlinear homothetic Aoki `K_S,c_S²` stable/unstable oracles. Only if they pass approach the first relative-mu fold `a≈0.0301646`. No observational/CMB viability claim before that.

**Bottom line:** the exact two-dust canonical first-order interface and the coherent 14-amplitude preconstraint action are verifiably reproducible on the homogeneous on-shell benchmark. **`GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`.**
