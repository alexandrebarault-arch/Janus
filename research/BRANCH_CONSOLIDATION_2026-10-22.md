# JANUS — Consolidation de branches (22 octobre 2026)

## Objectif demandé

**Une seule branche finale : `research/gate2b-nonhomothetic-transfer`.** Elle contient les travaux JANUS jusqu'à l'étape 49 et restera notre seule branche d'écriture. La consolidation ne vaut PAS validation physique de JANUS-R.

## Inventaire GitHub vérifié avant intervention

| Branche | Pointe Git vérifiée | Contexte |
| --- | --- | --- |
| `main` | `aead63f4098f0d15a849e579105af034b6317b30` | Branche par défaut au moment du contrôle ; ancien socle stable, déjà ancêtre de la branche active |
| `research/gate2b-nonhomothetic-transfer` | `9d6ca9e055ed52e3408b9b63fb2af1246d925977` | Recherche scientifique active jusqu'à Step49 |
| `research/v2-flrw` | `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` | Branche ancienne divergente avec **203 commits** supplémentaires absents de l'ascendance active avant consolidation |

GitHub compare `main...research/gate2b-nonhomothetic-transfer` : `ahead=830`, `behind=0`. GitHub compare `research/v2-flrw...research/gate2b-nonhomothetic-transfer` : `ahead=712`, `behind=203`.

Pull request existante : [#1 — V2: two-matter FLRW and linear segregation gates](https://github.com/alexandrebarault-arch/Janus/pull/1), **brouillon, non fusionnée**, base `main`, tête `research/v2-flrw`. Son texte contient des avertissements scientifiques historiques et ne doit pas être présenté comme résultat validé.

## Stratégie de préservation sans mélanger les fichiers

La **branche active** doit acquérir l'ancienne pointe `research/v2-flrw` comme **parent supplémentaire d'un commit à arbre inchangé** (fusion d'ascendance de type `ours`). Le commit conserve le contenu et les tests Step49 ; les 203 commits de la branche V2 restent accessibles par l'ascendance Git. L'ancienne `main` est déjà un ancêtre de l'actuelle branche de recherche, donc aucune copie supplémentaire n'est nécessaire. L'ancienne pointe exacte est notée ici.

**Ne PAS fusionner les fichiers V2 dans les sources numériques actuelles.** Une fusion de l'historique n'est PAS une validation des anciennes conclusions théoriques.

Après cette sauvegarde, il reste à effectuer **dans l'interface GitHub** les opérations d'administration que le connecteur de cette conversation ne sait pas exécuter :

1. Ouvrir les paramètres du dépôt `alexandrebarault-arch/Janus` et changer sa **branche par défaut** de `main` à `research/gate2b-nonhomothetic-transfer`.
2. Consulter la pull request V2 #1 et la fermer en tant que brouillon historique, **sans la fusionner dans `main`**.
3. Supprimer `research/v2-flrw` puis `main` dans la liste des branches du dépôt. Supprimer `main` seulement **après** avoir changé la branche par défaut.
4. Vérifier dans l'onglet Branches qu'il ne reste que `research/gate2b-nonhomothetic-transfer`.

**Statut de la suppression : non réalisée par ce connecteur.** L'application GitHub connectée dispose d'écriture sur les fichiers et les commits mais ne propose ni suppression d'une branche, ni modification de la branche par défaut. Ne jamais afficher « 1 branche » avant confirmation réelle de la liste distante.

## Reprise scientifique

Continuer à mettre à jour **`00_CURRENT_RESTART.md`** et le rapport de l'étape 50 sur **la branche active**. L'historique V2 est conservé uniquement comme mémoire de recherche. Les verrous Gate 2B (continuation globale certifiée, positivité continue du nouveau profil, conservation temporelle de la contrainte secondaire, fixation des lapses) restent ouverts.

**GATE_2B=OPEN ; JANUS-R NOT VALIDATED.**

## Résultat de la préservation de l'ascendance — VÉRIFIÉ LE 22 OCTOBRE

- Commit de préservation sans changement de fichiers : `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7`.
- Premier parent : `9c629156c8e05d7149421404490b2d77650b45e3` (pointe de JANUS actif après cet inventaire).
- Deuxième parent : `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` (ancienne pointe V2).
- **Git tree IDENTIQUE** avant/après ce commit : `e5da02813be6b378398520d9d129209fc5caf5c2`. Les fichiers actifs Step49 ont été préservés tels quels ; aucun fichier scientifique V2 n'a remplacé un fichier actif.
- Vérification GitHub après le nouveau parentage : `main...active` = `ahead 1035, behind 0` ; `research/v2-flrw...active` = `ahead 714, behind 0`. Ces deux anciennes pointes sont désormais ancêtres de la branche conservée.
- **Les 3 refs existent ENCORE sur GitHub** et la branche par défaut reste `main` tant que l'administration du dépôt ne change pas ces réglages. La suppression et la désignation de la branche par défaut ne sont pas réalisées par le connecteur.
- Ancienne PR brouillon `#1` toujours ouverte à la date du contrôle, base `main`, tête `research/v2-flrw`. Prévoir de la fermer SANS fusion de contenu avant suppression des deux refs.

### Mise à jour administrative effectivement exécutée

- **PR brouillon #1 FERMÉE LE 22 OCTOBRE 2026, SANS FUSION** via l'action GitHub connectée. État lu après action : `closed`, `merged=false`, ancien head `research/v2-flrw`, ancienne base `main`. Son historique de commits reste accessible depuis le commit de préservation `4f7a3a1`.
- **Toujours à faire par le propriétaire dans l'interface GitHub :** désigner `research/gate2b-nonhomothetic-transfer` comme branche par défaut, puis supprimer `research/v2-flrw` et `main`. Ne pas supprimer le défaut actuel `main` avant son changement. Le connecteur ne possède pas ces deux actions d'administration.
