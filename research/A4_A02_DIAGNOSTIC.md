# A4 / Candidate-C a=0.2 — conditioning and source diagnostic

Date: 2026-10-12
Branch: `research/v2-flrw`
Status: ACTIVE BLOCKER — do not repair Lagos production code yet.

## Reproducible RED

Commit `fb75b9614e82ab986ec135472b4fcb38ddf51525` adds the early-epoch three-mode gate to `tests/test_de_felice_candidate_c_reduction.py`.

Local reconstructed execution of the production reduction with `k=(250,600,1000)` gives approximately:

- k=250: `[0.37599169, 0.50523292, 0.63249198]`
- k=600: `[0.38001982, 0.63246179, 5.85644189]`
- k=1000: `[0.38009070, 0.63245778, 5.77433015]`
- naive `1/k^2` extrapolation: `[0.38057996, 0.64879073, 6.47709176]`

Independent targets are:

- gravity: `sqrt(0.11385802652451096) = 0.337428550251...`
- f matter: `ctilde * sqrt(0.3) ~= 0.38012193`
- g matter: `sqrt(0.4) = 0.632455532...`

This is a genuine RED: production conditioning/mode extraction fails badly before the subtle gravity-speed discrepancy is considered.

## Root-cause localization already established

1. The raw healthy two-matter action has rank three after the correct time-dependent BD reduction.
2. `a=0.5` already recovers all three high-k modes within the committed tolerance.
3. The old frozen-background pencil failure is closed: freezing before the null-coordinate integration by parts loses required `Kdot/Cdot/Rdot` terms.
4. At `a=0.2`, sorting roots by speed is not sufficient because the gravity and f-matter branches approach/cross.
5. The deeper production failure is numerical: nested finite differences are applied to a reduced action whose coefficients themselves are obtained through finite-difference Hessians and whose natural `S` scale is `O(k^-2)`.

## Stable prototype result — NOT GREEN YET

A local prototype (`prototype_stable_reduction.py`, not committed as production code) does the following:

- build one joint quadratic Hessian in `(Phi,B,varphi,b,u_g,Y2hat,S,Sigma, rates...)`;
- eliminate the four primary auxiliaries by a matrix Schur complement;
- take time derivatives only on the resulting primary coefficient matrices;
- differentiate the null-coordinate Schur complement explicitly;
- solve the final 3x3 Euler-Lagrange system;
- compare/track eigenvectors in a physically rescaled coordinate space where `k^2 S` is used instead of raw `S`.

This removes the catastrophic early-epoch behavior. Typical `a=0.2` stable-prototype speeds trend as:

- k=250: gravity/f/g around `0.330 / 0.390 / 0.63249`
- k=600: around `0.337 / 0.3825 / 0.63246`
- k=1000: around `0.3383 / 0.3813 / 0.63246`

At still larger k the f and g matter branches converge cleanly, while gravity tends near `0.339` rather than the independent `0.33742855` target.

Therefore the prototype fixes the large numerical pathology but must not be promoted to GREEN yet.

## Arbitrary-precision falsification of the roundoff hypothesis

The same source equations and matrix route were re-evaluated locally with `mpmath` at 70 decimal digits (`prototype_mp.py`). Results:

### a=0.5

- k=600: gravity `~0.83274422`
- k=1000: `~0.83228198`
- k=1500: `~0.83213735`
- k=2500: `~0.83206354`

Independent target: `0.831913452637...`.

### a=0.2

- k=600: gravity `~0.33709158`
- k=1000: `~0.33825696`
- k=1500: `~0.33863838`
- k=2500: `~0.33883626`

Independent target: `0.337428550251...`.

Conclusion: the residual gravity-speed bias is not ordinary IEEE-double roundoff or an ill-conditioned eigenvalue solve.

## Non-homothetic interaction sensitivity

The discrepancy grows as `ctilde` departs from 1:

- Candidate-C a=0.5: `ctilde ~= 0.9371`, residual small;
- Candidate-C a=0.2: `ctilde ~= 0.6940`, residual larger.

Controlled local sensitivity probes show that the gravity branch is highly sensitive to the explicitly non-homothetic spatial HR terms, while the matter speeds remain almost unchanged. This localizes the remaining source/reduction audit to the gravity interaction/background sector.

Do NOT tune `Gamma`, the `(ctilde-1)` coefficient, or any interaction coefficient to match Eq. (86). The sensitivity experiment is diagnostic only.

## Matter-variable caveat discovered

De Felice Eq. (54) contains `delta phi_dot / phi_dot_0`. If one defines `u = delta phi / phi_dot_0`, then generically

`delta phi_dot / phi_dot_0 = u_dot + (phi_ddot_0/phi_dot_0) u`.

The background field equations (18)-(19) fix the extra term for a genuine single P(X) fluid. A local prototype adding this term shifts the early gravity branch, but it cannot be adopted as a production correction in the current Candidate-C regression because that regression intentionally uses probe sound speeds (`c_g^2=0.4`, `c_f^2=0.3`) on a background that is actually g=matter+radiation and f=dust. Those probes are not a self-consistent pair of single P(X) background fluids.

This means the tiny residual difference between the raw P(X) action route and the independent Eq. (86) diagnostic may partly measure an inconsistent benchmark embedding, not a wrong Hassan-Rosen coefficient.

## Rejected approaches

- widening tolerances;
- cherry-picking k values;
- sorting modes only by speed magnitude;
- nested five-point differentiation of already-reduced matrices;
- arbitrary rescaling/tuning of `Gamma` or `(ctilde-1)` interaction terms;
- blindly adding the `phi_ddot/phi_dot` term while keeping inconsistent probe sound speeds.

## Required next discriminant

Before any GREEN implementation, construct a benchmark in which the raw Eq. (54) matter backgrounds are internally consistent with their chosen sound speeds, or derive the pure gravity principal limit directly from the raw action after eliminating matter perturbations analytically.

Acceptance condition for the next step:

1. three physical scalar pairs remain present over an objective high-k window;
2. f and g matter speeds converge to their independently imposed characteristics;
3. the gravity branch converges to the De Felice Eq. (86) principal speed without coefficient tuning;
4. the result is stable under derivative-window/step changes;
5. the already-passing a=0.5 regression remains passing.

NEXT: remove the ambiguity caused by inconsistent probe-fluid backgrounds. Build a self-consistent single-P(X) control (or an analytic matter-eliminated principal-symbol control), then decide whether the remaining ~1e-3 early-epoch gravity bias belongs to the source transcription or only to the benchmark embedding. Only after that promote the stable matrix reduction into production with RED/GREEN tests.
