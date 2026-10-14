# Non-homothetic screened-to-linear transition derivation

Date: 2026-10-14
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **KINEMATICS + HR WEAK-METRIC SOURCE LAYER DERIVED; DYNAMICAL TRANSITION NOT YET CLOSED**

## Purpose

Gate 2B is now blocked by two helicity-0 phase-space data that the late exact-dust linear system cannot determine.  They must come from a preceding nonlinear/screened evolution through the region `H ~ m_eff`.

The goal of this derivation is therefore not to tune `(Y3,Y3_N)`, but to construct the smallest non-homothetic nonlinear scalar system that can transport the missing canonical pair from the screened phase to the principal-stable late linear phase.

## Literature ruling

Aoki, Maeda & Namba (2015) provide the relevant nonlinear spherical Stueckelberg reduction around their constant-`K` cosmological setup.  Their adiabatic `mu` equation is algebraic and explicitly omits the dynamical scalar-graviton oscillation mode; they state that around a sufficiently fast `H ~ m_eff` transition the adiabatic approximation can fail and a numerical dynamical treatment is needed.

Lueben, Schmidt-May & Smirnov (2020) demonstrate cosmological Vainshtein screening on the finite FLRW branch and define a background Stueckelberg-like quantity `mu_bg = y'/y`.  This is determined algebraically by the background branch and transitions from order unity at early times to zero at late times.  It is **not** the perturbative nonlinear spherical scalar `mu(eta,r)` and does not provide the two late canonical matching data.

No located reference supplies the required nonlinear perturbative transition on a time-dependent non-homothetic two-matter background.

## 1. Correct non-homothetic Stueckelberg map

Use g-sector conformal coordinates `(eta,r)`.  Candidate C has

`b(eta) = a(eta) xi(eta)`

and the natural f conformal time satisfies

`d eta_f_bar / d eta = c(eta)`.

The nonlinear relative-coordinate map is therefore

`eta_f = eta_f_bar(eta) + sigma(eta,r)`,

`r_f = (1 + mu(eta,r)) r`.

Its exact radial Jacobian is

`J = [[c + sigma_dot, sigma_prime], [r mu_dot, 1+mu+r mu_prime]]`.

For an unperturbed f FLRW metric,

`ds_f^2 = b^2[-d eta_f^2 + d r_f^2 + r_f^2 dOmega^2]`,

the pulled-back radial block is

`f_ab = b^2 J^T diag(-1,1) J`.

This reproduces the exact Candidate-C background at `mu=sigma=0` and reduces to the Aoki off-diagonal kinematics when `c=1`, `b=K a`.

Implemented:

- `numerics/nonhomothetic_stueckelberg_spherical.py`
- `tests/test_nonhomothetic_stueckelberg_spherical.py`

## 2. Exact HR square root for the spherical pullback

For the radial two-by-two block, define

`A = g^{-1} f`.

Its principal square root is evaluated exactly as

`S = [A + sqrt(det A) I] / sqrt(tr A + 2 sqrt(det A))`.

The two angular eigenvalues are equal.  From the radial trace/determinant and angular eigenvalue, the full four-dimensional elementary symmetric polynomials `e_0...e_4` are reconstructed exactly.

Controls passed:

- `S^2=A` for a generic nonlinear map;
- background non-homothetic eigenvalues are `(xi c, xi, xi, xi)`;
- homothetic limit gives `e_n = C(4,n) K^n`.

Implemented:

- `numerics/nonhomothetic_hr_spherical.py`
- `tests/test_nonhomothetic_hr_spherical.py`

## 3. Weak metric potentials with nonlinear Stueckelberg fields

Keep the metric potentials weak but do **not** expand `mu` or `sigma`.

For g Newtonian gauge,

`ds_g^2 = a^2[-(1+2 Phi_g)deta^2 + (1-2 Psi_g)(dr^2+r^2dOmega^2)]`.

For f in its natural coordinates,

`ds_f^2 = b^2[-(1+2 Phi_f)deta_f^2 + (1-2 Psi_f)(dr_f^2+r_f^2dOmega^2)]`,

then pull back with the exact nonlinear Jacobian above.

Implemented:

- `numerics/nonhomothetic_stueckelberg_weak_metric.py`
- `tests/test_nonhomothetic_stueckelberg_weak_metric.py`

Targeted RED->GREEN control: `3 passed`.

## 4. Weak-metric HR interaction source layer

The exact standard-beta interaction density per spherical angular Jacobian is

`m^2 M_g^2 sqrt(-g) sum beta_n e_n(S)`.

The metric potentials are kept inside the exact square root while `mu,sigma` remain nonlinear.

Implemented:

- `numerics/nonhomothetic_hr_weak_spherical.py`
- `tests/test_nonhomothetic_hr_weak_spherical.py`

### Homothetic Aoki controls

A strong convention check is possible without importing the published source formulas into production code.

