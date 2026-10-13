# Gate 2B — RAF / restart ledger

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`

Read `research/GATE2B_CHECKPOINT.md` first.  This file is the short restart ledger.

## Current scientific position

The former scalar-physics blocker is closed at audit level:

- Case-C finite-k `NG3` recovered after pressure-consistent time-dependent BD canonicalization;
- Case-C Eq. (85) principal speeds recovered, including `c_s,grav^2 -> -0.666583341987...`;
- Candidate-C dust+dust benchmark recovered independently, `c_s,grav^2 -> 0.692071477288...`.

The repaired De Felice action does **not** project out the helicity-0 gradient.

Full-repository tests are still unavailable in the current environment.

## Current blocker

**Time-domain transfer architecture and exact dust variables.**

The raw P(X) second-order action is singular at `c_s^2=0`, so a long time-domain dust integration must not be performed by simply choosing an arbitrary finite sound speed.

A key regular variable has now been identified.  For one P(X) fluid,

`dL_m/d qdot = (rho+P)[(delta phidot/phidot - Phi)/c_s^2 + 3 psi]`.

Since

`delta rho = (rho+P)(delta phidot/phidot-Phi)/c_s^2`,

the canonical matter momentum is

`pi_q = delta rho + 3(rho+P) psi`

before sector volume factors.

In g-flat gauge, `psi_g=0`, so each visible-fluid canonical momentum is directly its density perturbation.  This is finite in the dust limit.

For a reduced physical Hessian

`Hphys=[[M,C],[C.T,K]]`

with common measure `a^3`, define

`pi = K Ydot + C.T Y`.

Then the exact first-order equations are

`Ydot = K^-1 (pi - C.T Y)`,

`pidot = M Y + C Ydot - 3 H pi`.

This formulation contains the full De Felice Eq. (84) but never evaluates `dot K` or `dot C`, avoiding the catastrophic cancellations encountered in the dispersion audit.

## Recommended next implementation order

1. **Two-dust late transfer first**, on the validated Candidate-C dust+dust action, starting at or below the clean late-linear threshold `m_eff/H=1` (`z ~= 16.25`).
2. Use canonical momenta/density variables so the dust limit is explicit rather than a finite-pressure approximation.
3. Compute the common/relative transfer from `z~16.25` to today and compare directly with the existing optimistic quasi-static reference (`~0.123` relative/common today).
4. If the exact late-linear conversion is still far below unity, record that as a robust negative result; visible radiation cannot change an order-of-magnitude conclusion in this domain.
5. Add the explicit visible-radiation scalar only when extending the transfer above the late regime or producing CMB/radiation-era observables.

Radiation-to-matter background ratio in the visible sector is

`rho_r/rho_m = (Omega_r0/Omega_m0)(1+z) = 3e-4(1+z)`.

Thus it is about

- `0.52%` at `z=16.25`;
- `0.33%` at `z=10`;
- `0.09%` at `z=2`;
- `4.3%` at `z=142`.

The two-dust solver is therefore a controlled late-regime falsification test, not a replacement for the eventual full radiation-era system.

## Remaining work

- [x] Case-C action/BD/NG3 reconstruction.
- [x] Case-C Eq. (85) three-speed validation.
- [x] Candidate-C dust+dust principal-speed validation.
- [ ] Derive/promote the canonical-momentum dust-limit reduced equations.
- [ ] Integrate Candidate-C dust+dust late transfer from `z~16.25` to 0.
- [ ] Track GR-connected/common and relative modes.
- [ ] Compute density/velocity transfer channels.
- [ ] Add visible radiation as a separate scalar for earlier epochs / exact Gate-2 observables.
- [ ] Full worktree regression suite.
- [ ] Final Gate-2B verdict.

## Do not redo

Unless new evidence appears, do not return to:

- Eq. (44)/(45)/(54) coefficient tuning;
- Eq. (72) normalization;
- the `dot(phi_f)/phi_f` sound-speed term;
- the old frozen speed extractor as a physical FLRW acceptance equation;
- the claim that the action intrinsically lost the helicity-0 gradient.
