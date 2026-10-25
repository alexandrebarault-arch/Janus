# JANUS — Étape 68e : quotient exact des jets seconds du déplacement relatif

**25 octobre 2026. Branche d'écriture :** `research/gate2b-nonhomothetic-transfer` uniquement. **GATE 2B OPEN — JANUS-R NOT_VALIDATED.**

## 1. Source physique originale véritablement exécutée

Le programme `numerics/hr_step68e_exact_shift_full_lapse_response.py` importe le **véritable fichier original Step45** `numerics/hr_step45_exact_physical_ward.py`, reconstitué **octet pour octet** et authentifié par son Git blob SHA `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. Les **neuf identités Ward** d'origine ont été recalculées exactement. Les six couples canoniques et les deux poussières mobiles sont inclus.

Le calcul reconstruit la variation de Fréchet complète de `z` à partir des vrais gradients d'Euler `eg,ef` : `delta_H z = Z_N^0 N + Z_N^1 N' + Z_M^0 M + Z_M^1 M'`. Les coefficients de lapses dérivés deux ou trois fois dans **cette seule variation du shift** sont nuls. Il reproduit indépendamment les identités de Step68d, sur `F_z=0,K>0` :

\[
Z_N^1=\frac{(1-z^2)^{3/2}}{K}H_g-\frac{1-z^2}{L_g},\qquad
Z_M^1=\frac{1-z^2}{L_f}.
\]

**Attention :** ce sont les coefficients de **delta_H z**, PAS ceux du crochet temporel complet **dot C**. Le module Step55 n'a pas été réexécuté ce tour.

## 2. Résultat NOUVEAU : suppression des douze jets seconds du coefficient Z_M^0

L'équation algébrique de stationnarité du modèle est

\[
F_z=D_g-\frac{Kz}{\sqrt{1-z^2}}=0,\qquad
D_g=p_{S_g}S'_g-L_gp'_{L_g}+p_g\theta'_g.
\]

Sur `F_z=0`, le coefficient `Z_N^0` n'emploie **aucune** dérivée seconde des douze champs canoniques. En revanche, le coefficient de lapse non dérivé `Z_M^0` en emploie **exactement trois**, qui ne s'annulent pas en général : `p''_{L_g},S''_g,theta''_g`. Il serait incorrect de les figer.

On prend la dérivée radiale **COMPLÈTE** de `F_z`, y compris les contributions de `K'` et `z'`, puis on forme

\[
\boxed{R_M=Z_M^0+\alpha F'_z,\qquad
\alpha=-\frac{z(1-z^2)^{3/2}}{L_fK}.}
\]

**Proposition démontrée par calcul formel exact :** sur le shell `F_z=0`, les douze dérivées \(\partial R_M/\partial q_i''\) sont exactement **nulles**, sans sélectionner de profil numérique ni supprimer un terme à la main. L'affinité de `Z_M^0` dans ses trois jets d'ordre 2 est aussi vérifiée.

Sur une donnée radiale satisfaisant les **deux** contraintes `F_z=F_z'=0`, `R_M` et `Z_M^0` sont égaux ; la représentation `R_M` ne contient plus aucune dérivée radiale canonique seconde. Le code produit ce représentant et vérifie son indépendance vis-à-vis des douze jets.

Les tests négatifs montrent qu'**omettre `F_z'`** ou employer le **mauvais signe** de `alpha` laisse une dépendance non nulle en `p''_{L_g}`. Il ne s'agit donc pas d'une annulation fabriquée par gel des champs.

## 3. Compatibilité avec le centre sphérique

Le coefficient `alpha` seul paraît singulier lorsque `r→0`. Cependant, sous les parités analytiques de la famille radiale

\[
s=r^2,\quad z=rw(s),\quad K=r^2k(s),\quad
F_z=r^3 f(s),\quad L_f(0)>0,\ k(0)>0,
\]

on a \(F_z'=r^2(3f+2sf_s)\) et exactement

\[
\boxed{\alpha F_z'=
-r\frac{w(1-sw^2)^{3/2}}{L_fk}(3f+2sf_s).}
\]

Ce **produit**, et non `alpha` pris isolément, est `O(r)` et régulier au centre lorsque les fonctions normalisées et `f_s` sont continues. La limite est nulle. Cette preuve **ne certifie pas à elle seule** la régularité complète de `Z_M^0` ni une évolution 4D.

## 4. Exécution, authenticité et sauvegarde

Nouveau code `numerics/hr_step68e_exact_shift_full_lapse_response.py`, blob Git `8f4e82bcec2b5c179f5c2d4e21ccb70f2828b206`.

Tests `tests/test_hr_step68e_exact_shift_full_lapse_response.py`, blob Git `0f9aef7510d4e6d035405cf87820d28f032d0db0`.

Les **deux fichiers définitifs ont été relus sur GitHub** : leurs blobs correspondent **octet pour octet** aux fichiers exécutés. **18 tests passent en 2,37 secondes**, incluant origine byte-authentique, rejet de mutation du fournisseur physique, Ward à six couples, les deux coefficients de Step68d, les douze dérivées secondes, mauvais signe et terme omis, et la parité au centre. Une première erreur de syntaxe du fichier de tests et une factorisation inutilement coûteuse du manifeste ont été corrigées **avant** cette exécution finale ; aucun succès n'est imputé à ces exécutions interrompues.

Commande réellement exécutée :

```bash
cd /mnt/data/janus-step68e
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. \
 pytest -q tests/test_hr_step68e_exact_shift_full_lapse_response.py
# 18 passed in 2.37s
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. \
 python -m numerics.hr_step68e_exact_shift_full_lapse_response
```

Manifeste brut local SHA-256 `024c4dc81ec76fc2076d683ac42154b43ada352f5aaa9812bd962d5c0695eda1`. Rapport structuré : `research/reports/gate2b-step68e-shift-Fzprime-quotient.json`. GitHub Actions restent désactivés.

## 5. Ce que l'étape 68e ne conclut PAS — et Step68f

Ce travail a simplifié le **déplacement relatif hamiltonien** après la stationnarité et sa première prolongation ; il n'a PAS calculé les quatre coefficients temporels physiques d'ordre inférieur `A_N,B_N,A_M,B_M` de `dot C` sur la **véritable** solution radiale Step55, ni réexécuté ce tour les originaux 46/55/57/58/59/60 ensemble. L'oracle non-IBP indépendant, les bords, le rang de Dirac, la fixation des lapses, le fantôme BD, les chartes `K=0,J=0` et la cosmologie 4D restent OUVERTS.

**Prochaine étape 68f :** reconstituer les originaux Step45/46/55/57/58/59/60 dans un seul environnement avec SHA authentifiés, substituer le quotient exact du shift dans le **vrai** opérateur temporel Step58/60 et les prolongations de toutes les contraintes, puis calculer les quatre coefficients restants et le rang/lapses avec bords et oracle indépendant.

**Verdict : GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
