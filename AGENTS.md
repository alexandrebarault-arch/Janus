# JANUS — Instructions permanentes pour agents de recherche

## Finalité
Conduire une recherche scientifique critique, reproductible et falsifiable sur la formulation cosmologique JANUS étudiée. Ne présupposer ni sa validité ni sa réfutation. Le but est un verdict étayé : (A) viabilité dans un domaine explicitement démontré et confrontation observationnelle, (B) réfutation de la formulation sous des hypothèses précises, ou (C) résultat partiel avec obstacles vérifiables. Une contradiction démontrée est un résultat positif de recherche. **GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED** tant que les preuves requises manquent.

## Reprise persistante — obligatoire à chaque session
1. Lire le HEAD réel de `main` sur GitHub ; figer ce SHA pour les lectures du cycle.
2. Lire à ce SHA, dans cet ordre, `research/AUTONOMOUS_WORK_QUEUE.md`, `research/AUTOMATION_STATE.json`, puis le début de `00_CURRENT_RESTART.md`.
3. Reprendre la tâche RUNNING au dernier jalon *prouvé*, sinon la priorité READY non bloquée ; respecter `NEXT_ACTION_EXACT`. Confronter les marqueurs aux artefacts et aux commits.
4. Si le HEAD change avant écriture, relire et réconcilier les modifications concurrentes.
5. La file est la source de vérité opérationnelle ; ce fichier contient la doctrine permanente et ne remplace ni les preuves ni les états.

## Boucle de travail et priorité scientifique
Travailler en boucle pendant toute la durée disponible : hypothèse falsifiable → critères d'échec → calcul/test/démonstration authentique → contrôle contradictoire indépendant → preuve persistée → nouvelle tâche. Ne pas terminer après un seul test ou rapport. Maximiser les **résultats scientifiques vérifiables**, pas le nombre de commits ou les contrôles informatiques répétés.

Pour JANUS-001, reconstruire les sources et dépendances originales Step45/46/55/58 (y compris fichiers historiques), comparer les SHA des blobs Git aux octets exécutés, rejouer les tests du dépôt et le pilote à une cellule avant les 256 cellules. Ne pas utiliser de shim ou de données synthétiques comme preuve physique. Si le Git CLI échoue par DNS, utiliser le connecteur GitHub pour transférer les octets authentifiés ; après deux tentatives équivalentes sans changement de cause, consigner l'erreur précise, marquer BLOCKED et poursuivre une autre piste scientifique indépendante. Ne pas refaire gratuitement des tests déjà prouvés au même SHA.

Maintenir les pistes parallèles : certification numérique, contraintes de Dirac et identités de Bianchi, fixation des deux lapses, régularité du centre, conditions aux deux vrais bords, rang et degrés de liberté, dynamique 4D, stabilité et observables (CMB, expansion, structures, lentilles). Prioriser les obstacles fondamentaux et les contre-exemples potentiellement décisifs ; éviter les calculs coûteux fondés sur des hypothèses non vérifiées.

## Rigueur des preuves
Pour toute affirmation, conserver hypothèses, domaine, commandes exactes, versions, provenance des sources, résultat et limites. Séparer tests unitaires/synthétiques, calculs ponctuels, résultats conditionnels, certificats d'intervalle et conclusions globales. Séparer cellules demandées, tentées, effectivement évaluées, certifiées et inconclusives ; `executed_cells` peut inclure INCONCLUSIVE. Une couverture trouée, une borne contenant zéro ou des points isolés ne prouvent pas un signe strict continu. Rechercher activement des contre-exemples et accepter les NO-GO prouvés dans leur domaine.

## Publication sûre
Travailler exclusivement sur `main`. Avant un calcul long/risqué, enregistrer un marqueur RUNNING s'il n'existe pas. Après un jalon réellement vérifié, enregistrer preuve, commande, empreintes, limites et `NEXT_ACTION_EXACT` dans la file ; actualiser `research/AUTOMATION_STATE.json` pour les vrais jalons scientifiques et le début de `00_CURRENT_RESTART.md` seulement pour un progrès substantiel, en préservant son historique. Publier des commits utiles et vérifier ensuite HEAD et blobs. Ne jamais inventer exécution, preuve ou commit ; aucun commit artificiel. Ne pas créer/supprimer de branches, forcer un push, modifier les tags d'archive, réactiver GitHub Actions ni modifier la programmation du job.

## Compte rendu
À chaque session, rapporter en français HEAD initial/final réellement vérifiés, tâches, commandes réellement exécutées (PASS/FAIL/SKIP), résultats nouveaux et contre-vérifications, cellules physiques évaluées/certifiées/inconclusives, artefacts et commits vérifiés, blocages et `NEXT_ACTION_EXACT`. Si aucun progrès nouveau, rester bref et l'indiquer. Ne jamais annoncer une validation globale sans démonstration complète et expertise contradictoire.
