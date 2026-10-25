# JANUS — Étape 68j : identité exacte du coefficient temporel de N' modulo la secondaire

**25 octobre 2026 — branche :** `research/gate2b-nonhomothetic-transfer` uniquement. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

## 1. Nouveau résultat décisif sur l'opérateur physique ORIGINAL

On appelle `B_N` le coefficient du lapse dérivé `N'` dans le crochet temporel complet `dot C_red` calculé par l'ORIGINAL six-pair Step58. Step60 puis Step68i ont fourni le représentant à jets canoniques inférieurs, sur la stationnarité `F_z=0` avec `K>0` et charte régulière :
```text
alpha = (1-z²)/(Lg Lf)
beta  = partial_(Sg'') [ B_N + alpha Hg' ] / [2 Mg² Sg/Lg]
R_BN  = B_N + alpha Hg' - beta Hg
```
Step68i a déjà prouvé que `R_BN` ne dépend d'aucun des douze jets `q''` ni `q'''` (et contrôle négatif de beta). **La présente étape franchit le dernier verrou algébrique :**

[
\boxed{F_z=0\quad\Longrightarrow\quad
R_{B_N}=\frac{z}{L_g}\,C.}
]

Ainsi, sur les contraintes `F_z=H_g=H_g'=C=0`, et pour les profils physiques dont la prolongation de la stationnarité est appliquée comme précédemment :
[
\boxed{B_N
=-\frac{1-z^2}{L_gL_f}H'_g+\beta H_g+\frac{z}{L_g}C
=0.}
]

Avec l'identité exacte Step68h `B_M=3z(z²-1)/(Lg Lf²)*Fz'` sur `Fz=0`, puis `B_M=0` sur `Fz'=0`, **les deux coefficients de dérivées premières des lapses s'annulent analytiquement** sur la surface des contraintes annoncée. Avec Step58, les coefficients d'ordre 2 s'annulent également sur `Fz=Hg=0`.

**Attention à la portée logique :** les expressions sont celles du noyau sphérique à six couples Step45/58, sur la charte positive régulière et les contraintes/prolongations citées. Elles ne préjugent ni les chartes `K=0,J=0`, ni les termes de bord, ni le rang de Dirac de la théorie 4D.

## 2. Preuve exécutable : 25 dérivées exactes ET ancrage rationnel

Les VRAIS fournisseurs physiques historiques Step45,57,58,59,60 sont importés avec **vérification SHA Git octet pour octet** ; la preuve part du représentant déjà certifié de Step68i, sans retaper le Hamiltonien.

Définir sur `Fz=0` :
[
T=R_{B_N}-\frac{z}{L_g}C_{\rm original}.
]
Le logiciel identifie précisément **25 variables symboliques indépendantes** dans `T`. Pour chacune, il calcule `partial T/partial x`, met sur un dénominateur commun et vérifie que le **numérateur développé est exactement le polynôme nul**. Il ne s'agit ni de nombres approchés ni d'une interpolation à partir d'échantillons.

Les groupes de preuve sont :

| Groupe indépendant | Variables vérifiées | Nombre |
|---|---|---:|
| Momenta et jets | `pLf,pLg,pSf,pSg,pSgr,pg,pgr,Lfr,Lgr,Sfr,Sgr,zr,tgr` | 13 |
| Métriques A | `Sg,Sf` | 2 |
| Métriques B | `Lg,Lf` | 2 |
| Paramètres et déplacement | `Mf2,Mg2,m2,beta0,beta1,beta2,beta3,z` | 8 |
| **Total** | **Ensemble exact des symboles libres** | **25** |

La constante restante est déterminée par substitution **rationnelle exacte** sur une charte sans singularité : `z=3/5`, `zr=1/10`, `tgr=0`, `beta2=-1/2`, tous les autres symboles libres à 1. On obtient
[
\boxed{T_{\rm reference}=0,\qquad
C_{\rm reference}=-53/40\ne0.}
]
Ce dernier point est essentiel : la preuve **n'a pas supposé `C=0`** pour faire apparaître artificiellement son facteur. Le contrôle négatif remplaçant `R_BN-zC/Lg` par `R_BN+zC/Lg` produit une dérivée non nulle par rapport à `pSf`.

La preuve des dérivées et le point d'ancrage concluent sur les composantes analytiques de la charte physique à racine positive où les dénominateurs sont réguliers. Les hypothèses `K>0,|z|<1,Lg,Lf,Sg,Mg²\ne0` sont conservées ; ne pas étendre cette identité sans contrôle aux cartes singulières.

## 3. Sources, tests, reproductibilité

- **Code réellement exécuté et SHA Git vérifié :** `numerics/hr_step68j_BN_exact_secondary_identity.py` — `a500cdb1a09c853d46848719e26be9bbec55fb64`.
- **Tests réellement exécutés et SHA Git vérifié :** `tests/test_hr_step68j_BN_exact_secondary_identity.py` — `44a84c5b5aa234ae719fa2e6f818456985c2dad9`.
- **Rapport machine complet des 25 dérivées :** `research/reports/gate2b-step68j-original-BN-C-identity.json` — `25a47c7eeed9dec111ecd3f5da891a02d84184d9`.

Les vérifications ont été fractionnées volontairement pour respecter les délais d'exécution des calculs lourds :

```bash
cd /mnt/data/janus-step68f
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step68j_BN_exact_secondary_identity.py -k 'canonical_and_gradients or reference or symbols or authenticity'
# 4 passed, 3 deselected in 16.88s
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step68j_BN_exact_secondary_identity.py -k 'metrics_a'
# 1 passed, 6 deselected in 27.53s
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step68j_BN_exact_secondary_identity.py -k 'metrics_b'
# 1 passed, 6 deselected in 30.21s
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -c "from numerics.hr_step68j_BN_exact_secondary_identity import group_certificate; print(group_certificate('couplings_and_z'))"
# CERTIFICATE_COMPLETE pour 8 dérivées
```

Une invocation Pytest du dernier groupe a affiché `1 passed`, mais la commande a dépassé ensuite la limite de l'outil ; **ce passage Pytest n'est pas compté comme une fin propre**. Le groupe de huit dérivées a été réexécuté directement à terminaison normale. Aucun test unifié de ces calculs n'est revendiqué, et les GitHub Actions restent désactivées.

## 4. Conséquence scientifique et verrou restant

La relation temporelle physique sur la surface des contraintes **n'a plus de `N'`, `M'`, `N''` ni `M''`** (sous les hypothèses décrites), d'où **au niveau de ce modèle local** :

[
\boxed{\dot C_{\rm red}=A_N(q)N+A_M(q)M.}
]

On a déjà observé NUMÉRIQUEMENT sur des jets locaux compatibles avec l'EDO authentique Step55 que `A_N>0,A_M<0` sur 17 rayons échantillonnés et `-A_N/A_M≈0.519`. **Ces observations ne constituent pas un certificat de signe sur la vraie trajectoire globale du centre** et ne fixent pas les lapses avec conditions aux bords.

**NEXT Step68k :** démontrer/certifier les signes et la régularité centrale de `A_N,A_M` sur le profil authentiquement prolongé et certifié du centre, puis confronter l'équation `A_NN+A_MM=0` à toutes les primaires, aux conditions de bord et à un oracle Poisson indépendant non intégré par parties. Les cas `K=0,J=0`, le rang complet, les degrés de liberté et le fantôme BD sont toujours OUVERTS.

**VERDICT : les deux coefficients temporels en dérivées premières sont prouvés nuls sur le shell pertinent ; GATE_2B OPEN — JANUS-R NOT_VALIDATED.**
