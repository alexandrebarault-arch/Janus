# JANUS — Step 33a: true spherical ADM Legendre transformation and HR relative-shift primary interface

**Date:** 2026-10-19. **Active branch:** `research/gate2b-nonhomothetic-transfer`.
**Result:** `SPHERICAL_ADM_LAPSE_AFFINITY=GREEN` and `SPHERICAL_RELATIVE_SHIFT_EQUATION_LAPSE_INDEPENDENT=GREEN` **for a strictly spherical canonical field-density identity**.
**Open:** `HR_BD_SECONDARY=NOT_DERIVED`, `FULL_4D_SCALAR_GAUGE_CLOSURE=NOT_DERIVED`, `DE_FELICE_AOKI=NOT_RUN`, `NONHOMOTHETIC_ON_SHELL=NOT_FOUND`, `GATE_2B=OPEN`.

## Why this step was necessary

Step 32e made all 18 compact scalar metric/dust trial fields time-integrable on the **physically homogeneous**, radiation-free, two-dust Candidate-C background. The finite-basis 4×4 Schur of Step 32c is **not** a true canonical lapse/shift constraint and is not a Boulware–Deser (BD) null elimination. Before trying to interpret kinetic eigenvalues, the correct canonical ADM variables and shift structure must be derived.

This step therefore uses a different, more fundamental interface: **unprojected spherical ADM field values and their exact radial derivatives**, not a truncated Hessian. It recovers the gravitational EH momenta via an exact local Legendre transformation, supplies the spherical Hamiltonian/momentum constraint densities, includes **both independently canonical dust matter densities**, and **explicitly redefines the bimetric relative shift** so the exact five-beta HR potential becomes *affine in both ADM lapses*.

The derivation holds at arbitrary positive metric data within the real square-root branch and is not tied to fitted Candidate-C background values. That makes it a reusable structural acceptance oracle for the future full time-dependent scalar constraint calculation. It **does not** independently validate a new background or the full BD secondary constraint.

## ADM geometry and positive-EH Legendre map

Use each spherical metric in its own common-time ADM form:

\[
 ds^2=-N^2dt^2+L^2(dr+Vdt)^2+S^2d\Omega^2,
 \qquad L,S,N>0.
\]

The positive-sign Einstein–Hilbert ADM+GHY density **per unit solid angle**, with the usual prefactor \(M^2/2>0\), is

