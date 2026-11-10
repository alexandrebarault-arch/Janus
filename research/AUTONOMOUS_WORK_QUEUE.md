# JANUS — FILE DE TRAVAUX AUTONOME ET POINT DE REPRISE

**Version :** 1 — 2026-11-08. **Branche :** `main` exclusivement.
**HEAD de référence lors de l'initialisation :** `058ca4a8fd211efe6552883cfd389e02741a50fa`.
**État scientifique :** `GATE_2B = OPEN` ; `JANUS_R = NOT_VALIDATED`.
**Dernier résultat exécuté connu :** 2026-11-05, 9/9 tests authentifiés `test_hr_b3c3d9_annular_direct_enclosure.py` PASS. Ce résultat n'est pas une certification physique.
**Dernier calcul physique du pilote :** aucun ; 0 cellule Step55/58 calculée et 0 certifiée dans la dernière session rapportée.
**Blocage constaté :** `git ls-remote` → `Could not resolve host: github.com` depuis le conteneur, alors que le connecteur GitHub permet la lecture ; reconstruction locale incomplète (premier import manquant : `numerics/hr_step55_global_barrier.py`).
**Curseur de reprise :** `JANUS-001`, reconstruire les dépendances transitives et les sources historiques exactes, puis rejouer le pilote.
**Dernière mise à jour de ce document :** 2026-11-08 (initialisation organisationnelle, aucun nouveau calcul).

## Contrat de reprise — impératif à chaque lancement du job

1. Lire le HEAD réel de `main`, puis à ce SHA : ce fichier, `research/AUTOMATION_STATE.json` et le début de `00_CURRENT_RESTART.md`. Vérifier les preuves associées à l'étape annoncée. En cas de divergence, les résultats et leurs preuves prévalent sur les marqueurs ; ne pas déclarer `DONE` sans preuve.
2. Reprendre d'abord toute tâche `RUNNING` interrompue **à son dernier jalon vérifié**, pas à son intention déclarée. Rejouer ou vérifier les résultats si les artefacts sont absents. Si `main` a changé, examiner les changements avant de continuer.
3. Choisir la première tâche `READY` non bloquée ; si elle devient `BLOCKED`, essayer une solution réaliste puis passer à une autre tâche indépendante utile. Ne pas répéter une commande identique vouée à la même erreur sans changement de prérequis.
4. Travailler en **boucle autonome durant toute la session disponible** : hypothèse → protocole → exécution réelle ou démonstration → contrôle contradictoire → rapport vérifiable → publication → tâche suivante. Ne pas s'arrêter après la première sous-étape réussie et ne pas demander au propriétaire de choisir les priorités scientifiques ordinaires.
5. **Avant une étape longue ou risquée**, noter dans ce fichier `RUNNING`, le HEAD de départ, la commande exacte, les entrées, le prochain jalon et le fichier de sortie prévu si cette tâche n'a pas déjà un marqueur exploitable. **Après chaque jalon vérifié**, publier un petit checkpoint (artefact + état) avant de commencer la suivante. Une interruption ne doit faire perdre au plus que le travail non publié depuis ce jalon.
6. Pour chaque tâche, noter : identifiant stable, statut `READY/RUNNING/BLOCKED/DONE/INVALIDATED`, priorité, dépendances, dernière preuve (chemin + SHA), **prochaine commande ou action exacte**, obstacle et condition de déblocage. Ajouter les tâches découvertes, éliminer ou réviser les tâches devenues non pertinentes, sans effacer l'historique des résultats négatifs.
7. Publier sur `main` seulement des artefacts nouveaux et vérifiés ou un vrai changement d'état utile à la reprise ; ne pas créer de commit ou de rapport identique chaque heure. Lire le HEAD avant chaque publication, vérifier l'absence de conflit, ne jamais forcer ni réécrire l'histoire. Conserver tags, workflows désactivés et une seule branche. Après écriture relire HEAD et blobs. Si GitHub est en lecture seule, conserver les artefacts localement pour la session et expliquer honnêtement la perte possible à l'interruption.
8. Garder `research/AUTOMATION_STATE.json` cohérent avec la dernière étape scientifique vérifiée. Les champs historiques concernant l'état du job peuvent être périmés : l'état réel du job se vérifie dans l'outil Automations, pas dans ce JSON. Ne pas réécrire l'intégralité de `00_CURRENT_RESTART.md` à chaque session (fichier historique volumineux). Y ajouter un checkpoint concis seulement lors d'un jalon scientifique substantiel, en conservant l'historique.
9. Ne pas présenter une intention `RUNNING`, une simple tentative, un test synthétique ou une enclosion inconclusive comme une preuve physique. Séparer **cellules planifiées, tentées, effectivement évaluées, certifiées, inconclusives**. Une borne contenant zéro, une couverture trouée et des points isolés ne démontrent pas le signe strict continu.
10. Si la piste principale reste bloquée : continuer sur les audits symboliques, contre-exemples, preuves de contraintes, conditions aux vrais bords, rang, 4D, stabilité ou observables avec des livrables vérifiables. Éviter de tourner en rond. Faire figurer le premier prérequis réellement externe et l'action minimale requise ; ne pas exiger l'intervention humaine tant qu'une alternative autonome est disponible.

