# JANUS — b3c3d8 : audit indépendant des domaines de signes Step58 (03/11/2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Cet audit vérifie la cohérence arithmétique et la couverture géométrique de certificats *déjà publiés*. Il **n'apporte aucune nouvelle preuve de signe physique sur l'anneau cible** et ne réexécute ni l'EDO Step55 ni l'opérateur Step58.

## Sources authentifiées et contrôles indépendants

HEAD main lu au démarrage : `222217d3067305d469a88274cfbe875dffd8d5bb`. Rapports lus directement via GitHub au HEAD :
- `research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json` : blob `0c688d6648e16064b1eb4e8ad9c55e7b44a95947`.
- `research/reports/gate2b-b3c3d6-step58-physical-ANAM-four-radii-sign.json` : blob `c502b9779056e8a493c43d330696515a661128c4`.

Un vérificateur **indépendant** en arithmétique rationnelle exacte (BigInt) a parcouru les **7 cellules et 225 feuilles** du certificat C2d2e3, comparé chaque bord à son voisin, vérifié les signes stricts et recalculé les extrema annoncés : **aucune lacune, aucun chevauchement, aucune incohérence**. Couverture réellement justifiée par ce rapport : `r∈[1/64,1/32]`, et uniquement celle-ci. Marges exactes du rapport confirmées :
- `min A_N.lower = 738081248225184126420269/312500000000000000000000000 > 0`.
- `max A_M.upper = -1514435823797833476506571291/1250000000000000000000000000 < 0`.

Le second rapport a quatre boîtes ponctuelles à `r=1/4,1/2,7/10,17/20`, avec `A_N>0, A_M<0, A_N+A_M<0` à **ces seuls points**. Aucune continuité des signes entre ces points ne découle des quatre boîtes.

## Carte exacte des domaines restant à prouver

Sur `r∈[0,17/20]`, les intervalles ouverts **non couverts** par ces certificats de signes sont :
1. `(0,1/64)` (centre non inclus dans la preuve de signe).
2. `(1/32,1/4)`.
3. `(1/4,1/2)`.
4. `(1/2,7/10)`.
5. `(7/10,17/20)`.

Les extrémités ponctuelles certifiées ne remplissent aucun intervalle ouvert. **L'anneau prioritaire entier `r∈[1/4,17/20]` (équivalent `s∈[1/16,289/400]`) reste dépourvu de certificat de signe continu.** Ce constat n'est ni un zéro démontré ni un contre-exemple physique.

## Code, tests et limites

Vérificateur autonome publié : `numerics/hr_b3c3d8_sign_coverage_integrity.py`. Tests : `tests/test_hr_b3c3d8_sign_coverage_integrity.py`. Exécution locale sur les **octets publiés** : `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d8_sign_coverage_integrity.py' -v` : **14 PASS, 0 FAIL, 0 SKIP** ; `python -m compileall -q numerics tests` : **PASS** sur le mini-arbre du vérificateur. Les deux SHA blobs du code et des tests ont été relus sur GitHub et comparés aux octets locaux. Les 14 tests utilisent des fixtures **synthétiques**, pas les deux rapports physiques complets. Ces derniers ont été vérifiés séparément par le parcours rationnel indépendant en JS ; le CLI Python du vérificateur sur le dépôt complet n'a pas été exécuté dans cette session.

**Prochaine action utile, non accomplie ici :** exécuter l'évaluateur physique Step55/Step58 authentifié avec intervalles rationnels sur chaque cellule de `[1/4,17/20]`, en recomposant `G,G_s,G_U,U_s,U_{ss}`, puis vérifier le signe direct `A_N>0,A_M<0`. En cas d'échec d'enclosure, subdiviser et distinguer inconclusif d'un vrai contre-exemple. Ensuite combler `[1/32,1/4]` et `[0,1/64]`, examiner les zéros et les deux vrais bords, puis Dirac, 4D, stabilité et observables.

**Aucune validation générale JANUS.**
