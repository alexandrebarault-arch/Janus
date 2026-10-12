# V2 Mean Gauge and Lapse-Ratio Representation

Date: 2026-10-11
Branch: `research/v2-flrw`
Status: `MEAN_GAUGE_USEFUL_BUT_NOT_A_LAPSE_SHORTCUT`

## Purpose

Determine whether the geometric-mean metric can remove the current implementation bottleneck associated with the general two-matter lapse ratio, and extract any additional falsification criterion for the future transition-wall evolution.

## 1. Mean gauge does not eliminate the lapse-ratio constraint

Torsello, *The mean gauges in bimetric relativity* (CQG 36, 235010; arXiv:1904.09297), defines the geometric-mean metric

`h = g (g^{-1} f)^{1/2}`

and its lapse `H` and mean shift `q`.

In the spherical/3+1 parametrization the gauge variables obey

`alpha^2 = H^2 lambda W`,

`alpha_f^2 = H^2 /(lambda W)`,

and therefore

`alpha = W alpha_f`,

with the same dynamical lapse ratio `W` fixed by preservation of the bimetric secondary constraint.

Equivalently, from Kocic-Lundkvist-Torsello (arXiv:1903.09646),

`W = - W_f/W_g`.

Therefore choosing a mean 1+log, mean maximal-slicing, or another gauge condition for `H` does **not** bypass the need to compute `W_g,W_f`.

Decision:

`MEAN_GAUGE_AS_LAPSE_SHORTCUT = REJECTED`.

## 2. What the mean gauge does give us

It gives a symmetric gauge choice that does not arbitrarily privilege either physical metric after `W` is known.

This is attractive for the JANUS-R wall because the research question itself is sector-relative.

A practical future choice is therefore:

1. evolve/fix the mean lapse `H` by a chosen mean gauge;
2. obtain `W=-W_f/W_g` from the secondary-constraint preservation law;
3. reconstruct
   `alpha = H sqrt(lambda W)`,
   `alpha_f = H / sqrt(lambda W)`;
4. derive the two shifts from the mean shift and separation parameter.

The exact gauge used for `H` should be selected only after the short one-fluid/twin-fluid regression works. A simple constant/controlled mean lapse is preferable for the first local wall experiment; mean 1+log can be tested later if singularity avoidance is needed.

## 3. New branch-sign criterion

For a real mean lapse `H`, with

`lambda = sqrt(1+p^2) > 0`,

the relation

`H^2 lambda = alpha alpha_f`

requires the product of the two physical lapses to be positive on a same-time-orientation foliation.

Hence

`W = alpha/alpha_f > 0`.

Using the secondary-constraint result,

`W = -W_f/W_g`,

our chosen mean-metric branch requires

`-W_f/W_g > 0`.

Thus the following are explicit transition-wall warnings/failures for this branch:

- `W_g -> 0` with `W_f != 0`: `W` diverges;
- `W_f -> 0` with `W_g != 0`: `W -> 0`;
- `W_g W_f > 0`: `W < 0`, incompatible with real same-oriented mean-lapse reconstruction;
- simultaneous `W_g,W_f -> 0`: degenerate case requiring separate analysis, not automatic regularity.

These conditions are more informative than monitoring either physical lapse alone.

## 4. Compact published form of the lapse coefficients

The general spherical result is

`0 = W_g alpha + W_f alpha_f`.

Kocic-Lundkvist-Torsello write

`W_g` and `W_f` as finite sums of

- non-derivative coefficients `c_i,d_i`;
- matter terms separated by `kappa_g` and `kappa_f`;
- first radial derivatives of the two angular metric functions.

The explicit published structure is

`W_g = lambda^2[...] + kappa_f lambda^2(c5+lambda c6)
       + kappa_g lambda^2[c7 + lambda^2 c9 + lambda(c8+p c10)+p^2 c11]
       + derivative terms`,

and

`W_f = lambda^2[...] + kappa_f lambda^2[d5 + lambda^2 d7 + lambda(d6+p d8)+p^2 d9]
       + kappa_g lambda^2(d10+lambda d11)
       + derivative terms`.

The coefficient sets obey the sector duality

`g <-> f`, `beta_(4-n) <-> beta_n`, `p <-> -p`,

under which

`W_g <-> -W_f`.

## 5. Upstream source localization

At pinned upstream revision

`nubirel/bim-solver@8852e8e9921edeeedf1a447d3bf27b82ec24433c`,

the one-fluid `include/eom-std/eomLapseRatios.h` has explicit `pfD/pfS/pftau` dependence only four times total:

1. monolithic `eq_gW`;
2. monolithic `eq_fW`;
3. runtime split coefficient `eq_gW_2`;
4. runtime split coefficient `eq_fW_2`.

The actual standard solver reconstructs

`W_g = Wg0 + r(Wg1+r Wg2)`,

`W_f = Wf0 + r(Wf1+r Wf2)`.

Therefore the explicit one-fluid matter dependence used at runtime is localized in the `W2` pair.

This makes a two-fluid extension tractable, but does not justify a hand-written replacement because the exact dual transformation also changes powers of `R=fB/gB` and the beta-index ordering.

## 6. Implementation ruling

Do not copy Appendix D by hand.

Preferred order when an executable GPL fork becomes available:

1. obtain the authors' machine-readable Mathematica ancillary source if possible;
2. generate the full two-matter `Wg2,Wf2` from that source;
3. preserve the existing geometric `W0,W1` machinery where the generated expressions agree;
4. validate exact sector duality numerically;
5. set f matter to zero and demand regression against the pinned upstream one-fluid lapse coefficients;
6. only then enable wall evolution.

If the ancillary files remain unavailable, a second-best route is to reconstruct only the **matter-dependent** coefficient block from the compact published `c_i,d_i` expressions and use symbolic algebra to apply/check the sector duality. Do not manually simplify the full generated C++ expression.

## 7. Dynamic wall acceptance criterion updated

A short wall evolution can be called `REGULAR` only if, over a resolution-convergent interval,

- both metric sectors remain nondegenerate;
- all Hamiltonian/momentum/secondary constraints converge;
- both fluid states remain physical;
- the bimetric square-root branch remains real;
- `W=-W_f/W_g` remains finite and strictly positive on the selected mean-time orientation;
- no unexplained `W_g/W_f` zero crossing occurs inside the compensation wall.

This criterion should be added to every future Gate A2 run table.

## Current verdict

`MEAN_GAUGE = RECOMMENDED_AFTER_W_IS_KNOWN`

`MEAN_GAUGE_BYPASSES_GENERAL_W = NO`

`W_POSITIVITY = NEW_EXPLICIT_BRANCH_GATE`

`GENERAL_TWO_MATTER_W_IMPLEMENTATION = STILL_OPEN`
