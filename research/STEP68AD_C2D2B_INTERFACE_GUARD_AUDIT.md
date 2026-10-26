# JANUS — 68ad-C2d2b : audit fail-closed de l'interface temporelle (Step58/60 encore NON exécutés)

Date : 2026-10-26. **Nature : correctif de sûreté de preuve, pas certificat physique temporel.**
Statut inchangé : `GATE_2B OPEN`, `JANUS_R NOT_VALIDATED`.

## Défauts concrets identifiés dans l'adaptateur 68ad-C2d2a

1. `evaluate_original_step58(box,...)` recalculait `expected_s=I.hull(rlo,rhi)**2` mais **ne vérifiait pas que `box["s"]` et les quatre intervalles de dérivées provenaient de cette même cellule arrondie**. L'injection vérifiait seulement que l'original Step68o demandait `expected_s`, non que le jet injecté était attaché à ce domaine. Un appel direct avec une boîte périmée pouvait donc traverser la frontière de validité d'une preuve.
2. Le booléen `seven_temporal_signs_certified` confondait potentiellement, à la lecture, « les deux coefficients excluent zéro » et « les signes historiques attendus N positif / M négatif sont reproduits ». Ces deux propositions sont distinctes : une orientation inverse peut être rigoureusement non nulle sans confirmer le motif historique.

## Correction publiée

- `numerics/hr_step68ad_c2d2b_guard.py` vérifie, **avant** toute injection dans Step68o, la présence du garde d'arrondi, l'égalité rationnelle exacte entre les deux bornes `s` de la boîte et le domaine entier `I.hull(rlo,rhi)**2`, la limite `s≤1/1024` et l'intégrité des quatre paires `U,U_s,U_ss,U_sss`. Une boîte périmée ou mal formée est rejetée.
- L'adaptateur `numerics/hr_step68ad_c2d2a_temporal_replay.py` appelle maintenant cette vérification avant `evaluate_cell`. Les sources originales Step45/55/58/60/68n/68o restent inchangées.
- La sortie distingue désormais `all_nonzero_signs_certified` et `all_expected_N_positive_M_negative` ; les coefficients indéterminés et les orientations contraires sont explicitement listés. `seven_temporal_signs_certified` conserve sa signification historique « non-zéro », pour compatibilité.

## Exécutions et provenance réellement vérifiées

- **12 tests Python PASS, 0 FAIL** sur le nouveau module de garde pur, exécutés localement : `cd /mnt/data/janus_c2d2b_guard && PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2b_guard.py` (0,06 s). Les deux fichiers publiés (module et tests) sont byte-identiques aux fichiers locaux exécutés, Git blobs `a0657a023fc59073bd1ab9f9a4255cf5248e0b9b` et `0daa20efbe1df763b91ba01268e25daf81d89731`.
- **6/6 SHA Git originaux indépendamment recalculés sur le texte complet du connecteur** : Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step60 `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`, Step68n `96370e0599748c6dc07faf339ab3646ae3474e7d`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7`, C2b `94928e285f7e04deaf546abbeb9d3f05db33b213`.
- **7/7 cellules** de la plage `[1/64,1/32]` contrôlées par calcul rationnel local indépendant à partir des bornes reportées par Step68v/68ac/B2, avec couverture arrondie `s≤1/1024`, intersections cubique/monotonie non vides et largeur U maximale ≈ `1.0624409173110848e-7`. Il s'agit d'un contrôle de cohérence des données, pas d'un rejeu du vrai moteur Step58.
- **Tests d'intégration du module original 68ad-C2d2a MODIFIÉ : NON EXÉCUTÉS** dans un checkout complet ; seule la source publiée a été relue et authentifiée. **Vrai Step58 sur sept cellules : NON EXÉCUTÉ. Vrai quotient Step60 : NON EXÉCUTÉ. Signes temporels nouveaux : 0.**

## Blocage exact et suite

Le connecteur GitHub lit et écrit normalement, mais le conteneur Python ne peut ni résoudre `github.com` ni établir une connexion HTTPS directe, et ne possède pas de checkout JANUS. Les dépendances originales complètes ne peuvent donc pas être importées dans ce conteneur par `git clone`. Ne jamais convertir ce défaut d'environnement en un faux résultat scientifique.

**NEXT = 68ad-C2d2b (reste PENDING, pas terminé scientifiquement)** : obtenir une copie byte-authentifiée de toutes les dépendances et des trois rapports dans le même environnement Python, rejouer les 20 tests d'origine + les 12 nouveaux, puis exécuter effectivement `run()` avec les sept cellules et contrôler les 14 coefficients N/M. Après cela seulement, prolonger les contraintes avec le vrai Step60, vérifier la cohérence des lapses, du rang de Dirac et des bords. Les résultats qui recouvrent zéro restent `INCOMPLETE`.

Aucun commit sur `main`, `research/v2-flrw` ou GitHub Actions/workflows n'est autorisé.
