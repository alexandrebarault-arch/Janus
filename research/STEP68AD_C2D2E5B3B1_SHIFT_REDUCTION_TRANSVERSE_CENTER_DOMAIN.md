# JANUS — 68ad-C2d2e5b3b1 : domaine tangent du shift réduit au centre

27 octobre 2026. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Étape **partielle** du chantier 68ad-C2d2e5b3b. Il ne s'agit ni de la matrice fonctionnelle de Poisson/Dirac ni d'une preuve d'obstruction physique.

## Provenance

Formules originales relues sur GitHub : `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` (D=pSg*Sg'-Lg*pLg'+pg*tg', K=m2*Mg2*Lg*Lf*At) ; `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` ; `numerics/hr_step68o_temporal_interval_annulus.py` blob `c99caebc17f243784450ddff94fb061767e6d8e7`. Sources relues et SHA vérifiés ; **modules originaux non réexécutés**. Les identités suivantes sont déduites algébriquement des formules authentifiées, avec des tests rationnels indépendants sur des témoins.

## Calcul exact de la Hessienne

Sur K>0, l'élimination du shift stationnaire dans F(z)=Dz+K sqrt(1-z²) donne F_red(K,D)=sqrt(K²+D²), z*=D/F_red. La Hessienne dans l'ordre (K,D) vaut

`H=1/(K²+D²)^(3/2) * [[D²,-KD],[-KD,K²]]`.

Son déterminant est exactement zéro et sa trace est `1/sqrt(K²+D²)` ; son rang ponctuel est **1** pour (K,D)≠(0,0). **Ceci est le rang de la Hessienne algébrique à deux variables, PAS le rang de Dirac.** Pour une variation (δK,δD), `δ²F_red=(K δD-D δK)²/(K²+D²)^(3/2)≥0` et `δz*=K(K δD-D δK)/(K²+D²)^(3/2)`.

## Variations transverses du chemin Step68o

Poser `K=r²k(r)>0`, `D=r³ k(r) a/w`, `w=sqrt(1-r²a²)>0`, `a=Z1` et `z=ra`. Pour `δK=r² κ` et `δD=r³ d`, on obtient exactement, pour r>0 :

`δz=r*w²/k*(w*d-a*κ)` et `δ²F_red=r⁴*w/k*(w*d-a*κ)²`.

Ainsi, pour k borné inférieurement et κ,d bornés, la variation du shift est O(r), la forme quadratique O(r⁴). C'est une **classe tangentielle suffisante** pour le contrôle central de cette contribution, pas une classification des variations admissibles du système contraint.

## Contre-exemple hors coquille à une linéarisation uniforme naïve

La perturbation canonique formellement lisse `pLg_ε=pLg+ε r²`, toutes les autres variables inchangées, donne `δD/δε=-2r Lg(r)`, `δK/δε=0`. Sur le chemin de référence :

`∂ε z|0=−2 Lg(r) w³/[r k(r)]`.

Comme `Lg(0)=0.4`, `k(0)>0`, cette dérivée diverge en `1/r`. Pour tout ε≠0 fixé, `D_ε=r³ k a/w−2 ε r Lg` et `K=r²k` donnent `z_ε(r)→−sign(ε)` lorsque r→0+, tandis que `z_0(r)→0`. Il n'existe donc pas de continuité uniforme de la carte réduite pour cette famille dans la norme sup sur l'intervalle poncturé jusqu'au centre. **La perturbation est hors coquille et n'est PAS déclarée tangentielle aux contraintes ni admissible aux conditions aux limites physiques.** Le calcul démontre qu'un oracle réduit autorisant sans contrôle toutes les variations `δpLg=εr²` peut perdre sa charte centrale ; il ne réfute pas la formulation non réduite.

## Exécution et limites

Le script BigInt rationnel `scripts/hr_step68ad_c2d2e5b3b1_shift_tangent.cjs` a exécuté **18 assertions exactes PASS, 0 FAIL** dans V8. Témoin rationnel synthétique r=3/4, a=w=4/5, k=2, κ=3, d=5, Lg=2/5 : K=9/8, D=27/32, z=3/5, δz=48/125, δ²F=81/250, ∂εz|0=−512/1875, Hessienne de cette direction=512/3125. Le test de contre-exemple avec a=0, r=1/100000, ε=1/100 donne D/K=−400 et z²>99/100. Les constantes centrales authentiques donnent k(0)>0 par arithmétique rationnelle.

**NON PROUVÉ :** oracle fonctionnel à six couples sur la vraie solution Step55/68o, différentiabilité sur l'espace des variations physiquement admissibles, rang Dirac, contraintes tertiaires, conditions aux bords et lapses, J=0, dynamique 4D, stabilité et observables.

**Prochaine étape effective : 68ad-C2d2e5b3b2**, déterminer les classes de variations canoniques autorisées par la régularité centrale et les contraintes linéarisées, puis exécuter l'oracle fonctionnel original six couples sur coquille avec bords, rang/tertiaires/J=0. Aucun verdict de validation.
