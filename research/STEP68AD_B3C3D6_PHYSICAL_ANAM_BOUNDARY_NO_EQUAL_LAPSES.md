# JANUS — Step58 : enclosures physiques conditionnelles de A_N, A_M (2 novembre 2026)

**Statut : avancée scientifique réelle, mais restreinte à la solution spatiale prescrite Step55 et aux bornes physiques archivées. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance authentifiée et champs réellement calculés

Le branchement observé lors de la reprise est `cb70fcb062363d87b0173baa5e53070b93226874`, branche `research/gate2b-nonhomothetic-transfer`.

Le programme `numerics/hr_b3c3d6_boundary_ANAM_interval_certificate.py` charge les expressions symboliques **originales** de l'opérateur Step58 pour **A_N=operator[N][0]** et **A_M=operator[M][0]** (Step58 blob Git `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step45 blob Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e`). Le shim Step57 est uniquement nécessaire à l'import original et ne rejoue **pas** le Step57 intégral.

Les données d'entrée en intervalles proviennent de `research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json`, blob Git contrôlé **`e74057dcf741bcdb655c7d9be48c6a9650d7ff3f`**. Ce sont des bornes ponctuelles amont issues de la géométrie et de l'EDO originales Step45/46/55. **La barrière originale à 256 cellules n'a pas été réexécutée pendant cette session** : ses résultats archivés sont réutilisés après contrôle des octets et des entrées, non présentés comme nouvelle preuve indépendante.

## Construction mathématique

Les quatre rayons sont exactement `1/4`, `1/2`, `7/10`, `17/20` ; `s=r²` est rationnel, *pas* l'approximation `float(r)**2`. L'archive contient les boîtes de `G(s,U)`, `G_s` composé (dérivée en s de **toute** la géométrie prescrite), `G_U`. L'invariance certifiée Step55 fournit `U0+U1*s+U2*s² ± 1/10000`. On applique :

```
U_s = (G-2U)/(2s)
U_ss = (G_s + (G_U-4)*U_s)/(2s)
```

Le moteur utilise des **intervalles entiers avec arrondi externe**, dénominateur `10^34`, opérations rationnelles, racines carrées délimitées par `isqrt`, et une arithmétique de jets holonomes en `r`. La valeur de `pLf'=d(r²U(r²))/dr` est propagée de façon cohérente ; `pSf` et `pf` sont reconstruits par les équations spatiales originales de poussière. Les symboles des 12 champs canoniques et leurs jets radiaux vont dans les **expressions originales** `operator[N][0]` et `operator[M][0]`. Un test structurel confirme qu'aucune dérivée radiale d'ordre >=2 de `pLf,pSf,pf` n'entre dans ces deux coefficients : `U_ss` suffit ; le polynôme quadratique holonome local est admissible pour ces coefficients ponctuels.

## Encadrements exacts stricts des coefficients

| r | A_N | A_M | A_N+A_M |
|---|---|---|---|
| 1/4 | (214,223) | (-430,-413) | (-215,-190) |
| 1/2 | (847,883) | (-1697,-1634) | (-850,-751) |
| 7/10 | (1639,1709) | (-3279,-3157) | (-1640,-1448) |
| 17/20 | (2385,2489) | (-4768,-4588) | (-2383,-2099) |

Les véritables extrémités rationnelles de l'enclosure, plus précises, sont reproductibles par la fonction `certified_report()`. Les inégalités des marges du tableau font l'objet d'assertions **exactes** `Fraction` dans les tests, sans tolérance flottante.

**Obstruction précise au bord :** sur le sous-secteur physique où `F_z=H_g=C=(H_g)_r=(F_z)_r=0` et sur la carte `K>0`, la factorisation exacte des jets de lapses dans l'original Step58 fournit `B_N=B_M=E_N=E_M=0`. La préservation temporelle locale donne donc `A_N N+A_M M=0`. Si le véritable bord extérieur est identifié à `R=17/20` avec `N(R)=M(R)>0`, il faudrait `A_N(R)+A_M(R)=0` ; ce qui est **incompatible** avec la marge stricte `-2383 < A_N(R)+A_M(R) < -2099`.

Cette conclusion est **conditionnelle à la coquille radiale complète, à l'archive certifiée Step55 et aux conditions au bord égales**. Elle ne démontre pas qu'aucune paire de lapses positifs n'existe pour d'autres conditions aux bords : en particulier au bord extérieur la relation algébrique `M(R)/N(R)=-A_N(R)/A_M(R)` autorise un rapport positif différent de 1. Le vrai problème global à deux bords et les générateurs/charges Dirac restent ouverts. Les coefficients `B/E` sont annulés par **identités de coquille**, **pas** par nouvelles boîtes d'intervalles hors coquille. Il ne s'agit donc pas encore des **24 boîtes physiques indépendantes A/B/E** exigées pour les quatre rayons.

## Rejeu et limitations

- `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_*bn*.py' -q` : **12 PASS, 0 FAIL** (rejeu b3c3d6 authentique).
- `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_boundary_ANAM_interval_certificate.py' -q` : **10 PASS, 0 FAIL**. Notamment : contrôle du SHA de l'archive, détection d'archive altérée, bornes d'intervalles à arrondi externe, dépendance aux jets, marges exactes.
- `python -m compileall -q numerics tests` : **PASS**.
- Source neuve blob Git `7e998fbbda8f3854093d530dc5e7e07703d70624` ; tests neufs blob Git `b5cf16826424bc624e15e18a8b18813a0251f859`. Octets identiques à ceux exécutés.
- Un calcul supplémentaire monolithique sur `B_M` a expiré lors du précédent travail interrompu : **non compté** comme réussite ici.
- Pas de nouveau rejeu original Step55/barrière 256 cellules, pas de nouveau DOP853 ; aucune certification du BVP général, du rang Dirac complet, du secteur `K=0`, de la 4D, de la stabilité ni des observables.

**Prochaine étape :** étudier explicitement l'admissibilité des lapses positifs avec rapport extérieur libre `M(R)/N(R)=-A_N/A_M` et deux vrais bords ; si des conditions imposent un rapport extérieur égal à 1, leur incompatibilité locale est désormais certifiée. Puis certificat indépendant des six coefficients dans la famille physique, Dirac et 4D.
