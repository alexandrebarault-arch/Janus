# JANUS-006 — Témoin algébrique sur les quatre contraintes et mineur alternatif (2026-11-20)

## Statut et provenance
**Résultat conditionnel à la fidélité de la transcription locale du code Step45** : le module GitHub `numerics/hr_step45_exact_physical_ward.py` a été lu au HEAD `5b69c3017e15d39ae824df2cdff603d49177083f`, blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. Une transcription manuelle locale de ses densités Ag,Bg,Af_full,Bf, de sa dérivation totale et des noyaux d'Euler a été exécutée sous SymPy 1.14.0 ; **pas** de comparaison Git hash-object octet pour octet du script transcrit. Le témoin est donc une preuve algébrique pour ces formules, non un certificat physique ni un rejeu authentifié du module.

## Hypothèse falsifiable
L'annulation du mineur choisi précédemment (facteur P=0) pourrait-elle coexister avec les quatre contraintes et imposer une perte de rang du jacobien ambiant complet ?

## Témoin rationnel
Fixer `Lg=Lf=Sg=Mg2=Mf2=m2=beta1=beta2=beta3=1`, `Sf=3`, `beta0=beta4=0`, `z=zr=zrr=0`. Fixer à zéro les moments `pLg,pSg,pLf,pSf,pg,pf`, les dérivées premières des douze coordonnées canoniques, et tous les jets seconds sauf `Sgrr=-15` et `Sfrr=-11/3`. Avec la convention de noms exacte Step45 (`Sgrr` et `Sfrr` désignent les dérivées secondes radiales), SymPy donne exactement :

- `At=16`, `K=16>0`, `P=0` ;
- `Hg=0`, `Hf=0`, `Fz=0`, `C_exact=0` ;
- avant fixation de `pLg`, `Hg=(8*Sgrr+pLg**2+120)/4`, `Hf=2*(3*Sfrr+11)` ;
- sur la tranche choisie, `C_exact=-8*pSf/3`.

Le jacobien des quatre contraintes `(Hg,Hf,Fz,C_exact)` par rapport aux colonnes `(Sgrr,Sfrr,pLgr,pSf)` au témoin vaut exactement `diag(2,6,-1,-8/3)`, donc **déterminant 32**. Le mineur antérieur avec colonne `pLg` s'annule, mais **un autre mineur 4×4 est non nul sur le même témoin satisfaisant les quatre contraintes**. Cela réfute l'inférence « P=0 entraîne rang ambiant <4 » sur cette configuration.

## Reproduction et contrôles
Commande réellement exécutée : `python /mnt/data/janus_check/check.py` (SymPy 1.14.0). Le script local a reconstruit indépendamment les Euler jets et `K00-K01'` depuis les densités lues, puis imprimé `MATCH True` pour la dérivée publiée de C, `ON SHELL [0,0,0,0]`, `J Matrix([[2,0,0,0],[0,6,0,0],[0,0,-1,0],[0,0,0,-8/3]]) DET 32`. Contrôle analytique indépendant : triangularité du jacobien au témoin et produit `2*6*(-1)*(-8/3)=32`. Le script local n'est pas encore archivé ni blob-authentifié.

## Limites et prochaines actions
Ceci est un **témoin dans l'espace ambiant des jets**, pas un profil radial intégrable, pas une solution des deux véritables conditions de bord, pas une preuve du rang de Dirac ni de stabilité 4D. Les jets secondes choisis ne satisfont pas automatiquement l'holonomie sur un intervalle. Les tests b3c3d9 et pilote sont SKIP ; cellules physiques effectivement évaluées/certifiées/inconclusives = 0/0/0.

**NEXT_ACTION_EXACT :** (1) transférer le module Step45 authentique, comparer son Git blob aux octets locaux et rejouer le calcul directement via `exact_physical_ward()` ; (2) examiner l'intégrabilité des jets et les deux vraies traces de bord, puis le rang Dirac et les lapses ; (3) reconstruire les dépendances historiques Step45/46/55/58 de JANUS-001 et exécuter neuf tests puis pilote physique. **GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**
