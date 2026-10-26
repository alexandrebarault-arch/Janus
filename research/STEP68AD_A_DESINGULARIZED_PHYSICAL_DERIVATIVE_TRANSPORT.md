# JANUS — Step68ad-A : transport des dérivées sans division par le rayon nul

**26 octobre 2026 — recherche, branche `research/gate2b-nonhomothetic-transfer`.**  
**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

## Résultat réellement nouveau

On conserve **la vraie équation physique originale** des Steps45/46/55, déjà authentifiée au Step68ac :

```
2 s U'(s) = G(s,U(s)) - 2 U(s),     s=r²,    U=pLf/r².
```

La dérivation de cette équation donne une hiérarchie exacte **non singulière au centre sous forme de transport**, plutôt qu'une estimation instable obtenue en divisant un intervalle contenant s=0. En posant `y_n=U^(n)(s)` et `G_U=∂G/∂U` sur la solution physique :

```
2 s y_n'(s) + a_n(s) y_n(s) = R_n(s),
a_n(s)=2(n+1)-G_U(s,U(s)),
R_n(s)=d^n/ds^n [G(s,U(s))] - G_U(s,U(s))*U^(n)(s).
```

**Fait important : R_n ne dépend pas de la dérivée U^(n) que l'on cherche à encadrer.** Les identités n=1,2,3,4 sont vérifiées exactement par SymPy, y compris tous les termes de la règle de chaîne.

Les premiers termes sources, écrits avec `u1=U_s`, `u2=U_ss`, `u3=U_sss` :

```
R1 = G_s.
R2 = G_ss + 2 G_sU u1 + G_UU u1².
R3 = G_sss + 3 G_ssU u1 + 3 G_sUU u1² + G_UUU u1³
     + 3 G_sU u2 + 3 G_UU u1 u2.
R4 = d⁴/ds⁴[G(s,U(s))] - G_U u4,
     sans u4, avec dérivées mixtes de G d'ordre <=4 et u1,u2,u3.
```

Ces formules sont des **identités mathématiques exactes**, pas des évaluations nouvelles des dérivées du G physique sur un anneau.

## Nouveau théorème de comparaison régulier à s=0

Si `a_n(s)>=amin>0` et `R_n(s)` sont continus sur `[0,S]`, si `a_n(s)<=amax`, et si la branche analytique au centre fournit `y_n` bornée, alors :

```
min_{a∈[amin,amax], R∈[Rlo,Rhi]} R/a
 <= U^(n)(s) <=
max_{a∈[amin,amax], R∈[Rlo,Rhi]} R/a
             pour TOUT s∈[0,S].
```

**Preuve :** pour s>0, la solution bornée de `2s y'+a(s)y=R(s)` s'écrit

```
y(s) = integral_0^s [a(t)/(2t)] exp(-integral_t^s a(v)/(2v) dv)
                       * [R(t)/a(t)] dt.
```

Le noyau est positif ; son intégrale est **exactement 1** parce que `a(t)>=amin>0` et donc le terme homogène diverge vers le centre sauf si sa constante est nulle. `y(s)` est une moyenne pondérée de `R/a`, ce qui prouve l'encadrement pour tous les s sans échantillonnage et sans diviser par s=0. La limite s→0 est donnée par continuité. Cette preuve ne suppose pas que R garde un signe.

Le programme `ratio_enclosure` calcule l'intervalle exact en `fractions.Fraction` en prenant les quatre quotients aux coins ; il rejette tout intervalle de damping non strictement positif.

## Application RÉELLE au G original : coefficients de transport strictement positifs

Le rapport historique **Step68v** (blob Git `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`) certifie, sur toute la branche physique `0<=s<=1/64` et le tube U associé :

```
-1.00608535216533... <= G_U(s,U) <= -0.99386192647064... < 0.
```

Les bornes exactes sont conservées dans le JSON. Ainsi, sur **l'intervalle continu physique original** (non seulement au centre), les quatre coefficients sont rigoureusement :

