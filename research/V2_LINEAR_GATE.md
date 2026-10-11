# V2 linear cosmology gate

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `GATE_1_PRELIMINARY_PASS__GATE_2_AT_RISK`

## Purpose

V1 established that the interesting surviving continuation of Petit's intuition is not literal negative mass or universal `+G/-G`, but a ghost-free two-metric / two-matter system whose relative spin-2 mode may generate scale-dependent segregation.

V2 asks a harder question:

> Can that relative mode be large enough to matter at late times while remaining small/stable enough to satisfy early-Universe and large-scale-structure constraints?

This document records the first answer.

---

## 1. Gate 1: background FLRW — preliminary pass only

A reproducible two-matter FLRW solver now lives in:

`numerics/two_matter_flrw.py`

It implements the spatially flat dynamical Bianchi branch with

- `y = a_f/a_g`,
- separate `g` and `f` matter conservation,
- `beta_0 = 0` allowed explicitly to test self-acceleration without inserting a visible-sector cosmological constant,
- algebraic branch tracking from the two Friedmann equations,
- lapse-ratio and mixing diagnostics.

A broad exploratory scan found many continuous backgrounds with positive lapse and positive simple mixing proxy that reproduce an expansion history very close to flat Lambda-CDM over `0 <= z <= 2`, despite `beta_0 = 0`.

This is consistent with the older twin-matter bigravity literature: Aoki & Maeda found de Sitter and matter-dominated attractors and showed that Lambda-CDM-like behavior can arise in this theory class.

### Decision

`BACKGROUND_EXISTENCE = PASS`

but

`FULL_STABILITY = NOT_TESTED`.

The background result is deliberately not promoted to a viable model. Scalar/vector/tensor kinetic signs and sound speeds can still kill any given branch.

### Scientific consequence

Background expansion is a **weak discriminator**. A model can hide behind an almost Lambda-CDM `H(z)` while differing strongly in perturbations.

Gate 2 therefore has priority over further background fitting.

---

## 2. Exact control limit: homothetic backgrounds

Aoki & Maeda show that when

`f_{mu nu} = K^2 g_{mu nu}`,

linear metric perturbations decompose into two mass eigenstates:

- `h[+]`: massless spin-2 mode;
- `h[-]`: massive spin-2 mode.

Their matter sources are corresponding linear combinations of the two twin matter perturbations.

This is the rigorous version of the V1 toy decomposition into common and relative modes.

However, the homothetic background itself also requires a tuned relation between the two background matter tensors. Therefore the exact decoupling **must not be blindly exported** to a generic non-homothetic FLRW solution.

### Safe conclusion

Near the homothetic regime, Janus-like segregation is associated primarily with the massive/relative mode. The GR-like/common mode can remain comparatively ordinary.

### Unsafe conclusion — rejected

`"adiabatic initial conditions can never generate a relative mode"`

This is exact only in the symmetric/homothetic control limit. Generic unequal sectors and a time-dependent metric ratio can mix the physical-sector variables.

---

## 3. The segregation-vs-observability tension

In the symmetric quasi-static limit already derived in V1,

`x(k,a) = k^2 / (k^2 + a^2 m_eff^2)`

and the relative mode feels

`mu_rel = 4 x / 3`.

Its maximally unscreened Einstein-de Sitter growth exponent is

`p_rel = (-1 + sqrt(33))/4 = 1.1861406616...`

instead of the common GR value `p = 1`.

A reproducible diagnostic is now in:

`numerics/relative_mode_gate.py`.

### Maximum optimistic growth

Even assuming an unrealistically favorable, continuously unscreened EdS phase:

- from `z=10` to today, the relative mode grows by only about `17.19` in absolute amplitude;
- from recombination-like `z=1100` to today, it grows by about `4055`;
- relative to the common `a` growth, its advantage since `z=1100` is only about `3.68`.

Thus a relative seed of `1e-5` at `z=1100` reaches only about `0.0405` today in this optimistic toy limit.

If the modified/unscreened regime switches on only around `z=10`, the same `1e-5` seed reaches only about `1.7e-4`.

### Interpretation

