# JANUS — Step48: independent original Poisson bracket for the new radial IVP, and exact centre obstruction

**22 October 2026.** Research branch: `research/gate2b-nonhomothetic-transfer`. **Scientific result:** A second, unintegrated original-action Poisson calculation supports the near-constrained Step47 interior numerical IVP; an independent exact leading-order expansion reveals the **necessary regular-centre momentum datum and a 1/r singular sensitivity mode**. Neither result is a proof of full Dirac time preservation, existence of a global exact positive-dust solution, or physical viability. **Gate 2B OPEN; JANUS-R NOT VALIDATED.**

## 1. Why these two verifications matter

Step45 proved within the positive-EH two-dust spherical reduced action the original six-canonical-pair Ward relation (W=zH_g/L_f) and derived (C=K_{00}-K'_{01}) **without numerical radial differentiation**. Step46 proved that on the f lapse/radial primary surface (C) is exactly affine in (p'_{L_f}), yielding an exact first-order radial equation (p'_{L_f}=-C_0/C_1). Step47 integrated that equation numerically on ([0.05,0.85]); its extremely small secondary residual was **algebraic by construction**, not an independent Poisson functional check, and the spherical origin (r=0) was excluded.

Step48 closes part of this gap by evaluating the original unintegrated Hamiltonians **on the new IVP** with all six canonical pairs, separately from the analytic (C) used to integrate the IVP. It also identifies mathematically why simply pushing this numerical solution towards (r=0) is not adequate to establish regularity.

## 2. Authentic original UNINTEGRATED Hamiltonian oracle on a genuinely nonpolynomial numerical profile

New reproducible module: `numerics/hr_step48_original_ivp_oracle.py`.

The new code reconstructs from the Step47 ODE's dense output the TWELVE original canonical fields ((L_g,p_{L_g},S_g,p_{S_g},	heta_g,p_g,L_f,p_{L_f},S_f,p_{S_f},	heta_f,p_f)), including the **true scalar dust clock values**. Given (	heta_i'(r)=k_i r L_i(r)), (L_i=a_i(1+c_i r^2)^2), the clock primitive is
[
	heta_i(r)=k_i a_ileft(rac{r^2}{2}+rac{c_i r^4}{2}+rac{c_i^2r^6}{6}ight)+	ext{constant}.
]
This step matters because the independent original nodal Hamiltonian differentiates (	heta_i) itself; filling that field with zero would give an artificial bracket.

The actual ORIGINAL `numerics/hr_step37_original_nonibp_oracle.py` was recovered byte-for-byte from GitHub, blob SHA `005449ade6e3582e3b9a5c3374a881a77e73e3f6`. Its `hamiltonians(q,r)` independently recomputes spherical ADM three-curvatures using second radial differences, the relative shift from (D_g/sqrt{K^2+D_g^2}) at each perturbed grid configuration, and both Einstein–Hilbert/HR/two-dust lapse densities. The new Step48 source evaluates all twelve complex-step grid functional derivatives and contracts all six canonical pairs. As a negative dependency guard, it pins FIVE historical sources to their original GitHub blobs before its default full-run mode; it refuses an altered file rather than silently using an adapter.

An additional standalone reimplementation of the original `hamiltonians` expression was compared locally to the authentic historical module on **real and complex-valued** 161-point canonical arrays. Both sectors returned **exactly identical NumPy arrays** (maximum absolute difference zero).

**Provenance restriction:** The original `hr_step37_original_nonibp_oracle.py` file IS byte-identical to GitHub in this run. The old Step45/46/47 source dependencies of the local experimental IVP were faithfully reconstructed with the same mathematical equations, but NOT byte-identical GitHub files. Their imported constants and canonical ordering were matched. Therefore the default five-source byte-pinning function deliberately was NOT marked as passed locally; the full five-source check is available in the committed module on a complete branch checkout.

### Four original-action grid resolutions, two independent lapse smearings

The same curved, two-positive-dust noncomoving **Step47 ODE initial-data profile** was sampled at 161, 321, 641 and 1,281 radial nodes from (r=.05) to (r=.85), with smooth lapse pairs A (support .2–.7) and B (.25–.73). Original non-integrated Poisson bracket results:

| Grid nodes | Pair A bracket | Pair B bracket |
|---:|---:|---:|
| 161 | −5.909466422134762e−7 | −9.466192093555981e−7 |
| 321 | −1.477085211689104e−7 | −2.3664938491891468e−7 |
| 641 | −3.6925373066772505e−8 | −5.916200890277411e−8 |
| 1281 | −9.231239094041176e−9 | −1.4790486907055242e−8 |

