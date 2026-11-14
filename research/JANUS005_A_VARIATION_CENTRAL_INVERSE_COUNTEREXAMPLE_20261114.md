# JANUS-005 — Contre-exemple à la fixation de M2/Z1 lorsque A varie (2026-11-14)

**Base lue :** main `60d001c114558c7e5e6ed8e7223e83297cb9a71f`; source `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Ce résultat teste une **famille algébrique étendue**, non l'admissibilité physique de la variation géométrique.

Poser `C=3*b1*Y+3*b2*Y**2+b3*Y**3`, `H=3/(10*A**3)+M2*C/3`, `PG=-2*A**2*sqrt(H)`, `U0=MF*A*Y*(PG/A-2*Z1)`. Fixer Y, MF et les b_i, mais laisser varier A, M2, Z1. Le jacobien 2×2 en (M2,Z1) est inversible pour C != 0 et H>0 ; cependant la matrice 2×3 en (A,M2,Z1) possède un noyau non nul.

**Tangente exacte conservant PG et U0 :** prendre dA=1, puis
```
dM2/dA = -(4*A**3*M2*C + 9/10)/(A**4*C)
dZ1/dA = -Z1/A
```
Ces deux formules sont obtenues en résolvant `J_(M2,Z1) * (dM2,dZ1) = - d_(A)(PG,U0)`. Vérification SymPy exacte : les deux composantes du résidu sont identiquement nulles.

**Contre-exemple fini indépendant :** pour tout A'>0 proche du A initial, maintenir PG et U0 à leurs valeurs initiales en définissant
```
M2' = 3/C * (PG**2/(4*A'**4) - 3/(10*A'**3))
Z1' = (PG/A' - U0/(MF*A'*Y))/2
```
sur la branche PG<0, H'>0. Avec les constantes originales Step55, A=0.4, M2=23.3348939346, Z1=0.004, et A'=0.401, le calcul à 30 chiffres donne M2'≈22.8337018656043305935906499686, Z1'≈0.00399002493765586034912718204489. Les deux valeurs PG et U0 sont reproduites avec résidus numériques inférieurs à 1e-20 ; H'>0 et M2'>0.

**Conclusion circonscrite :** l'affirmation « PG et U0 fixés impliquent M2 et Z1 fixés » est vraie **seulement à A et autres coefficients fixés**. Elle échoue dans la famille algébrique où A varie. Cela ne prouve absolument pas que A puisse varier dans les solutions Step45/49/55 avec les deux véritables bords et Dirac. Il faut filtrer cette tangente par les contraintes et conditions de bord. Aucun résultat physique certifié.

**Commande réellement exécutée :** `python /mnt/data/janus_audit/check.py` avec SymPy, PASS (résidu symbolique 2/2 nul, deux reconstructions finies PASS). Script local non encore persisté sur GitHub. Cellules physiques b3c3d9 évaluées/certifiées/inconclusives : 0/0/0.

**NEXT_ACTION_EXACT :** inspecter dans Step45/49/55 et les deux vrais bords si A est un paramètre libre ; substituer la tangente ci-dessus dans les contraintes linéarisées. JANUS-001 : transfert authentifié des dépendances historiques, neuf tests puis pilote physique une cellule.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
