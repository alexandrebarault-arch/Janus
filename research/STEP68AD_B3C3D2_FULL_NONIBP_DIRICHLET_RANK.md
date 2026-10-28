# JANUS — b3c3d2 : forme de bord non-IBP complète sur tranche Dirichlet canonique

28 octobre 2026. **Théorème exact sur jets ambiants, non sur l'espace physique de Dirac.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Provenance

Sources originales consultées sur la branche `research/gate2b-nonhomothetic-transfer` : Step37 `numerics/hr_step37_original_nonibp_oracle.py` blob `005449ade6e3582e3b9a5c3374a881a77e73e3f6`, Step45 `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, et audit complet des dix coefficients non-IBP `numerics/hr_step68ad_c2d2e5b3b2c2b2d2_boundary_one_form.py` blob `94bd7e089ebb0978569361c03a4f3ab950b950df`. Les identités de bord sont ici **recalculées symboliquement** depuis la densité de courbure originale, les deux poussières et les shifts, pas simplement recopiées. Les moteurs originaux Step45/55/58 et b3c2 n'ont pas été importés/rejoués dans un clone complet : DNS github.com indisponible dans le conteneur.

## Théorème et preuve

Sur une extrémité régulière `K>0`, tenir fixes les six coordonnées canoniques `Lg,Sg,tg,Lf,Sf,tf`, ainsi que `N,M,V` (et leurs données prescrites), mais laisser varier les jets des moments et les gradients radiaux des coordonnées. Poser `a=N+M Lg/Lf`, `D=pSg Sg'−Lg pLg'+pg tg'`, `Z=D/sqrt(D²+K²)`, `P=a pLg`, `A=2 Mg2 N Sg/Lg`, `B=2 Mf2 M Sf/Lf` et `C=A Sg'+B Sf'−V Lg pLg−V Lf pLf`. Après l'élimination stationnaire de `z`, la **forme de bord complète originale non-IBP restreinte à cette tranche** est

`Theta_D = A dSg' + B dSf' − (a Z+V Lg) dpLg − V Lf dpLf = dC − Z dP`.

La variation induite de `z=Z` ne produit aucun terme supplémentaire, car `∂F/∂z=Q(D−K z/sqrt(1−z²))=0` sur la carte stationnaire. Les autres coefficients de la forme non-IBP complète multiplient `dLg,dSg,dtg,dLf,dSf,dtf` et s'annulent sur cette tranche Dirichlet. **Donc `dTheta_D=dP∧dZ` exactement.** Sur toute sous-variété lisse de cette tranche, la forme est fermée ssi le rang différentiel de `(P,Z)` y est <=1. En particulier, sur `Z=F(P)` elle admet la primitive `C−∫F(P)dP` (locale ; explicite pour F polynomiale). Le secteur IBP `P dZ` de b3c3d1 et la forme non-IBP restreinte diffèrent d'une forme exacte : `Theta_D−P dZ=d(C−PZ)`.

Sur les deux jets libres `(pLg,pLg')`, `dTheta_D = −a Lg K²/(D²+K²)^(3/2) dpLg∧dpLg'`. Le témoin rationnel hors Step55 donne `−32/375`, donc l'espace Dirichlet **sans restriction supplémentaire** n'est pas isotrope. À l'inverse, une condition de graphe `Z=F(P)` peut rendre cette tranche isotrope et fournir un contreterme local ; elle n'est pas pour autant physiquement admissible.

## Limite démontrée du critère

Les multiplicateurs sont fixés. Si l'on autorise les variations de lapse, le coefficient de `dN∧dSg'` dans `dTheta` est `2 Mg2 Sg/Lg`, strictement positif sur les données positives, et vaut `2` pour `Mg2=Sg=Lg=1`. Ce terme subsiste même dans une direction où `dP∧dZ=0`. Les lapses ne sont pas des paires canoniques : cela **n'est pas** une obstruction physique ni un résultat sur le quotient de jauge temporelle.

Les conditions Dirichlet choisies ne sont pas prouvées compatibles avec les primaires, la secondaire fonctionnelle `C(r)=0`, sa préservation temporelle Step58, la régularité centrale, la conservation des conditions de bord, les charges ou le rang Dirac. Le résultat ne certifie ni la différentiabilité du générateur amélioré sur l'espace physique, ni l'existence d'une solution 4D, ni stabilité ou observables. Les cartes `K=0/J=0` sont exclues.

## Reproductibilité et suite

`python -m numerics.hr_step68ad_b3c3d2_full_dirichlet_boundary` : **29 résidus symboliques exacts nuls, 2 témoins rationnels PASS** ; `python -m unittest -v tests.test_hr_step68ad_b3c3d2_full_dirichlet_boundary` : **4 cas PASS**, rejouant les mêmes identités, 0 échec final. Un premier test attendait par erreur 28 au lieu de 29 résidus ; correction du compteur puis rejeu réussi. Aucun test d'import des moteurs originaux n'est revendiqué.

**Prochaine étape b3c3d3 :** rejeu authentique Step45/55/58+b3c2 en clone si possible ; calculer les variations tangentes aux primaires, secondaire, opérateur temporel et conditions aux bords sur Step55 ; tester les graphes `Z=F(P)` sur ce sous-espace, puis générateurs améliorés/charges, quotient temporel, Dirac six couples/rang/tertiaires, `K=0/J=0`, 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
