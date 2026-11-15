# JANUS-001 — contrôle du troisième jet (2026-11-15)

HEAD source : `6774eb9d9a17551e03b6a4870b22690124816f24`.

Calcul exact SymPy 1.14.0 exécuté :
```python
import sympy as sp
r=sp.symbols('r',positive=True)
U=sp.Function('U')
print(sp.diff(r*r*U(r*r),r,3))
```
Résultat : `pLf'''(r)=24*r*U_s+36*r**3*U_ss+8*r**5*U_sss` avec `pLf=r²U(r²)`.

Dans `hr_b3c3d6_boundary_ANAM_interval_certificate.py`, `physical_jet` construit `uc=u+us*h+uss*h*h/2` et n'introduit pas `U_sss`. Le runner b3c3d9 substitue pourtant les jets `qppp` dans les coefficients Step58. **Risque conditionnel de terme manquant**, pas erreur démontrée : le coefficient de `pLfrrr` pourrait s'annuler sur la coquille physique.

NEXT_ACTION_EXACT : dans les sources authentifiées, calculer `sp.diff(op['operator'][label][0],sp.Symbol('pLfrrr'))` pour N et M, puis réduire sur Fz=Hg=Hf=C=0 et les jets requis. Si non nul, dériver et enclore U_sss depuis l'ODE Step55 avant de prétendre certifier A_N/A_M. Reprendre parallèlement les transferts authentifiés, neuf tests et pilote.

Tests moteur SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0 ; GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