At n=1281 the sampled original-discrete lapse primaries have max error ~1.24e−9 (down from ~6.08e−8 at n=161). **None of these finite-grid bracket values is exactly zero**. The sign at finite n is negative, dominated by O((Delta r^2)) spatial discretization bias.

Assuming an even-power grid error expansion (not proven), the two-stage Richardson (R_4) estimates, from the last three successive grids, are:

[
	ext{Pair A}: -8.0411576792	imes10^{-15},qquad
	ext{Pair B}: -8.1981103993	imes10^{-15}.
]

The earlier frozen near-secondary polynomial's analogous estimates were O(+1e−13), whereas the **new nonpolynomial IVP** has near-zero extrapolated bracket at the O(1e−14) scale for two different lapse choices. It supports the new IVP's secondary constraint numerically, but cannot prove a zero limiting bracket: Richardson assumes an error expansion, the data are floating point, and the interpolation/integration error is not mathematically enclosed.

The locally generated complete raw six-canonical-pair contributions and grids are saved in `/mnt/data/janus-step48/research/reports/step48-local-nonibp-full.json`, SHA-256 `dfc18acda78163dff61021f51429a06d6d2db4854d19655fb5dd939ab472b9a1`. That particular raw file was **not uploaded**; the essential values are included in `research/reports/gate2b-step48-report.json` and the committed runner regenerates the complete data.

## 3. Exact spherical-centre compatibility condition from the ORIGINAL local secondary

New exact symbolic certificate: `numerics/hr_step48_center_compatibility.py`, independently based on the Step45 exact six-pair physical (C(q,q',z,z')).

Use regular spherical leading data with (a=L_g(0)), (b=L_f(0)>0), (z(r)=z_1r+O(r^3)),
[
S_g=ar+O(r^3),;S_f=br+O(r^3),;p_{L_g}=P_gr^2+O(r^4),;
p_{S_g}=2P_gr+O(r^3),
]
[
p_{L_f}=U_fr^2+O(r^4),quad
p_{S_f}=V_fr+O(r^3),qquad p_g=O(r^2).
]
Write (A_* = a^2eta_1+2abeta_2+b^2eta_3). Symbolically expanding the FULL physical (C) (not a reduced synthetic kernel) yields the **exact coefficient of (r^2)**:
[
lim_{r	o0}rac{C(r)}{r^2}
=-rac{m^2 A_*}{2M_f^2ab}
Big[6M_f^2M_g^2z_1ab-3M_f^2P_gb
+M_g^2a(U_f+V_f)Big].
]

