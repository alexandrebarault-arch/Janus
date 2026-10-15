# Gate 2B — latest restart addendum

Date: 2026-10-15
Branch: `research/gate2b-nonhomothetic-transfer`

This file supplements `research/GATE2B_CHECKPOINT.md` with the newest oscillation-mode work.

## Candidate-C kinetic warning retained

A homogeneous velocity-Hessian diagnostic has been calibrated on nonlinear homothetic Aoki dust roots.

Files:

- `numerics/nonhomothetic_oscillation_kinetic.py`;
- `tests/test_nonhomothetic_oscillation_kinetic.py`;
- `research/NONHOMOTHETIC_OSCILLATION_KINETIC_AUDIT.md`;
- `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md`.

The usually omitted background term `dot(sigma_bg)` is essential. Once restored, the single non-null homogeneous velocity eigenvalue agrees in sign with Aoki `K_S` on the tested nonlinear pressureless roots with positive interaction normalization. A broader scratch scan gave `27/27` sign agreements.

On the leading non-homothetic early regular pair, the more-negative branch has the positive Aoki-calibrated homogeneous kinetic signature and the less-negative branch the opposite sign.

Following the positive-sign branch gives a robust signature zero at approximately

`a_K = 0.030136993`,
`z_K = 32.18181`,
`mu_K = -0.76624`.

A 16-point radius/finite-difference scan keeps this zero within about

`0.030136989 < a_K < 0.030137012`.

The independently derived finite weak-metric adiabatic fold is

`a_1 ~= 0.0301646`, `mu_1 ~= -0.768883`.

Their relative separation in `a` is only about `9.2e-4`.

This remains a strong conditioning warning, but **not yet a kinetic no-go** because the oscillation-mode weak Einstein constraints at finite `m_eff/H` have not yet been eliminated. An algebraic fold does not generically force `K_S=0`: the homothetic dust control `B2=3`, `B3=2/3` has a double root `mu=-3/4` while `K_S=375/128>0`.

## New compact-support Aoki action oracle

A new boundary-safe audit now evaluates the exact spherical Hassan-Rosen interaction on compact support in both conformal time and radius.

Files:

- `numerics/aoki_compact_action_oracle.py`;
- `tests/test_aoki_compact_action_oracle.py`.

The compact support removes the total-derivative / finite-ball contamination that spoiled earlier local gradient Hessians. The production helper does **not** contain the published Aoki `K_S` or `c_S^2` formulas; they are kept only in the regression test.

For a representative pressureless nonlinear branch with

`(b1,b2,b3)=(1,-4.2383993109,13.6801214252)`, `K=1`, `mu~-0.6692344`,

the exact compact HR action gives a kinetic Hessian coefficient near

`-0.613109`,

versus the independently normalized Aoki value

`-2 D K_S ~= -0.613112`,

and gives

`c_S^2 ~= 13.27620`

versus Aoki

`13.27614`.

The committed regression covers three independent nonlinear dust controls, including opposite kinetic signs. Targeted reconstructed-workspace verification of the current Aoki-oracle / interaction-tensor subset reached `8 passed`; this is not a full-repository GREEN claim.

Scientific consequence: the earlier bad spatial speed was a boundary/constraint extraction artifact, not evidence of a wrong HR interaction potential.

## New weak-Einstein / interaction-source infrastructure

Three additional reusable audit layers are now present:

- `numerics/nonhomothetic_hr_interaction_tensor.py` — full mixed Hassan-Rosen interaction tensors `V_g^mu_nu`, `V_f^mu_nu`, including off-diagonal components;
- `numerics/aoki_spherical_einstein_linear.py` — linear mixed Einstein tensor for Aoki's spherical areal gauge;
- `numerics/aoki_hr_native_sources.py` — evaluates the HR tensors in a common chart and transforms them back into the native `g` and `f` radial charts.

The full interaction tensor is pinned by diagonal-source formulas and by similarity covariance. The native-source layer is pinned by invariance under a common radial chart change.

The linear Einstein operator has independent controls:

1. Minkowski areal-gauge spherical perturbations;
2. the exact FLRW constant-lapse expansion;
3. the Minkowski linearized Bianchi identity.

Its `delta G^0_0` also reproduces the left-hand side of Aoki Eq. (4.44) after identifying the physical Hubble parameter as `H=a'/a^2`.

This closes the convention layer needed to write the four finite-`m_eff/H` weak Einstein constraints without guessing signs or chart factors.

## Failed shortcuts to remember

Do not:

- extract the spatial sound speed from the raw local 2x2 Stückelberg symbol before the proper constraint reduction;
- use a finite-ball gradient Hessian with uncompensated boundary terms;
- replace the nonlinear branch by an instantaneous effective FLRW substitution `y=K(1+mu)`, `c=1/(1+mu)` — it does not reproduce Aoki `c_S^2`;
- infer a kinetic zero merely from the existence of an algebraic fold.

## Immediate restart

Continue `research/NONHOMOTHETIC_OSCILLATION_ACTION_PLAN.md` from the finite-mass constraint construction.

The next concrete task is to combine

`(phi_g, psi_g, phi_f, psi_f, delta_eta, delta_r)`

with the new native HR sources and the linear spherical Einstein operators, solve the four weak metric constraints at finite `m_eff/H`, and then derive the remaining Stückelberg scalar equation/action.

Acceptance remains two-stage:

1. homothetic control: recover Aoki Eqs. (4.50)-(4.56), including `K_S` and `c_S^2`;
2. non-homothetic linear control: as `mu -> 0`, recover the validated Candidate-C De Felice principal scalar.

Only after both are GREEN should the fully reduced kinetic/gradient operator be evaluated through the Candidate-C fold interval or a transition trajectory be integrated.
