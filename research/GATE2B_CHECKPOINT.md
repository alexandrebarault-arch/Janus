# Gate 2B — authoritative restart checkpoint

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Purpose: single restart point after interruption.

## Verdict

**Gate 2B remains OPEN / NOT YET FULLY VALIDATED, but the former high-k scalar-physics blocker is CLOSED at the scientific-audit level.**

The repaired De Felice/Hassan-Rosen action path now reproduces:

- the correct scalar degree count;
- the published finite-k kinetic invariant `NG3` on Case C;
- all three Case-C principal scalar propagation branches from the actual De Felice Eq. (85);
- the healthy positive Candidate-C helicity-0 speed on an independent dust+dust non-homothetic benchmark.

The remaining work is no longer “find the missing helicity-0 gradient.”  It is to promote the validated action reduction into a time-domain transfer system with the correct matter content and then quantify common/relative mode conversion.

The physical Candidate C contains g-dust + g-radiation + f-dust.  The current two-matter reducer has only one matter scalar on each metric, so a full transfer calculation must either explicitly add the extra visible-radiation scalar or deliberately restrict itself to a controlled late dust+dust regime.

## Closed hard facts

### Conventions / backgrounds

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi J`, `f1=Gamma`.
- Exact beta1 Case C: `numerics/comelli_case_c.py`.
- Candidate C: `numerics/flrw_two_matter.py::candidate_c()`.
- Independent principal gravity targets:
  - Case C at `a=0.05`: `c_s^2=-0.6665833419871022`;
  - full Candidate C at `a=0.5`: `c_s^2=0.6920799926788032`;
  - dust+dust Candidate-C benchmark at `a=0.5`: `c_s^2=0.6920714772884699`.

The dust-benchmark shift from the physical-radiation target is only about `1.2e-5` relative at `a=0.5`.

### Action blocks / historical fixes

- Eq. (44) EH scalar contractions audited.
- Eq. (54) P(X) matter action audited.
- Direct O(delta^2) HR interaction is `hr_scalar_quadratic_action_density_de_felice()`.
- Missing HR shift-volume terms were found and fixed (`8637753`, regression `181deda`).
- Eq. (72) normalization is correct: `1/(n H_f)=a/H_omega`.
- f-field drift is correct and must retain
  `dot(phi_f)/phi_f = dot(n)/n - 3 n H_f c_sf^2`.
- GR one-metric scalar degeneracy is preserved.

## DF4 — scalar degree count CLOSED

The Eq. (72) basis exposes one algebraic BD scalar.  Before its removal the `Zdot` kinetic direction is null.  After Schur elimination exactly three scalar kinetic directions remain for the two-fluid problem.

NG2 agrees with De Felice Eq. (78) at high accuracy in the audited reconstruction.

## DF5e.3 / DF5e.3e — origin of the old NG3~k^2 branch CLOSED

Before proper time-dependent BD elimination the rate/auxiliary Schur leaves

`K_Y3Y3 -> a^2 xi k^2/[4(c+1)]`.

On early Case C this explains the old `NG3~k^2` branch.

The apparently wrong algebraic coefficient `h_ZZ^eff ~ -2.15e3` was traced to differentiating `C_ZZ(a)` while freezing `P_f=0` at neighboring points despite finite diagnostic `c_sf^2`.

For barotropic P(X),

`dot P_f = c_sf^2 dot rho_f = -3 n H_f c_sf^2 (rho_f+P_f)`.

At `a=0.05,k=400,c_sf^2=0.1`, the omitted pressure contribution to `dot C_ZZ` is about `-2160.22`, moving the algebraic coefficient to the required O(1) value near `6.741...`.

No EH, matter, HR, or Eq. (72) coefficient was tuned.

## DF5e.4 — time-dependent BD canonicalization IMPLEMENTED

Committed components:

- `numerics/bd_time_canonicalization.py`;
- `numerics/de_felice_two_matter_exact_quadratic.py`;
- pressure-consistent adapter in `numerics/de_felice_bd_audit.py`;
- regressions for pressure chain rule, generic integration by parts, and four-k Eq. (78) NG3.

For `H=[[M,C],[C.T,K]]`, BD index `z`, `c_i=C[i,z]`, and `mu=d ln(Na^3)/dt`, the canonicalizer applies

- `C_new[z,i]=C[z,i]-c_i` for `i!=z`;
- `C_new[:,z]=0`;
- `M_new[i,z]=M[i,z]-(dot c_i+mu c_i)`;
- `M_new[z,z]=M[z,z]-(dot c_z+mu c_z)`.

At `N=1`, `mu=3H_cosmic`.

Fresh executable-subset NG3 values satisfy the existing 3% Eq. (78) tolerance at `k=100,200,400,800`.

## DF5e.5 — actual De Felice Eq. (85) dispersion CLOSED on Case C

The old helper `physical_squared_phase_speeds()` freezes the reduced matrices.  That is not the De Felice FLRW dispersion equation once coefficient time dependence is restored.

In repository Hessian conventions,

`Hphys=[[M,C],[C.T,K]]`,

Eq. (84) becomes

`K Yddot + A Ydot + B Y = 0`,

with

`A = dot K + 3 H K + C.T - C`,

`B = dot C.T + 3 H C.T - M`.

The characteristic equation is Eq. (85):

`det(K lambda^2 + A lambda + B)=0`.

### Crucial background-derivative fix

For the finite P(X) sound-speed regulator, neighboring points must lie on one locally on-shell regulated family.  Keeping the exact dust metric trajectory while assigning finite `c_sf^2` makes `c_prime`, `H_omega_prime`, and subsequent coefficient derivatives inconsistent.

For beta1 Case C the regulated local family follows

`a^-4 + xi - xi^2 rho_f/3 - 1/(3xi) = 0`,

`c = 1 + a xi_a/xi`,

`rho_f,a = -3 c (rho_f+P_f)/a`,

`P_f,a = c_sf^2 rho_f,a`.

At the control point this reproduces the exact dust `xi_a` but supplies the correct regulated higher background derivatives.

### Conditioned result

Using:

- an algebraically exact quadratic Hessian;
- the locally on-shell regulated trajectory;
- DF5e.4 time-dependent BD canonicalization;
- 70-80 digit arithmetic;
- symmetric seven-point coefficient derivatives;

removes the spurious high-k derivative growth.  For example the gravity-direction `dot K+3HK` coefficient stays O(H), rather than scaling as `k^2`.

Case-C principal mode pairs converge as

- gravity: `-0.6858646, -0.6714442, -0.6678011, -0.66688795, -0.66665950` at `k=400,800,1600,3200,6400`;
- g matter -> `1/3`;
- f matter -> `c^2 c_sf^2`.

A `c0+c2/k^2+c4/k^4` fit over `k=800...6400` gives

`c0=-0.6665833422935964`,

versus independent target

`-0.6665833419871022`.

Relative difference: about `4.6e-10`.

See `research/DF5E5_EQ85_ONSHELL_AUDIT.md`.

## DF5d / T2 — Candidate C dust+dust benchmark CLOSED

The same pipeline was generalized to the actual Candidate-C beta parameters and `kappa`, with visible radiation temporarily removed so that the physical system is exactly one dust fluid per metric.

At `a=0.5` the dust+dust branch has approximately

- `xi=0.5682425064594762`;
- `ctilde=0.9370846292570983`.

With local P(X) regulators `c_s,g^2=c_s,f^2=0.1`, Eq. (85) gives at high k:

- g matter -> `0.1`;
- f matter -> `ctilde^2*0.1 ~= 0.08781276024`;
- gravity -> `0.692071477...`.

Representative gravity values:

- `k=400`: `0.69418361`;
- `k=800`: `0.69259706`;
- `k=1600`: `0.69220272`;
- `k=3200`: `0.69210428`;
- `k=6400`: `0.69207968`.

A `1/k^2+1/k^4` extrapolation gives `0.6920714772308268`, versus the independent dust+dust target `0.6920714772884699` (relative difference about `8.3e-11`).

See `research/DF5D_CANDIDATE_C_DUST_AUDIT.md`.

**Conclusion:** the repaired action/reduction is not a special Case-C fix.  It transfers to a healthy non-homothetic Candidate-C background.

## What is now obsolete

The old statement that the reconstructed scalar action “projects out the helicity-0 high-k gradient” is no longer correct for the repaired De Felice path.

The old frozen `physical_squared_phase_speeds()` remains useful only as a synthetic/frozen-coefficient utility; it is not the final FLRW acceptance equation.

The historical 12x12 Comelli closure can still be studied to identify what it projected out, but it is no longer the only route to the transfer problem.

## Remaining Gate 2B work

- [x] convention bridge / exact Case-C background.
- [x] independent De Felice high-k gravity target.
- [x] EH / matter / HR action audits.
- [x] DF3 / DF4 scalar degree count and BD basis.
- [x] DF5e.2 HR shift-volume fix.
- [x] DF5e.3 rate/auxiliary Schur localization.
- [x] DF5e.3e pressure-chain diagnosis.
- [x] DF5e.4 time-dependent BD kinetic canonicalization + finite-k NG3.
- [x] DF5e.5 Case-C Eq. (85) three-speed recovery.
- [x] DF5d/T2 Candidate-C dust+dust gravity-speed recovery.
- [ ] **Transfer architecture: decide controlled two-dust late solver vs explicit third visible-radiation scalar. NEXT.**
- [ ] Promote conditioned Eq. (85)/time-dependent reduction into reusable production code rather than scratch high-precision audit.
- [ ] Build time-domain fundamental transfer matrix.
- [ ] Track GR-connected adiabatic/common and relative/isocurvature modes continuously.
- [ ] Compute `T_gg,T_gf,T_fg,T_ff` and relative growth.
- [ ] Quantify impact of visible radiation if starting above the clean late regime.
- [ ] Full Gate-2B regression suite in an actual repository worktree.
- [ ] Final Gate-2B scientific verdict.

## Current verification limitation

GitHub Actions are disabled and the container still cannot clone the full repository.  The high-precision DF5e.5/DF5d audits were executed in a minimal workspace reconstructed from repository formulas and committed parameters.  Do not claim the full repository suite is green until it runs in a real worktree.

## Immediate restart instruction

Resume from **transfer architecture**.

The scientific action path is now validated on both Case C and a non-homothetic Candidate-C two-dust benchmark.  Before writing the time-domain solver, preserve the physical matter degree count:

- full Candidate C has g-dust + g-radiation + f-dust;
- one P(X) scalar per metric is insufficient for the exact full scalar spectrum;
- a dust+dust late solver is a controlled approximation only if its domain and radiation error are stated explicitly.
