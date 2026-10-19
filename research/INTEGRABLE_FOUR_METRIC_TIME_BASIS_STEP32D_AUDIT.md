# JANUS Gate 2B — Step 32d: genuinely integrable compact time-basis for all four scalar metric fields

**Date:** 2026-10-19. **Branch:** `research/gate2b-nonhomothetic-transfer`.

**Verdict:** `FOUR_METRIC_PARENT_FIELD_VELOCITIES_INTEGRABLE_GREEN`; `HOMOGENEOUS_ONSHELL_COMPACT_TADPOLES_16_OF_16_GREEN`; `TWO_DUST_CANONICAL_PAIRS_GREEN`; **`TRUE_FIELD_THEORY_ADM_BD_REDUCTION_OPEN`, `GENUINE_NONHOMOTHETIC_ONSHELL_OPEN`, `GATE_2B_OPEN`**.

## Why this step was necessary

Step 31 built one nonlinear compact spherical Einstein–Hilbert_g (+), Einstein–Hilbert_f (+), all-beta Hassan–Rosen, covariant two-dust action on a **physically HOMOGENEOUS, radiation-free, on-shell Candidate-C** background. Step 32a transformed BOTH irrotational dust actions exactly into common-time canonical first-order form, retaining `(theta_g,p_g)` and `(theta_f,p_f)` independently. Step 32b added four independent spatial scalar *rate jets* into the same integrated action. Step 32c correctly found a finite-Galerkin four-lapse/shift auxiliary block of rank four and an algebraic Schur, but discovered the critical fact: its independent spatial scalar velocities were **not actual derivatives of the chosen compact parent fields**. Consequently the Step 32b 18x18 jet and the Step 32c Schur could not be treated as a physical quadratic scalar action.

**Step 32d repairs this specific mathematical inconsistency.** It makes the four additional rates part of bona fide compactly supported parent metric fields, changes spatial intrinsic curvature and the Hassan–Rosen interaction consistently along with extrinsic curvature, and checks all sixteen globally integrable compact field first variations on the original homogeneous on-shell background. It does **not** solve the remaining canonical gravitational constraints.

## Explicit compact parent fields and true time derivatives

Let

```
T(t) = [1-(t/Tmax)^2]^4,                 F(r) = [1-(r/Rmax)^2]^4,
G(t) = t T(t),                           G'(t) = T(t)+t T'(t).
```

Both `T` and `G` vanish smoothly at the time-support boundaries. The original spatial scalar perturbations `psi_s`, `E_s` (`s=g,f`) are now accompanied by TWO NEW, independently compact parent field amplitudes per metric:

```
psi_s(t,r) = [psi_s0 T(t) + psi_s1 G(t)] F(r),
E_s(t,r)   = [E_s0   T(t) + E_s1   G(t)] r^2 F(r),

dot(psi_s) = [psi_s0 T'(t) + psi_s1 G'(t)] F(r),
dot(E_s)   = [E_s0   T'(t) + E_s1   G'(t)] r^2 F(r).
```

The underlying spherical scalar metric is still **linear** in the trace/shear potentials (matching the original nonlinear Einstein–Hilbert/HR convention):

```
Q_r = 1+2psi - (2/3) k^2 E,
Q_t = 1+2psi + (1/3) k^2 E,
ADM_N = n sqrt(1+2Phi+U^2/Q_r),
ADM_shift^r=(n/a) U/Q_r.
```

The code recomputes **all** affected quantities from the same metric: `Q_r`, `Q_t`, their first/second radial derivatives, `Q_r_dot`, `Q_t_dot`, radial/angular extrinsic curvatures `K_r,K_t`, and the **intrinsic spherical 3-curvature**. Therefore the action is not obtained by bolting a kinetic-rate Hessian onto an unchanged spatial-metric action: both `EH_g/f` and the relative HR potential and the spatial geometry seen by both dust Hamiltonians are updated exactly and consistently.

The same compact spacetime Gauss–Legendre quadrature, the radiation-free Candidate-C homogeneous on-shell trajectory, the original scalar lapse/radial shift trial fields and both canonical dust phase/momentum profiles from Steps31/32a remain unchanged.

