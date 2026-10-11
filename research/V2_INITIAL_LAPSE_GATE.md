# V2 Initial Lapse-Ratio Gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `REFERENCE_INITIAL_LAPSE_BRANCH = PASS_PRE_EVOLUTION`

## Question

The Gate-A0 two-matter Hamiltonian constraints already admit a regular time-symmetric centre/wall geometry. A necessary additional condition is that preservation of the bimetric secondary constraint admit a real, finite, same-time-orientation lapse ratio on that initial slice.

The relevant ratio is

`W = alpha/alpha_f = -W_f/W_g`.

For the selected geometric-mean time orientation, require

`W > 0`.

This is still only an initial-slice condition. It does not prove regular evolution.

## Exact specialization used

Pinned upstream:

`nubirel/bim-solver@8852e8e9921edeeedf1a447d3bf27b82ec24433c`.

The standard solver reconstructs

`W_g = Wg0 + r (Wg1 + r Wg2)`,

`W_f = Wf0 + r (Wf1 + r Wf2)`.

On the time-symmetric rest-dust slice

`p=0`, `K_g=KD_g=K_f=KD_f=0`, `S_g=S_f=0`, `tau_g=tau_f=0`,

so

`Wg1=Wf1=0`

and all explicit extrinsic-curvature pieces in `W2` vanish.

The evaluator in

`numerics/time_symmetric_lapse_gate.py`

transcribes only the surviving source-code terms from the pinned upstream `eq_gW_0`, `eq_gW_2`, `eq_fW_0`, `eq_fW_2`, then adds the exact f-dust `W2` pieces independently derived in `V2_TWIN_LAPSE_MATTER_DUALITY.md`.

## Important debugging correction

The first source transcription failed the physical regression because `eq_gW_2` was initially parsed as if a single outer minus acted on multiple terms.

The actual upstream C++ is a sum beginning

`-A - B + ...`,

not

`-(A-B+...)`.

This single sign error made the proportional-vacuum cancellation fail and drove the computed lapse ratio to enormous values near the outer boundary.

The failing tests were not weakened. The source was re-read and the sign fixed at the transcription point.

## TDD evidence

### RED

Before the module existed:

`ModuleNotFoundError: No module named 'numerics.time_symmetric_lapse_gate'`.

### First implementation

- exact symmetric control passed;
- both reference-profile tests failed with huge/sign-changing outer `W`;
- root cause traced to the `eq_gW_2` source sign described above.

### GREEN after the single source fix

`3 passed in 0.52s`.

Tests verify:

1. an exactly sector-symmetric state with symmetric beta coefficients gives `W=1`;
2. the reference initial wall has finite `W>0` everywhere;
3. the asymptotically flat exterior returns to `W≈1`.

## Reference initial data

Same Gate-A0 reference point:

- `beta1=1`, `beta2=-0.2`, `beta3=0`;
- flat completion `beta0=-2.4`, `beta4=-0.4`;
- interaction scale `0.02`;
- `kappa_g=kappa_f=1`;
- central f Gaussian: amplitude `0.04`, sigma `2`;
- g shell: amplitude `0.025`, radius `5`, sigma `1`;
- outer radius `25`.

The Lane–Emden solution is converted to upstream standard-3+1 variables by

`A_g=B_g=psi_g^2`,

`A_f=B_f=psi_f^2`,

`DB_g=2 psi_g'/psi_g`,

`DB_f=2 psi_f'/psi_f`,

`R=(psi_f/psi_g)^2`.

At rest the Lane–Emden conserved sources are the Valencia `D_g,D_f`; `S=tau=0`.

The upstream bimetric coefficients absorb the interaction scale:

`b_n = interaction * beta_n`.

## Result

For the reference slice:

`W_min ≈ 0.795`,

`W_max ≈ 1.178`,

`W(r_max) ≈ 1.000000003`.

No zero, divergence or sign flip occurs across the centre/wall/exterior transition.

The result is stable under the tested radial refinements:

| points | BVP tolerance | min W | max W | outer W |
|---:|---:|---:|---:|---:|
| 300 | 5e-7 | 0.794959 | 1.178111 | 1.000000003 |
| 420 | 2e-7 | 0.794956 | 1.178161 | 1.000000003 |
| 600 | 1e-7 | 0.794940 | 1.178170 | 1.000000003 |
| 800 | 5e-8 | 0.794922 | 1.178179 | 1.000000003 |

The small drift in the extrema is much smaller than the margin to `W=0`.

## Scientific interpretation

The reference initial geometry passes a stronger necessary condition than the Hamiltonian constraints alone:

`INITIAL_CONSTRAINTS = PASS`

`INITIAL_LAPSE_BRANCH = PASS`

This matters because the compensation wall does **not** begin on an obviously forbidden secondary-constraint/lapse branch.

It does **not** establish:

- short-time dynamical regularity;
- absence of lapse zeros later;
- absence of shell crossing;
- ghost/gradient stability;
- attraction toward this configuration from ordinary cosmological initial data.

## Next falsification gate before C++ evolution

Map the local basin of admissible initial data around the reference configuration.

Vary, in controlled ranges:

- central f amplitude and width;
- g-shell amplitude/radius/width;
- moderate beta variations near the reference interaction family.

For each solved constraint profile require:

1. positive finite conformal factors;
2. finite `W_g,W_f`;
3. `W=-W_f/W_g > 0` throughout;
4. no near-zero denominator smaller than a chosen relative safety margin;
5. asymptotic return toward the selected flat branch.

The purpose is not parameter fitting. It is to determine whether the reference wall sits inside a finite admissible basin or on a finely tuned line before investing in the external C++ evolution fork.
