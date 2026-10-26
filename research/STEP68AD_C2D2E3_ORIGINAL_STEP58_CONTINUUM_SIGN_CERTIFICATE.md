# JANUS — 68ad-C2d2e3 : certification conditionnelle des deux coefficients temporels originaux Step58

Date : 2026-10-26. Branche autorisée : `research/gate2b-nonhomothetic-transfer`.

## Résultat principal

**Sur la branche radiale originale Step55/68o, sous les hypothèses de régularité et les trois certificats spatiaux SHA-pinnés Step68v/68ac/68ad-B2, les coefficients d'ordre zéro du véritable opérateur Step58 satisfont sur tout le continuum**

\[
 A_N(r)>0,\qquad A_M(r)<0,\qquad 1/64\le r\le1/32.
\]

Le résultat n'est pas une preuve du rang de Dirac, de l'existence de lapses globaux compatibles avec les bords, de la dynamique 4D, de la stabilité ni des observables. Les coefficients de dérivées de lapses sont annulés uniquement dans le cadre conditionnel des identités historiques Step58/68h/68j et de la coquille contrainte Step68o ; les résultats ne se transfèrent pas aux chartes singulières ou à des données initiales arbitraires.

## Provenance et opérateur

Les fichiers sources et les trois rapports physiques ont été transférés depuis le connecteur GitHub et **22/22 SHA blobs Git** recalculés sur les octets de l'environnement Python. Les sources originales Step45/46/55/57/58/59/60/68n/68o restent inchangées. Les six fichiers PINNED de l'adaptateur Step58, les huit sources de `verified_sources` Step68f et les quatre sources de Step68l sont revérifiés à l'exécution. Le dénominateur CSE original `T=beta1*Sg²+2 beta2*Sg Sf+beta3*Sf²` est remplacé, après identité symbolique exacte sur `Sg=r Lg,Sf=r Lf`, par `Sg²*(beta1+2 beta2 Lf/Lg+beta3*(Lf/Lg)²)` ; cette réécriture n'est valable que sur la coquille régulière `Lg>0,r>0`.

Le véritable opérateur `physical_operator()['operator'][label][0]` contient les troisièmes jets radiaux `q'''`. Une certification par le théorème des accroissements finis exige donc `q''''` ; utiliser seulement les jets Step68o d'ordre 3 pour différencier l'opérateur aurait été incorrect.

## Extension de quatrième ordre, exacte sous l'EDO originale

L'EDO physique originale est `2s U_s=G(s,U)-2U`, avec `s=r²`. Pour les intervalles certifiés `U, U_s, U_ss, U_sss`, le coefficient d'ordre 4 est reconstruit par une série de Taylor d'ordre 4 :

`[t³] (G(s+t,U(s+t))-2U(s+t))/(2(s+t)) = U_ssss/6` ; ainsi `U_ssss/24 = ([t³] RHS)/4`.

Cette formule utilise uniquement les coefficients d'ordre 0 à 3, déjà encadrés, et la fonction originale `G`, pas une différence finie ni une supposition sur le signe de `U_ssss`. Par chaîne :

`[r⁴] U(r²) = U_ss/2 + 2 r² U_sss + (2/3) r⁴ U_ssss`.

Les 12 jets canoniques Step68o sont prolongés à l'ordre 4 par les mêmes expressions algébriques originales ; les champs de poussière sont traités comme des jets locaux de fonctions globales, non comme des fonctions constantes nulles. Les 48 coefficients d'ordres 0 à 3 sont comparés **exactement** à la reconstruction originale Step68o sur trois rayons, soit 144 égalités d'intervalles, sans changement. Les valeurs ponctuelles de l'opérateur Step58 original ont aussi été comparées aux valeurs de l'AD d'intervalles sur deux rayons (intersections non vides, différences de centres négligeables au regard des enclosures ; les deux CSE produisent des arrondis légèrement différents).

## Certification continue par accroissements finis

Pour chaque sous-cellule rationnelle fermée `[a,b]`, `m=(a+b)/2`, l'AD d'intervalles évalue une enclosure du dérivé radial de chaque coefficient original sur **tout** `[a,b]`. Le théorème des accroissements finis donne exactement :

`A_X([a,b]) ⊆ A_X(m) + [-h,h] * A_X'([a,b])`, `h=(b-a)/2`, `X∈{N,M}`.

Le calcul part de 7 cellules originales, chacune divisée en 32. Une seule sous-cellule de la première cellule donnait initialement une borne inférieure de `A_N` négative (enclosure **INCOMPLETE**, pas contre-exemple). Sa bisection rationnelle en deux a produit deux bornes strictement positives. **Total : 225 sous-cellules fermées jointives, sans lacune, 225/225 avec `A_N.lower>0` et `A_M.upper<0`.**

Marges rationnelles globales certifiées (enclosures en arithmétique entière extérieure sur grille `10^28`) :

- `min(A_N.lower) = 738081248225184126420269/312500000000000000000000000 ≈ 0.00236185999432 > 0`.
- `max(A_M.upper) = -1514435823797833476506571291/1250000000000000000000000000 ≈ -1.21154865904 < 0`.

Le certificat JSON donne les 225 intervalles rationnels explicites et leurs bornes `N,M`. Il n'est pas suffisant de vérifier les bornes rapportées sans rejouer le code et authentifier les trois rapports physiques.

## Vérifications réellement exécutées

`PYTHONPATH=. python -m numerics.hr_step68ad_c2d2e3_step58_mvt --repo . --out research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json` : **7/7 cellules, 225 feuilles, 1 bisection**, terminaison normale.

`PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2e3_step58_mvt.py` : **18 PASS, 0 FAIL**. Les tests couvrent les 144 comparaisons de jets originaux, les deux évaluations Step58 originales, la présence des troisièmes jets, l'identité CSE, les identités de dérivation et de récurrence d'ordre 4, la fermeture des intervalles, le contrôle négatif de la sous-cellule trop large, le raffinement positif, la conservation des scopes et le rejet des sources/rapports altérés. Les campagnes historiques complètes ne sont pas comptées comme réexécutées.

## Limites physiques et prochaine étape

Les signes positifs/négatifs concernent les **coefficients de l'équation temporelle**, pas directement les signes des lapses. Sous l'hypothèse supplémentaire que les termes de dérivées de lapses s'annulent effectivement sur la coquille contrainte lisse, l'équation algébrique `A_N N + A_M M=0` impose un **rapport local** `N/M=-A_M/A_N>0`. Cette relation nécessaire ne prouve pas que deux lapses admissibles satisfont simultanément les contraintes complètes, les équations d'évolution et les conditions aux bords.

**Prochaine étape proposée : 68ad-C2d2e4**, audit contradictoire du rang Dirac complet et de l'existence globale de lapses avec bords sur le profil authentifié ; analyser les chartes `K=0`, `J=0`, puis 4D, stabilité, observables. Ne pas proclamer de fermeture cosmologique.

**Verdict inchangé : `GATE_2B OPEN` ; `JANUS_R NOT_VALIDATED`.**
