# JANUS — Step68ad-C2d1 : annulation exacte des jets élevés et régularité conditionnelle de la variation du shift

Date : 2026-10-26. **Avancée algébrique sur le véritable secteur de réponse du shift de Step58 ; aucun des sept signes temporels Step58/60 n'est encore évalué.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Provenance et méthode

Les sources originales Step45 (`66aa43841dccfe4a5d586a49be9c10af3a67a10e`), Step58 (`802c23aebd41780d8c462f1aa1711707fe4ee88f`) et Step60 (`9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`) ont été lues intégralement via le connecteur GitHub et authentifiées **3/3 par SHA-1 Git recalculé indépendamment à partir des octets UTF-8**, avec un vecteur de contrôle SHA-1 connu. Le module autonome reconstruit les densités post-IBP originales `Ag,Bg,Af,Bf` de Step45, leurs Euler jets `E0,E1,E2` et les huit composantes canoniques qui contribuent à `D` ou `K` (issues du système original à six paires), puis exactement les variations `deltaD` et `deltaK` de Step58. Les sources originales ne sont pas modifiées. Le clone local complet n'est pas disponible : **le code de Step58 lui-même et l'opérateur temporel `Cdot` n'ont pas été exécutés** ; le calcul est une re-dérivation indépendante de son sous-opérateur de shift.

## Résultat exact hors contraintes : les jets de lapse d'ordre 2 et 3 s'annulent dans δD et δK

Dans Step58, `D=pSg*Sg' - Lg*pLg' + pg*tg'`, `K=m2*mg*Lg*Lf*(b1*Sg²+2*b2*Sg*Sf+b3*Sf²)` et `deltaZ=Z_D*deltaD+Z_K*deltaK`. La variation canonique utilise exactement `X_i=+E_{p_i}` pour une coordonnée et `X_i=-E_{q_i}` pour son moment conjugué, avec `X'_i` comprenant la dérivée du lapse. Pour **les deux secteurs N et M**, l'algèbre SymPy donne identiquement, sans imposer Fz=0 ni les contraintes :

```
[deltaD]_{N''}=[deltaD]_{N'''}=[deltaK]_{N''}=[deltaK]_{N'''}=0
[deltaD]_{M''}=[deltaD]_{M'''}=[deltaK]_{M''}=[deltaK]_{M'''}=0
```

Il s'agit de **huit identités exactes**, pas de petits nombres numériques. Elles concernent **uniquement la variation du shift** et ne prétendent pas supprimer les dérivées de lapse dans l'ensemble de `Cdot`.

## Résultat au centre : condition de régularité de δZ

Pour les profils réguliers analytiques de Step68o, avec `s=r²`, `Lg=A+O(r²)`, `Lf=B+O(r²)` (A,B>0), `Sg=r*Lg`, `Sf=r*Lf`, `pLg=r²(G+O(r²))`, `pSg=r(P+O(r²))`, `z=r*Z`, les expansions exactes de la réponse du shift donnent :

```
lim_{r->0} ([deltaD]_N / r) = Z*(P-2*G)
lim_{r->0} ([deltaD]_M / r) = 3*A*Z*(P-2*G)/B
```

Les coefficients d'ordre supérieur des profils ont été laissés **symboliques et indépendants**, jusqu'à l'ordre nécessaire ; ces identités ne reposent pas sur un échantillon de constantes. La condition originale de stationnarité `Fz=D-K*z/sqrt(1-z²)=0` impose `P=2G`, puisque `D=A(P-2G)r+O(r³)` et `K*z=O(r³)`. Sur cette coquille, les deux variations à lapse d'ordre zéro deviennent `deltaD_{N0},deltaD_{M0}=O(r³)` (coefficients limites explicites certifiés dans JSON). Les deux coefficients à lapse dérivée sont `deltaD_{N1},deltaD_{M1}=O(r²)` ; les variations de K sont `deltaK_{N0},deltaK_{M0}=O(r²)` et `deltaK_{N1},deltaK_{M1}=O(r³)`. Les jets plus élevés sont identiquement nuls.

Pour des lapses réguliers **pairs** `N=N0+O(r²)`, `M=M0+O(r²)`, on a `N',M'=O(r)`. Ainsi `deltaD=O(r³)` et `deltaK=O(r²)` pour la variation totale. Step68ad-C2c a certifié `K=r²*kappa(r²)` avec `kappa>0` sur le domaine et `z=O(r)`. Dans la formule originale non figée `Z_D=(1-z²)^(3/2)/K=O(r^-2)`, `Z_K=-z*(1-z²)/K=O(r^-1)`, d'où **deltaZ=O(r)**. La divergence de `Z_D` prise isolément ne force donc pas une divergence de la variation complète du shift, **sous ces hypothèses de parité et de stationnarité**.

Cette régularité est une condition nécessaire utile à l'évaluation temporelle au centre, **pas une preuve d'existence de lapses positifs admissibles**, de préservation des contraintes ou de rang de Dirac. Elle ne s'étend pas automatiquement aux lapses non pairs ni aux perturbations hors Fz=0. Les sept cellules strictement positives `[1/64,1/32]` restent à évaluer numériquement.

## Vérification et reprise

`PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d1_shift_variation_center.py` : **22 tests réellement exécutés, 22 PASS, 0 FAIL** (~11,21 s). Les huit annulations exactes hors coquille, les deux limites centrales, les deux annulations sur Fz=0, les ordres de `deltaD`/`deltaK`, la portée scientifique et un test négatif de provenance sont vérifiés. Le certificat JSON contient les expressions symboliques complètes des coefficients centraux, avec les constantes laissées libres. **Pas de calcul de signes temporels**.

**NEXT 68ad-C2d2 :** dans un environnement permettant l'exécution des sources complètes authentifiées, construire l'adaptateur `Jet([U,U_s,U_ss/2,U_sss/6])` sur les sept boîtes C2b, injecter dans Step68o sans le modifier, exécuter les véritables coefficients `A_N,A_M` de Step58 puis les quotients Step60, et conserver INCOMPLETE pour tout intervalle recouvrant zéro. Exploiter les annulations exactes de `deltaD`/`deltaK` avant `1/K` pour le centre. Ensuite seulement : rang Dirac, lapses/bords, BD, dynamique 4D et observables.
