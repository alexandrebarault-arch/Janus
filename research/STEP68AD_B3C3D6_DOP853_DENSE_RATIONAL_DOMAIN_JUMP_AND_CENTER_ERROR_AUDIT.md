# JANUS b3c3d6 — DOP853 dense polynomial: exact rational domain, continuous-defect interface, jump budget (2026-10-30)

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.** This is a reproducible numerical-certification **infrastructure advance**, not a physical certificate for Step55/58.

## Original physical inputs and traceability

At start, GitHub branch HEAD was `cead29825bfce907f33a30b34decdb21cf347002`; the current `00_CURRENT_RESTART.md` and `research/AUTOMATION_STATE.json` were read. Original Step55 normalization `numerics/hr_step55_normalized_secondary.py` blob `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, original outward 256-cell barrier `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, original Step58 operator `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, and the physical four-radius report `research/reports/b3c3d6_original_step58_four_radius_physical_replay_summary.json` blob `ae221dab8e9f4eb0550fee617ba57f4850cff911` were read from the connector. The previously authenticated Step45/46 blobs remain `66aa43841dccfe4a5d586a49be9c10af3a67a10e` and `bac025c28dbe1561c0c36c56dbfda46dc326f804`. These original physical modules were **inspected but NOT executed in this session**.

## New exact rational numerical result

SciPy DOP853 stores scalar dense output as a degree-at-most-seven polynomial in `x=(s-t_old)/h`, with binary64 `F` and `y_old`. The module reconstructs that mathematical polynomial with `Fraction.from_float` and exact rational polynomial arithmetic. For the **true binary64 step** `[t_old,t]`, the right polynomial coordinate is `xmax=(t-t_old)/h`, **not necessarily 1**, because `h=fl(t-t_old)`. Therefore a continuous defect certificate must use `[0,xmax]` and must separately bound exact rational jumps between adjacent reconstructed polynomials at shared binary64 step times. Otherwise a residual-only global error estimate can silently ignore an interpolation discontinuity.

A real SciPy DOP853 **toy** `y'=(sin(s)+y)/(1+s)` on `[1e-4,0.7225]` with `rtol=1e-12,atol=1e-14` yielded **8 dense steps**; **1 exact endpoint mismatch**, `t_old+h-t=45/73786976294838206464 ≈ 6.098637220230962e-19`; and **1 nonzero exact rational inter-piece jump** among 7 boundaries, with maximum absolute jump `≈1.2781027279428647e-20`. These are **toy** facts about the exact rational reconstruction, not physical Step55 errors. The tests compare reconstruction to actual SciPy dense evaluation, and verify the gap/jump logic.

The new `interval_step_defect` covers each *true* binary64 step by rational subcells, Bernstein-encloses the exact polynomial and its derivative, and evaluates `H=2s P_s-G(s,P)+2P` using a caller-provided **outward** interval extension of G. The physical adapter `physical_step55_dense_defect` explicitly invokes the original Step55 outward integer `I`/G engine and rejects a polynomial enclosure that exits the original `Ustar±1/10000` tube. This adapter has **not** been executed against physical Step55 DOP853 dense pieces here. A future physical run must check every step, every inter-piece jump, the initial-error budget, and propagation into Step58. Bernstein on the polynomial alone does **not** enclose non-polynomial G; G must be interval-evaluated.

## Exact conditional center initial-error lemma

For `2s U_s=G(s,U)-2U`, a regular center branch `U(0)=P(0)`, a common tube, `G_U≤g<2`, and `|G(s,P)-2P-2sP_s|≤C s^p` **continuously** on `(0,s0]` with `p>0`, the integrating-factor comparison gives

`|U(s0)-P(s0)|≤C s0^p/(2p+2-g)`.

Proof: for `e=U-P`, `2s e_s=(G(s,U)-G(s,P))-2e+H`; the upper Dini derivative of `|e|` is bounded by `-((2-g)/(2s))|e|+C s^(p-1)/2`. Integrate from the regular center, where `e(0)=0`. For the archived **conditional** Step55 bound `g=-99/100`, `p=3`, `s0=1/10000`, the factor is `100/899`: `|e(s0)|≤(100/899) C 10^-12`. A toy `G=-U+3s^3, P=0` saturates this bound. **No physical C for Step55 has been certified**; this is not yet a numerical initial-error bound. Binary64 initialization and abscissa transport errors must be added separately.

## Tests and scope

Local command `cd /mnt/data/janus_oct30_new && PYTHONPATH=. python -m unittest discover -s tests -v`: **9 PASS, 0 FAIL** (actual SciPy DOP853 dense pieces, rational algebra, Bernstein, interval toy, gap/jump guard, conditional center lemma). `python -m compileall -q numerics tests`: **PASS**. Local Git blob SHA: module `b1c8909983171b7161b28e68ca442d9a17c21cfc`; tests `23e38ce06e5d596cd48ce1c12923c0902837238a`. Both were published via authenticated GitHub writes and checked against local tested bytes.

**Still missing:** actual Step55 dense-piece coefficients and full outward interval residual on every step; certified physical initial Taylor residual constant C, binary64 initial error and jump accumulation; Step58 interval enclosures for all six A/B/E, exact factorization of B/E, positive lapse BVP at two true boundaries; complete Dirac/rank/charges/time gauge, 4D dynamics, stability and observables. Numerical four-radius Step58 replay from the preceding checkpoint remains valid as **numerical only**. No changes to `main`, `research/v2-flrw`, or disabled workflows.
