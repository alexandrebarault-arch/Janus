# Late Dust Canonical Transfer Solver — Design

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Status: design specification; implementation has not started.

## 1. Purpose

Build the first trustworthy time-domain scalar transfer solver for the validated Hassan-Rosen / De Felice reconstruction on Candidate C.

The first production target is deliberately narrower than the final Gate-2 system:

- Candidate-C background;
- visible dust + twin dust;
- late linear interval from the clean transition `m_eff/H ~= 1` at `z_i ~= 16.2455` to `z=0`;
- the validated three physical scalar degrees of freedom;
- density observables in both matter sectors;
- continuous tracking of the GR-connected adiabatic mode;
- measurement of spontaneously generated relative/isocurvature amplitude.

This subsystem is a falsification test for the proposition that the late linear Candidate-C phase can create an order-unity relative mode from adiabatic initial data.

It is not yet the final baryon+CDM+radiation+CMB transfer solver.

## 2. Scientific scope and controlled approximation

At the start of the proposed late interval (`z ~= 16.25`), the visible radiation-to-matter background ratio is only about `0.52%`; it decreases thereafter.  Omitting radiation is therefore a controlled approximation for the first late-linear conversion test.

The approximation is acceptable for answering:

> Can the clean late linear phase generate a large relative mode by itself?

It is not acceptable for recombination-era transfer functions, CMB observables, or precision early-time initial conditions.  A three-fluid extension remains a later Gate-2 task if the late dust test survives falsification.

## 3. Why the old time-domain routes are not reused

The historical Comelli 12x12 closure is not an allowed input because it projected out the correct helicity-0 high-k structure.

The old frozen-Hessian mode equation is not an allowed evolution equation because De Felice Eq. (84) contains coefficient-time-derivative and measure terms.

A direct finite-`c_s^2` P(X) dust regulator is not a production solution.  In the unreduced field action the dust limit is singular, and keeping a small nonzero sound speed would introduce a fictitious acoustic scale at large `k`.

The new solver must inherit its coefficients from the already validated exact-quadratic De Felice/Hassan-Rosen action path.

## 4. Chosen architecture

### 4.1 Regular dust phase action

Perform the Legendre transform of each P(X) matter coordinate before taking `c_s^2 -> 0`.

For one matter sector, let

- `A = rho + P`;
- `q = delta_phi / dot(phi)`;
- `Phi` be the De Felice lapse perturbation;
- `psi` be the scalar spatial curvature perturbation;
- `s = c_s^2`.

The temporal part of De Felice Eq. (54) can be written as

`L_temp = A/(2s) (qdot-Phi)^2 + 3 A psi (qdot-Phi) + A Phi^2/2`.

Its momentum is

`p = A[(qdot-Phi)/s + 3 psi]`.

Equivalently,

`p = delta_rho + 3 A psi`.

The Legendre transform has the regular dust limit

`L_dust,temp = p (qdot-Phi) + A Phi^2/2`.

Including the spatial term, the common-normalized dust matter sector is therefore first order in `(q,p)` and contains no artificial dust sound speed.

For the f sector the full common-normalized momentum contains the usual background prefactor `n xi^3`; the physical density is reconstructed by dividing that prefactor and subtracting `3 rho_f psi_f`.

### 4.2 Metric action

Reuse only validated pieces:

- De Felice Eq. (44) EH scalar action;
- direct O(delta^2) HR interaction from Eqs. (45)-(46), including the corrected shift-volume terms;
- the regular dust phase actions above.

Do not finite-difference the nonlinear HR potential to recover a quadratic Hessian in the time-domain solver.

### 4.3 Gauge and algebraic reduction

Use the same g-flat gauge and background conventions as the validated DF5 reconstruction.

Metric lapses and shifts remain algebraic and are eliminated from the quadratic/first-order action, not from an independently transcribed Einstein-equation closure.

The remaining BD scalar is removed using the same time-dependent integration-by-parts identity validated in DF5e.4.  Boundary-term momentum shifts must be retained because they are needed to reconstruct the raw matter momenta and hence the physical densities.

The final physical phase space has six dimensions: three physical scalar coordinates and their three canonical momenta.

## 5. Evolution equations

For the reduced physical action written as

