# JANUS — 68ad-C2d2e5b3b2c2b2d1 : compensation exacte du flux de bord par les lapses et classification des contretermes

27 octobre 2026. **Résultat analytique exact sur une sous-famille spatiale seulement ; GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

## Sources authentifiées et périmètre

L'identité originale non-IBP moins IBP provient de Step37 (blob `005449ade6e3582e3b9a5c3374a881a77e73e3f6`), du primaire ADM (blob `c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41`) et du profil Step55 (blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`). Sources relues en direct. Aucun moteur Python original réexécuté dans cette étape. Les bornes physiques de la famille et des poussières demeurent celles des certificats b2/b2b/b2c antérieurs.

## Théorème de compensation sur le tiré-en-arrière au bord

À `R=17/20`, géométrie et shift fixés, `pLg(R)=a(Pg+lambda)`, `a=R²(1+5cg R²/2)>0`, `q=Lg/Lf>0`, `z=R z1>0`. La différence originale–IBP est `[B]_0^R=B(R)`, car le centre régulier a `B(0)=0` pour des lapses bornés. Posons `Ag=2Mg² R Sg'/Lg * Sg` et `Af=2Mf² R Sf'/Lf * Sf`, soit `Ag=2Mg² R Sgr` et `Af=2Mf² R Sfr` sur Step55. Alors exactement

`B(lambda,N,M)=[Ag-z a(Pg+lambda)]N+[Af-z q a(Pg+lambda)]M=Cg(lambda)N+Cf(lambda)M.`

Les dérivées mixtes `B_lambda,N=-za<0`, `B_lambda,M=-zaq<0` interdisent tout contreterme indépendant des lapses (ou indépendant du moment `pLg`) qui annulerait **toutes** les variations de cette différence sur les trois directions indépendantes `(lambda,N,M)`. Inversement, sur ce tiré-en-arrière connexe, la solution générale de `d(B+C)=0` est **exactement** `C=-B+constante`. Cette classification ne porte que sur la différence original–IBP, pas sur la différentiabilité du Hamiltonien total.

**Contre-exemple constructif à une extrapolation abusive de l'obstruction à lapses fixes.** Fixons `M=1` et imposons `B(lambda,N(lambda),1)=B(0,1,1)`. Alors

`N(lambda)=[Cg(0)+z q a lambda]/[Cg(0)-z a lambda]=1+z a(1+q)lambda/[Cg(0)-z a lambda]`,

et `N'(lambda)=z a(1+q)Cg(0)/[Cg(0)-z a lambda]^2>0`. Cette famille préserve exactement le flux `B` tout en gardant **les deux lapses strictement positifs**. Ce n'est ni une équation de lapse dérivée des contraintes temporelles ni une condition de bord physique sélectionnée.

## Certification rationnelle uniforme

Le paramètre central physique Step55 est `Pg=-2 A² sqrt(H2)`, avec `A=2/5`. Le programme calcule `H2` exactement et prouve `5<H2<6`, donc `-4/5<Pg<-16/25`. Sur `|lambda|<=1/5000`, `Pg+lambda<0`, `Cg>Ag>2/3`, `Cf>Af>0`, `0<z<1/250`, `0<a<3/4`, `1<q<2`. Ainsi `|N(lambda)-1|< (9/1000)(1/5000)/(2/3)<1/1000`, ce qui certifie `999/1000<N(lambda)<1001/1000` pour le vrai `Pg` sans arrondir sa racine carrée. Toutes les opérations numériques du certificat sont rationnelles BigInt ; les tests aux bornes sont des contrôles, la preuve uniforme repose sur les inégalités algébriques ci-dessus.

## Interprétation et verrous

Les variations indépendantes de lapses sont des variations de **multiplicateurs**, pas des directions symplectiques canoniques supplémentaires. La co-variation construite conserve seulement `B`, pas l'action totale ni les équations de conservation des contraintes. Ajouter `-B` convertit la fonctionnelle originale en sa représentation IBP sur ce périmètre, mais ne démontre pas que cette dernière est fonctionnellement différentiable pour des variations non compactes : les termes de courbure, les poussières, la variation du shift réduit et tous les six couples doivent encore être traités. Aucun contreterme physique n'est sélectionné. Les conditions aux limites globales, les contraintes tertiaires, le rang Dirac, les chartes `K=0/J=0`, la dynamique 4D, la stabilité et les observables restent ouverts.

**Tests exécutés : 114 assertions exactes BigInt V8 PASS, 0 FAIL** ; source et test `scripts/hr_step68ad_c2d2e5b3b2c2b2d1_boundary_lapse_compensation.cjs`, `tests/test_hr_step68ad_c2d2e5b3b2c2b2d1_boundary_lapse_compensation.cjs`, certificat `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2d1-boundary-lapse-compensation.json`. Prochaine étape : conditions de bord pour la fonctionnelle **totale** (avec variation du shift éliminé), puis véritable oracle non-IBP six couples et analyse Dirac. Ne pas confondre une identité de bord exacte avec une validation de JANUS.
