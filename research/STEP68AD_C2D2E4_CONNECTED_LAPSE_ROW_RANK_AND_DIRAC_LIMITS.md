# JANUS — 68ad-C2d2e4 : audit contradictoire du rang local des lapses sur quatre certificats Step58

Date : 2026-10-26. Branche : `research/gate2b-nonhomothetic-transfer`.

## Résultat conditionnel vérifié

Quatre rapports physiques originaux, authentifiés par les SHA Git ci-dessous, ont été relus intégralement et leurs **1 810 sous-cellules rationnelles** recalculées avec des entiers BigInt exacts : 225 cellules intérieures Step68ad-C2d2e3, 1 006 Step68s, 314 Step68q, 265 Step68p. La couverture est exactement **[1/64,17/20]**, sans lacune ni recouvrement intérieur ; tous les intervalles ont **A_N.lower>0, A_M.upper<0**. Les deux extremums rationnels du rapport **M/N = −A_N/A_M** restent situés dans la bande extérieure Step68p : l'extension vers le centre **ne resserre pas** les bornes uniformes historiques Step68w.

Sur tout l'anneau fermé, **sous les hypothèses de validité des quatre certificats physiques et de la coquille lisse Step55/68o**, la seule équation réduite `A_N N+A_M M=0` a une ligne algébrique de rang ponctuel 1 et un noyau de lapses localement positifs. Les inégalités vérifiées sont :

\[
 1/50000 < M/N < 14,\qquad A_N/r^2>7/20,\qquad A_M/r^2<-546.
\]

Ce sont des **bornes conservatrices des enclosures**, pas les valeurs physiques extrêmes. Les fractions exactes et les cellules extrémales figurent dans le rapport JSON. La construction locale `M(r)=−A_N(r)N(r)/A_M(r)` suppose des coefficients réguliers et `N(r)>0` ; elle ne fixe pas les conditions aux bords. Pour des données prescrites `N(a),M(a)`, la condition nécessaire est `M(a)/N(a)=−A_N(a)/A_M(a)` (et de même à l'autre bord) : **aucune donnée de bord physique n'a été authentifiée ou résolue ici**.

## Contre-exemple structurel à une extrapolation de rang

Une ligne non nulle de l'opérateur temporel ne fixe **pas** le rang de la matrice complète de Dirac. Même parmi les matrices antisymétriques, une première ligne `(0,a,b,0,0,0)`, avec `a²+b²>0`, admet la complétion où seules cette ligne et sa colonne sont non nulles (rang 2) et celle où l'on ajoute le bloc indépendant `D[3,4]=1, D[4,3]=-1` (rang 4). **Ces matrices sont des contre-exemples algébriques illustratifs, PAS des matrices de Poisson physiques de JANUS.** Elles réfutent seulement l'inférence illégitime « rang local 1 de la ligne temporelle ⇒ rang complet de Dirac connu ».

## Exécution et provenance

- 4/4 blobs GitHub attendus vérifiés à la lecture ; sources détaillées dans le JSON.
- **11 tests synthétiques exécutés** (un cas valide, dix rejets de données invalides) ; **1 audit réel complet** avec 1 810 cellules contrôlées ; 0 échec.
- Code exécuté dans le moteur JavaScript V8 du connecteur avec fractions exactes `BigInt`. Le CLI Node publié recalcule les SHA Git des octets locaux et permet un replay dans un clone complet. **Le CLI Node et les modules physiques originaux n'ont pas été réexécutés dans un clone complet pendant cette session.**
- L'audit dépend des quatre certificats physiques déjà établis ; il n'est **pas** un second oracle indépendant non-IBP.

## Limites et prochain verrou

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.** Le rang complet des contraintes, les chartes `K=0/J=0`, les conditions de bord, les éventuelles contraintes tertiaires, la jauge temporelle, la dynamique 4D, la stabilité et les observables ne sont pas démontrés. Prochaine étape **68ad-C2d2e5** : reconstruire l'opérateur de Dirac fonctionnel complet (six couples, non-IBP, termes de bord), confronter la dimension du noyau et les contraintes tertiaires aux conditions de bord ; analyser séparément les chartes singulières. Ne pas interpréter cet audit comme un certificat d'absence de fantôme BD.
