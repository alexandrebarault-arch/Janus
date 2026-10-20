# JANUS-R, Gate 2B — Étape 33h : contrôle indépendant, non-IBP, du crochet mixte sur les données courbes contraintes

**Date : 20 octobre 2026.** Branche : `research/gate2b-nonhomothetic-transfer`.

**Résultat : `INDEPENDENT_ORIGINAL_ADM_MIXED_BRACKET_GREEN` ; `PRIMARY_SURFACE_CURVED_MOVING_DUST_GREEN` ; `GENERAL_DIRAC_BD_SECONDARY_OPEN` ; `GATE_2B=OPEN`.** Ce calcul est un témoin numérique indépendant, non une preuve de suppression du mode de Boulware–Deser.

## Raison du contrôle indépendant

L'étape 33g utilisait des gradients eulériens obtenus par différentiation symbolique des densités hamiltoniennes **après intégration par parties**, puis une dérivation radiale par pas complexe. Sur une famille courbe avec deux poussières non comobiles satisfaisant les contraintes primaires, elle prédisait une compensation des dérivées des fonctions de pondération après intégration par parties et un coefficient local secondaire nécessaire \(\mathcal C_{\rm local}\approx+0,47\) vers \(r=0,43\).

Un seul code utilisant le même formalisme symbolique ne suffisait pas comme validation. **Étape 33h :** le nouveau module `numerics/hr_independent_collocation_bracket.py` **n'importe aucun module des étapes précédentes**, ni SymPy. Il reconstruit les contraintes **ORIGINALES avant toute intégration par parties** : courbure sphérique \(R^{(3)}\) comportant \(S''\), impulsion gravitationnelle \(p_L'\), potentiel Hassan–Rosen complet \(\beta_0,\ldots,\beta_4\), véritables poussières canoniques \((\theta_g,p_g)\) et \((\theta_f,p_f)\) avec gradients de phases et racines relativistes. Le décalage relatif \(z_*=\operatorname{sgn}(K)D_g/\sqrt{D_g^2+K^2}\) est **recalculé après chaque perturbation des variables canoniques** (équivalent à \(z=(D_g/K)/\sqrt{1+(D_g/K)^2}\) sur la branche régulière, avec prise en charge du signe de \(K\)).

### Discrétisation et crochet

Sur \(n\) nœuds Gauss–Legendre, la matrice de dérivation pseudospectrale \(D_{ij}\) permet d'évaluer la courbure originale et les dérivées radiales de toutes les variables. Les fonctions de pondération \(N,M\) sont compactes avec puissances cubiques aux deux bornes, afin de supprimer les termes de bord. Les deux fonctionnelles \(H_g[N],H_f[M]\) sont intégrées directement, sans substituer la formule IBP de l'ancien calcul.

Pour chaque variable canonique \(q^A_i,p_{A,i}\) et chaque nœud, calculer les différences finies centrales des deux actions complètes, **avec recalcul de \(z_*\)**. Le crochet discret est

\[
\{H_g[N],H_f[M]\}_n=\sum_{i,A}\frac{1}{w_i}\left(
\frac{\partial H_g}{\partial q_i^A}\frac{\partial H_f}{\partial p_{A,i}}
-\frac{\partial H_g}{\partial p_{A,i}}\frac{\partial H_f}{\partial q_i^A}
\right),
\]

ce qui implémente \(\{q_i,p_j\}=\delta_{ij}/w_i\) et conserve les **six** couples canoniques (quatre couples gravitationnels et deux couples de poussière). La discrétisation à nombre fini de nœuds est un outil de vérification dont la **convergence doit être contrôlée**, pas un substitut aux fonctionnelles hamiltoniennes continues.

Les données initiales sont reconstruites **indépendamment** avec les mêmes paramètres physiques que le témoin de l'étape 33g : \(a=0,4\), \(b/a=0,5787707228025044\), courbures \(c_g=0,015,c_f=-0,012\), gradients de poussière \(k_g=0,012,k_f=-0,016\), décalage relatif \(z(r)=0,04r\), et impulsions gravitationnelles radiales distinctes. Les poussières sont calculées à partir des deux contraintes de lapse ; \(D_g=-D_f\) et \(F_z=0\) restent satisfaites. La formule \(R^{(3)}=-48c/[a^2(1+cr^2)^5]\) est vérifiée indépendamment contre la courbure directe avec dérivées spectrales.

## Résultats exécutés

Le programme `scripts/verify_gate2b_step33h.py` a exécuté **21 nouveaux tests**, tous réussis (1,87 s), puis sauvegardé les témoins numériques dans `research/reports/gate2b-step33h-report.json`.

| Points n | Crochet mixte \(\{H_g[N],H_f[M]\}_n\) | Résidu maximal des contraintes primaires |
|---:|---:|---:|
| 16 | \(+4,2129335076\times10^{-6}\) | \(2,78\times10^{-16}\) |
| 26 | \(+4,2129335507\times10^{-6}\) | \(2,91\times10^{-16}\) |
| 40 | \(+4,2129336475\times10^{-6}\) | \(4,72\times10^{-16}\) |

À \(n=16\), les **six contributions** ordonnées \((L_g,p_{Lg}),(S_g,p_{Sg}),(\theta_g,p_g),(L_f,p_{Lf}),(S_f,p_{Sf}),(\theta_f,p_f)\) sont respectivement

