# JANUS-005 — domaine central exact de M2 et limite de transport du signe (2026-11-12)

## Provenance et question
Lecture fixée au HEAD `14b4d5bc371432eb33c04f485d7c640e9f0e0965`, source `numerics/hr_step55_global_barrier.py` (constantes `A,Y,M2,B0..B3,Z1,H2,PG,U0`). Déterminer si la variation formelle de M2 préserve au moins le signe central U0, sans supposer les contraintes radiales satisfaites.

## Proposition exacte (carte prescrite, paramètres restants fixes)
Poser `K=(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3` et `C=0.9/(3*A**3)`. Les décimales du code interprétées comme fractions rationnelles donnent `K>0` (valeur ~0.04308405810889453) et `C>0`. On a `H2=C+K*M2`, `PG=-2*A**2*sqrt(H2)`, `U0=MF*Y*(PG-2*A*Z1)`. Avec `A,Y,MF,Z1>0` :

- Pour tout `M2>=0`, `H2>0`, `PG<0`, `U0<0` **au centre**, même pour une variation finie de M2.
- Plus généralement, la branche réelle `PG<0` existe pour `M2>-C/K` (seuil ~-108.79894340854314), et `U0<0` dans tout ce domaine.
- `dPG/dM2=-A**2*K/sqrt(H2)<0` et `dU0/dM2=MF*Y*dPG/dM2<0`. La tangente de Friedmann de la preuve antérieure correspond bien à `dM2/dPG=PG/(2*A**4*K)`.
- Au seuil `M2=-C/K`, `PG=0`, la branche négative différentiable cesse ; ne pas étendre l'argument de rang à ce point.

## Contrôle reproductible
```python
from fractions import Fraction as F
A=F('0.4');Y=F('0.5787707228025044');Z=F('.004');MF=F('.10879548725')**2
B0=F(0);B1=F(1);B2=F('-4.2383993109');B3=F('13.6801214252')
K=(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3
C=F('.9')/(3*A**3)
assert all(v>0 for v in (A,Y,Z,MF,K,C))
assert -C/K < 0
assert C+F('23.3348939346')*K>0
print(float(K),float(-C/K))
```
Exécuté en Python (fractions exactes) : assertions PASS, K ~0.04308405810889453, seuil ~-108.79894340854314. Les signes des dérivées découlent directement des formules ; aucune intégration ODE n'a été effectuée.

## Contre-limite critique
La positivité conditionnelle de `den` au bord extérieur dépend du signe de **U(s)**, pas du seul signe de **U0**. La preuve ci-dessus **ne transporte pas** U0<0 jusqu'à s=289/400 lorsque M2 varie : les coefficients géométriques et G(s,U) varient avec M2, et la barrière Step55 n'a été certifiée que pour la carte prescrite. Elle ne certifie ni la liberté physique de M2, ni les deux vrais bords, ni Dirac, ni la stabilité. Ne pas présenter ce résultat central comme une extension du certificat extérieur.

**NEXT_ACTION_EXACT :** extraire la dépendance M2 de `geometry(s)` et de `G(s,U)`, puis tester une barrière paramétrique avec enclosures rationnelles sur un intervalle M2 explicitement choisi ; vérifier séparément les deux vrais bords et les contraintes de Dirac. JANUS-001 : transférer les modules originaux authentifiés, exécuter les neuf tests et le pilote à une cellule. `GATE_2B=OPEN` ; `JANUS_R=NOT_VALIDATED`. Cellules physiques nouvelles : 0 évaluée, 0 certifiée.
