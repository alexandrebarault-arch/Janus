# Scientific State

Last updated: 2026-10-11

## Executive verdict

### JANUS-EXACT (published Petit formulation)

**Status:** `NOT_CLOSED_AS_FUNDAMENTAL_THEORY`

The published Janus program contains genuine mathematical constructions and a physically meaningful Newtonian attraction/repulsion target, but the present general-relativistic formulation is not sufficiently closed to function as a complete fundamental bimetric theory.

Main reasons:

1. The 2015 constrained variation does not independently derive both field equations without an extra assumption.
2. The 2024 interaction sector is not specified in a unique complete nonlinear form from which all cross-sector source tensors follow.
3. The exact two-sector Newtonian sign matrix `[[+1,-1],[-1,+1]]` is singular and is structurally difficult to embed in a healthy canonical two-spin-2 theory.
4. Literal fundamental negative-energy matter is not needed to obtain effective cross-sector repulsion and introduces avoidable stability risks.

### JANUS-R Late (our continuation)

**Status:** `MATHEMATICALLY_PLAUSIBLE_BUT_STRONGLY_CONSTRAINED`

Current best continuation:

- Hassan-Rosen ghost-free bimetric potential;
- two positive-energy matter sectors, each minimally coupled to its own metric;
- ordinary baryons + conventional CDM retained in the visible `g` sector in the main branch;
- no explicit visible-sector cosmological constant while testing self-acceleration (`beta_0 = 0` as a research choice, not a theorem);
- finite/healthy cosmological branch only;
- Vainshtein/nonlinear screening required locally and in the early Universe;
- any Janus-like large-scale segregation must emerge dynamically and satisfy current lensing + velocity data.

This branch is worth continuing only as a quantitatively constrained modified-gravity/hidden-sector model, **not** as evidence that Petit's exact Janus cosmology is correct.

## Core derived results

### 1. 2015 constrained-variation defect

For `S[g_+,g_-]`, with the imposed variation

`delta g_- = -delta g_+`,

one gets

`delta S = (E_+ - E_-) delta g_+`.

Stationarity therefore gives the combined condition

`E_+ - E_- = 0`,

not independently `E_+=0` and `E_-=0` without another postulate.

**Verdict:** published separate equations can be sufficient to satisfy the constrained variation but are not uniquely derived by it.

### 2. 2024 Janus interaction sector remains incomplete

The modern paper introduces interaction Lagrangian/source terms but does not provide a fully specified nonlinear interaction functional sufficient to reconstruct the unique general cross-sector tensor in all relativistic regimes.

**Verdict:** `OPEN_DEFECT`.

### 3. Exact Janus Newtonian matrix is structurally singular

`J = [[1,-1],[-1,1]]`

has

`det J = 0`, eigenvalues `0,2`.

This exact equal-strength rule is not reproduced by the ordinary linear ghost-free bimetric propagator structure.

### 4. Cross-sector repulsion is nevertheless real in a healthy class

In the two-matter Hassan-Rosen weak-field solution, massless and massive spin-2 modes combine so that a positive-energy `f` source can repel a slow `g` test mass over part of the linear regime.

Therefore:

`CROSS_SECTOR_REPULSION_POSSIBLE = YES`.

### 5. Correct physical force threshold

For equal Planck masses the cross potential has the form

`U_gf ~ [1 - (4/3) exp(-u)]/r`, `u=mu r`.

The force sign comes from differentiating the whole expression. Repulsion persists while

`4(1+u) exp(-u) > 3`.

The positive root is

`u_force = 0.9612787631...`.

This is distinct from the smaller radius `ln(4/3)=0.28768` where the position-dependent potential coefficient itself changes sign.

### 6. Isolated positive twin matter does NOT produce negative lensing in the linear ghost-free solution

Direct null-ray integration of the full PPN metric gives

`Delta theta_gf(b) = - C M_f/b [1 - u K_1(u)]`, `u=mu b`, `C>0`.

Since `0 < u K_1(u) < 1` for `u>0`, the deflection is always convergent/toward the source and tends to zero as `u->0`.

Thus a slow visible particle may be repelled while a visible photon is not divergently lensed.

**Verdict:** Petit's literal negative-lens signature is not inherited by JANUS-R.

### 7. Linear two-metric cross repulsion is weaker than exact Janus

Define

`x = k^2/(k^2+a^2 mu^2)`.

For equal Planck masses, the linear slow-matter kernels are

`Q_dyn,self = 1 + 4x/3`,

`Q_dyn,cross = 1 - 4x/3`.

At `x->1`:

- self response -> `7/3`;
- cross response -> `-1/3`.

The modern linear ghost-free mechanism therefore reaches `-G/3`, not exact `-G`, in the normalized ultraviolet limit.

### 8. Adding more ordinary ghost-free metrics does not automatically restore `-G`

For a canonical multimetric linearization with positive Einstein-Hilbert kinetic terms, one massless spin-2 mode plus massive Fierz-Pauli modes, completeness of the mixing matrix implies for distinct sectors:

- high-momentum photon cross response -> `0`;
- high-momentum slow-matter cross response -> `-1/3` relative to the long-range massless cross coupling.

**Verdict:** `JANUS-R3` cannot be justified simply by increasing `N`.

### 9. Linear segregation exists but is modest

For equal background densities the common and relative modes are

`delta_+ = delta_g + delta_f`,

`delta_- = delta_g - delta_f`.

In the maximally unscreened linear regime the relative mode has effective strength `4/3`, giving in an Einstein-de Sitter approximation

`delta_- ~ a^1.186`,

