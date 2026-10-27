# JANUS — 68ad-C2d2e5b3b2c2b2d2b : courbure exacte de la forme de bord après réduction HR

27 octobre 2026. **Théorème sur les jets de bord ambiants, pas sur les variations tangentes aux contraintes. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance et domaine

Les trois sources originales sont relues sur la branche de recherche et authentifiées par leurs SHA Git : `numerics/hr_step37_original_nonibp_oracle.py` (`005449ade6e3582e3b9a5c3374a881a77e73e3f6`), `numerics/hr_spherical_adm_primary.py` (`c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41`) et `numerics/hr_spherical_mixed_hamiltonian_bracket.py` (`6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81`). Leurs moteurs Python n'ont pas été réexécutés dans cette étape. Le calcul indépendant ci-joint utilise la forme de bord originale d2a, les six couples et la véritable équation du shift `D-K z/sqrt(1-z²)=0`.

Fixer les six **coordonnées** `Lg,Sg,tg,Lf,Sf,tf` au bord, ainsi que les multiplicateurs `N,M,V`, mais autoriser les variations ambiantes indépendantes des jets canoniques. Sur la charte régulière `K=m² Mg² Lg Lf At>0`, poser `D=pSg*Sg'−Lg*pLg'+pg*tg'`, `z*=D/sqrt(K²+D²)`, `A=N+M Lg/Lf`. Les coefficients du secteur g/f de la forme de bord originale donnent exactement

```
Theta_D = (2 Mg² N Sg/Lg) dSg' + (2 Mf² M Sf/Lf) dSf'
          - (A z* + V Lg) dpLg - V Lf dpLf.
```

Il n'y a **aucun** coefficient de `dpLg'` ou `dpSg` dans cette forme de bord réduite. Cela découle du théorème de l'enveloppe à `F_z=0` et n'implique pas que `z*` soit indépendant des jets.

## Résultat exact : défaut d'intégrabilité

Sur l'espace des jets ambiants, avec les autres données fixées, l'extérieur différentiel vérifie

```
dTheta_D(∂pLg', ∂pLg) = A Lg K²/(K²+D²)^(3/2) > 0
dTheta_D(∂pSg,  ∂pLg) = -A Sg' K²/(K²+D²)^(3/2).
```

La première identité est strictement positive dès que `N,M,Lg,Lf,K>0`, **même si Sg'=0**. Puisque `d²C=0`, il est impossible de trouver une fonction scalaire locale différentiable `C` telle que `dC=-Theta_D` sur un ouvert de jets de bord Dirichlet qui autorise simultanément `δpLg` et `δpLg'` indépendants. Le résultat est plus fort que le seul constat de flux non nul pour le Hamiltonien nu : il exclut un contreterme scalaire sur **cet espace ambiant précis**, sans exclure d'autres espaces de variations.

Témoin rationnel hors coquille : `Lg=2,Lf=3,N=M=1,V=0,K=3,pSg=4,Sg'=1,pLg'=0,pg=1,tg'=0,pLg=2` donne `D=4,z*=4/5`, `dTheta_D(∂pLg',∂pLg)=6/25` et `dTheta_D(∂pSg,∂pLg)=-3/25`. Ce témoin **n'est pas** une solution physique Step55.

## Polarisations restreintes constructives (conditionnelles)

Pour les six coordonnées et `N,M,V` fixés, en imposant aussi `δpLg=0`, la forme de bord restreinte admet la primitive opposée

```
C_1 = -2 Mg² N Sg Sg'/Lg - 2 Mf² M Sf Sf'/Lf + V Lf pLf.
```

Si, à la place, on impose `δz*=0` comme condition de bord, une primitive opposée sur cette sous-variété est

```
C_2 = -2 Mg² N Sg Sg'/Lg - 2 Mf² M Sf Sf'/Lf
      + (A z* + V Lg) pLg + V Lf pLf.
```

Si `z*` varie librement, `dC_2` comporte le terme supplémentaire `A pLg dz*`, non présent dans `-Theta_D`. Au témoin ci-dessus, `A pLg ∂pSg z*=6/25`. Les variations indépendantes des lapses produisent également des termes supplémentaires ; aucune condition physique sur les lapses n'est déterminée ici. Ces deux polarisations sont **algébriquement cohérentes sur des sous-espaces déclarés**, sans preuve de compatibilité avec toutes les contraintes de Dirac, la dynamique ou les bords physiques.

## Tests et limites

Commande : `python numerics/hr_step68ad_c2d2e5b3b2c2b2d2b_boundary_curvature.py` — **21 assertions SymPy exactes PASS, 0 FAIL** (dérivées du shift, deux composantes de courbure, témoin rationnel, contrôle Sg'=0, deux primitives restreintes, sensibilité aux lapses). Commande : `python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c2b2d2b_boundary_curvature.py' -v` — **1 cas PASS**, rejouant les mêmes 21 assertions, non indépendant. Code et test comparés octet pour octet aux blobs GitHub publiés.

**Non démontré :** aucune classification physique globale des conditions de bord, aucune variation tangente aux contraintes complètes, aucun oracle non-IBP de Poisson/Dirac à six couples avec rang et tertiaires, aucune résolution des lapses ni chartes `K=0/J=0`, aucune dynamique 4D, stabilité ou observable cosmologique. **Prochaine étape :** calculer le pullback de `Theta_D` sur les variations tangentes aux contraintes et tester si la courbure s'y annule ; ensuite construire les gradients fonctionnels améliorés et l'algèbre Dirac complète.
