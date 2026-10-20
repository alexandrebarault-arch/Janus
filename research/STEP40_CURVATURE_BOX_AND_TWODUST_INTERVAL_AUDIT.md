# JANUS Gate 2B — Step 40: parameter-uniform HR algebraic shift chart and continuum two-dust positivity

**Date:** 2026-10-20. **Branch:** `research/gate2b-nonhomothetic-transfer`. **Status:** Two genuine **continuous exact-rational** positivity certificates for explicitly restricted spherical canonical data; full BD/Dirac closure remains **OPEN**. JANUS-R NOT VALIDATED.

## Motivation and exact mathematical increment

Steps37/39 had curved nonhomothetic spatial metric initial data with two noncomoving positive canonical dust momenta, plus only *numerically approximate* local secondary data. Step38 proved J(Sf/Sg) and K/r² nonzero throughout the radial interval for exactly one curved metric configuration; the dust positivity checks were only pointwise samples.

Step40 strengthens two independent and previously OPEN aspects:
1. certify J and K/r² for a **continuous parameter box of independently curved metrics**, with an explicit real algebraic J=0 failure control outside that box;
2. **prove dust canonical momenta divided by r² are strictly positive on EVERY radius**, for the original curved primary family and a broad box of independent even f-momentum corrections. This is not a complete proof for the actual Step39 corrected momentum until its coefficients are checked to lie in the certified ball.

All inequalities are decided using `fractions.Fraction` and certified outward square-root bounds using `math.isqrt`; reported decimals are only displays of exact rational lower bounds.

## 1. Robust J and K/r² chart, NOT just a sample of radial points

Spatial conformal spherical ansatz:
```text
Lg=a*(1+c_g*r²)²,    Sg=r*Lg
Lf=b*(1+c_f*r²)²,    Sf=r*Lf
y=b/a, eta=Sf/Sg=y*((1+c_f*r²)/(1+c_g*r²))²
J(eta)=beta1+2 beta2*eta+beta3*eta²
K/r²=m² Mg²*a^4*y*(1+c_g*r²)^6*(1+c_f*r²)^2*J(eta)
```

At a=.4, y=.5787707228025044, r∈[0,.85], independent **arbitrary** `|c_g|,|c_f|<=.015` (not necessarily oppositely signed), every conformal factor lies in [1-cR²,1+cR²]. Hence
```text
eta_min=y*((1-cR²)/(1+cR²))²
eta_max=y*((1+cR²)/(1-cR²))².
```
As `beta2+beta3*eta_min>0` (exact), J is increasing throughout this eta interval; using the positive lower bounds of the conformal factors gives **strict and continuous exact-rational** margins:
```text
J(Sf/Sg) >= 0.5039461792087735... > 1/2
K(r)/r² >= 0.15968997603142235... > 0.
```
These are conservative *bounds*, not actual extrema of K over the parameter box. A second independent background uncertainty box `a∈[.395,.405]`, `y∈[.5787,.5789]` retains `J>=0.5034934036212138...` and `K/r²>=0.15169896908005312...` throughout the same curvature/radial box.

**Sharp algebraic negative control:** taking `c_g=+c,c_f=-c` at r=.85 and varying c, the exact rational J function has a **unique** root in c∈(.07854,.07856), bisection midpoint ≈**.07854905913576156** (72 exact dyadic steps). At c=.08, `J≈-0.00796226854666`. Thus extending the positive-J bound uncritically to arbitrary curvatures would be FALSE. This is a counterexample for the **metric algebraic shift chart only**; there is no claim that the c=.08 profile has positive dusts or satisfies the primary+secondary constraints.

The spherical interaction K(r) itself has a geometric factor r². `K(0)=0` is not a proof of a physical BD degeneracy, and `K/r²>0` is not a proof of full Dirac matrix rank or lapse regularity.

## 2. Two noncomoving canonical dusts: continuum interval enclosure

For the actual **uncorrected** Step37 near-flat curved primary family:
```text
a=.4, y=.5787707228025044, c_g=.0015, c_f=-.0012,
z(r)=.004*r, theta'_g=.0012*r*Lg, theta'_f=-.0016*r*Lf,
pLg'=2r(1+5c_g*r²)Pg, pLf'=2r(1+5c_f*r²)Pf,
Pg=-2a² H, Pf=-2Mf²*b*a*H,
H²=.9/(3a³)+(m²/3)*(beta0+3beta1 y+3beta2 y²+beta3 y³).
```
The source algebra satisfies **both** lapse Hamiltonian primaries by independently solving positive matter momenta and both radial primaries by reconstructing pS_g,pS_f. To certify them without treating discrete samples as a proof, use s=r² and the exact geometry identities
```text
u_i=1+c_i*s, Li=a_i*u_i², Si=r*Li,
Si'=a_i*u_i*(1+5c_i*s),
pLi/r²=Pi*(1+5c_i*s/2),
Ri^(3)=-48*c_i/(a_i²*u_i^5).
```
The dust Hamiltonian numerator divided by r² is an algebraic combination of polynomial/rational functions in s, a positive square root `sqrt(1-z1²*s)`, plus the sector-dependent **different** `zD/Lg` and `zD/Lf` terms. Its coefficient is `sqrt(1+k_i²*s)+[pLi/(2Mi² Si Si')] theta'_i` and is positively bounded in the interval computation. Therefore a normalized dust momentum `p_i(r)/r²` has a regular finite limit as r→0 and can be checked over the CLOSED interval in s.

