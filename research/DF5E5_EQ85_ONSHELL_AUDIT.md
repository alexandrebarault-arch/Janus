# DF5e.5 — De Felice Eq. (85) on-shell dispersion audit

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **Case-C principal three-speed branch closed in high-precision executable audit.**

## Why the previous speed reconstruction failed

DF5e.4 fixed the kinetic invariant `NG3` by restoring the pressure-consistent time derivative of the BD mixed column and the full time-dependent integration by parts.  The remaining speed regression still failed because two distinct approximations were being mixed:

1. the old extractor froze the physical matrices, while De Felice Eq. (84)/(85) contains `dot K`, `dot N` and the `3H` measure terms;
2. neighboring points were taken on the exact dust Case-C metric trajectory while retaining a finite diagnostic `c_sf^2=0.1` in the f-sector P(X) action.

The second point is crucial.  At the control point `P_f=0`, the metric values are the same, but the first derivatives of the regulated on-shell family are not all the same as those of the exact dust family.  In particular `c_prime` and `H_omega_prime` feel the non-zero pressure tangent.

## Local on-shell regulated Case-C family

For the beta1-only benchmark, with `8piG=kappa=m^2=beta1=1`, g radiation `rho_g=3/a^4`, and arbitrary local f-fluid density/pressure, equating the two Friedmann equations gives

`F(a,xi,rho_f) = a^-4 + xi - xi^2 rho_f/3 - 1/(3 xi) = 0`.

The dynamical-branch lapse is

`c = 1 + a xi_a/xi`.

The separately conserved f fluid obeys

`rho_f,a = -3 c (rho_f+P_f)/a`,

and the local constant-sound-speed regulator obeys

`P_f,a = c_sf^2 rho_f,a`.

Differentiating `F=0` and eliminating `rho_f,a` gives a first-order on-shell equation for `xi(a)`.  At the central dust point (`P_f=0`, `rho_f=3/(a xi)^3`) this reproduces the exact Case-C `xi_a` to machine precision.

This local family is used only to evaluate coefficient time derivatives consistently.  No physical interaction coefficient is changed.

## Conditioned quadratic Hessian

The interaction is already available in the repository as the direct O(delta^2) De Felice Eqs. (45)-(46) helper.  For this audit, the complete 12-variable flat-gauge quadratic Hessian was evaluated algebraically from the exact quadratic EH + P(X) + HR expressions, avoiding finite differentiation in perturbation amplitude.

The auxiliary four-by-four Schur complement, Eq. (72) transform, DF5e.4 time-dependent BD canonicalization, and BD Schur elimination were then performed on the local on-shell regulated family.

This removes the spurious high-k behavior previously seen in the outer time derivative.  In particular, the gravity-direction damping coefficient no longer scales as `k^2`; it tends to an O(H) quantity (about `16.6` at the control point over `k=100...800`).

## Correct Eq. (85) characteristic equation

In repository Hessian conventions, after the physical three-variable reduction,

`Hphys = [[M,C],[C.T,K]]`,

De Felice Eq. (84) becomes

`K Yddot + A Ydot + B Y = 0`,

with

`A = dot K + 3 H K + C.T - C`,

`B = dot C.T + 3 H C.T - M`.

The six characteristic exponents are the roots of

`det(K lambda^2 + A lambda + B)=0`.

For each conjugate/real +/- mode pair, the principal squared speed is robustly extracted from the product of the two roots,

`c_s^2 = a^2 lambda_+ lambda_- / k^2`.

This product is preferable to squaring each damped root separately because the FLRW friction shifts the individual roots by O(H).

## High-precision seven-point result

Using 70-80 decimal digit arithmetic and a symmetric seven-point derivative for both the inner BD coefficient derivative and the outer Eq. (85) matrix derivative gives stable results across derivative step fractions `5e-4`, `2e-4`, `1e-4`, and `5e-5`.

At `a=0.05`, `c_sf^2=0.1`:

| k | gravity pair `c_s^2` | g-fluid pair | f-fluid pair |
|---:|---:|---:|---:|
| 400 | -0.6858646153 | 0.3383333408 | 0.4403539387 |
| 800 | -0.6714442202 | 0.3345833352 | 0.4101255168 |
| 1600 | -0.6678011233 | 0.3336458338 | 0.4025684101 |
| 3200 | -0.6668879478 | 0.3334114584 | 0.4006791333 |
| 6400 | -0.6666595035 | 0.3333528646 | 0.4002068141 |

The matter branches approach the expected principal limits `1/3` and `c^2 c_sf^2`.

Fitting the gravity sequence at `k=800,1600,3200,6400` to

`c_s^2(k) = c0 + c2/k^2 + c4/k^4`

gives

`c0 = -0.6665833422935964`.

The independent De Felice Eq. (86) target already implemented in `gravity_principal_action()` is

`-0.6665833419871022`.

The difference is about `3.1e-10`, or `4.6e-10` relative.

## Scientific conclusion of DF5e.5

The reconstructed action, once:

- differentiated along a locally on-shell regulated background,
- evaluated with an algebraically exact quadratic Hessian,
- canonicalized with DF5e.4 time dependence,
- and tested with the actual Eq. (85) characteristic equation,

recovers all three Case-C high-frequency scalar propagation branches.

Therefore the historical missing helicity-0 gradient is **not** evidence for a wrong EH, P(X), HR, Eq. (72), or BD coefficient.  It was produced by an inconsistent/frozen reduction path plus catastrophic numerical cancellation.

## Next step

Proceed to the Candidate-C transfer only with a background/action representation that preserves the correct number of matter scalar degrees of freedom.  Candidate C contains g-sector dust plus radiation and f-sector dust; collapsing the g mixture to one P(X) scalar is not automatically legitimate for the full scalar spectrum.

The next task is therefore to decide the minimal faithful Candidate-C matter representation for the gravity branch and transfer matrix before promoting the Case-C audit code into a generic production solver.
