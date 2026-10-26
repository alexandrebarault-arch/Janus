# JANUS — 68ad-C2d2b : véritable exécution Step58, dépendance d'intervalles et quotient Step60

Date : 2026-10-26. Branche d'écriture : `research/gate2b-nonhomothetic-transfer` exclusivement.

## 1. Provenance : blocage matériel résolu

22 fichiers (19 sources/tests Python et 3 rapports JSON) ont été lus directement par le connecteur GitHub, transférés par un document temporaire de transit, puis matérialisés dans un même environnement Python. Les **22 SHA Git blobs ont été recalculés sur les octets matérialisés et comparés aux SHA GitHub : 22/22 PASS**. Les trois rapports physiques 68v, 68ac, 68ad-B2 sont donc réellement présents et vérifiés, et non retranscrits à la main. Le document de transit doit être supprimé après vérification.

L'exécution utilise les véritables fichiers `hr_step58_temporal_operator.py` (`802c23aebd41780d8c462f1aa1711707fe4ee88f`), `hr_step60_full_constraint_prolongation.py` (`9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`), `hr_step68o_temporal_interval_annulus.py` (`c99caebc17f243784450ddff94fb061767e6d8e7`), ainsi que les rapports SHA-pinnés. Aucun de ces fichiers originaux n'a été modifié.

## 2. Exécution brute Step58 : erreur diagnostiquée

`python -m numerics.hr_step68ad_c2d2a_temporal_replay --repo . --out ...` est **réellement exécuté** et échoue sur la première cellule `[1/64,1/56]` avec `ZeroDivisionError: crossing zero (-322460524963163196404081, 931761500249409928975625)` dans le backend `I.inv()`. La valeur est exprimée sur la grille `10^28`.

La cause est la dépendance perdue dans l'évaluation d'un dénominateur commun à Step58 :

`T = beta1*Sg**2 + 2*beta2*Sg*Sf + beta3*Sf**2`.

Le CSE de l'opérateur original l'appelle `x79` pour `N` et `x75` pour `M`. L'arithmétique d'intervalles naturelle traite `Sg` et `Sf` comme indépendants sur une cellule entière ; la soustraction entre termes de signes opposés peut alors faire traverser zéro à l'enclosure **sans établir que le véritable dénominateur physique s'annule**. Ce constat est un défaut d'évaluation d'intervalles, pas une singularité physique démontrée.

## 3. Réécriture sur la coquille physique, preuve exacte et replay

Le profil canonique Step68o impose exactement `Sg=r*Lg`, `Sf=r*Lf`. Pour `r>0` et `Lg>0`, une substitution algébrique exacte donne :

`T = Sg**2 * (beta1 + 2*beta2*(Lf/Lg) + beta3*(Lf/Lg)**2)`.

Le nouveau code identifie les deux CSE de l'expression **originale**, développe leurs dépendances, vérifie symboliquement leur identité avec `T`, puis vérifie l'égalité de la factorisation sous `Sf=Sg*Lf/Lg`. Il ne remplace que l'évaluation de ces deux CSE dans une portée `patch` temporaire ; ni le Hamiltonien original, ni l'opérateur Step58, ni les jets canoniques Step68o ne sont changés. Cette technique est une **réécriture algébrique sur la coquille prescrite**, et non une certification d'une autre théorie.

Le replay complet du **véritable opérateur Step58** aboutit alors pour les sept cellules fermées couvrant `[1/64,1/32]`. **Résultat : 14/14 enclosures temporelles contiennent zéro ; 0/14 signes continus certifiés.** L'audit exact du garde C2d2b donne `all_nonzero_signs_certified=false`. Les intervalles sont très larges : première cellule `A_N ≈ [-10417.571,10422.414]`, `A_M ≈ [-8224.499,8207.700]` ; les fractions rationnelles exactes et les sept lignes sont conservées dans le rapport JSON.

En revanche, les **huit frontières radiales** évaluées chacune comme un point (`rlo=rhi`) possèdent des enclosures de signes stricts : `A_N>0` et `A_M<0` aux huit points. Par exemple :

- `r=1/64` : `A_N ≈ +0.85631619`, `A_M ≈ -1.65138589` ;
- `r=1/32` : `A_N ≈ +3.42513018`, `A_M ≈ -6.60524937`.