## Independent second derivation of exact native Einstein–Hilbert rate transport

At any individual time/radius point, the new parent profile can equivalently be written as an **instantaneous old scalar amplitude** `psi_eff=psi0+t*psi1`, `E_eff=E0+t*E1` multiplying the old time profile `T`. The full true velocity then equals:

```
psi_dot = psi_eff T' F + psi1 T F,
E_dot   = E_eff T' r² F + E1 T r² F.
```

That decomposition admits a direct **independent cross-implementation check** against the previously audited Step 31 spherical ADM metric and the Step 32b exact nonlinear extrinsic-curvature correction:

```
EH_step32d(psi0,E0,psi1,E1)
  = EH_step31(psi_eff,E_eff) + delta_EH_step32b(psi_rate=psi1,E_rate=E1)
```

at **finite nonzero** lapse, shift, trace and shear fields. Both g and f sectors pass, and their full native/common spherical metric components, angular area and intrinsic 3-curvature agree with the independent old Step 31 calculation at the chosen point. This is not merely a direct numerical derivative of the new density against itself.

## Main scientific result: the four previous apparent first variations disappear when fields become integrable

At `Tmax=0.027`, `Rmax=0.32`, 20×20 Gaussian quadrature and centered amplitude step `2e-5`, the integrable compact quadratic action gives the following **four NEW legal metric parent-field first variations**:

```
(field)                     dS/d(field amplitude)
psi_g extra compact G(t)    -1.3010426069826053e-13
E_g extra compact G(t)      +4.336808689942017e-14
psi_f extra compact G(t)     0.0
E_f extra compact G(t)      -4.336808689942017e-14
```

Including the original 12 legal compact metric/dust field directions, the maximum magnitude among **all sixteen globally admissible test-field first variations** is `1.3964523981613295e-11` in the dimensionless test normalization. This is the appropriate action-level integration-by-parts/on-shell check for these compact profiles.

As a crucial, deliberately **failing old-ansatz control**, the disconnected Step32b **g trace rate jet** `delta psi_dot = v*T(t)*F(r)` with no associated parent field produced:

```
OLD disconnected g metric velocity first variation: -0.0003058752883790261
NEW integrable g parent G=tT first variation:       -0.00000000000013010426069826053
```

The first number was NOT a physical background tadpole because that local rate amplitude was not a valid globally compact metric field variation. The second number is the valid test of the Euler–Lagrange first variation after enforcing time integrability. At `t=0`, `G=0` but `G'=1`, which explains how a compact global parent field can have a nonzero instantaneous rate without violating the boundary conditions. The exact derivative is `G'=T+tT'`, NOT just `T`.

**Two old dust `theta_rate` probes at indices 6 and 13 remain independent, nonintegrable local jets.** Their raw first derivatives are approximately `+3.00401582e-4` and `+4.14314475e-5` and are intentionally EXCLUDED from the set of sixteen legal compact test variations. This is a remaining step on the way to a fully time-integrable canonical field/rate basis.

## Both dust canonical pairs and full nonlinear metric sourcing

The two exact common-time canonical matter pairs remain independent:

```
H[p_g,theta_rate_g]=+9.450339095e-5,
H[p_f,theta_rate_f]=+1.303392697e-5,
H[p_g,theta_rate_f]≈H[p_f,theta_rate_g]≈0;
rank=2.
```

The `f` trace extra **parent field** at finite amplitude changes the intrinsic `f` spatial curvature and the HR interaction (though the *integrated* effect can be tiny because `G(t)` is temporally odd); the g EH and g dust actions remain exactly unaffected. A useful canonical subtlety was caught in the tests: for fixed matter canonical momentum and a comoving dust phase `theta_r=0`, the dust Hamiltonian is **`N p`** and does **not** directly depend on the spatial metric. Accordingly, the `f` dust piece does **not** change under a pure `f` spatial trace perturbation at this particular comoving canonical base point. Demanding a nonzero `f` matter variation here would be a wrong physics test.

## Test provenance, failures and scope

New files:

