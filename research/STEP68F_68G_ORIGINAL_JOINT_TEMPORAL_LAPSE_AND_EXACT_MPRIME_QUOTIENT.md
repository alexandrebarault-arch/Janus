# JANUS — Étapes 68f et 68g : huit originaux exécutés ensemble, premier test du rapport des lapses, quotient exact du coefficient M'

**25 octobre 2026 — branche exclusive d'écriture :** `research/gate2b-nonhomothetic-transfer`. **GATE 2B OUVERT, JANUS-R NON VALIDÉ.**

## 1. Huit sources physiques véritablement reconstituées et exécutées ENSEMBLE

L'environnement `/mnt/data/janus-step68f` contient les huit fichiers originaux au **même Git blob SHA** que le dépôt GitHub. Les sources portent sur la formulation sphérique à six couples canoniques, deux actions Einstein–Hilbert positives, interaction Hassan–Rosen et deux poussières mobiles.

| Historique | Source originale | SHA Git original |
|---|---|---|
| Step45 | `numerics/hr_step45_exact_physical_ward.py` | `66aa43841dccfe4a5d586a49be9c10af3a67a10e` |
| Step46 | `numerics/hr_step46_exact_secondary_ode.py` | `bac025c28dbe1561c0c36c56dbfda46dc326f804` |
| Step55 | `numerics/hr_step55_normalized_secondary.py` | `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` |
| Step55 | `numerics/hr_step55_global_barrier.py` | `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` |
| Step57 | `numerics/hr_step57_secondary_principal_symbol.py` | `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f` |
| Step58 | `numerics/hr_step58_temporal_operator.py` | `802c23aebd41780d8c462f1aa1711707fe4ee88f` |
| Step59 | `numerics/hr_step59_third_jet_gate.py` | `ae26a79cbfa7bb50fbb398d7d6c18478adf7627e` |
| Step60 | `numerics/hr_step60_full_constraint_prolongation.py` | `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509` |

Dans **un seul processus Python**, ont été réellement réexécutés et ont réussi : certificat Ward original Step45, EDO affine secondaire Step46, symbole des jets Step57, annulations temporelles supérieures Step58, jets tiers Step59, quotient des contraintes complètes Step60, et **certificat original global Step55 sur 256 cellules rationnelles**. Les deux témoins d'invariance des barrières sont strictement :

\[
\max F_+=-\frac{1480966474499367232302129}{10000000000000000000000000000}<0,
\qquad
\min F_-=\frac{295653233337826329055403}{2000000000000000000000000000}>0 .
\]

**C'est une authentification et une réexécution conjointe de la PREUVE SPATIALE, pas une preuve de fermeture en temps.** Trace exacte : `research/reports/gate2b-step68f-original-eight-module-joint.json`, environ 8,84 secondes d'exécution.

## 2. PREMIÈRE ÉVALUATION DU VRAI CROCHET TEMPOREL SUR DES JETS RADIAUX CONTRAINTS

Le nouveau module `numerics/hr_step68f_physical_pointwise.py` construit les douze champs et leurs jets depuis les **VRAIES formules** du Step55, et les deux moments poussière depuis les primaires originales.

À rayon intérieur fixé `s0=r²>0`, on prend `U(s0)=Ustar(s0)+offset` avec `|offset|<=10^-5`, donc strictement dans la barrière certifiée `|U-Ustar|<=10^-4`. Les dérivées en ce point ne sont **pas** celles du polynôme `Ustar` : elles sont reconstruites au travers du véritable second membre `G(s,U)` de Step55 :

\[
2sU_s=G(s,U)-2U,
\]
\[
2sU_{ss}=G_s+(G_U-4)U_s,
\]
\[
2sU_{sss}=G_{ss}+2G_{sU}U_s+G_{UU}U_s^2+(G_U-6)U_{ss}.
\]

