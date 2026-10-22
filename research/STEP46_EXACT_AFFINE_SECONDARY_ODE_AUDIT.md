# JANUS — Step46: exact local secondary becomes a first-order momentum equation

**22 October 2026 — branch `research/gate2b-nonhomothetic-transfer`.** The preceding Step45 audit established the exact spherical six-canonical-pair Ward identities and a finite-difference-free analytic secondary `C=K00-(K01)'`, while certifying that the frozen Step41 collocation polynomial does not make C identically zero in a specified exact-rational calibration. Step46 adds a genuinely constructive **algebraic/ODE reduction**, not an evolved cosmological solution.

## Exact primary elimination

Treat the two curved spherical metric functions, noncomoving dust phases, relative shift `z(r)`, and g-sector canonical data as fixed smooth functions satisfying their original primaries. Let

`P(r)=pLf(r)`, `V=P'(r)`, `beta_f=sqrt(1+(theta_f'/Lf)^2)`, `F=pLf/(2 Mf2 Sf Sf')`, `B_f=beta_f+F theta_f'`.

On the original independent f-sector lapse primary and radial momentum constraint `D_f=-D_g`, with original interaction potential `W_f`, solve algebraically:

```text
pf=-( Lf*P^2/(4 Mf2 Sf^2) -F*(-Dg+Lf*V)
      -Mf2*Lf*Sf^2*R3f/2 + z*Dg/Lf + Wf ) / B_f

pSf=(-Dg + Lf*V - pf*theta_f')/Sf'
```

These are original radial spherical ADM-HR-plus-dust equations, NOT a phenomenological surrogate. The shift `z` is on its algebraic stationarity shell `Fz=0` for the first variation.

## Exact physical secondary factorization

For the full original six-canonical-pair `C` derived at Step45, direct symbolic differentiation shows the **universal off-shell canonical** identity

[
rac{partial C}{partial p_{S_f}}
=-rac{m^2M_g^2 A_tsqrt{1-z^2}}{2M_f^2 S_f},
qquad A_t=eta_1 S_g^2+2eta_2S_gS_f+eta_3 S_f^2.
]

Substitution of the two f-primary solutions makes C **EXACTLY AFFINE** in `V=pLf'`:

[
oxed{C(r;P,V)=C_0(r;P)+C_1(r;P)V},
]

[
oxed{
C_1=-
rac{m^2M_g^2A_tsqrt{1-z^2}}{2M_f^2S_f}
rac{L_feta_f}{S_f'B_f}.}
]

No `V^2` or higher derivatives occur. Both identities, the vanishing second V derivative, and exact substitution

[
oxed{P'(r)=V=-C_0/C_1quadLongrightarrowquad C=0}
]

are independently and strictly tested by SymPy symbolic simplification, without tolerance, sampling or finite differences. A concrete executable right-hand side `pLf_prime_rhs` and the exact primary-eliminated expressions are returned by `numerics/hr_step46_exact_secondary_ode.py`.

**Nondegeneracy domain:** `m²,Mg²,Mf²,Lf,Sf,Sf',At,beta_f,B_f>0` and `|z|<1`. The fixed Step40/42 physical chart has `At=S_g²J(S_f/S_g)>0`, positive dust coefficient and S_f' on `0<r<=.85`, so `C1<0` there. This makes the implicit-function reduction and standard **local IVP** well-defined away from r=0 for smooth prescribed remaining fields.

This is NOT a proof of global continuation of an exact secondary-satisfying branch to r=0, nor does it show that the other gravitational sector evolves on shell. Continuation may fail if density signs or denominator margins change. Spherical parity imposes a separate regular singular-point issue at r=0.

## Reproduction and limitations

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
 tests/test_hr_step45_exact_physical_ward.py \
 tests/test_hr_step45_secondary_point_certificate.py \
 tests/test_hr_step46_exact_secondary_ode.py
# ACTUALLY executed in isolated /mnt/data/janus-step45: 32 PASSED in 2.04 s.

PYTHONPATH=. python -m numerics.hr_step46_exact_secondary_ode
```

All six new Step45–46 source/test Git blobs were compared against executed local files. Specifically:
- `numerics/hr_step46_exact_secondary_ode.py`: `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
- `tests/test_hr_step46_exact_secondary_ode.py`: `f09e5205d5915d546cf83875ffcafe44232411e2`.

Eight Step46 tests plus twenty-four Step45 tests pass in one coherent local lightweight symbolic/interval workspace. No full repository suite, user-disabled GitHub CI, or original historical six-provider numerical solver re-execution occurred this turn. The proof is a symbolic reconstruction of the genuine original density formulas and the preceding exact physical Ward expression, with the stated chart assumptions.

**Next Step47:** Solve the exact IVP for `pLf(r)` on a nontrivial interior interval, independently recalculate primary and secondary residuals from the ORIGINAL non-IBP action, bound dust positivity, analyze the regular center, and only then attempt Dirac secondary time preservation and actual lapse fixing. Preserve independent lapse smearing and all six canonical pairs; do NOT conflate the external sign-reversed f-EH JHR manuscript.

**FINAL:** Exact Ward `W=z Hg/Lf` established in the reduced spherical theory; analytic C and local FIRST-ORDER ODE for its exact satisfaction established; global exact on-shell radial data and full Dirac time preservation still OPEN; `GATE_2B=OPEN`, `JANUS-R NOT VALIDATED`.
