# Gate 2B — quasi-static late-linear reference bound

Date: 2026-10-11

Status: `PROVISIONAL_STRONG_NEGATIVE_FOR_LATE_LINEAR_CONVERSION__NONLINEAR_TRANSITION_REMAINS_OPEN`

Implementation: `numerics/candidate_c_quasistatic_bound.py`

Regression target: `tests/test_candidate_c_quasistatic_bound.py`

## 1. Purpose

The exact non-homothetic relativistic scalar transfer system is not yet validated: the current 12x12 metric closure satisfies its algebraic/Bianchi checks but does not reproduce the independent De Felice high-k helicity-0 propagation speed. It must therefore not be used as a physical Candidate-C transfer prediction.

A separate quasi-static diagnostic is useful because the late sub-horizon force law can be bounded without pretending that the full relativistic transfer problem has been solved.

This note keeps three statements strictly separate:

1. an exact proportional-background spin-2 kernel;
2. a frozen-background extrapolation of that kernel to Candidate C;
3. an intentionally optimistic reference estimate for late common-to-relative conversion.

Only item 1 is exact within its stated proportional linear regime.

## 2. Exact proportional static spin-2 kernels

Let

`r = alpha * y`

be the instantaneous mixing/Planck ratio on a proportional background and

`S(k) = k^2 / (k^2 + mu^2)`

be the Yukawa fraction of the massive spin-2 propagator.

After diagonalizing the massless and Fierz-Pauli massive modes and normalizing all channels to the common long-range massless interaction, the static kernels are

`Q_gg = 1 + (4/3) r^2 S`,

`Q_gf = Q_fg = 1 - (4/3) S`,

`Q_ff = 1 + [4/(3 r^2)] S`.

Consequences in the short-range limit `S -> 1`:

- the visible self-channel changes only by `+(4/3)r^2`;
- the cross-channel tends to `-1/3`;
- the twin self-channel is enhanced by `1 + 4/(3r^2)` when `r << 1`.

The large twin self-channel is therefore a real structural possibility of strongly asymmetric mixing; it is not evidence by itself for a cosmological growth history.

## 3. Frozen Candidate-C diagnostic

For Candidate C the non-homothetic background is frozen at each epoch and the instantaneous quantities are inserted into the proportional kernel:

`r(a) = alpha y(a)`,

`mu_comoving^2(a) = a^2 m_eff^2(a)`,

with the healthy-branch effective mass already used in `flrw_two_matter.py`,

`m_eff^2 = m^2 (1 + kappa y^2)/(kappa y^2) Gamma`.

This is a local quasi-static diagnostic only. It neglects time-derivative mixing, background non-proportionality corrections and nonlinear screening.

At `z=0`, `k=0.1 h/Mpc`, the reference values are approximately

- `y = 0.55688253`;
- `r = alpha*y = 0.06058631`;
- `m_eff/H0 = 42.31`;
- `S = 0.98047`;
- `Q_gg = 1.00480`;
- `Q_gf = -0.30729`;
- `Q_ff = 357.14`.

Thus the frozen kernel has a striking asymmetric structure: visible self-gravity stays nearly GR while the twin self-channel can be very large and the cross-channel becomes moderately repulsive inside the Compton regime.

This is a mechanism worth testing, but it is not yet a prediction of the full cosmology.

## 4. Where the linear late regime begins

Using the Candidate-C background and the same effective mass, the crossing

`m_eff/H = 1`

occurs at approximately

`z_cross = 16.2455`.

Representative values are

- `m_eff/H ~ 0.25` at `z~142`;
- `m_eff/H ~ 0.40` at `z~50`;
- `m_eff/H = 1` at `z~16.25`;
- `m_eff/H ~ 1.75` at `z~10`;
- `m_eff/H ~ 42.31` today.

The earlier interval is precisely the regime in which the cosmological Vainshtein/nonlinear scalar dynamics may be important, so a purely late linear calculation cannot be extrapolated through it without proof.

## 5. Mixing-angle rotation

Define the instantaneous proportional-reference mixing angle

`theta(a) = atan(alpha*y(a))`.

Candidate C rotates substantially with time. Representative values are

- `theta(z~142) ~ 33.2 deg`;
- `theta(z~100) ~ 27.1 deg`;
- `theta(z~50) ~ 16.7 deg`;
- `theta(z_cross~16.25) ~ 7.624 deg`;
- `theta(z=10) ~ 5.81 deg`;
- `theta(z=0) ~ 3.467 deg`.

Therefore most of the total basis rotation occurs before the clean late `m_eff > H` regime. The residual late rotation from the crossing to today is only

`Delta theta_late ~ 4.157 deg = 0.07255 rad`.

This is the central qualitative result of the bound.

## 6. Deliberately optimistic late-linear conversion reference

To give late linear mode conversion every advantage, assume:

1. the entire late basis rotation is converted into relative-mode amplitude, with fraction

   `f_convert = sin(Delta theta_late)`;

2. after conversion the relative mode grows at the maximum homothetic Aoki-Maeda short-wavelength exponent

   `p_rel,max = (-1 + sqrt(33))/4 = 1.18614066...`,

   while the common mode grows as `a`.

This gives

`f_convert ~ 0.07249`,

and the maximum differential growth from `z_cross` to today is

`G_rel/common,max = (1+z_cross)^(p_rel,max-1) ~ 1.699`.

The resulting optimistic reference is

`(delta_rel/delta_common)_0 ~ 0.123`.

This number is **not a rigorous mathematical upper bound** on arbitrary non-homothetic or nonlinear evolution. It is intentionally generous and serves only as a falsification yardstick for the proposition that the *late linear phase alone* creates an order-unity relative mode from an adiabatic state.

Under this yardstick, it does not.

## 7. Interpretation

The evidence now points to the following hierarchy:

- homothetic linear spontaneous conversion: zero;
- late non-homothetic linear conversion: provisionally too small to generate order-unity segregation by itself;
- nonlinear transition around `H ~ m_eff`: still open and now the dominant serious loophole;
- primordial large isocurvature: mathematically possible but unattractive because it inserts the desired segregation in the initial conditions.

The large frozen `Q_ff` does not contradict the negative late-conversion result. A strong twin self-channel can greatly amplify an already existing twin/relative perturbation. The unresolved question is whether the cosmological transition creates enough of that relative perturbation while remaining on a regular stable branch.

## 8. Required next work

Priority now shifts to two parallel validations:

1. **Nonlinear transition scan.** Apply the Aoki-Maeda-Namba two-matter scalar polynomial to Candidate-C-like parameters through the interval roughly `16 < z < 142`, tracking real roots, branch mergers and stability proxies as the relative source is varied.
2. **Relativistic transfer repair.** Reconstruct a scalar formulation that preserves the helicity-0 graviton and reproduces the independent De Felice high-k scalar speed before using it for Candidate-C transfer functions.

JANUS-R should be rejected if every nonlinear path capable of producing a sizable anti-correlated relative mode either becomes singular/complex, unstable, or remains too screened to leave a measurable late signal.
