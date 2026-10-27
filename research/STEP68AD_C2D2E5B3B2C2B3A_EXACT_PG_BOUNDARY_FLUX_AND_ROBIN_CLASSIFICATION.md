# JANUS — 68ad-C2d2e5b3b2c2b3a : trace de bord et variation non-IBP sur le tube spatial Pg

27 octobre 2026. **Résultat exact limité à la famille Step55/68o à géométrie et shift fixés, et à des lapses fixés à la variation. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources et portée

Sources originales relues via connecteur GitHub : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, oracle original non-IBP Step37 `005449ade6e3582e3b9a5c3374a881a77e73e3f6`. Identité de bord originale–IBP déjà dérivée dans `research/STEP68AD_C2D2E5A_ORIGINAL_NONIBP_BOUNDARY_DIFFERENTIABILITY_AUDIT.md`. Les moteurs physiques originaux **ne sont pas réexécutés dans cette étape** ; on applique une identité de bord exacte à la famille spatiale précédemment certifiée `|lambda|<=1/5000` (étape b2).

## Théorème de trace exact

Pour `r=R=17/20`, `s=r²`, `Lg=a(1+cg*s)²`, `Lf=b(1+cf*s)²`, `z=r*z1`, `pLg=r²(Pg+lambda)(1+5*cg*s/2)`, les coordonnées géométriques et les potentiels de poussière étant indépendants de lambda :

- `partial_lambda pLg(R)=92730563/128000000` ; `partial_lambda pLg'(R)=2734739/1600000` ; `partial_lambda U(0)=274023815147385251710689588080861/40000000000000000000000000000000000`.
- `z(R)=17/5000`, `Lg(R)/Lf(R)=2505421686285156250000000000/1444418923561876775155324829` ; tous deux strictement positifs.
- L'identité de bord pour le Hamiltonien original non intégré par parties est `H_original-H_IBP=[B]_0^R`, `B=2Mg² N Sg Sg'/Lg+2Mf² M Sf Sf'/Lf-z pLg (N+M Lg/Lf)`.
- Pour N et M **fixés pendant la variation**, `partial_lambda B(R)=-z(R)*partial_lambda pLg(R)*(N(R)+M(R)*Lg(R)/Lf(R))`. Au centre `B(0)=0` pour des lapses bornés et la charte régulière. Pour N=M=1 : `partial_lambda [B]_0^R=-6226606039693438177138189375297828359/924428111079601136099407890560000000000` ≈ -0.006735630348174554. **Non nul et strictement négatif**. Cette différence d'actions change donc le long d'une direction de données spatiales contraintes, même si les coordonnées géométriques sont fixes.

En particulier, imposer seulement Dirichlet sur les coordonnées géométriques et de poussière **n'annule pas** le terme `-z(N+M Lg/Lf)delta pLg` de la variation originale pour des lapses positifs non compacts. Une fonctionnelle différentiable nécessite des conditions supplémentaires (fixer cette variation de moment, imposer lapses nuls au bord, ou contreterme adapté), avec examen de tous les autres termes de bord. **Aucune condition physique définitive n'est sélectionnée ici.** Si N et M varient avec lambda, la formule ci-dessus n'est pas la variation totale : les termes `delta N,delta M` doivent être ajoutés.

## Classification exacte des traces mixtes

Pour la condition linéaire `alpha*pLg(R)+beta*pLg'(R)=const` avec coefficients fixes, la famille ne permet un `lambda !=0` que si `alpha*a+beta*d=0`. Si `alpha=1`, la seule pente exceptionnelle est `beta=-5454739/12869360`. Toute autre condition Robin de cette forme supprime cette direction uniparamétrique. Cette observation ne prouve pas l'inexistence d'autres variations compensatrices.

## Tests et limites

Le script `scripts/hr_step68ad_c2d2e5b3b2c2b3a_nonibp_boundary.cjs` et son wrapper `tests/test_hr_step68ad_c2d2e5b3b2c2b3a_nonibp_boundary.cjs` ont été exécutés dans V8 : **25 assertions BigInt exactes PASS, 0 FAIL**. Les tests incluent les coefficients rationnels, les deux lapses, les différences finies exactes sur quatre valeurs de lambda, le produit original–IBP, le centre et la condition Robin. Certificat machine `research/reports/gate2b-step68ad-C2d2e5b3b2c2b3a-nonibp-boundary.json`. Aucune exécution Node ni du moteur Python physique complet n'est revendiquée dans cette étape.

**Non prouvé :** choix des conditions aux limites physiques, carte des traces du secteur f au bord, tangence aux contraintes temporelles, rang de Dirac, tertiaires, lapses, K=0/J=0, dynamique 4D, stabilité et observables. Les résultats précédents sur le tube spatial restent valables sous leurs hypothèses.

**Prochaine étape 68ad-C2d2e5b3b2c2b3b :** caractériser les conditions de bord réellement compatibles avec les variations canoniques (et les contretermes), calculer la sensibilité du secteur f à R sur le tube authentique, puis engager l'oracle fonctionnel non-IBP six couples.
