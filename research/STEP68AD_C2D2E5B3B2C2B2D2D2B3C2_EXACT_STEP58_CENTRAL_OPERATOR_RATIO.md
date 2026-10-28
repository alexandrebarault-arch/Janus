# JANUS — b3c2 : coefficients centraux exacts de l'opérateur Step58 original

28 octobre 2026. **Résultat local exact sous les hypothèses de la branche spatiale Step55 ; pas de fermeture Dirac complète. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources originales et provenance

Les sources GitHub lues et authentifiées par SHA blob sont : Step45 `numerics/hr_step45_exact_physical_ward.py` = `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ; Step58 `numerics/hr_step58_temporal_operator.py` = `802c23aebd41780d8c462f1aa1711707fe4ee88f` ; Step55 `numerics/hr_step55_global_barrier.py` = `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Le moteur Step58 est le véritable opérateur local six couples incluant la réponse du shift relatif `z,z'`, et **non** un substitut minisuperspace. Les sources originales Python n'ont pas été réexécutées dans un clone intégral pendant cette session ; leurs expressions ont été reconstruites et évaluées localement en arithmétique algébrique exacte, puis un script de reproduction important a été publié pour exécution dans le dépôt complet.

## Résultat central

Notons `A_N(r),A_M(r)` les coefficients d'ordre zéro du véritable opérateur temporel `physical_operator()['operator']`, et `B_N,B_M`, `E_N,E_M` ses coefficients de `N',M'` et `N'',M''`. Sur les données centrales analytiques Step55, avec les deux poussières obtenues par les primaires originales, `z=r/250`, `S_i=rL_i`, `pLf=r²U(r²)` et `U(0)=U0` fixé par Step49, le développement formel donne :

```text
A_N(r) = a_N r² + O(r⁴)
A_M(r) = a_M r² + O(r⁴)
B_N(r), B_M(r), E_N(r), E_M(r) = O(r⁴)
```

Les coefficients `a_N,a_M` appartiennent exactement au corps quadratique `Q(sqrt(H2))`, où `H2` est la fraction rationnelle du certificat JSON. Le certificat fournit `a_N=a+b sqrt(H2)`, `a_M=c+d sqrt(H2)` avec leurs quatre fractions **exactes**, sans approximation décimale. Les comparaisons de signe par carrés d'entiers rationnels donnent strictement :

```text
3507 < a_N < 3508
-6765 < a_M < -6764
1037/2000 < -a_N/a_M < 2593/5000
```

La valeur affichée `-a_N/a_M ≈ 0.518543059543765887366640491501` n'est qu'un arrondi du nombre algébrique exact.

**Point nouveau décisif :** les coefficients `N',M',N'',M''` ne contribuent pas au terme `r²` pour des lapses scalaires réguliers au centre (`N',M'=O(r)`, `N'',M''=O(1)`). Il n'est donc pas nécessaire de supposer leur annulation globale pour déterminer **ce seul coefficient dominant central**. Leurs contributions hors centre et l'opérateur global restent ouverts.

La vérification formelle autorise les sept coefficients `u1,...,u7` arbitraires de `U(s)=U0+sum(u_k s^k)` : les 28 dérivées des quatre composantes algébriques de `a_N,a_M` par rapport à ces `u_k` sont exactement nulles. Le contrôle de valuation des dépendances de `A_N,A_M` en `pLf,pSf,pf` et leurs dérivées montre que toute correction `U(s)-U0=O(r²)` n'affecte ces coefficients qu'à partir de `O(r⁴)`. Cette conclusion ne suppose donc pas que les sept coefficients libres décrivent eux-mêmes des solutions physiques : ils servent de test de non-dépendance du terme dominant.

## Conséquence temporelle — conditionnelle, mais plus forte que b3c1

Pour des lapses positifs, pairs et `C²` au centre, si la préservation temporelle originale `dot C=0` s'applique sur la coquille spatiale Step55, son terme dominant impose :

```text
a_N N(0) + a_M M(0) = 0
M(0)/N(0) = -a_N/a_M in (1037/2000,2593/5000)
```

En revanche, maintenir stationnaire au centre la différence des horloges avec shift diagonal régulier impose `M(0)=N(0)` (b3a/b3c1). Les deux exigences sont **incompatibles si N(0)>0**. Plus directement, `a_N+a_M<-3256<0`. C'est un **no-go conditionnel pour cette condition de bord temporelle particulière** sur la branche Step55 prescrite, **pas un no-go JANUS** : on peut laisser évoluer la différence d'horloges, choisir d'autres données aux bords ou examiner un autre fond, et la dynamique complète n'est pas certifiée.

Le résultat ne constitue ni un calcul de la matrice complète de Dirac, ni une preuve d'absence de fantôme BD, ni une condition de stabilité 4D.

## Reproductibilité et limites de l'exécution

Le programme Python publié `numerics/hr_step68ad_c2d2e5b3b2c2b2d2d2b3c2_center_operator.py` réimporte les véritables Step45/Step58 et vérifie les trois SHA avant de développer les jets. Le test publié `tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d2b3c2_center_operator.py` vérifie les coefficients, les annulations, la non-dépendance aux sept `u_k` et les inégalités par comparaison algébrique exacte. Le JSON contient les fractions nécessaires à un contrôle indépendant.

**Exécuté dans cette session :** 190 comparaisons symboliques/algébriques exactes sur une reconstruction locale des expressions originales, 0 échec ; 6 vérifications de signe supplémentaires avec fractions BigInt dans V8 sur le certificat publié, 0 échec ; sonde numérique haute précision sur huit rayons uniquement exploratoire. Les trois SHA sources ont été relus sur GitHub. Le test Python **publié** n'a pas été exécuté dans un clone GitHub complet ; ne pas le compter comme un passage supplémentaire. La validité de l'évaluation locale exige la fidélité de la reconstruction, vérifiable lors d'un rejeu dans le dépôt avec les imports originaux.

## Prochaine étape

**b3c3 :** rejouer le nouveau script/test dans un clone complet et comparer le certificat aux expressions authentiques ; contrôler indépendamment les termes de shift diagonal dans la préservation fonctionnelle, la compatibilité des bords et la conservation des charges. Puis générateurs temporels améliorés, quotient de jauge temporelle, matrice Dirac non-IBP six couples/rang/tertiaires, chartes `K=0/J=0`, dynamique 4D, stabilité et observables. Ne pas étendre le no-go conditionnel à d'autres conditions de bord sans preuve.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