Ces relations déterminent le jet local d'une solution de l'EDO physique. Les constantes sont issues des intervalles rationnels historiques Step55 (milieux utilisés ici pour évaluer numériquement). On construit ensuite `q,q',q'',q''',q''''`, sans supprimer les poussières ou la variation du shift.

L'original `physical_operator()` de Step58 produit le crochet complet
\[
\dot C=A_NN+B_NN'+D_NN''+A_MM+B_MM'+D_MM''.
\]

**Au point `r=0,4` :** évaluation `mpmath` à 55 chiffres :

```text
|Fz|,|Hg|,|Hf|,|C|,|Hg'|,|C'| < 2 × 10^-54
B_N, B_M, D_N, D_M = O(10^-54)
A_N = +556.3983109239983805209505844...
A_M = -1071.784882043146390125740547...
rapport candidat M/N = -A_N/A_M
                   = +0.5191324492871505994400431975...
```

La formule est un **constat numérique de l'opérateur temporel ORIGINAL**, sur un **jet local de l'EDO physique** ; elle n'est ni une identité symbolique prouvée sur toutes les contraintes ni une condition aux bords.

Au total, sur 17 rayons distincts examinés entre `0,05` et `0,85`, les évaluations numériques donnent partout `A_N>0`, `A_M<0` et un ratio local `M/N>0`. La valeur varie approximativement de `0,518552348` à `0,521119910`, avec variation régulière dans cet échantillon. Aux rayons `0,2;0,4;0,6;0,8`, `B_N,B_M,D_N,D_M` ont été revérifiés à haute précision. Deux contrôles à `r=0,4`, `offset=±10^-5`, conservent le signe positif et un ratio voisin de `0,51913`.

**Contrôle négatif :** après une modification volontaire, NON physique, `pSf += 0,001` à `r=0,4`, en laissant les autres jets inchangés, on obtient `C ≈ -0,18355984`, `Hf≈0,00037430` et `B_N≈-0,000733887` ; les annulations précédentes ne sont donc pas triviales.

### Limitation impérative

Ces valeurs **ne sont pas des bornes par intervalles** sur les coefficients temporels. Les valeurs initiales `U(s0)=Ustar(s0)+offset` définissent des jets locaux de l'EDO, pas obligatoirement le même prolongement du centre analytique exact Step49–55. Même pour les valeurs dans le tube certifié, le **rang du Dirac et le rapport des lapses ne sont PAS certifiés sur tout le continuum**, ni avec conditions aux bords. Les nombreuses décimales affichées servent à contrôler les résidus numériques, **pas** à revendiquer une précision certifiée de la théorie ou de la branche globale.

## 3. NOUVELLE IDENTITÉ ANALYTIQUE EXACTE : le coefficient temporel B_M

À partir des trois sources originales et authentifiées Step45/57/58, le module `numerics/hr_step68g_full_Cdot_Mprime_quotient.py` considère `B_M=[\dot C]_{M'}`, et non simplement une variation du shift.

Sur `F_z=0`, avant prolongation, `B_M` dépend précisément de `p''_{L_g},S''_g,\theta''_g`, avec des coefficients en général non nuls. En dérivant l'ENTIÈRE stationnarité `F_z=D_g-Kz/\sqrt{1-z²}`, on obtient `F_z'` et on pose

\[
\lambda=\frac{3z(z^2-1)}{L_gL_f^2}
=-\frac{3z(1-z^2)}{L_gL_f^2},\qquad
\boxed{R_{B_M}=B_M-\lambda F_z'.}
\]

**IDENTITÉ EXACTE vérifiée symboliquement :** sur `F_z=0`,
\[
\boxed{\forall i=1,\ldots,12,\quad \frac{\partial R_{B_M}}{\partial q_i''}=0.}
\]

La dépendance initiale est affine en les trois jets, et le représentant sans jets seconds est vraiment construit **après** la vérification des dérivées. Sur les données satisfaisant `F_z=F_z'=0`, `R_{B_M}=B_M`. Un mauvais signe ou l'omission du terme de prolongation préserve au contraire un coefficient non nul devant `p''_{L_g}` (contrôles négatifs).

