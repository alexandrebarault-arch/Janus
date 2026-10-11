# Gate 2A — reference twin-matter transfer system

Date: 2026-10-11

Status: `PASS_AS_REFERENCE__STRONG_NEGATIVE_RESULT_FOR_SPONTANEOUS_LINEAR_SEGREGATION`

Implementation: `numerics/aoki_twin_transfer.py`

Primary reference: K. Aoki & K.-i. Maeda, *Dark matter in ghost-free bigravity theory: From a galaxy scale to the universe*, Phys. Rev. D 90, 124089 (2014), arXiv:1409.0202.

## Why this intermediate gate was needed

Candidate C is a non-homothetic, time-dependent two-matter cosmology. Before deriving its full scalar transfer matrix, a solver should reproduce a published twin-matter perturbation system in a regime where the equations simplify into physical eigenmodes.

Aoki & Maeda's homothetic matter-era calculation provides exactly that benchmark.

Their linear perturbations split into:

- a massless/common mode;
- a massive/relative mode.

This diagonalization is the key conceptual test for spontaneous segregation.

## Equations reproduced

In an Einstein-de Sitter matter era and using `N=ln a`, the common mode obeys

`delta_+'' + (1/2) delta_+' - (3/2) delta_+ = 0`,

so its growing solution is

`delta_+ ~ a`.

The relative/massive density mode obeys the Aoki-Maeda scale-dependent equation

`delta_-'' + (1/2) delta_-' - (3/2) lambda_-(a,k) delta_- = 0`,

with

`lambda_-(a,k) = (4/3) [k^2/a^2]/[k^2/a^2 + m_eff^2]`.

Equivalently, defining

`q = k/(a m_eff)`, 

`lambda_- = (4/3) q^2/(1+q^2)`.

The short-physical-wavelength limit is

`lambda_- -> 4/3`.

Then

`delta_- ~ a^p`,

with

`p = (-1+sqrt(33))/4 = 1.1861406616...`.

## Regression checks

The committed code passes three independent checks.

### 1. Exact adiabatic-decoupling check

Starting with

`delta_-(a_i)=0`,

and

`delta_-'(a_i)=0`,

the numerical solution remains identically zero to machine precision.

This is not a numerical coincidence. The common and relative equations are homogeneous and linearly decoupled on the homothetic background.

**Therefore the published linear homothetic mechanism cannot create a relative mode from an exactly adiabatic state.**

### 2. Analytic asymptotic growth

For `q >> 1`, the code returns

`p_num = 1.186140632`,

versus

`p_exact = 1.186140662`.

### 3. Aoki-Maeda numerical growth cross-check

Choosing a finite `q_today ~= 1.6`, the integrated effective growth from `a=10^-3` to `a=1` is

`p_eff ~= 1.17577`,

consistent with Aoki & Maeda's reported numerical

`delta_- ~ a^1.176`.

This verifies that the scale-dependent implementation captures the published relative-mode behavior.

## Scale-dependent optimistic bound for Candidate C range

Candidate C has a present reference reduced Compton scale of about

`lambda_C ~= 101.2 Mpc`.

To give segregation every possible advantage, the reference calculation lets the Aoki-Maeda linear relative mode grow from recombination (`z_i=1100`) all the way to today. This is deliberately **optimistic**: Candidate C is expected to require nonlinear/screened treatment during part of this interval.

Using `h=0.7` and

`q0 = k lambda_C`,

with `k` in physical inverse Mpc after converting from `h/Mpc`, the differential transfer gain is:

| k [h/Mpc] | q0 | D_rel / D_common | initial |delta_rel/delta_common| required to reach unity today |
|---:|---:|---:|---:|
| 0.001 | 0.0708 | 0.501 | 1.995 |
| 0.002 | 0.1417 | 0.967 | 1.034 |
| 0.005 | 0.3542 | 1.971 | 0.507 |
| 0.010 | 0.7084 | 2.814 | 0.355 |
| 0.020 | 1.4168 | 3.370 | 0.297 |
| 0.050 | 3.5420 | 3.625 | 0.276 |
| 0.100 | 7.0840 | 3.668 | 0.273 |
| 0.200 | 14.168 | 3.679 | 0.272 |

Thus even under this maximally favorable reference evolution, void/LSS scales around `k~0.01-0.1 h/Mpc` need an initial relative component of roughly **27-36% of the common mode** to make the two eigencomponents comparable by today.

On the very largest scales (`k~0.001 h/Mpc`) the massive relative mode actually loses ground relative to the common mode because the physical mode exits the modified/inside-Compton regime.

## Relation to Aoki-Maeda's sign-flip example

Aoki & Maeda's published example that produces dramatic repulsive evolution does not begin with near-adiabatic amplitudes. At decoupling they take approximately

`delta_g = 10^-5`,

`delta_f = 10^-1`,

so the twin perturbation is `10^4` times larger than the visible one.

Their result therefore confirms that the force law can **exploit** a large relative perturbation. It is not evidence that the linear theory can **create** one from adiabatic seeds.

## Strong result

For the published homothetic linear regime:

`ADIABATIC -> RELATIVE MODE CONVERSION = ZERO`

and

`SMALL RELATIVE SEED -> ONLY MODEST DIFFERENTIAL AMPLIFICATION`.

This substantially weakens any claim that ordinary linear twin-matter repulsion automatically generates a Janus cosmic web.

## What remains open

This result is not a no-go theorem for full JANUS-R because Candidate C is not homothetic and its transition from the early screened phase is nonlinear/time dependent.

There are only two serious loopholes left:

1. **non-homothetic linear mode conversion:** time-dependent background mixing may source the relative eigenmode from the common mode;
2. **nonlinear transition mode conversion:** the cosmological Vainshtein-to-bigravity transition may transfer a significant fraction of the common perturbation into the relative mode.

A primordial large twin isocurvature mode is mathematically another option but is no longer considered an attractive default explanation because it merely inserts the desired segregation into the initial conditions and faces strong CMB/isocurvature pressure.

## Decision

Gate 2A is closed.

Do not spend more effort asking whether the homothetic linear theory spontaneously segregates near-adiabatic matter: **it does not**.

Proceed to Gate 2B: derive the non-homothetic Candidate-C scalar transfer/mixing system, or establish rigorously that no tractable published equation set exists and derive it from the quadratic action.
