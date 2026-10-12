# JANUS-R — Latest checkpoint

Date: 2026-10-12
Canonical branch: `research/v2-flrw`
Draft PR to `main`: `#1`
Authoritative restart queue: `research/RESTART_TASKS.md`

## Current conclusion

`LITERAL_PUBLISHED_JANUS = REJECT_AS_ESTABLISHED_THEORY`.

If forced into a binary decision on Jean-Pierre Petit's published Janus model today: **MOST LIKELY FALSE OR FUNDAMENTALLY INCOMPLETE AS WRITTEN.**

That conclusion has not changed. The surviving research program is JANUS-R: a ghost-free Hassan-Rosen bimetric descendant with two positive-energy matter sectors, each minimally coupled to its own metric. It does not impose fundamental negative mass, a universal exact `+G/-G` law, or isolated negative photon lensing by twin matter.

## Gate 2B — major update

The previous apparent hard failure of the scalar gate has been localized and largely resolved.

The old Lagos-based diagnostic showed both matter modes correctly but a third scalar frequency saturating at finite `omega` instead of propagating as `omega ~ k`. That behavior is **not** evidence that the raw Hassan-Rosen two-matter scalar action lacks the helicity-0 mode.

The main cause was the order of reduction: the background was frozen before removing the null Boulware-Deser coordinate. In the time-dependent quadratic action

`L = 1/2 qdot^T K qdot + qdot^T C q + 1/2 q^T Q q`,

the physical equations are

`K qddot + (Kdot + C - C^T) qdot + (Cdot - Q) q = 0`.

The f-sector physical scalar variable in g-flat gauge is, up to a harmless background normalization,

`Y2hat = u_f - (Sigma + k^2 S/6)/(n H_f)`.

Its derivative necessarily contains the background derivative term

`Rdot (Sigma + k^2 S/6)`, with `R=1/(n H_f)`.

Dropping this term or freezing before the null-coordinate integration by parts produces the false saturating branch.

## Raw source action

The independent raw De Felice route is now implemented in `numerics/de_felice_raw_scalar_action.py` from:

- Eq. (44) EH scalar action for g and f;
- Eqs. (45)-(46) exact Hassan-Rosen interaction;
- two copies of Eq. (54) P(X) matter action.

A genuine Fourier-sign transcription bug in Eq. (44) was found and fixed:

`B * E_dot` coefficient -> `-2 k^4/(3 N a)`.

RED: `64bfd19a184a7df39b9d075822f9a621c62fd59f`

GREEN: `7d9f57d8a892cf51c1c9823b9c74655f2e914e71`

Independent cross-checks now include:

- exact cancellation of the spurious pure-E shift/velocity term under the De Felice/Lagos map;
- exact de-Sitter mapping of the source EH/background-determinant combination to the Lagos EH block;
- exact proportional-limit mapping of the HR relative block to the healthy Lagos interaction;
- Minkowski Eq. (44)+Fierz-Pauli gives `omega^2=k^2+m_eff^2`, hence high-k `c_s^2=1`.

## Time-dependent physical reduction

Generic reduction code is in `numerics/time_dependent_quadratic_reduction.py`.

Key commits:

- RED generic null reduction: `0ba69ef36b0396fc5eb7457f6fda52e21a95a445`
- GREEN generic reduction + `Y2hat` map: `a2e47995bec88d61501e36da8c02b83333420edf`
- RED local Schur-conditioning regression: `afce1faaf404393b03f89e1d33534e37f81be737`
- GREEN local conditioning fix: `e865ccf3e1fc4eb6c7191cec3aebc7cc814d0ea5`

After the four primary auxiliaries `(Phi,B,varphi,b)` are eliminated, the 4-coordinate kinetic Hessian has rank exactly 3. Its null vector matches the De Felice BD combination. After the time-dependent null reduction, the physical system is a proper 3x3 scalar system.

## Candidate-C quantitative result at a=0.5

Committed benchmark: `numerics/de_felice_candidate_c_reduction.py`.

RED: `2553b53bd8a2a9aac8482300651602d3ad0360c2`

GREEN: `cebd1e2b04c7a7b0ae1c2deb9d8dcc7246efae7e`

Using probe sound speeds `c_g^2=0.4`, `c_f^2=0.3`, finite `k=(100,150,250)`, and a linear extrapolation in `1/k^2`:

- f matter: `~0.51313903`; independent target `~0.51326362`;
- g matter: `~0.63245555`; target `0.63245553`;
- gravity: `~0.83187090`; independent De Felice target `0.83191345`;
- gravity error: about `4.3e-5`.

The committed `a=0.5, k=150` physical 3x3 kinetic matrix is also positive.

This is the first quantitative recovery of all three expected high-k scalar modes from the independent raw two-matter action without coefficient tuning.

## Verification status

Latest reconstructed targeted command:

`python -m pytest -q tests/test_time_dependent_quadratic_reduction.py tests/test_de_felice_raw_scalar_action.py tests/test_de_felice_candidate_c_reduction.py`

Result on 2026-10-12:

**`16 passed in 4.07s`**

This is **not** a clean full-repository-suite result. GitHub Actions remain disabled.

## Multi-epoch gate

The scalar gate is **not yet fully passed** because A4 requires more than `a=0.5`.

### a=1

Preliminary result is consistent:

- independent gravity target `~0.97345679`;
- extrapolated raw-action result `~0.97421582`;
- error `~7.6e-4`;
- both matter branches also converge correctly.

This has not yet been frozen as an acceptance regression.

### a=0.2

This is the active blocker.

Independent default-probe targets are approximately:

- gravity `0.33742855`;
- f matter `0.38012193`;
- g matter `0.63245553`.

The gravity and f-matter branches become close enough that sorting eigenvalues by speed permutes their identity. At higher k the nested finite-difference derivatives of the coefficient matrices also become ill-conditioned, while the g branch stays stable.

A symmetric five-point derivative experiment was tried and **rejected**: it degraded the already-good `a=0.5` gravity result by roughly `6e-3`. It was never pushed to Git.

The next fix must therefore improve branch continuation and derivative conditioning objectively; tolerances will not be widened to hide the problem.

## Immediate next action

1. Track physical modes across k by eigenvector overlap/continuation rather than sorting by eigenvalue magnitude.
2. Replace the ill-conditioned nested background finite differences with a better-conditioned analytic/semianalytic derivative route where possible.
3. Require any numerical change to preserve the committed `a=0.5` regression.
4. Freeze `a=1` and `a=0.2` acceptance tests only after convergence is demonstrated.
5. Only after the multi-epoch A4 gate passes, compare the validated raw reduction back to the old Lagos/Comelli transfer and repair the production solver.

## Research decision

- Literal Janus: **conclusion reached; do not spend effort rescuing its negative-mass / exact +/-G formulation absent genuinely new mathematics.**
- JANUS-R: **still open as targeted falsification-driven R&D.**
- Gate 2B: **major progress — the helicity-0 scalar has been recovered at `a=0.5`; multi-epoch numerical validation remains.**
- PR #1 remains draft and must not be merged as a validated cosmological model.
