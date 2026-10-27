# JANUS — 68ad-C2d2e5b3b2c2b3c2b2b : dérivées du véritable G et barrière de sensibilité physique

**27 octobre 2026 — résultat spatial rigoureux sous les hypothèses de continuation analytique centrale Step49 et du tube authentique Step55/b2. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Changement scientifique effectif

Pour la première fois dans cette sous-campagne, les dérivées du **véritable** moteur normalisé Step45/46/55 sont évaluées sur le continuum radial et paramétrique, et non sur un moteur synthétique. Les quatre sources physiques originales sont copiées localement depuis GitHub, authentifiées **octet pour octet** par SHA Git, puis exécutées ; leurs empreintes sont :

- `numerics/hr_step45_exact_physical_ward.py` : `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
- `numerics/hr_step46_exact_secondary_ode.py` : `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
- `numerics/hr_step55_normalized_secondary.py` : `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`.
- `numerics/hr_step55_global_barrier.py` : `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.

L'évaluation exploite `compiled()`, qui compile le `normalized_symbolic()` exact issu du Poisson sphérique original à six couples. Un nombre dual d'intervalles dirigés `(valeur, dérivée_U, dérivée_Pg)` traverse **le même programme compilé**, avec toutes les règles produit, quotient et racine carrée. Le dérivé paramétrique inclut obligatoirement les quatre entrées `Gmom`, `Gprime`, `Rhog` et `Psg0`, reconstruites avec `Pg+lambda`. Les autres coefficients géométriques sont indépendants de Pg sur cette famille.

## Théorème de barrière pour la véritable sensibilité

Poser `s=r²`, `S=289/400`, `|lambda|<=1/5000`, et `v(s,lambda)=partial_lambda U(s,lambda)`. La variation du moteur original satisfait

```
2s v_s = (G_U(s,U,Pg+lambda)-2)v + G_Pg(s,U,Pg+lambda)
v(0)=Mf2*b/a.
```

Les 256 cellules rationnelles jointives du domaine radial, le tube de comparaison `U_star(s,lambda) ± 1/10000` précédemment certifié dans b2 et l'arithmétique entière extérieure `10^-28` donnent **simultanément pour tout le domaine** :

```
-1.001099494671 < G_U < -0.993939366018
 0.020435412499 < G_Pg < 0.020578225856
```

Ces affichages décimaux sont volontairement arrondis **vers l'extérieur** ; les fractions exactes du certificat JSON font autorité. Les signes stricts sont certifiés et le coefficient `A=G_U-2` est négatif. Les barrières constantes `v_-=681/100000=0.00681` et `v_+=689/100000=0.00689` vérifient, avec fractions exactes :

```
min_s,lambda,U [ A*v_- + G_Pg ] >=
1024922611588406880813/62500000000000000000000000 > 0

max_s,lambda,U [ A*v_+ + G_Pg ] <=
-841114594602624479574991/10000000000000000000000000000 < 0.
```

L'identité centrale originale `G(0,U,P)=3*Mf2*b*(P/a-2*z1)-U` implique `G_U(0)=-1`, `G_Pg(0)=3*Mf2*b/a`, et `v(0)=Mf2*b/a` strictement **à l'intérieur** de ces barrières. Par l'argument du premier contact appliqué à `2s v_s=A v+B` pour `s>0`, et la solution régulière analytique au centre, la sensibilité reste enfermée sur le domaine :

```
0.00681 < v(s,lambda) < 0.00689
pour 0 <= s <= 289/400 et |lambda| <= 1/5000.
```

En particulier, **`0.00681 < v(R²,lambda) < 0.00689` à `R=17/20`**. Il s'agit d'un **encadrement uniforme** de la vraie sensibilité extérieure, **pas** d'une valeur ponctuelle exacte de v(R) ni d'un calcul de la dérivée de chaque trace f. L'énoncé demeure conditionné par le théorème Step49 et par le tube spatial authentique b2 ; il ne sélectionne pas les conditions aux limites physiques.

## Contrôles exécutés

Commande exécutée dans une arborescence isolée contenant les quatre sources originales SHA-identiques :

```bash
PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational.py' -v
PYTHONPATH=. python -m numerics.hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational
```

**17 tests unittest PASS, 0 FAIL**, comprenant la vérification des quatre SHA, les identités centrales, les opérations différentielles duales, une **contre-vérification indépendante par dérivation symbolique SymPy** des dérivées du moteur original à `s=1/3`, l'identité des valeurs du moteur dual et du moteur original, les barrières à 256 et 512 cellules et la détection attendue d'une barrière trop étroite `[0.00682,0.00688]`. Ce dernier échec de certification ne signifie pas que la vraie sensibilité sort de l'intervalle plus étroit.

Fichiers de cette étape :
- `numerics/hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational.py`.
- `tests/test_hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational.py`.
- `research/reports/gate2b-step68ad-C2d2e5b3b2c2b3c2b2b-authentic-variational-barrier.json`.

## Limites scientifiques et suite

Cette étape **ne calcule pas** les quatre sensibilités des traces f, ne détermine pas les conditions physiques aux frontières, ne construit aucun contreterme admissible, et ne démontre ni fermeture temporelle, ni rang complet de Dirac, ni tertiaires, ni lapses admissibles, ni chartes K=0/J=0, ni évolution 4D, ni stabilité, ni observables. Le rang du jacobien formel de traces antérieur n'est pas le rang de Dirac.

**Prochaine étape effective : 68ad-C2d2e5b3b2c2b3c2b2c** — utiliser le nouveau tube de v et les identités Step46 pour encloser `delta V=G_U*v+G_Pg`, puis les quatre dérivées des traces f à R ; définir ensuite l'espace des bords et les contretermes, avant l'oracle original non-IBP six couples et la fermeture de Dirac.

**Verdict : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