`L = a^3 [ 1/2 Ydot^T K Ydot + Y^T C Ydot + 1/2 Y^T M Y ]`,

define the canonical momentum

`Pi = K Ydot + C^T Y`.

The evolution equations are

`Ydot = K^{-1}(Pi - C^T Y)`,

`Pidot = M Y + C Ydot - 3 H Pi`,

for g-cosmic lapse `N=1`.

This formulation is the production route because it implements the full time-dependent Euler-Lagrange equation without explicitly differentiating `K` or `C`.  It therefore avoids the catastrophic cancellations encountered in the direct numerical reconstruction of De Felice Eq. (85).

The independent Eq. (85) high-precision audit remains a regression oracle, not the time integrator.

## 6. Background provider

The solver uses the Candidate-C algebraic healthy branch from `flrw_two_matter.py` / `candidate_c_transfer.py`.

For the dust+dust late benchmark, the visible background density supplied to the perturbation action is the visible matter component only.  Radiation is omitted from both perturbations and the dust action for this first test.

Background metric quantities, branch derivatives, `J`, `Gamma`, lapse ratio and interaction coefficients must remain those of the chosen Candidate-C benchmark and must be generated from one consistent on-shell provider.

No derivative may be taken by varying action coefficients along an off-shell neighboring family.

## 7. Observable reconstruction

The primary outputs are sector density contrasts, not canonical coordinates.

At each time step:

1. recover `Ydot` from `(Y,Pi)`;
2. reconstruct the algebraic BD variable `Z` from the pre-Schur canonical action;
3. reconstruct the canonical momenta before the `Y_i Zdot` integration-by-parts boundary transformation;
4. use the exact Eq. (72) basis map to identify the original matter momenta associated with `q_g` and `q_f`;
5. reconstruct local matter density perturbations from
   `p_matter = delta_rho + 3 (rho+P) psi`;
6. for the f sector divide the common-normalization prefactor `n xi^3` before subtracting the curvature term;
7. report `delta_g = delta_rho_g/rho_g` and `delta_f = delta_rho_f/rho_f`.

The momentum shift from the time-dependent integration by parts is explicit.  If the dropped boundary function is

`F = sum_{i!=Z} c_i Y_i Z + 1/2 c_Z Z^2`,

then the pre-canonical momenta are recovered from

`Pi_before = Pi_after + dF/dY`.

This observable map receives its own finite-sound-speed regression before the exact dust solver is trusted.

## 8. Initial conditions and mode tracking

The solver's primary mathematical product is the full six-dimensional fundamental matrix.  No 2x2 density transfer matrix is defined by silently choosing arbitrary initial velocities.

For the first scientific test, initialize and track the GR-connected adiabatic growing mode at `z_i ~= 16.2455`:

- no initial relative entropy between the two dust sectors;
- common growing density perturbation normalized to unity;
- the phase-space direction selected by continuity with the regular GR-connected local mode, not by setting all unused canonical variables to zero.

At each later time, track the same mode continuously by overlap with the previous normalized phase-space eigenvector / evolved solution.  Avoid re-sorting modes independently at every time.

Define the diagnostic amplitudes

`delta_common = (rho_g delta_g + rho_f_eff delta_f)/(rho_g + rho_f_eff)`

and

`delta_relative = delta_g - delta_f`.

The exact weighting `rho_f_eff` used for the common source is taken from the same background normalization entering the two-sector action; it is not hard-coded from the equal-density Aoki reference system.

The key late-conversion observable is

`R(a,k) = delta_relative / delta_common`

for the initially adiabatic mode.

## 9. Transfer matrices

The full six-dimensional fundamental matrix is authoritative.

A reduced `2 x 2` density transfer matrix `T_gg,T_gf,T_fg,T_ff` is exported only after an explicit two-dimensional regular input lift is defined and regression-tested.

The input lift must specify both density and velocity/phase information.  The preferred basis is:

1. the GR-connected common growing mode;
2. the regular relative/isocurvature mode.

After these two phase-space directions are fixed, they can be transformed to and from the sector-density basis to report `T_gg,T_gf,T_fg,T_ff` without hidden initial-condition conventions.

Until that lift is validated, reports must use the six-dimensional fundamental matrix and the adiabatic conversion ratio `R`, not an ambiguous 2x2 matrix.

