# JANUS — Gate 2B, étape 33c : premier crochet de Poisson radial fonctionnel des deux poussières

Date : 2026-10-19. Branche de recherche : `research/gate2b-nonhomothetic-transfer`.

**Conclusion rigoureuse : `RADIAL_DUST_SMEARED_BRACKET=GREEN` sur chaque secteur, `FULL_RADIAL_EH_HR_BD_SECONDARY=OPEN`, `GATE_2B=OPEN`.** Ce résultat est **local en rayon**, mais ne vaut pas démonstration de la contrainte secondaire de Boulware–Deser de la gravitation bimétrique.

## Nouvelle étape réelle au-delà de l'homogénéité

L'étape 33b a prouvé la factorisation exacte de `{H_g,H_f}` sur **huit variables homogènes**, avec deux poussières canoniques conservées. En homogénéité, `theta'_g=theta'_f=0`, et les termes de crochet impliquant des dérivées de fonctions de test spatiales disparaissent. L'étape 33c restitue l'une de ces contributions : le **crochet de deux contraintes hamiltoniennes de poussière dans une véritable dimension radiale**, sans raccourci homogène.

Par secteur `i ∈ {g,f}`, prendre une longueur ADM radiale `L_i(r)>0`, un champ de phase de poussière `theta_i(r)`, son impulsion densité positive `p_i(r)` et deux lapses de test `N(r),M(r)` à support compact. Le Hamiltonien exact de la poussière irrotationnelle de l'étape 33a/32e est :

```
C_i(r) = p_i(r) sqrt[1 + (theta_i'(r)/L_i(r))²],
D_i(r) = p_i(r) theta_i'(r),
H_i[N] = ∫ dr N(r) C_i(r).
```

Avec `u=theta'`, `h=sqrt(1+u²/L²)` et `s=u/(L²h)`, les dérivées fonctionnelles sont

```
δH_i[N]/δp_i = N h,
δH_i[N]/δtheta_i = -∂r[N p_i s].
```

L'intégration par parties, dont les termes de bord disparaissent parce que les deux fonctions de test s'annulent aux bords, conduit exactement à

```
{H_i[N],H_i[M]}
 = ∫ dr p_i(r) theta_i'(r)/L_i(r)² · (N M' - M N')
 = D_i[(N M' - M N')/L_i²].
```

Les DEUX poussières possèdent des paires `(theta_g,p_g)` et `(theta_f,p_f)` **distinctes**, et leurs crochets canoniques croisés sont identiquement nuls. Cette indépendance n'implique pas l'indépendance gravitationnelle une fois les contraintes communes assemblées.

### Contrôle discriminant de la racine relativiste

La fermeture exacte exige `h dh/du = u/L²`. Pour `h=sqrt(1+u²/L²)` c'est une identité symbolique. L'approximation prématurée `h_wrong=1+u²/(2L²)` donne au contraire

```
h_wrong dh_wrong/du - u/L² = u³/(2L⁴).
```

Une dérivée radiale non nulle produit donc un résidu réel. Le test négatif rejette cette approximation au niveau de la contrainte locale.

## Vérifications numériques indépendantes

Fichiers exécutables :

- `numerics/hr_spherical_dust_smeared_bracket.py` : formule fonctionnelle exacte, Hamiltonien radial discrétisé avec impulsions canoniques nodales `P_j=w_j p_j`, calcul **indépendant** du crochet par différences finies en chaque `theta_j` et `P_j`, et contrôle de l'approximation non relativiste.
- `tests/test_hr_spherical_dust_smeared_bracket.py` : 12 tests nouveaux, dont les cas paramétrés, convergence radiale, antisymétrie, deux poussières indépendantes, racine relativiste, limite homogène et gardes d'entrée.
- `scripts/verify_gate2b_step33c.py` : relance conjointe avec l'étape 33b et manifeste de provenance exact.

Pour des fonctions lisses non homogènes au profil de contrôle (`seed_shift=0.3`), les résultats en unités normalisées sont :

| n radial | `D[(N M'-M N')/L²]` | Poisson par variations du Hamiltonien discrétisé | approximation tronquée |
|---:|---:|---:|---:|
| 33 | -0.0004657855164 | -0.0004649820789 | -0.0005662203666 |
| 65 | -0.0004712738461 | -0.0004710696252 | -0.0005738996559 |
| 129 | -0.0004726532006 | -0.0004726019329 | -0.0005758332733 |

La discrétisation des dérivées radiales explique les résidus qui diminuent au raffinement. Le **crochet canonique numérique** résulte de différentiations indépendantes du Hamiltonien discret en toutes ses variables nodales, et non d'une réécriture codée de la formule cible. Les contrôles de deux profils de poussière différents, de l'antisymétrie et du champ homogène sont également vérifiés.

## Portée scientifique — limite majeure

Cette étape **ne calcule pas** les crochets croisés `EH_g/HR`, `EH_f/HR`, `EH/dust` ni le système complet des contraintes sphériques de quantité de mouvement ; les contributions de la courbure intrinsèque, des impulsions gravitationnelles radiales, du décalage relatif `z`, et les termes de distribution dérivée `δ'(r-r')` restent à traiter simultanément. Une fermeture du **sous-secteur poussière** ne prouve absolument pas une contrainte BD secondaire locale ni sa préservation, et ne fixe pas les signes des modes physiques.

La variante Candidate-C on-shell utilisée par les étapes précédentes demeure **homogène et sans rayonnement**. Aucune véritable solution physiquement non homothétique ni vitesse physique `c_S` n'est produite ici.

## Provenance et tests

Après copie exacte du code et des tests des étapes 33a et 33b depuis leurs versions locales à empreintes GitHub vérifiées, la suite combinée **a effectivement été exécutée** dans `/mnt/data/janus33c` :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests
# 69 passed : 21 (33a) + 36 (33b) + 12 nouveaux (33c)
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33c.py gate2b-step33c-report.json
```

Les suites historiques des étapes 31–32e (93 tests) n'ont PAS été relancées dans cet environnement ; aucun résultat cumulatif 162 n'est revendiqué. L'environnement n'est pas un clone Git complet, pas de CI ni d'évaluation scientifique externe indépendante. Le manifeste déclare explicitement `full_repository_regression=false`, `local_spherical_HR_BD_secondary=NOT_DERIVED`, `DeFelice/Aoki=NOT_RUN`, `GATE_2B=OPEN`.

## Reprise après interruption : priorité ordonnée

1. Construire sur l'Hamiltonien **sphérique complet** de l'étape 33a les crochets fonctionnels espacés (`smearings`) des **contraintes gravitationnelles, de l'interaction HR et des deux poussières**. Les dérivées radiales et termes de bord doivent être conservés. Faire émerger ou réfuter une **contrainte secondaire BD locale**.
2. Étudier l'évolution de cette condition, le rang des contraintes, la fixation des lapses et le décalage relatif après traitement correct de ses équations ; maintenir les deux paires canoniques de poussière.
3. Relier cette réduction à l'action des perturbations compactes entièrement intégrables de l'étape 32e, sur un fond réellement non homothétique sur solution (encore absent), puis reproduire les deux limites indépendantes De Felice et Aoki sur la **même action réduite**.
4. Seulement alors tester le premier pli relatif Candidate-C `a≈0.0301646` et examiner les observations. Si une incompatibilité décisive apparaît, conclure négativement sans ajustement ad hoc.

**État : `STEP33C_RADIAL_DUST_BRACKET_GREEN`, `TRUE_LOCAL_BD_SECONDARY_OPEN`, `GATE_2B_OPEN`, `JANUS_R_NOT_VALIDATED`.**
