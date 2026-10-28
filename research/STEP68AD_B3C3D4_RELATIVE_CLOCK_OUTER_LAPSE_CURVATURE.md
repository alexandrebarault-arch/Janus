# JANUS — b3c3d4 : courbure extérieure après préservation de l'horloge relative

28 octobre 2026. **Théorème exact sur une tranche de multiplicateurs étendue de la famille spatiale Step55 ; NON une obstruction Dirac.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Sources et portée

Step45 physique `numerics/hr_step45_exact_physical_ward.py` (blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`), Step55 `numerics/hr_step55_global_barrier.py` (`a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`), audit de la famille Step55 `research/STEP68AD_C2D2E5B3B2C2B2D2D1_STEP55_SPATIAL_SHELL_MULTIPLIER_CURVATURE.md` (`1ba6d012133a92b69a8c91498d065b22649afbe0`), évolution des horloges `research/STEP68AD_C2D2E5B3B2C2B2D2D2B3A_CLOCK_TIME_EVOLUTION_BOUNDARY_PRESERVATION.md` (`f0756adb6b98574700591ae8cb8a1b10bbc60eb9`). Sources relues par connecteur ; imports originaux Step45/55/58 et b3c2 **NON rejoués**, le clone Git échouant en DNS.

À `R=17/20`, la famille spatiale Step55 a une direction canonique `lambda`, avec `a=∂lambda pLg=92730563/128000000>0` et `b=∂lambda pLf>0` (bornes précédemment certifiées), tandis que `Lg,Lf,tg',tf',z` sont fixes dans cette famille. Poser `q=Lg/Lf>0`, `T=tg'>0`, `U=-tf'>0`, `sg=sqrt(1+(T/Lg)^2)>0`, `sf=sqrt(1+(U/Lf)^2)>0`, `H=Lg*a+Lf*b>0` et lapses indépendants `N,M` (cette indépendance **n'est pas** imposée par Step58). La forme non-IBP, tirée sur cette direction à géométrie fixée, est

`Theta=F(lambda,N,M,V) d(lambda)`, `F=-z*a*(N+q*M)-H*V`.

Préserver instantanément `tg-tf` au bord impose le shift diagonal unique

`Vrel=[M*sf-N*sg-z*(N/Lg+M/Lf)*T]/(T+U)`.

En substituant `V=Vrel`, `F=cN*N+cM*M`, avec

`cN=-z*a+H*(sg+z*T/Lg)/(T+U)` et

`cM=-z*q*a-H*(sf-z*T/Lf)/(T+U)`.

**Identité exacte et stricte :**

`cM-q*cN=-H*(sf+q*sg)/(T+U)<0`.

Ainsi, les deux coefficients mixtes `dN∧d(lambda)` et `dM∧d(lambda)` de `dTheta` ne peuvent **jamais** être simultanément nuls sur l'espace étendu avec `N,M` libres, malgré le choix de shift préservant l'horloge relative. Le terme `z` s'annule exactement de cette combinaison. Cette propriété est plus précise que le constat de courbure mixte avant fixation du shift dans d2d1. Elle ne prouve aucune non-fermeture sur le sous-espace de lapses **admissibles** par Step58 : une relation temporelle `M=M(N,lambda)` pourrait retirer une direction de variation. Les lapses sont des multiplicateurs, pas des coordonnées canoniques ; le rang physique n'est pas établi.

Témoin rationnel **non Step55** : `Lg=2/5,Lf=3/5,a=3/4,b=1/200,T=3/10,U=1/4,sg=5/4,sf=13/12,z=1/5` : `cN=3417/5500`, `cM=-7059/11000`, `cM-q*cN=-2323/2200`. Les valeurs `sg=5/4` et `sf=13/12` vérifient exactement `sg²=1+(T/Lg)²` et `sf²=1+(U/Lf)²`. Le témoin respecte donc les relations cinématiques des horloges, mais **ne** constitue **pas** une solution Step55 ou Dirac.

## Reproductibilité

`python -m numerics.hr_step68ad_b3c3d4_relative_clock_lapse_curvature` : **13 résidus symboliques exacts nuls**, 6 assertions rationnelles/contrôle négatif PASS. `python -m unittest -v tests.test_hr_step68ad_b3c3d4_relative_clock_lapse_curvature` : **4 cas PASS**, non indépendants. 0 FAIL. Les 4 tests rejouent la même fonction, et ne constituent pas une validation indépendante. Aucun test d'import des moteurs originaux n'est revendiqué.

## Verrous

Les variations de lapses libres ne sont pas nécessairement tangentes à la préservation temporelle Step58 ; les variations spatiales de lambda ne sont pas certifiées tangentes à la chaîne Dirac complète ; la forme de bord extérieure complète sur un espace physique de variations et les générateurs/charges améliorés restent à calculer. L'horloge relative stationnaire au bord extérieur n'assure pas les conditions centrales. Il faut ensuite quotienter la jauge temporelle, calculer les six couples/rang/tertiaires, couvrir `K=0/J=0`, reconstruire 4D et tester stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

**Prochaine étape b3c3d5 :** contraindre effectivement `(N,M)` par l'opérateur original Step58 sur Step55 et calculer `dTheta` sur la sous-variété temporelle, avec replay original b3c2 et contrôle des conditions aux deux bords. Ne pas prolonger une chaîne de résultats de jets libres comme preuve physique.