A dramatic late-time twin-sector segregation cannot be generated from an arbitrarily tiny relative seed by the linear two-metric mechanism alone.

At least one of the following must occur:

1. a non-negligible early relative/isocurvature component exists;
2. non-homothetic evolution continuously sources the relative mode;
3. nonlinear dynamics around `H ~ m_eff` strongly amplifies/generates it;
4. the desired segregation is in fact modest rather than order-unity.

---

## 4. Scale tension if `m_eff ~ H0`

Using

`H0/c = 3.33564e-4 h/Mpc`,

a spin-2 mass of order the Hubble scale implies a Compton wavenumber far below ordinary linear-LSS modes.

For example with `m_eff = 1.5 H0` at `a=1`:

- `k_C ~= 5.00e-4 h/Mpc`;
- at `k=0.01 h/Mpc`, `x ~= 0.99750`;
- at `k=0.1 h/Mpc`, `x ~= 0.999975`.

Therefore a cosmologically light massive mode is already essentially in the **maximally modified linear kernel** throughout much of the observed galaxy-clustering range.

This creates an important tension:

- if the relative mode has appreciable amplitude, its modified dynamics should be visible in LSS/growth/lensing-vs-velocity observables;
- if its amplitude is kept tiny enough to remain invisible, it struggles to generate the strong Janus-like segregation we are looking for.

Nonlinear screening can alter this conclusion, but then it must operate well beyond compact-object environments and has to be demonstrated rather than assumed.

---

## 5. CMB / isocurvature warning

Planck 2018 finds no evidence for the standard primordial isocurvature modes. For the standard uncorrelated, scale-invariant cold-dark-matter isocurvature template, the quoted 95% limit is

`beta_iso(k_mid) < 0.038`.

More generally, Planck reports that mixed isocurvature models are consistent with zero isocurvature and that the observable non-adiabatic fraction is small.

**Do not directly apply `0.038` as a JANUS-R parameter bound.**

The JANUS-R relative spin-2/twin-matter mode is not identical to the standard CDI template. Its CMB visibility depends on

- the two metric potentials,
- which sector carries radiation,
- time-dependent mixing,
- early nonlinear screening,
- the initial correlation matrix,
- the transfer of the massive mode into the visible Weyl potential.

The Planck number is therefore a **warning benchmark**, not yet a likelihood constraint.

A potentially important loophole is a compensated relative mode: standard baryon-CDM compensated isocurvature can evade first-order CMB density signatures. But JANUS-R is not automatically compensated in the gravitational sector because the massive spin-2 mode can itself source visible metric potentials. This must be calculated.

---

## 6. Gate-2 status

`LINEAR_COSMOLOGY = AT_RISK, NOT REJECTED`

The model is not dead, but the burden has shifted.

A viable JANUS-R now needs to demonstrate **all** of the following in one parameter region:

1. regular FLRW evolution from radiation domination to today;
2. positive scalar/vector/tensor kinetic terms;
3. positive propagation-speed squares;
4. GR-like/common adiabatic evolution where observations demand it;
5. a sufficiently hidden early relative mode;
6. late generation or amplification of that relative mode to an observable level;
7. no excessive CMB, matter-power, RSD or lensing signature.

If the full transfer calculation shows that the only stable/allowed relative mode is observationally negligible, the scientific value of JANUS-R as a continuation of Petit's segregation idea collapses even if the background remains viable.

---

## 7. Next implementation

The next code should no longer be another algebraic background scan.

Build a coupled linear perturbation prototype with state variables for

- visible CDM/baryon density and velocity,
- visible radiation at minimum through the early transition,
- twin dust density and velocity,
- `g`-metric scalar potentials,
- `f`-metric scalar potentials,
- time-dependent `y(a)` and lapse from the FLRW solver.

First deliverables:

`T_gg(k,z), T_gf(k,z), T_fg(k,z), T_ff(k,z)`

plus visible

- growth rate `f sigma8` proxy,
- Weyl/lensing transfer,
- relative-mode transfer.

The first target is **not precision CMB likelihoods**. It is a stability and amplitude map that tells us whether any parameter region deserves a full Boltzmann implementation.
