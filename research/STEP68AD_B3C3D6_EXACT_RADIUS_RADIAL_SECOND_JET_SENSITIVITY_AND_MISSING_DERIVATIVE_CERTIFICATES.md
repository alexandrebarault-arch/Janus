# b3c3d6 — second radial jet at the exact outer radius (31 October 2026)

**Verdict: PARTIAL / conditional exact algebra; GATE_2B OPEN; JANUS_R NOT_VALIDATED.**

## Source provenance and scope

Read through the connected GitHub repository on `research/gate2b-nonhomothetic-transfer`:
- `numerics/hr_step55_normalized_secondary.py` Git blob `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`;
- `numerics/hr_step46_exact_secondary_ode.py` Git blob `bac025c28dbe1561c0c36c56dbfda46dc326f804`;
- `numerics/hr_step55_global_barrier.py` Git blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`;
- `numerics/hr_b3c3d6_physical_correlated_replay.py` Git blob `47a0c80cea2554daf62f3fea9ffb7f28421ae22c`;
- `numerics/hr_b3c3d6_exact_radius_prefix_ledger.py` Git blob `bb88b8eb407ca4b2c05f43d5bc1862544ceb4391`.

No original physical Step45/46/55/58 engine was rerun in **this** session. The already-published exact-radius prefix ledger is used as a **conditional** input. The earlier physical DOP853 endpoint `s_b` lies **outside** the certified Step55 domain and remains uncertified as a physical endpoint.

## Exact new radial identity

For `s=r^2>0`, `pLf(r)=s U(s)`, `2s U_s=G(s,U)-2U`, set
`F(s,u)=(G(s,u)-2u)/(2s)`. The **ODE-consistent**, not dense-polynomial, second radial derivative is

```text
pLf'(r)/r = G(s,U),
pLf''(r) = 2U + 10s F(s,U) + 4s^2 U_ss
          = G(s,U) + 2s G_s(s,U) + G_U(s,U)*(G(s,U)-2U).
D(s,u) := G + 2s G_s + G_U*(G-2u)
D_U = G_U*(G_U-1) + 2s*(G_sU + G_UU*F).
```

These identities follow by differentiation of the Step55 equation, without assuming the DOP853 dense polynomial satisfies the ODE. SymPy checked the three general symbolic residuals exactly.

For `|U(s)-P(s)|<=eps`, with both values and their connecting segment in one certified convex `u`-tube, assume **outward-certified** `G_U in [glo,ghi]`, `|G_sU|<=Lsu`, `|G_UU|<=Luu`, `|F|<=Mf` on that segment. The mean-value theorem gives the exact conditional budget

```text
|pLf''(r) - D(s,P(s))|
 <= eps * [ max_{g in [glo,ghi]} |g(g-1)| + 2s*(Lsu+Luu*Mf) ].
```

The quadratic maximum is obtained exactly from the endpoints and the possible vertex `g=1/2`. This is a **bound on the physical ODE jet**, not `d²(sP)/dr²`.

## Known physical input and precise missing term at r=17/20

At `s*=289/400`, the prior conditional prefix bound gives `eps≈4.849547003502490e-6`; inherited `G_U` enclosure is `[-1.0010994328099383,-0.9939716062572771]` (exact rational constants in code). Thus

```text
|pLf''(r*)-D(s*,P(s*))|
 <= 9.715095122174026e-6
    + 7.007595420061098e-6 * (Lsu + Luu*Mf).
```

The first term and the multiplier are computed from exact fractions, with displayed decimals only for readability. **Lsu, Luu, Mf have NOT been certified for the original physical G**, and `P(s*)` has NOT been re-extracted from a new physical DOP853 run here. Therefore **no numeric upper bound for physical pLf'' or U_ss is certified** and no Step58 coefficient A/B/E enclosure follows.

## Why the missing derivatives cannot be silently set to zero

Exact rational **toy counterexample**: `G_n(s,u)=alpha*T_n(2s/S-1)*u`, `S=289/400`, `alpha=1/10`, Chebyshev `T_n`. On `0<=s<=S`, `|G_U|<=alpha` for all `n`, but at `s=S`, `G_sU=2alpha*n^2/S` and `D_U=alpha(alpha-1)+4alpha*n^2`. Thus a uniform `G_U` bound **alone** cannot bound the second radial jet sensitivity. This is NOT a counterexample to the physical Step55 G, only to an invalid inference from its first derivative.

## Reproducibility

New executable source: `numerics/hr_b3c3d6_radial_second_jet_budget.py`; new tests: `tests/test_hr_b3c3d6_radial_second_jet_budget.py`.

Executed in `/mnt/data/janus_b3c3d6_next`:
```sh
PYTHONPATH=. python -m unittest discover -s tests -v
python -m compileall -q numerics tests
PYTHONPATH=. python -m numerics.hr_b3c3d6_radial_second_jet_budget
```
**8 unittest PASS, 0 FAIL**; compileall PASS; module execution PASS. Toy tests include an attained sharp bound and the Chebyshev derivative amplification. No original physical runner executed in this session.

## Next priority

1. Re-execute SHA-authenticated original Step55 and dense DOP853 partition, evaluate the **correct** dense polynomial at `s=1/16,1/4,49/100,289/400` (corresponding to `r=1/4,1/2,7/10,17/20`), retaining all true binary64 domains and jumps.
2. Independently interval-certify `G_sU`, `G_UU`, `F` and `G_s` on the common Step55 physical tube and connecting segments; use the new second-jet bound for `pLf''`, `U_ss` and downstream `pSf'`.
3. Evaluate/enclose all **six** original Step58 coefficients A_N/A_M/B_N/B_M/E_N/E_M; factor exact zeros, address centre and global strictly-positive lapse BVP with both genuine boundaries.
4. Only then tackle full Dirac constraints/rank/charges/gauge, 4D dynamics, stability and observables. **GATE_2B OPEN; JANUS_R NOT_VALIDATED.**
