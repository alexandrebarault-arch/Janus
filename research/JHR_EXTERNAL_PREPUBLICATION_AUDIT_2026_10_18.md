# Independent prepublication review — external SJHR/JHR note (14 October 2026)

**Audit date:** 2026-10-18  
**Status:** FOUR REPRODUCIBLE DIAGNOSTICS / MATERIAL SCIENTIFIC OBJECTIONS.  
**Scope:** externally supplied `Travaux Scientifiques - Modele Cosmologique Janus Covariant (JHR) et Scripts Python.pdf` and accompanying note to J.-P. Petit. This is NOT the separate positive-kinetic Hassan–Rosen `JANUS-R Late` research branch.

## Decision for scientific circulation

**DO NOT PRESENT THE SUPPLIED JHR NOTE AS A DEMONSTRATED, GHOST-FREE COSMOLOGICAL THEORY OR AS A COMPUTED FIT TO THE CMB.** As explicitly written, its relative-sign Einstein–Hilbert action has an unresolved and, under standard positive-coupling/common-time assumptions, immediate tensor kinetic ghost; its Noether demonstration is weaker than its stellar claim; its strong-coupling cutoff estimate is inconsistent with a cosmological spin-2 mass if claimed to be 1 meV; and its acoustic test is a phenomenologically forced toy oscillator, not a self-consistent CMB Boltzmann calculation.

This is a conditional mathematical audit of the **specified equations and code**. It is not a sweeping theorem that every possible two-sector cosmology or every positive-kinetic Hassan–Rosen continuation is inconsistent.

## 1. Relative Einstein–Hilbert sign: tensor ghost is NOT the BD ghost

The note specifies schematically (suppressing matter and HR interaction)

```text
S = (1/2 chi_g) ∫ sqrt(-g) R[g]
  - (1/2 chi_f) ∫ sqrt(-f) R[f] + S_HR,
```

with `chi_g,chi_f>0`. Expand around two regular compatible Lorentzian backgrounds in a common time and isolate transverse-traceless tensor velocities. Up to overall positive factors,

```text
L_TT,kin = + (1/chi_g) (dot h_g,TT)^2
           - (1/chi_f) (dot h_f,TT)^2;
K_TT = diag(1/chi_g, -1/chi_f).
```

