# JANUS Gate 2B — Step 32e: both dust phase clocks are genuinely time-integrable

**Date:** 2026-10-19  
**Active branch:** `research/gate2b-nonhomothetic-transfer`  
**Positive result:** `SAME_ACTION_ALL_18_COMPACT_FIELDS_INTEGRABLE=GREEN`, `TWO_DUST_PHASE_SPACE_PAIRS_PRESERVED=GREEN`.  
**Open physics:** `TRUE_ADM_LAPSE_SHIFT_CONSTRAINTS=OPEN`, `TIME_DEPENDENT_HR_BD_NULL=OPEN`, `NONHOMOTHETIC_ON_SHELL_BACKGROUND=OPEN`, `DE_FELICE_AND_AOKI_PHYSICAL_ORACLES=NOT_RUN`, **`GATE_2B=OPEN`**.

## 1. Previous precise obstruction

The Step31 common-time, positive-EH g+f, all-beta Hassan–Rosen and **two canonical dust phase-space pairs** action was on shell for the PHYSICALLY HOMOGENEOUS radiation-free Candidate-C background. Step32d corrected four formerly independent metric trace/shear velocity *jets*: it introduced compact parent fields using

\[
T(t)=\left[1-(t/t_*)^2\right]^4,\qquad G(t)=tT(t),\qquad \dot G(t)=T(t)+t\dot T(t),
\]

whose values and derivatives vanish at the temporal boundary. **However** two dust slots, indices `(6,13)` of the prior 18-amplitude action, were still independent `theta_rate` jets:

\[
\delta\theta_i=\eta_i T(t)F(r),\quad
\delta\dot\theta_i=\eta_i\dot T(t)F(r)+\nu_i T(t)F(r).
\]

Such a pair is not the time derivative of any single compact field for general `nu_i`. On the homogeneous on-shell background these two isolated rate-jet first variations were *not* zero; they are not admissible compact field variations. Their previous numeric values, measured in this Step32e workspace at 20×20 quadrature, are

```text
old disconnected dS/d theta_rate_g  = +3.004015815613603e-4
old disconnected dS/d theta_rate_f  = +4.143144750889948e-5
```

These numbers **were never physical tadpoles** and must not be used to reject the background or diagnose the BD constraint.

## 2. Corrected exact common-time phase-space action

Use two independent **actual compact parent fields**:

\[
\delta\theta_i(t,r)=[\eta_i T(t)+\xi_i G(t)]F(r),
\]
\[
\partial_t\delta\theta_i=[\eta_i\dot T(t)+\xi_i\dot G(t)]F(r),\qquad
\partial_r\delta\theta_i=[\eta_i T(t)+\xi_i G(t)]F'(r),
\]

for both `i=g,f`, and retain **independent positive** canonical momenta

\[
p_i(t,r)=C_i r^2[1+\pi_i T(t)F(r)]\,, \quad p_i>0.
\]

The field order stays 18 slots. The two old `theta_rate` labels at indices 6,13 are now **real additional phase-parent** amplitudes `theta_g_extra_tT, theta_f_extra_tT`, not new local rate-only degrees of freedom.

The exact dust multipliers are eliminated **only after performing** the Legendre transform of each original covariant irrotational dust sector, as derived and independently verified in Step32a. On the same nonlinearly perturbed native/common spherical metrics, both first-order dust densities are

\[
\mathcal{L}^{\rm can}_i=p_i\partial_t\theta_i
 -N_i p_i\sqrt{1+\frac{(\partial_r\theta_i)^2}{\gamma_{rr,i}}}
 -N^r_i p_i\partial_r\theta_i.
\]

The complete integrated common-time action still contains exactly the same five contributions:

\[
S=4\pi\int dt\,dr\,\bigl[
\mathcal{L}_{EH,g}+\mathcal{L}_{EH,f}+\mathcal{L}_{HR}
+\mathcal{L}^{\rm can}_g+\mathcal{L}^{\rm can}_f\bigr],
\]