| n | a_n = 2(n+1)-G_U, bornes décimales indicatives |
|---|---|
| 1 | 4.99386192647 < a1 < 5.00608535217 |
| 2 | 6.99386192647 < a2 < 7.00608535217 |
| 3 | 8.99386192647 < a3 < 9.00608535217 |
| 4 | 10.99386192647 < a4 < 11.00608535217 |

**Ceci exclut un dénominateur de transport nul ou une résonance au centre pour les ordres 1 à 4 sur ce chart certifié.** Les quatre encadrements rationnels EXACTS sont enregistrés dans le rapport machine, sans recours à des flottants pour la preuve.

Le Step68ac (blob `16ae8dab3563c17134e4e20f886fb7306dc2e4ba`) fournit `G_U(0,U0)=-1` exactement, ainsi que U1..U4. Donc, avec `U^(n)(0)=n! U_n` :

```
R1(0)=  5 U1   >0,
R2(0)= 14 U2   <0,
R3(0)= 54 U3   <0,
R4(0)=264 U4   <0.
```

Ces signes et leurs intervalles sont **certifiés en fractions rationnelles originales**, mais ils ne sont pas des bornes de R2/R3/R4 sur tout `0<s<=1/1024`. Ne pas les extrapoler.

## Périmètre des calculs et vérifications

Sources historiques réellement relues via le connecteur GitHub : Step57 `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step60 `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7d`. **Ces opérateurs temporels ont été inspectés mais NON exécutés dans cette étape** ; le résultat ne concerne pas encore leurs signes ni le rang Dirac.

Les deux rapports physiques Step68v et Step68ac ont été **reconstitués localement avec SHA Git identiques** avant le calcul. Les 19 tests locaux Step68ad-A sont PASS (`pytest -q tests/test_hr_step68ad_center_derivative_transport.py`, 1.21s). Ils incluent : authentification fail-closed de deux blobs, quatre damping physiques, les quatre identités exactes, sources au centre, quotients rationnels positifs/négatifs/mélangés, exemple analytique fabriqué de contrôle, cas homogène singulier, non-validation explicite des jets et de la physique temporelle. L'exemple fabriqué n'est pas un nouvel oracle du G JANUS.

**Fichiers :**

- `numerics/hr_step68ad_center_derivative_transport.py` — blob Git attendu `3768d309f008391813c5fd70302ff487141afe1b`.
- `tests/test_hr_step68ad_center_derivative_transport.py` — blob Git attendu `79946d5f7220f7445676f27b68a92c0be30bf98e`.
- `research/reports/gate2b-step68ad-A-derivative-transport.json` — blob Git attendu `6be5cc1e9cb61479cf4b9dd897aa28105195d4f5`.

## Prochaine sous-étape 68ad-B — verrou réel, pas une formalité

**Le théorème ne fournit aucune borne U_ss ou U_sss sans bornes CONTINUES des sources physiques R2 et R3.** La prochaine tâche est d'évaluer les dérivées partielles du **G original fixe** via une AD multivariée à intervalles entiers, et non par différences finies ni différentiation de la seule enveloppe U.

1. Importer et SHA-authentifier Steps45/46/55/68n/68v/68ac. Sur `s∈[0,1/1024]`, propager le tube prouvé `Ustar ± kappa*s³` et le tube de `U_s` (Steps68v/x/z).
2. Enclore `G_ss,G_sU,G_UU` sur la totalité du chart et former R2 ; appliquer la comparaison positive pour U_ss.
3. Enclore `G_sss,G_ssU,G_sUU,G_UUU`, former R3 en réutilisant U_ss et appliquer la comparaison pour U_sss. Si nécessaire R4 pour le reste d'ordre supérieur, via G jusqu'à l'ordre quatre.
4. Convertir les jets U en jets canoniques radiaux, puis calculer l'opérateur temporel **original Step58** `A_N/r²,A_M/r²` sur les sept cellules PENDING `[1/64,1/32]`, l'anneau intérieur et le centre. Contrôler les contraintes de prolongation Step60 et tous les bords.
5. Ne pas déclarer GATE fermé sans rang Dirac complet, lapses, conditions aux limites, branches exceptionnelles et dynamique 4D.

**Verdict exact : Step68ad-A complétée, Step68ad-B NON complétée. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
