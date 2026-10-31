# b3c3d6 — Dérivées physiques composées par différentiation automatique d'intervalles (31/10/2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED. Travail d'instrumentation, pas un nouveau certificat physique.**

## Résultat technique vérifié

Le Step55 original définit `G(s,U)=E(s,U,v_1(s),...,v_k(s))` et exige `G_s=E_s+Σ E_vi v_i'(s)` à `U` fixé. Un adaptateur à nombres duaux `(valeur,dérivée)` applique exactement la règle de chaîne aux opérations rationnelles et racines carrées, avec intervalles sortants lorsqu'il reçoit le type `I` du Step55. Il refuse `abs` sur un intervalle traversant zéro, ainsi que les divisions par des intervalles contenant zéro.

**Point d'intégration important :** la fonction originale `geometry(s)` utilise des constantes `I` à gauche des produits (`A*ug**2`), et `I.__mul__` ne délègue pas à un objet dual. Le candidat clone uniquement le dictionnaire de variables globales de la fonction en relevant les constantes `I` vers des nombres duaux à dérivée nulle. Le code source original, ses globals et ses SHA restent intacts. Deux passes indépendantes donnent `G_s` (semence `ds=1,dU=0`) et `G_U` (semence `ds=0,dU=1`).

Le candidat `original_physical_boxes_at_four_radii()` authentifie les sources Step45/46/55 via le module de rejeu existant, **réexécute la barrière originale de 256 cellules s'il est appelé**, évalue les quatre rayons exacts `1/4,1/2,7/10,17/20`, puis combine `U,G,G_s,G_U` avec l'enclosure directe publiée pour `U_s,U_{ss},pLf''`. Il utilise le tube de barrière `Ustar±1/10000` (potentiellement plus large que le tube DOP853) et ne requiert pas de dépassement binary64.

## Tests réellement exécutés dans cette session

`cd /mnt/data/janus_ad_20261031 && PYTHONPATH=. python -m unittest discover -s tests -v` : **9 tests PASS, 0 FAIL**. `python -m compileall -q numerics tests` : **PASS**. Tests de la règle de chaîne avec géométrie variable aux quatre rayons rationnels, enveloppe d'intervalle sur neuf couples de points, division/sqrt, signe de abs, garde de symbole manquant, clone des constantes sans mutation et rejet de division par zéro.

**NON EXÉCUTÉ :** `original_physical_boxes_at_four_radii()`, car le conteneur de calcul ne dispose pas du checkout authentifié Step45/46/55/58 et l'accès direct à raw.githubusercontent.com échoue (ConnectionError/DNS). Les sources ont été **lues en direct** via le connecteur GitHub, mais aucun moteur original n'a été importé/rejoué dans le conteneur. Aucun `G_s` physique, `U_{ss}` physique, six coefficients Step58, BVP positif aux deux bords, Dirac/4D/stabilité/observables n'a été certifié dans cette session. La validité numérique et la largeur des intervalles de ce candidat restent à établir par un vrai rejeu.

## Provenance des octets testés

- `numerics/hr_b3c3d6_composed_dual_interval_jets.py` : Git blob `170598ab5ceff3ba6e9fa26575b4c0fed3a36c0a`.
- `tests/test_hr_b3c3d6_composed_dual_interval_jets.py` : Git blob `9d35930b07603e94e40088e81eea887d6d5d87a2`.
- Sources originales consultées : Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 normalisé `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, barrière `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Le code de rejeu authentifiant Step45/46/55 est `47a0c80cea2554daf62f3fea9ffb7f28421ae22c`.
- GitHub a relu les deux fichiers publiés et confirmé des SHA de blobs identiques à `git hash-object` sur les fichiers réellement testés.

## Prochaine étape scientifique

**Ne pas assimiler ce candidat à une certification.** Exécuter `original_physical_boxes_at_four_radii()` sur checkout authentifié ; vérifier toutes les opérations de l'expression originale, le passage des 256 cellules et les intervalles physiques `G_s,G_U,G,U_{ss},pLf''`. Si la barrière seule donne des boîtes trop larges, les resserrer à l'aide du certificat DOP853 corrélé aux quatre rayons exacts. Rejouer Step58 original, certifier six coefficients A/B/E, factoriser, puis résoudre ou exclure les lapses strictement positifs aux deux vrais bords. Poursuivre seulement ensuite Dirac, 4D, stabilité et observables.
