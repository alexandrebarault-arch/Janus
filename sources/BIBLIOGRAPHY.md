# Working bibliography and evidentiary role

Date: 2026-10-11

This is not an exhaustive Jean-Pierre Petit bibliography. It is the primary-source set currently used by the technical audit and continuation program.

## Published Janus / Petit sources

### Petit & D'Agostini (2015)

**Lagrangian derivation of the two coupled field equations in the Janus cosmological model**  
Astrophysics and Space Science 357, 67 (2015).  
DOI: `10.1007/s10509-015-2250-6`

Used for:

- the constrained metric-variation construction;
- the relation `delta g_+ = - delta g_-`;
- the audit showing that a constrained variation supplies one combined Euler-Lagrange condition rather than two independent equations without an extra assumption.

### Petit, Margnat & Zejli (2024)

**A bimetric cosmological model based on Andreï Sakharov's twin universe approach**  
European Physical Journal C 84, 1226 (2024).  
DOI: `10.1140/epjc/s10052-024-13569-w`  
arXiv: `2412.04644`

Used for:

- the modern published Janus action/equation architecture;
- Newtonian attraction/repulsion claims;
- the audit of the unspecified general interaction sector;
- the current `JANUS-EXACT = NOT_CLOSED` verdict.

## Ghost-free bimetric foundations

### Hassan & Rosen (2012)

**Bimetric Gravity from Ghost-free Massive Gravity**  
JHEP 02 (2012) 126.  
arXiv: `1109.3515`

Used for:

- the nonlinear ghost-free bimetric skeleton adopted by JANUS-R;
- the massless + massive spin-2 decomposition;
- removal of the Boulware-Deser ghost in the Hassan-Rosen construction.

### Aoki & Maeda (2014)

**Cosmology in ghost-free bigravity theory with twin matter fluids: The origin of dark matter**  
Phys. Rev. D 89, 064051.  
arXiv: `1312.7040`

Used for:

- explicit cosmology with two matter sectors, each coupled to a different metric;
- existence of matter-dominated and de Sitter attractors;
- demonstration that a twin sector can alter the effective Friedmann matter contribution.

### De Felice et al. (2014)

**Viable cosmology in bimetric theory**  
JCAP 06 (2014) 037.  
arXiv: `1404.0008`

Used for:

- healthy cosmological branch;
- generalized Higuchi/no-ghost condition;
- perturbation propagation-speed / gradient-stability conditions with two fluids.

### Aoki, Maeda & Namba (2015)

**Stability of the Early Universe in Bigravity Theory**  
Phys. Rev. D 92, 044054.  
arXiv: `1506.04543`

Used for:

- nonlinear helicity-0/Stueckelberg cosmological screening;
- the seventh-order scalar polynomial implemented in `numerics/aoki_scalar_polynomial.py`;
- explicit dependence on both `g`- and `f`-matter perturbations;
- demonstration that nonlinear scalar dynamics can restore a GR-like stable early-Universe phase in suitable parameter regions;
- twin-matter Vainshtein scale depending on a weighted *difference* of sector masses;
- branch-continuity warning around transitions.

### Hohmann (2017)

**Post-Newtonian parameter gamma and the deflection of light in ghost-free massive bimetric gravity**  
Phys. Rev. D 95, 124049.  
arXiv: `1701.07700`

Used for:

- two-sector linear PPN point-source solution;
- massless/massive spin-2 cross-sector force kernels;
- our direct re-derivation of the physical force-sign threshold;
- our direct null-ray calculation of cross-sector lensing;
- distinction between slow-matter repulsion and photon lensing.

### Högås & Mörtsell (2021a)

**Constraints on bimetric gravity. Part I. Analytical constraints**  
JCAP 05 (2021) 001.  
arXiv: `2101.08794`

Used for:

- joint screening + cosmological branch constraints;
- rejection of the infinite branch as a primary healthy candidate;
- existence of viable finite self-accelerating regions;
- local Vainshtein-screening requirements.

### Högås & Mörtsell (2021b)

**Constraints on bimetric gravity. Part II. Observational constraints**  
JCAP 05 (2021) 002.  
arXiv: `2101.08795`

Used for:

- evidence that the standard one-matter-sector Hassan-Rosen framework can satisfy local screening and background cosmological datasets simultaneously;
- proof-of-principle that self-acceleration without an explicit cosmological constant is observationally viable at background level.

### Högås & Mörtsell (2025)

**Bimetric gravity improves the fit to DESI BAO and eases the Hubble tension**  
Phys. Rev. D 112, 103515 (2025).  
arXiv: `2507.03743`

Used for:

- current external benchmark showing that standard bimetric background cosmology remains observationally viable with DESI DR2 + CMB + SNe;
- order-of-magnitude spin-2 mass scale for `research/SCALE_WINDOW.md`.

Important: this is a one-visible-matter-sector analysis and does **not** validate JANUS-R's extra twin sector.

## Current observational tests relevant to JANUS-R

### Sartori et al. (2025)

**The imprint of cosmic voids from the DESI Legacy Survey DR9 Luminous Red Galaxies in the Planck 2018 lensing map through spectroscopically calibrated mocks**  
Astronomy & Astrophysics 700, A17 (2025).  
DOI: `10.1051/0004-6361/202453562`

Used for:

- current precision void-lensing gate;
- full void sample `A_kappa = 1.016 +/- 0.054`, consistent with calibrated Lambda-CDM mocks.

### Rauhut et al. (2025)

**Testing gravitational physics by combining DESI DR1 and weak lensing datasets using the E_G estimator**  
Open Journal of Astrophysics 8 (2025).  
DOI: `10.33232/001c.145197`  
arXiv: `2507.16098`

Used for:

- current direct observational comparison between lensing and galaxy velocities;
- no reported evidence for departures from Planck GR+Lambda-CDM through `z ~ 1`.

### Gonzalez et al. (2026)

**Testing Scale-Dependent Modified Gravity with DESI DR1**  
arXiv: `2604.26915`

Used only as a **sensitivity benchmark**:

- DESI full-shape data find no evidence for the tested scale-dependent Hu-Sawicki `f(R)` modification;
- in that scalar model, correction scale constrained to `<17.81 Mpc` at 95% CL.

This result is **not transferable as a numerical bound** to JANUS-R because JANUS-R has a different spin-2 tensor structure and screening mechanism.

## Citation discipline

- A paper demonstrating that a mathematical branch exists is not counted as observational evidence for JANUS-R.
- Results for one-matter-sector bimetric cosmology are used only to establish viability of the Hassan-Rosen skeleton, not of the twin-sector model.
- Constraints on scalar modified gravity are not directly reinterpreted as massive spin-2 constraints.
- Claims unique to this repository (force-threshold correction, full cross-lensing sign derivation, linear mode diagonalization, multimetric linear-class no-go) are labeled as our derivations and kept separate from published results.
