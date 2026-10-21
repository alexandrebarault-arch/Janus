# JANUS Gate 2B — Step44: first genuine physical six-pair Ward and original non-IBP cross-oracle run

Date: 2026-10-21. **Branch: `research/gate2b-nonhomothetic-transfer` ONLY.** Status: **real original-source physical numerics PASS for a finite-resolution Ward and Poisson cross-check**. This does **not** constitute an exact local secondary, Dirac time preservation or validation of JANUS-R.

## 1. The Step43 physical blocker has been genuinely lifted

The actual historical GitHub files were reconstructed byte-for-byte in one coherent **`/mnt/data/janus-step44`** Python runtime. All **SEVEN** source Git blob SHA-1 hashes were computed locally with `git hash-object` and MATCH the genuine GitHub file blobs:

| Module | Git blob SHA-1 |
|---|---|
| `numerics/hr_curved_moving_dust_primary.py` | `ee801e324ae0282f764e29c2b39ff34b1efb73f1` |
| `numerics/hr_curved_primary_mixed_kernel.py` | `45ccd73177cc1588efaf1d53e3dd0179d41ec30b` |
| `numerics/hr_step37_curved_solver.py` | `ce627177d7fa97bad21a7689b292ee24a63930cc` |
| `numerics/hr_step37_original_nonibp_oracle.py` | `005449ade6e3582e3b9a5c3374a881a77e73e3f6` |
| `numerics/hr_step39_cross_oracle.py` | `5b66a1fd416cfa0eaaaef7e43601b6a497b8e8c0` |
| `numerics/hr_step39_highorder_secondary.py` | `0da008cc7d5810235ad1bd73549ef1ac1957f656` |
| `numerics/hr_step43_physical_ward_gate.py` | `386febaa9b805cf423efd6feb7a8027a2069301b` |

Thus, unlike several earlier sessions, **the actual Step43 physical mode DID RUN** with original Step33g/37/39 physical provider modules (not a proxy/adaptor), followed by an independent original **non-integrated-by-parts** oracle. The original source and six-canonical-pair Hamiltonian density were left UNMODIFIED. This is still a **targeted coherent worktree**, not a complete Git clone or an all-repository regression. Shell GitHub DNS access remains unavailable. GitHub Actions/workflows remain user-disabled.

## 2. Actual physical Step43 mode: all nine mixed Kij versus reduced C

Execute on original corrected curved two-dust data:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step43.py --physical \
  --output research/reports/gate2b-step44-original-physical-ward-run.json
```

The witness is constructed by `solve_five_point(scale=.1,degree=4,iterations=6,h=.001)`; all nine Kij are recomputed using the original full six-pair Poisson Euler kernel. From the genuine numerical physical run:

| r | C=K00−K01' | W=K01−K10+K20' | D=K20−K11 |
|---:|---:|---:|---:|
| .11 | +1.7371e−14 | −4.16e−17 | 0 |
| .21 | −1.3422e−13 | −3.82e−17 | +2.17e−19 |
| .31 | −2.9050e−13 | +1.23e−16 | 0 |
| .43 | +5.1559e−13 | −5.81e−16 | −4.34e−19 |
| .61 | −3.2362e−13 | +1.05e−15 | 0 |
| .71 | +1.8344e−12 | −1.02e−15 | 0 |
| .83 | +5.0186e−11 | +1.04e−15 | 0 |

The four excluded coefficients `K02,K12,K21,K22` were **numerically exactly zero** at all seven points. This is a numerical structure observation, not a symbolic identity over the complete phase space.

For two independent smooth compact lapse pairs A and B:

| Pair | Full six-pair 3×3 Gauss bracket (48 points) | Reduced ∫NMC | Difference |
|---|---:|---:|---:|
| A | +7.913770365260479e−14 | +7.930804929346914e−14 | −1.703456408643471e−16 |
| B | +1.3164723517088146e−13 | +1.317326181790549e−13 | −8.538300817343919e−17 |

Repeating with 96 Gaussian points: A full (+7.911118062876338	imes10^{-14}), B full (+1.3162936854562068	imes10^{-13}); the full−C-only differences stay near (10^{-16}).

These confirm that, for this numerical primary+approximately-secondary witness, the Step43 warning about potential untested W,D/high-jet obstructions does **not** manifest above numerical noise. A proof that the physical Ward identities hold exactly (for all admissible canonical fields, lapses, and boundary conditions) remains **OPEN**.

## 3. Independent original-action NON-IBP canonical Poisson oracle at FOUR resolutions

The independent original nodal code `hr_step37_original_nonibp_oracle.hamiltonians` uses the original **UNINTEGRATED** positive-EH spherical ADM 3-curvature and two-dust Hamiltonians. It perturbs ALL 12 canonical grid fields, recalculates the radial derivatives and algebraic relative shift, then computes the six canonical-pair Poisson contribution sums. This is mathematically and discretely distinct from the symbolic-Euler/IBP Kij compiler.

The Step44 runner `scripts/verify_gate2b_step44.py` **REFUSES any change in the seven original provider blobs** before running. Its actual full-mode output was generated locally from real original files:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step44.py --full \
  --output research/reports/gate2b-step44-physical-verification.json
```

Actual original nodal bracket values:

| Number of radial grid points | Pair A | Pair B |
|---:|---:|---:|
| 161 | −5.909465625175692e−7 | −9.466190735718527e−7 |
| 321 | −1.477084414225338e−7 | −2.3664925166699824e−7 |
| 641 | −3.692529046417370e−8 | −5.916187453824939e−8 |
| 1281 | −9.231157505062981e−9 | −1.479034814066971e−8 |

