# JANUS Gate 2B — étape 33e : crochet fonctionnel mixte radial des deux contraintes hamiltoniennes

Date : 2026-10-19. Branche : `research/gate2b-nonhomothetic-transfer`.

**Verdict exact :** `SPHERICAL_MIXED_HG_HF_SMEARED_BRACKET=COMPUTED_ON_OFFSHELL_RADIAL_FAMILY`; `RELATIVE_SHIFT_REGULAR_ROOT=ELIMINATED`; **`LOCAL_BD_SECONDARY=NOT_DERIVED`**, **`GATE_2B=OPEN`**. Les 31 tests nouveaux ont été exécutés dans un espace local autonome, **et non** avec les 95 tests historiques de l'étape 33d ni sur un clone complet du dépôt.

## Question et progrès effectif

L'étape 33a a établi une écriture sphérique hamiltonienne du secteur gravitationnel positif Einstein–Hilbert, du potentiel Hassan–Rosen aux cinq coefficients β₀…β₄ et des deux poussières canoniques indépendantes. L'étape 33b a calculé la contrainte secondaire du **modèle homogène**, tandis que les étapes 33c–33d ont testé l'algèbre des transformations spatiales et les contraintes radiales. Aucun de ces résultats n'avait évalué les **dérivées fonctionnelles mixtes** des deux contraintes hamiltoniennes complètes avec les dérivées spatiales de la courbure et des impulsions.

Le nouveau fichier `numerics/hr_spherical_mixed_hamiltonian_bracket.py` calcule

\[
\{H_g[N],H_f[M]\}=\sum_{I=1}^{6}\int_{r_-}^{r_+}\!dr\,
\left(\frac{\delta H_g[N]}{\delta q_I}\frac{\delta H_f[M]}{\delta p_I}
-\frac{\delta H_g[N]}{\delta p_I}\frac{\delta H_f[M]}{\delta q_I}\right)
\]

sur **six couples** indépendants `(L_g,pL_g),(S_g,pS_g),(θ_g,p_g),(L_f,pL_f),(S_f,pS_f),(θ_f,p_f)`. Les fonctions `N(r),M(r)` s'annulent aux deux bornes du domaine radial `[0.1,0.9]`. Les profils polynomiaux sont non homogènes, réguliers et **hors de la surface des contraintes** ; ce sont des témoins d'algèbre, non un fond cosmologique sur solution.

## Identités exactes implémentées

Dans chaque secteur `i=g,f`, avec `L_i>0,S_i>0`, gravitation sphérique positive et unités d'angle solide fixées,

