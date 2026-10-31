# b3c3d6 — premier rejeu physique des dérivées composées, quatre rayons exacts (31 octobre 2026)

**Statut : GATE_2B OPEN ; JANUS_R NOT_VALIDATED ; b3c3d6 PARTIELLE.**

## Exécution et authenticité

Quatre sources originales **octet pour octet** du Step45/46/55 ont été récupérées via le connecteur GitHub, recopiées dans un environnement Python isolé et authentifiées par leurs **Git blob SHA-1** :
- Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ;
- Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804` ;
- Step55 normalisé `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` ;
- Step55 barrière `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.

La **barrière originale 256 cellules a réellement été réexécutée avec succès**. Le candidat de différentiation automatique composé publié précédemment (blob `170598ab5ceff3ba6e9fa26575b4c0fed3a36c0a`) a été exécuté sur la véritable expression Step45/46 normalisée. Son premier calcul direct `G(s,[U-,U+])` était valide mais très large par dépendance d'intervalles. Le nouveau module certifie `G_U<0` sur le tube complet de chaque `s=r²` exact, puis utilise la monotonie en `U` et les évaluations originales sortantes aux **deux extrémités** :

`G(s,[U-,U+]) ⊂ [ lower(G(s,U+)), upper(G(s,U-)) ]`.

Cette dernière boîte est certifiée par le théorème des accroissements finis et l'arithmétique entière sortante originale `I` ; aucune hypothèse de monotonie radiale globale n'est faite. Le `G_s` physique est la dérivée à `U` fixé **incluant toutes les dérivées de géométrie prescrite**.

## Résultats certifiés aux quatre points, et seulement à ces points

| r exact | G_s composé | G_U | pLf''(r) | gain de largeur G |
|---|---|---|---|---|
| 1/4 | [0,00383732 ; 0,00404203] | [-0,999786 ; -0,999605] | [-0,0103265 ; -0,00950106] | 18,51× |
| 1/2 | [0,00380952 ; 0,00401542] | [-0,999113 ; -0,998385] | [-0,00860562 ; -0,00770363] | 18,64× |
| 7/10 | [0,00377385 ; 0,00398128] | [-0,998187 ; -0,996750] | [-0,00643493 ; -0,00543308] | 18,80× |
| 17/20 | [0,00373920 ; 0,00394814] | [-0,997221 ; -0,995087] | [-0,00436632 ; -0,00326587] | 18,97× |

Les décimales ci-dessus sont **indicatives et arrondies** ; les bornes exactes sont les fractions du certificat JSON. Ainsi `G_s>0`, `G_U<0` et `pLf''<0` sont effectivement démontrés **aux quatre rayons** sur le tube Step55 ; `U_s>0` est démontré à `r=1/2,7/10,17/20`, pas à `1/4`. Les quatre enclosures de `U_ss` existent dans la sortie intégrale de `certify_four_radii()`, mais **contiennent zéro** ; aucun signe de `U_ss` n'est revendiqué. Le rayon `17/20` est évalué exactement à `s=289/400` ; aucun dépassement binary64 n'est utilisé.

## Tests et reproductibilité

Exécutés dans le conteneur local sur les sources SHA-authentifiées : `PYTHONPATH=. python -m unittest discover -s tests -v` : **4 PASS, 0 FAIL** (rejeu physique quatre rayons et barrière, quatre SHA, témoin rationnel de monotonie, rejet d'un signe non prouvé). `python -m compileall -q numerics tests` : **PASS**. `PYTHONPATH=. python -m numerics.hr_b3c3d6_monotone_physical_four_radii` : **PASS**, certificat rationnel généré. Le script `hr_b3c3d6_physical_correlated_replay` complet n'a **pas** été exécuté : seul son rôle d'authentification a été remplacé localement par un vérificateur SHA minimal explicite, indépendant du nouveau module. Le DOP853 original et Step58 ne sont **pas** rejoués.

Fichiers : `numerics/hr_b3c3d6_monotone_physical_four_radii.py`, `tests/test_hr_b3c3d6_monotone_physical_four_radii.py`, `research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json`. Le certificat contient les fractions exactes pour `G,G_s,G_U,pLf''`, et les indicateurs de signe.

## Prochain verrou

Ces enclosures ne sont **pas** des enclosures des six coefficients `A_N,A_M,B_N,B_M,E_N,E_M` du Step58 ; aucune factorisation exacte de leurs annulations numériques, aucun problème global de lapses positifs à deux bords, ni aucune analyse Dirac complète, évolution 4D, stabilité ou observables n'est certifié. Prochaine étape : employer les jets ponctuels certifiés dans le **moteur original Step58 SHA-authentifié**, propager les intervalles et tenter les six enclosures ; affiner `U` par DOP853 corrélé aux rayons exacts seulement si nécessaire. Un certificat ponctuel à quatre rayons ne prouve aucun signe sur tout l'intervalle.