## Liste ordonnée des travaux

### JANUS-001 — RECONSTRUCTION ET REJEU DU PILOTE
- **Statut : READY** ; **Priorité : P0** ; **Dépendances :** aucune.
- **But :** exécuter le vrai moteur `numerics/hr_b3c3d9_annular_direct_enclosure.py` avec les octets originaux Step45/46/55/58, sans shim scientifique non justifié.
- **Prochaine action atomique :** lire à un HEAD fixé le runner, `tests/test_hr_b3c3d9_annular_direct_enclosure.py`, tous les imports directs/transitifs (notamment `hr_step55_global_barrier`, `hr_step55_normalized_secondary`, `hr_step57_secondary_principal_symbol`, `hr_b3c3d6_boundary_ANAM_interval_certificate`) et les fichiers historiques ouverts à l'exécution ; reconstruire les chemins exacts, authentifier chaque octet par SHA Git, puis lancer la suite ciblée.
- **Commandes cibles :** `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v`, puis `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`.
- **Acceptation :** compte rendu horodaté, provenance des sources, résultats effectivement exécutés, barrière Step55 authentique, une cellule réellement évaluée **ou** premier échec concret avec commande/trace et contournement vérifiable.
- **Preuve précédente :** `research/STEP68AD_B3C3D9_AUTHENTIC_NINE_TEST_EXECUTION_20261105.md` ; 9/9 PASS antérieurs, pilote arrêté avant calcul physique.
- **Blocage hérité :** DNS du Git CLI et arbre local incomplet ; le connecteur GitHub en lecture fonctionne.

### JANUS-002 — ESSAI ANNULAIRE INTÉGRAL ET TRAITEMENT DES INCONCLUSIFS
- **Statut : READY** ; **Priorité : P0** ; **Dépendances :** pilote JANUS-001 reproductible et valide.
- **Prochaine action :** exécuter `--cells 256 --out <rapport.json>`, enregistrer les lignes, valider indépendamment la couverture exacte et les signes stricts, puis subdiviser méthodiquement les cellules inconclusives si la méthode l'autorise.
- **Acceptation :** nombres séparés de cellules planifiées/tentées/évaluées/certifiées/inconclusives, bornes rationnelles et couverture ; aucune certification globale si un trou persiste.
- **Remarque :** même 256 cellules certifiées ne valident pas JANUS à elles seules.

### JANUS-003 — INFRASTRUCTURE REPRODUCTIBLE
- **Statut : READY** ; **Priorité : P0** ; **Dépendances :** aucune ; peut être menée si JANUS-001 est bloquée.
- **Prochaine action :** établir un manifeste des dépendances Python réellement utilisées, un script de vérification des blobs Git originaux et un script reproductible pour tests/pilote. Relever les versions et prérequis ; vérifier par exécution réelle, sans modifier les sources authentifiées.
- **Acceptation :** commandes déterministes documentées et une exécution de validation dans l'environnement disponible. Sinon conserver une procédure documentée et étiquetée NON EXÉCUTÉE.

### JANUS-004 — AUDIT INDÉPENDANT DES ENCLUSIONS ET DES CONCLUSIONS
- **Statut : READY** ; **Priorité : P1** ; **Dépendances :** aucune.
- **Prochaine action :** rechercher un contre-exemple au vérificateur de couverture, aux signes, aux bornes invalides et aux hypothèses de provenance ; distinguer un défaut du logiciel d'une invalidation du modèle physique.
- **Acceptation :** test contradictoire reproductible ou preuve de cohérence circonscrite, avec limites et résultat négatif conservés.