Ces **16 signes ponctuels** ne prouvent pas les signes sur les intervalles ouverts entre les points. Ce sont des résultats d'évaluation sur la solution spatiale conditionnellement certifiée par les rapports précédents, pas une démonstration de dynamique 4D.

Un diagnostic de raffinement sur la première cellule, subdivisée uniformément en 32, 64, 128 et 256 sous-cellules, laisse respectivement **64, 128, 256 et 512 coefficients INCOMPLETE**. Les majorants absolus observés décroissent (`A_N`: 31.48, 14.75, 7.45, 4.07 ; `A_M`: 25.49, 12.47, 6.79, 4.35), mais les signes continus restent non prouvés. La subdivision seule à cette échelle n'est pas une solution suffisante ; une meilleure conservation des corrélations entre jets canoniques ou une enclosure de Taylor/Lipschitz est à étudier.

## 4. Step60 réellement exécuté, mais pas encore sur les sept cellules

`python -m numerics.hr_step60_full_constraint_prolongation` a été exécuté avec les **sources originales SHA-authentifiées** : `EXIT=0`, `ELAPSED≈11.49s`. Le manifeste confirme l'annulation symbolique des coefficients de jets canoniques d'ordre trois après soustraction des dérivées complètes des contraintes (BN : 1 coefficient ; AM : 3 coefficients ; tous égaux à zéro).

**Attention :** c'est la réexécution du **quotient symbolique original Step60**, pas son évaluation numérique sur les sept cellules. Le manifeste lui-même indique `full_lower_jet_constraint_quotient=NOT COMPLETED` et `remaining_first_lapse_operator=NOT evaluated on exact Step55 spatial profile`. Il serait incorrect de déclarer Step60 spatialement certifié.

## 5. Non-régression réellement exécutée

`PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2b_executed_temporal_probe.py tests/test_hr_step68ad_c2d2b_guard.py tests/test_hr_step68ad_c2d2a_temporal_replay.py tests/test_hr_step58_temporal_operator.py tests/test_hr_step60_full_constraint_prolongation.py` : **79 PASS, 0 FAIL (21.60s pytest, 24.69s temps total)**.

Le groupe nouveau comporte **9 tests** : authenticité des sources et rapports, identités des deux CSE, reproduction du `ZeroDivisionError` de l'évaluateur brut, replay factorisé, sept cellules INCOMPLETE, huit frontières de signes ponctuels, manifeste Step60 original et restauration de la fonction compilée. Les 70 tests préexistants ont également passé.

## 6. Verdict scientifique et prochain chantier

**`GATE_2B OPEN` — `JANUS_R NOT_VALIDATED`.** Résultats : 7 cellules Step58 physiquement exécutées, mais **0/14 signes continus certifiés** ; 8 points avec deux signes stricts chacun ; Step60 original exécuté symboliquement, mais quotient inférieur sur cellules **non évalué**. Aucune conclusion sur rang de Dirac, lapses admissibles, conditions aux bords, dynamique 4D, stabilité ou observables.

**Prochaine étape effective 68ad-C2d2c :** construire un encadrement **corrélé** du véritable opérateur Step58 (Taylor models, sensibilité radiale ou dérivation symbolique factorisée), le valider par inclusion des enclosures ponctuelles et des sous-cellules, et obtenir des signes continus sur les sept cellules ou un contre-exemple. Ensuite seulement, évaluer le quotient inférieur Step60 sur les cellules, avec les contraintes et les jets exacts du shift. Ne pas confondre preuve conditionnelle de signes et preuve du rang global des contraintes.

### Fichiers de cette étape

- `numerics/hr_step68ad_c2d2b_executed_temporal_probe.py` : replay authentifié avec factorisation sur coquille, preuve des CSE, huit frontières, manifeste Step60.
- `tests/test_hr_step68ad_c2d2b_executed_temporal_probe.py` : 9 tests de non-régression.
- `research/reports/gate2b-step68ad-C2d2b-executed-physical-temporal.json` : 7×2 enclosures continues, 8×2 enclosures ponctuelles, manifeste Step60.
- `research/STEP68AD_C2D2B_AUTHENTIC_STEP58_EXECUTION_AND_INTERVAL_DEPENDENCY.md` : audit et limites.
