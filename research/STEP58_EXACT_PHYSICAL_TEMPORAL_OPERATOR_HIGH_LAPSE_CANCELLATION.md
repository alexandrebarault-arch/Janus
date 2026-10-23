# JANUS — Étape 58 : opérateur temporel physique complet (factorisé) et annulation exacte des seconds jets des lapses sur les primaires

**Date : 23 octobre 2026. Branche active et seule autorisée en écriture :** `research/gate2b-nonhomothetic-transfer`. **GATE_2B OPEN — JANUS-R NOT VALIDATED.** Ne pas modifier `main` ni `research/v2-flrw`, ne pas réactiver GitHub Actions.

## 1. Origine : véritable action sphérique ADM-HR positive-EH avec deux poussières et six couples

Les résultats utilisent SANS RÉÉCRITURE la source historique originale `numerics/hr_step45_exact_physical_ward.py`, Git blob authentifié `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, qui génère les deux densités hamiltoniennes `H_g,H_f`, la secondaire locale `C=K00-(K01)'`, et **tous les gradients d'Euler** correspondant à leurs six couples canoniques sphériques (12 variables).

Étape 56 : sur la charte `K>0`, la stationnarité algébrique du déplacement relatif impose exactement

\[
F_z=D_g-\frac{Kz}{\sqrt{1-z^2}}=0,\quad
D_g=p_{S_g}S_g'-L_g p_{L_g}'+p_g\theta_g',
\]
\[
K=m^2M_g^2L_gL_f(\beta_1S_g^2+2\beta_2S_gS_f+\beta_3S_f^2),\quad
z=\frac{D_g}{\sqrt{D_g^2+K^2}}.
\]

L'étape 57 a vérifié que la secondaire `C(q,q',z,z')` dépend explicitement de `z'` : il est FAUX de tenir `z` fixe dans sa variation. Cela crée trois dérivées secondes canoniques dans `C_red`.

## 2. Évolution temporelle LOCALE construite avec les six couples

Le nouveau `numerics/hr_step58_temporal_operator.py` assemble le **véritable champ hamiltonien** pour chaque paire :

\[
X_{q_a}=\frac{\delta H_{\rm tot}}{\delta p_a},\qquad
X_{p_a}=-\frac{\delta H_{\rm tot}}{\delta q_a},
\quad H_{\rm tot}=\int dr\, (N H_g+M H_f).
\]

Les gradients d'Euler de l'ORIGINAL Step45 contiennent explicitement les jets des lapses jusqu'à `N'',M''`. La dérivée radiale totale `D_r` agit sur TOUS les jets canoniques, leurs dérivées, et les jets du déplacement externe `z,z',z''`. L'opérateur polynomial en jets des lapses est assemblé **sans suppression arbitraire** de ses ordres élevés.

Sur `F_z=0`, la dérivée de la racine algébrique vaut exactement

\[
Z_D=\frac{\partial z}{\partial D_g}=\frac{(1-z^2)^{3/2}}{K},\quad
Z_K=\frac{\partial z}{\partial K}=-\frac{z(1-z^2)}{K}.
\]

Avec les gradients hamiltoniens des douze variables, on calcule