### JANUS-004A — JET RADIAL TROISIÈME ORDRE : CONDITION DE CERTIFICATION
- **Statut : DONE (question de dépendance aux jets variables déjà résolue le 02/11 ; contre-exemple générique conservé)** ; **Priorité : P0 historique** ; **Dépendances :** aucune pour la conclusion structurale déjà publiée ; reprise physique via JANUS-001.
- **Réconciliation contradictoire du 10/11 :** le rapport antérieur `research/STEP68AD_B3C3D7_STEP58_REDUCED_JET_ORDER_AUDIT.md` (blob `95a2c05632c302ba862a09c45d8da0a6710be1a0`, 13 tests PASS rapportés) avait déjà établi sur Step45/46/58 authentiques que `A_N=A_N(r,U,U_s)` et `A_M=A_M(r,U,U_s,U_ss)`. Les `qppp` présents dans les coefficients concernent des champs prescrits, pas les champs variables `pLf,pSf,pf`. Le contre-exemple générique `U=s^3` reste exact (SymPy rejoué : `48*r0**5`, `3/2` à `r0=1/2`), mais ne prouve donc PAS une lacune des coefficients finaux sur cette carte. Ne pas traiter le rapport récent comme découverte d'un défaut physique ni demander inutilement `U_sss` pour la voie directe. Limite : l'ancien audit utilise un shim Step57 transparent et ne remplace pas le rejeu intégral Step55/58.
- **NEXT_ACTION_EXACT :** JANUS-001, reconstruire les dépendances physiques authentiques, rejouer les neuf tests puis le pilote 1 cellule ; examiner les valeurs et leur provenance avant toute certification.
- **Preuve :** `research/STEP68AD_B3C3D9_THIRD_RADIAL_JET_MISSING_DERIVATIVE_AUDIT_20261110.md` ; contre-exemple SymPy exact PASS : pour `U(s)=s^3`, l'approximation quadratique du runner sous-estime `(sU)_{rrr}` de `48*r0**5`, soit `3/2` à `r0=1/2`.
- **Portée :** défaut générique de reconstruction du troisième jet ; **pas** de faux certificat physique établi ; vérifier la dépendance réelle des opérateurs `A_N,A_M` à `qppp` avant de conclure.
- **NEXT_ACTION_EXACT :** reconstruire `physical_operator()` authentique, évaluer `sp.diff(op['operator'][label][0], v)` pour chaque `v in op['qppp']` et `label in ('N','M')`, contrôler la simplification sur la coquille Step55/58 ; si non nul, certifier `U_{sss}` ou éliminer exactement la dépendance avant tout signe global.

### JANUS-005 — COMPLÉTUDE CENTRE, DEUX VRAIS BORDS ET CONTRAINTES
- **Statut : READY** ; **Priorité : P1** ; **Dépendances :** lire les preuves existantes avant de choisir la sous-proposition.
- **Prochaine action :** dresser la matrice des hypothèses et lacunes exactes pour centre, deux vrais bords, contraintes de Dirac, fixation des lapses et rang ; isoler une proposition falsifiable, la démontrer ou chercher un contre-exemple.
- **Acceptation :** résultat mathématique vérifiable (positif ou négatif), pas un simple récit de l'état des connaissances.

### JANUS-006 — DYNAMIQUE 4D, STABILITÉ ET OBSERVABLES
- **Statut : READY** ; **Priorité : P2** ; **Dépendances :** conditions mathématiques utiles issues de JANUS-005.
- **Prochaine action :** sélectionner une prédiction quantitative discriminante ou un obstacle de stabilité qui puisse être calculé ou réfuté avec les sources disponibles.
- **Acceptation :** calcul/proposition explicite et contradictoire avec hypothèses, pas de validation prématurée.

## Format de mise à jour d'un jalon

```text
[YYYY-MM-DDTHH:MM:SSZ] ID: JANUS-00X
HEAD de départ : ...
Statut AVANT → APRÈS : ...
Étape vraiment terminée : ...
Commandes/exécutions réelles : ...
Fichiers de preuve et blobs : ...
Résultat (dont résultats négatifs) : ...
Limites / blocage / alternative : ...
NEXT_ACTION_EXACT : ...
HEAD relu après publication : ...
```

**Règle finale :** si interrompu brutalement, le prochain lancement doit pouvoir comprendre **en quelques minutes de lecture** quelle est la prochaine commande utile, sans dépendre du contexte de conversation ou du répertoire éphémère du cycle précédent.
