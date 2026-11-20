# JANUS-006 — réduction exacte du mineur 4×4 à une dérivée de C_exact — 2026-11-20

## Source et domaine
Source authentifiée `numerics/hr_step45_exact_physical_ward.py` blob Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, au HEAD `46e5f5e4f229154996ab2edce251559e9625a0a9`. La source établit que `C_exact=K00-d_r(K01)` ne dépend d'aucun second jet canonique; `Fz` non plus. Les trois premiers jets retenus sont `(Sgrr,Sfrr,plgr)`. Leurs coefficients dans `(Hg,Hf,Fz)` sont ceux du jalon précédent.

## Mineur et élimination sans division par K
Ajouter une quatrième colonne `x` indépendante des trois jets, et poser `c=∂C_exact/∂plgr`, `j=∂C_exact/∂x`, `h=∂Fz/∂x`. Le mineur est exactement
```
[ 2 Mg2 Sg/Lg      0       -z        ∂x Hg ]
[      0       2 Mf2 Sf/Lf -z Lg/Lf   ∂x Hf ]
[      0            0       -Lg       ∂x Fz ]
[      0            0        c          j   ]
```
et son déterminant
`(4 Mg2 Mf2 Sg Sf/(Lg Lf))*(-Lg*j-h*c)`
soit
`(-4 Mg2 Mf2 Sg Sf/Lf)*(j+(h/Lg)*c)`.

Pour `x=pLg` (moment canonique non dérivé), la formule authentifiée `Fz=pSg*Sgr-Lg*plgr+pg*tgr-interaction*z/root` donne `h=0`. Donc le mineur vaut exactement
`-4 Mg2 Mf2 Sg Sf/Lf * ∂C_exact/∂pLg`.

**Critère falsifiable** : si cette dérivée est non nulle en un point régulier, les quatre contraintes sont indépendantes dans l'espace des jets ambiants en ce point, sans aucune division par K. Si elle s'annule, CE MINEUR est nul, sans conclure que le rang complet est inférieur à 4 : tester d'autres colonnes. Aucune non-annulation de ∂C_exact/∂pLg n'est démontrée ici.

## Contrôle indépendant
Commande Python/SymPy 1.14.0 réellement exécutée :
```python
import sympy as s
a,b,c,d,e,f,g,h,i,j=s.symbols('a b c d e f g h i j')
J=s.Matrix([[a,0,c,d],[0,b,e,f],[0,0,g,h],[0,0,i,j]])
print(s.factor(J.det()))
```
Résultat `a*b*(g*j-h*i)`, cohérent avec développement direct par les deux premières colonnes. La formule avec h=0 est `a*b*g*j`.

## Portée et prochaine expérience
Résultat structurel exact et conditionnel, pas un rang 4 prouvé, pas une preuve de Dirac. La prochaine commande scientifique doit réellement évaluer `sp.diff(exact_physical_ward()['C_exact'], exact_physical_ward()['q'][1])`, puis factoriser, tester la non-nullité sur la surface des contraintes et sur les strates K=0, z=0, et vérifier par une colonne alternative si nécessaire. Après cela, holonomie, deux vrais bords, fixation des lapses et dynamique 4D. JANUS-001 toujours bloqué pour la reconstruction historique; aucun test moteur ni pilote exécuté, 0 cellule physique évaluée/certifiée/inconclusive. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
