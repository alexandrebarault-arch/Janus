# Gate 2B — authoritative restart checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption.

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The former scalar-action/reduction blocker is closed: the repaired De Felice/Hassan-Rosen path reproduces the correct scalar degree count, Case-C `NG3`, the full De Felice Eq. (85) Case-C propagation branches, and the healthy Candidate-C dust+dust principal gravity speed.

The late exact-dust time-domain system has also been built and conditioned.  It exposed two new scientific blockers rather than a unique healthy transfer prediction:

1. the finite-speed exact-dust principal scalar is unstable between the old `m_eff/H=1` matching surface (`z ~= 16.26`) and a nearly scale-independent healthy boundary near `z ~= 8.84` for `k=0.05...0.2 h/Mpc`;
2. even after that healthy boundary, the four common/relative adiabatic conditions leave two helicity-0 phase-space matching data unfixed.

Therefore the previously large provisional values of `R=delta_relative/delta_common` are **not physical predictions** and must not be promoted to `T_gg,T_gf,T_fg,T_ff`.

The next problem is no longer linear transfer implementation.  It is the **nonlinear screened-to-linear transition that must determine the missing helicity-0 matching data**.

## Closed hard facts

### Conventions / action

- JANUS/Comelli -> De Felice/Hassan-Rosen bridge:
  `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Eq. (44) EH scalar action audited.
- Eq. (54) P(X) matter action audited.
- Direct O(delta^2) HR Eqs. (45)-(46) audited; missing shift-volume terms were fixed.
- Eq. (72) basis audited.
- f-field drift remains
  `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2`.
- GR scalar degeneracy is preserved.

### DF5e.4 / DF5e.5

The old `NG3~k^2` branch was traced to pressure-inconsistent differentiation of the BD mixed column.  Time-dependent canonicalization restores the omitted `dot P_f` chain contribution and implements

`M_iZ -> M_iZ - (dot c_i + 3 H c_i)`

with the corresponding rate-block integration by parts.

The full De Felice Eq. (85) reconstruction on a locally on-shell regulated trajectory gives the Case-C gravity limit

`c_s^2 = -0.6665833422935964`

versus independent target

`-0.6665833419871022`,

relative difference `~4.6e-10`.

See `research/DF5E5_EQ85_ONSHELL_AUDIT.md`.

### Candidate-C dust+dust local action

At `a=0.5`, the same reduction gives the dust Candidate-C principal gravity limit

`0.6920714772308268`

versus independent target

`0.6920714772884699`,

relative difference `~8e-11`.

See `research/DF5D_CANDIDATE_C_DUST_AUDIT.md`.

## Exact-dust time-domain solver — implemented

The strict dust benchmark re-solves its own on-shell background instead of deleting radiation only from perturbations.

Implemented components include:

- `numerics/candidate_c_dust_background.py`;
- `numerics/de_felice_dust_phase_action.py`;
- `numerics/de_felice_two_dust_action.py`;
- `numerics/de_felice_dust_physical_action.py`;
- `numerics/de_felice_dust_local_modes.py`;
- `numerics/candidate_c_dust_late_transfer.py`;
- `numerics/dust_observables.py`;
- `numerics/dust_mode_tracking.py`;
- `numerics/candidate_c_dust_stability.py`;
- `numerics/candidate_c_dust_mode_projection.py`.

The exact dust limit is first order.  `p_g,p_f` are canonical phase variables, not ordinary auxiliaries.  The regular reduction uses a 5x5 KKT saddle on `(Ydot,p_g,p_f)` rather than an invalid Schur elimination of the two dust momenta.

## Late dust principal stability

The strict dust benchmark has its own

`a_start = 0.057951440818742664`,
`z_start = 16.25582635861885`

where `m_eff/H=1`.

At that surface, the finite-speed principal exact-dust scalar is negative for the production high-k scales:

- `k=0.05 h/Mpc`: `c_principal^2 ~= -8.26e-3`;
- `k=0.10 h/Mpc`: `~-8.43e-3`;
- `k=0.20 h/Mpc`: `~-8.9e-3`.

The principal zero is almost scale independent:

- `k=0.05`: `a ~= 0.101648`, `z ~= 8.8379`;
- `k=0.10`: `a ~= 0.101647`, `z ~= 8.8379`;
- `k=0.20`: `a ~= 0.101658`, `z ~= 8.8369`.

Thus the old `m_eff/H=1` surface is not a healthy linear matching surface.

See `research/LATE_DUST_TRANSFER_AUDIT.md` and `research/LATE_DUST_MODE_MIXING_AUDIT.md`.

## Mode identity ruling

A spectral pair transported continuously from today is **not** the same thing as the local finite-speed principal mode through the quasi-degenerate region.

The continuously transported late pair becomes dust-like at the early endpoint (`c^2 ~ k^-2`), while the finite-speed character transfers to another local pair.  Strong nonnormal/quasi-degenerate mixing is exposed by low biorthogonal projector overlap.

Therefore:

- continuous eigenpair transport is a mode-mixing diagnostic;
- local finite-speed principal character is the stability diagnostic;
- one global label “the gravity pair” is ill-conditioned through the exchange region.

## Matching ambiguity — current central blocker

At any principal-stable late surface, the regular phase state has six dimensions:

`(Y1,Y2,Y3,Y1_N,Y2_N,Y3_N)`.

The physically motivated conditions

- `delta_common=1`;
- `delta_relative=0`;
- `delta_common,N=1`;
- `delta_relative,N=0`

fix only four combinations.

Two independent helicity-0 matching data remain free.  The historical choice

`Y3=0`, `Y3_N=0`

is only one convention; it is not derived from the screened phase.

At `k=0.1 h/Mpc`, `a_match=0.12`, an independent conditioned reconstruction gives approximately

`delta_common,0 ~= 83.17 + 8.32e4 Y3_i + 3.13e2 Y3N_i`,

`delta_relative,0 ~= -2468.7 - 2.65e6 Y3_i - 1.05e4 Y3N_i`.

Therefore the late linear subsystem alone does not predict a unique `R(z=0,k)`.

See `research/LATE_DUST_MATCHING_AUDIT.md`.

## Local fast relative-rich mode

Even after the principal gradient boundary, the local exact-dust system contains a real fast growing direction.  At `a=0.12`, `k=0.1 h/Mpc`,

`lambda_N ~= 7.6274`

under derivative-step convergence, and the local mode is relative-rich (`delta_relative/delta_common ~= 1.44`).

The historical `Y3=Y3_N=0` lift excites this direction; its total initial adiabatic values are produced by cancellation among several local modes.  This is another reason not to interpret the old large late `R` values as healthy spontaneous conversion.

## Aoki-Maeda-Namba nonlinear proxy

The only legitimate source of the two missing late matching data is the preceding nonlinear/screened dynamics.

A local diagnostic based on Aoki, Maeda & Namba (2015) has now been added:

- `numerics/candidate_c_aoki_proxy.py`;
- `tests/test_candidate_c_aoki_proxy.py`;
- `research/CANDIDATE_C_AOKI_PROXY_AUDIT.md`.

Candidate-C raw interaction coefficients satisfy the Aoki sufficient early nonlinear-stability coupling condition

`b2 < 0`,
`b2^2 - b1*b3 > 0`.

Using only the instantaneous proxy `K -> xi(a)`, the early `w=0` admissible root `mu>-1` is smooth and has positive Aoki `K_S` and `c_S^2` over the tested early dust interval.

This means **nonlinear early screening is not excluded by the interaction couplings**.

It does **not** solve Candidate C because the Aoki derivation assumes a homothetic background with constant `K`, while Candidate C is strongly non-homothetic (`ctilde ~= 0.34` at the old linear start rather than 1).  Their asymptotic formulas also assume `H >> m_eff`, whereas the old start is defined by `H~m_eff`.

Most importantly, Aoki's adiabatic `mu` is algebraic and explicitly omits the dynamical scalar-graviton oscillation degree of freedom.  It cannot by itself supply the two canonical matching data required by the late exact-dust system.

For realistic `w<1/3`, Aoki et al. themselves note that the `H~m_eff` transition may invalidate the adiabatic approximation and require a full numerical treatment.

## Current scientific ruling

- `LINEAR_SCALAR_ACTION_RECONSTRUCTION = CLOSED`.
- `STRICT_DUST_LATE_TRANSFER_EQUATIONS = BUILT`.
- `OLD_m_eff/H=1_MATCHING_SURFACE_HEALTHY = NO`.
- `LATE_TRANSFER_UNIQUE_FROM_FOUR_ADIABATIC_CONDITIONS = NO`.
- `NONLINEAR_SCREENING_EXCLUDED_BY_CANDIDATE_C_COUPLINGS = NO`.
- `PUBLISHED_AOKI_ALGEBRAIC_PROXY_FIXES_MATCHING = NO`.
- `FULL_NONHOMOTHETIC_DYNAMICAL_TRANSITION_REQUIRED = YES`.

Gate 2B therefore remains open, but its unresolved content is now sharply localized.

## Remaining work

- [x] conventions / backgrounds / action audits.
- [x] scalar degree count / BD removal.
- [x] Case-C finite-k kinetic and full Eq. (85) dispersion.
- [x] Candidate-C dust local principal regression.
- [x] regular exact-dust time-domain/KKT system.
- [x] late fundamental-matrix infrastructure.
- [x] principal stability boundary / mode-mixing distinction.
- [x] expose two-dimensional matching ambiguity.
- [x] local Aoki nonlinear-screening coupling proxy.
- [ ] **Derive a dynamical nonlinear helicity-0 system on the non-homothetic Candidate-C background. NEXT HARD BLOCK.**
- [ ] Evolve that system through `H~m_eff` and read `(Y3,Y3_N)` on a principal-stable surface.
- [ ] Re-run late transfer using derived rather than chosen matching data.
- [ ] If successful, extend from dust+dust to physical g-dust + g-radiation + f-dust.
- [ ] Compute unambiguous `T_gg,T_gf,T_fg,T_ff` only after matching is fixed.
- [ ] Full-repository regression suite in a real worktree.
- [ ] Final Gate-2B verdict.

## Verification limitation

The container still cannot clone GitHub and GitHub Actions remain disabled.  Targeted reconstructed workspaces and independent numerical checks were used for the hard diagnostics above.  Do not claim the full repository suite is globally green until it runs in a complete worktree.

## Immediate restart instruction

Resume from **non-homothetic nonlinear transition derivation**.

Do not spend more time tuning the late linear initial lift or fitting `R` by choosing `Y3,Y3_N`.  Those two data must come from a preceding nonlinear/screened evolution or the Candidate-C branch is not predictive.
