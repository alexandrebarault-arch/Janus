# Nonlinear twin-matter screening and cosmological branch structure

Date: 2026-10-11

Status: `KEY_GATE_PARTIALLY_RESOLVED`

Primary source: K. Aoki, K.-i. Maeda, R. Namba, Phys. Rev. D 92, 044054 (2015), arXiv:1506.04543.

## 1. Why this paper is directly relevant

Unlike many later bimetric cosmology analyses which set the second matter sector to zero, Aoki-Maeda-Namba explicitly use two separately coupled positive-energy matter sectors:

`S_m = S_g[g, psi_g] + S_f[f, psi_f]`.

They retain nonlinearities of the helicity-0/Stueckelberg mode and derive the subhorizon adiabatic scalar equation in the presence of perturbations in both sectors.

This is close to the mathematical core required by JANUS-R.

## 2. Exact diagnostic equation

Their Eqs. (5.8)-(5.11) give

`C_m2(mu) + C_H2(mu) + C_matter(mu) = 0`,

where the full expression is a seventh-order polynomial in `mu`.

The leading matter source is schematically

`C_matter ~ kappa_g^2 rho_g delta_g - K^2 kappa_f^2 rho_f delta_f`.

This sign is crucial.

Define the weighted relative/isocurvature source

`S_rel = kappa_g^2 rho_g delta_g - K^2 kappa_f^2 rho_f delta_f`.

For a Janus-like configuration

`delta_g < 0` (visible-sector void),

`delta_f > 0` (twin-sector overdensity),

the two terms have the **same sign** in `S_rel`:

`S_rel = - |S_g| - |S_f|`.

Therefore an anti-correlated Janus mode maximizes, rather than cancels, the nonlinear scalar source for fixed perturbation magnitudes.

By contrast, same-sign perturbations can partially cancel in `S_rel` if their weighted amplitudes are similar.

## 3. Early and late regimes

### Early / GR phase

When

`H^2 >> m_eff^2`,

Aoki-Maeda-Namba find nonlinear scalar branches for which the metric perturbations recover the GR result and can avoid the linear Higuchi/gradient instability in appropriate coupling regions.

Thus the linear early-time instability is not by itself a fatal no-go; it can signal breakdown of linearization and onset of a cosmological Vainshtein regime.

### Late / bigravity phase

When

`H^2 << m_eff^2`,

the equation reduces approximately to

`C_m2 + C_matter ~= 0`.

There is a linear branch `mu_infinity = 0` and, depending on the interaction parameters, additional nonlinear branches with `mu_infinity = O(1)`.

The late linear branch is the regime connected to the simple massless+massive spin-2 force kernels used in the JANUS-R linear calculations.

## 4. Published nonlinear examples reproduced numerically

The repository script `numerics/aoki_scalar_polynomial.py` implements Eqs. (5.8)-(5.11).

It reproduces the main quoted roots:

### Case A

`beta2 = -3`, `beta3 = 3`, `m_g^2 = m_f^2`.

- early matter-era (`H >> m_eff`, `w=0`) stable branch: `mu_0 ~= 0.3964` (paper: `~0.40`);
- late nonlinear root: `mu_infinity = 0.698872...` (paper: `0.698872`).

The paper identifies this late nonlinear branch as stable for its tested parameters.

For `w=0`, the published adiabatic solution can evolve from the early GR phase around `mu~0.4` to the late **nonlinear** bigravity branch around `mu~0.7`.

### Case B

`beta2 = -1`, `beta3 = 1/2`, `m_g^2 = m_f^2`.

- early matter-era root: `mu_0 = 1.095445...` (paper: `~1.1`);
- in the late regime, the only stable branch identified by the paper is the linear `mu_infinity=0` branch;
- for `w=0`, the authors do **not** find a stable adiabatic solution connecting the early stable branch to that late linear branch.

They explicitly leave open whether a full non-adiabatic nonlinear transition could connect the phases.

## 5. Twin matter changes the Vainshtein scale

For static localized twin sources, the same paper derives approximately

`R_V ~= [2 |G M_g - K^2 G M_f| / (3 m_eff^2 - 2 Lambda_g)]^(1/3)`.

This is a major structural result: screening is controlled by a **difference of weighted sector masses**, not simply by the total mass.

For cosmological perturbations the analogous driver is the weighted relative source `S_rel` above.

Consequences:

- co-located same-sign `g` and `f` overdensities can partially cancel the scalar source and reduce screening;
- an anti-correlated visible-void / twin-overdensity configuration increases `|S_rel|` and pushes the scalar sector toward its nonlinear regime earlier.

This does **not** imply that Janus-like voids are permanently screened: the source density falls with cosmic expansion and the nonlinear regime can end. It does imply that a naive statement "voids are unscreened because they are low density" is insufficient in a two-matter theory. The relevant variable is the weighted relative density, not the visible density alone.

## 6. Important branch-risk result

Aoki-Maeda-Namba show that stable branches can become disconnected as the relative amplitudes of the two matter perturbations change. At a branch endpoint, two real roots can merge and become complex; in their adiabatic approximation `d mu/d(H^{-1})` can diverge.

They caution that this may be an artifact of the adiabatic approximation and that the full nonlinear dynamics is required to determine what actually happens through such a transition.

For JANUS-R this is not a peripheral issue:

- the target signal is a large relative/isocurvature perturbation;
- this is precisely the sector that strongly sources `mu`;
- therefore continuity and stability of the branch through `H ~ m_eff` must be demonstrated, not assumed.

## 7. Independent current-literature cross-check

Modern analyses of ordinary (single-matter-sector) ghost-free bimetric gravity find parameter regions that simultaneously have:

- a functioning Vainshtein screening mechanism;
- a real, nonsingular finite cosmological branch;
- self-acceleration without an explicit cosmological constant;
- acceptable CMB/BAO/SN background fits.

This establishes that the Hassan-Rosen mathematical skeleton itself is not ruled out.

However those observational analyses generally set the second separately coupled matter sector to zero. They therefore do **not** validate JANUS-R.

## 8. Current verdict on the nonlinear gate

`NONLINEAR_SCREENING_EXISTENCE = PASS_IN_PRINCIPLE`

`JANUS_RELATIVE_MODE_BRANCH_CONTINUITY = NOT_PROVEN`

`JANUS_RELATIVE_MODE_STABILITY_THROUGH_H~m = NOT_PROVEN`

`FULL_TWO_MATTER_VOID_SOLUTION = OPEN`

The important change relative to the earlier research state is that the required nonlinear equations are not hypothetical: a concrete seventh-order scalar equation with both matter sectors exists and can be explored numerically. But the desired Janus-like cosmological branch has not been shown to remain regular and stable throughout cosmic history.

## 9. Stop condition

JANUS-R Late should be rejected if, after scanning interaction parameters compatible with a healthy finite cosmological branch, every path that develops a sizable anti-correlated `(delta_g<0, delta_f>0)` mode either:

1. loses all real roots;
2. crosses a ghost/gradient-unstable branch;
3. becomes singular near `H~m_eff`;
4. remains so strongly screened that the late cross-sector dynamical effect is observationally negligible.

Passing the gate requires at least one continuous stable path plus a measurable late-time signal.