\[
 \mathcal{L}_{EH}=\frac{M^2}{2}NL S^2
 ({}^{(3)}R-4K_rK_t-2K_t^2),
\]
\[
 {}^{(3)}R=\frac{2}{S^2}\left[1-\left(\frac{S'}L\right)^2
 -\frac{2S}{L}\left(\frac{S'}L\right)'\right],
\quad
 K_r=\frac{\dot L-VL'-LV'}{NL},\quad
 K_t=\frac{\dot S-VS'}{NS}.
\]

The canonical radial and area momenta are **exactly**

\[
 p_L=-2M^2S^2K_t,\qquad
 p_S=-2M^2LS(K_r+K_t).
\]

The full Legendre transformation and a radial integration by parts yield, modulo compact radial boundary terms,

\[
\mathcal H_{EH}=NC_{EH}+VD_{EH},
\]
\[
 C_{EH}=\frac{Lp_L^2}{4M^2S^2}-\frac{p_Lp_S}{2M^2S}
           -\frac{M^2}{2}LS^2\,{}^{(3)}R,\qquad
 D_{EH}=p_SS'-Lp_L'.
\]

This is a **true ADM spherical field-density** Hamiltonian identity, not a finite-matrix Schur inverse. A separate explicit test integrates the compact radial derivative identity

\[
 \int dr\,[V(p_LL'+p_SS')+V'Lp_L]
 =\int dr\,V(p_SS'-Lp_L')
\]

with a zero boundary term. The test suite also finite-differentiates the original nonlinear EH Lagrangian to recover the two momenta and inverts the Legendre map independently.

## Two real dust canonical pairs, preserved

Each separately coupled pressureless irrotational dust sector has already undergone its **exact** covariant-to-canonical Legendre reduction, with its density multiplier eliminated after the Legendre map. In true ADM radial variables:

\[
 \mathcal H_{dust,i}=N_i\underbrace{p_i\sqrt{1+\theta_i'^2/L_i^2}}_{C_{dust,i}}
 +V_i\underbrace{p_i\theta_i'}_{D_{dust,i}}, \quad p_g,p_f>0.
\]

This keeps \((\theta_g,p_g)\) and \((\theta_f,p_f)\) **distinct**, rather than setting a dust clock on shell inside the Lagrangian before variation. It makes each matter sector affine in its *own* true ADM lapse and shift. **However**, after the HR relative-shift redefinition the \(g\)-matter radial constraint appears in both lapse coefficients. That is an expected gravitational coupling and **does not** merge the two dust canonical pairs.

An early regression test incorrectly expected changing \(p_g\) to leave the \(f\)-lapse coefficient unchanged. It failed, exposing the legitimate term \(zD_g/L_f\); that assertion was corrected and replaced with an exact check of the predicted cross-coupling. One finite-difference lapse-gradient tolerance was also relaxed slightly to allow floating-point subtraction, with the exact algebraic affine identity retained unchanged.

## All-five-beta exact spherical HR lapse affinity

Write both ADM metrics as above and introduce the positive angular radius ratio \(\ell=S_f/S_g\). Define the beta combinations

\[
 A_0=\beta_0+2\beta_1\ell+\beta_2\ell^2,\quad
 A_s=\beta_2+2\beta_3\ell+\beta_4\ell^2,\quad
 A_\tau=\beta_1+2\beta_2\ell+\beta_3\ell^2.
\]

The exact principal radial 2×2 square-root invariants are

\[
 s=\frac{N_fL_f}{N_gL_g},\qquad
 \tau=\sqrt{\left(\frac{N_f}{N_g}+\frac{L_f}{L_g}\right)^2
 -\left(\frac{L_f(V_g-V_f)}{N_g}\right)^2}.
\]

The exact interaction density is

\[
 \mathcal L_{HR}=-m^2M_g^2S_g^2
 \left[N_gL_g A_0+N_fL_f A_s
 +A_\tau\sqrt{(N_gL_f+N_fL_g)^2-(L_gL_f(V_g-V_f))^2}\right].
\]

This nontrivial square root is **not generally affine** in lapses when the *old* \(V_g,V_f\) are held fixed. Make the explicit **relative shift redefinition**

\[
 V_f=V,\qquad V_g=V+\left(\frac{N_g}{L_g}+\frac{N_f}{L_f}\right)z,
 \quad |z|<1.
\]

Then, holding \(V,z,L_i,S_i\) fixed, the exact interaction Hamiltonian \(-\mathcal L_{HR}\) is

\[
 \mathcal H_{HR}=N_gW_g(z)+N_fW_f(z),
\]
\[
 W_g=m^2 M_g^2 S_g^2\big[L_gA_0+L_f A_\tau\sqrt{1-z^2}\big],
\]
\[
 W_f=m^2 M_g^2 S_g^2\big[L_fA_s+L_g A_\tau\sqrt{1-z^2}\big].
\]

The complete spherical canonical Hamiltonian density, including the two dust species, therefore becomes

\[
 \mathcal H=N_g\big[C_g+zD_g/L_g+W_g\big]
 +N_f\big[C_f+zD_g/L_f+W_f\big]
 +V(D_g+D_f).
\]

Here \(C_i=C_{EH,i}+C_{dust,i}\) and \(D_i=D_{EH,i}+D_{dust,i}\). The canonical \(N_g,N_f,V\) are **actual Lagrange multipliers in this spherical first-order Hamiltonian density**, unlike the earlier component perturbation \(\Phi\) in a finite Galerkin Hessian. The two constraint coefficients and common-shift coefficient are **lapse independent at fixed \(z\)**.

Furthermore, variation of \(z\) factorizes:

\[
 \frac{\partial\mathcal H}{\partial z}
 =\left(\frac{N_g}{L_g}+\frac{N_f}{L_f}\right)
 \left[D_g-\mathcal K\frac{z}{\sqrt{1-z^2}}\right],\qquad
 \mathcal K=m^2M_g^2S_g^2L_gL_f A_\tau.
\]

Consequently on nondegenerate regular branches where \(\mathcal K\neq0\), the algebraic shift equation is **independent of both lapses**. Solving it gives

\[
 z=\mathrm{sgn}(\mathcal K)\frac{D_g}{\sqrt{D_g^2+\mathcal K^2}}.
\]

When \(\mathcal K=0\) the system degenerates and its constraints must be considered separately; no arbitrary \(z\) root is invented.

### Diagnostic values, not observables

At an arbitrary admissible, **off-shell** spherical sample with \(M_g^2=1.8\), \(M_f^2=.91\), \(m^2=.67\), \(\boldsymbol\beta=(.21,.78,-.35,.16,.11)\), and positive sample canonical dust momenta:

```text
C_g                     -0.2597594014987879
C_f                     +0.4376153019917649
D_g                     -0.3438200000000000
D_f                     +0.3104320000000000
D_diagonal              -0.0333880000000000
z from lapse-free eq.   -0.8408245009767221
z equation residual     +1.1102230246251565e-16
H coefficient of N_g    +0.9937352307773410
H coefficient of N_f    +0.9021031542323786
```

These sample values **do not solve** the Hamiltonian constraints; they certify structural identities at an arbitrary field point. They are NOT the physically homogeneous Candidate-C background or the genuinely nonhomothetic solution sought by Gate 2B.

## Reproducibility and independent checks

New committed source/test:

- `numerics/hr_spherical_adm_primary.py` — source of exact EH Legendre map, spherical constraints, all-beta HR lapse-affine redefinition, relative-shift equation, and both independent dust terms.
- `tests/test_hr_spherical_adm_primary.py` — **21 passing focused tests** including independently constructed 2×2 inverse-metric HR principal-root oracle, finite derivatives of original EH Lagrangian and HR potential, explicit compact radial boundary/IBP, beta0/beta4 decoupling, both matter terms, shift-solving and degeneracy guards.
- `scripts/verify_gate2b_step33a.py` — JSON provenance runner, focused tests only.

To reproduce in a complete repository checkout (with NumPy and pytest):

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33a.py gate2b-step33a-report.json
```

The **21 tests were executed in a NEW standalone local workspace** `/mnt/data/janus33`; earlier 93 Step31–32e focused tests were **NOT** rerun here. No claim of 114 combined tests. Source fingerprints are reported in the JSON. The complete clean GitHub checkout/full suite and independent peer reproduction remain separately unverified.

## Exact next blockers and scientific limits

1. **Derive the spherical HR BD secondary** from time preservation of the primary Hamiltonian combination. Calculate the relevant Poisson brackets, boundary terms and possible lapse-fixing, **with both dust phases retained**. The lapse-linear identity is necessary but not sufficient to show the BD ghost is absent after coupling and background evolution.
2. Link this **unprojected spherical ADM field-density** to the full Step32e common-time nonlinearly perturbed on-shell action, verifying canonical momenta of each radial/angular metric function, spatial derivatives, genuine ADM lapses/shifts and time-dependent gauge generators. Spherical symmetry alone does **not** capture the full four-dimensional helicity-0 perturbation symbols.
3. Find or explicitly exclude a **physically nonhomothetic on-shell** two-metric/two-dust background beyond the Step30 passive coordinate compensation. Enforce all local metric, relative Stückelberg and dust Euler equations, including boundary and time transport.
4. Reproduce BOTH **same-constrained-action** physical scalar benchmarks: finite-H `mu→0` De Felice principal speed, and homothetic nonlinear Aoki `K_S,c_S²` stable/unstable branches; only then test the Candidate-C first relative-mu fold `a≈0.0301646`.

**Research disposition:** this is the first explicit *local spherical Hamiltonian* lapse/relative-shift identity in the present Step31–32e progression. It corrects an earlier dependence on a restricted lapse-amplitude Schur. **It does not pass Gate 2B or establish JANUS-R stability.**
