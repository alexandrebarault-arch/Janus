# DF5e.3e — BD algebraic/state audit checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Parent checkpoint: `research/GATE2B_CHECKPOINT.md`

## Goal

Identify the exact paper/code mismatch in the algebraic Boulware-Deser scalar sector before changing any physical coefficient. The Case-C finite-k target at `a=0.05`, `k=400` is De Felice Eq. (78) `NG3 = 0.0185421788`.

The current reconstruction has the correct scalar degree count, correct first two kinetic invariants, correct GR degeneracy and audited rate/auxiliary Schur structure, but the physical reducer still uses a frozen-coefficient BD canonicalization and therefore `NG3` still scales as `k^2`.

## Closed facts

- Eq. (72) basis normalization is closed: `A = 1/(n H_f) = a/H_omega`.
- Before BD elimination the spurious Y3 kinetic term tends to `a^2 xi k^2/[4(c+1)]`.
- The HR shift-volume omission was fixed previously; it was real but insufficient.
- The transformed raw BD state coefficient at the control point is about `h_ZZ ~ 1.609e6`.
- Time-dependent integration by parts requires `h_ZZ^eff = h_ZZ - (dot(C_ZZ)+3 H C_ZZ)`.
- In repository conventions `ScalarBackground.H` is the conformal Hubble rate `calH=a H_cosmic`. Along Case C with g-lapse `N=1`, `dot a = calH`; this conversion is explicit in the audit code.

## Reproducible audit instrumentation

- Commit `8a4e876`: RED regression added for an explicit decomposition of the transformed `Z^2` coefficient.
- Commit `a725fef`: added `numerics/de_felice_bd_audit.py` as a read-only diagnostic module.
- Commit `6fe17c9`: test imports the isolated audit helper; no physical reduction coefficient was changed.
- Commit `d555f6a`: RED tests added for the Case-C time correction and for the cosmic-time/conformal-H conversion.
- Commit `f7506d3`: `case_c_bd_effective_coefficient()` implemented. It evaluates the raw BD coefficient and `C_ZZ` at neighboring exact Case-C background points, computes `dot C_ZZ=(dC_ZZ/da) calH`, adds the `3 H_cosmic C_ZZ` measure term, and returns `h_ZZ^eff` without altering the physical reducer.

`bd_state_coefficient_decomposition()` exposes the exact old-basis pieces for a pure Eq. (72) `Z` displacement:

- `Sigma2 = Q_{Sigma,Sigma}`;
- `2A_Sigma_qf = 2 A Q_{Sigma,q_f}`;
- `A2_qf2 = A^2 Q_{q_f,q_f}`;
- `2Adot_Sigma_qfdot = 2 A_dot Q_{Sigma,q_f_dot}`;
- `2AAdot_qf_qfdot = 2 A A_dot Q_{q_f,q_f_dot}`;
- `Adot2_qfdot2 = A_dot^2 Q_{q_f_dot,q_f_dot}`.

Their sum equals the directly transformed `H[Z,Z]`. The helper also reconstructs `C_ZZ = H[Z,Zdot]` independently from the old basis.

## DF5e.3e.4 hard finding — the O(1e3) residual was an off-trajectory pressure derivative

The component derivative audit localizes almost all of `dot C_ZZ + 3 H C_ZZ` to the old-basis `Q_{Sigma,Sigma_dot}` channel; the `q_f` rate pieces cancel pairwise to high precision. More importantly, the previous Case-C central derivative was not following a locally consistent k-essence trajectory for the diagnostic f fluid.

`_case_c_audit_pieces()` sets `P_f=0` at the center and at both neighboring points while simultaneously using `c_sf^2=0.1`. For a barotropic `P(X)` field this is inconsistent at first derivative order. De Felice Eq. (10) gives `c_s^2=dP/d rho` along the background, while Eq. (18) gives the f-sector background field equation. Together they imply

`dot(P_f) = c_sf^2 dot(rho_f) = -3 n H_f c_sf^2 (rho_f + P_f)`.

At the control point `a=0.05`, `k=400`, `P_f=0`, `c_sf^2=0.1`, an independent exact-quadratic scratch reconstruction gives approximately

