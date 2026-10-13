# Late exact-dust mode mixing and principal stability audit

Date: 2026-10-13
Branch: `research/gate2b-nonhomothetic-transfer`
Status: **PRINCIPAL INSTABILITY CONFIRMED; CONTINUOUS EIGENPAIR LABEL IS NOT THE STABILITY ORACLE**

## Why this addendum exists

`research/LATE_DUST_TRANSFER_AUDIT.md` correctly found a negative finite-speed scalar branch at the planned dust matching surface for `k >= 0.05 h/Mpc`, but its next step was to determine whether that result survived continuous mode tracking.

The new continuous/biorthogonal tracking work found an important distinction:

- a spectral pair followed continuously backward from today can exchange its physical character with a dust-like pair near a quasi-degeneracy;
- the local finite-speed principal scalar character is therefore not guaranteed to stay attached to the same pair of eigenvalue labels;
- stability must be diagnosed from the principal finite-speed mode, while continuous pair transport is a separate mode-mixing diagnostic.

This corrects the *interpretation of pair identity*, not the existence of the early exact-dust instability.

## 1. Nonnormal tracking correction

The original biorthogonal tracker used

`|Tr(P_old P_new)| / rank`

as a projector-overlap score.  For non-orthogonal spectral projectors this quantity is similarity invariant but not bounded by one.  In strongly nonnormal regions it can therefore prefer a wrong pair.

The replacement score uses the nonzero eigenvalues of `P_old P_new`.  If they are `lambda_i`, define

`distance = max_i |lambda_i - 1|`,

`score = 1/(1+distance)`.

It is bounded and remains similarity invariant.  Synthetic nonnormal regressions and an adaptive refinement helper are committed in `numerics/dust_mode_tracking.py` and `tests/test_dust_mode_tracking.py`.

A persistent low score after refinement is now treated as a real quasi-degenerate/mixed cluster and is exposed to the caller rather than being mislabeled as numerical failure.

## 2. Continuous late-pair transport is positive but becomes dust-like

Independent executable reconstruction of the committed Candidate-C dust generator gives, at the planned start `a_start=0.057951440818742664`, the continuously transported late pair approximately

| k [h/Mpc] | transported-pair c^2 at a_start |
|---:|---:|
| 0.05 | `+2.254e-3` |
| 0.10 | `+5.636e-4` |
| 0.20 | `+1.337e-4` |

The approximate `k^-2` decrease is the key fact: this transported pair has become dust-like at the early endpoint.  It is not the finite-speed principal gravity character there.

At `a ~= 0.5` the same late-connected transport returns values around the independently validated Candidate-C gravity target (`~0.692`, with finite-k deviations), so the mode character is exchanged through the intervening mixed/quasi-degenerate region.

At `k=0.2 h/Mpc` the two-dimensional spectral projector becomes strongly mixed near `N ~= -2.39`; individual-pair overlap can remain near `~0.5` even under aggressive refinement.  A single globally named two-dimensional “gravity pair” is therefore not a well-conditioned object through that region.

## 3. Principal finite-speed branch remains unstable at the planned start

The exact-dust system has two pressureless matter branches whose squared phase products vanish with increasing k, plus one finite-speed scalar principal branch.

At `a_start`, the three local squared-speed diagnostics previously obtained were

| k [h/Mpc] | two dust-like diagnostics | finite-speed principal diagnostic |
|---:|---:|---:|
| 0.05 | `~1.0e-5`, `~2.25e-3` | `-8.26e-3` |
| 0.10 | `~2.5e-6`, `~5.64e-4` | `-8.43e-3` |
| 0.20 | `~6.1e-7`, `~1.34e-4` | `-8.89e-3` |

The negative branch stays O(1e-2) rather than falling as `k^-2`; the positive pair transported from today is precisely the branch that *does* fall as `k^-2`.

Therefore the negative start-point branch is not a labeling artifact.  It is the finite-speed exact-dust principal instability.

## 4. Stability boundary

Using the conditioned production-like generator and identifying the local finite-speed principal character at each point gives a remarkably scale-coherent zero:

| k [h/Mpc] | principal c^2(a_start) | zero a | zero z |
|---:|---:|---:|---:|
| 0.05 | `-0.0082583` | `~0.1016483` | `~8.83785` |
| 0.10 | `-0.0084287` | `~0.1016475` | `~8.83792` |
| 0.20 | `-0.0089205` | `~0.1016576` | `~8.83694` |

The spread in the crossing is only about `1e-5` in scale factor across these three production scales.  This is consistent with a real background-controlled stability boundary, not a random pair-sorting failure.

The committed production diagnostic is now split explicitly:

- `track_candidate_c_dust_gravity(...)`: transport a late spectral pair and expose mixing/low-overlap regions;
- `candidate_c_dust_principal_stability(...)`: follow the local finite-speed principal character used for stability.

## 5. Scientific consequence

The earlier negative conclusion for the strict dust+dust benchmark survives, but for a more precise reason:

> The planned `m_eff/H=1` start at `z ~= 16.26` lies before the finite-speed exact-dust principal scalar becomes healthy.  For `k=0.05...0.2 h/Mpc`, the principal branch crosses to positive only near `z ~= 8.84`.

Continuous late-pair transport does not remove this instability.  It reveals a mode-character exchange: the pair that is gravity-like at late times becomes dust-like before the unstable interval, while the finite-speed gravity character transfers to another local spectral pair.

The provisional large transfer values (`R(z=0)` of order 10-30 in earlier runs) still cannot be counted as successful healthy segregation when initialized at `m_eff/H=1`, because the evolution interval includes the principal unstable regime.

## 6. Next discriminating test

The next controlled calculation is **not** another global eigenpair label.  It is:

1. define a new matching surface on or after the principal healthy boundary (`a >= ~0.10165`, `z <= ~8.84`), with a safety margin;
2. construct the GR-connected/common initial lift directly on that healthy surface using the production KKT observable maps;
3. integrate only the healthy late interval;
4. measure `R(z=0,k)` at `k=0.01,0.05,0.1,0.2 h/Mpc`;
5. test sensitivity to moving the matching surface later;
6. only if this healthy-interval conversion is both large and stable should a 2x2 density transfer matrix be promoted.

If healthy-interval conversion is small, then the large earlier `R` values are diagnosed as instability-driven rather than a viable late Janus-like mechanism.

## Verification limitation

The numerical values above were independently reproduced from the committed production formulas in a reconstructed executable workspace.  The full repository suite still cannot be run in this environment because the container cannot clone GitHub and GitHub Actions remain disabled.  Do not describe the full branch as globally green until an actual full worktree test run is available.
