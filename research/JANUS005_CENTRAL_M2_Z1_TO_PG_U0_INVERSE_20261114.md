# JANUS-005 — Inversibilité de la carte centrale (M2,Z1) → (PG,U0) — 2026-11-14

**Source originale :** `numerics/hr_step55_global_barrier.py`, blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, HEAD initial `f6710275e627f283c6f96e38943c523d308f032c`. Domaine : paramètres prescrits A,Y,MF et coefficients b0..b3 fixés, M2 variable, Z1 variable, H2>0, branche PG<0. Résultat purement algébrique sur les données initiales Step55.

Définir `B=A*Y`, `C=b0+3*b1*Y+3*b2*Y**2+b3*Y**3`, `H2=0.9/(3*A**3)+M2*C/3`, `PG=-2*A**2*sqrt(H2)`, `U0=MF*B*(PG/A-2*Z1)`. Le jacobien exact est

```
det(d(PG,U0)/d(M2,Z1)) = 2*MF*B*A**2*C/(3*sqrt(H2)).
```

**Preuve :** dPG/dZ1=0, dU0/dZ1=-2*MF*B, dPG/dM2=-A**2*C/(3*sqrt(H2)). Ainsi J=(-2*MF*B)*(dPG/dM2), strictement positif si A,B,MF,C,H2 sont positifs. Pour les constantes prescrites Step55, C>0 et H2>0, J≈0.000015833960768022369638 à M2=23.3348939346. La carte est donc localement inversible à ces paramètres. Sur la branche PG<0, elle admet aussi l'inverse explicite `M2=3*(PG**2/(4*A**4)-0.9/(3*A**3))/C`, `Z1=(PG/A-U0/(MF*B))/2`, tant que C≠0. La branche et H2>0 sont indispensables : sans elles le carré de PG introduit une ambiguïté de signe.

**Contrôle contradictoire :** ce calcul n'ajoute PAS deux degrés de liberté physiques. Il montre au contraire que PG et U0 sont des coordonnées algébriques équivalentes à M2 et Z1 dans cette famille prescrite. Imposer simultanément PG et U0 constants élimine toute variation infinitésimale de M2,Z1 à coefficients fixés, mais aucune preuve n'établit que les vrais bords/Dirac imposent ces deux constantes. Si C=0, ou si les coefficients A,Y,MF peuvent varier, la conclusion doit être réexaminée.

**Reproduction réellement exécutée :** Python/SymPy (commande `python - <<'PY'` avec le code ci-dessous). Une identité symbolique PASS, évaluation exacte des signes et valeur numérique. Aucun test du moteur b3c3d9 exécuté ; **0 cellule physique évaluée/certifiée/inconclusive**.

```python
import sympy as s
A=s.Rational(2,5); Y=s.Rational('0.5787707228025044')
MF=s.Rational('0.10879548725')**2
M,Z=s.symbols('M Z',real=True)
b=list(map(s.Rational,['0','1','-4.2383993109','13.6801214252']))
C=b[0]+3*b[1]*Y+3*b[2]*Y**2+b[3]*Y**3
H=s.Rational('0.9')/(3*A**3)+M*C/3
PG=-2*A**2*s.sqrt(H)
U=MF*A*Y*(PG/A-2*Z)
J=s.det(s.Matrix([PG,U]).jacobian([M,Z]))
assert s.simplify(J-2*MF*A*Y*A**2*C/(3*s.sqrt(H)))==0
assert C>0 and H.subs(M,s.Rational('23.3348939346'))>0
assert J.subs(M,s.Rational('23.3348939346'))>0
print(s.N(J.subs(M,s.Rational('23.3348939346')),20))
```

**NEXT_ACTION_EXACT :** lire les équations Step45/49 et les deux vraies conditions de bord, déterminer si PG et U0 sont prescrits par la physique ou des données initiales ajustables ; linéariser ensuite la carte physique et les contraintes Dirac, sans supposer la liberté indépendante de M2/Z1. En parallèle JANUS-001 : transférer les dépendances authentifiées du runner, vérifier blobs et lancer les neuf tests puis le pilote une cellule.

**Statuts : GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**
