# JANUS — Étape 68r : relecture exacte de TOUTES les 579 cellules temporelles certifiées

**25 octobre 2026 ; écriture sur `research/gate2b-nonhomothetic-transfer` uniquement ; GATE_2B OPEN, JANUS-R NOT_VALIDATED.**

## Objectif et limite d'indépendance

Afin de réduire les risques de corruption/reprise incorrecte, le nouveau programme `numerics/hr_step68r_cell_replay.py` **réexécute les 579 évaluations arithmétiques d'intervalles**, à partir des vrais modules physiques Step45/46/55/57/58/59/60, plutôt que de simplement croire les signes enregistrés dans les fichiers JSON.

**Ce replay utilise le MÊME évaluateur `evaluate_cell` et les MÊMES expressions Step58 authentifiées**. Il vérifie donc la reproductibilité des calculs/encadrements, et **n'est PAS un deuxième oracle de Poisson non intégré par parties indépendant**. Cette distinction est fondamentale pour la suite.

## Contrôles exhaustifs et résultats

Pour chaque certificat, le programme :
- refuse l'archive si son SHA256 attendu ne correspond pas aux octets ;
- revérifie les huit Git blob SHA physiques originaux et le SHA de la source d'arithmétique des jets ;
- vérifie une nouvelle fois, en fractions exactes, la couverture du domaine fermé sans trou, le nombre de feuilles, l'absence de cellules non résolues et les deux signes stricts ;
- calcule de nouveau `A_N,A_M` à CHAQUE cellule `[rlo,rhi]` par `evaluate_cell` et demande l'égalité exacte **des quatre fractions** aux intervalles enregistrés ;
- écrit atomiquement l'état et le dernier index vérifié après chaque cellule, avec rejet des modifications de source ou de certificat à la reprise.

**Résultats observés sans erreur :**
- **Annulus extérieur Step68p : 265 / 265 cellules** rejouées exactement, statut `PASSED`.
- **Bande intérieure Step68q : 314 / 314 cellules** rejouées exactement, statut `PASSED`.
- **TOTAL : 579 cellules** dont les encadrements rationnels calculés sont **octet pour octet identiques aux limites enregistrées**.

Les quatre jobs ont été lancés avec `scripts/janus_bounded_job.py --timeout-seconds 25 --grace-seconds 2`, chacun terminé `PASSED` avant son timeout. États et comptes rendus sur GitHub :
- `research/reports/gate2b-step68r-replay-summary.json`
- `research/reports/gate2b-step68r-inner-replay-state.json`
- `research/reports/gate2b-step68r-outer-replay-state.json`

Le script et les tests `tests/test_hr_step68r_cell_replay.py` sont publiés avec leurs Git SHA octet-identiques à l'exécution :
- source `60214f32d16ea2aa1f04ff63ce76338e28457034` ;
- tests `b0ddcd8d8504d8bb090148764a06824f86d1c978`.

**6 tests réussis** en 4,40s sur la suite ciblée : deux preuves/provenances, deux replays de sous-listes sous reprise atomique, faux certificat SHA rejeté et reprise avec SHA moteur falsifié rejetée. Un premier essai a échoué (3 échecs / 3 réussites) parce que le nouveau JSON intérieur n'était pas encore copié localement sous son nom final ; la correction du chemin et les 6 réussites ultérieures sont toutes enregistrées dans `research/reports/gate2b-step68r-pytest.log`. Aucune réussite n'est attribuée à la première exécution incomplète.

## Conclusion et problème restant

Cette relecture renforce le caractère **reproductible** de la preuve de `A_N>0, A_M<0` pour toute la bande non homothétique `r∈[1/16,17/20]`, sous les hypothèses de la véritable ODE Step55 et du certificat Step68l. **Elle ne modifie pas le domaine ni ne prouve la théorie 4D.**

Prochaine étape Step68s : rapprocher le certificat du centre `r∈[1/32,1/16]`, toujours par lots sous timeout et avec états persistants ; si le schéma de Taylor ODE en `1/s` perd sa capacité de signer les intervalles, construire un développement normalisé central différent à partir des coefficients U0..U3 rigoureusement encadrés à Step67b.

**TOUJOURS OUVERT :** `r=0`, conditions aux limites et jauge temporelle, rang Dirac global, oracle 6 paires non-IBP, chartes `K=0,J=0`, absence du fantôme BD et validation JANUS-R.