For a regular (p_{L_f}=r^2 U_f(r^2)), the f radial momentum primary implies (V_f=2U_f) at leading order: (D_f=O(r^3)), (	heta_f'p_f=O(r^3)). Thus on the nondegenerate (A_*>0) chart, (C=0) necessarily requires:

[
oxed{U_f(0)=M_f^2 bleft(rac{P_g}{M_g^2a}-2z_1ight).}
]

This is **not an arbitrary tuning heuristic**; it is the unique exact necessary regular-centre leading coefficient under these assumptions.

The published Step41 polynomial has normalized coefficient (U_f(0)approx-0.005252426896763941), while the computed necessary value is (-0.005252426896760733) in displayed binary64 arithmetic; they differ by ~(3.21	imes10^{-15}). That is extremely small but **not a mathematical demonstration of exact equality**, and it can be magnified by the singular radial equation.

## 4. Near-centre regular-singular mode and numerical sensitivity

The exact leading condition before substituting (V_f=2U_f) gives the local relation for a profile *attempting regular scaling* (P(r)=p_{L_f}(r)sim r^2 U(r^2)):

[
rac{P'(r)}{r}=3U_f(0)-rac{P(r)}{r^2}+O(r^2)
]
or
[
P'(r)+rac{P(r)}{r}=3U_f(0)r+O(r^3).
]

The **linearized leading regular-singular equation** has the general solution

[
P_{m lead}(r)=U_f(0)r^2+rac{C_{m singular}}{r}.
]

A regular-centre solution MUST have (C_{m singular}=0). The displayed (1/r) solution is a **formal leading/linearized mode**, not a proof that a generic nonlinear branch retains this asymptotic globally or that the center-tuned exact solution exists.

A separate numerical sensitivity experiment integrated the Step47 exact-C ODE **backwards**, from (r=.05) to .002, once with baseline (P(.05)) and once with an intentional (+10^{-12}) perturbation, using tightened solver controls. The measured amplification factors for the perturbation at r=.04,.02,.01,.005,.002 were:

| r | Measured amplification | Predicted (0.05/r) |
|---:|---:|---:|
| .04 | 1.2499973 | 1.25 |
| .02 | 2.4999873 | 2.50 |
| .01 | 4.9999710 | 5.00 |
| .005 | 9.9999401 | 10.00 |
| .002 | 24.9998492 | 25.00 |

The prediction is borne out to within around (1.5	imes10^{-4}) in absolute amplification at the smallest radius. This illustrates WHY extrapolating an inward double-precision integration to r=0 is unsafe without a true centre boundary condition and validated error bounds.

## 5. Executed tests and honest GitHub provenance

The new GitHub files, with **exact matching local executed Git blob hashes**:

- `numerics/hr_step48_center_compatibility.py` — `aa181529d33fcfa7d1e61a4525cade3e1b0ca4c7`;
- `numerics/hr_step48_original_ivp_oracle.py` — `dc5101d4b0d1d5b8d0834aacff4a3ad3715a28db`;
- `tests/test_hr_step48_center_and_original_ivp.py` — `e1f2946eabb4e47335940c7ce010cfd7dbe2b505`;
- historical ORIGINAL `hr_step37_original_nonibp_oracle.py` — `005449ade6e3582e3b9a5c3374a881a77e73e3f6`.

The following **10 Step48 tests actually passed** against the new committed source/test bytes and historical original Hamiltonian oracle, in the isolated reconstruction `/mnt/data/janus-step48` (~5.27s):

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step48_center_and_original_ivp.py \
  -k 'not test_original_provider_source_pins_match_real_checkout and not test_interrupted_run_manifest_keeps_Dirac_red'
# 10 PASSED, 2 DESELECTED — NOT 12 passed.
```

The two deliberately deselected controls require ALL five historical GitHub provider files to be byte-identical in the same worktree, not just the original Hamiltonian evaluator; local Step45–47 dependencies were faithfully reimplemented/mathematical adapters. They remain **explicitly PENDING**, along with a complete historical regression and GitHub CI (Actions remain disabled by user). From a complete authenticated checkout, run the **full** unfiltered test module and the default pin-enforcing original oracle:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step48_center_and_original_ivp.py
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step48_original_ivp_oracle
```

The standalone local oracle ran all N=161,321,641,1281 grids for both pairs with `check_git=False` and preserved the disabled source-pin caveat in its raw JSON. The byte-exact ORIGINAL Step37 oracle was additionally independently compared to a separate duplicate implementation of the original mathematical expressions on both real and complex-perturbed node fields, with zero array differences.

## 6. Critical next steps — Step49

1. **FULL SOURCE-AUTHENTIC REGRESSION:** recover historical Step45/46/47 GitHub files byte-exact, run the two currently deselected Step48 tests, both dual-lapse original non-IBP four-grid experiment modes, and verify all SHA-1. Do not report a full pass until actually achieved.
2. **REGULAR CENTRE SHOOTING:** impose (p_{L_f}/r^2	o U_f(0)=M_f^2 b[P_g/(M_g^2a)-2z_1]) as a genuine boundary datum, preferably reformulate in even (s=r^2), remove the (C_{m singular}/r) mode, and develop a controlled Frobenius/interval numerical continuation. Prove or refute continuous positivity of both dusts and chart determinants for the *actual new nonpolynomial IVP* on [0,.85].
3. **FIELD-THEORETIC TIME PRESERVATION:** only on data satisfying primaries and exact secondary with regular center, evaluate ({C,H_{m total}}) with all six canonical pairs, functional boundary terms, true lapse fixing and rank; also investigate exceptional (J=0) / centre (K=r^2ar K) charts.
4. If this succeeds, investigate genuinely nonhomothetic on-shell time evolution, same-action De Felice/Aoki perturbative stability, Candidate-C first fold and empirical viability. The separate external opposite-sign f-EH JHR manuscript remains a distinct criticism track.

**VERDICT: independent original-action Poisson extrapolation supports Step47 interior IVP; an exact necessary regular-centre condition and formal singular sensitivity mode have been derived. Global regular exact-secondary solution and full Dirac time preservation/lapses remain OPEN; Gate2B OPEN; JANUS-R NOT VALIDATED.**