La correction est régulière sous les parités analytiques du centre :

\[
z=rw(s),\quad F_z=r^3f(s),\quad s=r^2
\quad\Rightarrow\quad
\lambda F_z'=
-\frac{3r^3 w(1-sw^2)(3f+2sf_s)}{L_gL_f^2}=O(r^3).
\]

**Ceci ne démontre PAS `B_M=0` sur la branche Step55.** Cela enlève rigoureusement l'obstruction des jets seconds du coefficient temporel de `M'`, et permet de chercher les réductions restantes dans les jets inférieurs.

## 4. Code, tests et sauvegardes

Nouveaux blobs Git **vérifiés identiques aux sources réellement exécutées** :

- `numerics/hr_step68f_physical_pointwise.py` : `82e1ebb3a290f54a0d3b5069df67504044381626`.
- `tests/test_hr_step68f_joint_profile.py` : `5d423b4d646c6c3ac4d28884e3116bf56a35bde0`.
- `numerics/hr_step68g_full_Cdot_Mprime_quotient.py` : `2245403862795569d3d6215aeb5e6227ee1148d6`.
- `tests/test_hr_step68g_full_Cdot_Mprime_quotient.py` : `5afc5b52e260532eb94e8ecec940354eb3f12d9d`.

Tests ciblés Step68f (13), Step68g (10) et Step68e historique (18), exécutés **ENSEMBLE** :

```bash
cd /mnt/data/janus-step68f
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q \
 tests/test_hr_step68f_joint_profile.py \
 tests/test_hr_step68g_full_Cdot_Mprime_quotient.py \
 tests/test_hr_step68e_exact_shift_full_lapse_response.py
# RÉELLEMENT : 41 passed in 16.48s
```

Quatre traces **réellement produites**, copiées dans GitHub avec leurs octets exacts et relues :

- `research/reports/gate2b-step68f-original-eight-module-joint.json`
- `research/reports/gate2b-step68f-physical-highprecision-scan.json`
- `research/reports/gate2b-step68f-extended-radius-scan.json`
- `research/reports/gate2b-step68f-negative-off-primary.json`

Synthèse machine supplémentaire : `research/reports/gate2b-step68f-68g-integrated-status.json`.

Les workflows GitHub Actions restent **désactivés**. Ni `main` ni `research/v2-flrw` ne sont modifiées.

## 5. Verrou prioritaire — prochaine étape 68h

La nouveauté est une indication numérique crédible d'un rapport de lapses **positif** sur la branche radiale considérée, accompagnée d'une réduction symbolique exacte d'un coefficient temporel. Il reste absolument à :

1. Prouver analytiquement, ou certifier par intervalles sur la **vraie branche globale du centre**, `B_N=B_M=0` sur `F_z,H_g,H_f,D_{\rm diag},C` et leurs prolongations. Pour `B_M`, partir du représentant sans jets seconds de l'étape 68g. Traiter tous les jets et les dérivées des contraintes sans les figer.
2. Encadrer uniformément `A_N>0`, `A_M<0` sur `0<r\le0,85`, avec la dépendance `U(s)` certifiée par l'EDO et non un simple point `U_*`. Traiter séparément la limite `r\to0` pour démontrer l'existence et la régularité de `M/N` au centre.
3. Vérifier que les conditions aux bords et les contraintes temporelles primaires/gauge sont compatibles avec un `N>0` et le rapport `M/N` trouvé.
4. Construire un **oracle Poisson temporel indépendant de la formulation post-IBP** sur les SIX couples, avant tout verdict concernant rang complet, fantôme de Boulware–Deser et cosmologie JANUS 4D. Traiter les secteurs exceptionnels `K=0,J=0` à part.

**VERDICT À CE JOUR : le premier calcul numérique contraint du rapport des lapses est favorable sur les points testés, mais la certification temporelle, le rang de Dirac et JANUS-R restent OUVERTS et NON VALIDÉS.**