The original discrete primary residual also improves by roughly a factor four when the grid doubles: (6.09	imes10^{-8}) at 161, (1.53	imes10^{-8}) at 321, (3.89	imes10^{-9}) at 641, (1.30	imes10^{-9}) at 1281. These grid values are **not** zero; do not misrepresent them as an exact finite-grid constrained physical solution.

Assuming (but **NOT proving**) an even-power spatial-grid error expansion, first- and second-level Richardson extrapolation of the independent original-action oracle gives:

| Extrapolation R4 using successive triple of grids | Pair A | Pair B |
|---|---:|---:|
| 161/321/641 | +8.169391088888889e−14 | +1.330960033586667e−13 |
| 321/641/1281 | +7.305637576480000e−14 | +1.324021139624889e−13 |
| Gauss full Kij 96 nodes | +7.911118062876338e−14 | +1.316293685456207e−13 |

The smallest absolute difference of the **last** R4 estimate to the independent 96-point Gauss result is about (6.05	imes10^{-15}) for A and (7.73	imes10^{-16}) for B. Extrapolation here is an **empirical convergence model**, not a rigorous continuum bound, and floating-point cancellation becomes relevant near (10^{-13}).

The GitHub-persisted `research/reports/gate2b-step44-report.json` includes all these original grid values, independent Gauss comparisons, seven physical Ward points and provenance. The **entire** generated 14.5-KB raw output was created locally under `research/reports/gate2b-step44-physical-verification.json` (SHA256 `7ae03597e0ba95e9775d434274aa75ecb8264ba72a58157849687e09d2b05ab9`) but was NOT separately uploaded; reproduce with the now-committed `--full` runner. This distinction is essential for audit honesty.

## 4. The Ward near-zero is not a side effect of fitting C

We also ran the true physical six-pair kernel on THREE additional primary-satisfying witnesses without the Step39 secondary fit:

| Additional primary data family | Max sampled |C|, r=.21,.43,.71 | Max sampled |W| |
|---|---:|---:|
| Same curved geometry, no f-momentum correction | 0.4286432361840241 | 1.0200e−15 |
| Independently changed curvatures, gravitational momentum gradients, dust phases, relative shift | 0.5819868015092623 | 1.3808e−15 |
| Spatially flat but noncomoving and nonzero gravitational gradients | 0.5215030263987035 | 1.0547e−15 |

All three have (D) at the ~1e−19 floating floor and excluded high jets zero at sampled radii, **even though C is intentionally far from zero**. This is strong evidence that Ward near-cancellations are structural in this restricted source family, not a mere consequence of the numerical secondary correction. An exact structural identity is still to be derived.

## 5. Actual regression, protection from interrupted work

New files, uploaded and verified with GitHub blob hashes identical to the local EXECUTED bytes:

- `scripts/verify_gate2b_step44.py` — `2d088b7734abfb2487da43bd5330d465f114a1ae`.
- `tests/test_hr_step44_original_physical_ward.py` — `bb06f2f56911b9f5f8932184b650a90e21b73bdd`.

Commands executed from the same exact-provider worktree:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step44_original_physical_ward.py
# ACTUAL: 10 passed in 11.97 seconds

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step43_ward_operator.py \
  tests/test_hr_step43_physical_ward_gate.py \
  tests/test_hr_step44_original_physical_ward.py
# ACTUAL: 33 passed in 13.17 seconds.
```

The two historical Step43 test modules in the 33-test run were additionally reconstructed with actual GitHub SHA matches `04825a5034421fc1e12dd51ba361d81cfbd5b753` and `c9eea74b6b14eef81d0816d960b10f9744e0b8b9`. These passes are **joint**, unlike some separately run earlier tests. No claim that the whole repository test suite or GitHub CI was run; user disabled Actions and workflows.

## 6. Remaining HARD RED — Step45

1. **Analytic/interval derivation of the PHYSICAL Ward identities:** starting with the original six canonical-pair positive-EH two-dust HR action, prove or disprove `K02=K12=K21=K22=0`, `D=K20-K11=0`, and `W=K01-K10+(K20)'=0` as **exact** identities on the intended physical constraint surface. If not identically true, establish the full five-coefficient adjoint obstruction, including boundaries. Do not use numerical ≈0 as an exact mathematical identity.
2. **Exact local secondary:** eliminate the numerical finite-h radial derivative `(K01)'`, derive/satisfy `C_local(r)=0` on a nontrivial continuous curved noncomoving radial interval while preserving positive two-dust initial data and centre regularity, or identify a genuine obstruction. The current best `~5e-11` sampled C is only approximate.
3. **True Dirac time preservation:** calculate `{C_local,H_total}` with ALL SIX canonical pairs and corresponding smearing/boundary terms; show actual lapse fixing or independent obstruction and full constraint rank, including exceptional K/J sectors. DO NOT infer Boulware–Deser absence from Step44 alone.
4. Only subsequently assess genuinely nonhomothetic **ON-SHELL** evolution, same-action De Felice finite-H mu→0 and Aoki nonlinear (K_S,c_S^2) healthy/unhealthy controls, Candidate-C fold and eventual observations.

**VERDICT: STEP44 physical original-source Ward and independent Poisson cross-checks numerically consistent; symbolic physical Ward and exact secondary + its preservation = OPEN; Gate 2B OPEN; JANUS-R NOT VALIDATED.** The separate sign-reversed f-EH external JHR critique is not this positive-EH HR initial-data construction.