with the same Step32d true parent metric spatial trace/shear fields and their exact derivatives. `hr_integrable_two_dust_phase.action()` recomputes the actual nonlinearly perturbed metric, ADM 3-curvature, ADM extrinsic curvature, all beta0..4 interaction and both canonical matter terms on one common time-and-radius integration domain. Setting the two **new** phase extras to zero reproduces the complete Step32d action exactly, including its other 16 amplitude inputs.

## 3. Genuine integration by parts and projected canonical interface

For a compact phase fluctuation vanishing at both ends of the time interval,

\[
\int dt\,dr\,p\,\partial_t\delta\theta
 =-\int dt\,dr\,(\partial_t p)\,\delta\theta.
\]

The *two sides are computed independently* from the explicit parent fields and finite `\partial_t p`. With nonzero `eta,xi,pi` for the g dust the sampled result is

```text
∫ p δtheta_dot           = +3.5438771600125422e-6
-∫ delta_theta p_dot     = +3.5438771600122983e-6
difference               = +2.439454888092385e-19
```

The same controls pass for the f dust. The background momentum `p_i=C_i r²` is time-independent, so the **first-order** compact dust clock action is a pure boundary term and vanishes as required. In the previous disconnected local-jet construction it did not.

The projected symplectic coefficients are a particularly useful independent identity. Define the old shape projection `p_i` against a *disconnected* `theta_rate_i*T F`:

\[
Q_i=4\pi C_i\int dt\,dr\,r^2 T^2(t)F^2(r).
\]

In the corrected basis the additional phase-parent `G=tT` enters through `G'=T+tT'`. Since `T` vanishes at both time boundaries,

\[
\int T\dot G\,dt
 =\int(T^2+tT\dot T)dt
 =\tfrac12\int T^2dt.
\]

Thus the **projected** `p_amp_i – theta_extra_i` Hessian coefficient is **exactly one half** of its former rate-jet value, a basis-projection effect rather than a change in the fundamental symplectic structure:

```text
                         finite second diff      independent analytic integral
H[p_g, theta_g_extra]    +4.72516954726101e-5     +4.725169546683118e-5
H[p_f, theta_f_extra]    +6.516963494914475e-6   +6.5169634892587114e-6
cross-dust block          0                         0
projected rank            2                         2
maximum discrepancy       5.778926328355721e-15
```

The old same-time-profile `p_amp*T – theta_amp*T` projected symplectic inner product can vanish by time integration (`∫ T T'=0`); it is the **two-shape** basis that captures the nonzero symplectic bilinear above. This finite-dimensional rank is a regression for preservation of both matter pairs **only**, not the number of propagating physical scalar modes.

## 4. All eighteen legitimate on-shell compact first variations

On the existing radiation-free **PHYSICALLY HOMOGENEOUS on-shell Candidate-C** trajectory (`a(t)` evolved by `a_dot=aH`, all-beta HR potential, two independently conserved dust charges), all 18 compact first variations of the nonlinear integrated action vanish within numeric precision:

```text
max |delta S / delta compact amplitude| = 1.3964523981613295e-11
first variations of new phase-parent g/f = [0., 0.]
quadrature order 20 x 20; centered first variation step = 2e-5
```

All previously valid 16 field variations remain valid; their numeric residuals are unchanged to floating point. Nonzero perturbations of either new compact phase-parent affect only their own matter contribution and do not change EH or HR by construction. Independent tests cover actual time- and radial-differentiation of both parent phases, multiple nonzero clock/momentum amplitudes, mixed species decoupling, positive momentum, time integration by parts, and quadrature/support refinement.

### Negative controls and errors not to repeat