\[
C_i^{EH}=\frac{L_i p_{L_i}^{2}}{4M_i^2 S_i^2}-\frac{p_{L_i}p_{S_i}}{2M_i^2 S_i}
-M_i^2 L_i+M_i^2\frac{S_i'^2}{L_i}
+2M_i^2 S_i\left(\frac{S_i'}{L_i}\right)',
\]

et `C_i^dust=p_i sqrt(1+θ_i'^2/L_i²)`. La contrainte de quantité de mouvement du secteur g est

\[
D_g=p_{S_g}S_g'-L_g p_{L_g}'+p_g\theta_g'.
\]

Après le changement de variable du décalage relatif de Hassan–Rosen, les densités primaires sont

\[
\mathcal H_g=C_g+\frac{zD_g}{L_g}+W_g(z),\qquad
\mathcal H_f=C_f+\frac{zD_g}{L_f}+W_f(z),
\]

avec `C_i=C_i^EH+C_i^dust` et les mêmes coefficients `W_g,W_f` que l'étape 33a. **Attention :** les deux poussières restent présentes ; le fait que `D_g` apparaisse dans *les deux* densités est une conséquence de la redéfinition du décalage, pas une identification des poussières.

Pour l'intégrale compacte, la courbure se réécrit **exactement** par intégration par parties :

\[
\int dr\,N\left[-M_i^2L_i+M_i^2\frac{S_i'^2}{L_i}
+2M_i^2S_i\left(\frac{S_i'}{L_i}\right)'\right]
=\int dr\,\left[-M_i^2NL_i-M_i^2N\frac{S_i'^2}{L_i}
-2M_i^2 N'\frac{S_iS_i'}{L_i}\right].
\]

Le terme `-N z pL_g'` est intégré comme `+(Nz)'pL_g`, et son analogue dans `H_f` comme `+(Mz L_g/L_f)'pL_g`. Ces changements de forme ne sont valables que pour les supports compacts et les hypothèses de bord explicites. Leurs conséquences sont **vérifiées contre l'action originale non intégrée par parties**, avec les vrais `S''`, `L'` et `pL'`.

Les dérivées partielles par rapport aux champs et à leurs premières dérivées radiales sont calculées **symboliquement** avec SymPy, sans supprimer aucune paire. Les dérivées fonctionnelles d'Euler sont ensuite obtenues selon

\[
\delta H/\delta q=\partial F/\partial q
-\frac{d}{dr}(\partial F/\partial q'),
\]

la dernière dérivée radiale étant contrôlée par la méthode complexe à pas infinitésimal appliquée aux profils radiaux analytiques. Le premier essai générant les expressions symboliques entièrement développées a dépassé le délai d'exécution ; la méthode retenue évite cet accroissement d'expressions **sans approcher les dérivées partielles**. Les gradients des **douze champs** et des **deux** contraintes sont comparés à des différences finies indépendantes de l'action originale sur des variations compactes. Des tests supplémentaires vérifient les gradients lorsque le décalage `z` reste un champ externe fixé.

### Traitement exact du décalage relatif

Sur la branche régulière `K≠0` avec

\[
K=m^2 M_g^2 L_gL_f\bigl(\beta_1 S_g^2+2\beta_2 S_gS_f+\beta_3 S_f^2\bigr),
\]

l'équation auxiliaire est `D_g-K z/sqrt(1-z²)=0`. On calcule

\[
u=D_g/K,\quad z_*=u/\sqrt{1+u^2},\quad
z_*'=u'/(1+u^2)^{3/2},\quad
z_*''=u''/(1+u^2)^{3/2}-3u(u')^2/(1+u^2)^{5/2}.
\]

Ces expressions incluent **toutes les dérivées radiales** de la contrainte de quantité de mouvement et de `K`. Pour **chacune** des deux contraintes, `∂H_g/∂z=(D_g-K z/sqrt(1-z²))/L_g` et `∂H_f/∂z=(D_g-K z/sqrt(1-z²))/L_f`. Sur la racine, le théorème de l'enveloppe permet donc d'évaluer les gradients fonctionnels à `z=z_*` sans ajouter de variation canonique supplémentaire de `z_*`; ses dérivées spatiales restent indispensables aux gradients intégrés par parties. Cette démarche n'est **pas** l'analyse de Dirac finale avec les contraintes primaires de la variable auxiliaire et leur conservation ; la branche `K=0` est explicitement exclue du solveur.

## Résultats numériques de contrôle

Avec les paramètres dimensionnels de régression `M_g²=1.7`, `M_f²=0.63`, `m²=0.91`, `β=(0.2,1.3,-0.35,0.4,-0.17)` et deux fonctions de pondération compactes distinctes, quadrature de Gauss–Legendre à 48 points :

| Contribution canonique au crochet | Résultat |
|---|---:|
| `(L_g,pL_g)` | `+1.9582294901110296e-05` |
| `(S_g,pS_g)` | `-1.8544242941402666e-05` |
| `(θ_g,p_g)` | `+2.372118038057092e-08` |
| `(L_f,pL_f)` | `-3.4075573609340606e-08` |
| `(S_f,pS_f)` | `+2.1609387048281924e-07` |
| `(θ_f,p_f)` | `0` (structure de cette paire dans le crochet mixte choisi) |
| **Somme** | **`+1.2437914369616798e-06`** |

Dans ce même témoin arbitraire : `H_g[N]=+0.0010622901711922336`, `H_f[M]=+0.00032012710659204115`, résidu maximal de l'équation algébrique du décalage relatif `4.16e-17`. À `z` externe maintenu sur le profil polynomial de contrôle, le crochet devient `+4.993895796055337e-07` : **garder `z` fixé et le mettre sur sa racine ne sont pas la même opération**. L'inversion des fonctions de pondération entre les deux contraintes change le résultat en `+1.2077059811667116e-06` : il existe des contributions de dérivées radiales du lapse de test, impossibles à obtenir en recopiant uniquement une formule homogène ultralocale.

La contribution directe de la paire `(θ_f,p_f)` au **crochet mixte défini ici** est nulle car `H_g` et `z_*` ne dépendent pas de ces deux variables, mais **la paire demeure présente** dans `H_f` et dans la structure canonique totale. L'annuler dans le compte des degrés de liberté serait une erreur. Sur la limite distincte `m²=0` et `z=0` externe, les deux Hamiltoniens de gravité et poussière se découplent et le crochet mixte est exactement nul ; la racine `z_*` est alors dégénérée et ne doit pas être inventée.

### Véritable erreur détectée puis corrigée

Une première implémentation associait incorrectement `S_g` et `pL_g` (ainsi que `S_f` et `pL_f`) lors de l'extraction de variables symboliques depuis la liste canonique intercalée `(q,p,q,p,...)`. Elle donnait un crochet **faux** d'environ `0.00636`. La comparaison de l'intégrale gravitationnelle **originale** avec son expression intégrée par parties a échoué et permis de corriger la permutation. Le résultat **corrigé et testé** est `1.2437914e-06`. Ce contrôle négatif réel est conservé dans le présent audit pour empêcher sa réapparition.

## Reproduction et périmètre

Nouveaux fichiers :

- `numerics/hr_spherical_mixed_hamiltonian_bracket.py`
- `tests/test_hr_spherical_mixed_hamiltonian_bracket.py`
- `scripts/verify_gate2b_step33e.py`

Commande :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33e.py gate2b-step33e-report.json
```

**Exécution effectivement réalisée : 31/31 tests réussis** dans `/mnt/data/janus33e`. Les 31 tests comprennent l'égalité de l'action d'origine avec l'action radiale intégrée par parties, la validation par différences finies des dérivées fonctionnelles pour les 12 champs sur la racine `z_*`, huit contrôles supplémentaires à `z` fixé, la convergence de la quadrature, le défaut attendu de la racine dégénérée, le découplage `m²=0`, et l'indépendance des deux poussières.

Le rapport JSON inclut SHA-256 des fichiers, valeur du crochet, les six contributions, vérification `F_z≈0`, test des deux fonctions de pondération et état des portes physiques. Il précise **`prior_step33d_95_tests_rerun=false`**, **`full_repository_regression=false`** et les deux contrôles De Felice/Aoki non exécutés. Aucun résultat d'une campagne de 126 tests **conjoints** ne doit être affirmé : les 95 tests de l'étape 33d ont été exécutés dans un autre environnement. Les nouveaux fichiers déposés sont à comparer aux empreintes Git exactes de la branche scientifique.

## Le verrou restant : ne pas annoncer trop tôt la contrainte BD

L'obtention du crochet mixte **hors surface de contraintes** est une donnée manquante importante de l'algèbre locale ; sa valeur numérique non nulle **n'est pas** en soi une « contrainte secondaire », un fantôme ni une preuve de santé du modèle. Les prochaines étapes obligatoires sont :

1. Dégager les termes distribués/localisés en `N M`, `N'M`, `N M'` et les contributions aux contraintes spatiales et à l'équation auxiliaire `F_z`, sur une base testant plusieurs fonctions de pondération. Répéter sur la surface **des deux** contraintes primaires et de `D_diag` (pas sur des profils arbitraires hors solution).
2. Effectuer la conservation temporelle complète de la combinaison de contraintes résiduelle, calculer les crochets de Dirac primaires/secondaires et vérifier un véritable rapport de lapses, en gardant `(θ_g,p_g),(θ_f,p_f)`.
3. Vérifier la limite homogène analytique de l'étape 33b, puis raccorder **cette même action** aux champs compacts temporels intégrables de l'étape 32e ; obtenir les principaux cinétique et gradient **après contraintes**.
4. Rechercher un vrai fond non homothétique sur solution (au-delà d'une reparamétrisation du fond homogène), puis vérifier les oracles indépendants De Felice finite-H `mu→0` et Aoki homothétique `K_S,c_S²` stables/instables avant toute étude du premier pli `a≈0.0301646`.

**État final :** `RADIAL_MIXED_HH_BRACKET_COMPUTED_OFFSHELL`; `HR_BD_SECONDARY_OPEN`; `NONHOMOTHETIC_ONSHELL_OPEN`; **`GATE_2B_OPEN`** ; **JANUS-R NON VALIDÉ cosmologiquement**. La critique du manuscrit externe JHR à signe Einstein–Hilbert f opposé demeure indépendante de ce programme positif-cinétique.