\[
\delta_H D_g = \sum_i (D_{g,q_i}X_i+D_{g,q_i'}D_r X_i),\quad
\delta_H K=\sum_i K_{q_i}X_i,\quad
\delta_H z=Z_D\delta_H D_g+Z_K\delta_H K.
\]

**Formule complète, exactement implémentée sous forme factorisée**, sur la surface stationnaire `F_z=0` et ses conséquences différentielles :

\[
\boxed{
\dot C_{\rm red}=
\sum_{i=1}^{12}\big[C_{q_i}X_i+C_{q_i'}D_rX_i\big]
+C_z\,\delta_H z+C_{z'}D_r(\delta_H z).
}
\]

Les dérivées de `C` sont prises à `z,z'` externes **avant** d'éliminer le déplacement, et la première variation de `H` à déplacement fixé est permise par l'enveloppe stationnaire. Les bords doivent être contrôlés pour la correspondance aux crochets fonctionnels. Ce sont les dérivées directionnelles LOCALES du champ physique, pas une approximation en différences finies.

L'opérateur exact obtenu a la structure brute

\[
\dot C_{\rm red} = A_N N+B_NN'+C_NN''+A_M M+B_M M'+C_MM''.
\]

**Aucun terme en `N''',M''',N'''',M''''` ne subsiste dans l'assemblage symbolique**, même avant les contraintes primaires. Chaque coefficient est conservé comme expression SymPy factorisée, sans expansion illisible. Les termes `A_N,B_N,A_M,B_M` existent et sont enregistrés algorithmiquement mais **ne sont pas encore réduits sur la solution exacte Step55**.

## 3. NOUVEAU RÉSULTAT EXACT : les seconds jets des lapses s'annulent sur `F_z=H_g=0`

Il ne s'agit PAS d'une limite numérique. L'identité est prouvée par annulation SYMBOLIQUE sur les paramètres et champs originaux, sans spécialiser le benchmark.

Sur `K>0`, résoudre la VRAIE stationnarité `F_z=0` pour le jet de moment canonique :

\[
p_{L_g}'=\frac{p_{S_g}S_g'+p_g\theta_g'-Kz/\sqrt{1-z^2}}{L_g}.
\]

En substituant cette expression dans **les coefficients issus des douze variables canoniques**, SymPy vérifie identiquement :

\[
\boxed{\left.C_M\right|_{F_z=0}=0}
\]

et

\[
\boxed{
\left.C_N\right|_{F_z=0}
=\frac{z^2-1}{L_gL_f}\left.H_g\right|_{F_z=0}.
}
\]

Pour une donnée primaire `F_z=H_g=0`, les deux coefficients `C_N,C_M` s'annulent donc EXACTEMENT, et l'opérateur restant est au plus du **premier ordre spatial** :

\[
\boxed{\left.\dot C_{\rm red}\right|_{F_z=H_g=0}
=A_N N+B_NN'+A_M M+B_MM'.}
\]

**Attention :** `F_z=0` seul ne suffit PAS à éliminer `N''`. La réduction finale de l'équation implique aussi `H_f=0`, la contrainte spatiale diagonale, `C=0`, les compatibilités des dérivées radiales des contraintes et la régularité des bords. On ne peut PAS inférer la fixation d'un ratio `M/N` ou le rang de Dirac des seules annulations `C_N,C_M`. Il serait encore prématuré de proclamer l'élimination du fantôme BD.

## 4. Reproductibilité et vérification indépendante de l'intégration par parties

Les NOUVEAUX fichiers sont vérifiés **byte-identical** par `git hash-object` dans l'environnement local puis par lecture directe des blobs GitHub :

- `numerics/hr_step58_temporal_operator.py` — Git blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`.
- `tests/test_hr_step58_temporal_operator.py` — Git blob `0f9f91de0f607e811dc168e1ead0c3e9296574d0`.

Workspace d'exécution isolée : `/mnt/data/janus-step58`, où la source historique originale Step45 et les sources de Step57 furent reprises en octets exacts. Commande exécutée :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
 tests/test_hr_step57_secondary_principal_symbol.py \
 tests/test_hr_step58_temporal_operator.py
# 27 PASSED in 3.75s (12 historiques Step57 + 15 nouveaux Step58).
```

Les contrôles couvrent : les 12 champs canoniques et 6 couples, les signatures symplectiques exactes, tous les jets de lapses avant contraintes, l'absence des jets de lapses >2, la réponse du déplacement `z` via `p_{L_g}'`, la formule de chaîne complète, les deux identités de `N''/M''` sur la vraie surface `F_z=0`, l'interdiction d'annuler `N''` sans imposer `H_g=0`, et l'adjoint compact.

**Oracle indépendant complémentaire, mais NON JANUS :** un exemple polynomial à dérivées secondes, avec deux paires canoniques actives (quatre inactives), fonctions tests compactes et `z=z(q,p,q',p')`, montre EXACTEMENT que l'intégrale de la dérivée locale le long du champ hamiltonien est égale à l'intégrale du crochet fonctionnel obtenu par l'Euler d'ordre 2 et intégrations par parties. Il vérifie la méthode d'adjoint, mais ne remplace pas un **oracle original non-IBP** de la contrainte temporelle JANUS.

## 5. Verrous scientifiques précis — Étape 59

1. **RÉDUIRE LES QUATRE COEFFICIENTS** `A_N,B_N,A_M,B_M` sur la solution radiale EXACTE et à poussières positives certifiée Step55 : imposer `F_z=H_g=H_f=D_{\rm diag}=C=0` ainsi que les dérivées de `F_z` nécessaires pour `z',z''`. Conserver leurs signes/rangs, notamment au centre. Si la réduction est trop lourde, pratiquer un calcul d'AD/intervalle validé sur l'EDO de secondaire Step55, en vérifiant la convergence.
2. Étudier la **matrice des multiplicateurs**, les directions de jauge et le ratio physique des lapses ; éliminer les solutions dégénérées et rendre explicites les termes de bord. Aucune conclusion de rang ne découle automatiquement d'un système du premier ordre.
3. Construire un contrôle physique indépendant de ce véritable crochet temporel avec l'original ADM **non intégré par parties**, et les 12 variations canoniques, avant de conclure sur fantôme ou cosmologie 4D. Examiner séparément `K=0`, `J=0` et les branches hors charte.

**VERDICT : vrai opérateur temporel à six couples construit sous forme factorisée, annulation analytique EXACTE des deux seconds jets de lapse sur `F_z=H_g=0`, 27 tests passent. Rang Dirac, fixation des lapses et absence du fantôme Boulware–Deser PAS établis. Gate 2B OPEN ; JANUS-R NOT VALIDATED.**
