# JANUS — Step55: global invariant radial barrier and continuous positive two-dust constrained initial data

**23 October 2026. Scientific work branch: research/gate2b-nonhomothetic-transfer. Gate 2B OPEN. JANUS-R NOT VALIDATED.**

## 1. Exact result and scope

The original positive-EH spherical Hassan–Rosen canonical action with two moving dusts produced an exact six-canonical-pair local secondary \(C=K_{00}-(K_{01})'\) in Step45 and its primary-reduced radial equation in Step46. The analytic local regular-centre branch was established conditionally on prescribed regular background data in Step49. Exact quadratic-algebraic coefficients \(U_1,U_2\) followed in Steps52–53. Step54 independently certified continuum positivity for an explicit tube of normalized canonical variables but did NOT prove the exact radial solution lies in that tube.

**Step55 now proves this missing tube-membership property for the regular analytic constrained radial solution on the entire real interval \(0\le r\le0.85\).**

Put \(s=r^2\), \(P=p_{L_f}(r)=r^2U(s)\), and \(V=P'(r)/r\). Define the exactly algebraic reference polynomials

\[
U_*(s)=U_0+U_1s+U_2s^2,\qquad V_*(s)=2U_0+4U_1s+6U_2s^2.
\]

The original primary-reduced secondary equation, after exact symbolic removal of spherical powers, takes the normalized form

\[
V=G(s,U),\qquad 2sU_s=G(s,U)-2U,
\]

with the regular centre identity \(G(0,U)=3U_0-U\). The new integer-rational interval certificate proves, for this exact regular-centre branch and the fixed analytically prescribed benchmark data,

\[
\boxed{|U-U_*|\le0.0001,\qquad -0.00205<V-V_*<0.00205}
\]

at **every real \(s\in[0,0.7225]\)**. These are real continuum bounds, not sampled numerical ODE residuals.

As both tolerances are strictly inside the previous Step54 \(0.01\) conditional positivity tube, its independently established inequalities now apply to the **actual exact constrained radial branch** throughout the interval:

\[
\boxed{p_g/r^2>0.8854,\quad p_f/r^2>0.063,\quad J>0.659,\quad K/r^2>0.229.}
\]

The two original dust lapse denominators, \(S_f'\) and \(\sqrt{1-z^2}\), also remain positive under the same certified conditions. At the spherical centre, use their regular normalized limits. **This result is for the reduced constrained radial initial-data sector only**, not full tensorial four-dimensional geometry or time evolution.

## 2. Physical source identity, original files and mathematical assumptions

The new normalized kernel is in numerics/hr_step55_normalized_secondary.py. It imports the TRUE historical source files, refuses any SHA drift, and performs exact SymPy rational cancellation before setting \(s=r^2\):

- numerics/hr_step45_exact_physical_ward.py — original blob 66aa43841dccfe4a5d586a49be9c10af3a67a10e.
- numerics/hr_step46_exact_secondary_ode.py — original blob bac025c28dbe1561c0c36c56dbfda46dc326f804.

The substitution uses regular original canonical parities \(S_i=rL_i\), \(p_{L_i}=r^2U_i\), \(p_{S_i}=rV_i\), \(p_i=r^2\rho_i\), relative shift \(z=r z_1\), \(D_g=r^3\bar D_g\), and \(W_f=r^2\bar W_f\), plus consistent spherical derivatives and dust phase gradients. Positive square-root branches are those of the original action, with \(L_f,S_f'\) and all required denominators positive on the fixed chart. The new normalized RHS contains no leftover \(r\), and direct interval evaluation of the independent UNNORMALIZED original Step46 physical expression at three radii contains the more precise normalized enclosures.

The calibration decimals, including the mass parameters and interaction coefficients, are treated as exactly rational input, with the positive algebraic background \(H=\sqrt{H^2}\); the Step52/53 exact \(U_1,U_2\) are enclosed by their certified rational endpoints. The prescribed remaining g-sector and metric backgrounds and dust phase gradients are real analytic in \(s\).

## 3. Rigorous scalar first-exit comparison and derivative check

Set \(\delta=1/10000\) and the two barrier functions \(U_\pm=U_*\pm\delta\). On the upper/lower walls define

\[
F_+(s)=G(s,U_+)-2U_+-2sU_*'(s),\quad
F_-(s)=G(s,U_-)-2U_--2sU_*'(s).
\]

The executable program numerics/hr_step55_global_barrier.py partitions **the full real interval** \(s\in[0,0.7225]\) into 256 closed rational cells and encloses each whole cell in a \(10^{-28}\) integer lattice using outward rounding for every sum, multiplication, inverse, integer power, and square root. It obtains the following **exact strict rational margins**:

\[
F_+(s)\le-\frac{1480966474499367232302129}{10000000000000000000000000000}<0,
\]

\[
F_-(s)\ge\frac{295653233337826329055403}{2000000000000000000000000000}>0.
\]

The analytic Step49 centre solution begins at \(U(0)=U_*(0)=U_0\), strictly between the walls. A first exit through the upper wall at any \(s>0\) would require a nonnegative derivative of \(U-U_+\), contradicting \(2s(U-U_+)'=F_+<0\). The lower first exit analogously contradicts \(F_->0\). Original rational chart denominators remain nonzero and the normalized right-hand side smooth on this compact interval; standard ODE continuation therefore extends the locally analytic regular solution through the endpoint, inside the barrier.

The **derivative is checked separately**. For every \(U\) in this barrier rectangle, each cell encloses \(G(s,U)-V_*(s)\) by the rational bounds

\[
-\frac{10209601928354599272595789}{5000000000000000000000000000}
\le V-V_*
\le\frac{20404447710211286903383733}{10000000000000000000000000000}.
\]

These are inside \((-0.00205,+0.00205)\), hence well inside Step54's required \(0.01\) derivative tube. A deliberately wider trial \(\delta_U=0.001\) was **rejected** by the derivative guard despite the U barrier signs; the code does not falsely equate a U-only barrier with full two-variable positivity. Refinement to 512 cells tightens the barrier margins.

The inequalities cover continuum cells, NOT 256 independent sample points. Outward rounding is computed with exact integer division and integer square roots and refuses intervals containing a forbidden denominator zero or negative radicand.

## 4. Actual execution and source hashes

**12 tests passed locally in 3.85 seconds**, in the isolated Python directory /mnt/data/janus-step55, using byte-for-byte copies of both historical Step45/46 files (verified by git hash-object). Targeted command:

    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step55_global_barrier.py

Runnable certificate:

    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step55_global_barrier

The three new source/test blobs were compared against the actually executed local files and are **identical**:

- numerics/hr_step55_normalized_secondary.py — a54a6acf2f7ad2f64c500faecfa1406ecbf7b862.
- numerics/hr_step55_global_barrier.py — a6e7004120d0a166a3a8973c2fbe1487a8eb70fe.
- tests/test_hr_step55_global_barrier.py — 5dfb8036c66c9b2774847b0989be15ea41c65408.

Tests cover source pinning and tamper refusal, rational interval arithmetic with negative denominators and radicals, complete rational coverage of the interval, the exact normalized centre identity, strict inward barriers and independent \(V\) enclosure, a finer-grid monotonicity control, false-success rejection for overly wide U tube, illegal inputs, and an independent evaluation of the original unnormalized physical Step46 RHS at three interior radii. The separately executed Step54 conditional sign-certificate suite previously passed 9 tests, but there was **no whole-repository regression** or GitHub Actions workflow this turn; Actions remain intentionally disabled.

The full machine summary with exact fractional margins and all limitations is in research/reports/gate2b-step55-report.json. An independent raw local execution JSON has SHA-256 4f22328452d36ee252f966fbe6a1fa476e7aaba8daee43ec9d555b11619f0cfd. That raw file is locally generated and **not a separate GitHub upload**.

## 5. Real remaining physics gate: TEMPORAL Dirac, not radial dust signs

**Radially closed on the prescribed benchmark:** analytic local regular secondary centre, exact initial Taylor coefficients, full-interval invariant barrier, and strictly positive original two-dust initial-data momenta and J/K chart.

**Still OPEN:** the full six-canonical-pair time preservation \(\{C,H_{\rm tot}\}\), consistent elimination/variation of the algebraic relative shift in time, fixing of the lapse ratio, functional boundary terms, the true Dirac constraint rank, exceptional J/K-zero sectors, full 4D Cartesian tensor-density centre regularity, a truly time-evolved nonhomothetic cosmology, perturbation stability and ghost-freedom. The spatial proof does NOT establish a successful full Dirac algorithm, and no such claim should be made.

**NEXT STEP56:** use the now certified positive radial branch to derive and test the actual temporal Dirac algorithm, with original six canonical pairs and lapse multipliers; independently audit it against original non-integrated action densities. Retain all errors and partial results even if an obstruction is found. Do not reactivate GitHub workflows.

**Repository:** work only on research/gate2b-nonhomothetic-transfer and update 00_CURRENT_RESTART.md. Older main and V2 heads are already preserved in this branch's ancestry (commit 4f7a3a1), and the historical PR #1 was closed unmerged. Three named branches remain and main remains the default until the owner changes the default and deletes two refs via GitHub UI; the connected tools cannot perform those administrative operations.

**Verdict: Step55 global RADIAL initial-data existence and positive dust tube confirmed for fixed benchmark. GATE_2B OPEN, JANUS-R NOT VALIDATED.**