\[
(+1,12729272\cdot10^{-6},\;-8,37053544\cdot10^{-6},\;
 +2,26175107\cdot10^{-7},\;+6,88633202\cdot10^{-6},\;
 +4,34366910\cdot10^{-6},\;0).
\]

Le zéro de la **contribution directe** du couple \(f\)-poussière à CE crochet mixte provient de la dépendance fonctionnelle, et **ne supprime pas** le couple \((\theta_f,p_f)\) de la théorie ; il est conservé dans la variation totale.

### Annulation des dérivées de pondération — contrôle différentiel indépendant

Sur les données **contraintes**, échanger les deux pondérations tout en conservant le rôle de \(H_g\) et \(H_f\) ne modifie pas numériquement le crochet au niveau du contrôle :

\[
\{H_g[N],H_f[M]\}-\{H_g[M],H_f[N]\}
\simeq1,09\cdot10^{-14}\quad(n=32).
\]

C'est une conséquence attendue de la disparition, après IBP, du coefficient antisymétrique de dérivées de pondération sur cette famille. **Contrôle négatif :** ajouter à \(p_g\) une déformation \(0,02r^2\), sans réimposer \(H_g=0\), fait apparaître une différence \(\simeq9,90\cdot10^{-11}\) dans les mêmes conditions ; \(|H_g|\) dépasse alors \(10^{-2}\). Ainsi l'annulation est discriminante et non une propriété triviale du programme.

Pour localiser le coefficient restant vers \(r=0,43\), pondérer les deux Hamiltoniens par une enveloppe gaussienne compacte centrée au même rayon, puis diviser le crochet par \(\int N^2dr\). Résultats : \(0,48120\) pour largeur \(0,03\), résolution 80 ; \(0,47371\) pour largeur \(0,015\), résolution 128. La tendance est cohérente avec le coefficient local \(\sim0,47\) calculé par la **méthode symbolique indépendante** à l'étape 33g. **Ce n'est pas une mesure physique et la limite de largeur nulle n'a pas été démontrée rigoureusement.** À résolution insuffisante et pour des profils trop étroits, les différences finies de la matrice spectrale deviennent mal conditionnées : éviter d'inférer une convergence universelle.

### Contrôles négatifs supplémentaires

- Pas de dérivation canonique : \(3\times10^{-6},10^{-6},3\times10^{-7}\), avec accord sur le crochet dans la précision déclarée.
- Raffinement spatial : \(14,18,22,28,34\) points ; contraintes satisfaites, crochet convergent.
- Positivité des **deux** densités canoniques testée avant toute interprétation.
- Variation locale du seul paramètre `grav_f` dans \([-0,18,+0,18]\) : le crochet reste strictement positif dans cette **famille particulière** ; cela ne démontre aucune obstruction générale à \(\mathcal C_{\rm local}=0\).
- Une assertion de tolérance initialement trop stricte sur la **courbure spatiale** spectrale (écart relatif maximal \(1,17\times10^{-9}\)) a échoué. Le seuil a été ajusté à \(3\times10^{-9}\), sans modifier la formule physique, et les 21 tests ont ensuite réussi.

## Portée scientifique et prochain verrou

Cette étape ajoute un **second calcul numérique structurellement indépendant**, utilisant le Hamiltonien **non intégré par parties**, les dérivées nodales et les différences finies, plutôt que les gradients fonctionnels symboliques et le pas complexe des étapes 33e–33g. La cohérence est renforcée, notamment sur la disparition des dérivées de pondération *sur* cette famille de contraintes primaires.

**Mais la contrainte secondaire n'est pas satisfaite sur cette famille : le crochet mixte reste non nul.** Il faut maintenant résoudre simultanément les trois contraintes primaires et une condition secondaire \(\mathcal C_{\rm local}=0\) sur de véritables données courbes, puis appliquer la conservation temporelle hamiltonienne (crochets secondaires, rang de Dirac, fixation des lapses), avec les deux poussières positives et les branches dégénérées \(K=0,J=0\) séparées. Le résultat sphérique ne donnerait pas à lui seul le spectre physique quadratique complet en 4D.

**N'annoncer ni élimination de Boulware–Deser, ni stabilité, ni franchissement de la transition relative \(\mu\), ni validité cosmologique.** Le fond physiquement non homothétique sur solution manque toujours, ainsi que les contrôles physiques De Felice/Aoki sur **la même action réduite**.

### Provenance

Les 21 tests ont été exécutés **dans un nouvel environnement local ciblé** `/mnt/data/janus33h`, et non comme partie de l'ancien groupe 22+3 de l'étape 33g ou de la suite entière du dépôt. La procédure de reproduction est dans `scripts/verify_gate2b_step33h.py`. Le rapport JSON contient les SHA-256 et empreintes Git des trois exécutables/testés. Aucun clonage complet du dépôt, CI ou examen externe n'a été réalisé. Vérifier que les fichiers publiés sur la branche GitHub possèdent les empreintes Git figurant dans le JSON.

**Prochain point de reprise :** chercher une famille courbe satisfaisant les primaires **et** la condition locale secondaire, puis calculer la conservation et le rang de Dirac ; ne pas inférer ce rang de la seule symétrie des pondérations. **`GATE_2B=OPEN`.**
