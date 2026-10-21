# JANUS Gate 2B — Step43: EXACT Ward/adjoint criterion and safeguards against a false local secondary

**21 October 2026 — branch \`research/gate2b-nonhomothetic-transfer\`.** Status: mathematically exact **FORMAL** Hamiltonian smearing audit and an executable numerical diagnostic for the physical kernel. **NO new claim of exact Hassan–Rosen/BD closure.** Gate 2B OPEN; JANUS-R NOT VALIDATED.

## 1. Critical distinction newly made executable

The Step33g/37 mixed Poisson kernel is the functional bracket of the original spherical ADM g/f Hamiltonians evaluated across all SIX canonical pairs. With independent smeared lapses \(N,M\), the formal integral is

\[
B[N,M]=\int dr\,\sum_{i,j=0}^2 N^{(i)}(r)\,K_{ij}(r)\,M^{(j)}(r).
\]

The earlier Step37/39 local secondary proxy is \(C=K_{00}-\partial_rK_{01}\). Very small numerical \(C\) on a spatial grid cannot by itself establish \(B[N,M]\approx0\) for arbitrary admissible lapses, let alone that the corresponding secondary is preserved in time.

Performing ALL formal integrations by parts on **N**, with compactly supported smears (or vanishing necessary boundary traces), gives the unique differential-operator coefficients

\[
B[N,M]=\int dr\,N\,\sum_{p=0}^{4}A_p(r)\,M^{(p)}(r)
\]

with the **exact universal identity**

\[
A_p=\sum_{\substack{0\leq i,j\leq2\\j\leq p\leq i+j}}
(-1)^i\binom{i}{p-j}\,\partial_r^{\,i+j-p}K_{ij}.
\]

This formula checks every coefficient of \(M,M',M'',M''',M''''\); it forbids silently dropping high-smearing jets. An exact physical reduction \(B[N,M]=\int NCM\) requires **all** five operator identities \(A_p-\delta_{p0}C=0\), including the high-jet coefficients, modulo well-defined boundary conditions.

For the restricted five-coefficient class \(\{K_{00},K_{01},K_{10},K_{11},K_{20}\}\) encountered in earlier JANUS numerical calculations (with \(K_{02}=K_{12}=K_{21}=K_{22}=0\)), define

\[
C=K_{00}-K_{01}',\qquad
W=K_{01}-K_{10}+K_{20}',\qquad
D=K_{20}-K_{11}.
\]

Then the **exact** formal identity is

\[
\boxed{B[N,M]=\int dr\,N\,\big[C\,M+(WM)'+(D M')'\big].}
\]

Therefore **\(C=0\) is NOT by itself sufficient**. It is sufficient, under the stated sparsity and boundary hypotheses, to prove \(C=W=D=0\). More complicated non-sparse kernels might still have cancellations in the five \(A_p\) terms; the particular sparsity assumption is a sufficient **path** to reduction, not a logically necessary property for every theoretical kernel.

The previous Step37/39 empirical controls \(K_{11}\approx K_{20}\) and \(W\approx0\) were finite-derivative numerical checks. Step43 **does not silently promote these to exact physical identities**. An analytical physical-kernel proof or rigorous interval calculation remains pending.

## 2. Exact counterexamples: false-zero secondary can be exposed

The new \`numerics/hr_step43_ward_operator.py\` constructs the exact formal adjoint using SymPy and, on compact polynomial lapse pairs \(N=(r-a)^4(b-r)^4\) and independent \(M\), integrates rational polynomials **exactly** (no floating tolerance). Manufactured kernels demonstrate:

- An exactly Ward-closed nontrivial \(K_{11}=K_{20}=1+r^3\) example with \(W=D=0\) has identical original and \(C\)-only integrated brackets for different lapse choices. An explicit positive control gives **both integrals exactly** \(10753/21358810497024000\).
- A kernel with \(C=0\) and **\(W=-r\neq0\)** has an exactly NONZERO original integrated bracket while its \(C\)-only bracket is identically zero.
- A kernel with \(C=W=0\) and **\(D=-1\neq0\)** likewise has a nonzero original integrated bracket.
- A kernel with \(C=W=D=0\) but **\(K_{22}=1/7\)** produces an explicitly nonzero \(M''''\) adjoint coefficient, and the original smeared bracket is nonzero.
- Non-compact lapse test functions can leave unaccounted boundary terms. The required compactness/boundary assumptions are tested separately.

These are **abstract mathematical countercontrols**, NOT counterexamples to the specific JANUS theory. Their purpose is to prevent a faulty implementation from accepting a false BD-secondary proof.

## 3. Instrument to inspect the ACTUAL HR kernel; physical run is still PENDING

The new \`numerics/hr_step43_physical_ward_gate.py\` is a numerical diagnostic which, on a genuine \`CurvedPrimary\` witness, calls the **existing** \`numerics.hr_step37_curved_solver.kernel_fast\` (full six-canonical-pair mixed functional bracket) and returns, at a chosen interior radius:

\`\`\`text
C = K00 - five_point_d_dr(K01)
W = K01 - K10 + five_point_d_dr(K20)
D = K20 - K11
K02, K12, K21, K22 individually and max absolute value
\`\`\`

It also compares the **full nine-jet Gaussian smeared integral** to the separately integrated \(NMC\) approximation, and reports the discrepancy, sampled max \(|W|\), \(|D|\), excluded high coefficients. Finite five-point derivatives and 48/96 Gauss quadratures cannot prove exact identities.

\`scripts/verify_gate2b_step43.py\` provides deliberately **distinct** modes:

\`\`\`bash
# RUN and verified, no physical JANUS provider imported:
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step43.py --selftest

# NOT YET RUN: Requires an authentic coherent Step33g/37/39 GitHub worktree:
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step43.py --physical \
  --output /tmp/janus-step43-physical-report.json
\`\`\`

The real mode constructs the Step39 degree-4, six-correction, \(h=.001\) curved/noncomoving two-positive-dust near-secondary initial data, samples seven radii, and runs two independent Step39 compact lapse pairs A and B. **The command exists and is checked into GitHub, but was not executed with the actual model providers this turn.** A selftest result must NEVER be confused with a physics result.

## 4. Executed tests and exact provenance

Local isolated execution in \`/mnt/data/janus-step43\`:

\`\`\`bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step42_center_regular_interval.py \
  tests/test_hr_step43_ward_operator.py \
  tests/test_hr_step43_physical_ward_gate.py

# ACTUAL: 40 passed in 3.53 seconds (17 Step42 + 16 Step43 formal + 7 instrumentation).
\`\`\`

The following **five new executable files were checked against their actual executed Git blob hashes and GitHub**:

- \`numerics/hr_step43_ward_operator.py\` \`fd91411ad6cec88d88f0889ccf99a5f070ccbb54\`
- \`tests/test_hr_step43_ward_operator.py\` \`04825a5034421fc1e12dd51ba361d81cfbd5b753\`
- \`numerics/hr_step43_physical_ward_gate.py\` \`386febaa9b805cf423efd6feb7a8027a2069301b\`
- \`tests/test_hr_step43_physical_ward_gate.py\` \`c9eea74b6b14eef81d0816d960b10f9744e0b8b9\`
- \`scripts/verify_gate2b_step43.py\` \`98ae82adaad17e8be9240ceed51ddfe2e141a476\`.

The historic Step42 source and tests were ALSO byte-exact GitHub blobs. The local Step41 report was manually reconstructed with the complete authentic schema, actual nine coefficients, true coefficient SHA-256 and all relevant fields: it is **semantically consistent with the real GitHub report, but NOT byte-identical to that report** (\`fcb887e89f8723e5ddbbbceb2755420586a3dda8\` local vs \`16c8de6ee66725622c40ba2f327c8aafa99a5cb7\` original). All 17 Step42 tests pass with this complete-schema copy. This is **not** a full branch checkout or a live authentic-provider regression of the Step41 numerical profile. Direct shell GitHub clone is unavailable due to DNS in the runtime; GitHub Actions stay disabled.

Runner's standalone \`--selftest\` passed. Example numerical residuals are \(|W|\approx3.33\times10^{-16}\), full-versus-reduced smeared difference \(\approx-9.90\times10^{-25}\) **FOR A MANUFACTURED POLYNOMIAL**, not JANUS.

## 5. Precise next blocking tasks (Step44)

1. **RUN THE ACTUAL PHYSICAL GATE:** obtain a coherent, BYTE-IDENTICAL Step33g/37/39 worktree, run \`--physical\` above. Vary \(h\), Gaussian order and two independent compact lapse pairs. Commit machine report with all \(K_{ij}\) and \(C,W,D\), and be willing to record nonzero obstructions.
2. Prove physically whether \(K_{02}=K_{12}=K_{21}=K_{22}=0\), \(D=0\), \(W=0\) EXACTLY, or determine complete adjoint \(A_p\) cancellations from the **original** two-dust HR spherical canonical action. Numerical near-zero alone does not count.
3. Derive \((K_{01})'(r)\) analytically or with certified intervals; solve or rule out \(C_{\rm local}(r)=0\) on a NONTRIVIAL radial continuum preserving the already proved positive normalized dust momenta and restricted centre parity. Do not equate a fitted polynomial's nine-point residual with a continuous exact solution.
4. Then compute the **time preservation** of the exact secondary under \(H_{\rm tot}\) with ALL six canonical pairs and all boundary terms, full Dirac rank and actual lapse fixing. Only after that genuinely nonhomothetic on-shell physics, same-action De Felice and Aoki oracles, fold and observations.

**FINAL:** Step43 formal Ward/adjoint algorithm and negative controls EXACT; actual HR Ward/Dirac preservation NOT PROVED; full physical test PENDING. Gate 2B OPEN; JANUS-R NOT VALIDATED. Do not conflate this with the separate sign-reversed f-EH external JHR manuscript.
