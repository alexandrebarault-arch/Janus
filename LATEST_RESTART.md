# JANUS — REPRISE PRIORITAIRE : ÉTAPE 33f (2026-10-19)

**READ FIRST:** `research/SPHERICAL_LOCAL_PRIMARY_SURFACE_STEP33F_AUDIT.md`.
**NEW CODE:** `numerics/hr_spherical_local_mixed_kernel.py`, `numerics/hr_spherical_radial_primary_surface.py`.
**NEW TESTS:** `tests/test_hr_spherical_local_primary_kernel.py`.
**REPRODUCE NOW:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33f.py gate2b-step33f-report.json`.

## 33f. Mixed H_g/H_f radial differential kernel + explicit positive-two-dust radial PRIMARY surface GREEN — GENERAL BD SECONDARY STILL OPEN (LATEST)

**Real advance over 33e:** Step33e gave a true radially smeared `{H_g[N],H_f[M]}` but only on an arbitrary OFF-SHELL radial benchmark. Step33f (1) reconstructs all N,N',N'' × M,M',M'' LOCAL bilinear bracket coefficients `K_ij(r)` directly from all 12 exact canonical functional Euler derivatives in six metric/dust pairs, and (2) evaluates them on an explicit radial family where BOTH Hamiltonian primaries H_g,H_f and the diagonal momentum primary Ddiag vanish pointwise with BOTH independently positive dust momenta. This is a **restricted but genuinely radially inhomogeneous canonical PRIMARY-CONSTRAINT surface**; it is NOT a time-evolved Einstein solution or full general HR BD secondary proof.

**Off-shell local operator:**
```
{H_g[N],H_f[M]}=integral dr sum_{i,j=0}^2 K_ij(r) N^(i)(r) M^(j)(r).
K(r=.43) = [[+0.756718835596,-0.028692400055,0],
            [-0.214603323052,+0.264894709296,0],
            [+0.264894709296,0,0]].
