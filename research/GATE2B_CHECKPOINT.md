# Gate 2B — authoritative restart checkpoint

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The scalar-action/reduction problem and the late exact-dust linear system are no longer the blockers.  The unresolved problem is now sharply localized to the **nonlinear, non-homothetic screened-to-linear helicity-0 transition** that must determine the two late canonical matching data.

The newest result is stronger than the former instantaneous Aoki proxy: an exact spherical Hassan-Rosen Stückelberg pullback plus weak-metric constraints has been calibrated against the full homothetic Aoki equations and then evaluated on the actual non-homothetic Candidate-C dust background.  The regular nonlinear adiabatic pair disappears at a fold near `z=32.15` and reappears near `z=19.36`; only a separate near-singular branch close to `mu=-1` remains between those folds.

Therefore a simple algebraic/adiabatic continuation from the early screened branch to the late linear regime is **not available**.  A genuinely dynamical nonadiabatic scalar-graviton transition is required if Candidate C is to survive.

Do **not** promote the historical large late `R=delta_relative/delta_common` values to physical transfer functions.  The late linear subsystem still has two unfixed helicity-0 phase-space data.

## Closed hard facts — linear scalar sector

### Conventions / action

- JANUS/Comelli -> De Felice/Hassan-Rosen bridge:
  `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- De Felice Eq. (44) EH scalar action audited.
- Eq. (54) P(X) matter action audited.
- Direct O(delta^2) HR Eqs. (45)-(46) audited; missing shift-volume terms fixed.
- Eq. (72) basis audited.
- f-field drift remains
  `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2`.
- GR scalar degeneracy is preserved.

### DF5e.4 / DF5e.5

The historical `NG3~k^2` artifact came from pressure-inconsistent differentiation of the BD mixed column.  Time-dependent canonicalization restores

`M_iZ -> M_iZ - (dot c_i + 3 H c_i)`.

On the locally on-shell regulated Case-C trajectory, the full De Felice Eq. (85) gravity branch gives

`c_s^2 = -0.6665833422935964`

versus independent target

`-0.6665833419871022`,

relative difference `~4.6e-10`.

See `research/DF5E5_EQ85_ONSHELL_AUDIT.md`.

### Candidate-C dust local action

At `a=0.5`, the same action/reduction gives

`c_s,grav^2 = 0.6920714772308268`

versus independent target

`0.6920714772884699`,

relative difference `~8e-11`.

See `research/DF5D_CANDIDATE_C_DUST_AUDIT.md`.

## Exact-dust late system — implemented

The strict Candidate-C-like dust benchmark re-solves its own on-shell background instead of deleting radiation only from perturbations.

Implemented components include:

- `numerics/candidate_c_dust_background.py`;
- `numerics/de_felice_dust_phase_action.py`;
- `numerics/de_felice_two_dust_action.py`;
- `numerics/de_felice_dust_physical_action.py`;
- `numerics/canonical_quadratic_evolution.py`;
- `numerics/de_felice_dust_observables.py`;
- `numerics/de_felice_dust_local_modes.py`;
- `numerics/candidate_c_dust_late_transfer.py`;
- mode tracking / stability / projection helpers.

The exact dust limit is first order: `p_g,p_f` are canonical phase variables, not ordinary auxiliaries.  The regular reduction uses a KKT saddle rather than an invalid Schur elimination of the dust momenta.

## Late principal stability and matching ambiguity

The strict dust benchmark has

`a_start = 0.057951440818742664`,
`z_start = 16.25582635861885`

at `m_eff/H=1`.

That is **not** a healthy linear matching surface.  The finite-speed exact-dust principal scalar remains negative there and crosses to positive only near

`a ~= 0.10165`, `z ~= 8.84`

for `k=0.05...0.2 h/Mpc`.

At a principal-stable late surface the physical phase state has six dimensions.  The four adiabatic common/relative conditions

- `delta_common=1`;
- `delta_relative=0`;
- `delta_common,N=1`;
- `delta_relative,N=0`

leave two independent helicity-0 data unfixed.

The historical convention `Y3=0`, `Y3_N=0` is not derived from the screened phase and can strongly excite a fast relative-rich late direction.  Therefore the late linear equations alone do not predict a unique `R(z=0,k)` or a unique `2x2` sector transfer matrix.

See `research/LATE_DUST_MATCHING_AUDIT.md`.

## Earlier Aoki proxy — superseded as transition model

The Candidate-C interaction coefficients satisfy the Aoki sufficient early nonlinear-stability coupling condition and the instantaneous homothetic proxy admits an early stable root.  The full instantaneous Aoki polynomial also showed that the early branch does not adiabatically approach `mu=0`.

Those calculations remain useful coupling diagnostics, but **the substitution `K -> xi(a)` is no longer the best available transition model**.  Candidate C is strongly non-homothetic in the relevant era.

See:

- `research/CANDIDATE_C_AOKI_PROXY_AUDIT.md`;
- `research/CANDIDATE_C_AOKI_FULL_POLYNOMIAL_AUDIT.md`.

## New exact non-homothetic Stückelberg derivation

### Exact spherical HR pullback

`numerics/nonhomothetic_stueckelberg.py` computes the exact spherical elementary symmetric polynomials of `sqrt(g^-1 f)` after a Stückelberg pullback.

For

`T=t + s(t) r^2/2`,
`R=(1+mu(t)) r`,

its temporal Euler equation factorizes.  On the interaction branch,

`s = -(a^2/c) [ dot(mu) + H mu (c+1+mu) ]`.

For `c=1` this is exactly Aoki-Maeda-Namba Eq. (64) after time-coordinate conversion.

The multiplying interaction factor is

`beta1 + 2 beta2 xi (1+mu) + beta3 xi^2 (1+mu)^2`,

which becomes `J` at `mu=0`.

### Leading non-homothetic nonlinear pair

After the temporal constraint, the leading radial equation has the linear factor `mu=0`; the two nonlinear branches satisfy

`A2 mu^2 + A1 mu + A0 = 0`,

with `e=dot(H)/H^2`,

`A2 = xi [ beta2 + beta3 xi (c+e+1) ]`,

`A1 = beta1 + beta2 xi (c+2e+5) + beta3 xi^2 (3c+2e+2)`,

`A0 = beta1 (e+3) + 2 beta2 xi (c+e+2) + beta3 xi^2 (2c+e+1)`.

For `c=1`, `e=-3(1+w)/2`, this reduces exactly to the polynomial whose roots are Aoki Eq. (68).

## Weak-metric constraints recovered from HR Y tensors

The weak metric interaction sources were reconstructed directly from the diagonal Hassan-Rosen `Y_(n)` tensors.  In the homothetic limit they reproduce Aoki Eqs. (98)-(101) exactly, including the f-sector `(1+mu)^-3` structure.

The same tensor formulas define the actual non-homothetic sources for

`S = diag(xi c, xi(1+mu), xi(1+mu), xi(1+mu))`.

A crucial normalization correction is closed:

**static weak metric sources use `D=xi J`, not the propagation coefficient `Gamma`.**

In repository conventions,

`m_g^2 = m^2 D`,

`m_f^2 = m^2 D / (alpha^2 xi^2)`.

At the leading merger `Gamma/D ~= 0.0829`; using `Gamma` would underestimate the finite weak response by roughly a factor 12.

## Auto-diff calibration against full Aoki finite equation

Targeted x64 JAX automatic differentiation is used only as an audit oracle, not a production dependency.

On homothetic controls:

1. without weak metric potentials, the exact radial Euler equation reproduces the nonlinear Aoki Eq. (68) roots;
2. after injecting the four weak potentials, it reproduces the roots of Aoki's full `C_H^2+C_m^2=0` equation to approximately `1e-6` or better for multiple independent `(m_g^2,m_f^2)` values.

This validates the weak-potential insertion before applying it to `c!=1`.

See `research/NONHOMOTHETIC_WEAK_METRIC_TRANSITION_AUDIT.md`.

## New fold result — current central nonlinear fact

Solving the finite weak-metric corrected non-homothetic local Euler equation together with

`partial E_R / partial mu = 0`

gives two conditioned folds for the **regular nonlinear pair**.

### Fold 1 — disappearance

`a_1 ~= 0.0301646`,
`z_1 ~= 32.151`,
`mu_1 ~= -0.768883`.

### Fold 2 — reappearance

`a_2 ~= 0.0491246`,
`z_2 ~= 19.356`,
`mu_2 ~= -0.67015`.

The values were checked over 27 combinations of background-derivative step, local radial expansion point and centered `mu` derivative step.  Normalized fold residuals are typically `<=1e-9` and often much smaller.

Independent root scans show:

- before fold 1: near-singular branch + regular pair + `mu=0`;
- between folds: only the near-singular nonlinear branch + `mu=0`;
- after fold 2: near-singular branch + regular pair + `mu=0`.

Representative exact roots:

- `a=0.0300`: `mu ~= -0.96489, -0.77621, -0.76283, 0`;
- `a=0.040`: `mu ~= -0.94343, 0`;
- `a=0.052`: `mu ~= -0.91830, -0.68454, -0.61931, 0`.

Thus the regular screened algebraic pair does **not** exist continuously through approximately

`32.15 > z > 19.36`.

See `research/NONHOMOTHETIC_FOLD_AUDIT.md`.

## Weak-expansion control near the folds

For the intended modes `k=0.05...0.2 h/Mpc`, the weak potentials remain small.

At fold 1, for `k=0.05 h/Mpc`,

`a H / k ~= 0.0215`,

and the largest absolute weak potential is about `2.3e-4`.

At `a=0.04` on the surviving near-singular branch `mu~-0.9434`, the largest weak potential at `k=0.05 h/Mpc` is about `1.7e-4`.

So the disappearance of the regular pair is not caused by a blow-up of the weak metric amplitudes on these scales.

However, the near-singular branch has `R_r=1+mu` small (`~0.0566` at `a=0.04`).  Its physical viability and map regularity are **not established** merely because the weak potentials are small.

## Current scientific ruling

- `LINEAR_SCALAR_ACTION_RECONSTRUCTION = CLOSED`.
- `STRICT_DUST_LATE_TRANSFER_EQUATIONS = BUILT`.
- `OLD_m_eff/H=1_MATCHING_SURFACE_HEALTHY = NO`.
- `LATE_TRANSFER_UNIQUE_FROM_FOUR_ADIABATIC_CONDITIONS = NO`.
- `EARLY_AOKI_SCREENING_EXCLUDED_BY_COUPLINGS = NO`.
- `INSTANTANEOUS_K_TO_XI_PROXY_IS_SUFFICIENT = NO`.
- `EXACT_NONHOMOTHETIC_TEMPORAL_STUECKELBERG_RELATION = DERIVED`.
- `LEADING_NONHOMOTHETIC_RADIAL_BRANCH = DERIVED`.
- `AOKI_EQ68_AND_FINITE_WEAK_METRIC_ROOTS_RECOVERED_IN_HOMOTHETIC_LIMIT = YES`.
- `REGULAR_NONLINEAR_ADIABATIC_PAIR_EXISTS_CONTINUOUSLY = NO` over `32.15 > z > 19.36` in the local finite-correction audit.
- `NEAR_SINGULAR_BRANCH_IS_A_VALID_PHYSICAL_CONTINUATION = NOT ESTABLISHED`.
- `DYNAMICAL_NONADIABATIC_HELICITY0_TRANSITION_REQUIRED = YES` if Candidate C survives.
- `MISSING_LATE_MATCHING_DATA_DERIVED = NO`.

Gate 2B remains open.

## Remaining work

- [x] conventions / backgrounds / action audits.
- [x] scalar degree count / BD removal.
- [x] Case-C finite-k kinetic and full Eq. (85) dispersion.
- [x] Candidate-C dust principal regression.
- [x] regular exact-dust late time-domain/KKT system.
- [x] late fundamental-matrix infrastructure.
- [x] principal stability boundary / mode-mixing distinction.
- [x] expose two-dimensional late matching ambiguity.
- [x] early Aoki coupling and full-polynomial proxies.
- [x] exact spherical non-homothetic Stückelberg pullback.
- [x] recover Aoki Eq. (64), Eq. (68), and weak metric Eqs. (98)-(101) as control limits.
- [x] calibrate finite weak-metric Euler roots against full homothetic Aoki equation.
- [x] localize the two finite-correction regular-branch folds on Candidate C.
- [ ] **Derive the oscillating/dynamical helicity-0 equation/action about the non-homothetic nonlinear branch, including weak metric constraints. NEXT HARD BLOCK.**
- [ ] Test whether a regular dynamical trajectory crosses the fold interval without `mu=-1`, kinetic zero/ghost, singular constraint matrix or divergent `dmu/dN`.
- [ ] If such a trajectory exists, read the induced `(Y3,Y3_N)` on a principal-stable late surface.
- [ ] Re-run late transfer with derived rather than chosen matching data.
- [ ] If successful, extend dust+dust to physical g-dust + g-radiation + f-dust.
- [ ] Compute unambiguous `T_gg,T_gf,T_fg,T_ff` only after matching is fixed.
- [ ] Full-repository regression suite in a real worktree.
- [ ] Final Gate-2B verdict.

## Verification limitation

The container still cannot clone GitHub and GitHub Actions remain disabled.  Hard identities and fold locations were checked in targeted reconstructed workspaces and independent x64 auto-diff scratch calculations.  **Do not claim the full repository suite is globally green** until it runs in a complete worktree.

## Immediate restart instruction

Resume from **the dynamical oscillating helicity-0 action/equation around the non-homothetic nonlinear branch**.

Do not spend more time tuning late `Y3,Y3_N`, fitting `R`, or forcing an algebraic branch jump through the fold gap.  The next discriminating test is whether the omitted dynamical scalar-graviton degree of freedom supplies a regular nonadiabatic trajectory through the interval `a~0.03016...0.04912` and thereby determines the two canonical late matching data.
