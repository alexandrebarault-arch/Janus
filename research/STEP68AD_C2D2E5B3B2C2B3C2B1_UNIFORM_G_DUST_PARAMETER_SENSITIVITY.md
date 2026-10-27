# JANUS — 68ad-C2d2e5b3b2c2b3c2b1 : sensibilité de la poussière g, certification exacte

27 octobre 2026. Résultat **partiel** ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.

## Identité analytique

Reconstruction g originale de `numerics/hr_step55_global_barrier.py` (SHA blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`), avec s=r², P=Pg+lambda, h=1+(5/2)cg s, j=1+5cg s, Lg=a(1+cg s)², Sgr=a(1+cg s)(1+5cg s) :

`rho_g=-(a2 P²+a1 P+a0)/(b0+dP)`, avec `a2=h²/(4Mg2 Lg)-h*j/(Mg2 Sgr)`, `a1=-h*s*Dbar/(2Mg2 Lg Sgr)`, `a0=-Mg2 Lg³ Rg/2+s*z1*Dbar/Lg+Wgbar`, `b0=sqrt(1+kg²s)`, `d=s*h*kg/(2Mg2 Sgr)`. Tous les termes géométriques et de potentiel sont indépendants de P. Cette identité est obtenue par expansion algébrique de la reconstruction g originale, sans recours à une différence finie.

Les dérivées exactes à géométrie/shift fixés sont :

`partial_lambda rho_g=-[(2a2 P+a1)(b0+dP)-(a2 P²+a1 P+a0)d]/(b0+dP)²` ;

`partial_lambda² rho_g=-2(a2 b0²-a1 b0 d+a0 d²)/(b0+dP)³`.

## Certificat continu

Sur `s in [0,289/400]`, `|lambda|<=1/5000`, 256 cellules jointives, arithmétique BigInt à intervalles sortants (maille 10^-28), en évaluant les racines carrées par isqrt avec arrondi dirigé, les bornes strictes sont :

**-2.88 < partial_lambda rho_g < -2.85 ; 3.74 < partial_lambda² rho_g < 3.77 ; 0.88 < rho_g < 0.90 ; b0+dP > 0.999.**

Le certificat JSON donne les bornes rationnelles non arrondies. 512 cellules confirment les signes. Les résultats sont uniformes, pas une simple grille de valeurs. Au centre s=0, a1=d=0, a2=-3/(4 Mg2 a), d'où `partial_lambda rho_g(0)=3P/(2Mg2 a)<0` et `partial_lambda² rho_g(0)=3/(2Mg2 a)>0`.

## Reproductibilité et limites

`node tests/test_hr_step68ad_c2d2e5b3b2c2b3c2b1_gdust_sensitivity.cjs` ; **1551 assertions V8 PASS, 0 FAIL** avant publication, incluant 256 cellules x six inégalités, centre et contre-vérification à 512 cellules. Source et tests doivent être relus après écriture et réexécutés depuis les octets publiés.

Ce calcul n'exécute PAS les moteurs Python originaux, mais transcrit indépendamment la reconstruction g Step55 authentifiée. Ce n'est PAS `G_U` ou `G_Pg` de l'EDO secondaire du secteur f. Il ne donne ni v(R), ni dérivées des traces f, ni conditions aux limites physiques, ni matrice Dirac. Les résultats antérieurs du tube f/g restent la base de la continuation spatiale, et ne sont pas remplacés par ce calcul.

**Prochaine étape effective : 68ad-C2d2e5b3b2c2b3c2b2** — différencier le véritable G Step45/46/55, certifier la sensibilité v jusqu'au bord, calculer les traces f, puis bords et oracle Dirac non-IBP six couples.
