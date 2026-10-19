# JANUS Gate 2B — Étape 33c : fermeture fonctionnelle de la contrainte de moment radial

**Date :** 19 octobre 2026. **Branche :** `research/gate2b-nonhomothetic-transfer`.

**Passage partiel :** `SPHERICAL_SPATIAL_DIFF_WARD=GREEN`, `SPHERICAL_MOMENTUM_PB_ALGEBRA=GREEN`. **Limites maintenues :** `MIXED_HAMILTONIAN_PB=NOT_DERIVED`, `HR_BD_SECONDARY=NOT_DERIVED`, `GATE_2B=OPEN`, `JANUS_R_NOT_VALIDATED`.

## 1. Pourquoi ce calcul vient après le résultat homogène

L'étape 33b a démontré `{H_g,H_f}∝J(y)χ` **seulement dans le modèle homogène à huit variables canoniques**, puis le rapport des lapses sur une solution Candidate-C sans rayonnement. Le passage à des champs dépendant de `r` nécessite des dérivées fonctionnelles et une bonne gestion des distributions, des poids des densités et des termes de bord. L'étape 33c teste la partie exacte et non triviale **des transformations spatiales radiales** dans la véritable base sphérique de l'étape 33a, sans supposer un résultat sur les crochets hamiltoniens mixtes.

## 2. Variables canoniques et générateur exact

Chaque secteur possède les deux paires métriques `(L_i,pL_i)` et `(S_i,pS_i)` et sa paire de poussière propre `(theta_i,p_i)`. Les six paires sont gardées séparées (quatre gravitationnelles et deux de poussière). Pour une fonction compacte `η(r)` telle que `η(0)=η(1)=0`, le générateur de translation radiale diagonale est

```text
D[η] = ∫_0^1 dr η(r) ∑_{i=g,f}
       [pS_i(r) S_i'(r) - L_i(r) pL_i'(r) + p_i(r) theta_i'(r)].
```

Après intégration par parties **avec terme de bord nul**, ses vraies dérivées fonctionnelles, dans chaque secteur, sont :

```text
δD/δL = -η pL'       δD/δpL = (η L)'
δD/δS = -(η pS)'     δD/δpS = η S'
δD/δtheta = -(η p)'  δD/δp  = η theta'.
```

Elles donnent les poids de Lie radiale suivants : `L`, `pS`, `p_dust` sont des densités de poids 1, tandis que `S`, `pL`, `theta`, et le décalage relatif `z` sont scalaires de poids 0. `D(r)` est de poids 2. Les coefficients hamiltoniens locaux `H_g(r),H_f(r)` après la redéfinition Hassan–Rosen sont de poids 1. La courbure intrinsèque sphérique `R^(3)` est scalaire.

## 3. Résultat : crochet de deux contraintes radiales *avec poussières*

Le calcul reprend les douze vraies dérivées fonctionnelles du générateur et les intègre avec leurs signes canoniques ; il ne remplace pas l'algèbre par la formule attendue. On obtient :

```text
{D[η], D[ξ]} = D[η ξ' - ξ η'].
```

Sur les polynômes d'essai compacts et l'intervalle radial retenus :

```text
{D[η],D[ξ]} dérivées fonctionnelles = +2.3726108629148702e-5
 D[η ξ'-ξ η'] intégration séparée     = +2.3726108629152910e-5
 différence                            = -4.21e-18.
```

Les tests vérifient l'antisymétrie, l'annulation de `{D[η],D[η]}`, et **les 12 dérivées fonctionnelles individuelles** par perturbation directe de `D[η]`. Ainsi les deux poussières participent à l'algèbre : leurs contributions ne sont ni oubliées ni fusionnées.

## 4. Covariance de la densité hamiltonienne complète

