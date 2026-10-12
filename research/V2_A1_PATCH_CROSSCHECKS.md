# V2 A1 — Source-patch physics cross-checks

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `ANALYTIC_CROSSCHECKS_PASS__CXX_EXECUTION_PENDING`

## 1. Interaction-parameter convention

Kocic et al. define the ghost-free potential as

`V(S) = - ell^{-2} sum_n beta_n e_n(S)`

with dimensionless `beta_n` and a separate inverse-length-squared scale `ell^{-2}`.

The pinned `bim-solver` runtime model has no independent `ell` parameter. Its shifted polynomials `P_*_*` are built directly from `b_0...b_4`.

Therefore the runtime coefficients correspond to the dimensionful combination

`b_n = ell^{-2} beta_n`

(up to the solver's explicit `V_SIGN` convention, already built into `P_*_*`).

The reference initial-data solver uses

`interaction = 0.02`

and

`beta = (-2.4, 1, -0.2, 0, -0.4)`.

The matching runtime config is therefore

- `b_0 = -0.048`
- `b_1 = 0.020`
- `b_2 = -0.004`
- `b_3 = 0`
- `b_4 = -0.008`.

`numerics/bim_solver_reference_config.py` writes exactly these values.

## 2. Why the mixed momentum term uses `pfS + pfFS`

A potential normalization ambiguity was identified in the standard-3+1 patch to `eq_C_3`.

The general bimetric interaction currents obey the spherical momentum identity

`sqrt(gamma) j_g^b + sqrt(phi) j_f^b = 0`.

For the solver's Valencia variables,

`j_g^m = pfS / (gA gB^2)`

and, by exact sector duality,

`j_f^m = pfFS / (fA fB^2)`.

But

`sqrt(gamma) = gA gB^2`,

`sqrt(phi) = fA fB^2`.

Hence the densitized matter momenta entering the combined interaction-current constraint are simply

`sqrt(gamma) j_g^m = pfS`,

`sqrt(phi) j_f^m = pfFS`.

Therefore the two-matter term is proportional to

`pfS + pfFS`

with **no additional metric-ratio factor** multiplying `pfFS`.

This matches the current patcher's replacement inside the pre-existing outer `k_f*k_g` structure of `eq_C_3`.

## 3. Valencia f-fluid equations

The new f-fluid evolution equations were compared directly against the pinned upstream g-fluid equations in `include/eom-std/eomMatter.h`.

They are the exact sector copy under

- `gA,gBet,gAlp,gDAlp,gK1 -> fA,fBet,fAlp,fDAlp,fK1`;
- `pfD,pfS,pftau,pfv -> pfFD,pfFS,pfFtau,pfFv`.

No modified equation of state, cross-fluid drag or new matter force has been introduced. Each matter sector remains minimally coupled to its own metric; all cross-sector influence occurs through the interacting metrics.

## 4. Consequence

The remaining A1 uncertainty is no longer an identified normalization ambiguity in these blocks.

It is executable validation:

- source patch compiles;
- zero-f regression reproduces upstream;
- sector-dual f-only control is consistent;
- the reference twin wall has a regular short-time development.

Do not promote this analytic cross-check to an executable PASS until those runtime gates have been run.
