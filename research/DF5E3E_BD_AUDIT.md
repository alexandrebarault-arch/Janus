# DF5e.3e — BD algebraic/state audit checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Parent checkpoint: `research/GATE2B_CHECKPOINT.md`

## Goal

Identify the exact paper/code mismatch in the algebraic Boulware-Deser scalar sector before changing any physical coefficient. The Case-C finite-k target at `a=0.05`, `k=400` is De Felice Eq. (78) `NG3 = 0.0185421788`.

The current reconstruction has the correct scalar degree count, correct first two kinetic invariants, correct GR degeneracy and audited rate/auxiliary Schur structure, but `NG3` still scales as `k^2`.

## Closed facts

- Eq. (72) basis normalization is closed: `A = 1/(n H_f) = a/H_omega`.
- Before BD elimination the spurious Y3 kinetic term tends to `a^2 xi k^2/[4(c+1)]`.
- The HR shift-volume omission was fixed previously; it was real but insufficient.
- The transformed raw BD state coefficient at the control point is about `h_ZZ ~ 1.609e6`.
- Time-dependent integration by parts gives the formal correction `dot(C_ZZ)+3 H C_ZZ ~ 1.611e6`, leaving `h_ZZ^eff ~ -2.15e3`.
- Eq. (78) would instead require an effective algebraic coefficient of order `+6.74175` at the same point.
- The numerical clue `A_DF/6 + m^2 xi J c^2/(c+1)` is close to the required coefficient, but this is NOT accepted as a derivation or fit.

## New reproducible audit instrumentation

- Commit `8a4e876`: RED regression added for an explicit decomposition of the transformed `Z^2` coefficient.
- Commit `a725fef`: added `numerics/de_felice_bd_audit.py` as a read-only diagnostic module.
- Commit `6fe17c9`: test imports the isolated audit helper; no physical reduction coefficient was changed.

`bd_state_coefficient_decomposition()` now exposes the exact old-basis pieces for a pure Eq. (72) `Z` displacement:

- `Sigma2 = Q_{Sigma,Sigma}`;
- `2A_Sigma_qf = 2 A Q_{Sigma,q_f}`;
- `A2_qf2 = A^2 Q_{q_f,q_f}`;
- `2Adot_Sigma_qfdot = 2 A_dot Q_{Sigma,q_f_dot}`;
- `2AAdot_qf_qfdot = 2 A A_dot Q_{q_f,q_f_dot}`;
- `Adot2_qfdot2 = A_dot^2 Q_{q_f_dot,q_f_dot}`.

Their sum must equal the directly transformed `H[Z,Z]`. The helper also reconstructs `C_ZZ = H[Z,Zdot]` independently from the old basis.

## Active task list

- [x] DF5e.3e.1 — isolate BD-state audit from the physical solver.
- [x] DF5e.3e.2 — expose exact raw `h_ZZ` decomposition and independent `C_ZZ` reconstruction.
- [ ] **DF5e.3e.3 — compute `C_ZZ(a)` on the exact Case-C trajectory and evaluate `dot C_ZZ` with a convergence test in the background step.**
- [ ] DF5e.3e.4 — decompose `dot C_ZZ` into derivatives of `A`, `A_dot`, and the underlying old-basis Hessian entries; identify which term carries the O(1e3) residual.
- [ ] DF5e.3e.5 — rederive the offending old-basis state/rate entry directly from De Felice Eqs. (44), (45), (54), including `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2`.
- [ ] DF5e.3e.6 — compare the derived result to Eq. (79) `A,B,C,D`; do not tune coefficients.
- [ ] DF5e.4 — only after an exact mismatch is found, add a RED regression for that single coefficient, implement one fix, and require Eq. (78) NG3 green at `k=100,200,400,800`.
- [ ] DF5d — Candidate-C gravity branch only after Case C is green.

## Restart instruction

Resume at **DF5e.3e.3**.

1. Use exact Case C `a=0.05`, `k=400`, beta1 only, with the same `cs_f^2=0.1` diagnostic fluid used by `tests/test_de_felice_two_matter_action.py`.
2. Evaluate `bd_state_coefficient_decomposition()` at nearby points on the exact Case-C trajectory.
3. Convert derivative with respect to `a` to the cosmic-time derivative consistently with the g-sector lapse (`N=1`): `dot a = a H`.
4. Form `h_ZZ^eff = h_ZZ - (dot C_ZZ + 3 H C_ZZ)`.
5. Verify convergence as the background finite-difference step is reduced before interpreting any component.
6. Then differentiate the six raw state pieces and `C_ZZ` analytically/numerically to localize the O(1e3) residual.
7. Do not modify `de_felice_two_matter_action.py`, EH, matter or HR coefficients until one exact primary-equation mismatch is demonstrated.
8. After the first hard finding, update both this file and `GATE2B_CHECKPOINT.md`.
