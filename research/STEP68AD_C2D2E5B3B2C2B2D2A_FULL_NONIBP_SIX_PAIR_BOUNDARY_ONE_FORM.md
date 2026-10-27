# JANUS — 68ad-C2d2e5b3b2c2b2d2a : forme de bord totale du Hamiltonien radial original non-IBP

27 octobre 2026. **Résultat symbolique exact sur l'espace ambiant des champs, et non validation de JANUS. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance

Sources originales relues directement sur la branche de recherche et blobs authentifiés : `numerics/hr_step37_original_nonibp_oracle.py` (`005449ade6e3582e3b9a5c3374a881a77e73e3f6`), `numerics/hr_spherical_adm_primary.py` (`c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41`) et `numerics/hr_spherical_mixed_hamiltonian_bracket.py` (`6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81`). L'oracle Step37 n'inclut pas le multiplicateur de shift diagonal commun `V` dans ses deux densités de lapse : il est ajouté depuis le primaire ADM. Les modules originaux ne sont **pas** réexécutés ; le script est une dérivation symbolique indépendante de leurs formules.

## Forme de bord exacte, six couples et shift commun

Poser `Q=N/Lg+M/Lf`, `Dg=pSg*Sg'−Lg*pLg'+pg*tg'`, `Df=pSf*Sf'−Lf*pLf'+pf*tf'`. Le Hamiltonien radial nu avant intégration par parties est la somme des deux courbures ADM non-IBP, des deux cinétiques gravitationnelles, des deux poussières indépendantes, du potentiel HR, de `z Q Dg` et de `V(Dg+Df)`. Pour la variation des champs canoniques à multiplicateurs `N,M,V` fixés, la forme de bord `Theta_R` possède les dix coefficients non nuls possibles suivants :

```
delta Sg' :  2 Mg2 N Sg/Lg
delta Sf' :  2 Mf2 M Sf/Lf
delta Sg  : -2 Mg2 N' Sg/Lg + (z Q+V) pSg
delta Sf  : -2 Mf2 M' Sf/Lf + V pSf
delta Lg  : -2 Mg2 N Sg Sg'/Lg^2
delta Lf  : -2 Mf2 M Sf Sf'/Lf^2
delta pLg : -z (N+M Lg/Lf)-V Lg
delta pLf : -V Lf
delta tg  : pg [N tg'/(Lg^2 sqrt(1+(tg'/Lg)^2))+z Q+V]
delta tf  : pf [M tf'/(Lf^2 sqrt(1+(tf'/Lf)^2))+V]
```

La formule de variation avec dérivées secondes est `Theta_q=(∂F/∂q'−d_r ∂F/∂q'') delta q+(∂F/∂q'')delta q'`. Les moments `pSg,pg,pSf,pf` n'ont pas de dérivée radiale dans la densité originale, donc ne fournissent pas de coefficient de bord indépendant `delta pSg`, `delta pg`, `delta pSf` ou `delta pf`. La contribution du centre régulier doit être contrôlée séparément : les identités ci-dessus valent à chaque extrémité régulière, avec signe opposé à la borne inférieure.

## Réduction algébrique du shift : point critique

La variation de `z` de la densité originale, en incluant la vraie racine HR, est `Q (Dg−K z/sqrt(1−z²))`, `K=m² Mg² Lg Lf At`. Sur la charte régulière `K≠0`, `|z|<1`, l'élimination `z=z*(champs, jets)` annule **point par point** le terme `F_z delta z*` de la variation de la densité originale. Comme la densité originale ne contient pas de `z'`, elle n'introduit pas de terme de bord indépendant `delta z*` : les dix coefficients ci-dessus sont évalués en `z*`.

Mais la différence exacte entre densités originale et IBP est `d_r B`, où `B=2 Mg² N Sg Sg'/Lg+2 Mf² M Sf Sf'/Lf−z pLg(N+M Lg/Lf)`. La variation `delta B` contient **nécessairement** `−pLg(N+M Lg/Lf) delta z*`. La forme de bord de la densité IBP, si `z` est traité comme champ auxiliaire, contient `+pLg(N+M Lg/Lf) delta z` provenant de `z'`. Les **onze** identités exactes `Theta_original−Theta_IBP=delta B` ont été vérifiées symboliquement (dont celle de `delta z`). Supprimer `delta z*` dans `delta B` sans conserver le terme IBP correspondant est donc incorrect. Cette égalité des formes de bord ne sélectionne pas de contreterme physique.

## Conséquence et limites

Avec conditions de Dirichlet uniquement sur les six coordonnées canoniques `(Lg,Sg,tg,Lf,Sf,tf)` au bord, `delta Sg'=1` ou `delta Sf'=1` peut rester autorisé dans l'espace **ambiant** des variations lisses. Pour `Mg²,Mf²,N,M,Sg,Sf,Lg,Lf>0`, les coefficients `2 Mg² N Sg/Lg` et `2 Mf² M Sf/Lf` sont strictement positifs : le Hamiltonien radial **nu** original non-IBP n'est pas fonctionnellement différentiable sur cet espace de variations Dirichlet non compactes sans restriction additionnelle ou contreterme. Témoin rationnel hors coquille : `N=M=1,V=0,z=4/5,Lg=2,Lf=3,Sg=5,Sf=7,Mg²=2,Mf²=3` donne les coefficients `10`, `14`, `−4/3` pour `delta Sg'`, `delta Sf'`, `delta pLg`. Ce témoin n'est pas une solution Step55. Il n'exclut ni des conditions mixtes, ni des contretermes, ni une restriction aux variations tangentes à la surface de contraintes.

**Non démontré :** différentiabilité du Hamiltonien amélioré, conditions aux limites physiques, compatibilité des variations avec les contraintes complètes, Poisson/Dirac sur six couples et rang, contraintes tertiaires, lapses globaux, chartes `K=0/J=0`, dynamique 4D, stabilité, observables.

## Exécution

`python numerics/hr_step68ad_c2d2e5b3b2c2b2d2_boundary_one_form.py` : **27 assertions exactes SymPy/rationnelles PASS, 0 FAIL** (10 coefficients, 1 factorisation de shift, 1 dérivée de B en z, 3 témoins rationnels, 11 identités originale−IBP, 1 dérivée du potentiel HR). `python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c2b2d2_boundary_one_form.py' -v` : **1 cas unittest PASS, 0 FAIL**, qui exécute le script. Ce sont les mêmes 27 assertions dans le cas unittest, pas 54 tests indépendants.

**Prochaine étape :** sélectionner des conditions de bord/contretermes et calculer les gradients fonctionnels complets du Hamiltonien amélioré, puis la matrice de Dirac sur les six couples et les contraintes tertiaires, en gardant les chartes singulières et les contraintes 4D ouvertes.
