# JANUS — 68ad-C2d2e5b3b2c2b2d2d1 : tiré-en-arrière spatial Step55 et courbures mixtes des multiplicateurs

27 octobre 2026. **Résultat exact/encadré sur une famille spatiale authentique, mais NON sur la surface complète de Dirac. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Question et sources

Après le témoin d2c à interaction artificielle, la question pertinente est la portée de la courbure de bord sur la famille **physique Step55/68o**, qui satisfait la secondaire radiale C(r)=0 sous les hypothèses Step49 et les certificats b2/b2b. Les sources physiques originales relues et leurs SHA sont : Step37 `005449ade6e3582e3b9a5c3374a881a77e73e3f6`, Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. La borne physique de la trace f est héritée du certificat `b53eb93c48fba7099ae2d3275ec4eb5e0464a7a4`. Aucun moteur Python physique original n'a été réexécuté ici.

## Théorème de tiré-en-arrière

Au bord R=17/20, à géométrie et shift HR z fixés, le terme de bord du Hamiltonien **original non-IBP** est, selon la forme exacte d2a,

`Theta_D=(2Mg² N Sg/Lg)dSg'+(2Mf² M Sf/Lf)dSf' -[z(N+M Lg/Lf)+V Lg]dpLg -V Lf dpLf`.

Sur la famille spatiale Step55, les coordonnées, Sg',Sf',z sont fixes, tandis que `a=dpLg/dlambda=92730563/128000000>0` et `b(lambda)=dpLf/dlambda` est strictement encadré par `196809/40000000 < b < 199121/40000000`. Écrire `q=Lg/Lf>0`. Pour les multiplicateurs de bord N,M,V indépendants,

`i*Theta_D=F(lambda,N,M,V) d(lambda)`,
`F=-z*a*(N+q*M)-V*(Lg*a+Lf*b(lambda))`.

**À N,M,V fixés, le tiré-en-arrière de dTheta sur la famille spatiale unidimensionnelle est identiquement NUL par dimension.** Cela ne prouve pas que Theta soit exacte sur un espace canonique plus grand ; cela interdit de transporter automatiquement l'obstruction ambiante d2b/d2c à la seule direction physique lambda.

Sur l'espace étendu (lambda,N,M,V), en revanche,

`d(i*Theta_D)=(-z*a)dN∧d(lambda)+(-z*q*a)dM∧d(lambda)-[Lg*a+Lf*b(lambda)]dV∧d(lambda)`.

Les trois coefficients sont **strictement négatifs** pour les données Step55 et le tube certifié. Les deux premiers sont des fractions rationnelles exactes ; le troisième appartient à l'intervalle rationnel dirigé consigné dans le JSON. La composante dV, absente de la différence original−IBP, est un apport propre à la forme de bord du Hamiltonien original avec shift diagonal.

La non-fermeture sur l'espace **étendu des multiplicateurs** exclut une primitive scalaire sur cet espace ouvert avec variations indépendantes, mais **ne démontre aucune obstruction physique** : N,M,V sont des multiplicateurs, pas des paires canoniques, et leurs variations admissibles, les conditions aux limites et la préservation temporelle ne sont pas fixées. Le signe des courbures mixtes ne donne aucun rang de Dirac.

## Reproductibilité

Programme `scripts/hr_step68ad_c2d2e5b3b2c2b2d2d1_step55_multiplier_curvature.cjs`, wrapper `tests/test_hr_step68ad_c2d2e5b3b2c2b2d2d1_step55_multiplier_curvature.cjs`, certificat `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d2d1-step55-multiplier-curvature.json`. Exécution réelle du corps du programme dans V8 : **35 assertions rationnelles BigInt PASS, 0 FAIL**. Le wrapper est exécuté avec le même module et vérifie quatre invariants (rejeu non indépendant). Tests : paramètres Step55 et ratio exact, coefficients de courbure, positivité, encadrement f et différences finies algébriques de trois multiplicateurs. Le b médian n'est qu'un **point de contrôle algébrique**, jamais une prétendue valeur physique de b(lambda).

## Prochaine difficulté

Construire **au moins deux directions canoniques réellement indépendantes** satisfaisant la secondaire fonctionnelle C(r)=0, les primaires, la régularité et la préservation temporelle, puis calculer leur couplage par dTheta. Les variations des multiplicateurs doivent être traitées séparément. Définir des conditions aux bords et contretermes physiques, puis seulement oracle non-IBP six couples, rang Dirac, tertiaires, K=0/J=0, dynamique 4D, stabilité et observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
