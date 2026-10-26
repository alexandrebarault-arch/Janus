# JANUS — 68ad-C2d2b : contre-exemple au certificat de signes déclaratifs (2026-10-26)

**Nature : résultat négatif de sûreté de preuve, PAS exécution du vrai Step58/Step60.**
**État scientifique : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Contre-exemple reproductible

Le `summarize_temporal_signs(rows)` publié précédemment ne consultait que le champ déclaratif `temporal.N.sign` / `temporal.M.sign`, sans vérifier `enclosure`. Pour sept lignes contenant chacune `N.sign=POSITIVE_CERTIFIED`, `M.sign=NEGATIVE_CERTIFIED` mais **les deux intervalles `[-1,1]`**, l'ancien algorithme renvoie pourtant `all_nonzero_signs_certified=True` et `all_expected_N_positive_M_negative=True`. Les quatorze intervalles contiennent zéro : la conclusion est logiquement fausse. Le contre-exemple a été exécuté en Python sur une reconstruction fidèle du contrôle de flux de l'ancienne fonction, après lecture directe de son source GitHub `a0657a023fc59073bd1ab9f9a4255cf5248e0b9b`.

Ce résultat **ne démontre pas** que les calculs Step58 originaux sont faux : la fonction d'évaluation construit normalement son signe à partir des bornes. Il démontre qu'un rapport corrompu, un changement d'appelant ou une sortie fabriquée pouvait franchir le dernier vérificateur sans preuve.

## Correction testée

Le module `numerics/hr_step68ad_c2d2b_guard.py` recalcule désormais les quatorze signes **directement depuis les fractions rationnelles exactes** des intervalles `enclosure`, et rejette tout désaccord avec les étiquettes déclarées, tout intervalle manquant, inversé ou non rationnel. Il vérifie également les sept cellules ordonnées, contiguës et non dégénérées couvrant exactement `[1/64,1/32]`. Les contrôles d'injection `U,U_s,U_ss,U_sss` existants restent inchangés.

Le libellé `N/M` désigne ici les **coefficients `A_N/A_M` d'ordre zéro** de l'opérateur temporel, **pas les signes des lapses N/M eux-mêmes**. Le résultat comporte donc la clé non ambiguë `all_expected_A_N_positive_A_M_negative`, tout en préservant l'alias historique pour compatibilité. Même si les quatorze coefficients étaient certifiés, cela ne prouverait ni l'existence de lapses positifs, ni la préservation complète des contraintes, ni le rang de Dirac.

## Exécution locale réellement effectuée

```text
cd /mnt/data/janus_c2d2b_integrity
PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2b_guard.py
....................... [100%]
23 passed in 0.07s
```

- 23 tests du garde/certificat : **23 PASS, 0 FAIL** (dont 11 cas supplémentaires par rapport aux 12 précédents).
- Contrôle négatif supplémentaire exécuté : l'ancienne logique, reproduite fidèlement, accepte faussement 14 intervalles traversant zéro.
- Code testé localement puis publié byte-identique : `numerics/hr_step68ad_c2d2b_guard.py`, blob `7ea03654054632d1ca8ecbe9dbf8df0d66cf582c`.
- Tests testés localement puis publiés byte-identiques : `tests/test_hr_step68ad_c2d2b_guard.py`, blob `cf8532bfc15ef2ebc0c2ec71a46985d8f6f866f1`.
- **Vrai Step58 sur les sept cellules : NON EXÉCUTÉ ; vrai Step60 : NON EXÉCUTÉ ; 0/14 nouveaux signes physiques.** Tests d'intégration de l'adaptateur modifié : NON exécutés.

## Prochaine étape effective : 68ad-C2d2b (toujours ouverte)

Réunir les sources Python et rapports originaux dans un même environnement d'exécution authentifié ; rejouer l'intégration complète ; exécuter le véritable Step58 sur les sept cellules, puis les quotients de contraintes Step60. Toute borne traversant zéro reste `INCOMPLETE`. Vérifier séparément les coefficients `N,N',M,M'`, les lapses admissibles, les conditions aux bords et le rang de Dirac.

**Verrou opérationnel :** le conteneur Python de cette session n'a aucun checkout JANUS et ne peut résoudre `github.com` ; le connecteur GitHub permet lecture/écriture mais pas l'import des fichiers directement dans le conteneur. Ne pas prétendre que ce correctif constitue une preuve physique.
