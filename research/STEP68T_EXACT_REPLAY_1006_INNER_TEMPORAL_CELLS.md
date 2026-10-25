# JANUS — Étape 68t : relecture exhaustive des 1 006 cellules de la bande r=1/32..1/16

**25 octobre 2026 ; `research/gate2b-nonhomothetic-transfer` seulement ; GATE_2B OPEN, JANUS-R NOT_VALIDATED.**

Le calcul historique physique Step58 des deux coefficients d'ordre zéro `A_N=[dot C]_N`, `A_M=[dot C]_M` sur la branche non homothétique Step55 a été **réexécuté pour CHACUNE des 1006 cellules** du nouveau certificat Step68s, avec la même arithmétique entière extérieure original Step55 et les mêmes huit sources authentiques. Ce replay vérifie l'égalité de chaque paire de fractions inférieure/supérieure des intervalles `A_N,A_M` avec la preuve archivée ; il ne se contente pas de vérifier les signes.

**Résultat : 1006 / 1006 replays EXACTEMENT IDENTIQUES, aucun échec.**

La source `numerics/hr_step68t_replay_near_center.py` étend le relecteur Step68r en ajoutant le fichier certifié `research/reports/gate2b-step68s-inner-1over32-to-1over16-cover.json` :
- SHA256 strict attendu `7491e166286279f8ac6423677fec069f7fc9d6bca7bfda4271cedd1c0addedd4`;
- bornes `[1/32,1/16]` contrôlées EXACTEMENT ;
- 1006 cellules fermées jointives dont le statut est CERTIFIED, aucune pending/failed ;
- fournisseurs historiques et moteurs jets/original Step58 pin par git SHA.

Le module `numerics/hr_step68r_cell_replay.py` effectue un nouveau calcul borné pour chaque cellule et enregistre atomiquement la cellule vérifiée et son index : tout redémarrage avec un SHA modifié est rejeté. Il s'agit du **MÊME** moteur physique d'évaluation de l'opérateur Step58, utilisé à nouveau, pas de l'oracle théorique indépendant non-IBP qui manque encore.

Six jobs de replay avec un **timeout individuel explicite de 24 secondes**, chacun terminé normalement :
- après jobs 1..5 : 200, 400, 600, 800, 1000 cellules cumulées ;
- job 6 : 1006/1006, statut `PASSED`.

**3 tests ciblés ont réussi en 4.19 secondes** sous timeout de 16 secondes (authenticité, reprise 3 puis 2 cellules, fichier falsifié rejeté).

Artefacts GitHub SHA byte-identiques aux fichiers exécutés :
- `numerics/hr_step68t_replay_near_center.py` — `4cf195f22ec2218de7453797bccaf5f151a4d2cd`.
- `tests/test_hr_step68t_replay_near_center.py` — `2f9929f1433d00d2026478d48606a46a790dd2b7`.
- `research/reports/gate2b-step68t-replay-1006-cells-report.json` — `b5c5a52a0b3960ae630ef2d3521e0d4d9689f4d3`.
- `research/reports/gate2b-step68t-replay-state.json` — `1ac99ccbbd5413f67ffa140d28bf091c8c6eb5f2`.
- `research/reports/gate2b-step68t-pytest-state.json`, `...-pytest.log`.

**Bilan actuel :** 265 cellules (Step68p) + 314 cellules (Step68q) + 1006 cellules (Step68s) = **1 585 cellules fermées formant un recouvrement continu de `r∈[1/32,17/20]`**, toutes signées strictement et toutes relues une fois (avec le même moteur) : `A_N>0, A_M<0`.

**Reste :** `0≤r<1/32`, centre `r=0`, régularité du rapport de lapses, jauge/bords/contrainte temporelle globale, oracle Poisson indépendant non intégré par parties et rang de Dirac. Ces résultats ne valident pas JANUS-R.

Prochaine piste Step68u : approcher davantage `r=0` par bandes avec timeouts, mais surveiller le coût quadratiquement croissant de la subdivision ; si la méthode brute ne converge pas efficacement, privilégier normalisation centrale (A_N/r^2,A_M/r^2) et séries U0..U3 du certificat original Step67b.