versus

`delta_+ ~ a`.

Thus the relative/common ratio grows only as `a^0.186`.

A late unscreened phase cannot generate enormous segregation from an initially negligible relative perturbation by linear growth alone.

### 10. Nonlinear two-matter scalar dynamics exist and directly source the Janus relative mode

Aoki-Maeda-Namba (2015) derive a seventh-order nonlinear scalar/Stueckelberg equation with both matter sectors. Its leading relative source is

`S_rel ~ kappa_g^2 rho_g delta_g - K^2 kappa_f^2 rho_f delta_f`.

For a visible void plus twin overdensity,

`delta_g<0`, `delta_f>0`,

the contributions add in magnitude rather than cancel.

The same theory possesses nonlinear branches that can restore a GR-like stable early-Universe phase for suitable parameters.

**Verdict:** nonlinear screening/relative-mode dynamics are a real mechanism, not a hypothetical patch.

### 11. But nonlinear branch continuity is not generic

Published examples include:

- Case A (`beta2=-3`, `beta3=3`, equal metric mass scales): stable early matter branch near `mu~0.40` and stable late nonlinear root `mu=0.698872...`;
- Case B (`beta2=-1`, `beta3=0.5`): early stable root near `mu~1.1`, but no stable adiabatic connection to the late stable linear branch for matter domination.

Branches may merge/disappear in the adiabatic polynomial analysis.

**Verdict:** a healthy Janus-like cosmological trajectory must be demonstrated parameter by parameter.

## Current scale window

A standard one-matter-sector bimetric DESI DR2+CMB+SNe analysis in 2025 finds viable masses around/above a few `10^-32 eV` (model-dependent). For orientation only, at

`m_FP = 3e-32 eV`, `H0=69 km/s/Mpc`,

the reduced Compton length is about

`lambda ~= 213 Mpc`,

and the unscreened point-force repulsive radius would be

`~0.961 lambda ~= 205 Mpc`.

The crude condition `H~m` occurs around `z~10` for this scale.

This coincidence with large-void/supervoid scales is interesting but **not validation**. The extra matter sector changes the phenomenology and must be fitted separately.

## Observational gate (2025-2026)

### Void lensing

DESI Legacy Survey DR9 LRG voids cross-correlated with Planck 2018 CMB lensing give

`A_kappa = 1.016 +/- 0.054`

for the full sample relative to calibrated Lambda-CDM mocks (Sartori et al. 2025).

Strong arbitrary distortions of void lensing are therefore disfavored.

### Lensing versus velocities

DESI DR1 + KiDS/DES/HSC `E_G` measurements are consistent with the Planck GR+Lambda-CDM prediction to `z~1` (Rauhut et al. 2025).

A large universal JANUS-R dynamics/lensing mismatch is therefore not observed.

### DESI scale-dependent gravity sensitivity

A 2026 DESI DR1 full-shape analysis constrains a scalar Hu-Sawicki `f(R)` correction scale to `<17.81 Mpc` in that model and finds no evidence for modified gravity.

This numerical limit does **not** apply directly to spin-2 JANUS-R, but shows that new gravity on tens-to-hundreds of Mpc scales is observationally testable now.

## Correct void diagnostic

For

`delta_g=-D`, `delta_f=R D`,

the linear visible responses relative to a GR visible-only void are

`A_lens = (1+x) - R(1-x)`,

`A_dyn = (1+4x/3) - R(1-4x/3)`.

For the equal anti-correlated Janus-like mode `R=1`:

`A_lens=2x`,

`A_dyn=8x/3`,

so

`A_lens/A_dyn=3/4`.

A key consequence is that at `x=1/2`, lensing is exactly GR-like (`A_lens=1`) while the slow-matter dynamics is enhanced by `4/3`.

Using the measured `A_kappa` only as a toy single-scale inversion gives

`x ~= 0.508 +/- 0.027`,

which would imply

`A_dyn ~= 1.355 +/- 0.072`.

This is **not a formal fit**, but it identifies the most discriminating future observable: void velocities/RSD jointly with void lensing.

## Branch status

| Branch | Status |
|---|---|
| `JANUS-EXACT` | `NOT_CLOSED` |
| literal fundamental negative mass | `NOT_REQUIRED / DISFAVORED_AS_FOUNDATION` |
| naive linear cosmological Yukawa extrapolation | `REJECTED` |
| minimal beta1 final model | `REJECTED` |
| beta1-beta4 infinite branch | `REJECTED_AS_PRIMARY` |
| constant-mass twin sector = all DM + large-scale repulsion | `REJECTED` |
| `JANUS-R Late` finite/healthy + screening | `OPEN_BUT_CONSTRAINED` |
| `JANUS-R2` evolving effective mass | `HIGH_RISK_EXPLORATORY` |
| `JANUS-R3` ordinary multimetric route to exact -G | `DOWNGRADED_EXPLORATORY` |

## Bottom line

The research does **not** support the statement "Janus is demonstrated".

It does support a narrower and technically respectable statement:

> A positive-energy, two-sector ghost-free bimetric theory can contain an emergent cross-sector repulsive force and nonlinear relative-sector dynamics reminiscent of part of Petit's physical intuition. However, the exact `+G/-G` Janus law, fundamental negative mass and negative lensing do not survive our present healthy-theory audit, while current large-scale observations already constrain any strong late-time version.

The remaining scientifically serious problem is to compute and fit the full two-matter cosmological perturbations/nonlinear void solutions. Until that is done, JANUS-R is a research hypothesis, not a cosmological replacement for Lambda-CDM.
