# V2 full spherical / wall gate

Date: 2026-10-11
Status: `INITIAL_DATA_PASS__DYNAMICAL_WALL_OPEN`

## 1. Major literature correction

The gradient-resolved spherical equations needed by Gate A do **not** need to be derived from scratch.

Aoki, Maeda & Tanabe, *Relativistic stars in bigravity theory*, Phys. Rev. D 93, 064054 (2016), arXiv:1602.02227, derive the full static bidiagonal spherical Hassan-Rosen equations with both matter sectors retained. Their Eqs. (3.11)-(3.17) contain the radial gradients of both metrics, the two perfect-fluid conservation laws, and the bimetric Bianchi constraint. After fixing `r_g=r`, they reduce the system to seven first-order ODEs plus an algebraic constraint.

Important: the main numerical examples in that paper set `f` matter to zero, but the basic equations themselves contain `rho_f` and `P_f` explicitly.

## 2. Better dynamical formulation already exists

Kocic, Torsello, Hogas & Mortsell, *Initial data and first evolutions of dust clouds in bimetric relativity*, Class. Quantum Grav. 37 (2020) 165010, arXiv:1904.08617, formulate spherical Hassan-Rosen relativity in full 3+1 form and numerically evolve dust clouds.

Their metric ansatz is dynamical and allows nonbidiagonality through the separation/relative-shift variable. They explicitly state that a simple LTB analogue does not exist in bimetric gravity, so a true cosmological void problem is a numerical-relativity problem rather than an analytic LTB substitution.

The corresponding open-source code is:

- `https://github.com/nubirel/bim-solver`

The public solver already implements spherical bimetric standard-3+1 and cBSSN evolution.

## 3. Exact extension point for twin matter

The public `bim-solver` implements Valencia hydrodynamics for the `g` sector. In

`include/eom-BSSN/eomBSSNMatterReg.h`

the `f`-sector matter source functions currently return zero:

- `eq_pf_frho`
- `eq_pf_fj`
- `eq_pf_fJ11`
- `eq_pf_fJ22`

Therefore a genuine two-matter evolution is conceptually a symmetric second-fluid extension, not a rewrite of the gravitational equations.

However, this is **not purely a four-line patch**: the present fluid variables (`pfD`, `pfS`, `pftau`, `pfv`) are single-sector variables and they also enter lapse-ratio expressions, generated Jacobians, initial conditions and evolution descriptors. A production-quality twin-fluid fork would need a second conserved-variable set and regenerated/update-consistent Jacobian machinery.

Decision: do not vendor or casually patch the upstream GPL solver inside the Janus research repository yet. First prove that the desired twin-wall initial data satisfy the bimetric constraints.

## 4. Time-symmetric constraint gate

Kocic et al. show that, for conformally-flat spatial metrics at a moment of time symmetry,

`A=psi_g^2`, `B=psi_g^2 r`, `A_f=psi_f^2`, `B_f=psi_f^2 r`,

with vanishing extrinsic curvatures and separation parameter, the constraints reduce to two coupled generalized Lane-Emden equations (their Eqs. 2.20a,b).

The published example includes `g` matter only. Because the full Hamiltonian constraint (their Eq. 2.11b) already contains the `f`-matter density term, the symmetric twin-matter extension is obtained by adding `+ kappa_f D_f` to the second Lane-Emden equation.

Flat proportional asymptotics `psi_g=psi_f=1` require

`beta0 + 3 beta1 + 3 beta2 + beta3 = 0`,

`beta1 + 3 beta2 + 3 beta3 + beta4 = 0`.

A new independent Python diagnostic is in:

`numerics/twin_lane_emden_initial.py`

with regression tests in:

`tests/test_twin_lane_emden_initial.py`.

## 5. Manual TDD verification

Local execution (GitHub Actions disabled):

RED, before implementation:

`ModuleNotFoundError: No module named 'lane_emden_twin'`

GREEN after implementation:

`3 passed in 0.48s`

This verifies the module-level prototype only, not the full repository and not the upstream C++ solver.

## 6. First Janus-like initial-data result

Profiles used for the regression test:

- `f` matter: positive central Gaussian;
- `g` matter: positive compensating shell, regularized to vanish at the center;
- asymptotic vacuum / bi-Minkowski boundary;
- both conformal factors required to remain positive.

For the minimal flat interaction choice

`(beta0,beta1,beta2,beta3,beta4)=(-3,1,0,0,-1)`

with dimensionless interaction strength `0.05`, the BVP converges to a regular solution with positive `psi_g` and `psi_f` and residual below the numerical test threshold.

Exploratory scans also converged over a broad range of matter amplitudes and for the parameter combination corresponding to the earlier robust nonlinear Case A.

### Verdict

`JANUS_LIKE_INITIAL_DATA_EXISTENCE = PASS`

This is a limited but meaningful result: a central twin concentration plus visible compensating wall is **not forbidden by the time-symmetric bimetric constraints**.

It does **not** prove:

- that a cosmological void evolves into this state;
- that the wall remains regular under evolution;
- that it is stable;
- that the static/time-symmetric configuration has realistic FLRW asymptotics;
- that the resulting observable dynamics are Janus-like.

## 7. Why the original static-wall shortcut is insufficient

A cosmological dust void is time dependent. The 2016 static-star equations are excellent for a quasi-static radial consistency check but cannot settle the physical void question.

The 2020 numerical-relativity framework is therefore the correct next architecture because it evolves both metric sectors with radial gradients and relative shifts. A simple LTB ansatz is not available.

## 8. Next decisive implementation

### Gate A1 — twin-fluid initial data in full 3+1 variables

Before touching time evolution:

1. map the Python Lane-Emden profiles to the 3+1 variables used by `bim-solver`;
2. introduce an independent `f`-sector conserved dust state (`D_f,S_f,tau_f`) in a research fork or minimal compatibility layer;
3. verify both Hamiltonian constraints, both momentum constraints and the secondary bimetric constraint on the same initial slice;
4. use a compensated visible shell + central twin profile and compare against the one-fluid published data.

### Gate A2 — short-time evolution

Only if A1 is clean:

- evolve for a short interval using cBSSN/standard 3+1;
- monitor all constraints;
- track lapse ratio and metric determinants;
- detect shell crossing / zero lapse / loss of hyperbolicity;
- compare `g`-sector evolution with matched GR control.

### Gate B — wall stability

If a regular evolving wall exists, apply the general spherical perturbation machinery already identified in Brizuela-de Cesare-Soler Oficial (2024), or extract principal symbols directly from the cBSSN evolution around the numerical background.

## 9. Current conclusion

The research has crossed an important threshold:

**The principal obstacle is no longer existence of constrained spherical Janus-like initial data. The obstacle is dynamical evolution and stability of the compensation/branch-transition wall.**

The next useful work is therefore twin-fluid numerical relativity, not another algebraic root scan.
