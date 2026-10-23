# JANUS — Étape 60 : réduction exacte par les contraintes radiales COMPLÈTES dans le crochet temporel

**23 octobre 2026. Branche unique de recherche :** `research/gate2b-nonhomothetic-transfer`. **Gate 2B OUVERT ; JANUS-R NON VALIDÉ.** Le résultat démontré ici concerne l'ordre différentiel des champs canoniques dans le calcul de Dirac temporel ; il ne démontre ni la fixation des lapses, ni la fermeture temporelle, ni l'absence du fantôme de Boulware–Deser.

## 1. Les équations originales, non un noyau fabriqué

Quatre modules scientifiques d'origine ont été exécutés ensemble et authentifiés par leur **vrai Git blob SHA-1** avant le calcul. Le nouveau programme refuse de démarrer si l'un de ces fichiers est modifié :

| Module original | SHA Git authentifiée |
|---|---|
| `numerics/hr_step45_exact_physical_ward.py` | `66aa43841dccfe4a5d586a49be9c10af3a67a10e` |
| `numerics/hr_step57_secondary_principal_symbol.py` | `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f` |
| `numerics/hr_step58_temporal_operator.py` | `802c23aebd41780d8c462f1aa1711707fe4ee88f` |
| `numerics/hr_step59_third_jet_gate.py` | `ae26a79cbfa7bb50fbb398d7d6c18478adf7627e` |

La théorie utilisée est la formulation sphérique ADM avec deux actions Einstein–Hilbert positives, interaction Hassan–Rosen, deux poussières mobiles et **SIX couples canoniques**. Les gradients et les expressions `H_g,H_f,C` proviennent de l'original Step45, les coefficients temporels de l'original Step58.

Le Step58 prouve sur `F_z=H_g=0` l'annulation exacte des dérivées secondes des lapses. On a donc, avec `N,M` indépendants,

\[
\dot C_{\rm red}=A_N N+B_N N'+A_M M+B_M M'.
\]

Au Step59, nous avions montré uniquement que les **parties principales** d'ordre trois de `B_N` et `A_M` étaient proportionnelles aux dérivées des contraintes `H'_g` et `C'_{\rm red}`. **La présente étape utilise les dérivées complètes**, sans supprimer leurs contributions d'ordre inférieur.

## 2. L'équation du déplacement relatif est prolongée jusqu'à `z''`

Dans la branche stationnaire `K>0` :

\[
F_z=D_g-\frac{Kz}{\sqrt{1-z^2}}=0,\qquad
z=\frac{D_g}{\sqrt{D_g^2+K^2}}.
\]

Posons

\[
Z_D=\frac{(1-z^2)^{3/2}}{K},\qquad Z_K=-\frac{z(1-z^2)}{K}.
\]

La dérivation radiale TOTALE donne exactement

\[
z'=Z_DD'_g+Z_KK',
\]

\[
\boxed{z''=Z_DD''_g+Z_KK''+(Z_D)'D'_g+(Z_K)'K'.}
\]

Les dérivées de `Z_D,Z_K` conservent la dépendance en `z'`. Pour appliquer ces expressions au profil physique, il faut y substituer la vraie valeur stationnaire de `z'` ; figer `z''` serait mathématiquement faux. Les jets canoniques d'ordre trois proviennent notamment de `D''_g`, en raison du terme original `-L_gp'_{L_g}` dans `D_g`.

## 3. Théorème : les dérivées troisièmes disparaissent des résidus COMPLETS

La dérivée `H'_g` est obtenue par dérivation totale de toute la densité primaire originale. La dérivée `C'_{\rm red}` est obtenue par dérivation totale de **toute** la secondaire originale `C(q,q',z,z')`, puis substitution de la véritable expression stationnaire `z''`. On ne remplace **pas** ces contraintes par leurs seules parties principales.

Sur `F_z=0`, le jet canonique `p'_{L_g}` est éliminé en respectant

\[
p'_{L_g}=\frac{p_{S_g}S'_g+p_g\theta'_g-Kz/\sqrt{1-z^2}}{L_g}.
\]

On forme les deux expressions **COMPLÈTES**