We partition the EXACT rational interval `s∈[0,289/400]` into 256 closed, touching rational subintervals, and propagate exact lower/upper Fraction bounds through all operations. Each square root receives an outward rational enclosure computed by integer `isqrt` with decimal grid 10^-22; exact comparisons, not float, decide positivity. The resulting global **strict** conservative lower bounds are:

| Source / allowed f-momentum polynomial | Exact guaranteed inequality, for all 0<=r<=.85 |
| --- | --- |
| Baseline, f_delta=0 | `p_g/r²>0.885`, `p_f/r²>0.114` |
| Any independent even coefficient `|delta_{2k}|<=.005`, k=0..4 | `p_g/r²>0.885`, `p_f/r²>0.039` |

The actual Fraction lower bounds for the worst admissible full correction ball display approximately g=.8854472033872441 and f=.03930997556977505. The exact proof is preserved by the executable code rather than rounded decimals; it automatically **fails closed** if any bound becomes nonpositive. For uncertainty radius .007, this particular interval certificate DOES fail; this is NOT a proof of physical negative f dust (it could simply be an inconclusive enclosure).

**Crucial generator conversion** preserved from Step37: if the f radial momentum generator is `Qf=Pf+sum_{k=0}^4 delta_{2k}*s^k`, the actual momentum density is
```text
pLf/r²=Pf*(1+5*c_f*s/2)
       +sum delta_{2k}*[s^k/(k+1)+5*c_f*s^(k+1)/(k+2)].
```
Both functions are bounded with independent coefficients each in `[-.005,.005]`, including the two-dust lapse and shift contributions. The original and f dust phases are noncomoving and distinct. At the coordinate center, the *canonical radial densities themselves* satisfy `p_i(r)=r²[p_i/r²]` and hence vanish as r²; one must not write that the coordinate densities are strictly positive at r=0. What is certified is `p_i/r²>0` on the closed normalized domain and `p_i>0` for every r>0.

## 3. Independent comparison to original Hamiltonians and test provenance

The new independent test reconstructs the original **unsimplified** spherical primary lapse Hamiltonian, `pLi,pLi',Si,Si',R3,At,K,Dg,z` and both independent `zDg/L_i` matter equations from scratch in ordinary floating point, rather than reusing the simplified Fraction expressions. It compares the resulting normalized dust momenta with the exact enclosure at five distinct radii, plus a nonzero independent even-f-momentum perturbation at three points. Floating-point reference comparisons explicitly allow a 1e-12 numerical tolerance: the certified exact Fraction enclosures at a single radius can be considerably narrower than a binary64 computation's rounding error. The entire-interval certificate itself is NOT decided using this tolerance.

Actual executed `/mnt/data/janus-step40` local worktree:
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step40_curvature_box.py \
  tests/test_hr_step40_twodust_interval.py
# 35 passed in 1.80 seconds
```
All FOUR actual executed source/test Git blob hashes matched the uploaded GitHub files:
- `numerics/hr_step40_curvature_box.py` — `8c574210fc72969d9fb03257b5a930174c6db5c3`
- `tests/test_hr_step40_curvature_box.py` — `670b3e07ecafc4c81fa6a20086bc2efe2ea03bbd`
- `numerics/hr_step40_twodust_interval.py` — `30b20707a9d9d94c9620f37d3ce0c72cd904943d`
- `tests/test_hr_step40_twodust_interval.py` — `2b1d05e7069f88ba555205c6e1117fc3ea82fe5e`.

This is a stand-alone *mathematical* test suite on FOUR files, NOT a live Step39 high-order corrected-profile solve, a whole-repository suite or GitHub CI.

## 4. Hard RED to resume at Step41, before Dirac closure

1. **Actually rerun** Step39 high-order `solve_five_point(h=.001,degree=4,iterations=6)` with byte-identical source/provider modules; explicitly save its FULL f_delta coefficients in a machine-readable artifact (the Step39 reports preserve residuals but not the final coefficient tuple). Check that EVERY even coefficient magnitude is <=.005 and every odd coefficient is zero. ONLY IF SO apply the Step40 exact interval positivity certificate to that ACTUAL high-order near-secondary profile. Otherwise increase/refine the independent correction interval and prove new bounds, or report failure.
2. Derive an exact analytic radial derivative of `K01` (or independently validated high-order/spectral construction), and establish `C_local(r)=0` on a continuous radial interval for a noncomoving curved profile, with controlled errors and center/boundary regularity. Step39 residual ~5e-11 sampled and integrated ~1e-13 **does not** prove this.
3. Explicitly compute and evaluate time preservation `{C_local,H_g[N]+H_f[M]+D[shift]}` with **all six canonical pairs**, the full Dirac matrix rank and actual lapse fixing. The J/K positivity gates are NECESSARY chart controls only; never misrepresent them as BD absence or degrees-of-freedom counting.
4. Only after a successful or negative Dirac result: genuinely nonhomothetic ON-SHELL evolution, consistent same-action De Felice finite-H mu→0 AND Aoki nonlinear K_S,c_S² stable/unstable controls, first Candidate-C fold, then possible observational checks.

**VERDICT:** STEP40 EXACT-RATIONAL CONTINUUM SHIFT-CHART/DUST PRIMARY POSITIVITY=PASSED IN RESTRICTED FAMILIES; STEP39 CORRECTED-PROFILE COEFFICIENT LINK=OPEN; CURVED SECONDARY EXACT=OPEN; DIRAC PRESERVATION/LAPSE FIXING=OPEN; `GATE_2B=OPEN`; `JANUS-R NOT VALIDATED`. The external opposite-sign-f-EH JHR manuscript audit remains distinct.
