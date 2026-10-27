# JANUS — 68ad-C2d2e5b3b2c2b3c2b2a : régularisation exacte de la sensibilité au centre (résultat conditionnel)

**27 octobre 2026. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Cette étape ne calcule pas les dérivées du véritable moteur physique sur le domaine radial et ne donne pas v(R). Elle fournit un outil analytique vérifié pour préparer une intégration rigoureuse sans mode singulier.

## Hypothèses et identité héritée

La source originale Step55 `numerics/hr_step55_normalized_secondary.py` (blob `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`) et la certification b2 antérieure donnent au centre, sur la charte analytique, `G(0,U,P)=3*Mf2*b*(P/a-2*z1)-U`. L'identité centrale a été authentifiée lors de b2, **pas réexécutée dans cette session**. Pour `v=partial_P U`, `2s*v_s=(G_U-2)*v+G_P`, donc `G_U(0)=-1`, `G_P(0)=3*v0`, et la solution analytique impose `v0=Mf2*b/a=274023815147385251710689588080861/40000000000000000000000000000000000>0`.

## Nouveau lemme de récurrence (exact, conditionnel)

Si le véritable G est analytique près de la solution centrale et `A(s)=G_U(s,U(s),P)-2=-3+sum_{k>=1}a_k*s^k`, `B(s)=G_P(s,U(s),P)=3*v0+sum_{k>=1}b_k*s^k`, alors l'unique sensibilité analytique bornée s'écrit `v(s)=sum_{n>=0}v_n*s^n` avec

`(2n+3)*v_n=b_n+sum_{k=1}^n a_k*v_{n-k}` pour tout `n>=1` ; en particulier `v1=(a1*v0+b1)/5`. Le mode homogène `s^(-3/2)` est exclu par la régularité centrale. Les coefficients a_k,b_k **physiques** ne sont pas encore calculés. Le test polynomial utilise seulement un moteur **synthétique** A=-3+s/10 et B=3*v0+s/100.

## Nouveau critère de continuation quantitative (conditionnel)

Si, pour tout `s in [0,S]`, `|G_U+1|<=alpha*s`, `|G_P-3*v0|<=beta*s` avec `alpha,beta>=0`, alors, en posant `w=v-v0`, un facteur intégrant de l'EDO donne

`|w(s)| <= (alpha*|v0|+beta)*s*exp(alpha*s/2)/5`.

Si `alpha*S/2<1`, `exp(x)<=1/(1-x)` fournit la majoration entièrement rationnelle `|v(s)-v0| <= (alpha*|v0|+beta)*S/[5*(1-alpha*S/2)]`. Si ce majorant est inférieur à v0, alors v reste strictement positive sur le segment. Le programme calcule ce test pour alpha=1/10 et beta=1/100 **à titre synthétique seulement** : aucune de ces deux bornes n'est démontrée pour le G original. Ce critère est une condition suffisante, pas une estimation physique.

## Vérifications et portée

47 assertions rationnelles BigInt exécutées dans V8, zéro échec, dont 11 résidus polynomiaux, la récurrence, la donnée centrale et des cas adversariaux. Les tests ne remplacent pas l'exécution des modules physiques originaux. Fichiers : `scripts/hr_step68ad_c2d2e5b3b2c2b3c2b2a_variational_regularization.cjs`, `tests/test_hr_step68ad_c2d2e5b3b2c2b3c2b2a_variational_regularization.cjs`, `research/reports/gate2b-step68ad-C2d2e5b3b2c2b3c2b2a-regular-variation.json`.

**Verrou effectif inchangé :** exécuter le vrai `G_U,G_Pg` Step45/46/55, certifier alpha/beta ou des bornes d'intervalles équivalentes, propager v jusqu'à R, puis dériver les traces f et étudier bords, contretermes et oracle Dirac non-IBP six couples. Aucune preuve de conditions aux bords, lapses, rang Dirac, tertiaires, K=0/J=0, 4D, stabilité ou observables.
