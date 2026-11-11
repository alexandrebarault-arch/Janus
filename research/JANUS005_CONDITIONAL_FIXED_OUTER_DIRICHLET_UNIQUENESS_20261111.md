# JANUS-005 — Obstruction conditionnelle à une trace extérieure de Dirichlet fixe (2026-11-11)

**HEAD source fixé :** `e4e2c75faa803974f0ba280f4143f4b02a8b1d37`. **Nature :** corollaire analytique des bornes Step49/55 déjà publiées, non nouvelle exécution des opérateurs physiques.

## Énoncé précisément conditionnel

Soit une famille différentiable `lambda -> U(s,lambda)` sur l'intervalle connecté `I=[-1/5000,1/5000]`, satisfaisant *uniformément* les hypothèses et bornes Step49/55 des rapports `JANUS005_CONDITIONAL_PHYSICAL_G_PARAMETER_TOTAL_VARIATION_SIGN_20261111.md` et `JANUS005_CONDITIONAL_OUTER_F_MOMENTUM_TRACE_TANGENT_BOUNDS_20261111.md`. Au vrai rayon extérieur `R=17/20`, posons `P(lambda)=pLf(R,lambda)` et `Q(lambda)=pLf'(R,lambda)`. Les résultats antérieurs donnent

```
0.004920225 < P'(lambda) < 0.004978025,
0.0115071614336092885 < Q'(lambda) < 0.011738073957404807.
```

Pour tout `lambda_1<lambda_2` dans `I`, le théorème des accroissements finis (ou l'intégrale de la dérivée) implique strictement

```
0.004920225*(lambda_2-lambda_1) < P(lambda_2)-P(lambda_1)
                                      < 0.004978025*(lambda_2-lambda_1),
0.0115071614336092885*(lambda_2-lambda_1) < Q(lambda_2)-Q(lambda_1)
                                      < 0.011738073957404807*(lambda_2-lambda_1).
```

**Corollaire falsifiable :** la condition de Dirichlet `pLf(R,lambda)=C`, avec **C indépendant de lambda**, possède *au plus une solution* sur cette famille conditionnelle. Il en va de même de `pLf'(R,lambda)=D` avec D fixe. Il est donc impossible que deux valeurs distinctes du paramètre satisfassent simultanément une de ces conditions fixes, tant que les hypothèses uniformes sont vraies.

Cela **n'exclut pas l'existence d'une solution isolée**, ne démontre pas l'existence d'une telle solution, et ne vaut **pas** pour des conditions au bord qui dépendent de lambda, pour une autre famille, ou pour une famille où les bornes échouent. Ce n'est pas une preuve que les conditions physiques de JANUS prescrivent ces traces séparément. Une condition mixte `aP+bQ=C` n'est strictement monotone que si `a,b` rendent la combinaison de dérivées de signe strict; par exemple `a,b>=0` non tous nuls. Les conditions couplées avec d'autres traces restent ouvertes.

## Contrôle arithmétique indépendant réellement exécuté

Commande locale `python` utilisant `fractions.Fraction` et les décimales exactes des deux rapports antérieurs : calcul des quatre bornes dérivées et des variations sur `Delta lambda=1/2500`, puis assertions `0<m<M`, `0<a<b`, `m*Delta>0`, `a*Delta>0`. **PASS**.

Pour les extrémités de I, les variations conditionnelles sont strictement comprises entre `0.00000196809` et `0.00000199121` pour P, et entre `0.0000046028645734437154` et `0.000004695229582961923` pour Q. Ces valeurs ne sont pas des évaluations physiques directes de la famille : ce sont des bornes conditionnelles.

## Limites et contre-épreuve

La monotonie ne donne pas l'absence de racine : la fonction abstraite `P(lambda)=C+0.00495*(lambda-lambda_0)` respecte les bornes et satisfait `P(lambda_0)=C`. Inversement `P(lambda)=C+1+0.00495*lambda` les respecte sans jamais satisfaire `P=C` sur I. La preuve est donc exactement une **unicité éventuelle**, non une existence ou un NO-GO cosmologique.

**Nouveaux tests originaux Step55/58 : 0. Cellules physiques nouvelles évaluées : 0, certifiées : 0.** Aucun calcul du jacobien Step46 des deux autres traces.

**NEXT_ACTION_EXACT :** déterminer dans les sources originales les véritables conditions extérieures (fixes, mobiles ou mixtes), calculer les coefficients H, chi, Lf/Sfr, kf et les deux traces restantes; tester la transversalité des conditions effectivement imposées. En parallèle, JANUS-001 reste bloqué sur la reconstruction authentique des dépendances du pilote à une cellule.

**GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.**