- Treating the old *disconnected* `theta_rate` variables as independent field variations yields spurious first derivatives `+3.004e-4` and `+4.143e-5`; the corrected fields give zero. Do NOT call the former physical constraints or background tadpoles.
- On-shell normalization of the covariant dust constraint must NEVER be substituted before its original multiplier/lapse variation. The **exact canonical** action used here was derived by Legendre then stationary multiplier elimination.
- The `G=tT` compact phase shape is not the same as the `T` profile for momentum; the projected symplectic coefficient must be `Q/2`, not `Q`.
- The numerically finite *projected canonical* block does NOT certify BD elimination, diagonal diffeomorphism generator closure or physical kinetic positivity. The full spatial and time dependence and boundary terms of the actual metric/HR constraints remain to be derived.

## 5. Reproduction and source provenance

New files:

- `numerics/hr_integrable_two_dust_phase.py`
- `tests/test_hr_integrable_two_dust_phase.py`
- `scripts/verify_gate2b_step32e.py`

Command:

```bash
cd /path/to/Janus
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step32e.py gate2b-step32e-report.json
```

**Actually executed in the ONE focused local workspace `/mnt/data/janus32`:**

```text
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests
93 passed in 27.21 s

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step32e.py gate2b-step32e-report.json
93 passed in 24.82 s; exit_code=0
```

Breakdown **29 Step31 + 20 Step32a + 11 Step32b + 11 Step32c + 10 Step32d + 12 Step32e = 93**, genuinely combined, not a sum across isolated sessions. The runner verifies the expected Git blob SHA for **five previously published main calculation modules** before invoking tests, records SHA-256/Git blobs for all focused source/test/runner files, and marks `workspace_origin=focused_non_git_workspace`, `full_repository_regression=false`, `true_hamiltonian_ADM_auxiliary_constraints=NOT_DERIVED`, `HR_time_dependent_BD_null=NOT_DERIVED`, `physically_nonhomothetic_on_shell_solution=NOT_FOUND`, both physical De Felice/Aoki oracles `NOT_RUN`, and `GATE_2B=OPEN`.

The new Step32e source/test/runner and this audit are published on GitHub and must be **byte-for-byte Git blob checked** before claiming repository provenance. No clean repository clone or CI was executed here; earlier Step27–30 historical tests were not rerun. This does not constitute peer replication.

## 6. Next rigorous RED steps

1. **One field-theory ADM/Hamiltonian constraint analysis:** from the now **temporally integrable 18 compact parent fields**, abandon the restriction to only one Galerkin profile per field when computing constraints. Reparameterize both lapse and shift in true ADM variables, identify diagonal diffeomorphism gauge generators in a basis closed under their action, vary the full fields locally (not only the 4×4 invertible restricted matrix) and impose background/no-boundary Noether identities.
2. Derive the HR **time-dependent BD-null primary/secondary constraints** in the genuinely coupled theory and reduce the scalar action canonically **while retaining both dust `(theta,p)` pairs**. Only then compute physical scalar kinetic and spatial-gradient principal symbols. Do NOT interpret Schur or raw Hessian signs as ghost/stability statements.
3. Independently derive or exclude a **genuinely nonhomothetic on-shell** two-metric/two-dust solution beyond Step30's passive change of chart; demand all g/f Einstein, HR Stückelberg and matter Euler tadpoles vanish. The current on-shell background remains physically homogeneous and radiation-free.
4. From the SAME constrained action, reproduce independent physical De Felice finite-H `mu→0` scalar characteristic and Aoki nonlinear homothetic `K_S,c_S²` stable + unstable controls; only then study the first Candidate-C relative-mu fold near `a≈0.0301646`, and subsequently observational transfer/CMB likelihood if warranted. Report a **negative verdict** if any decisive physics gate fails.

**Scientific verdict:** `TIME_INTEGRABLE_ALL_EIGHTEEN_PARENT_FIELDS_GREEN`, `TWO_DUST_PHASE_SPACE_PAIRS_GREEN`, `GATE_2B_OPEN`, `JANUS_R_NOT_VALIDATED`. Keep `main`, archived `research/v2-flrw` and external 2026 JHR opposite-sign-EH paper audit distinct.
