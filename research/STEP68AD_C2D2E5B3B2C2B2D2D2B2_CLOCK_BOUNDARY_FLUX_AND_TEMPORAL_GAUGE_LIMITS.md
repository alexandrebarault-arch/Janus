# JANUS — 68ad-C2d2e5b3b2c2b2d2d2b2 : flux d'horloges, charges et conditions aux frontières

28 octobre 2026. **Résultat exact restreint au Hamiltonien radial original nu et aux signes Step55. Ce n'est PAS une classification de la jauge temporelle. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Problème et source

L'étape b1 a montré deux translations constantes canoniques des horloges de poussière et une forme de bord non nulle. Il faut distinguer une symétrie des contraintes dans le volume d'une transformation admissible sur le domaine du Hamiltonien amélioré. Les densités originales sont celles de Step37/45, la forme de bord originale non-IBP celle de d2a, et les pentes Step55 celles du code authentifié.

Les coefficients de variation des deux horloges au bord, en posant les autres jets fixés et en utilisant l'enveloppe de l'équation du shift, sont

```
Jg = pg [ N*ag + z*(N/Lg+M/Lf) + V ]
Jf = pf [ M*af + V ]
ag = tg'/(Lg^2*sqrt(1+(tg'/Lg)^2))
af = tf'/(Lf^2*sqrt(1+(tf'/Lf)^2))
Theta_clock = Jg delta(tg) + Jf delta(tf).
```

Sur Step55 à R=17/20 : `Lg,Lf>0`, `tg'=kg R Lg` avec `kg=0.0012>0`, `tf'=kf R Lf` avec `kf=-0.0016<0`, `z=17/5000>0`. Les deux poussières `pg,pf>0` sont héritées du certificat spatial antérieur, non recalculées ici. Ainsi `ag>0`, `af<0`.

## Théorème de flux simultané : incompatibilité pour N,M>0

Définir `A=ag+z/Lg>0`, `B=z/Lf>0`, `D=af<0`. Alors

```
Jg/pg = N*A + M*B + V
Jf/pf = M*D + V.
```

Si `Jg=0`, il faut `V=-N*A-M*B<0`. Si `Jf=0`, il faut `V=-M*D>0`. **Contradiction stricte pour tous N,M>0**, indépendamment de leur rapport. Plus précisément, l'écart des deux valeurs requises est `N*A+M*(B-D)>0`.

Donc, sur la frontière extérieure Step55, **aucun shift diagonal réel commun ne permet de laisser varier indépendamment les deux horloges avec un flux de bord nul dans le Hamiltonien ORIGINAL NU, pour des lapses strictement positifs et sans contreterme**. Cela ne vaut pas pour des conditions mixtes, des contretermes améliorés, des lapses contraints par Dirac, ou des changements de secteur/paramètres.

## Rang des multiplicateurs et obstruction de primitive sur espace étendu

Pour `pg,pf>0`, la matrice des coefficients de `(N,M)` dans `(Jg,Jf)` est

```
[ pg*A    pg*B ]
[   0     pf*D ].
```

Son déterminant `pg*pf*A*D<0` est strictement non nul. Ainsi **aucune direction fixe non nulle du plan (delta tg, delta tf) n'annule le flux pour tous les N,M indépendants**, même à V fixé. Cette assertion est algébrique sur le domaine des multiplicateurs indépendants, et ne prouve pas leur indépendance après préservation temporelle.

Sur le sous-espace où `N,M,V,pg,pf` et tous les autres jets sont FIXES, `Theta_clock` possède la primitive `Jg*tg+Jf*tf`; le contreterme formel `C=-Jg*tg-Jf*tf` annule donc cette composante SUR CE PLAN. Dès que les multiplicateurs varient indépendamment, `dTheta_clock` contient `pg*A dN∧dtg` et `pf*D dM∧dtf`, non nuls. Aucun scalaire ne peut annuler `Theta_clock` sur cet espace étendu ouvert avec les autres champs fixés. Ce n'est pas un no-go contre tous les contretermes du Hamiltonien complet : des variations et conditions aux limites supplémentaires peuvent changer le domaine et les termes autorisés.

## Conditions sur les valeurs d'horloge et charges

Les translations constantes sont engendrées FORMELLEMENT par `Qg=∫pg dr`, `Qf=∫pf dr`, avec `{ti(r),Qj}=δij` pour la structure canonique de volume. Elles préservent les contraintes dans le volume mais **leur caractère de charges physiques conservées, de jauge temporelle ou de transformations exclues reste indéterminé** sans générateurs temporels améliorés et conditions aux bords.

Pour le plan des translations constantes `(cg,cf)`, toute valeur d'horloge fixée au centre OU au bord élimine la translation correspondante. Fixer `tg(0)` et `tf(0)` élimine les DEUX, même si les valeurs extérieures sont libres. Fixer uniquement `tg-tf` à une frontière laisse la translation diagonale `cg=cf`. Fixer les deux valeurs extérieures élimine les deux. Les sept cas sont certifiés par rangs exacts de matrices 0/±1. **Ces rangs sont des rangs de compatibilité des données de bord, PAS des rangs physiques de Dirac.**

Pour des conditions de Neumann/Robin ou une condition dépendant des lapses, une direction non triviale peut rester autorisée ; sa préservation temporelle et sa charge doivent être vérifiées, pas supposées.

## Calcul reproductible et limites

Le programme `scripts/hr_step68ad_c2d2e5b3b2c2b2d2d2b2_clock_boundary_flux.cjs` a exécuté **57 assertions rationnelles BigInt exactes, 0 échec**. L'encadrement de `1/sqrt(1+u)` utilise `1-u/2 <= 1/sqrt(1+u) <= 1` pour `0<=u<=2`, démontré par `(1-u/2)^2(1+u)=1-u^2(3-u)/4<=1` ; aucun flottant n'est utilisé pour les certificats. Les fractions précises sont dans le JSON. Le test Node rejoue ces assertions et ajoute dix gardes non indépendants.

Sources relues et SHA Git authentifiés : Step37 `005449ade6e3582e3b9a5c3374a881a77e73e3f6`, Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, forme de bord d2a `94bd7e089ebb0978569361c03a4f3ab950b950df`, b1 `1d973e04f296df9144f6ddef40681dd18342e28e`. Les moteurs Python originaux **n'ont pas été réexécutés**.

## Prochaine étape

**68ad-C2d2e5b3b2c2b2d2d2b3** : calculer les générateurs temporels AMÉLIORÉS et leurs charges, leur action sur les horloges et la préservation des conditions au centre et à R, puis classifier les translations après quotient de la jauge temporelle. Construire deux directions canoniques non-jauge sur la surface complète de Dirac, calculer le pullback de dTheta et les contretermes admissibles. L'oracle original non-IBP à six couples, le rang, les tertiaires, les lapses, K=0/J=0, la dynamique 4D, la stabilité et les observables restent ouverts.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
