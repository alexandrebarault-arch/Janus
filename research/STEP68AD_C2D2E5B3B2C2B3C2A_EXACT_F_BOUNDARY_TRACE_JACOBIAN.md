# JANUS — 68ad-C2d2e5b3b2c2b3c2a : jacobien exact des traces f au bord

**27 octobre 2026. Résultat exact sur la reconstruction primaire f originale Step46, à géométrie et shift fixes.** Ce calcul ne résout pas l'équation variationnelle Step55 et ne certifie pas v(R). **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Identités et hypothèses

Source : `numerics/hr_step46_exact_secondary_ode.py`, blob Git `bac025c28dbe1561c0c36c56dbfda46dc326f804`. À `s=r²`, `pLf=s U`, `pLf'=r V`, `pf=s rho`, la primaire f reconstruite est `rho=-A/D`, avec :

`D=beta_f+kf*s*U/(2*Mf2*Sfr)`,

`A=U²/(4*Mf2*Lf)-U*(V-s*Dbar/Lf)/(2*Mf2*Sfr)-Mf2*Lf³*Rf/2+s*z1*Dbar/Lf+Wfbar`.

La contrainte radiale reconstruite impose `pSf=(-r³*Dbar+Lf*r*V-pf*r*kf*Lf)/Sfr`. Les paramètres géométriques `Lf,Sfr,Dbar,Wfbar,Rf,z1,kf` restent fixes durant la variation.

À `R=17/20`, définir `H=-(A_U+rho*D_U)/D` et `chi=R*U/(2*Mf2*Sfr*D)`, où `A_U=U/(2*Mf2*Lf)-(V-s*Dbar/Lf)/(2*Mf2*Sfr)`, `D_U=kf*s/(2*Mf2*Sfr)`. Alors, pour toutes variations de U et V :

**`delta pf = H*delta pLf + chi*delta pLf'`**,

**`delta pSf = (Lf/Sfr)*delta pLf'-(R*kf*Lf/Sfr)*delta pf`**.

Ces deux relations sont des identités différentielles algébriques des reconstructions primaires, pas des contraintes temporelles Dirac. Le jacobien formel `(delta U,delta V) -> (delta pLf,delta pLf',delta pSf,delta pf)` est de rang **exactement 2** puisque ses deux premières lignes valent `diag(R²,R)` avec R>0. Le rang de la vraie famille à un paramètre est au plus 1 et demeure inconnu faute de `v(R)`.

## Borne rationnelle exacte sur chi

Le certificat spatial authentique b2 (blob `012e70e49b41cc3180da423c3962d279e3909a26`) encadre U sur tout `|lambda|<=1/5000`. Les constantes physiques Step55 donnent `Mf2=(0.10879548725)²`, `kf=-0.0016`, `Sfr=b(1+cf*s)(1+5cf*s)>0`, `cf=-0.0012`, `b=0.4*0.5787707228025044`.

En utilisant `1<=sqrt(1+kf²*s)<=1+kf²*s/2` et `kf*U>0`, l'algorithme encadre D par des fractions rationnelles exactes et démontre, uniformément :

**`-21/25 < chi < -71/100`**, soit `-0,84<chi<-0,71`.

Les fractions non arrondies de D et chi figurent dans le certificat JSON. Le coefficient chi de bord **n'est pas le J temporel** du problème Dirac. Cette borne dépend du certificat b2 ; les moteurs physiques originaux ne sont pas réexécutés dans cette étape.

## Tests et limites

`node tests/test_hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs` : **24 assertions rationnelles BigInt PASS, 0 FAIL**. Dix identités sur cinq directions vérifiées par nombres duaux rationnels, plus signes, ordre des fractions et garde-fous. Les données des tests de dérivées sont synthétiques ; la borne chi utilise les vraies constantes Step55 et les fractions b2.

**Non prouvé :** `G_U`, `G_Pg` du moteur physique, `v(R)`, `V_lambda(R)`, signes des dérivées des traces f pour la famille réelle, conditions aux bords, contretermes, rang Dirac, tertiaires, lapses, K=0/J=0, 4D, stabilité et observables.

**Prochaine étape 68ad-C2d2e5b3b2c2b3c2b :** différencier le véritable G Step45/46/55 par AD d'intervalles ou symboliquement, certifier l'EDO variationnelle jusqu'à R, insérer `delta U=v(R)`, `delta V=G_U*v+G_Pg` dans ces identités, puis auditer les bords et l'oracle Dirac non-IBP six couples.