- pressure-frozen audit: `h_ZZ^eff = -2153.48`;
- `partial C_ZZ / partial P_f = 4.6882748e-8`;
- `dot P_f = -4.60771344e10`;
- omitted contribution to `dot C_ZZ`: `(partial C_ZZ/partial P_f) dot P_f = -2160.22`;
- pressure-consistent result: `h_ZZ^eff = +6.7421`.

Solving the transformed kinetic Schur complement for the value of `h_ZZ^eff` that reproduces De Felice Eq. (78) gives about `+6.7417` at the same point. Thus the entire O(1e3) discrepancy is accounted for by the missing pressure-trajectory contribution, without changing Eq. (44), Eq. (45), Eq. (54), the HR coefficients, or the `dot(phi_f)/phi_f` drift.

The earlier numerical clue is now understood rather than fitted: at the control point

`A_DF/6 + m^2 xi J c^2/(c+1) = 6.741811...`,

consistent with the pressure-corrected algebraic coefficient at the precision of the scratch finite-difference reconstruction.

A useful falsification check is the sound-speed dependence: with the pressure incorrectly frozen, the residual is nearly linear in `c_sf^2` and extrapolates to the correct O(1) value as `c_sf^2 -> 0`. Adding the required `dot P_f` chain-rule term removes that artificial `c_sf^2` dependence and leaves `h_ZZ^eff ~ 6.742` over diagnostic `c_sf^2` values from `0.01` to `1` at `k=400`.

## Interpretation

This clears the suspected primary-action mismatch in DF5e.3e. The root cause is two-layered:

1. the diagnostic time derivative in `case_c_bd_effective_coefficient()` omitted the local `P_f` drift while differentiating `C_ZZ`;
2. the production reducer still uses `_canonicalize_linear_zdot_frozen()`, so it deliberately omits the full time-dependent `Z Zdot` correction required by Eq. (73)'s `N a^3` measure.

The physical coefficients in Eqs. (44), (45), and (54) are not to be tuned.

## Active task list

- [x] DF5e.3e.1 — isolate BD-state audit from the physical solver.
- [x] DF5e.3e.2 — expose exact raw `h_ZZ` decomposition and independent `C_ZZ` reconstruction.
- [x] DF5e.3e.3 — implement `C_ZZ(a)`, `dot C_ZZ`, the measure term and a background-step convergence regression on exact Case C.
- [x] **DF5e.3e.4 — decompose the correction and identify the O(1e3) residual: missing `dot P_f` contribution in the Case-C derivative path.**
- [x] **DF5e.3e.5 — check the suspected matter drift against De Felice Eqs. (10), (18), (54): `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2` is correct and must not be removed.**
- [x] **DF5e.3e.6 — compare to Eq. (78)/(79): pressure-consistent `h_ZZ^eff` matches the required O(1) coefficient at the `k=400` control point without tuning.**
- [ ] **DF5e.4 — RED first: make the Case-C derivative pressure-consistent, then implement the time-dependent BD canonicalization and require Eq. (78) `NG3` green at `k=100,200,400,800`. NEXT.**
- [ ] DF5d — Candidate-C gravity branch only after Case C is green.

## Verification status

The hard finding above was reproduced in an independent scratch reconstruction using the exact quadratic HR interaction, not by changing the committed physical reducer. Repository tests have still not been executed in this environment because the working container cannot clone GitHub and GitHub Actions are disabled for this project. Do not claim the new regression or DF5e.4 green until it is run in an executable repository worktree.

## Restart instruction

Resume at **DF5e.4**.

1. Add a RED regression showing that a finite-`c_sf^2` local Case-C derivative must include `dot P_f = -3 n H_f c_sf^2 (rho_f+P_f)` and that the corrected `h_ZZ^eff` is O(1), not O(1e3).
2. Correct only the diagnostic derivative path first; do not change Eq. (44), Eq. (45), Eq. (54), EH, matter, or HR coefficients.
3. Add a RED finite-k regression for time-dependent BD canonicalization: after `Zdot` integration by parts, use `h_ZZ^eff = h_ZZ-(dot C_ZZ+3H C_ZZ)` while retaining the antisymmetric `Z-Ydot` couplings.
4. Implement the minimal time-dependent canonicalization needed to make Eq. (78) `NG3` green at `k=100,200,400,800`.
5. Verify the first two kinetic invariants and GR degeneracy remain unchanged.
6. Only after Case-C NG3 is green, resume the Case-C physical speed regression and then Candidate C.