Let

`D = b1 + 2 K b2 + K^2 b3`,

`beta2_A = (K b2 + K^2 b3)/D`,

`beta3_A = K^2 b3/D`.

After subtracting the `mu=0` background, the exact derivative of the HR potential with respect to the g lapse gives

`delta(dV/dPhi_g) = 3 m^2 M_g^2 a^4 K D [mu + beta2_A mu^2 + beta3_A mu^3/3]`.

This is exactly the interaction polynomial entering Aoki Eq. (5.2).

To recover the radial source one must vary radial and angular spatial metric factors independently before imposing Newtonian-gauge isotropy.  The radial variation combines with one third of the lapse variation to give

`m^2 M_g^2 a^4 K D [-mu + beta3_A mu^3/3]`,

which is exactly the mass polynomial in Aoki Eq. (5.3).

For the f sector the source must first be converted from g radial coordinate volume to the physical f coordinate volume.  For the static homothetic map this contributes the Jacobian factor `(1+mu)^-3`.

After that conversion, the lapse source becomes

`-3 m^2 M_g^2 a^4 K D /(1+mu)^3`
` * [mu + (1+beta2_A)mu^2 + (1+beta2_A+beta3_A)mu^3/3]`,

matching the polynomial of Aoki Eq. (5.4).

The corresponding radial combination is

`+m^2 M_g^2 a^4 K D /(1+mu)^3`
` * [mu + 2mu^2 + (2+2beta2_A-beta3_A)mu^3/3]`,

matching Aoki Eq. (5.5).

These identities fix the interaction sign conventions, factors of three, normalized coupling map, and the f-coordinate Jacobian independently.

Targeted reconstructed-workspace result for the weak HR controls after the latest additions: `7 passed`.  This is not a full-repository-suite claim.

## 5. Important failed shortcut

The HR potential alone does **not** reproduce the Aoki Stueckelberg constraint `sigma' = -r mu_dot` in the static homothetic limit.

This is expected after tracing the Aoki derivation: their constraint is obtained only after the weak metric potentials have been solved from the Einstein equations and substituted into interaction conservation.

Therefore the next system must retain

`Phi_g, Psi_g, Phi_f, Psi_f`

as weak auxiliary fields while keeping

`mu, sigma`

nonlinear.

A sign tweak or a potential-only equation for `mu` would be structurally wrong.

## 6. Full Aoki polynomial proxy result

The complete algebraic Aoki Eq. (5.8), evaluated instantaneously on Candidate C with exact polynomial coefficients, shows that the early screened algebraic branch remains real and simple but does not approach `mu=0` near the late linear stability boundary.

At `a ~= 0.10165`, the tracked branch remains near `mu ~= -0.667`, with root separation about `0.21`.

Small equal-source sensitivity probes do not close the gap.

See:

- `numerics/candidate_c_aoki_full_proxy.py`
- `tests/test_candidate_c_aoki_full_proxy.py`
- `research/CANDIDATE_C_AOKI_FULL_POLYNOMIAL_AUDIT.md`

Ruling: if Candidate C survives, the screened-to-linear connection must be genuinely non-adiabatic/dynamical; an algebraic root continuation is insufficient.

## Current derivation status

Closed:

- exact non-homothetic spherical Stueckelberg kinematics;
- exact spherical HR square-root invariants;
- weak-metric/nonlinear-Stueckelberg HR interaction density;
- all four homothetic Aoki weak-metric mass-source polynomials recovered from the exact interaction;
- early algebraic branch shown not to adiabatically approach `mu=0` in the full-polynomial instantaneous proxy.

Open:

1. derive the weak Einstein constraint operators on the time-dependent non-homothetic background, including the terms proportional to `H`, `xi_dot` and `c_dot` that disappear in the static/homothetic control;
2. solve the four weak metric potentials as auxiliaries in the sub-horizon nonlinear-Stueckelberg regime;
3. substitute them into interaction conservation / the reduced action and derive the dynamical `sigma-mu` system;
4. verify the `c->1`, `xi->K` limit reproduces Aoki Eq. (4.31) and Eq. (5.8);
5. linearize the new system at small `mu,sigma` and match its canonical pair to the already validated late exact-dust helicity-0 `(Y3,Y3_N)` sector;
6. only then evolve through `H~m_eff`.

## Acceptance rule for the transition

A Candidate-C transition is acceptable only if one continuous solution can evolve from the screened branch to a principal-stable late linear surface while maintaining:

- real metric/Stueckelberg square root;
- orientation `mu>-1`;
- nonsingular weak metric constraint matrix;
- no kinetic zero of the dynamical helicity-0 mode;
- finite `d mu/dN` and canonical momentum;
- continuous mapping onto the late `(Y3,Y3_N)` pair.

Until this is shown, Gate 2B remains open and no unique late transfer function is claimed.
