# JANUS — 68ad-C2d2e5b3b2c2b2d2d2b1 : deux translations canoniques des horloges de poussière

28 octobre 2026. **Résultat exact de symétrie canonique dans le volume, et résultat partiel sur les traces de bord ; PAS deux degrés de liberté physiques de Dirac. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Question scientifique

L'étape d2d2a avait construit deux directions de jauge radiale à traces de bord nulles. Existe-t-il deux directions canoniques à traces indépendantes **modulo les seuls difféomorphismes radiaux diagonaux**, qui soient réellement tangentes aux contraintes fonctionnelles ? La présente étape fournit deux candidats naturels mais montre aussi pourquoi ils ne suffisent **pas** à établir le rang physique recherché.

## Lemme exact : translations constantes des deux horloges

Dans les six couples canoniques de l'action sphérique originale, poser

`X_g: δt_g(r)=1, δt_f(r)=0, δq_{àutres}=0`, et
`X_f: δt_g(r)=0, δt_f(r)=1, δq_{àutres}=0`.

Les densités originales `H_g,H_f,D_g+D_f,F_z`, l'interaction `K`, le shift réduit `z_*=D_g/sqrt(K²+D_g²)` et les deux densités post-IBP Step45 ne dépendent que des dérivées radiales `t'_g,t'_f`, jamais des valeurs `t_g,t_f`. Par conséquent les transformations finies `t_i -> t_i+c_i` les laissent **identiquement** inchangées, sans supposer les primaires satisfaites. Ces transformations sont canoniques, engendrées formellement par `Q_g=∫p_g dr`, `Q_f=∫p_f dr` pour des fonctionnelles et smearings différentiables. L'automorphisme canonique commute avec les crochets de Poisson : **toute contrainte secondaire/tertiaire formée algébriquement par crochets et dérivées radiales des contraintes originales est également invariante dans le volume**. Cela ne calcule ni ces contraintes ni leur rang.

Cette invariance vaut en particulier pour la secondaire fonctionnelle Step45 `C(r)=K00-(K01)'` : si une solution complète existe, ses translations constantes restent solutions des **équations de contraintes dans le volume**. La préservation temporelle est covariante formellement lorsque les multiplicateurs et le domaine fonctionnel sont compatibles. **Aucune solution temporelle complète n'est construite**, et les termes de bord des générateurs restent à traiter.

## Rang des traces modulo jauge radiale, et limite de ce rang

L'application `(X_g,X_f) -> (δt_g(R),δt_f(R))` a pour matrice l'identité 2×2 : rang exact **2**. Les deux directions ne sont pas des difféomorphismes **radiaux** : sur Step55, `S'_g=a(1+c_g s)(1+5c_g s)>0` et `S'_f=b(1+c_f s)(1+5c_f s)>0` pour `0<=s<=289/400`. Une jauge radiale produisant `δS_g=ηS'_g=0` doit avoir `η=0` et ne peut engendrer une translation non nulle de poussière.

**Mais le quotient par la jauge radiale n'est PAS le quotient par toute la jauge de Dirac.** Les translations des horloges peuvent contenir une direction de reparamétrisation temporelle ; elles peuvent aussi être interdites par `t_i(0)=0` ou des conditions de Dirichlet des horloges au bord. Le rang physique modulo **toutes** les contraintes de première classe et les conditions de bord reste **NON CALCULÉ**.

## Forme de bord originale et courbure

Pour le Hamiltonien original non-IBP à six couples, la forme de bord d2a donne les coefficients exacts

`Θ[X_g]=p_g [ N t'_g/(L_g² sqrt(1+(t'_g/L_g)²)) + z_*(N/L_g+M/L_f) + V ]`,

`Θ[X_f]=p_f [ M t'_f/(L_f² sqrt(1+(t'_f/L_f)²)) + V ]`.

Comme **tous** les coefficients de `Θ` sont indépendants des valeurs `t_g,t_f`, on a exactement `dΘ(X_g,X_f)=0`. Le plan est **isotrope** pour cette 2-forme, et non démontré inclus dans son noyau total.

Sur la géométrie Step55, à `R=17/20`, `t'_g=k_g R L_g>0` avec `k_g=0.0012`, `t'_f=k_f R L_f<0` avec `k_f=-0.0016`, et `z_*=0.004 R>0`. Pour `N=M=1,V=0`, la positivité des poussières déjà certifiée antérieurement implique strictement `Θ[X_g]>0` et `Θ[X_f]<0`. **La forme de bord ne s'annule donc pas sur ces deux directions**, bien que leur couplage par `dΘ` soit nul. La variation totale d'un Hamiltonien sous une translation constante peut néanmoins être nulle par compensation entre le terme d'Euler volumique et le terme de bord ; ne pas confondre `Θ[X]≠0` avec `δH[X]≠0`.

## Preuves, contrôles et sources

Programme reproductible `numerics/hr_step68ad_c2d2e5b3b2c2b2d2d2b1_clock_translation.py` : **48 assertions exactes SymPy PASS, zéro FAIL**, exécutées localement. Un `unittest` de rejeu passe (1 test ; mêmes 48 assertions, non indépendant). Vérifications : indépendance explicite des deux valeurs de clocks dans douze expressions originales et de bord, invariance sous dix substitutions finies, dérivées des coefficients de bord, isotropie, rang des traces, signes géométriques Step55.

Sources originales lues et SHA Git authentifiés : `numerics/hr_step37_original_nonibp_oracle.py` `005449ade6e3582e3b9a5c3374a881a77e73e3f6` ; `numerics/hr_step45_exact_physical_ward.py` `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ; `numerics/hr_step58_temporal_operator.py` `802c23aebd41780d8c462f1aa1711707fe4ee88f` ; `numerics/hr_step55_global_barrier.py` `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` ; `numerics/hr_curved_primary_mixed_kernel.py` `45ccd73177cc1588efaf1d53e3dd0179d41ec30b` ; forme de bord d2a `94bd7e089ebb0978569361c03a4f3ab950b950df`. **Les moteurs Python originaux Step45/55/58 n'ont pas été réexécutés ; le script reconstruit indépendamment leurs dépendances pertinentes.**

Le certificat JSON contient les 48 vérifications et les exclusions explicites. Les données Step55 utilisées pour les signes sont des constantes rationnelles exactes ; la positivité des poussières est héritée du certificat antérieur et non recertifiée ici.

## Prochaine étape

**68ad-C2d2e5b3b2c2b2d2d2b2** : classifier les deux charges de translation des horloges face aux contraintes temporelles de Dirac, à leurs générateurs améliorés et aux conditions `t_i(0)`/`t_i(R)`; calculer le rang des traces après quotient par la jauge **temporelle** et par les conditions de bord. Ensuite rechercher deux véritables directions non-jauge admissibles et calculer `i^*dΘ` ; puis conditions physiques de bord/contretermes, oracle non-IBP six couples, rang, tertiaires, lapses, K=0/J=0, dynamique 4D, stabilité et observables.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