## 10. Numerical integration

Use `N = ln a` as the integration variable for the production solver.

The conversion from g-cosmic time is

`d/dN = (1/H_g) d/dt`.

Requirements:

- adaptive integration with explicit relative/absolute tolerances;
- condition-number monitoring for `K`, auxiliary Schur blocks and the BD algebraic coefficient;
- event/fail-fast checks for loss of branch regularity, rank changes or non-finite coefficients;
- optional fundamental-matrix QR re-orthogonalization if basis growth causes severe conditioning, while the single adiabatic-mode run is integrated directly;
- outputs sampled on a deterministic `N` grid for reproducible regressions.

## 11. Validation sequence

Implementation follows TDD and must pass these gates in order.

### V1 — one-sector dust Legendre identity

At finite `c_s^2`, compare the Hamilton/phase reconstruction against the existing P(X) action and verify the momentum identity

`p = delta_rho + 3(rho+P)psi`.

Then verify the analytic `c_s^2 -> 0` phase action is finite.

### V2 — synthetic time-dependent quadratic system

For known time-dependent `K,C,M`, verify the canonical first-order equations reproduce the second-order Euler-Lagrange solution.

### V3 — Case C local principal regression

Linearize/freeze the new phase system locally and recover the already closed Case-C high-k branches, including gravitational `c_s^2 -> -0.666583341987...`.

### V4 — Candidate-C local regression

At `a=0.5`, recover the dust+dust principal target

`c_s^2 -> 0.692071477288...`

and the two dust matter branches in the appropriate zero-sound-speed limit.

### V5 — observable pullback

At finite regulator sound speed, compare density perturbations reconstructed from the canonical observable map with the direct P(X) density formula before taking the dust limit.

### V6 — GR/decoupling control

In a controlled GR/decoupled limit, recover the standard pressureless growing and decaying modes and verify that an exactly adiabatic common mode does not spuriously generate a relative mode.

### V7 — Candidate-C late integration

Integrate from `z_i ~= 16.2455` to `z=0` on several representative Fourier scales covering the existing quasi-static table, at minimum `k = 0.01, 0.05, 0.1, 0.2 h/Mpc`.

Report:

- `delta_g(a,k)`;
- `delta_f(a,k)`;
- `delta_common`;
- `delta_relative`;
- `R(a,k)`;
- kinetic/BD/auxiliary conditioning diagnostics.

## 12. Scientific decision rule for the first late solver

The previous deliberately optimistic quasi-static reference found a late relative/common amplitude of order `0.123`, not order unity.

The new solver is allowed to disagree with that estimate; the estimate is not a target to fit.

The late-linear spontaneous-conversion hypothesis is strongly disfavored if the validated relativistic solver keeps `|R(z=0,k)| << 1` over the relevant linear scales starting from the GR-connected adiabatic mode.

If instead `|R|` becomes order unity, the result is not accepted automatically: the run must also retain regular auxiliary/BD elimination, positive kinetic signatures where required, and continuous mode identity.

## 13. Explicit non-goals of this subsystem

This implementation does not yet:

- include visible radiation perturbations;
- include separate baryon and CDM perturbations;
- start at recombination;
- compute CMB transfer functions;
- solve the nonlinear `H ~ m_eff` transition;
- claim the full Gate-2 verdict;
- replace the documented nonlinear-screening Gate 3.

Those extensions are justified only after the late dust solver passes its own validation gates.

## 14. Files / component boundaries

The implementation should preserve small, auditable modules:

- new dust phase-action module: analytic regular dust matter sector and finite-`c_s^2` comparison bridge;
- new reduced phase-system module: auxiliary/BD reduction and `K,C,M` / canonical RHS assembly;
- new Candidate-C late-transfer module: background sampling, mode initialization/tracking, integration and observable output;
- new tests split by the validation sequence V1-V7;
- existing `de_felice_two_matter_exact_quadratic.py`, `bd_time_canonicalization.py`, `de_felice_action_principal.py`, and Candidate-C background helpers remain independent regression oracles rather than being duplicated.

No changes to EH, HR or previously audited P(X) coefficients are permitted merely to make the transfer result look desirable.