```
Numerical operator identities `K20=K11`, `K02=K12=K22=K21=0` hold on regular off-shell root and fixed-z samples. The NONZERO derivative terms must NOT be removed before spatial IBP. Independent 40-point radial integration of this local kernel reproduces the original Step33e mixed functional Poisson value `1.2437914369613e-6` with the original arbitrary offshell compact N,M. Local jets are generated using unit-smearing profiles `1,(r-r0),(r-r0)^2/2`; all six canonical Poisson pairs retained.

**NEW primary-satisfying radial two-dust witness:** spatial slices `Lg=a, Sg=a r, Lf=b, Sf=b r` are flat; choose INDEPENDENT nonconstant polynomial momenta `pL_g=r² Pg(r), pS_g=(pL_g)'`, `pL_f=r² Pf(r), pS_f=(pL_f)'`; comoving matter phases `theta'_g=theta'_f=0`. Then Dg=Df=Ddiag=0 EXACTLY, z*=0, and solve Hg=Hf=0 pointwise for TWO distinct positive matter momentum profiles:
```
p_g=r²[(3Pg²/4+r Pg Pg'/2)/(Mg² a)-m² Mg² a³ V_g(y)],
p_f=r²[(3Pf²/4+r Pf Pf'/2)/(Mf² b)-m² Mg² a³ V_f(y)],
y=b/a, V_g=β0+3β1 y+3β2 y²+β3 y³,
V_f=β1+3β2 y+3β3 y²+β4 y³.
```
**The full original unintegrated spherical EH+HR+dust primary constraints are independently evaluated; no primary residual is suppressed in code.** This family includes radially varying grav momentum AND two dust densities, so it is NOT merely a homogeneous canonical phase point; the 3-geometries nevertheless remain spatially flat and the dust clocks comoving.

**NEW restricted necessary secondary witness:** the full local mixed bracket on this explicit constraint surface has ONLY K00 nonzero, with the verified closed form:
```
K00(r)=[m² Mg² a² J(y)/2] r² [3X(r)+r X'(r)],
X=Pg/(Mg² a)-Pf/(Mf² b),
J(y)=β1+2β2 y+β3 y².
```
At `a=.4,r=.43,y=.5787707228025044`, all 5 checked primary residuals `(Hg,Hf,Ddiag,Dg,Df)=(+2.08e-17,-3.47e-18,0,0,0)`, `p_g=.189515033378>0,p_f=.022872502691>0`. The full independent local Poisson coefficient is **-0.11307718948650103**, versus analytical candidate **-0.11307718948650095**; all K-derivative slots are zero. Integrated against original compact N,M, bracket = **-7.916775842392439e-7** versus original full functional bracket **-7.916775842392432e-7**. Dropping radial X' incorrectly yields `-0.08394271077`. Synchronized `Pf=(Mf² b/(Mg² a))Pg` sets X=0, K00=0 while keeping both dust densities positive and distinct. When Pg and Pf are constants, `3X=chi` and the exact previously verified homogeneous Step33b `(m² Mg² a²/2)J chi` bracket is recovered after dividing by r². Benchmarks cover a=1,.4,.2,.05,.03, multiple radial points and different polynomial momenta, plus 7 homogeneous chi=0 Candidate epochs. **Necessary condition on THIS subclass only, no universal local BD theorem.**

**ACTUALLY EXECUTED:** 52 focused tests PASS together in **/mnt/data/janus33e** = original 31 Step33e tests (both original source/test exact SHA matches preexisting live GitHub) + **21 new Step33f pytest cases**. `scripts/verify_gate2b_step33f.py` independently exits 0/52 and writes `gate2b-step33f-report.json` with reproducibility digests and flags: `full_repository_regression=false`, `general_local_BD_secondary=NOT_DERIVED`, `Dirac_secondary_preservation_and_lapse_fixing=NOT_DERIVED`, DeFelice/Aoki NOT_RUN, GATE2B OPEN. Earlier Step33d 95 and Step32e 93 tests NOT rerun here; no Git checkout full suite/CI/peer replication. A minor initial Python generator-parentheses syntax mistake in the new test witness was caught and corrected before all tests passed. Five newly published files EXACT GitHub blob SHA matched local tested files:
- `numerics/hr_spherical_local_mixed_kernel.py` `122351f41dd85d6d2a91ca1345cec54a2ad1fad3`
- `numerics/hr_spherical_radial_primary_surface.py` `a6dc81ff47c335cf9f41a46e760e910ebd451a43`
- `tests/test_hr_spherical_local_primary_kernel.py` `473caf36c7a17f3a998dbb3c4118815004b99786`
- `scripts/verify_gate2b_step33f.py` `c258c6bd2cbd45b9af8222fab75f112ee4971a2e`
- `research/SPHERICAL_LOCAL_PRIMARY_SURFACE_STEP33F_AUDIT.md` `5560023dc2789a5996f546e1799abad1a28f4b37`

**NEXT EXACT HARD RED:**
1. Generalize the PRIMARY-SURFACE analysis beyond spatially FLAT g/f slices and comoving dust phases. Include genuinely curved/relative radial profiles, Dg/Df nonzero but Ddiag=0, radial matter phase gradients and exact relative shift z*. Analyze local differential smearing coefficients only AFTER imposing the true full local Hamiltonian and momentum primary constraints.
2. On this genuine general primary surface, derive and preserve any local HR BD SECONDARY using the complete Dirac Poisson/rank/lapse-fixing algorithm; handle regular and degenerate J(y)=0 or K(r)=0 branches honestly. Do not extrapolate `3X+rX'` beyond this witness subfamily.
3. Integrate with the Step32e full time-supported, fully time-integrable action; find a genuine physically NONHOMOTHETIC ON-SHELL two-metric/two-dust solution, not the Step30 pure coordinate transformation; pass independent same-constrained-action De Felice finite-H mu→0 and nonlinear Aoki KS,cS² stable/unstable controls before relative μ fold1 a≈.0301646.
4. Publish NEGATIVE conclusion if a physics acceptance criterion fails; no physical ghost/speed/CMB claim from these algebraic tests.

**VERDICT:** `STEP33F_LOCAL_MIXED_KERNEL_GREEN`, `RESTRICTED_RADIAL_PRIMARY_SURFACE_GREEN`, `GENERAL_BD_SECONDARY_AND_PRESERVATION_OPEN`; **`GATE_2B=OPEN`, JANUS-R NOT VALIDATED**. Continue ONLY on branch `research/gate2b-nonhomothetic-transfer`, preserve `main` and `research/v2-flrw`, external wrong-sign-f-EH JHR audit separate.

---

# JANUS — REPRISE PRIORITAIRE : ÉTAPE 33e (2026-10-19)

**FIRST READ:** `research/SPHERICAL_MIXED_HAMILTONIAN_POISSON_STEP33E_AUDIT.md`.
**NEW module:** `numerics/hr_spherical_mixed_hamiltonian_bracket.py`.
**NEW 31 tests:** `tests/test_hr_spherical_mixed_hamiltonian_bracket.py`.
**REPRODUCE:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33e.py gate2b-step33e-report.json`.

## Step33e — MIXED radially smeared spherical Poisson {H_g[N],H_f[M]} COMPUTED on off-shell family; full BD SECONDARY STILL OPEN

**Real mathematical advance over Step33d:** both positive-EH spherical ADM gravitational constraints (including exact intrinsic spatial curvature and radial pL derivatives), the full all-beta Hassan–Rosen potential and BOTH independently canonical dust phase/momentum pairs now enter the explicitly computed *radially smeared mixed* functional Poisson bracket of the two lapse constraints. The exact lapse-linear relative shift is algebraically eliminated on its REGULAR K!=0 branch with z*=u/sqrt(1+u²), u=Dg/K. Both derivatives z*'(r) and z*''(r) are included. Each primary H_g,H_f is separately stationary under z at z* (∂_z H_g=F_z/Lg, ∂_z H_f=F_z/Lf), allowing an exact envelope-theorem functional differentiation — no treating z as a physical canonical pair.

**Crucial radial integrations by parts:** the 3-curvature contribution integrated against a compact N becomes `-M²[N L+N S_r²/L+2N_r S S_r/L]`. The g momentum-gradient term in H_g transforms `-N z pL_g'→(Nz)'pL_g`; in H_f transforms `-M z Lg pL_g'/Lf→(M z Lg/Lf)'pL_g`. Symbolic partial functional jets are differentiated via SymPy; radial total derivatives are computed using complex-step on analytic nonhomogeneous radial profiles. Independent direct variations of the ORIGINAL curvature-containing, pL'-containing action verify **all 12 canonical field gradients of BOTH Hamiltonians** for eliminated z*, plus eight additional canonical gradient controls at externally fixed z.

**Actual OFF-SHELL arbitrary nonhomogeneous regression on r in [.1,.9], positive Mg²=1.7 Mf²=.63 m²=.91, five beta values (.2,1.3,-.35,.4,-.17), 48-point Gauss quadrature:**
```
{H_g[N],H_f[M]}                  = +1.2437914369616798e-06
Six pair contributions in order:
(Lg,pLg)                        = +1.9582294901110296e-05
(Sg,pSg)                        = -1.8544242941402666e-05
(theta_g,p_g)                   = +2.372118038057092e-08
(Lf,pLf)                        = -3.4075573609340606e-08
(Sf,pSf)                        = +2.1609387048281924e-07
(theta_f,p_f)                   = 0 [structural to THIS mixed bracket, NOT elimination of f dust]
shift equation |F_z| max         = 4.163336342344337e-17
when z is EXTERNAL fixed          = +4.993895796055337e-07 [NOT identical]
with radial smearings N ↔ M      = +1.2077059811667116e-06 [radial test derivatives matter]
when m²=0 and fixed z=0          = 0 [independently decoupled sectors]
```
**DO NOT CONFUSE with a physical observable or an ON-SHELL secondary constraint**: test data deliberately violate primary constraints. Both matter pairs remain in the full canonical action, although f dust's direct contribution to this specific mixed bracket is zero because H_g and z* are independent of (theta_f,p_f). A nonzero off-shell bracket alone cannot infer the local BD secondary or propagating ghost count.

**ACTUAL meaningful RED→GREEN bug:** the first symbolic implementation wrongly unpacked the interleaved canonical vector and swapped Sg with pLg and Sf with pLf, producing a FALSE bracket ~0.00636. Independent comparison against the ORIGINAL non-IBP Einstein–Hilbert+HR+dust primary smearing caught this error; corrected exact result is 1.2437914e-06. The full error and correction are documented in the audit and protected by new tests. A full expansion of all symbolic functional Euler expressions previously exceeded compute timeout; retained exact partial symbolic derivatives combined with controlled analytic-profile complex-step radial total derivatives.

**ACTUALLY EXECUTED:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests` => **31 NEW tests PASS in NEW standalone /mnt/data/janus33e**, ~12s. `scripts/verify_gate2b_step33e.py` independently ran the 31 tests (exit0, ~10.5s), produced `gate2b-step33e-report.json` and explicit provenance/physical NOT_DERIVED. Prior Step33d 95 tests and Step32e 93 tests were **NOT rerun here**; NEVER claim 126 combined tests in a single run, no clean Git clone/CI/independent peer review. All FOUR new source/test/runner/audit Git blob hashes MATCH the real local source bytes:
- numerics/hr_spherical_mixed_hamiltonian_bracket.py `6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81`
- tests/test_hr_spherical_mixed_hamiltonian_bracket.py `ed3525383bc61b6b1cc838f29139df9663add918`
- scripts/verify_gate2b_step33e.py `4946e1afd06d3d750f93f635ce0ce446c562811c`
- research/SPHERICAL_MIXED_HAMILTONIAN_POISSON_STEP33E_AUDIT.md `85e1d346c19ef5ca4f9649968d3514b51f08816a`

**NEXT STRICT RED, exact ordered continuation:**
1. **LOCAL DISTRIBUTION + PRIMARY CONSTRAINT SURFACE:** express the mixed bracket as local smearing coefficients of N M, N'M, N M' plus contributions proportional to Ddiag and F_z; choose radial canonical test data satisfying BOTH H_g=0,H_f=0 and Ddiag=0, rather than off-shell arbitrary polynomials. Determine whether a further independent secondary condition is forced or lapses are simply fixed.
2. Compute full Dirac time preservation, secondary Poisson rank and lapse-fixing with BOTH g and f canonical dust pairs; establish or falsify the genuine SPHERICAL local HR BD primary-secondary pair. Never directly extrapolate the homogeneous chi result of Step33b.
3. Compare to fully time-integrable same-action Step32e compact perturbations and gauge closure; independently obtain a truly NONHOMOTHETIC on-shell two-matter bimetric background beyond passive chart compensation.
4. SAME reduced physical action must reproduce BOTH finite-H mu→0 De Felice scalar and nonlinear homothetic Aoki K_S,c_S² stable+unstable benchmarks prior to Candidate-C relative mu fold at a≈0.0301646; no physical ghost/speed/fold/CMB claim yet.

**Verdict:** `STEP33E_RADIAL_MIXED_HH_POISSON_OFFSHELL_GREEN`; `LOCAL_BD_SECONDARY_OPEN`; `GENUINE_NONHOMOTHETIC_ONSHELL_OPEN`; **`GATE_2B_OPEN`; JANUS-R NOT VALIDATED**. Work ONLY in `research/gate2b-nonhomothetic-transfer`; main and research/v2-flrw untouched; external wrong-sign-f-EH JHR audit separate.

---

# JANUS — REPRISE PRIORITAIRE : ÉTAPE 33d (2026-10-19)

**READ FIRST** `research/SPHERICAL_RADIAL_DIAGONAL_WARD_STEP33D_AUDIT.md`.
**NEW** `numerics/hr_spherical_diagonal_primary_ward.py`; `tests/test_hr_spherical_diagonal_primary_ward.py`.
**FOCUSED ONE-COMMAND REPRODUCTION** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33d.py gate2b-step33d-report.json`.
**ALSO READ** `research/SPHERICAL_DUST_SMEARED_POISSON_STEP33C_AUDIT.md`, `numerics/hr_spherical_radial_diffeo_ward.py` (these Step33c files were already committed unchanged).

## Step 33d — local diagonal SPATIAL gauge algebra and both spherical primary H Ward GREEN; mixed H_g/H_f and local BD SECONDARY OPEN

**New work beyond Step33b homogeneous PB:** radial canonical field functions with TWO independent full metric pairs `(Lg,pLg),(Sg,pSg)`, `(Lf,pLf),(Sf,pSf)`, and TWO irrotational dust canonical pairs `(theta_g,p_g),(theta_f,p_f)`, all retained in the exact spherical ADM gravitational+all-beta HR+two-dust primary constraint functions `H_g(r),H_f(r),Ddiag(r)`. The relative-shift scalar z and its exact algebraic root are transported correctly.

**Step33c (previously on GitHub):** independently finite-differentiate the discretized exact square-root dust Hamiltonians in EVERY nodal phase/momentum component and independently evaluate the radial continuum identity `{H_d[N],H_d[M]}=D_d[(N M'-M N')/L²]` in EACH dust sector. The two species have zero cross Poisson bracket. The relativistic square root is essential: a prematurely quadratic `sqrt(1+u²/L²)` approximation fails local algebra. 12 new Step33c dust tests; no full EH/HR mixed PB yet.

**Step33c spatial Ward (also previously on GitHub):** full spherical diagonal radial momentum density `Ddiag=Σ_i[pS_i S_i'-L_i pL_i'+p_i theta_i']`. Independently differentiated all TWELVE functional gradients of its smearing `D[eta]`, retaining all SIX canonical pairs. The exact canonical radial bracket closes:
```
{D[eta],D[xi]} = D[eta xi' - xi eta'],
canonical-gradient numerical witness    +2.1205209587301715e-05
directly integrated RHS                 +2.1205209587301945e-05
difference                              -2.30392961653e-19.
```
At nonhomogeneous radial test profiles, BOTH full HR+EH+dust primary lapse coefficients H_g,H_f transform as radial densities of weight1, Ddiag and the z equation as weight2, relative shift root z* as a scalar, and the two 3-curvatures as scalars. Differencing near the origin has known 1/r² cancellation conditioning; tolerances controlled. 23 Step33c spatial tests.

**NEW Step33d discriminating check:** directly integrate BOTH entire `H_g[N],H_f[N]` for a compact radial lapse test N; independently vary all canonical fields under a common radial diffeomorphism, compare to the exact integration-by-parts Ward `delta_eta H_i[N] = -∫dr eta N' H_i` across 3 quadrature orders. TWO additional negative tests deliberately (a) transform f dust p_f as scalar instead of radial density, and (b) transform relative z as density instead of scalar; BOTH produce Ward failures. 3 NEW Step33d tests. This is **NOT an evaluation of `{H_g[N],H_f[M]}`**.

**ACTUAL EXECUTED TOGETHER:** in fresh focused `/mnt/data/janus33c`, `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests` → **95 PASSED**; the Step33d JSON runner independently returned exit0 / 95 passed (21 Step33a + 36 Step33b + 12 Step33c dust + 23 Step33c spatial + 3 Step33d). Step33a/b and Step33c spatial source/test exact GitHub blob bytes matched local; the four NEW Step33d files exact local-vs-live SHA:
- `numerics/hr_spherical_diagonal_primary_ward.py` `4a8a14a7294f810265f309eb5575d73f4528b988`
- `tests/test_hr_spherical_diagonal_primary_ward.py` `2d0a546fe3136d550d034a668c631d3e3ae93ce9`
- `scripts/verify_gate2b_step33d.py` `0207bef57cd68e17ad3ca9061ad1456d71a8529d`
- `research/SPHERICAL_RADIAL_DIAGONAL_WARD_STEP33D_AUDIT.md` `d38f2eb68ff0e2e0e01e92ded47ebec5b20b86cc`

**HONEST scope:** a focused reconstructed project, **NOT a complete clean Git checkout or full repo suite/CI**, old 93 Step32e tests NOT rerun in this workspace. The homogeneous Step33b secondary is NOT a proof of inhomogeneous bimetric BD secondary. A radial `D-D` closure and `D-H` Ward are NECESSARY BUT INSUFFICIENT. NO gauge-complete 4D HR BD primary/secondary constraint reduction, physical kinetic/gradient signs, genuinely NONHOMOTHETIC on-shell Candidate-C branch, finite-H De Felice/Aoki same-action validation, relative-mu fold crossing, or CMB likelihood established.

**NEXT HARD RED — PRIORITY FOR NEXT RUN:**
1. From `numerics/hr_spherical_adm_primary.py`, derive the **SPATIALLY SMEARED MIXED FUNCTIONAL POISSON BRACKET** `{H_g[N],H_f[M]}`, including radial metric spatial-curvature derivative terms/IBP, both independent matter momenta, the lapse-independent z equation and the boundary contributions. Avoid substituting the homogeneous chi blindly.
2. Compute the time preservation of any resulting local constraint, full Dirac rank and lapse fixing with both dust canonical pairs; prove or disprove the local HR BD secondary instead of inferring its existence from background or trial Hessian.
3. Match to exact time-integrable Step32e two-dust field action, solve independently a genuinely nonhomothetic on-shell Candidate-C background beyond passive diffeomorphic compensation, and pass De Felice finite-H mu->0 + Aoki homothetic nonlinear `K_S,c_S²` stable/unstable oracles from SAME physical reduced action.
4. Only then test the first relative mu fold at a≈0.0301646 and discuss viability/observables. Report negative result honestly if unavoidable.

**Scientific status:** `STEP33D_SPATIAL_DIFFEO_BRACKET_GREEN`; `STEP33D_HAMILTONIAN_SPATIAL_WARD_GREEN`; `FULL_MIXED_HH_AND_BD_SECONDARY_OPEN`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`. Continue ONLY on branch `research/gate2b-nonhomothetic-transfer`, leave main and v2-flrw untouched. The external JHR negative-f-EH-sign audit remains separate.

---

# JANUS — REPRISE PRIORITAIRE : 33c-SPATIAL, CONTRÔLE COMPLÉMENTAIRE (2026-10-19)

**READ FIRST:** `research/HAMILTONIAN_SPATIAL_DIFF_STEP33C_AUDIT.md`.
**Exact new source:** `numerics/hr_spherical_radial_diffeo_ward.py`.
**23 new tests:** `tests/test_hr_spherical_radial_diffeo_ward.py`.
**Dedicated reproducibility:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33c_spatial.py gate2b-step33c-spatial-report.json`.

## Latest supplemental result — full diagonal *radial momentum* functional bracket closes with both dust pairs (NOT the mixed HR Hamiltonian bracket)

This checkpoint is **COMPLEMENTARY**, not a replacement, to the existing independent Step33c dust-sector smeared Hamiltonian bracket in `research/SPHERICAL_DUST_SMEARED_POISSON_STEP33C_AUDIT.md`. Both are on the SAME protected research branch. Do not overwrite that work or its runner `scripts/verify_gate2b_step33c.py`. Their local test numbers come from separate reconstructions unless explicitly rerun together.

**Scientific proof:** use true spherical ADM data `L_i(r),S_i(r),pL_i(r),pS_i(r)` for BOTH metrics and independent canonical dust pairs `theta_i(r),p_i(r)`. The diagonal radial generator is
```
D[eta]=∫dr eta Σ_i[pS_i S'_i-L_i pL'_i+p_i theta'_i].
```
With eta zero at radial boundaries, directly integrate by parts to derive the 12 exact functional derivatives (for each g/f sector) `δD/δL=-eta pL'`, `δD/δpL=(eta L)'`, `δD/δS=-(eta pS)'`, `δD/δpS=eta S'`, `δD/δtheta=-(eta p)'`, `δD/δp=eta theta'`. Their Poisson bracket numerically satisfies **`{D[eta],D[xi]}=D[eta xi'-xi eta']`** with sample `+2.3726108629148702e-05` vs separate direct integral `+2.372610862915291e-05`, residual -4.21e-18. All 12 functional gradients are independently verified against direct varied smeared action.

**Full nonlinear radial density Ward:** keep BOTH positive EH ADM 3-curvatures and momenta, all-beta HR potential, independent g/f canonical dust H and momentum contributions, the relative shift z(r), its algebraic equation and root. Under diagonal radial coordinate variations `delta H_g=(eta H_g)'`, `delta H_f=(eta H_f)'`, `delta D=eta D'+2eta' D`. Two EH 3-curvatures and solved z root transform as scalars; the relative shift equation has density weight2. The tested metric Hamiltonian residuals are <2e-10 and D residuals <1e-11 across five radii. 3-curvature near center suffers explicit 1/r² cancellation: residual ~1e-7 at r=.14, retained as numerical-conditioning limitation rather than silently accepted as exact zero.

**Actual tests and provenance:** **80 PASS in ONE focused local `/mnt/data/janus33b`** = 21 previous Step33a (byte-exact) + 36 previous Step33b (byte-exact) + 23 new 33c-spatial. Direct pytest and `scripts/verify_gate2b_step33c_spatial.py` report exit0/80; script verifies prior Step33a/33b Git blob hashes, emits source SHA-256, marks `focused_non_git_workspace`, `full_repository_regression=false`, mixed local Hamiltonian bracket NOT_DERIVED, HR BD secondary NOT_DERIVED, De Felice/Aoki NOT_RUN, true nonhomothetic background NOT_FOUND and GATE2B OPEN. All four new files exactly match local executed Git blobs:
- `numerics/hr_spherical_radial_diffeo_ward.py`: `89e7f6eab35d28317f2f7a4330601736525487e5`
- `tests/test_hr_spherical_radial_diffeo_ward.py`: `62282904a78af356121fb2fc1dc8046d7f92e0d7`
- `scripts/verify_gate2b_step33c_spatial.py`: `39167ce8fd02fe3e83cf6059c072ca108ff84900`
- `research/HAMILTONIAN_SPATIAL_DIFF_STEP33C_AUDIT.md`: `a06dee160a35bcd905a32c865eb9a743cd0bf428`.

**Critical missing physical gate:** The above closes `D-D` and covariance of complete `H_g,H_f` under D; separate Step33c dust audit closes its own matter Hamiltonian bracket. **Neither computes `{H_g[N],H_f[M]}` and the full nonlinear functional HR Boulware–Deser secondary constraint.** Next form that functional bracket with all curvature derivatives, `pL'`, two dust pairs and relative shift z on compact smearings; then time-preserve the secondary and derive full constrained kinetic/gradient operators on an actual nonhomothetic on-shell background. Require same action physical De Felice finite-H mu→0 and Aoki homothetic KS,cS² stable/unstable oracles before first relative mu fold a≈0.0301646.

**Verdict:** `RADIAL_DIAGONAL_D_D_FUNCTIONAL_CLOSURE_GREEN`, `TWO_DUST_PAIRS_GREEN`, `MIXED_HAMILTONIAN_FUNCTIONAL_BRACKET_RED_OPEN`, `LOCAL_HR_BD_SECONDARY_OPEN`, `GATE_2B_OPEN`; JANUS-R not yet validated. This step is a structural spatial gauge test, not a physical ghost/speed proof. Active branch ONLY research/gate2b-nonhomothetic-transfer; main/v2-flrw untouched.

---

# JANUS — REPRISE PRIORITAIRE, ÉTAPE 33c (2026-10-19)

**FIRST READ:** `research/SPHERICAL_DUST_SMEARED_POISSON_STEP33C_AUDIT.md`.
**New exact matter radial bracket:** `numerics/hr_spherical_dust_smeared_bracket.py`.
**New tests:** `tests/test_hr_spherical_dust_smeared_bracket.py`.
**Reproduce:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33c.py gate2b-step33c-report.json`.

## 33c — TWO-dust RADIAL FUNCTIONAL constraint Poisson bracket GREEN; full spherical HR/BD secondary still OPEN

**ACTUAL MATHEMATICAL ADVANCE beyond 33b homogeneous Poisson:** at arbitrary regular nonhomogeneous radial dust field `theta(r)`, positive canonical p(r) and metric radial length L(r)>0, each irrotational dust has EXACT canonical constraints
`C_d(r)=p sqrt[1+(theta'/L)²]`, `D_d(r)=p theta'`. For smooth compact smeared lapses N,M the FUNCTIONAL radial Poisson bracket closes exactly on the dust momentum constraint:
```
{H_d[N],H_d[M]} = D_d[(N M'-M N')/L²]
                = int dr p theta'/L² (N M'-M N').
```
Direct functional variations `δH[N]/δtheta=-(N p theta'/(L² h))'`, `δH[N]/δp=N h` were used, with h=sqrt(1+theta'²/L²), plus compact-support radial IBP. The g and f dust canonical phase-space pairs remain separate and their **cross-dust** Poisson brackets vanish identically. This bracket is generically NONZERO if theta' !=0; the homogeneous reduction 33b suppresses it. An intentionally nonrelativistic truncated dust h=1+theta'²/(2L²) FAILS closure by symbolic residual theta'³/(2L⁴); negative numerical control passes.

**Independent numerical check:** from the **discretized nonlinear dust Hamiltonian** H[N]=sum_j N_j P_j sqrt[1+(Dtheta)_j²/L_j²] with true nodal canonical P_j=w_j p_j, separately finite-differentiate EVERY nodal theta and P coordinate and compute the discrete PB. Its result converges under n=33→65→129 to the INDEPENDENT continuum momentum-bracket integral. Example seed_shift=.3 target n129 -0.0004726532006 versus nodal PB -0.0004726019329; the truncated relativistic Hamiltonian gives -0.0005758332733. Antisymmetry, homogeneous theta'=0, two disjoint dust species, invalid metric, boundary and step controls pass.

**ACTUALLY TESTED together IN ONE focused non-git /mnt/data/janus33c:** 69 PASS = 21 Step33a +36 Step33b +**12 NEW Step33c**. Step33c JSON runner exit0/69 PASSED, confirms original 33a/b Python/test Git blob SHA exact, flags full repo regression false, radial HR BD constraint NOT_DERIVED, De Felice/Aoki NOT_RUN and GATE_2B OPEN. Historical Step32e 93 NOT rerun, no claim 162 combined. All FOUR new files exact-byte matched local executed Git hashes:
- `numerics/hr_spherical_dust_smeared_bracket.py`: `d64ba7f790e63e21c626bb93763d971bb50b8fc2`
- `tests/test_hr_spherical_dust_smeared_bracket.py`: `3a986c01c1ef1cd25d9ad2f9314719fe82233772`
- `scripts/verify_gate2b_step33c.py`: `4222c527c56b4e98adfab2ee4083cd28e3135de7`
- `research/SPHERICAL_DUST_SMEARED_POISSON_STEP33C_AUDIT.md`: `b3cccbdb4c28d20841722492c9bbc1ffeaeb7a99`

**HARD LIMITATION:** Dust-only functional bracket ≠ full coupled spherical field-theory ADM/HR primary/secondary bracket. Still missing EH radial curvature/momenta in cross brackets, all-beta HR radial/Stueckelberg relative shift z and its constraint, boundary terms, local diagonal Noether and BD secondary temporal preservation. Do NOT infer no BD ghost, kinetic stability, De Felice/Aoki scalar speed or Candidate-C fold from this. Existing on-shell Candidate-C controls are homogeneous and WITHOUT RADIATION, genuine physical nonhomothetic solution not yet found.

**NEXT EXACT RED:**
1. Extend this smearing/functional derivative engine to the **COMPLETE spheriсal coupled** positive-EH_g/f + all-beta HR + two-dust Hamiltonian (Step33a), including radial derivatives, z stationarity, constraints and boundary terms. Verify full smeared `{C_g[N],C_f[M]}`, diagonal momentum constraint and potential local HR BD secondary against independent finite differences.
2. Determine local secondary time preservation, appropriate lapse-fixing and constraint rank; preserve both canonical dust phase-space pairs. Compare action-level to Step32e integrable 18-field spacetime action without illicit finite-basis Schur.
3. Separately seek full genuinely NONHOMOTHETIC on-shell two-metric+two-dust Candidate-C or scientifically document failure, then SAME reduced-action De Felice finite-H mu→0 and nonlinear homothetic Aoki K_S,c_S² stable+unstable limits, then first relative mu-fold at a~0.0301646. No observational claims until physical gates.
4. Keep checkpoint and scientific audits updated after every correction; commit only research/gate2b-nonhomothetic-transfer, main/v2-flrw untouched.

**STATUS `STEP33C_RADIAL_DUST_FUNCTIONAL_POISSON_GREEN`; `FULL_SPHERICAL_BD_SECONDARY_OPEN`; `GATE_2B=OPEN`; JANUS-R NOT VALIDATED.** Distinguish external JHR 2026 negative f Einstein–Hilbert-sign manuscript from positive-EH JANUS-R audited here.

---

# JANUS — REPRISE PRIORITAIRE : ÉTAPE 33b (2026-10-19)

**FIRST READ** `research/HOMOGENEOUS_POISSON_SECONDARY_STEP33B_AUDIT.md`.
**Executable:** `numerics/hr_homogeneous_poisson_secondary.py`.
**Tests:** `tests/test_hr_homogeneous_poisson_secondary.py`.
**Reproduce:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33b.py gate2b-step33b-report.json`.

## Step33b — exact HOMOGENEOUS Poisson secondary and two-dust lapse fixing GREEN, local radial BD still OPEN

**MAJOR VERIFIED ADVANCE:** from Step33a exact two-metric spherical ADM primary Hamiltonian, impose HOMOGENEITY only AFTER reduction to eight minisuperspace canonical coordinates `(a,b,theta_g,theta_f,p_a,p_b,p_g,p_f)` keeping TWO independently conserved dust momenta. Positive-EH g/f and exact all-beta HR produce primary constraints `Hg=-pa²/(12Mg²a)+m²Mg² a³ V(b/a)+pg`, `Hf=-pb²/(12Mf²b)+m²Mg² a³ W(b/a)+pf`. The exact Poisson bracket factorizes:
```
{Hg,Hf}=(m² Mg² a² / 2) J(b/a) chi,
J(y)=beta1+2 beta2 y+beta3 y²,
chi=pa/(Mg² a)-pb/(Mf² b).
```
The scalar `chi=0` is a HOMOGENEOUS secondary condition only on the regular dynamical branch m²*J !=0. On the branch J=0 or m²=0, dividing by the factor is ILLEGAL; negative tests prevent spurious secondary inference. Its time preservation `Ng{chi,Hg}+Nf{chi,Hf}=0` fixes the lapse ratio when the second bracket is nondegenerate. The exact formula recovers Candidate-C dust-only `Nf/Ng=y+y_N` independently at a=1,.8,.4,.2,.09,.05,.03. Two dust momenta retain independent canonical brackets; a three-constraint HOMOGENEOUS Dirac matrix has rank2 on these examples, with diagonal-lapse null combination. Full true spherical 4D primary/secondary and local radial derivatives NOT DERIVED.

**Independent tests:** Symbolic exact SymPy eight-variable PB + two separate numerical finite-difference PB controls + literal homogeneous embedding into REAL spherical ADM Step33a density (including essential radial momentum derivative) + seven Candidate-C epochs + J=0/m²=0 degeneracy + independent dust clocks + homogeneous Dirac rank. **57 tests PASS IN ONE focused non-Git workspace `/mnt/data/janus33b` =21 exact Step33a +36 new Step33b**; test runner reports exit0. Prior Step32e 93 tests NOT rerun; DO NOT claim 150 jointly executed. No full clean clone/GitHub Actions or external peer reproduction.

**Live GitHub files already committed on this research branch** (verified):
- `numerics/hr_homogeneous_poisson_secondary.py` blob `43e03d01da57ddc23acb75db0ae660c001ea8e38`.
- `tests/test_hr_homogeneous_poisson_secondary.py` blob `0c09ae4ae470a7e8b96dabac4909b1dfa7b8510d`.
- `scripts/verify_gate2b_step33b.py` blob `83a32704a819e9a94785be0c0de6b87a663a8b15`.
- `research/HOMOGENEOUS_POISSON_SECONDARY_STEP33B_AUDIT.md` blob `85f120309697b9a47796825034e7415bb07f7d9b`.
The two executable/test source blobs match local tested code exactly. The GitHub runner/audit were committed independently of the local runner text; do NOT claim their SHA matches the locally generated alternatives without a byte comparison. Stage33b user report produced locally as `/mnt/data/janus33b/gate2b-step33b-report.json`.

**NEXT CRITICAL RED:** compute actual SPATIALLY SMEARED radial functional Poisson brackets of the exact spherical ADM constraints including radial gradients and BOTH dust clocks/charges; determine local HR BD secondary and its time preservation with lapse/shift equations. The homogeneous secondary `chi` is NECESSARY controlled benchmark, NOT the answer in local field theory. Compare constraints with full time-integrable Step32e action, find genuinely nonhomothetic on-shell Candidate-C beyond pure-chart compensation, then independently pass De Felice finite-H mu→0 and Aoki nonlinear homothetic K_S,c_S² stable+unstable physical oracle from SAME fully reduced action BEFORE a≈0.0301646 fold.

**Verdict: `HOMOGENEOUS_SECONDARY_AND_LAPSE_FIXING_GREEN`; `LOCAL_SPHERICAL_BD_SECONDARY_OPEN`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`.** Leave `main` and `research/v2-flrw` untouched. Distinguish external opposite-f-EH-sign JHR manuscript from our positive-sign JANUS-R.

---

# JANUS — POINT DE REPRISE PRIORITAIRE : ÉTAPE 33b (2026-10-19)

**READ FIRST:** `research/HOMOGENEOUS_POISSON_SECONDARY_STEP33B_AUDIT.md`.
**New code/test:** `numerics/hr_homogeneous_poisson_secondary.py`, `tests/test_hr_homogeneous_poisson_secondary.py`.
**Reproduce EXACTLY:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33b.py gate2b-step33b-report.json`.

## 33b — Canonical two-dust HOMOGENEOUS primary Poisson and secondary conservation GREEN; true LOCAL radial BD SECONDARY still OPEN

**Scientifically new:** from Step33a's EXACT positive Einstein–Hilbert g/f spherical ADM+GHY and all-beta HR lapse-affine Hamiltonian with TWO canonical dust pairs, derive the separate spatially-flat **homogeneous** constraints `H_g,H_f` with 8-dimensional canonical variables `(a,b,theta_g,theta_f,pa,pb,pg,pf)`. The phases are cyclic and both dust momenta separately conserved (NO dust merger, NO early dust elimination). On generic off-shell samples, the Poisson bracket is not zero. Exact symbolic and numeric independent Poisson derivations agree on

```
{H_g,H_f} = (m² Mg²/2) a² J(y) χ,
y=b/a, J(y)=β1+2β2 y+β3 y²,
χ=pa/(Mg² a)-pb/(Mf² b).
```

On the **REGULAR homogeneous dynamical branch** `m² J(y) !=0`, primary preservation imposes `χ=0` as **HOMOGENEOUS secondary**. This is NOT the field-theoretic inhomogeneous Hassan–Rosen BD secondary. Branch `J=0` (algebraic) and `m²=0` are guarded: they do NOT imply `χ=0` from this bracket.

**Explicit secondary time preservation:** `Bg={χ,Hg}`, `Bf={χ,Hf}` are derived exactly including both HR potentials, both GR kinetic terms and both dust charges. On homogeneous primary+secondary surface with `Bf !=0`, `Nf/Ng = -Bg/Bf`. Independent 8-variable centered Poisson checks and symbolic SymPy test pass. On the no-radiation dust-only Candidate-C branch, this lapse ratio agrees with the independently recomputed `Nf=y+d y/dln a` Bianchi relation:
```
a=1    y=.556882559187308   Nf/Ng=.551545778648274
a=.4   y=.578770722802504   Nf/Ng=.518526433827902
a=.09  y=.939977525126337   Nf/Ng=.416922093339096
a=.03  y=1.979545244854517  Nf/Ng=.461831564933199.
```
Representative homogeneous constraint/secondary residuals ~1e-13 or smaller. Explicitly refuse to claim physical lapse fixing OFF the constraint surface.

**Dirac constraint matrix in the HOMOGENEOUS 3-constraint model** (Hg,Hf,χ) is antisymmetric with elements `{χ,Hg}=Bg`, `{χ,Hf}=Bf`: on the regular on-shell branch it has rank TWO and null vector `(1,Nf/Ng,0)`. This counts only the homogeneous mini gauge and second-class structure; it does **NOT** establish a BD ghost degree-of-freedom count for 3+1 gravity.

**Independent embedding into Step33a TRUE radial spherical ADM:** `L=a,S=a r,pL=(pa/3)r²,pS=(2pa/3)r,pLr=(2pa/3)r` (same for f), with dust p density `pg r²,pf r²`, reproduces `H_{g,f}^{spherical}/r² = H_{g,f}^{mini}` and `Ddiag=0` for radii .12,.31,.47 on Candidate-C and generic offshell. Deleting the radial momentum derivative `pLr` breaks Ddiag; this guards normalization and radial gradient but is NOT a computation of the functional field-theory Poisson bracket.

**ACTUAL REPRODUCTION:** **57 TESTS PASS in ONE local standalone workspace** `/mnt/data/janus33b`: 21 original exact-byte prior Step33a tests PLUS 36 newly parametrized Step33b tests. Both targeted pytest and `scripts/verify_gate2b_step33b.py` returned exit code 0, 57 passed. Runner JSON in `/mnt/data/janus33b/gate2b-step33b-report.json` records source SHA, `workspace_origin=focused_non_git_workspace`, `full_repository_regression=false`, `spatially_dependent_spherical_BD_secondary=NOT_DERIVED`, De Felice/Aoki NOT_RUN, true nonhomothetic background NOT_FOUND, `Gate2B=OPEN`. FOUR NEW files byte-exact Git blob match live GitHub:
- `numerics/hr_homogeneous_poisson_secondary.py`: `43e03d01da57ddc23acb75db0ae660c001ea8e38`
- `tests/test_hr_homogeneous_poisson_secondary.py`: `0c09ae4ae470a7e8b96dabac4909b1dfa7b8510d`
- `scripts/verify_gate2b_step33b.py`: `83a32704a819e9a94785be0c0de6b87a663a8b15`
- `research/HOMOGENEOUS_POISSON_SECONDARY_STEP33B_AUDIT.md`: `85f120309697b9a47796825034e7415bb07f7d9b`

Historical Step32e suite 93 tests was NOT rerun here; 57+93 is NOT a jointly executed count. Direct full repo clone/CI and independent peer reproduction not performed. No physical propagation/ghost/tensor/CMB interpretation from this homogeneous rank.

**NEXT EXACT HARD RED — STEP 33c:** compute FUNCTIONAL Poisson brackets of the **unreduced spherical radial** field-theory constraints `C_g(r),C_f(r),D(r)` from Step33a with compact smearings. Retain ALL spatial derivatives of `L,S,pL,pS`, curvature, HR relative shift solution `z(r)`, both independent dust phase and momentum fields, and boundary terms. Derive (or falsify) LOCAL HR BD secondary and its lapse-dependent time preservation; test closure with spatial diffeo generator. Do NOT transplant the homogeneous `χ` as the answer. Next also reconcile exact Step32e time-integrable action/Noether on shell and genuinely physical NONHOMOTHETIC two-metric/dust trajectory; pass same-action De Felice finite-H μ→0 & Aoki nonlinear homothetic KS,cS² stable/unstable oracles before Candidate-C first mu fold near `a≈0.0301646`.

**VERDICT:** `HOMOGENEOUS_SECONDARY=GREEN`; `TWO_DUST_CANONICAL_PAIRS=GREEN`; `TRUE_RADIAL_HR_BD_SECONDARY=OPEN`; `GENUINE_NONHOMOTHETIC_ONSHELL=OPEN`; **`GATE_2B=OPEN`; JANUS-R NOT VALIDATED.** Work ONLY on research/gate2b-nonhomothetic-transfer; leave main and research/v2-flrw unchanged. External JHR negative f Einstein–Hilbert sign critique separate.

---

# JANUS — REPRISE PRIORITAIRE, ÉTAPE 33a (2026-10-19)

**FIRST READ:** `research/SPHERICAL_ADM_HR_PRIMARY_STEP33A_AUDIT.md`.
**New module:** `numerics/hr_spherical_adm_primary.py`.
**21 new tests:** `tests/test_hr_spherical_adm_primary.py`.
**Repeat:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33a.py gate2b-step33a-report.json`.

## 33a. TRUE SPHERICAL ADM+HR Lapse-Affine Primary Interface GREEN — BD SECONDARY STILL OPEN

**New essential structural development beyond Step32e and the Step32c restricted Galerkin Schur:** formulate both positive Einstein–Hilbert metrics in spherical ADM variables
`ds_i²=-N_i²dt²+L_i²(dr+V_i dt)²+S_i²dOmega²`. The FULL nonlinear spherical EH ADM+GHY Legendre transformation produces exact momenta `pL_i=-2Mi² S_i² Kt_i`, `pS_i=-2Mi² L_i S_i(Kr_i+Kt_i)`, with gravitational constraints
`C_EH= L pL²/(4M²S²)-pL pS/(2M²S)-(M²/2) L S² R3`;
`D_EH=pS S'-L pL'` after explicit compact radial integration by parts. This is **field-density** Hamiltonian algebra, not a finite radial mode Schur. Both independently canonical dust pairs enter as `C_dust=p sqrt(1+theta_r²/L²)`, `D_dust=p theta_r` with p_g,p_f>0.

**Five-beta exact HR spherical principal-square-root:** the original potential at fixed old shifts `Vg,Vf` is NOT generically linear in lapses. Introduce relative shift
`Vf=V`, `Vg=V+(Ng/Lg+Nf/Lf) z`, `|z|<1`. Then **the exact total canonical density** is
`H=Ng[Cg+z Dg/Lg+Wg(z)]+Nf[Cf+z Dg/Lf+Wf(z)]+V(Dg+Df)`,
where `Cg,f=C_EH,g,f+C_dust,g,f`; `Dg,f=D_EH,g,f+D_dust,g,f`;
`Wg=m²Mg² Sg²[Lg A0+Lf A_tau sqrt(1-z²)]`,
`Wf=m²Mg² Sg²[Lf As+Lg A_tau sqrt(1-z²)]`,
`ell=Sf/Sg`,
`A0=β0+2β1 ell+β2 ell²`,
`As=β2+2β3 ell+β4 ell²`,
`A_tau=β1+2β2 ell+β3 ell²`.
**This is EXACTLY affine in the TWO true ADM lapses Ng,Nf and common radial shift V at fixed z**. The relative shift equation factorizes:
`dH/dz=(Ng/Lg+Nf/Lf) [Dg-K z/sqrt(1-z²)]`,
`K=m² Mg² Sg² Lg Lf A_tau`.
When K!=0, z is solved algebraically **without lapse dependence**:
`z=sign(K) Dg/sqrt(Dg²+K²)`. Test control K!=0 yields z≈-0.8408245009767221 with residual≈1.11e-16. No guessed root at K=0.

**TESTED:** 21/21 PASS in a NEW standalone `/mnt/data/janus33` with only new Step33a source/tests. Independent oracle computes exact HR potential via a separate matrix-inverse/determinant 2x2 principal root and all β0..4, compares to new closed form. Independently finite-differentiated original nonlinear EH Lagrangian reproduces canonical momenta. Radial integration by parts and lapse-affine gradient identities pass. **Genuine RED→GREEN:** an early test incorrectly assumed p_g cannot enter the f lapse coefficient; the shift redefinition explicitly introduces `z Dg/Lf`, a legitimate cross-sector coupling without mixing either dust phase pair. A numerical centered finite-difference tolerance was relaxed slightly; exact affine algebra remains fixed. The local JSON runner exit 0, 21 passed; `full_repository_regression=false`, `historical_step32e_93_tests_rerun=false`, full 4D gauge NOT_DERIVED, HR BD SECONDARY NOT_DERIVED, DeFelice/Aoki NOT_RUN, NONHOMOTHETIC on-shell NOT_FOUND; GATE2B OPEN. **Do not claim 93+21=114 jointly executed.** Git clone/CI not run.

**All FOUR new source/test/runner/audit bytes MATCH GitHub blob SHA EXACTLY**:
- `numerics/hr_spherical_adm_primary.py` `c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41`
- `tests/test_hr_spherical_adm_primary.py` `f71b687e9a9027dd0ce6b41553bcad68ba2b1133`
- `scripts/verify_gate2b_step33a.py` `e6b1aedd35183b2ce61ab08152ce6c5472d27858`
- `research/SPHERICAL_ADM_HR_PRIMARY_STEP33A_AUDIT.md` `e48b686b328bb7a4f7be322c1b33d55bfd570418`

**LIMITS, avoid overstating:** Spherical ADM lapse-affinity and lapse-independent z equation are **necessary primary constraint-structure** controls, NOT proof that a BD secondary closes and eliminates its mode, nor a proof of complete 4D helicity-0 dynamics. This arbitrary sample does not solve Cg=Cf=Ddiag=0. The earlier Step32e action is on shell only for PHYSICALLY HOMOGENEOUS dust-only Candidate-C, and passive compensated Step30 chart is not a new solution.

**IMMEDIATE NEXT RED:**
1. Explicit Poisson brackets/time preservation of the lapse-linear spherical HR constraints, derive (or falsify) BD secondary and lapse-fixing consistently with both conserved canonical dust pairs. Test boundary/noether and rank; do not infer from finite Hessian.
2. Connect this unprojected spherical ADM Legendre/relative shift to the Step32e exact common-time positive EH_g/f+HR+two-dust action, preserving time-dependent gauge closure and all spatial derivative terms.
3. Independently find or rule out a genuinely NONHOMOTHETIC physical on-shell g/f+two-dust background, not the Step30 passive compensator.
4. SAME-CONSTRAINED-ACTION De Felice finite-H μ→0 scalar and nonlinear homothetic Aoki KS,cS² (stable/unstable) oracles, then first Candidate-C relative μ-fold≈0.0301646. If failed publish precise negative gate.

**Verdict:** `SPHERICAL_ADM_HR_LAPSE_AFFINITY_GREEN`, `HR_BD_SECONDARY_OPEN`, `NONHOMOTHETIC_ON_SHELL_OPEN`, **`GATE_2B_OPEN`; JANUS-R NOT VALIDATED**. Work ONLY on research/gate2b-nonhomothetic-transfer. Protect main/v2-flrw; separate external JHR opposite-f-EH-sign tensor ghost criticism.

---

# JANUS — REPRISE PRIORITAIRE : ÉTAPE 32e (2026-10-19)

**FIRST READ:** `research/INTEGRABLE_DUAL_DUST_PHASE_STEP32E_AUDIT.md`.
**NEW EXECUTABLE:** `numerics/hr_integrable_two_dust_phase.py`.
**NEW 12 TESTS:** `tests/test_hr_integrable_two_dust_phase.py`.
**ONE-COMMAND REPRODUCTION:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step32e.py gate2b-step32e-report.json`.

## 32e — ALL 18 same-action compact parent fields and BOTH dust phase clocks now TIME-INTEGRABLE (LATEST)

**Actual RED→GREEN:** the prior Step32d complete positive Einstein–Hilbert g/f + full Hassan–Rosen beta0..4 + BOTH canonical irrotational pressureless dust action, on the physically HOMOGENEOUS radiation-free on-shell Candidate-C background, already had four true compact metric time-rate *parent* fields. But the TWO dust theta_rate jets at indices (6,13) were artificial independent rates and their nonzero first derivatives (+3.0040158156e-4, +4.1431447509e-5) were NOT legal tadpoles. Step32e now **reinterprets precisely those two slots as true compact parent fields** `theta_i(t,r)=theta_background_i(t)+[eta_i*T(t)+xi_i*G(t)]*F(r)`, with `G(t)=t*T(t)`, `G'(t)=T(t)+t*T'(t)`, and `T=[1-(t/time_radius)^2]^4`, while BOTH independent canonical positive momenta are `p_i=C_i r²[1+pi_i T(t)F(r)]`. Both theta_t AND theta_r derive from this ONE parent field in each sector, including nontrivial native/common lapse/shift.

**One exact five-sector common action:** no metric, EH radial/spatial intrinsic 3-curvature, extrinsic kinetic, HR interaction, measure or background source has been changed. Only the formerly nonintegrable canonical dust phase time/radial sampling was corrected. At zero new phase-parent amplitudes, the entire Step32d action (including all other 16 nonzero fields) is identical EXACTLY. Positive dust density multipliers are eliminated ONLY after the covariant dust Legendre transform; full reduced first-order density remains `p theta_t -N p sqrt(1+theta_r²/g_rr)-N^r p theta_r`. All 18 LEGITIMATE compact field first variations vanish on the on-shell homogeneous benchmark, max abs **1.3964523981613295e-11** at 20×20 quadrature and h=2e-5. The two newly integrable phase-parent first variations are **[0.,0.]**, versus disconnected old spurious numbers quoted above.

**True compact IBP/gauge-no-boundary control:** `integral p*delta_theta_dot = -integral delta_theta*p_dot` in both sectors. For a nonzero g phase/momentum trial, lhs=+3.5438771600125422e-6, rhs=+3.5438771600122983e-6; difference 2.439454888e-19. Canonical **projected** 2×2 p-amplitude vs NEW theta_extra parent coefficients are EXACTLY HALF the old rate-only projected coefficients since `integral T(t)*G'(t)dt = 1/2 integral T(t)^2 dt` by compact IBP:
```
H[p_g,theta_g_extra] = +4.725169547261010e-5
H[p_f,theta_f_extra] = +6.516963494914475e-6
off-diagonal cross-dust block = 0
rank = 2, max difference from independent analytic projection = 5.779e-15.
```
**These are projected symplectic phase-space pair controls, NOT the number, kinetic signs or speed of physical propagating modes.** The 18-compacted Galerkin basis is STILL NOT closed under the full local bimetric diagonal diffeomorphism group, and its formerly computed Step32c restricted 4×4 Schur is STILL NOT an ADM field constraint or BD reduction.

**ACTUAL single-workspace evidence:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests` -> **93 passed in 27.21s** in `/mnt/data/janus32` (29 Step31 + 20 Step32a + 11 Step32b + 11 Step32c + 10 Step32d + **12 NEW Step32e**). `scripts/verify_gate2b_step32e.py` separately returned exit 0 / **93 passed in 24.82s**, saved `/mnt/data/janus32/gate2b-step32e-report.json` with all exact source SHA-256/Git blobs, `workspace_origin=focused_non_git_workspace`, `full_repository_regression=false`, `true ADM=NOT_DERIVED`, `HR BD=NOT_DERIVED`, `DeFelice/Aoki=NOT_RUN`, `GATE_2B=OPEN`. It explicitly checks five original published source SHA against local source bytes before running. All FOUR new Step32e source/test/runner/audit files byte-identically match GitHub blobs:
- `numerics/hr_integrable_two_dust_phase.py` `fb6aaaadb1d5a99c0a119fbd05a706874fbfaa1a`
- `tests/test_hr_integrable_two_dust_phase.py` `daa84468756cdcc11bb62641350f89682a93cdf4`
- `scripts/verify_gate2b_step32e.py` `dc7041d790350c642a81e4519eb626018a1acf5e`
- `research/INTEGRABLE_DUAL_DUST_PHASE_STEP32E_AUDIT.md` `22590defae469b705f137d1402b3451bf6006a88`.

**HONEST SCOPE:** new 18-field compact time-integrable trial action is ON SHELL for the dust-only PHYSICALLY HOMOGENEOUS Candidate-C solution. NO physically genuinely NONHOMOTHETIC on-shell branch has been constructed; Step30's compensated f chart is ONLY a passive reparametrization. No full clean Git clone/full repo test/CI/peer review, and old Step27–30 separate suite tests not rerun. No actual field-theory lapse/shift gauge generator closure, no HR BD primary+secondary time-dependent constraint, no De Felice finite-H mu→0 physical speed, no Aoki nonlinear homothetic `K_S,c_S²`, no fold crossing and no CMB likelihood demonstrated.

**NEXT HARD RED — EXACT ORDER:**
1. From THIS Step32e integrable field/phase-space five-sector action, promote metric lapse and radial shift to genuine **ADM** local multiplier fields (not `Phi` as a restricted metric-component amplitude); formulate their local field-theory first-order auxiliary equations and on-shell diagonal Noether identities on a gauge-complete scalar ansatz. The finite-radial Step32c Schur must NOT be treated as the answer.
2. Extract & canonically reduce the HR **time-dependent BD-null primary/secondary constraints** while keeping BOTH independent dust `(theta,p)` pairs, deriving actual reduced physical scalar principal kinetic/gradient operators.
3. Separately solve or exclude a **genuinely nonhomothetic on-shell** g/f+two-dust background beyond passive chart compensation with all local Einstein/HR/Stückelberg/matter tadpoles.
4. On the SAME physical constrained action, pass De Felice finite-H `mu→0` physical scalar and Aoki nonlinear homothetic `K_S,c_S²` stable+unstable oracles, then test first relative-mu fold a≈0.0301646. Publish a negative verdict if physics gate fails, not a fitted matching claim.

**Verdict:** `STEP32E_ALL_18_TIME_INTEGRABLE=GREEN`; `TWO_DUST_CANONICAL_PAIRS=GREEN`; `TRUE_ADM_AND_BD_REDUCTION_OPEN`; `GENUINE_NONHOMOTHETIC_ON_SHELL_OPEN`; **`GATE_2B=OPEN` and JANUS-R NOT VALIDATED.** Work ONLY on branch `research/gate2b-nonhomothetic-transfer`; leave `main` and `research/v2-flrw` untouched. External JHR 2026 wrong-sign EH tensor-ghost audit remains SEPARATE.

---

# JANUS — REPRISE PRIORITAIRE, ÉTAPE 32d (2026-10-19)

**FIRST READ:** `research/INTEGRABLE_FOUR_METRIC_TIME_BASIS_STEP32D_AUDIT.md`.
**New source/test:** `numerics/hr_integrable_metric_time_basis.py`, `tests/test_hr_integrable_metric_time_basis.py`.
**One-command focused reproduction:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step32d.py gate2b-step32d-report.json`.

## 32d. REAL compact parent trace/shear fields and their TRUE time derivatives — all 16 legal on-shell tadpoles GREEN; ADM/BD physics still OPEN

**ROOT ISSUE FROM STEP32c HAS BEEN CORRECTED.** The Step32b scalar EH metric time-rate jets `delta psi_dot=b*T(t)*F(r)` and `delta E_dot=b*T(t)*r²F(r)` were disconnected from the derivatives of their actual compact parent spatial-metric profiles `a*T(t)F(r)`, which are `a*T'(t)F(r)`. Their nonzero raw integrated first action variations were NOT physical tadpoles and their 18-jet restricted 14×14 Schur was merely finite-basis algebra (NOT the physical kinetic/BD reduction).

**NEW Step32d action:** choose an independent smooth compact parent profile `G(t)=t*T(t)`, `G'(t)=T(t)+t*T'(t)`, where `T(t)=(1-(t/Tmax)^2)^4` vanishes with derivatives at the time boundaries. For both g and f use `psi_s=[psi0*T+psi1*G]F(r)` and `E_s=[E0*T+E1*G]r²F(r)`, and their EXACT time/radial derivatives. Recompute the nonlinear spherical EH_g/f **intrinsic 3-curvature and extrinsic rates**, the full all-beta HR interaction, and BOTH common-time canonical dust Hamiltonians on the SAME metric tensors. At zero extra four amplitudes the complete earlier Step32a 14-slot action is recovered exactly. Independently at two finite nonzero scalar metric points, `EH_new=EH_step31(psi_eff=psi0+t psi1,E_eff=E0+t E1)+exact_Step32b_ADM_rate_delta(psi_rate=psi1,E_rate=E1)`, including unchanged independent angular/spatial metric geometry.

**ACTUAL decisive on-shell result:** with the radiation-free PHYSICALLY HOMOGENEOUS on-shell Candidate-C background, ALL SIXTEEN legal compact field first variations vanish, max `1.3964523981613295e-11` (20×20 quadrature, finite amplitude step 2e-5). For FOUR new compact parent fields, first variations are `(-1.3010426069826053e-13,+4.336808689942017e-14,0,-4.336808689942017e-14)`. The old DISCONNECTED g trace rate jet first variation was `-3.058752883790261e-4`, compared to new integrable parent `-1.3010e-13`. This is genuine repaired time-integrability, NOT artificial constraint cancellation.

**Important dust subtlety from real RED-to-GREEN tests:** at a comoving canonical dust configuration with phase radial derivative=0 and positive FIXED momentum, `H_dust=N p` has no direct spatial-metric dependence. Thus a pure independent f trace perturbation changes the f Einstein–Hilbert 3-curvature and HR potential, but does NOT change its f dust action piece in that particular canonical configuration. The initially oversized numerical thresholds for tiny f EH/HR integrated responses were also corrected without modifying physics formulas. The two independent matter canonical p--theta_rate coefficients remain `+9.450339095e-05`, `+1.303392697e-05`, rank TWO.

**ACTUALLY EXECUTED together:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests` -> **81 PASS in ONE focused workspace** `/mnt/data/janus32`: 29 Step31 +20 Step32a +11 Step32b +11 Step32c +10 Step32d. `scripts/verify_gate2b_step32d.py` separately returned exit0/81 and recorded 16 legal tadpoles, dual canonical rank2, and all physical oracles NOT_RUN. New FOUR file Git blobs match local executed file bytes EXACTLY:
- `numerics/hr_integrable_metric_time_basis.py` `d6d8200ef583c25c232dd79b0e5aba1a206d41e5`
- `tests/test_hr_integrable_metric_time_basis.py` `f080670b594d0d084640d637ad2482e66bc5b9ea`
- `scripts/verify_gate2b_step32d.py` `02c86de9e348b4f7e0502c0ad180905ea903052d`
- `research/INTEGRABLE_FOUR_METRIC_TIME_BASIS_STEP32D_AUDIT.md` `63938f4cad110c18af899ca20e4b6e360cc5d01b`

**Still LIMITED:** two old dust `theta_rate` slots (6,13) remain disconnected LOCAL jets with nonzero raw first derivatives. Therefore the full 18-slot basis is NOT YET completely time-integrable. Nor is it complete under arbitrary local diagonal diffeomorphisms. The Step32c restricted 4x4 Schur must NOT be re-used unchanged as a physical ADM/BD or ghost/gradient analysis after this corrected field basis. The background is ON SHELL only for the dust-only PHYSICALLY HOMOGENEOUS Candidate-C, not a new nonhomothetic physical solution; Step30 compensations are coordinate relabellings. No true lapse/shift canonical constraints, HR BD-null, physical De Felice/Aoki scalar acceptance, relative mu fold or CMB likelihood yet.

**NEXT EXACT RED:**
1. Replace the TWO disconnected canonical dust phase-rate local jets with globally integrable compact parent phase perturbations (while preserving independent positive p_g,p_f variables). Demand all EIGHTEEN legal compact field first variations vanish after full time-supported integration and true dust phase IBP.
2. From the SAME action with genuine field/rate integrability derive full ADM lapse/shift and HR BD-null canonical constraints, keeping BOTH matter phase-space pairs; recover physical principal kinetic/gradient symbols only after constraint reduction and on-shell diagonal Ward.
3. Separately solve/certify truly NONHOMOTHETIC on-shell g/f Einstein+HR+two-dust background, NOT the passive compensated homogeneous background.
4. Test De Felice finite-H mu→0 and homothetic nonlinear Aoki KS,cS² stable/unstable on the SAME physical reduced action, THEN fold1 at a≈0.0301646 if both pass. Report precise negative gate if obstructed.

**Verdict:** `STEP32D_INTEGRABLE_METRIC_FIELDS_GREEN`; `TWO_DUST_PAIRS_GREEN`; `DUST_PHASE_TIME_INTEGRABILITY_RED`; `TRUE_ADM_BD_REDUCTION_OPEN`; `GENUINE_NONHOMOTHETIC_ONSHELL_OPEN`; **`GATE_2B_OPEN` / JANUS-R NOT VALIDATED.** Branch ONLY `research/gate2b-nonhomothetic-transfer`, main and v2-flrw untouched. External JHR opposite-f-EH-sign audit separate.

---

# JANUS — REPRISE PRIORITAIRE, ÉTAPE 32c (2026-10-19)

**FIRST READ:** `research/RESTRICTED_FOUR_AUXILIARY_SCHUR_STEP32C_AUDIT.md`.
**New code/tests:** `numerics/hr_metric_auxiliary_restricted.py`, `tests/test_hr_metric_auxiliary_restricted.py`.
**Run ONE focused combined verification:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step32c.py gate2b-step32c-report.json`.

## 32c. Restricted 4-lapse/shift Galerkin Schur GREEN — TRUE PHYSICAL METRIC + BD CONSTRAINTS OPEN

Starting from the EXACT same positive EH_g, positive EH_f, all-beta HR and TWO reduced canonical dust common-time spherical action on the **radiation-free HOMOGENEOUS on-shell Candidate-C** branch, Step32c differentiates ALL 18 Step32b compact amplitude/rate jets to construct one symmetric full 18×18 PRECONSTRAINT Hessian. Four restricted metric coordinate amplitudes `(Phi_g,U_g,Phi_f,U_f)` at indices `(0,1,7,8)` define the 4×4 matrix `A`. It has rank 4, condition `545.9152166038742`, eigenvalues `(-2.80991e-4,-9.52783e-7,+5.14715e-7,+5.18734e-5)` on the tested off-shell*trial* directions (*the background itself is homogeneous on shell*). Its **ALGEBRAIC FINITE-BASIS** stationarization is `x_aux=-A^{-1}B y` and `S_14=C-B^T A^{-1}B`. Numeric and independent inverse constructions agree, multiple direct substitutions give `Q18=Q14` to ~1e-17, and the 4 restricted trial auxiliary equations vanish. A separate central difference of the ORIGINAL FULL NONLINEAR action along one Schur-compensated matter trial direction agrees with the predicted quadratic curvature to better than .7%; quadrature and Hessian step refinements pass. Two dust p-theta_rate canonical coefficients remain independently `+9.45033909345e-05`, `+1.30339269771e-05`, cross zero and rank 2. The original four independent EH metric rate block matches analytic Step32b coefficients to about 5e-15.

**CRITICAL NO-PHYSICS CLAIM:** This algebraic Schur is **NOT** the four true Hamiltonian ADM field constraints, is **NOT** a physical 14-mode kinetic/gradient matrix, and is **NOT** BD-null elimination. True ADM lapses/shifts are multiplier fields before arbitrary radial/time Galerkin truncation, and `Phi` is a component perturbation rather than the canonical lapse. Most decisively, Step32b's independent metric rate jets `b T(t)F(r)` are NOT the derivative `a T'(t)F(r)` of their compact parent spatial fields; at t=0, T'=0 but T=1. Consequently this 18-jet trial space is NOT closed under physical time derivatives or diagonal diffeomorphism generators. No ghost, scalar speed or fold conclusion can be drawn from the restricted Schur signs/rank.

**ACTUALLY EXECUTED:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests` → **71 PASSED in ONE focused local workspace** `/mnt/data/janus32`: 29 Step31 + 20 Step32a + 11 Step32b + **11 new Step32c**. The Step32c runner independently reports exit code 0, 71 passed, restricted aux rank 4, cond ~545.9152, 2 dust symplectic rank 2, `full_repository_regression=false`, `true_canonical_ADM_constraints_reduced=false`, `time_dependent_BD_null_reduced=false`, DeFelice/Aoki NOT_RUN, Gate2B OPEN. All FOUR newly published source/test/runner/audit files match local Git blobs EXACTLY:
- `numerics/hr_metric_auxiliary_restricted.py` `de568fa5b64f0195eaad5d60acbaf13996c912f6`
- `tests/test_hr_metric_auxiliary_restricted.py` `e3424451efe8ee4628ba0f6554bc3ca419bd3f83`
- `scripts/verify_gate2b_step32c.py` `6c91b81c42f32616c97f15b13b016f414ea09fc5`
- `research/RESTRICTED_FOUR_AUXILIARY_SCHUR_STEP32C_AUDIT.md` `670df71ee09ec47010c39cfeca13fa91dca9b656`

**NOT a full clean Git checkout / full repo CI / independent replication.** Historical Step27–30 tests NOT rerun in this environment. A first invocation of the full Step32c JSON runner was interrupted by environment timeout; a SECOND completed run gave 71/71 PASS and wrote `/mnt/data/janus32/gate2b-step32c-report.json`. Never claim first invocation completed.

**NEXT HARD RED, exact order:**
1. Replace independent nonintegrable metric rate jets with compact time-supported `psi(t,r),E(t,r)` and their ACTUAL derivatives, preserving native EH 3-curvature, correct integration by parts and diagonal on-shell Ward checks. Rerun the Step31/32 tests and both dust canonical pair controls.
2. Derive TRUE field-theory ADM lapse/shift auxiliary constraints and the HR time-dependent BD-null canonical reduction WITHOUT eliminating either dust phase pair; no finite restricted Schur substitution.
3. Independently solve/assess a genuinely NONHOMOTHETIC physical g/f Einstein+HR+two-dust background. Step30 compensated chart is merely a diffeomorphic homogeneous solution.
4. On the SAME full constrained action pass finite-H `mu→0` De Felice scalar and nonlinear homothetic Aoki `K_S,c_S²` stable+unstable, THEN test first Candidate-C relative `mu` fold a≈0.0301646. Reject model if real physical gate fails; no predicted observational likelihood yet.

**Verdict:** `RESTRICTED_SCHUR_ALGEBRA_GREEN`; `PHYSICAL_ADM_AND_BD_REDUCTION_OPEN`; `NONHOMOTHETIC_ONSHELL_OPEN`; **`GATE_2B_OPEN`; JANUS-R NOT VALIDATED.** Work ONLY on `research/gate2b-nonhomothetic-transfer`, leave main/v2-flrw untouched; external JHR negative f-EH-sign tensor ghost critique remains separate.

---

# JANUS — REPRISE PRIORITAIRE ÉTAPE 32b (2026-10-19)

**READ FIRST:** `research/FOUR_METRIC_RATE_JETS_STEP32B_AUDIT.md` (full derivation, RED->GREEN regression, independent controls, exact next gates). Read `research/COMMON_TIME_TWO_DUST_CANONICAL_STEP32_AUDIT.md` for exact two-dust Legendre bridge.

**Executable files:**
- `numerics/hr_full_onshell_tadpole.py` — original exact Step31 on-shell HOMOGENEOUS positive EH+HR+2 covariant dust action.
- `numerics/hr_two_dust_common_time_canonical.py` — Step32a common-time 2-dust Legendre first-order canonical action, 14 amplitude compact jet.
- `numerics/hr_common_time_metric_rates.py` — **NEW Step32b exact independent 4 metric trace/shear time-rate jets** added to same five-sector common-time 2-dust canonical action (18 amplitude compact interface).
- `tests/test_hr_full_onshell_tadpole.py`, `tests/test_hr_two_dust_common_time_canonical.py`, `tests/test_hr_common_time_metric_rates.py`.
- `scripts/verify_gate2b_step32b.py`.

**One-command rerun:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step32b.py gate2b-step32b-report.json`.

## 32b. Common-time 2-dust exact canonical pairs + four independent EH scalar metric rates — PRECONSTRAINT GREEN

Step32a derived from the same positive EH_g/f + all-beta HR + two dust common-time on-shell HOMOGENEOUS action an exact dust phase-space Legendre transformation, with rho multiplier eliminated ONLY after partial Legendre. It preserved both independent (theta_g,p_g),(theta_f,p_f) pairs, exhibiting a rank TWO compact symplectic p--theta_rate block (diagonals +9.450339095e-05,+1.303392697e-05, cross zero) and all 12 legitimate compact field tadpoles |grad|<3.73e-12. Its 14×14 Hessian is UNREDUCED, and phase_rate local jets have nonzero first derivatives because they are not independent compact theta field variations.

**NEW Step32b:** add **FOUR independent local spatial scalar EH metric time-rate jets** `psi_rate_g,E_rate_g,psi_rate_f,E_rate_f`, extending the SAME first-order canonical action to 18 amplitude slots. Reuse EXACT Step31 spherical ADM metric/positive EH g/f, same all-beta HR, same two phase-space dust actions and compact time/radial integration. At fixed metric spatial fields, ADM lapse and shift, rate perturbations change extrinsic eigenvalues by `δK_r=δQ_rdot/(2Qr N)`, `δK_t=δQ_tdot/(2Qt N)`. The exact nonlinear EH change is `(M²/2)N sqrt(gamma)[-4(Kr δKt+δKr Kt+δKr δKt)-4 Kt δKt-2 δKt²]`. Independently recomputed finite-amplitude nonlinear ADM kinetic density agrees exactly with this correction.

**Unreduced 4×4 metric-rate Hessian on homogeneous Candidate-C benchmark:** isotropic trace/shear closed-form controls, diagonal approximately `(-4.03436606e-05,+3.04798291e-09,-1.78523029e-07,+1.34875005e-11)`, cross metric/trace-shear entries zero, absolute finite-difference vs analytic error max **9.382496509350257e-16** at step .03. Both trace diagonals are negative and both shear diagonals positive as expected for UNREDUCED ADM gravity; these are NOT physical ghost signs or physical kinetic eigenvalues. Prior two-dust symplectic block remains independent rank 2. Exciting any single new rate changes ONLY its own EH sector, not HR or dust. With all 4 rate jets zero the complete old 14-amplitude action is recovered EXACTLY.

**Actual local evidence:** **60 tests passed IN ONE focused workspace** `/mnt/data/janus32` = 29 exact-byte Step31 tests + 20 Step32a tests + 11 Step32b tests. Both direct pytest and `scripts/verify_gate2b_step32b.py` report exit 0/60 passing, analytic rate deviation <1e-15, both matter canonical pairs preserved. All SIX newly created step32a/32b source/test/runner files and both audits have GitHub blob SHA exactly matching locally executed bytes (Step32b hashes in audit). Previous Steps27–30 separate test suites NOT rerun; this is NOT full Git checkout/CI or independent validation. Git clone blocked in prior contexts.

**CRITICAL scientific limitation:** the four extra metric time-rate directions (and both extra dust phase-rate jets) are **local jet probes**, NOT independently admissible globally compact field variations. Their raw first derivatives can be nonzero even on an on-shell background and are NOT tadpoles. The 18-amplitude compact action does **NOT** solve true ADM metric lapse/radial shift constraints, DOES NOT identify the time-dependent HR Boulware–Deser null direction, and DOES NOT supply the fully constrained physical scalar kinetic/gradient operators. The background is ON SHELL only for the radiation-free HOMOGENEOUS dust Candidate-C, NOT a truly nonhomothetic physical solution; Step30 passive compensation is pure coordinates.

**EXACT NEXT RED (DO NOT SKIP):**
1. Join metric field/velocity jets with valid time-supported profile integrability and time IBP; impose 4 ADM g/f lapse and radial shift auxiliary equations and diagonal Ward (on-shell) in SAME 5-sector action.
2. Compute and canonicalize the time-dependent HR BD-null constraint, retaining BOTH positive canonical dust phase/momentum pairs; derive actual *constrained physical* scalar principal matrices.
3. Independently seek/certify a genuinely NONHOMOTHETIC on-shell Candidate-C Einstein+HR+two-dust background, beyond passive f chart. Full g/f Einstein, Stückelberg/HR, both matter Euler tadpoles required.
4. Require same-action physical controls finite-H μ→0 De Felice and nonlinear homothetic Aoki K_S,c_S² (stable and unstable), THEN first Candidate-C relative μ fold a≈0.0301646, then optional observations. If not possible, publish precise negative verdict.

**VERDICT:** `STEP32B_METRIC_RATE_PRECONSTRAINT_GREEN`; `TWO_DUST_CANONICAL_GREEN`; `METRIC_AND_BD_CONSTRAINT_REDUCTION_OPEN`; `GENUINE_NONHOMOTHETIC_ONSHELL_OPEN`; **`GATE_2B=OPEN`; JANUS-R NOT VALIDATED.** Active branch ONLY `research/gate2b-nonhomothetic-transfer`, main/v2-flrw unchanged. External opposite-f-EH-sign JHR ghost objection remains a separate audit.

---

# JANUS — REPRISE PRIORITAIRE : ÉTAPE 32 (2026-10-19)

**READ FIRST:** `research/COMMON_TIME_TWO_DUST_CANONICAL_STEP32_AUDIT.md`.
**New module:** `numerics/hr_two_dust_common_time_canonical.py`.
**New tests:** `tests/test_hr_two_dust_common_time_canonical.py`.
**Reproduce in one command:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step32.py gate2b-step32-report.json`.

## 32. Exact two-dust COMMON-TIME phase-space Legendre bridge GREEN — full metric-velocity, BD and physical oracles STILL OPEN

**Advance over Step31:** The previous complete positive EH_g + positive EH_f + all-beta HR + TWO *covariant* irrotational dust spherical scalar action was tested at 12 compact first variations on the **radiation-free, HOMOGENEOUS on-shell Candidate-C** trajectory. Step32 now performs an **EXACT local ADM Legendre transform** of BOTH dusts on the SAME Step31 nonlinearly perturbed spherical metric tensors, BEFORE eliminating the dust density multiplier. This preserves the two dust momenta and two dust phase variables in a single common-time, five-sector **first-order canonical** spacetime action. It additionally evaluates the full **14×14 compact preconstraint Hessian** and compares its two phase-velocity/momentum columns with a separate analytic 4π radial/time integral.

For each metric, `N=sqrt(-g_tt+g_tr²/g_rr)`, `N^r=g_tr/g_rr`, `sqrt(gamma)=sqrt(g_rr)*g_angular`. The original dust scalar density is `sqrtgamma*rho/(2N)*[(theta_dot-N^r theta_r)^2-N²(1+theta_r²/g_rr)]`. Exact Legendre gives `p=sqrtgamma*rho*(theta_dot-N^r theta_r)/N`, `H_rho=N[p²/(2sqrtgamma*rho)+sqrtgamma*rho(1+theta_r²/g_rr)/2]+N^r p theta_r`. ONLY AFTER THIS, stationary multiplier `rho*=p/[sqrtgamma sqrt(1+theta_r²/g_rr)]` yields **`L_dust,red=p theta_dot-N p sqrt(1+theta_r²/g_rr)-N^r p theta_r`**. Exact equality of off-shell covariant and Legendre dust densities is tested in BOTH sectors for nonzero perturbations, not by the trivial zero-on-clock value.

**Important auxiliary fact:** at fixed spatial fields and p, the dust Hamiltonian is affine in true ADM lapse and shift. This DOES NOT solve full coupled EH+HR constraint algebra or BD null reduction. In the 14-amplitude trial jet the seven slots per sector are `(Phi,U,psi,E,theta,p,theta_rate)`, and the two independent *local* phase-rate jets are NOT independently admissible compact theta field variations. Their linear derivatives are NONZERO and are correctly excluded from the on-shell field-tadpole test.

**Reproducible diagnostics:** full preconstraint Hessian H has `H[p_g,theta_rate_g]=+9.450339095258206e-05`, `H[p_f,theta_rate_f]=+1.3033926965066306e-05`, cross-pair zero, 2×2 symplectic block rank 2. The two independent phase-rate rows are zero elsewhere; momentum-momentum and rate-rate dust blocks vanish in this stationary-rho reduced canonical representation. Twelve valid compact metric/phase/momentum field first variations remain zero to max `3.729655473350135e-12`; HR cross-metric coefficient `H[Phi_g,psi_f]≈-0.0001842360821` remains nonzero (and is zero with m²=0, while the background lapse tadpoles then fail).

**ACTUAL TEST:** **49 PASS in ONE local focused workspace /mnt/data/janus32** = 29 original exact Step31 tests (the Step31 original module and test have exact GitHub blob hash matching local bytes) + **20 NEW Step32 tests**. Both the direct pytest suite and independent `scripts/verify_gate2b_step32.py` runner returned exit code 0 / 49 passed, manifest marks incomplete full-repo checkout, BD/De Felice/Aoki `NOT_RUN`, `GATE_2B=OPEN`. This is a real combined 29+20 test result, UNLIKE prior separate step test counts. All FOUR new files exactly match tested local Git blobs:
- numerics/hr_two_dust_common_time_canonical.py `6b6c8a8e8f5373005ff51cf169b0360fc9caec37`
- tests/test_hr_two_dust_common_time_canonical.py `020c87f1b3a805f23c66cf20516ba82fb7f1796d`
- scripts/verify_gate2b_step32.py `c2887ec07ac6aec1ca3a27716dbcb038713b4c76`
- research/COMMON_TIME_TWO_DUST_CANONICAL_STEP32_AUDIT.md `dd3a8ebddde6716b2817de69ec26cdf991e31467`

**CURRENT EXACT RED:** (1) extend the Step31 EH+HR+two dust action to retain INDEPENDENT metric spatial trace and shear TIME-RATE jets `psi_dot_g,E_dot_g,psi_dot_f,E_dot_f`; then form a coherent common-time quadratic field/rate operator and ADM lapse/shift auxiliary constraints. Do not read physical kinetic/ghost signs from the current UNREDUCED 14×14 Hessian. (2) Canonically eliminate the time-dependent HR BD-null direction while preserving BOTH independent dust (theta,p) symplectic pairs. (3) Independently solve a genuinely NONHOMOTHETIC on-shell Candidate-C two-dust background beyond the passive compensated chart; full 5-sector Einstein and matter tadpoles required. (4) Reproduce De Felice finite-H μ→0 scalar and nonlinear homothetic Aoki K_S,c_S² (stable+unstable) on the SAME reduced action before first relative μ-fold `a≈0.0301646` or any CMB prediction.

**Verdict:** `COMMON_TIME_TWO_DUST_CANONICAL_GREEN`, `METRIC_BD_REDUCTION_OPEN`, `GENUINE_NONHOMOTHETIC_ON_SHELL_OPEN`, `GATE_2B=OPEN`; JANUS-R NOT VALIDATED. Work ONLY on `research/gate2b-nonhomothetic-transfer`, leave main/v2-flrw untouched; external 2026 JHR negative-f-EH-sign audit separate.

---

# JANUS — POINT DE REPRISE PRIORITAIRE, ÉTAPE 31 (2026-10-19)

**FIRST READ:** `research/FULL_ONSHELL_TWELVE_FIELD_TADPOLES_STEP31_AUDIT.md`.
**NEW SOURCE:** `numerics/hr_full_onshell_tadpole.py`.
**NEW TESTS:** `tests/test_hr_full_onshell_tadpole.py`.
**ONE COMMAND:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step31.py gate2b-step31-report.json`.

## 31. ONE full nonlinear common-chart spherical scalar + TWO dust action on HOMOGENEOUS ON-SHELL Candidate C — 12 first variations GREEN; physical nonhomothetic Gate2B OPEN

After Step30 exact passive-chart compensation, a NEW standalone code now computes **ONE spacetime-integrated** action with five contributions (EH_g positive, EH_f positive, all-beta Hassan–Rosen, covariant dust_g, covariant dust_f) over the SAME metric/field basis, at the **actual on-shell radiation-free homogeneous dust-only Candidate-C** trajectory obtained by integrating a_dot=aH. Earlier step27's five-sector common action was OFF SHELL and step30 checked only the g lapse tadpole; this step checks TWELVE directions of independent fields on the homogeneous on-shell branch.

**All 12 independent compact time+radius first variations vanish** for `(Phi_g,U_g,psi_g,E_g,theta_g,rho_g,Phi_f,U_f,psi_f,E_f,theta_f,rho_f)`. This time includes *all spatial 3-curvature, ADM extrinsic rates, native metric trace/shear and both covariant dust phase/multiplier terms*. At time halfwidth .027, radial support .32 and quadrature 24, centered amplitude step 2e-5, max abs first variation is `1.4051260155412136e-11`; tested quadrature/step/domain refinements. Contributions are genuinely individually nonzero and cancel: dS/dPhi_g approx EH_g +3.64871135e-4, HR -6.44695537e-5, dust_g -3.00401582e-4; dS/dPhi_f approx EH_f +1.29610824e-6, HR +2.01858490e-5, dust_f -2.14819573e-5. Both matter phase and density directions cancel only after the original covariant dust action has been varied (NO prematurely imposing theta_dot=N in L).

**Independent physical trial deformation beyond Step30 pure-chart map:** varying only f spatial trace psi_f changes its physical common-chart 3-curvature and relative angular eigenvalue while keeping g fixed, and yields a NONZERO quadratic action. Mixed relative Hessian H[Phi_g,psi_f] ≈ -0.0001842360131; removing the HR interaction makes this cross-metric block vanish and immediately breaks both g/f background lapse tadpoles. Other controls independently check beta4 is f-volume-only, both native local dust Legendre phase pairs, exact tilted native f tensor pullback even with nonzero independent f perturbation. **These are UNREDUCED trial-field Hessian coefficients, NOT physical scalar speeds, canonical kinetic eigenvalues or physical ghost criteria.**

**Actually executed NEW standalone:** `PYTHONPATH=/mnt/data/janus31 OPENBLAS_NUM_THREADS=1 python -m pytest -q /mnt/data/janus31/tests/test_hr_full_onshell_tadpole.py` → **29 passed**. `scripts/verify_gate2b_step31.py` reproduced 29/29 with exit 0, `workspace_origin=standalone_focused_workspace`, `full_repo_test_suite=false`, `historical_test_suites_rerun=false`, De Felice/Aoki NOT_RUN, BD reduction NO, `GATE_2B_OPEN`. FOUR newly committed files are **exact-byte SHA identical** to local tested ones:
- numerics/hr_full_onshell_tadpole.py `e05d8f54cf4eff76a92c278ffdd971612d1ec56b`
- tests/test_hr_full_onshell_tadpole.py `68fb2302ae57c350db087ea3caf5898ca31661af`
- scripts/verify_gate2b_step31.py `6ae34372ccc5a034fc5ef6bf27339ebca9a446bf`
- research/FULL_ONSHELL_TWELVE_FIELD_TADPOLES_STEP31_AUDIT.md `b8abf50a91cdf6a75e2a4a19e6b6d2ec404b9119`

Historical steps 30 (18), 29 (21), 28 (17), 27 (75) were in SEPARATE workspaces and **NOT rerun here**: do not claim cumulative passing counts. Git clone still DNS blocked; GitHub Actions disabled. No fresh full repository verification.

**CRITICAL LIMITATION:** the homogeneous on-shell background in common chart is merely the *same physical* compensated configuration identified in Step30. An independent finite-amplitude f field variation is a valid mathematical test direction, NOT a newly solved genuinely NONHOMOTHETIC background. No full time-dependent canonical/metric/BD constraint elimination, no De Felice/Aoki independent physical oracles, no relative-mu fold crossing or cosmological likelihood yet.

**NEXT EXACT RED:** from this *single* full spherical EH_g+EH_f+HR+two-dust action derive a consistent common-time quadratic **field and rate** operator, identify all lapse/shift metric auxiliary directions and exact diagonal Noether constraints ON SHELL, and canonically reduce both dust phase/momentum pairs and the time-dependent BD-null direction. In parallel, solve full radial/time Einstein+HR+matter first variations for a **genuinely nonhomothetic** background beyond Step30 pure-chart compensation; test its tadpoles. Only from the SAME full reduced physical action attempt De Felice finite-H mu→0 and Aoki nonlinear homothetic KS,cS² stable/unstable, then first Candidate-C relative μ-fold a≈0.0301646. If impossible, publish specific failed gate; no fabricated validation.

**Verdict:** `COMMON_HOMOGENEOUS_ONSHELL_12_FIELD_ACTION_GREEN`, `GENUINE_NONHOMOTHETIC_BACKGROUND_OPEN`, `GATE_2B_OPEN`, `JANUS_R_NOT_VALIDATED`. Work ONLY in research/gate2b-nonhomothetic-transfer; leave main and research/v2-flrw untouched; external 2026 JHR opposite-f-EH-sign ghost audit separate.

---

# JANUS — POINT DE REPRISE PRIORITAIRE, ÉTAPE 30 (2026-10-18)

**READ FIRST:** `research/INVERSE_CHART_COMPENSATION_STEP30_AUDIT.md`.
**Code/tests:** `numerics/hr_compensated_native_chart.py`, `tests/test_hr_compensated_native_chart.py`.
**Reproduce:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step30.py gate2b-step30-report.json`.

## 30. EXACT native f metric+dust inverse-chart compensation established — PURE GAUGE BASELINE, NOT NEW PHYSICAL SOLUTION

Step29 proved that naïvely inserting the homogeneous on-shell Candidate-C two-dust solution into `T=t+sigma(t)r²/2, R=lambda(t)r` fails the visible g lapse equation unless the native f geometry is adjusted. Simply setting `b_native=b_hom/lambda` repairs only the central scale ratio and fails at finite radius for tilted/evolving charts.

**NEW exact inverse-chart construction:** start from the real *on-shell radiation-free homogeneous two-dust Candidate-C* metric `f_common=diag(-Nf(t)²,b(t)²)`, angular `b(t)²r²`, physical comoving f dust `theta_fdot=Nf, rho_f=Cf/b³`. On a regular nonhomothetic background chart `X=(T,R)`, `J=dX/d(t,r)`, obtain

```
f_native=J^{-T} f_common J^{-1}
f_native_ang=b(t)² r²
(theta_native,T,theta_native,R)=(Nf,0) J^{-1}
rho_native=Cf/b(t(T,R))³
native dust current density^A=Cf r² J^A_t / det(J).
```

**Critical physical restriction:** the fully transported f-native metric generically has nonzero `f_TR`, radial/angular non-FLRW components, radial-dependent dust clock and a NONZERO native radial dust flux. This is a PURE passive reparametrization of the SAME homogeneous physical f metric, NOT a new nonlinear nonhomothetic physical solution. It cannot produce the independent helicity-0 canonical matching data or demonstrate crossing the mu fold at a≈0.0301646. Imposing the old f-native diagonal/FLRW ansatz after the coordinate change is NOT an equivalent metric.

**Numerical witness:** at a=.4, t=0, r=.2, lambda=.78, sigma=.08, lambda_dot=.04, sigma_dot=.025, the exact transported native f off-diagonal component is +0.00480694489921799. All 2×2 common f metric components and angular area are recovered to ~1e-16 via `J^T f_native J`. The native dust normalization is -1 and its density current divergence is ~5.4e-12 (finite differences). The exact HR potential matches the homogeneous all-beta expression at multiple t/r, and a NONZERO off-shell native dust Lagrangian agrees with its common counterpart only after multiplying by the full Jacobian determinant.

**Physical necessary g lapse test, also integrated across COMPACT TIME+RADIUS:** on this compensated, homogeneous-on-shell baseline the direct visible lapse residual at r=.2 is ~2.66e-10 and compact time/radial first action variation is +1.30104260698e-13 (finite-difference cancellation). The deliberately truncated scale-only diagonal native ansatz gives +0.0003116455094 and +3.50278833716e-8 respectively. The tested compact action includes g positive EH ADM+GHY, canonical g dust charge and exact all-beta HR with fully transported f geometry. This is ONE necessary Euler direction, NOT full coupled five-sector tadpoles.

**ACTUALLY EXECUTED in NEW standalone `/mnt/data/janus30`: 18/18 targeted tests PASS.** Runner JSON exit 0 / 18 passed, `workspace_origin=standalone_focused_workspace`, `full_repository_regression=false`, `previous_step29_tests_rerun=false`, `DeFelice/Aoki NOT_RUN`, `GATE_2B OPEN`. All FOUR new source/test/runner/audit GitHub files have been byte-verified against the actual local git hash:
- numerics/hr_compensated_native_chart.py = `14bf842c9bcfe792a1891c7a8d758c76f37f30c9`
- tests/test_hr_compensated_native_chart.py = `b81966e9395a8fc7728773fd4b0745e704a9c13f`
- scripts/verify_gate2b_step30.py = `1036166d4bfe57ad9bf6e6c67ca157d5267c1c5b`
- research/INVERSE_CHART_COMPENSATION_STEP30_AUDIT.md = `e897229ea831f162252db2845c630b2dd4a42b47`

Previous Step29 21, Step28 17 and Step27 75 tests were run in OTHER workspaces and **not rerun together**; NEVER claim 131 tests passed in one run. Full clean repo clone still DNS-blocked and GitHub Actions disabled.

**NEXT EXACT RED:** starting FROM THIS EXACT compensated on-shell baseline, introduce a *physically independent* f native metric/Stückelberg relative deformation (e.g. independent shift, trace/shear, time/radial profiles AND both matter phases), not merely `J^{-T}f J^{-1}`. Calculate ALL g/f Einstein, HR relative chart, and both dust Euler/tadpoles on one shared time/radial action. Demand their cancellation for a genuinely nonhomothetic on-shell branch; only then derive physical constrained scalar action, reduce four metric auxiliaries and time-dependent BD-null with two canonical dust pairs, and pass the independently required SAME-ACTION De Felice finite-H mu→0 and Aoki nonlinear homothetic `K_S,c_S²` physical controls before testing the first relative-mu fold and any observational transfer.

**Verdict:** `COORDINATE_COMPENSATION_BASELINE_GREEN`; `GENUINE_NONHOMOTHETIC_ONSHELL_BRANCH_OPEN`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`. Work ONLY on research/gate2b-nonhomothetic-transfer. main and research/v2-flrw untouched. Keep external opposite-EH-sign JHR tensor critique separate.

---

# JANUS — REPRISE PRIORITAIRE : ÉTAPE 29 (2026-10-18)

**FIRST READ:** `research/NONHOMOTHETIC_ONSHELL_INSERTION_STEP29_AUDIT.md`.
**Reproduce immediately:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step29.py gate2b-step29-report.json`.
**New verified code/tests:** `numerics/hr_nonhomothetic_center_obstruction.py`, `tests/test_hr_nonhomothetic_center_obstruction.py`.

## 29. Naïve on-shell Candidate-C -> finite-μ nonhomothetic insertion: EXPLICIT RED (LATEST)

**Actual scientific result: a falsified SUBSTITUTION, NOT a general no-go for JANUS.** Step28 proved the TWO-DUST, NO-RADIATION homogeneous Candidate-C background solves its homogeneous positive-EH+HR+two-dust Routhian. Step27's common full 5-sector spacetime action still uses arbitrary OFF-SHELL g/f polynomials. Step29 checks the proposed direct substitution of Step28 into the nonhomothetic f chart `T=t+σ(t)r²/2`, `R_f=λ(t)r`, `λ=1+μ>0`, leaving the previously on-shell native f scale `b(T)` unchanged. At the center the square-root spatial eigenvalues are `λ b/a`, NOT `b/a`, so the g lapse potential is `V_g(λy)` rather than `V_g(y)`. Hence the exact necessary center lapse residual is

```
R_g(λ) = 3 Mg² a adot²/Ng² - Cg - m² Mg² a³ V_g(λ y),
R_g(1)=0  on homogeneous Candidate-C dust-only branch,
R_g(λ)-R_g(1)=-m² Mg² a³ [V_g(λy)-V_g(y)],
V_g(z)=β0+3β1 z+3β2 z²+β3 z³,
d R_g/dλ |_{λ=1}=-3m² Mg² a³ y J_g(y).
```

**Quantitative decisive benchmark:** at `a=.4`, `y=.578770722803`, `Ng=1`, `Nf=.518526433828`, `λ=.78` (μ=-.22), previously on-shell `R_g(1)≈0` becomes **`R_g(.78)=+0.160780603695`** in the normalized action. The analytically independent exact 2x2 principal-root spherical Hassan–Rosen density, directly finite-differentiated with respect to the g lapse at radius 10^-4, recovers the same residual. The independently compact-radial g-EH+canonical-dust+HR first action variation for support radius .035 is **+3.20003248e-6**, matching the exact bump integral. No need to interpret raw off-shell Hessian eigenvalues. At a=.03 and λ=.231117 (relative μ fold location used only as reference), the same naïve source is +.03919434, NOT proof of physical fold failure.

**Critical NON-NO-GO counterexample:** setting `b_native=b_homogeneous/λ` for CONSTANT λ restores `λb_native/a=y` and cancels this CENTER g lapse obstruction. But at finite r, `σ≠0` introduces common-slice component anisotropy `f_rr-f_theta_theta/r²=-n(T)²σ²r²` and the direct g lapse source remains nonzero in the chosen off-shell f time/scale jets even after center compensation; q.g. at a=.4, λ=.78, r=.2, σ=.08 yields roughly -0.0017545. This is a slicing component identity, NOT invariant physical anisotropic stress and NOT a theorem that the fully corrected nonhomothetic system has no solution. Native f matter phase/charge and all metric radial/time derivatives must be re-solved.

**Actually executed new test evidence:** 21/21 PASS, `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_nonhomothetic_center_obstruction.py` in isolated `/mnt/data/janus29`. Includes independent recomputation of radiation-free Candidate-C quartic roots and f lapse `Nf=y+y_N` for FOUR epochs; independent direct spherical HR matrix-square-root differentiation at FIVE parameter points, compact g lapse action variation, analytic J slope, radius/step convergence, β4 decoupling, m²=0, compensated central scaling and residual finite radius. `scripts/verify_gate2b_step29.py` generates exact SHA-256 source manifests, diagnostic witness, `workspace_origin=standalone_focused_workspace`, `full_repository_regression=false`, `DeFelice/Aoki NOT_RUN`, `GATE_2B=OPEN`. All FOUR new source/test/script/audit Git blobs have been matched BYTE FOR BYTE against locally executed files. Prior Step27 75 tests and Step28 17 tests belong to OTHER workspaces and were NOT rerun together; do NOT claim 113 combined tests. Direct Git clone DNS fails; no CI/independent replication claimed.

**NEXT EXACT RED:** construct a chart-**COMPENSATED** f-native background `b_native(T)` and both dust phase/charge transformations consistent with the nonhomothetic common geometry and native dust conservation. Then evaluate ALL g and f lapse, radial/time/scale, scalar and Stückelberg Euler residuals from the SAME Step27 five-sector action on one common compact spacetime support, not only the center. Reject trial backgrounds with nonzero tadpoles. Only if a genuine full on-shell nonhomothetic solution is found, derive time-dependent EH+HR+two-dust physical scalar quadratic action, reduce metric auxiliaries/time-dependent BD-null with BOTH matter canonical pairs, pass BOTH De Felice finite-H μ→0 and Aoki homothetic K_S,c_S² oracles, THEN assess the first relative μ fold at a≈0.0301646. No ghost/gradient/fold/CMB viability conclusion yet.

**Verdict:** `NAIVE_HOMOGENEOUS_INSERTION_FAIL`; `CORRECTED_FULL_NONHOMOTHETIC_BACKGROUND_OPEN`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`. Preserve exact branch `research/gate2b-nonhomothetic-transfer`; do not touch main or research/v2-flrw; keep external JHR negative-f-EH ghost critique separate.

---

# JANUS — POINT DE REPRISE PRIORITAIRE, ÉTAPE 28 (2026-10-18)

**READ FIRST:** `research/MINISUPERSPACE_ONSHELL_STEP28_AUDIT.md`.

**Sources + 17 new tests:** `numerics/hr_minisuperspace_onshell.py`, `tests/test_hr_minisuperspace_onshell.py`.

**Repeatable step28 runner:** `python scripts/verify_gate2b_step28.py gate2b-step28-report.json`.

## 28. Candidate-C TWO-DUST homogeneous on-shell background and compact action tadpoles GREEN — full nonhomothetic Gate 2B OPEN

The previous Step27 has ONE full nonlinear **OFF-SHELL** spacetime integral for EH_g (+), EH_f (+), all-beta HR and two separately coupled irrotational dust sectors on shared native metric coordinates, but its polynomial backgrounds do NOT satisfy the two metric Friedmann equations. Step28 establishes an **independent exact on-shell HOMOGENEOUS** five-sector minisuperspace Routhian and validates its first variations:

```
L = -3 Mg² a a_dot²/Ng -3 Mf² b b_dot²/Nf
    -m² Mg² a³[Ng (β0+3β1 y+3β2 y²+β3 y³)
              +Nf (β1+3β2 y+3β3 y²+β4 y³)]
    -Ng Cg-Nf Cf,    y=b/a.
```

**Critical matter issue (NEW regression):** the homogeneous covariant dust Lagrangian evaluates to zero on its normalized clock, but its *partial lapse variation* does NOT vanish: ∂L_dust/∂N|theta_dot,rho = -C. Early on-shell substitution before variation would erase both dust Friedmann sources. The fixed-charge Routhian terms -Ng Cg -Nf Cf are derived by canonical Legendre/Routh reduction and preserve both independent matter phase momenta. All four scale/lapse Euler residuals are analytically derived from this ONE action and separately tested by numerical partial differences.

**Candidate C scope STRICT:** radiation is REMOVED intentionally (Ω_g,r0=0) to match existing `candidate_c_dust_background.py` stress test, NOT the complete radiation-era model. Re-solve present y0 after this removal: y0=0.5568825591873054; E(1)=0.9999551638376833, not exactly 1. On its regular dynamical homogeneous branch with Ng=1 and Nf=y+y_N, the two Friedmann constraints, two acceleration Euler equations, Bianchi relation and both conserved dust constants pass to max ~5.4e-13 over representative points a=1,.8,.4,.2,.09,.05,.03. Independent implicit polynomial derivatives supply y_N,y_NN; no tuned acceleration input.

**NEW real time-domain tadpole test:** solve da/dt=aE(a) in both time directions, sample on-shell a,b,Ng,Nf on Gauss–Legendre temporal points, independently perturb each with compact F(t)=(1-t²/T²)^4 and the correct derivative Fdot for scale factors. The first variation of the **integrated homogeneous Routhian** vanishes in all four directions. At time half-window .025, 26 quadrature points and finite amplitude 1e-6: (-1.8041e-10,+1.3878e-11,0,-6.9389e-12) in order (a,b,Ng,Nf). Refinement tests 18/26/32 and different time supports pass. A test with too-large initial variation steps 1e-5/2e-5 showed O(h²) truncation (1e-8/1e-7); reduced step to 1e-6, not edited physical equations.

**Negative controls:** increasing Nf by 2% at a=.4 causes f lapse residual -2.90764390585e-4 and Bianchi failure; increasing Cf by 1% induces exactly -0.01 Cf shift of f lapse constraint. Generic polynomial off-shell sample has nonzero lapse and scale Euler residuals. A smooth homogeneous y(a) on either side of the previously found local nonlinear **relative-μ** folds at a~.0301646/.0491246 is NOT a proof of Stückelberg fold crossing.

**ACTUAL testing now:** 17 new focused tests PASS (Python 3.13.5, standalone `/mnt/data/janus28`). Runner exit 0 / 17 passed / `standalone_focused_workspace` / `full_repository_regression=false` / `DeFelice/Aoki NOT_RUN` / `GATE_2B OPEN`. **Do not claim 75+17=92 executed together**: 75 prior tests belong to earlier separate reconstructed workspace; no clean full Git clone or CI run. FOUR new source/test/runner/audit files are EXACT byte-matched GitHub blobs (SHA in audit). Branch only `research/gate2b-nonhomothetic-transfer`; main/v2-flrw unchanged.

**NEXT EXACT RED — priority:** substitute the actual on-shell Candidate-C TWO-DUST background into the full Step27 **nonhomothetic common spacetime five-sector action**, including native chart T(t,r),R(t,r) and all lapse/scale derivative transport. Demand first variations/tadpoles of actual shared action vanish, without imposing dust clock constraints before varying. Then construct shared **time-dependent scalar quadratic action**, keep BOTH canonical dust phase pairs, eliminate metric auxiliaries and time-dependent BD-null constraint. From the SAME physical action reproduce finite-H μ→0 De Felice and homothetic nonlinear Aoki K_S,c_S² before attempting relative-μ fold 1 and later cosmological predictions.

**Verdict:** `CANDIDATE_C_DUST_ONLY_HOMOGENEOUS_ON_SHELL_GREEN`; `STEP27_NONHOMOTHETIC_ON_SHELL_STILL_RED`; `GATE_2B=OPEN`; `JANUS_R_NOT_VALIDATED`. External JHR negative f EH sign tensor-ghost objection remains separate.

---

# JANUS — REPRISE PRIORITAIRE, ETAPE 27 (2026-10-18)

**FIRST READ:** `research/UNIFIED_FIVE_SECTOR_SPACETIME_STEP27_AUDIT.md`.
**One-command reproducibility:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step27.py gate2b-step27-report.json`.

## 27. Real common nonlinear spacetime EH_g + EH_f + HR + 2 covariant dusts (LATEST)

**SIGNIFICANT new structural gate:** there is NOW ONE **off-shell common native-field-space** 2D spacetime integral with five real action densities: positive EH_g and EH_f ADM+GHY, all-beta HR, and two irrotational pressureless covariant dust actions. Same nonhomothetic T(t,r),R(t,r) chart and Jacobians, same exact g/f spherical metric perturbations for ALL terms, same radial/time integration, no double angular factor. Native dust backgrounds separately satisfy rho_g a^3=const, rho_f alpha^3=const, theta_gdot=N_g, theta_f,T=n_f; full coupled gravity background remains OFF SHELL.

The **five independently integrated sector actions** each remain invariant under simultaneous compact DIAGONAL coordinate changes. Under a relative f-native chart displacement EH_g, EH_f, dust_g and dust_f are individually invariant, while **only the HR interaction responds**. The new HR action matches the older independent exact Step26 HR spacetime action at multiple finite chart displacements with factor hr_mass2=0.7. Both native EH lapse/shift specializations reproduce the older independent exact flat spherical ADM density; all native metric components agree with the HR input. At 48-point quadrature baseline 5 pieces are approximately (-0.1013110024,-0.0509346122,-0.8289092689,-0.0044339941,+0.0023538524); total -0.9832350252 (arbitrary dimensionless control). For relative f shift (+.035,-.023), HR alone changes by -1.00718622362e-5; rest remain unchanged to numerical precision.

**Separate exact native dust canonical/Legendre control:** covariant irrotational action -rho sqrt(-g)(g^-1 dtheta dtheta+1)/2 yields p_theta=gamma rho(theta_T-N^R theta_R)/N, Hamiltonian H=N[p²/(2gamma rho)+gamma rho(1+theta_R²/gamma_RR)/2]+N^R p theta_R; on stationary rho it reduces to N p sqrt(1+theta_R²/gamma_RR)+N^R p theta_R. Both native matter momentum/velocity derivatives are positive and rank TWO. This preserves independent pairs in this **native local canonical identity**, NOT an already established common-time canonical reduction on a Candidate-C trajectory.

**ACTUALLY TESTED:** 18 new targeted tests (13 unified sectors, 5 native Legendre) + 57 prior = **75 tests passed**, `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests`. Step27 provenance runner returned exit_code 0/75 passed, workspace_origin **non_git_workspace_reconstruction**, full_repository_regression=false, DeFelice/Aoki NOT_RUN, GATE_2B=OPEN. The six new source/test/runner/audit files have been transferred from the ACTUAL local files and each GitHub blob SHA was compared exactly to local `git hash-object`. **Historical HR/dust prerequisites in this local environment are still algorithm-preserving but not all byte-exact GitHub checkout files.** No full repo/CI or independent review claimed.

**IMMEDIATE SCIENTIFIC RED:** (1) make the now-shared off-shell full action a truly **ON-SHELL Candidate-C** solution satisfying BOTH metric Friedmann equations, HR background and two independent dust conservation and cancel all tadpoles; (2) derive the coherent common-time *quadratic* field/rate Hessian and exact covariant→canonical dust phase pair equivalence, including f chart derivative sampling and compact time boundary terms; (3) eliminate four metric auxiliaries plus time-dependent BD-null variable without dropping either dust pair; (4) pass finite-H mu→0 De Felice and nonlinear homothetic Aoki K_S, c_S² on the SAME reduced physical action. Only THEN assess Candidate-C first fold a≈0.0301646. Never infer physical kinetic signs/ghost freedom from off-shell test Hessians. No JANUS cosmological validity claim.

**VERDICT: FIVE_SECTOR_OFFSHELL_ACTION_GREEN_AS_REGRESSION; GATE_2B=OPEN; JANUS_R_NOT_VALIDATED.** Work only on `research/gate2b-nonhomothetic-transfer`, NOT main/v2-flrw. Preserve separate external JHR tensor ghost criticism.

---

# JANUS — POINT DE REPRISE PRIORITAIRE: ETAPE 26 (2026-10-18)

**READ FIRST:** `research/COUPLED_DIAGONAL_NOETHER_STEP26_AUDIT.md`. The full nonlinear potential, its four-chart Hessian, and reproducible tests are:
- `numerics/hr_coupled_diagonal_ward.py`
- `numerics/hr_coupled_chart_hessian.py`
- `tests/test_hr_coupled_diagonal_ward.py`
- `tests/test_hr_coupled_chart_hessian.py`
- `scripts/verify_gate2b_step26.py`.

**Single command:** `OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step26.py gate2b-step26-report.json`.

## 26. All-five-beta full bimetric diagonal Ward GREEN — OFF-SHELL Hessian caution (LATEST)

**Novel coupled result:** on a genuinely time-dependent nonhomothetic f chart (T=t+sigma(t)r²/2, R_f=[1+mu(t)]r), the exact nonlinear HR potential for ALL five beta0..beta4 coefficients, with full g/f spherical 2x2 metric blocks + angular radii, is integrated over compact time and radial support. Four scalar lapse/shift/trace/shear perturbations per sector are sampled at correctly displaced coordinates. The finite **DIAGONAL** diffeomorphism acting on both metrics preserves the full interaction action to machine precision. A relative f-only native chart displacement gives NONZERO beta1,beta2,beta3 action variations, while beta0 and beta4 remain separately invariant (g volume/f volume controls). This is a true coupled-action Ward test, beyond the earlier f-only EH chart checks.

**Cross-oracle:** the new directly evaluated 2x2 principal-square-root HR density equals `r² * native_hr_stueckelberg_jet(...).value` from the prior independent exact native HR jet at t=0, r=.12,.23,.39. At r=.23 both are -0.0823859285303577. Fully independent g/f coordinate pullbacks agree in diagonal mode.

**Critical observed RED-to-GREEN:** an initial test equated an f-native displacement delta(T,R) to an f displacement delta(t,r) with the same amplitudes; that is WRONG when the background Jacobian is nontrivial. They obey deltaX_f^A=J0^A_mu delta x_f^mu to FIRST order and have different finite expressions. The corrected tests distinguish both charts. A separate positive-orientation check has replaced a placeholder diagnostic. All changed file bytes verified.

**Off-shell Noether/gauge caution:** finite diagonal coordinate paths preserve the action exactly, so their directional first and quadratic second derivatives vanish. But the independent 4x4 g/f chart Hessian H on the arbitrary off-shell background does **NOT** necessarily satisfy H v_diag=0, since the nonlinearly field-dependent Ward generator obeys S_,ij R^j = -S_,j partial_i R^j and the tadpoles S_,j are nonzero. Numerically `||H v_T||~3.0e-4`, `||H v_R||~1.73e-3`, even though direct finite diagonal action changes are ~0. The finite-difference directional `v^T H v` error decays as O(h²), verified. **NEVER infer BD or physical gauge-null eigenvectors from OFF-SHELL raw Hessian.**

**Actual local evidence:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests` => **57 passed** in `/mnt/data/janus-next`. 16 new tests and the 41 prior focused. `scripts/verify_gate2b_step26.py` returned exit 0/57 passed, provenance `non_git_workspace_reconstruction`, `full_repository_regression=false`, `DeFelice/Aoki=NOT_RUN`, `GATE_2B=OPEN`. All FIVE new source/test/runner files byte-identical to live GitHub blob SHA (see audit). Earlier HR/dust prerequisites are still algorithm-preserving local reconstructions, **NOT a clean Git clone** (DNS access blocked); no full repository suite or independent verification.

**IMMEDIATE NEXT RED:** assemble one shared **time-dependent EH_g+EH_f+HR+TWO dust phase** action using the SAME native/common profiles, chart Jacobians, angular density and time-supported boundary terms. Impose one ON-SHELL Candidate-C trajectory and both dust conservations, verify all first-order tadpoles vanish, THEN derive four true metric auxiliary constraints and time-dependent BD-null canonical reduction with both phase pairs preserved. Reproduce finite-H mu->0 De Felice physical scalar plus nonlinear homothetic Aoki K_S,c_S² from the SAME action, THEN test fold 1 a≈0.0301646. If failing, issue negative physical gate; do not invent observational viability.

**Scientific verdict: coupled all-beta diagonal Ward GREEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.** Work ONLY on branch `research/gate2b-nonhomothetic-transfer`; leave main and research/v2-flrw untouched. Separate external JHR opposite-sign EH ghost prepublication audit unchanged.

---

# JANUS — RESTART POINT / CURRENT HEAD: STEP 25 (2026-10-18)

**READ FIRST:** research/EH_CHART_QUADRATIC_STEP25_AUDIT.md.
**Reproduction:** python scripts/verify_gate2b_step25.py gate2b-step25-report.json.
**Code:** numerics/hr_eh_full_scalar_quadratic_chart.py, tests/test_hr_eh_full_scalar_quadratic_chart.py.

## 25. f-Einstein–Hilbert exact spacetime 6×6 chart Hessian: isolated gauge-null directions GREEN (LATEST)

New analytic/geometric result: differentiate the **exact nonlinear full native-scalar Einstein–Hilbert ADM+GHY action** on a compact time/radial common domain with respect to six independent amplitudes (deltaT,deltaR,Phi_f,U_f,psi_f,E_f). The chart variations are compact and vanish at outer boundaries. With all native metric field values AND native derivative jets sampled at their moved (T,R) positions, the resulting 6×6 Hessian has both chart rows/columns zero within ~8.7e-13 finite-difference residual while the native 4×4 metric block is substantial (Frobenius norm ~11.089). The metric block itself stays invariant under a finite compact chart deformation to ~4.63e-12.

Reason: first chart variation of D rho(X) is the total divergence div[rho Cof(J) xi] by the Piola identity; it vanishes on the fixed spacetime boundary. Thus the isolated f-EH sector has no independent chart kinetic terms in this native parametrization. This is a **boundary/Noether acceptance control**, NOT the BD constraint or complete coupled physical action. Freezing metric field sampling breaks the null block decisively (up to ~0.312 mixed residual). A separate HR beta1–beta3 compact radial Hessian retains NONZERO relative chart response (chart Hessian Frobenius norm ~0.22018; metric/chart cross ~0.51215), which turns off when m²=0. Its profile/integration differs: the numbers are NOT physical comparable magnitudes.

**Actual executed local focused tests:** PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests => **41 passed** (32 step24 controls + 9 new step25). The new step25 manifest runner independently reports 41 passed / exit_code 0 / origin non_git_workspace_reconstruction / full_repository_regression false / DeFelice and Aoki NOT_RUN / Gate2B OPEN. Three new source/test/runner blobs EXACTLY match live GitHub; historical HR/dust prerequisites remain local algorithmic reconstructions rather than a clean Git checkout. DO NOT claim full repo or external reproduction.

**CURRENT EXACT RED:** one shared time-dependent, on-shell full EH+HR+TWO-dust action with consistent native/common f metric derivative transport and compact boundary treatment. Demand both background dust conservations and all tadpoles zero; derive true metric auxiliary constraints then time-dependent BD-null reduction preserving both dust canonical momenta. From that SAME constrained action pass (a) finite-H mu->0 De Felice scalar and (b) nonlinear homothetic Aoki K_S, c_S² oracles. Only then test Candidate-C fold 1 a≈0.0301646. Do NOT diagonalize off-shell 6×6, 24×24 or 22×22 as physical kinetic matrices.

**Scientific status: isolated full-scalar f-EH chart quadratic GREEN; Gate 2B OPEN; JANUS-R NOT VALIDATED.** Preserve external JHR opposite-sign EH criticism as a separate audit. Commit ONLY on branch research/gate2b-nonhomothetic-transfer, leave main and v2-flrw untouched.

---

# JANUS — POINT DE REPRISE PRIORITAIRE, ETAPE 24 (2026-10-18)

**READ FIRST:** `research/FULL_SCALAR_EH_CHART_WARD_STEP24_AUDIT.md`.
**New direct executable research:** `numerics/hr_eh_full_scalar_chart_ward.py`, `tests/test_hr_eh_full_scalar_chart_ward.py`.
**Reproduce with:** `python scripts/verify_gate2b_step24.py gate2b-step24-report.json`.

## 24. Full native EH scalar kinematic chart Ward GREEN; physical Gate 2B OPEN (LATEST)

The native f Einstein–Hilbert ADM+boundary density is now calculated **nonlinearly with all four independent spherical scalar channels**: lapse Phi, radial shift U, scalar spatial trace psi and traceless shear E, including the necessary native first/second radial derivatives and time rates. It is pulled into a moving/tilted common chart with the exact time+radius Jacobian. For compact interior chart variations, the full finite-action change is zero and the eight mixed Ward derivatives (4 fields x 2 chart modes) vanish to max ~3.25e-12 under finite differences. All eight controls where field sampling is intentionally frozen instead fail by nonzero amounts (min ~1.10e-5; max ~0.312). A simultaneously excited four-field finite-chart action differs by only ~1.73e-18.

**Crucial independent cross-check:** the NEW native ADM nonlinear density, finite-differentiated on the same native compact scalar field/rate profiles, reproduces the prior **independently implemented exact 6-variable EH quadratic Hessian** from `hr_full_scalar_eh_homothetic.py`, including shift/trace/shear kinetic terms. It separately recovers the old repository's spatially flat native ADM EH primitive.

**Actually executed local suite:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests` => **32 passed** (previous 24 focused + 8 new). New step24 manifest script ran and reported exit 0 / 32 passed / non_git_workspace_reconstruction / Git HEAD null / full_repository_regression=false / DeFelice and Aoki NOT_RUN / Gate2B OPEN. The THREE new source/test/runner files are now byte-identical to live GitHub (see SHA in audit). The existing HR/dust prerequisites are still manual algorithm-preserving reconstructions, NOT a clean complete Git worktree. Do not conflate the 32 focused tests with a full independent regression.

**Scope caution:** the result is a **kinematic change-of-variable identity of the f-native ADM+GHY scalar density**. It does NOT implement the complete EH **chart-perturbation quadratic Hessian** in the same native HR+two-dust action, nor prove the full diffeomorphism constraint algebra. The background remains OFF SHELL. No physical kinetic/gradient/fold conclusion can be drawn.

**NEXT EXACT RED:** derive full f-native scalar EH chart variation with `deltaT,deltaR` and all native metric modes on the SAME time-supported compact basis, including boundary terms and native derivative transport, then assemble true EH+HR+two dust action with on-shell Candidate-C background/tadpoles, eliminate four metric auxiliaries and time-dependent BD-null direction, KEEP both dust phase pairs, and pass both independent physical De Felice `mu->0` finite-H and homothetic Aoki `K_S,c_S²` oracles before testing fold 1 at a~0.0301646. If the action cannot pass, report a negative Gate-2B result, not tuned late matching.

**Research branch ONLY:** `research/gate2b-nonhomothetic-transfer`; leave `main` and `research/v2-flrw` untouched. **GATE_2B=OPEN**, JANUS-R NOT VALIDATED; external opposite-EH-sign JHR critical manuscript audit remains separate.

---

## 23.1 — One-command test/provenance runner (2026-10-18; latest addition)

File `scripts/verify_gate2b_step23.py` was committed and exact SHA verified (Git blob `17c7a7693dfd2ed7f0191d8d22b65345da8f952e`). In a complete Git clone on the active research branch, run:

```bash
python scripts/verify_gate2b_step23.py gate2b-step23-report.json
```

It launches the four precisely scoped pytest files, records test exit code/count, Python version, SHA-256 of relevant sources/tests, git commit/worktree origin where available, and explicitly declares `GATE_2B=OPEN`, `full_repository_regression=false`, `DeFelice/Aoki NOT_RUN`. **ACTUAL local reconstructed run:** `tests_passed_count=24`, `tests_exit_code=0`, `workspace_origin=non_git_workspace_reconstruction`, `git_head=null`. No clean Git clone has been run yet; passing on a future clean clone remains a separate acceptance gate. Research audit: `research/REAL_PROVIDER_AND_EH_WARD_AUDIT_2026_10_18.md`.

**Resume next RED unchanged:** full f-native trace/shear+shift EH chart variation and complete spacetime Ward with time tilt, then on-shell background/two-dust/metric/BD constraints and same-action De Felice+Aoki acceptance before first Candidate-C fold. No final JANUS-R physical validation.

---

# JANUS — CURRENT RESUME HEAD, 2026-10-18 (STEP 23)

**FIRST READ:** research/REAL_PROVIDER_AND_EH_WARD_AUDIT_2026_10_18.md. Code/tests: numerics/hr_eh_spacetime_ward.py; tests/test_hr_eh_spacetime_ward.py; tests/test_hr_full_scalar_eh_two_dust_real.py.

## 23. Real native EH+HR+two-dust integration + independent f EH chart Ward (LATEST)

Previous section 22.1 left the real-provider 24-slot combined action as an UNEXECUTED test. **That test has NOW EXECUTED GREEN**, with the actual HR native Hessian algorithms and both real dust canonical blocks (not a MOCK). Two added real-provider regressions pass: 18/30-point combined radial Hessian/gradient quadrature convergence and m²=0 pure EH+two-dust limit. Independent canonical pairs p_g/Y_gdot and p_f/Y_fdot remain rank 2. The diagnostic gradient is NOT zero (off-shell background), so do not interpret matrix eigenvalues as physical stability.

**Independent NEW f Einstein–Hilbert FLRW spacetime diffeomorphism/Ward control is GREEN:** full ADM native lapse density times complete 2D chart determinant, with time/radial compact displacements and moving native perturbation sampling, integrates to zero mixed variation (~1e-18). If native lapse perturbation sampling is deliberately frozen, nonzero residuals remain (-3.22107248e-4, -2.77619145e-5). Direct finite-displacement action and the repo's native ADM primitive confirm the result. This is a **FLRW lapse-only** control, not the full scalar EH Ward. The two new Ward files were byte SHA-verified against GitHub; direct ADM primitive likewise.

**ACTUAL focused local test run:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests` => **24 passed** (11 direct EH, 2 mock-assisted structure, 4 real-provider integration, 7 f EH Ward). Existing HR/dust prerequisites had to be manually reconstructed from GitHub tool source: **same algorithms but NOT byte-identical to GitHub blobs** (docstrings/formatting were compacted); therefore this is NOT a clean checkout or full branch regression. Actions disabled; DNS blocks clone. Do not combine this 24 count with previous separate-session counts.

**NEW IMMEDIATE RED:** extend the full 6-variable f-native spherical scalar EH (including shift, spatial trace/shear, their derivatives and f-chart perturbation jets) through inclined T(t,r), R(t,r), with full compact TIME integration and EH diffeo Ward. Then same-action on-shell Candidate-C background, both dust conservation laws, metric auxiliary/BD-null reduction retaining canonical pairs, and TWO physical oracles (finite-H mu->0 De Felice plus homothetic nonlinear Aoki K_S,c_S²) before first fold a≈0.0301646. No kinetic/fold/CMB validation.

**Status: REAL-ALGORITHM UNTILTED PARTIAL ACTION GREEN; EH FLRW LAPSE WARD GREEN; GATE_2B=OPEN; JANUS-R NOT VALIDATED.** Continue ONLY branch research/gate2b-nonhomothetic-transfer; leave main/v2-flrw unchanged. Keep external JHR critical manuscript audit separate.

---

## 22.1 — Real provider action integration pending (2026-10-18)

**NEXT UNEXECUTED FULL-PROVIDER TEST:** tests/test_hr_full_scalar_eh_two_dust_real.py has now been committed. It imports the REAL hr_two_dust_preconstraint module and the new native scalar EH assembly and checks 24x24 block addition, both canonical dust momentum-rate entries, the two new g trace/shear rate channels and positive f Planck scaling. Its exact GitHub blob SHA is 3ecbf81ea429d5475e902cde2b24fd7441204126. This test has been syntax-compiled locally, but NOT executed because the full prerequisite GitHub worktree cannot be cloned in this environment; do not count it among the 13 passed tests. **Immediate resume action: reconstruct/fetch all real provider modules, RUN this test, fix any actual failure, and record full evidence before extending the chart.**

---

# JANUS — restart checkpoint HEAD (2026-10-18, step 22)

**FIRST READ** research/FULL_NATIVE_SCALAR_EH_UNTILTED_AUDIT.md, then numerics/hr_full_scalar_eh_homothetic.py and tests/test_hr_full_scalar_eh_homothetic.py.

## 22. FULL NATIVE SCALAR EH WITH TWO SECTORS ON AN UNTILTED CHART — LATEST

NEW GitHub files:
- numerics/hr_full_scalar_eh_homothetic.py
- tests/test_hr_full_scalar_eh_homothetic.py
- numerics/hr_full_scalar_eh_two_dust_untilted.py
- tests/test_hr_full_scalar_eh_two_dust_untilted.py
- research/FULL_NATIVE_SCALAR_EH_UNTILTED_AUDIT.md

The native Einstein–Hilbert ADM spatial scalar action now retains BOTH trace and traceless shear of each metric, including their independent temporal rates, intrinsic spherical 3-curvature and extrinsic curvature, in addition to native lapse/radial shift. An exact 6-variable analytic quadratic Taylor jet was checked against an independently written nonlinear spherical ADM density and previous flat-spatial EH limit. The two-metric 24-slot compact spatial projection is valid only on an UNTILTED chart T=t, R_f=(1+mu)r, mu constant.

**Important RED-to-GREEN issue:** f spatial shear potential requires E_f,native=(1+mu)^2 E_f,common and the same scaling for E_f,dot, while f radial shift B_f,native=(1+mu)B_f,common. A cross-HR/EH physical metric shear matching test exposed the missing m² scaling; code corrected. Radial-coordinate rescaling then passes after consistent field redefinition.

**Actual local test evidence:** 13/13 tests PASS in newly created /mnt/data/janus-next. Eleven directly test EH; two use a **MOCK** of the existing HR+two-dust provider to check wrapper structure. The actual combined full 24-slot action has NOT been numerically exercised with the real HR/dust provider in this fresh workspace. Previous 47 targeted test results are historical from a separate session, not re-run; never claim 60 new tests passed. All four newly tested source/test files have exact GitHub blob SHA matching the local bytes (in audit).

**Next immediate RED:** get the actual full 24-slot combined native EH+HR+two-dust provider to run on a single verified workspace, THEN extend EH to nonhomothetic sigma/mu_dot chart with f-native second derivative and chart variation/compact time support. Verify full f EH diffeomorphism Ward. Tie to on-shell Candidate-C, then constraints/BD reduction retaining both dust phase pairs, and reproduce both De Felice and Aoki physical limits before fold.

Scientific result is strictly NATIVE_FULL_SCALAR_EH_UNTILTED_GREEN, GATE_2B_OPEN; full JANUS cosmology is NOT validated. Keep main and research/v2-flrw untouched, work ONLY on research/gate2b-nonhomothetic-transfer.

---

# JANUS — authoritative restart head

## 21. 2026-10-18 — native-flat Einstein-Hilbert interface (CURRENT)

**START HERE:** research/FLAT_EH_HR_TWO_DUST_BRIDGE_AUDIT.md; numerics/hr_flat_eh_two_dust_bridge.py; tests/test_hr_flat_eh_two_dust_bridge.py.

A restricted 22-amplitude EH+HR+two-dust partial Hessian now includes BOTH positive Einstein–Hilbert native lapse/radial-shift ADM blocks evaluated on the same regular compact radial profile as finite-mu HR and two independently preserved dust canonical pairs. The f-native shift radial derivative uses the full inverse chart, producing a B_f-B_f_dot mixed term when the background f-time foliation is tilted. At static g background, the flat ADM shift quadratic integrates to an exact radial boundary.

**ACTUAL local targeted tests:** 10 new tests passed; 47 total tests passed in a reconstructed workspace. Both new source/test files are byte-identical to the exact live GitHub blobs. Independent finite-difference controls required refining a too-large amplitude step 2e-4 to 2e-5; see audit. No full worktree suite or GitHub Actions run.

**CRITICAL LIMIT:** EH spatial traces/shears (psi_g, E_g, psi_f, E_f) and EH relative-chart perturbation columns are MISSING. Thus this is NOT a full EH+HR+dust action; its restricted lapse-shift 4x4 rank 4 does NOT validate the full metric constraints or BD elimination. The background is an off-shell Taylor control, not the on-shell Candidate-C cosmological solution. No ghost/gradient/fold conclusion.

**NEXT EXACT RED:** construct the full native scalar Einstein–Hilbert trace/shear and time/radial chart-variation terms on a single compact spacetime support; test EH diffeomorphism Ward identity, on-shell dust/background tadpoles, metric auxiliary and time-dependent BD-null reductions preserving both phase pairs. Then require both independent physical oracles: finite-H mu->0 De Felice and homothetic nonlinear Aoki K_S,c_S^2. Only then inspect fold 1 a≈0.0301646.

**Gate 2B OPEN. Main/v2-flrw untouched.**


---

# JANUS — authoritative restart head

## 20. 2026-10-18 — finite-mu HR plus BOTH canonical dust phase pairs (NEWEST)

**First read:** `research/HR_TWO_DUST_PRECONSTRAINT_AUDIT.md`, then `numerics/hr_two_dust_preconstraint.py` and `tests/test_hr_two_dust_preconstraint.py`.

New **time-local spatial compact 22x22 partial-action Hessian** combines the validated 16-amplitude finite-mu native HR interaction with two independent canonical dust phase pairs `(Y_g,p_g)` and `(Y_f,p_f)`. The f phase includes the relative time chart variable `q_f=(Y_f-T)F`; all f-native phase gradients are pulled back by the full inverse non-homothetic Jacobian. The f dust momentum is kept dynamical: `H[p_f,Y_f_dot]=-H[p_f,T_dot]`. Both momentum/velocity pairs have rank 2.

**Two actual RED-to-GREEN findings:** (1) the initial new dust implementation doubled `4*pi` in the spherical measure; an independent canonical normalization test failed by precisely `4*pi`; fixed in BOTH sectors. (2) an initial test incorrectly expected the f phase-rate-square block to vanish. The inclined f-native foliation induces a nonzero negative coordinate rate-square from the *native spatial gradient*: `H[Y_f_dot,Y_f_dot]=-4*pi*n_f^3 alpha rho_f(1+mu)^2 int dr r^2 (sigma r)^2 F^2/D`; independently derived and verified, zero when sigma=0. It must not be incorrectly read as a physical ghost before EH/BD constraints.

**Verification:** 10 new targeted tests passed, 37 total tests passed in the reconstructed local workspace; both new file git blob hashes matched live GitHub (see audit). NOT a clean entire repository suite, NOT a physical propagation/fold conclusion.

**LATEST EXACT RED:** include complete native Einstein-Hilbert contributions on THE SAME spacetime compact profiles and common/f-native chart, check tadpoles/IBP and the four metric constraints, then reduce the time-dependent BD null coordinate while retaining both canonical dust pairs. Pass BOTH finite-H mu->0 De Felice and nonlinear homothetic Aoki `K_S,c_S^2` acceptance oracles on this **one** physical action. Fold 1 remains out of scope until both pass.

**Scientific verdict:** `HR_TWO_DUST_PRECONSTRAINT=GREEN_AS_PARTIAL_ACTION`; `GATE_2B=OPEN`. Do not assert JANUS validation. Main and v2-flrw remain untouched.


---

## CURRENT CHECKPOINT — 2026-10-18, compact spacetime beta4 Ward

**Read FIRST:** research/BETA4_SPACETIME_WARD_AUDIT.md.

Four new committed files:
- numerics/hr_beta4_spacetime_ward.py
- numerics/hr_beta4_native_jet_ward.py
- tests/test_hr_beta4_spacetime_ward.py
- tests/test_hr_beta4_native_jet_ward.py

**GREEN only for the off-shell beta4 geometric identity** sqrt(-g)e4(sqrt(g^-1 f))=sqrt(-f) after full compact time/radial integration. Two independent routes agree: direct f-volume variation and the already committed 22x22 native HR jet with coherent native f-field time/radial sampling. If f-field sampling is deliberately omitted, mixed chart/field residuals are nonzero (~+7.13598e-3 and +6.0751e-4 in negative-sign HR jet conventions). Added the f spatial trace factor-3 control and zero linear shift/shear source.

**Actual local targeted verification:** PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests -> 27 passed. The EXACT two existing native HR prerequisite files plus the four new source/test files were matched to live GitHub SHA with git hash-object before final rerun. This is NOT the repository-wide suite (GitHub clone DNS blocked; Actions disabled).

**RED → GREEN incident documented:** while extending field controls the new test harness temporarily reused the field index as the chart-mode loop index, causing four failing tests. Corrected to mode_index; all 27 rerun passed. Do not interpret this diagnostic coding error as physical instability.

**NEXT EXACT RED:** coherent **Einstein–Hilbert + Hassan–Rosen + TWO dust phase** compact spacetime action on an on-shell non-homothetic background. Check beta4 Ward throughout assembly, all boundary/tadpole terms, then four metric constraints and time-dependent BD-null reduction, preserving both dust canonical pairs. Require BOTH the finite-H mu->0 De Felice physical scalar and homothetic nonlinear Aoki K_S,c_S² oracles before any Candidate-C first-fold kinetic/gradient verdict.

**Scientific verdict remains GATE_2B=OPEN; Janus-R not validated.** Preserve JHR external manuscript critical audit as a separate line. Work ONLY on research/gate2b-nonhomothetic-transfer, not main/v2-flrw.

---

# JANUS Gate 2B — point de reprise prioritaire

Date: 2026-10-18
Active branch: research/gate2b-nonhomothetic-transfer
Scientific status: GATE_2B_OPEN

**Read this file first after an interrupted session.** The larger historical journal is research/GATE2B_LATEST_RESTART.md (sections 1–18); the NEW mathematical details are in research/FINITE_MU_NATIVE_TRANSPORT_AUDIT.md.

## Latest commits/results

- numerics/hr_native_sampling_compact.py — 22x16 profile pullback based on the FULL inverse f-native background chart Jacobian, then finite-radius 4*pi*r^2 integration.
- tests/test_hr_native_sampling_compact.py — 10 targeted tests passed in a locally reconstructed environment.
- research/FINITE_MU_NATIVE_TRANSPORT_AUDIT.md — full derivation, assumptions, tests, limitations, ordered next gates.

The inverse-chart identity is

```text
T=t+sigma(t)*r^2/2,   R=(1+mu(t))*r
D=(1+sigma_dot*r^2/2)*(1+mu)-sigma*mu_dot*r^2>0
q_T=((1+mu)*q_t-mu_dot*r*q_r)/D
q_R=(-sigma*r*q_t+(1+sigma_dot*r^2/2)*q_r)/D
```

An actual RED test caught a missing `1/k` in the derivative of the radial metric shift profile; this was corrected. All 10 new targeted tests pass after correction, including finite quadrature convergence and beta0/beta4 sector separation.

**NO physical kinetic or dispersion conclusions follow**: these 16 trial action slots are not the historical 16-dimensional physical pre-metric De Felice state, and the four f-native perturbation amplitude rates are not independent new propagating fields.

## Exact next RED, in order

1. Assemble a coherent time-supported Einstein-Hilbert + native HR + TWO dust canonical phase actions, using this same common/native chart and regular radial support, including all background and perturbation field transports.
2. Check integration by parts, tadpoles, native f-volume/Noether boundary identity and metric auxiliary block rank.
3. Reduce the four metric auxiliaries and the time-dependent BD null coordinate; KEEP both dust canonical phase pairs dynamical.
4. From the SAME completed action reproduce (a) finite-H Candidate-C mu->0 De Felice physical scalar speed, and (b) homothetic Aoki nonlinear kinetic/gradient K_S,c_S^2 including stable AND unstable branches.
5. Only then approach fold 1 (a ~ 0.0301646) and test constrained kinetic/gradient regularity. Continue with transition/late transfer only if healthy.

## Verification and branch rules

- Last targeted local run: `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_native_sampling_compact.py` -> 10 passed. These tests used locally reconstructed prerequisite sources from the committed implementations.
- Whole repository suite NOT run; clone DNS failure and disabled GitHub Actions.
- Keep main and research/v2-flrw untouched; commit on research/gate2b-nonhomothetic-transfer.
- Keep an explicit FAIL/OPEN verdict if the two physical acceptance oracles fail, rather than claiming JANUS validated.

## Parallel audit — external SJHR note, 2026-10-18

**Mandatory reading before external scientific circulation:** `research/JHR_EXTERNAL_PREPUBLICATION_AUDIT_2026_10_18.md`. The corresponding executable tests are `tests/test_jhr_prepublication_gates.py` (4 targeted tests passed in a reconstructed local workspace).

The externally supplied 2026 JHR action is **not** the ongoing positive-kinetic JANUS-R continuation. The source note's *negative* f Einstein–Hilbert sign creates an indefinite common-time TT kinetic form if both couplings are positive. The HR BD constraint does not repair this tensor kinetic sign. The stellar Noether numerical sum cancellation does not establish each separate metric Bianchi constraint, the stated 1 meV strong-coupling scale is incompatible with m~1e-32 eV under the displayed Lambda3 formula, and the apparent CMB third-peak fit is a tunable forced-oscillator output rather than a predicted C_ell.

**Publication gate: external JHR as written FAILS current validation. Do not present as proven.** Keep this audit distinct from Gate 2B, which remains OPEN.
