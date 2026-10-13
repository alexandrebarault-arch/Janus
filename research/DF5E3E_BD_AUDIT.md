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
- In repository conventions `ScalarBackground.H` is the conformal Hubble rate `calH=a H_cosmic`. Along Case C with g-lapse `N=1`, `dot a = calH`; this conversion is now explicit in the audit code.

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

Their sum must equal the directly transformed `H[Z,Z]`. The helper also reconstructs `C_ZZ = H[Z,Zdot]` independently from the old basis.

## Active task list

- [x] DF5e.3e.1 — isolate BD-state audit from the physical solver.
- [x] DF5e.3e.2 — expose exact raw `h_ZZ` decomposition and independent `C_ZZ` reconstruction.
- [x] **DF5e.3e.3 — implement `C_ZZ(a)`, `dot C_ZZ`, the measure term and an explicit background-step convergence regression on exact Case C.**
- [ ] **DF5e.3e.4 — decompose `dot C_ZZ` into derivatives of `A`, `A_dot`, and the underlying old-basis Hessian entries; identify which term carries the O(1e3) residual. NEXT.**
- [ ] DF5e.3e.5 — rederive the offending old-basis state/rate entry directly from De Felice Eqs. (44), (45), (54), including `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2`.
- [ ] DF5e.3e.6 — compare the derived result to Eq. (79) `A,B,C,D`; do not tune coefficients.
- [ ] DF5e.4 — only after an exact mismatch is found, add a RED regression for that single coefficient, implement one fix, and require Eq. (78) NG3 green at `k=100,200,400,800`.
- [ ] DF5d — Candidate-C gravity branch only after Case C is green.

## Verification status

The new diagnostic tests are committed but have not been executed in this environment because the working container has no network access to clone the GitHub repository and GitHub Actions are disabled for this project. Do not claim them green until they are run in a repository worktree or another execution environment. Their purpose is to make the next run deterministic and falsifiable.

## Restart instruction

Resume at **DF5e.3e.4**.

1. Use exact Case C `a=0.05`, `k=400`, beta1 only, with the same `cs_f^2=0.1` diagnostic fluid used by `tests/test_de_felice_two_matter_action.py`.
2. Start from `case_c_bd_effective_coefficient()` and `bd_state_coefficient_decomposition()`; do not rebuild the background or Eq. (72) transform independently.
3. Differentiate each component of raw `h_ZZ` and the components entering `C_ZZ` with respect to `a`, convert with `dot a=calH`, and include the `3H` measure contribution.
4. Track separately derivatives of `A`, `A_dot`, and derivatives of the old-basis reduced-Hessian entries. The aim is to identify which exact term accounts for the O(1e3) residual in `h_ZZ^eff`.
5. Re-derive only that entry from the primary Eq. (44), Eq. (45) or Eq. (54), including the background k-essence drift `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2`.
6. Do not modify `de_felice_two_matter_action.py`, EH, matter or HR coefficients until one exact primary-equation mismatch is demonstrated.
7. After the first hard finding, update both this file and `GATE2B_CHECKPOINT.md`.
