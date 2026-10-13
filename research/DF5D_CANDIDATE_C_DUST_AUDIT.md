# DF5d — Candidate C dust+dust action audit

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **two-fluid Candidate-C gravity branch reproduced in high-precision Eq. (85) audit.**

## Purpose

After closing Case C, the next question was whether the repaired De Felice action path was merely benchmark-specific or transferred to the non-homothetic Candidate C background.

The clean intermediate benchmark is Candidate C with visible radiation removed, leaving exactly one dust fluid on each metric.  This matches the two-matter action's physical degree count.  At `a=0.5` the radiation contribution in the full Candidate-C background is tiny, so the principal gravity target changes only at the `~1e-5` relative level.

## Dust+dust Candidate-C control point

Parameters are the existing `candidate_c()` values, with `Omega_g,r0` set to zero only for this exact two-fluid action benchmark.

At `a=0.5`, following the branch continuously from the present-day root gives approximately

- `xi = 0.5682425064594762`;
- `ctilde = 0.9370846292570983`.

The independent De Felice Eq. (86) principal gravity speed is

`c_s,grav^2 = 0.6920714772884699`.

For comparison, retaining the physical radiation background gives

`0.6920799926788032`,

so the dust-benchmark shift is about `1.2e-5` relative.

## Regulated local on-shell family

Both dust P(X) sectors are assigned finite local sound-speed regulators only to make the quadratic action nonsingular.  At the central point both pressures remain zero.

The general dynamical-branch constraint is

`F = rho_g/3 + m^2 U_g(xi)/3 - xi^2 rho_f/(3 kappa) - m^2 xi^2 U_f(xi)/(3 kappa) = 0`.

With

`c = 1 + a xi_a/xi`,

separate conservation gives

`rho_g,a = -3 (rho_g+P_g)/a`,

`rho_f,a = -3 c (rho_f+P_f)/a`,

and constant local P(X) regulators obey

`P_g,a = c_s,g^2 rho_g,a`,

`P_f,a = c_s,f^2 rho_f,a`.

Differentiating the branch constraint gives `xi_a` algebraically, so all neighboring points used in `dot K`, `dot N`, and the BD coefficient derivatives lie on one locally consistent regulated background family.

## Eq. (85) reconstruction

The same conditioned pipeline as DF5e.5 was used:

1. algebraically exact quadratic EH + P(X) + HR Hessian;
2. four-auxiliary Schur complement;
3. Eq. (72) transform;
4. pressure/on-shell time-dependent BD canonicalization;
5. BD Schur elimination;
6. seven-point high-precision derivatives of the physical matrices;
7. De Felice Eq. (85) characteristic polynomial.

For the audit, `c_s,g^2=c_s,f^2=0.1`.  The two matter principal targets are therefore `0.1` and `ctilde^2*0.1 ~= 0.08781276024`.

## Results

At `a=0.5`:

| k | f-matter branch | g-matter branch | gravity branch |
|---:|---:|---:|---:|
| 400 | 0.08799536 | 0.10000705 | 0.69418361 |
| 800 | 0.08785982 | 0.10000176 | 0.69259706 |
| 1600 | 0.08782462 | 0.10000044 | 0.69220272 |
| 3200 | 0.08781573 | 0.10000011 | 0.69210428 |
| 6400 | 0.08781350 | 0.10000003 | 0.69207968 |

The matter branches converge to their expected regulator speeds.

Fitting the gravity branch at `k=800,1600,3200,6400` to

`c_s^2(k) = c0 + c2/k^2 + c4/k^4`

gives

`c0 = 0.6920714772308268`,

versus the independent target

`0.6920714772884699`.

The difference is about `5.8e-11`, or `8.3e-11` relative.

## Conclusion

The repaired action/reduction path is not specific to early beta1 Case C.  It reproduces the healthy positive helicity-0 Candidate-C principal speed on an independent non-homothetic two-dust background.

This closes the old T2/DF5d benchmark at the scientific-audit level.

## Radiation / full transfer implication

The physical Candidate C background contains g-sector dust plus radiation and f-sector dust.  A faithful full scalar transfer system therefore has one additional matter scalar degree of freedom compared with the current two-matter action.

For late epochs the radiation background fraction is small, so the dust+dust benchmark is an excellent gravity-branch validation.  It is not, by itself, a license to collapse dust and radiation into one P(X) fluid for a full transfer matrix, because the dust-radiation entropy/acoustic mode is a real independent scalar degree of freedom.

The next implementation decision is whether to:

- first build the validated two-dust time-domain transfer solver for the clean late regime and add radiation afterwards, or
- generalize the action reducer directly to multiple separately conserved fluids on one metric.
