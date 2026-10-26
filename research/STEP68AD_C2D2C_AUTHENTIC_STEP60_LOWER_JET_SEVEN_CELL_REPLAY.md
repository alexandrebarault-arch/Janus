# JANUS — 68ad-C2d2c : quotient inférieur original Step60 évalué sur sept cellules (INCOMPLETE)

Date : 2026-10-26. Branche unique d'écriture : `research/gate2b-nonhomothetic-transfer`.

## 1. Question et provenance

L'étape précédente avait réellement exécuté l'opérateur temporel original Step58 sur sept cellules mais pas les deux représentants inférieurs du quotient original Step60. Cette étape comble **ce manque d'exécution**, sans revendiquer de signe continu, de rang de Dirac ou de solution de lapse.

Un environnement Python commun a été reconstruit depuis le connecteur GitHub avec **24 fichiers sources/tests/rapports, 24/24 empreintes Git blob authentifiées sur les octets réellement exécutés**. Le moteur original Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, le quotient original Step60 `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7` et les trois rapports physiques pinnés sont inchangés. La campagne de non-régression antérieure a été rejouée.

## 2. Expressions originales et réécriture exacte

`full_constraint_prolongation()` fournit les deux représentants originaux dont les troisièmes jets ont été éliminés **après** soustraction des dérivées complètes des contraintes :

- `third_free_BN_on_Fz = B_N + (1-z²)/(Lg Lf) * Hg'`, avec élimination de `pLg'` par la stationnarité ;
- `third_free_AM_on_Fz = A_M - z/Lf * C_red'`, avec le même traitement et `z''` prolongé exactement.

Le programme authentifie l'annulation des jets d'ordre trois avant de les écarter. La compilation par SymPy CSE donne un dénominateur d'interaction original `T = beta1*Sg² + 2*beta2*Sg*Sf + beta3*Sf²` aux positions **103** (BN) et **107** (AM). La preuve symbolique redéveloppe les CSE antérieurs et vérifie exactement l'identité, puis vérifie sur `Sg=r Lg`, `Sf=r Lf`, `r>0`, `Lg>0` :

`T = Sg² * [beta1 + 2 beta2 (Lf/Lg) + beta3 (Lf/Lg)²]`.

Le code remplace **uniquement l'évaluation** de ce dénominateur dans les deux expressions originales, sans toucher les fichiers historiques. Cette opération est valable sur la coquille stationnaire positive `K>0`, `Fz=0` et avec la substitution originale de `pLg'` ; elle ne constitue pas une identité hors coquille. Le backend original `I` utilise une grille rationnelle à arrondi extérieur `10^-28`, et les boîtes `U,U_s,U_ss,U_sss` sont recalculées sur le **domaine effectivement arrondi**.

## 3. Résultat continu sur les sept cellules

**7/7 cellules exécutées ; 14/14 enclosures calculées ; 0/14 signes continus certifiés.** Toutes les enclosures `BN` et `AM` contiennent strictement zéro, donc leur classification est **INCOMPLETE**. Les bornes exactes sont dans `research/reports/gate2b-step68ad-C2d2c-original-Step60-lower-quotient.json` ; les décimales ci-dessous ne sont qu'un résumé.

| Rayon | BN intervalle approx. | AM intervalle approx. |
| --- | ---: | ---: |
| [1/64,1/56] | [-311.105,309.715] | [-8224.506,8207.707] |
| [1/56,9/448] | [-242.270,241.247] | [-5998.400,5979.382] |
| [9/448,5/224] | [-195.197,194.434] | [-4584.566,4563.163] |
| [5/224,11/448] | [-161.533,160.964] | [-3631.695,3607.750] |
| [11/448,3/112] | [-136.589,136.171] | [-2959.316,2932.681] |
| [3/112,13/448] | [-117.569,117.270] | [-2467.232,2437.762] |
| [13/448,1/32] | [-102.716,102.515] | [-2096.273,2063.824] |

Ces enclosures contiennent les valeurs du quotient sous les hypothèses certifiées des rapports spatiaux antérieurs. Le passage par zéro de **l'intervalle calculé** n'établit pas l'existence d'une racine physique.

## 4. Vérifications ponctuelles indépendantes

Les **huit frontières** ont été évaluées avec les mêmes sources et le même backend. Les huit enclosures de `AM` sont strictement négatives : valeurs centrales indicatives de `-1.65138589` à `-6.60524937`. Les huit enclosures de `BN` contiennent zéro et ont une largeur maximale d'environ `7.71e-15`. Les huit enclosures `AM` intersectent les enclosures du coefficient `A_M` de Step58 original, comme attendu si `C_red'` s'annule sur la coquille spatiale.

**Attention :** ni la proximité numérique de `BN` avec zéro, ni les huit signes négatifs de `AM`, ni les intersections d'intervalles ne prouvent une identité exacte, un signe sur tout le continuum, ou le rang d'un opérateur différentiel.

## 5. Tests et reproduction

Dans un checkout de la branche contenant les sources originales et les trois rapports SHA-pinnés :

`PYTHONPATH=. python -m numerics.hr_step68ad_c2d2c_step60_lower_quotient_replay --repo . --out research/reports/gate2b-step68ad-C2d2c-original-Step60-lower-quotient.json`

`PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2c_step60_lower_quotient_replay.py tests/test_hr_step68ad_c2d2b_executed_temporal_probe.py tests/test_hr_step68ad_c2d2b_guard.py tests/test_hr_step68ad_c2d2a_temporal_replay.py tests/test_hr_step58_temporal_operator.py tests/test_hr_step60_full_constraint_prolongation.py`

**88 PASS, 0 FAIL**, dont 9 nouveaux tests et 79 tests précédents. Les tests contrôlent les empreintes, l'originalité des CSE, le rejet d'un mauvais dénominateur, la couverture sans trou, la classification INCOMPLETE, les huit évaluations ponctuelles, la cohérence d'intersection avec Step58 et la restauration du compilateur original.

## 6. Verdict et priorité

**`GATE_2B OPEN` ; `JANUS_R NOT_VALIDATED`.** L'étape **68ad-C2d2c a réellement évalué les représentants inférieurs Step60 sur les sept cellules**, mais le résultat demeure **INCOMPLETE** : 0/14 signes continus Step60 et toujours 0/14 Step58. La suppression des troisièmes jets est une preuve algébrique conditionnelle, pas une preuve du rang complet de Dirac. Les lapses admissibles, conditions aux bords, dynamique 4D, stabilité et observables restent ouverts.

**Prochaine difficulté effective :** conserver les corrélations radiales dans les opérateurs originaux Step58/Step60 (factorisation globale sur la coquille, modèle de Taylor avec majorant de reste prouvé ou arithmétique affine validée), plutôt que multiplier les seules subdivisions ou échantillons ponctuels. Tout certificat futur doit prouver l'inclusion sur les sept cellules entières ; si zéro reste dans l'enclosure, rester INCOMPLETE. Examiner ensuite le système différentiel de lapses et son rang, sans le déduire des signes de deux coefficients isolés.