Pour des champs polynomiaux réguliers indépendants `L_i(r),S_i(r),pL_i(r),pS_i(r),theta_i(r),p_i(r)` des deux secteurs, et un décalage relatif `z(r)` non nul, on construit les vrais coefficients locaux de l'étape 33a : gravitation Einstein–Hilbert **avec courbure `R3` et dérivées radiales**, interaction HR **avec tous les cinq coefficients bêta**, et **les deux Hamiltoniens de poussière**. On compare la dérivée numérique du changement infinitésimal de chaque champ à la dérivée radiale attendue :

```text
δH_g = (η H_g)',      δH_f = (η H_f)',
δD = η D' + 2η' D,    δR3_i = η (R3_i)'.
```

Le zéro des résidus est vérifié à plusieurs rayons de contrôle `r=.26,.31,.48,.63,.84`. Les résidus numériques de `H_g/H_f` restent sous `2e-10`, ceux de `D` sous `1e-11` et ceux de `R3` sous `2e-8`. Au voisinage de `r=.14`, le calcul de `R3` fait une soustraction de termes d'ordre `1/r²`, et le résidu de différences finies atteint `~1.7e-7`; le test conserve explicitement ce conditionnement au lieu d'annoncer une précision fictive.

L'équation algébrique du décalage relatif `F_z=D_g-K z/sqrt(1-z²)=0` est une densité de poids 2 ; sa solution non dégénérée `z_*` se transforme comme un scalaire. Les différences finies confirment aussi ce contrôle. **C'est une condition structurelle nécessaire, pas le calcul des crochets `{H_g[N],H_f[M]}`.**

## 5. Sources, exécution et provenance

Trois nouveaux fichiers :

- `numerics/hr_spherical_radial_diffeo_ward.py` — gradients fonctionnels explicites, vrai crochet de deux `D[η]`, et action infinitésimale sur les densités sphériques HR/Einstein/dust.
- `tests/test_hr_spherical_radial_diffeo_ward.py` — 23 nouveaux tests (12 dérivées fonctionnelles individuelles, 5 rayons, contrôles de courbure, branche du décalage, garde-fous de bord).
- `scripts/verify_gate2b_step33c_spatial.py` — reproductibilité avec provenance SHA-256, empreintes Git et indication des portes de validation qui restent ouvertes.

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests
# 80 passed, dans le même espace de travail ciblé

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33c_spatial.py gate2b-step33c-report.json
```

Dans `/mnt/data/janus33b`, les **80 tests exécutés ensemble** comprennent 21 tests exacts antérieurs de l'étape 33a, 36 contrôles de l'étape 33b et 23 nouveaux tests de l'étape 33c. Les fichiers de base 33a–33b sont comparés aux empreintes déjà publiées. Ce n'est **pas** un clonage intégral du dépôt ni un passage de sa CI ; les 93 tests de l'étape 32e ne sont PAS inclus dans ces 80.

## 6. Le verrou encore ouvert

Pour passer d'un contrôle des transformations spatiales à la question Boulware–Deser, il reste **le crochet fonctionnel complet des deux contraintes hamiltoniennes radiales**, après résolution cohérente du décalage relatif, y compris les termes en `∂r pL`, les dérivées spatiales de la courbure, les smearings distincts, l'évolution temporelle et les deux poussières. La matrice de Dirac fonctionnelle et ses contraintes primaires/secondaires devront alors être réduites sur un véritable fond non homothétique sur solution. Ce n'est pas déduit du seul rang de la mini-matrice homogène.

Les deux références physiques De Felice (H fini, `mu→0`) et Aoki (homothétique non linéaire, `K_S,c_S²` stable et instable), puis la première transition relative Candidate-C `a≈0.0301646`, ne sont toujours pas validées sur une action scalaire physique contrainte unique.

**Verdict :** `SPATIAL_DIFF_CANONICAL_ALGEBRA_GREEN`, `MIXED_HAMILTONIAN_FUNCTIONAL_BRACKET_OPEN`, `BD_SECONDARY_RADIAL_OPEN`, **`GATE_2B_OPEN`**. Ne pas confondre cette vérification avec une preuve de stabilité cosmologique.
