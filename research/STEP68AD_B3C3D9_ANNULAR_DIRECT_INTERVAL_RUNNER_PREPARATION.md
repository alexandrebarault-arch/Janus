# JANUS — b3c3d9 : évaluateur d'intervalles physiques Step55/58 préparé, NON exécuté sur le dépôt complet (03/11/2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Aucun nouveau signe continu physique n'est certifié dans cette session.

## Travail réellement effectué

Le nouveau module `numerics/hr_b3c3d9_annular_direct_enclosure.py` prépare un calcul **direct, sans interpolation ponctuelle** des coefficients originaux `A_N,A_M` sur une partition rationnelle jointive de `r=[1/4,17/20]`, soit `s=[1/16,289/400]`. Il vérifie d'abord les SHA des sources originales Step45/46/55/58 et rejoue la barrière Step55 de 256 cellules **lorsqu'il est exécuté dans le dépôt complet**. Il évalue ensuite `G,G_s,G_U` avec la géométrie composée, construit `U_s=(G-2U)/(2s)` et `U_ss=(G_s+(G_U-4)U_s)/(2s)`, puis soumet les jets radiaux à l'opérateur Step58 original via `physical_jet`. Les intervalles utilisent les deux moteurs existants à arithmétique entière dirigée (`10^-28` pour Step55, `10^-34` pour Step58), avec conversion englobante exacte entre leurs échelles.

Chaque cellule rapporte ses bornes rationnelles et son statut. `CERTIFIED` exige strictement `A_N.lower>0` et `A_M.upper<0`. Une division par intervalle contenant zéro, une racine impossible ou une enclosure trop large reste `INCONCLUSIVE` ; elle **n'est jamais présentée comme un zéro physique**. La conclusion globale exige aussi que toutes les cellules aient été réellement traitées et couvrent exactement le domaine, sans trou ni chevauchement. `--max-cells` autorise un pilote borné sans possibilité de certification globale artificielle.

**Précaution technique :** la fonction Step58 `physical_jet` déjà publiée est utilisée sans modification. Quand son centre radial est un intervalle, son `h=r²-r_0²` inclut bien la valeur exacte zéro, mais perd une corrélation ; les bornes peuvent donc être trop larges. Ce phénomène est un **risque d'inconclusivité**, pas une preuve de changement de signe. Une passe ultérieure pourra réduire cette dépendance par jets localement centrés et subdivisions adaptatives.

## Exécution vérifiable et limites

Exécuté localement sur les **octets publiés** : `PYTHONPATH=<mini-arbre> python -m unittest discover -s <mini-arbre>/tests -p test_hr_b3c3d9_annular_direct_enclosure.py -v` : **7 PASS, 0 FAIL, 0 SKIP**. Les tests couvrent les identités rationnelles de jets sur une solution analytique synthétique, la partition jointive exacte et le refus des faux PASS (trous, chevauchements, signes non stricts, cellules manquantes). `python -m compileall -q <mini-arbre>` et `python -m numerics.hr_b3c3d9_annular_direct_enclosure --help` : PASS. Ces tests **ne rejouent pas la physique**.

Les fichiers du dépôt original ne sont pas montés dans le conteneur de calcul de cette session, et l'accès réseau Git direct a échoué par résolution DNS (`Could not resolve host: github.com`). Le connecteur GitHub permet la lecture et la publication mais **pas l'exécution Python des moteurs physiques dans ce conteneur**. Il serait trompeur d'annoncer une barrière Step55 ou des cellules Step58 exécutées. **Cellules physiques nouvelles réellement évaluées : 0/256.** Aucune sortie JSON physique b3c3d9 n'est publiée.

Fichiers code et tests publiés sur `main`, puis relus :
- `numerics/hr_b3c3d9_annular_direct_enclosure.py` — Git blob `d2de0887170fc7048c312fe620d4ab2a0ee0c8cc`.
- `tests/test_hr_b3c3d9_annular_direct_enclosure.py` — Git blob `21506f95f2122a07aa82a63fc6b5194e41b040a2`.

Ces deux blobs correspondent exactement aux octets des 7 tests exécutés et compilés.

## Reprise prioritaire

Dans un checkout complet propre de `main`, lancer d'abord :

`PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1`

Puis, si la première cellule fonctionne, lancer le calcul complet :

`PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --out research/reports/gate2b-b3c3d9-annular-direct-attempt.json`

Auditer les premières erreurs réelles, raffiner les cellules inconclusives sans masquer les dépendances et ne publier un certificat physique que si toutes les cellules passent. Ensuite raccorder `r=[0,1/4]`, les zéros possibles, les deux vrais bords temporels, Dirac/charges, dynamique 4D, stabilité et observables. Aucun résultat sur la branche physique ne peut être inféré des tests synthétiques de cette session.
