# JANUS b3c3d6 — premier probe numérique COMPLET de l'opérateur Step58 original sur Step55 (29/10/2026)

**Verdict : progrès expérimental reproductible, NON théorème. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Ce qui a réellement été exécuté

- Octets des moteurs **originaux** Step45, Step46, Step55-normalized, Step55-global-barrier et Step58 reconstruits localement et vérifiés contre les Git blob SHA : respectivement `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `bac025c28dbe1561c0c36c56dbfda46dc326f804`, `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, `802c23aebd41780d8c462f1aa1711707fe4ee88f`.
- **Step57 complet NON exécuté** : shim minimal d'import pour le moteur Step58, explicitement déclaré.
- **Step55 original** : `certify_global_barrier(cells=256)` exécuté et PASS. L'EDO radiale originale normalisée `2s U_s=G(s,U)-2U` est intégrée numériquement par DOP853, rtol `1e-12`, atol `1e-14`, depuis la série centrale jusqu'à quatre rayons. Les constantes géométriques Step55 ont été transcrites en mpmath et comparées point par point aux intervalles du moteur Step55 original (tolérance d'arrondi mpmath `1e-40`, **pas** un nouveau certificat d'intervalle temporel).
- **Step58 original** : `physical_operator()` complet, avec ses **six coefficients** `A_N,A_M,B_N,B_M,E_N,E_M`, évalué à `r=1/4,1/2,7/10,17/20` sur les jets Step55 et `pLf'=r G(s,U)`. Les valeurs de `pSf,pf` viennent des primaires originales Step46. Les résidus `Fz,Hg,Hf,C` sont inférieurs à `9e-45` à 45 décimales ; les jets d'ordre supérieur effectivement présents dans Step58 ont été calculés. Une répétition à 70 décimales a confirmé le changement d'échelle des résidus vers `<1e-60`.
- **5 tests unittest PASS, 0 FAIL**, non indépendants. Commande : `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m unittest tests.test_hr_b3c3d6_full_original_step58_point_probe -v` ; 13,078 s dans l'exécution locale. Les contrôles négatifs hors coquille `pSg' += 0.01` donnent `B_N≈-0.0879797594`, `B_M≈-0.00191798592`, donc les coefficients ne sont pas identiquement nuls hors coquille.

## Résultats numériques nouveaux

| r | A_N | A_M | -A_N/A_M | max abs(B_N,B_M,E_N,E_M) |
|---|---:|---:|---:|---:|
| 1/4 | 218.4855763 | -421.1571062 | 0.5187745216 | < 6e-45 |
| 1/2 | 865.1666034 | -1665.5134395 | 0.5194593949 | < 2e-44 |
| 7/10 | 1673.8606391 | -3217.0155459 | 0.5203147499 | < 3e-44 |
| 17/20 | 2437.0939964 | -4676.6472342 | 0.5211199123 | < 2e-44 |

**Observation importante :** les quatre coefficients de jets de lapses `B_N,B_M,E_N,E_M` sont numériquement compatibles avec une annulation **sur la solution Step55**. Cela suggère de rechercher une factorisation exacte de `B_N,B_M` par les contraintes `Fz,Hg,Hf,C` et leurs dérivées. L'ancienne discussion des cartes `B_M≠0` pourrait être inapplicable à cette coquille spécifique, mais **aucune identité exacte n'est encore démontrée**.

**Conséquence STRICTEMENT CONDITIONNELLE :** si les quatre coefficients de jets s'annulent exactement sur la solution et si `A_M≠0`, la préservation temporelle impose localement `M/N=-A_N/A_M`. À `R=17/20`, la condition de bord **supplémentaire** `N(R)=M(R)>0` serait alors incompatible avec la relation locale, puisque `A_N+A_M≈-2239.5532378`. Cette égalité des lapses au bord est une hypothèse de bord particulière, **pas** une obligation physique générale, et les nombres ci-dessus ne sont pas des bornes certifiées.

## Limites et prochaine étape

Le test est un **probe numérique à quatre points**, non une preuve uniforme des signes, des zéros, des dérivées, du centre ou du problème aux deux vrais bords. L'intégration DOP853 n'est pas une intégration à erreur rigoureusement bornée. Les 70 décimales testent l'annulation algébrique à jets construits, **pas** la précision globale de `U(R)` issue du solveur double. La jauge temporelle, les générateurs/charges, le pullback Dirac, les six couples, les secteurs `K=0/J=0`, la dynamique 4D, la stabilité et les observables restent ouverts.

**Prochaine action b3c3d6 :** factoriser exactement `B_N,B_M` sur les contraintes Step55/Step58 (et tester des contre-exemples), puis certifier `A_N>0,A_M<0` et `A_N+A_M<0` par arithmétique rationnelle/intervalle sur `0<r≤17/20`, raccord central et deux bords. Ne conclure ni no-go global ni validation JANUS avant le traitement Dirac complet.

## Fichiers et commande

- `numerics/hr_b3c3d6_full_original_step58_point_probe.py` : exécution originale et contrôles négatifs.
- `tests/test_hr_b3c3d6_full_original_step58_point_probe.py` : 5 tests.
- `research/reports/gate2b-b3c3d6-original-step58-numeric-summary.json` : six coefficients, quatre rayons et provenance.

Aucun changement autorisé hors de `research/gate2b-nonhomothetic-transfer`. Aucun workflow GitHub Actions activé.
