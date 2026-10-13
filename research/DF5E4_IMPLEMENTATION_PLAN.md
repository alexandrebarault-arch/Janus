# DF5e.4 — pressure-consistent time-dependent BD canonicalization plan

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Status: design/checkpoint only; production code and new tests not yet changed in this environment.

## Hard finding carried into DF5e.4

The O(1e3) discrepancy in the BD algebraic coefficient was not a wrong coefficient in De Felice Eqs. (44), (45), or (54). The Case-C audit differentiated `C_ZZ` while forcing `P_f=0` at neighboring points even though the diagnostic fluid uses finite `c_sf^2`.

For barotropic k-essence,

`dot P_f = c_sf^2 dot rho_f = -3 n H_f c_sf^2 (rho_f+P_f)`.

At `a=0.05`, `k=400`, `c_sf^2=0.1`, the missing chain-rule contribution to `dot C_ZZ` is approximately `-2160.22`, moving the stable scratch result from `h_ZZ^eff ~ -2153.48` to `+6.7421`. The value required by De Felice Eq. (78) through the transformed kinetic Schur complement is about `+6.7417`.

No EH, matter, HR, Eq. (72), or background `dot(phi_f)/phi_f` coefficient is to be tuned.

## Canonicalization identity to implement

After the Eq. (72) transform, write the quadratic Hessian in state/rate form

`H = [[M, C], [C^T, K]]`,

with state order `(Y1,Y2,Y3,Z)` and rate order `(Y1dot,Y2dot,Y3dot,Zdot)`.

Let

`c_i = C[i,Z]`.

The action contains `mu_measure * dt` through the common measure `N a^3`, with

`mu_measure = d ln(N a^3)/dt`.

For the current g-cosmic convention `N=1`, `mu_measure = 3 H_cosmic`.

Integrating every `c_i X_i Zdot` term by parts gives:

1. rate block / antisymmetric coupling
   - `C_new[Z,i] = C[Z,i] - c_i` for `i != Z`;
   - `C_new[:,Z] = 0`;
   - the `Zdot` kinetic row/column remains zero.

2. state block
   - for `i != Z`, `M_new[i,Z] = M[i,Z] - (dot c_i + mu_measure c_i)` and symmetrically `M_new[Z,i]`;
   - for the diagonal BD entry,
     `M_new[Z,Z] = M[Z,Z] - (dot c_Z + mu_measure c_Z)`.

Thus

`h_ZZ^eff = h_ZZ - (dot C_ZZ + mu_measure C_ZZ)`.

The existing `_canonicalize_linear_zdot_frozen()` implements only the rate-block part with `dot c_i = mu_measure = 0`. DF5e.4 must add the state correction without changing the already-correct antisymmetric `Z-Ydot` structure.

## Pressure-consistent derivative

The generic canonicalizer should not know about Case C or k-essence thermodynamics. It should receive the coefficient derivative `dot c` and `mu_measure` explicitly.

The Case-C diagnostic/adapter should construct `dot c` on a locally consistent trajectory. For the f fluid at the control point,

`dP_f/da = dot P_f / dot a`,

with

`dot a = calH`,
`dot P_f = -3 n H_f c_sf^2 (rho_f+P_f)`.

The exact Case-C `rho_f(a)` path already satisfies the density continuity equation at the center. The missing first-order datum is the pressure drift.

For the full physical-speed reconstruction, the pressure contribution affects the whole `c_i` column, not only `C_ZZ`. At `a=0.05,k=400,c_sf^2=0.1`, the scratch pressure-chain contributions to `dot c_i` are approximately

- `Y1`: negligible;
- `Y2`: `-0.458`;
- `Y3`: `-15.24`;
- `Z`: `-2160.22`.

The `Z` component controls NG3; the `Y2/Y3` components must also be retained when reconstructing the full physical Hessian and phase speeds.

## TDD sequence for the next executable worktree

1. **RED — pressure trajectory**
   - Add a regression around Case C `a=0.05,k=400,c_sf^2=0.1`.
   - Require a pressure-consistent derivative to produce O(1) `h_ZZ^eff` near the Eq. (78)-required value instead of O(1e3).
   - Confirm the existing pressure-frozen derivative fails this assertion for the expected reason.

2. **GREEN — diagnostic derivative only**
   - Allow the audit trajectory evaluator to carry the first-order f-pressure drift.
   - Do not modify the physical reducer yet.

3. **RED — generic time-dependent canonicalization**
   - Add a small synthetic quadratic action with known time-dependent `c_i(t)` and measure.
   - Require the canonicalized state/rate blocks to match the integration-by-parts identities above exactly.

4. **GREEN — minimal canonicalizer**
   - Add a function that takes the transformed Hessian, `dot c`, and `mu_measure` explicitly.
   - Keep the frozen helper if needed for principal/local diagnostics, but do not use it for the finite-k physical Case-C comparison.

5. **RED/GREEN — De Felice Eq. (78)**
   - Case C `a=0.05`, beta1 only, diagnostic `c_sf^2=0.1`.
   - Require `NG3` to match Eq. (78) at `k=100,200,400,800`.
   - Keep NG1/NG2 and the three-degree kinetic rank checks green.

6. **Then physical speeds**
   - Re-run the three scalar branches using the complete state corrections `dot c_i + mu_measure c_i`.
   - Only after Case C is green continue to Candidate C.

## Non-negotiable checks

- No coefficient tuning to force Eq. (78).
- Preserve the already-audited `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2` relation.
- Preserve the corrected HR shift-volume terms.
- Preserve GR one-metric degeneracy.
- Do not claim RED/GREEN execution until tests actually run in a repository worktree; GitHub Actions are intentionally disabled at this checkpoint.
