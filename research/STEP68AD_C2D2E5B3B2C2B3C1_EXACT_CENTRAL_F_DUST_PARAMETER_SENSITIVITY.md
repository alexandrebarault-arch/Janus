# JANUS — 68ad-C2d2e5b3b2c2b3c1 : sensibilité physique centrale de la poussière f

27 octobre 2026. **Résultat EXACT au centre, PARTIEL : ni sensibilité au bord R ni oracle Dirac. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Identités physiques et preuve

Sur la branche Step55/68o, avec `a=2/5`, `b=a*y`, `y=0.5787707228025044`, `Mf2=(0.10879548725)^2`, `z1=0.004`, et `Pg(lambda)=Pg0+lambda`, l'EDO Step49/55 donne exactement `U0(lambda)=Mf2*b*(Pg(lambda)/a-2*z1)`, `V0=G(0,U0,Pg)=2*U0`. Donc `v0=dU0/dlambda=Mf2*b/a=274023815147385251710689588080861/40000000000000000000000000000000000>0`, et `dV0/dlambda=2*v0`.

La primaire f **originale Step46**, réécrite en variables normalisées dans l'audit b2, donne au centre (dénominateur f=1 et termes en s nuls) :
`rho_f0 = 3*U0^2/(4*Mf2*b) + Mf2*b^3*Rf0/2 - Wfbar0`.
Ici `Rf0=-48*cf/b^2`, `cf=-0.0012`, `Wfbar0=m2*(b*Tf0+a*T0)`, `T0=beta1*a^2+2*beta2*a*b+beta3*b^2`, `Tf0=beta2*a^2+2*beta3*a*b+beta4*b^2`.
La dépendance à lambda est donc **quadratique exactement** :
`rho_f0(lambda)=rho_f0(0)+(3*U0(0)/(2*a))*lambda+(3*v0^2/(4*Mf2*b))*lambda^2`.
Ainsi `d rho_f0/dlambda=3*U0(lambda)/(2*a)`, strictement négatif pour `|lambda|<=1/5000` ; sa valeur initiale est environ `-0.01969660086285`. La valeur initiale `rho_f0(0)` est environ `0.12427000026205`.

## Certification rationnelle et portée

`Pg0=-2*a^2*sqrt(H2)`, `H2=0.9/(3*a^3)+m2*(3*beta1*y+3*beta2*y^2+beta3*y^3)/3`. Le programme encadre strictement `-0.764<Pg0<-0.763` en **élevant au carré des rationnels** et en conservant la branche négative. Il propage les fractions vers `U0`, `rho_f0` et la dérivée, établissant exactement `-0.020<d rho_f0/dlambda<-0.019` sur l'intervalle de paramètres et `rho_f0(lambda)>0.12`. Il établit également les sensibilités centrales `d(pLf/r^2)/dlambda=v0`, `d(pLf'/r)/dlambda=2*v0`, `d(pSf/r)/dlambda=2*v0` (ce dernier suit de la reconstruction radiale Step46 et de la géométrie fixée).

Les formules ont été confrontées aux sources GitHub originales SHA `bac025c28dbe1561c0c36c56dbfda46dc326f804` (Step46) et `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` (Step55). **Ces moteurs Python originaux n'ont pas été réexécutés ici** : il s'agit d'une dérivation exacte indépendante de leurs identités centrales. Ce résultat n'établit aucune sensibilité `v(R)`, ni `partial_lambda pf(R)`, `partial_lambda pSf(R)`, ni les conditions physiques de bord. La positivité du secteur f sur tout le domaine radial est celle du certificat b2 antérieur, non une nouvelle preuve globale.

## Tests et suite

`node scripts/hr_step68ad_c2d2e5b3b2c2b3c1_center_f_sensitivity.cjs` génère le certificat ; `node tests/test_hr_step68ad_c2d2e5b3b2c2b3c1_center_f_sensitivity.cjs` exécute **20 assertions BigInt PASS, 0 FAIL**. Une première erreur locale de chemin du test a été corrigée avant la campagne finale ; le code publié est celui de la campagne réussie. Les contrôles internes supplémentaires du générateur ne sont pas comptés comme tests distincts.

**Prochaine étape 68ad-C2d2e5b3b2c2b3c2 :** différencier le véritable `G(s,U,Pg)` et certifier l'EDO variationnelle jusqu'à `R=17/20` ; calculer la carte différentielle des quatre traces f ; définir l'espace de bord/lapses et les contretermes ; puis oracle Poisson/Dirac non-IBP six couples, rang/tertiaires, K=0/J=0, 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