\[
\boxed{R_N=B_N+\frac{1-z^2}{L_gL_f}H'_g}
\]

\[
\boxed{R_M=A_M-\frac{z}{L_f}C'_{\rm red}}.
\]

Le calculateur Step60 dérive symboliquement les deux résidus par rapport aux **douze jets canoniques d'ordre trois indépendants**. Toutes les dérivées sont **EXACTEMENT NULLES** une fois `F_z=0` imposé. Les quatre annulations non triviales sont :

\[
\frac{\partial R_N}{\partial S'''_g}=0,\qquad
\frac{\partial R_M}{\partial p'''_{L_g}}
=\frac{\partial R_M}{\partial S'''_g}
=\frac{\partial R_M}{\partial\theta'''_g}=0.
\]

Les huit autres jets de troisième ordre ne figurent pas dans ces expressions dès le départ ; les dépendances sont affines, sans produits cachés de jets d'ordre trois.

**DÉDUCTION RIGOUREUSE :** `R_N` et `R_M` sont entièrement indépendants des douze `q'''` sur cette surface de stationnarité. Des représentants normaux ne contenant que les jets d'ordre inférieur sont effectivement construits dans le programme, *après* vérification de l'identité. On ne met donc pas arbitrairement des dérivées troisièmes à zéro.

Sur une solution radiale qui satisfait exactement `H'_g=C'_{\rm red}=0`, ces résidus coïncident avec les coefficients temporels correspondants, mais **ils ne sont PAS démontrés nuls eux-mêmes**.

## 4. Deux contrôles négatifs importants

Les tests ne se limitent pas à contrôler des annulations voulues :

1. Si l'on soustrait le **mauvais signe** de `H'_g`, au lieu de l'ajouter, on obtient rigoureusement
   \[
   \partial_{S'''_g}\left(B_N-\frac{1-z^2}{L_gL_f}H'_g\right)
   =-\frac{4M_g^2S_g(1-z^2)}{L_fL_g^2}\ne0.
   \]
2. Si l'on **fige artificiellement `z''=0`** dans la dérivée de la secondaire, on obtient
   \[
   \partial_{p'''_{L_g}}\left(A_M-\frac{z}{L_f}C'_{\rm faux}\right)
   =\frac{z(1-z^2)}{L_f^2},
   \]
   généralement non nul lorsque le déplacement relatif l'est.

Les tests détecteraient donc une soustraction incohérente ou l'oubli de la réponse fonctionnelle de `z`.

## 5. Exécution et sauvegarde

Nouveau code : `numerics/hr_step60_full_constraint_prolongation.py`, Git blob **`9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`**.

12 nouveaux tests : `tests/test_hr_step60_full_constraint_prolongation.py`, Git blob **`1e9a0f227af3795297de882964b53337225db9ce`**.

Les deux nouvelles empreintes ont été **vérifiées sur GitHub et comparées exactement aux octets exécutés localement**. Le nouveau calcul passe ses 12 tests, puis tous les tests ciblés Steps57–60 ont été exécutés **ENSEMBLE** :

```bash
cd /mnt/data/janus-step58
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q \
  tests/test_hr_step57_secondary_principal_symbol.py \
  tests/test_hr_step58_temporal_operator.py \
  tests/test_hr_step59_third_jet_gate.py \
  tests/test_hr_step60_full_constraint_prolongation.py

# RÉEL : 56 passed in 9.23s = 12 + 15 + 17 + 12
```

Le manifeste est reproductible par `python -m numerics.hr_step60_full_constraint_prolongation`. Les faits et empreintes sont aussi sauvegardés dans `research/reports/gate2b-step60-report.json`. Ceci N'EST PAS une suite complète de tests sur l'ensemble du dépôt ; GitHub Actions demeure désactivé.

## 6. Ce qui reste à démontrer — étape 61

- Réduire les **résidus d'ordre inférieur** `R_N,R_M`, ainsi que `A_N,B_M`, modulo toutes les contraintes `H_g,H_f,D_{\rm diag},F_z,C_{\rm red}` et les prolongations compatibles de l'EDO de la solution radiale exacte et strictement positive Step55. Les représentants `third_free_BN_on_Fz` et `third_free_AM_on_Fz` sont dans le code ; ne pas en inférer leur nullité.
- Calculer l'opérateur différentiel de préservation temporelle restant sur la VRAIE branche Step55, contrôler sa régularité au centre et son rang ainsi que l'admissibilité des lapses, sans supposer d'avance un rapport fixé.
- Produire un oracle Poisson temporel indépendant, fondé sur l'action originale non intégrée par parties et les six couples, et expliciter les conditions de bord ; examiner les chartes singulières `K=0` et `J=0` séparément.

**VERDICT :** l'annulation exacte de TOUS les jets canoniques de troisième ordre après soustraction des CONTRAINTES RADIALES COMPLÈTES est démontrée pour les coefficients concernés, sur la charte `F_z=0,K>0`. Les équations temporelles de plus bas ordre, le rang de Dirac, la fixation des lapses et l'absence du fantôme BD restent **ouverts**. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**
