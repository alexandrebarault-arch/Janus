# V2 regular-center LTB-LTB gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `SIMPLE_COMOVING_LTB_VOID_ROUTE_DOWNGRADED`

## 1. Source result

Nersisyan, Akrami & Amendola (2015), arXiv:1502.03988, analyze metric combinations in Hassan-Rosen bigravity. For the consistent LTB-LTB subclass they use

`g = -dt^2 + A(t,r)^2 dr^2 + B(t,r)^2 dOmega^2`

and

`f = -X(t)^2 dt^2 + Y(t,r)^2 dr^2 + Z(t,r)^2 dOmega^2`.

The Bianchi/off-diagonal constraints imply the separable forms

`B = B_e(t) s(r)`,
`Z = Z_e(t) s(r)`,
`A = A_e(t) q(r)`,
`Y = Y_e(t) q(r)`,

with

`A_e = C1 B_e`,
`Y_e = C2 Z_e`.

Their remaining radial consistency conditions are

`s'^2/q^2 - 1 = C3 s^2`,

`s' q' - q s'' = C4 s q^3`.

## 2. Direct reduction

From the first condition,

`q = s' / sqrt(1 + C3 s^2)`

(up to the radial orientation sign).

Differentiating this and inserting into the second condition gives

`C4 = -C3`

for the nontrivial region away from the center.

Now introduce the radial coordinate

`chi = s(r)`.

The g-sector spatial metric is

`dl_g^2 = B_e(t)^2 [ C1^2 dchi^2/(1+C3 chi^2) + chi^2 dOmega^2 ]`.

Near a regular spherical center (`chi -> 0`), the proper radial distance is approximately

`ell ~= B_e C1 chi`,

while the areal radius is

`R_areal ~= B_e chi`.

Elementary flatness therefore requires

`C1 = 1`.

The same argument gives

`C2 = 1`

for the f metric.

Consequently the regular-center metrics reduce to

`dl_g^2 = B_e(t)^2 [ dchi^2/(1+C3 chi^2) + chi^2 dOmega^2 ]`,

`dl_f^2 = Z_e(t)^2 [ dchi^2/(1+C3 chi^2) + chi^2 dOmega^2 ]`,

apart from the f lapse `X(t)`.

This is simply the standard constant-curvature FLRW spatial geometry with

`k = -C3`.

## 3. Interpretation

Within this separable/comoving perfect-fluid LTB-LTB subclass, imposing a regular center removes the apparent local radial inhomogeneity: both metrics become FLRW-like with the same spatial curvature profile.

Therefore this particular LTB-LTB route does **not** provide the gradient-resolved localized void that JANUS-R needs.

This is stronger than the qualitative statement "LTB-LTB is allowed": the special allowed subclass collapses to standard constant-curvature spatial geometry once regular-center conditions are imposed.

## 4. Scope / non-overclaim

This is **not** a no-go theorem for every spherically symmetric bimetric void.

The derivation inherits the assumptions of the 2015 ansatz:

- simultaneous diagonal/comoving LTB form;
- f lapse depending on time only;
- separability forced by their Bianchi/off-diagonal equations;
- ordinary perfect-fluid form used in their consistency scan.

JANUS-R with two separately coupled matter sectors may require a more general spherical geometry, e.g.

- Lemaître rather than LTB, with spatially varying lapse/pressure;
- relative radial velocities/fluxes between sectors;
- nonzero shifts / metrics not simultaneously bidiagonal;
- fully dynamical 1+1 spherical evolution.

Twin matter does not automatically remove the geometric off-diagonal/Bianchi restrictions, so the simple comoving LTB ansatz should not be assumed viable without a new derivation.

## 5. Full static-gradient control already exists

Aoki, Maeda & Tanabe (2016), arXiv:1602.02227, derive the full static bidiagonal spherical equations with two separately coupled perfect-fluid matter sectors.

In gauge `r_g=r`, they have:

- four first-order Einstein equations for `N_g,F_g,N_f,F_f`;
- two matter conservation equations;
- one Bianchi/interation constraint;
- after differentiating the constraint, seven first-order ODEs including the radial-coordinate ratio variable `mu=r_f/r_g-1`.

Thus a genuine radial-gradient ODE skeleton already exists and should be used as a control rather than inventing a smoothing prescription for the weak-field algebraic AMN branch endpoint.

The same paper explicitly notes that when `rho_g ~ rho_f`, the asymptotically homothetic static branch generally cannot be extended inward, except for the exactly tuned homothetic matter relation.

This independently reinforces the branch-selection problem already seen in the repository's static diagnostics.

## 6. Decision

`SEPARABLE_REGULAR_LTB_LTB_LOCAL_VOID = FAIL_AS_DISTINCT_INHOMOGENEOUS_ROUTE`

`FULL_STATIC_TWO_MATTER_GRADIENT_ODE = AVAILABLE_AS_CONTROL`

`GENERAL_DYNAMICAL_SPHERICAL_TWO_MATTER_VOID = STILL_OPEN`

## 7. Next step

Do not build the cosmological void solver from the separable LTB-LTB ansatz above.

Instead:

1. encode/reproduce the Aoki-Maeda-Tanabe full static gradient system as a validation/control problem;
2. formulate the minimally more general dynamical spherical ansatz needed for a regular void (likely Lemaître/ADM with nontrivial lapse/relative flow);
3. derive its Hassan-Rosen interaction/Bianchi equations with both matter sectors;
4. only then solve the compensated void transition wall and apply full perturbative stability tests.

## 8. Reproducibility

The algebraic regular-center reduction is encoded in

`numerics/ltb_regular_center.py`

with tests in

`tests/test_ltb_regular_center.py`.

Manual TDD verification:

- RED: `ModuleNotFoundError` before implementation;
- GREEN: `3 passed in 0.03s` after implementation.