Therefore `det K_TT<0`; one eigenvalue is strictly negative. No regular nonsingular real linear change of tensor variables can change the one-positive/one-negative inertia (Sylvester's law). An HR *algebraic, derivative-free* interaction potential cannot change this leading high-frequency velocity signature. A Hamiltonian constraint that removes the **extra Boulware–Deser scalar** does not remove an ordinary TT tensor ghost.

Thus the note's inference *HR potential ⇒ positive Hamiltonian and quantum vacuum stability* is mathematically unjustified for the action as written. Claiming that each sector separately has positive intrinsic energy or invoking PT does not supply a shared positive-energy Hamiltonian for the interacting system. The only acceptable alternative would be an explicitly defined nonstandard physical Hilbert space/canonical theory whose tensor kinetic positivity can actually be proven.

Context: Hassan & Rosen, *Bimetric Gravity from Ghost-free Massive Gravity*, JHEP 02 (2012) 126, DOI 10.1007/JHEP02(2012)126; Hassan & Rosen, *Confirmation of the Secondary Constraint and Absence of Ghost*, JHEP 04 (2012) 123. These establish a specific BD constraint construction; they do not license the above sign reversal as proof of positive kinetic energy.

## 2. Combined Noether identity does not imply BOTH sector constraints

With separately minimally coupled, on-shell matter, each sector stress tensor is separately covariantly conserved. Applying the respective Bianchi identities to each of the two field equations forces separate on-shell conditions schematically

```text
nabla_g^mu V_{mu nu}=0,
nabla_f^mu Vbar_{mu nu}=0,
```

with the appropriate coefficients/conventions. The common-diffeomorphism Noether identity implies a *weighted relation between* the interaction divergences, but it does not imply that either divergence is independently zero on an arbitrary proposed stellar background.

The note's own numerical 'Noether' example, reproduced from the committed `numerics/jhr_independent_audit.py` `stellar_weighted_divergences(compactness=.05)` code, gives:

```text
max |div_g|            ~ 0.10418776057
max |div_f|            ~ 0.10418776057
max |div_g + div_f|    ~ 2.21e-15
```

These are **the toy implementation's weighted divergence quantities**, not by themselves a proof that any exact proposed star solves or violates the full field equations. Their near-perfect sum cancellation is an algebraic identity; it is **not** a simultaneous test of the two separate Bianchi+matter conservation equations and therefore does not close the claimed hydrostatic stellar objection.

To substantiate the stellar claim, provide an explicit regular two-metric star, both matter profiles, both sets of field equations and boundary conditions, and show each sector's on-shell divergence vanishes individually.

## 3. Lambda_3 scale: order-of-magnitude arithmetic and unsupported lifetime

The displayed massive-spin-2 strong coupling scale is

```text
Lambda_3=(m^2 M_Pl,reduced)^(1/3).
M_Pl,reduced=2.435e27 eV.
```

For a cosmologically light illustrative mass `m=1e-32 eV`:

```text
Lambda_3 = 6.2445285448e-13 eV,
(1 meV)/Lambda_3 = 1.601401920e9.
```

Conversely, demanding `Lambda_3=1 meV=1e-3 eV` yields

```text
m = sqrt((1e-3 eV)^3/(2.435e27 eV))
  = 6.4084133611e-19 eV.
```

**Conditional warning:** the note's `~1 meV` value does not follow at cosmological graviton masses `~10^-32 eV`. The note must state its actual `m`, its normalization and dimensional units. If another `m` is used, derive its cosmological interaction range/compatibility independently.

Moreover a dimensional inequality of the form `Gamma/V <= Lambda_UV^4` **does not establish a vacuum lifetime**, since a decay rate per spacetime volume must be integrated over spacetime and the dynamical transition amplitude actually computed. An EFT cutoff is not a mechanism that automatically makes negative-energy vacuum decay harmless.

## 4. Toy CMB third peak: input forcing vs predictive solution

The supplied script uses a scalar oscillator forced by a prescribed `psi(k,alpha)`, where `alpha` is a free effective amplification parameter. Reproduction using `toy_acoustic_peak_amplitudes` gives:

| alpha (specified by hand) | toy third-to-second amplitude ratio |
|---:|---:|
| 0 | ~0.5031 |
| 1 | ~0.7541 |
| 2 | ~0.8657 |
| 4.4 | ~0.9805 |
| 8 | ~1.0443 |
| 20 | ~1.1027 |

A chosen `alpha=4.4` makes the **toy** ratio look close to the quoted reference value; it does NOT follow from a solved, gauge-consistent coupled scalar Einstein–Boltzmann system or from a calculated physical `C_ell`. The oscillator does not supply a full photon-baryon-neutrino/twin-matter gravitational transfer, acoustic visibility, line-of-sight projection or Planck likelihood.

The meaningful claim is only that an **externally prescribed, tunable potential** can alter a toy oscillator's third-to-second amplitude ratio. The claim that SJHR has restored the observed CMB peak with no dark matter is **unproven**.

## Reproducibility: independent targeted tests

The existing helper `numerics/jhr_independent_audit.py` is independently exercised by

```bash
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_jhr_prepublication_gates.py
# 4 passed in a locally reconstructed source workspace, 2026-10-18
```

The tests cover opposite-EH kinetic inertia under an arbitrary invertible field mixing, independent Lambda_3 dimensional arithmetic, the combined-vs-individual Noether distinction in the note's own code, and dependence of the toy acoustic output on prescribed `alpha`.

**Verification limitation:** the current runtime could not clone GitHub (DNS failure), and GitHub Actions remain disabled. The targeted test and its prerequisite functions were executed in a reconstructed local workspace, not the entire GitHub worktree.

## Scientific disposition and requested fixes

1. **STOP: JHR as written with inverted f Einstein–Hilbert kinetic sign is not certified ghost-free.** Rewrite with explicitly healthy kinetic terms and rederive signs/forces, or present a rigorous alternative canonical Hamiltonian treatment. Do NOT cite BD ghost freedom as proving all kinetic eigenvalues positive.
2. **OPEN: stellar Noether argument.** Solve both metric/fluid systems and satisfy BOTH separate on-shell divergences; a weighted sum cancellation is insufficient.
3. **CORRECT: dimensional EFT cutoff.** Specify graviton mass and proper Lambda_3 numeric units; remove unsupported quantitative vacuum-lifetime assertions.
4. **RECLASSIFY: acoustic result as a toy parameter scan.** Predict alpha(k,z) dynamically from the field equations; solve full linear scalar system and radiation transfer, compute and fit full `C_ell` with an unambiguous likelihood.
5. Only then consider submitting a corrected technical note; until then circulate as a **critical audit/preprint of open problems**, not an established cosmological solution.

These objections are independent of the ongoing `JANUS-R Late` positive-kinetic Gate 2B calculations. `JANUS_R_GATE_2B=OPEN`.