- `numerics/hr_integrable_metric_time_basis.py` — exact four compact parent trace/shear fields and their derivatives in both nonlinear EH metrics; same all-beta HR and dual-dust canonical matter action.
- `tests/test_hr_integrable_metric_time_basis.py` — 10 new regressions: true compact time derivatives and edge support; exact zero-extra reduction to Step32a; independent Step31+32b finite-amplitude nonlinear EH identity for g AND f; sixteen legitimate field first-variation cancellations; old bad rate-only control; genuine `f` spatial curvature/HR response; two dust canonical pairs; quadrature convergence; full-metric parent-vs-rate-only difference; invalid-domain guards.
- `scripts/verify_gate2b_step32d.py` — exact source hash manifest and all physical acceptance gates marked honestly open.

**Two new tests initially failed** due to excessively large thresholds for tiny integrated `f` EH and local EH perturbation differences. A related incorrect expectation that the comoving, fixed-momentum dust Hamiltonian depends directly on the spatial metric was found and removed. The equations were not tuned to make tests green; the corrected expectations follow exactly from `H_dust=N p sqrt(1+theta_r²/g_rr)+N^r p theta_r`. Their new controls distinguish nonzero EH curvature/HR interaction from exactly unchanged comoving fixed-momentum dust. All 10 new tests then pass.

**Actual combined local execution** in `/mnt/data/janus32`:

```
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests
# 81 passed

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step32d.py gate2b-step32d-report.json
# 81 passed; exit 0
# max_abs_legal_compact_first_variation=1.3964523981613295e-11
# canonical_dust_pair_rank=2
# full_repository_regression=false; Gate2B OPEN; BD/DeFelice/Aoki NOT_RUN.
```

Breakdown: 29 exact Step31 + 20 Step32a + 11 Step32b + 11 Step32c + **10 new Step32d** in **ONE** focused environment. The Step32c restricted Schur remains a separate **finite-basis diagnostic**, not a validated physical constraint reduction, and its numerical complement must NOT be substituted unchanged after changing the actual metric time basis.

**Provenance caveat:** the exact Step31/32a/32b/32c modules and tests were checked as local Git hashes against their corresponding GitHub blobs in previous steps. However this workspace is NOT a complete clean checkout of the full repository and the Steps 27–30 test suites were not run here. The Step32d GitHub hashes must be checked byte for byte against the tested local files before publishing this audit as final. GitHub Actions were previously disabled; no external independent run is claimed.

## Precise next RED gates

1. Close the **remaining two canonical dust `theta_rate` jets** by choosing compact, time-integrable parent phase profiles while retaining independent canonical momentum fields. Redo the 18-slot complete quadratic with the corrected four metric parent fields and correct full boundary integration-by-parts.
2. Derive the actual field-theory **ADM lapse and shift constraints** on this gauge-/derivative-compatible basis. In particular a finite-dimensional Schur from the old Step32c jet action does not suffice, and complete diagonal diffeomorphism Ward closure must be checked on shell.
3. Derive the HR time-dependent **Boulware–Deser null/canonical constraint** while preserving BOTH independent dust phase-momentum pairs; only then physical reduced kinetic/gradient matrices and mode speeds can be evaluated.
4. Independently construct a truly **nonhomothetic PHYSICAL on-shell** Candidate-C solution rather than relabeling the homogeneous one with an inclined f-native chart; check ALL g/f Einstein, HR and two-dust first variations.
5. Demand SAME-ACTION physical De Felice finite-H `mu→0` and nonlinear homothetic Aoki `K_S,c_S²` stable and unstable controls before approaching Candidate-C first relative-mu fold at `a≈0.0301646`, then only later observational likelihood. Publish a negative viability conclusion if genuine obstructions persist.

**Scientific disposition:** `FOUR_INTEGRABLE_COMPACT_METRIC_PARENT_FIELDS_GREEN`, `DUAL_CANONICAL_DUST_PAIRS_GREEN`, **`PHYSICAL_ADM_AND_BD_CONSTRAINTS_OPEN`, `GENUINE_NONHOMOTHETIC_BACKGROUND_OPEN`, `GATE_2B_OPEN`, `JANUS_R_NOT_VALIDATED`**.
