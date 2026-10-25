# JANUS — Étape 68w : contrôle indépendant rationnel du rapport des lapses sur 1 585 cellules publiées

**25 octobre 2026. Branche exclusive :** `research/gate2b-nonhomothetic-transfer`. **GATE_2B OPEN — JANUS_R NOT_VALIDATED**.

## Résultat nouveau, portée exacte

Les étapes 68p, 68q et 68s ont produit trois certificats par intervalles du VRAI opérateur temporel sphérique à six couples Step58 sur la branche contrainte non homothétique Step55. Le présent travail **ne suppose pas ces certificats vrais sans les contrôler** : il charge leurs octets archivés depuis GitHub (Git blobs vérifiés), puis vérifie de manière indépendante en arithmétique rationnelle `BigInt` chaque intervalle et chaque cellule.

Les archives authentifiées sont :

| Étape | Domaine radial fermé | Cellules signées vérifiées | SHA Git blob |
|---|---|---:|---|
| 68s | `[1/32,1/16]` | 1 006 | `e890998a2f925f881ab85b60a9027e5828e35ed5` |
| 68q | `[1/16,1/8]` | 314 | `82f5d046cd0ca0c342adabe8b8f13cfc3f99308d` |
| 68p | `[1/8,17/20]` | 265 | `978d77d7dc8b30c3bdd78b25f1ca0d1c68900fe6` |

**Bilan vérifié : 1 585 cellules fermées** rangées en ordre de rayon, sans lacune, sans chevauchement, avec bornes rationnelles strictes `A_N>0` et `A_M<0` dans chaque cellule. Les trois statuts sont `CERTIFIED`, les files et listes d'échecs sont vides, et les jointures `r=1/16` et `r=1/8` concordent exactement. Vérification directement exécutée contre les trois sources GitHub, sans calcul en virgule flottante.

### Quotient exact, calculé SÉPARÉMENT par cellule

Sur chaque cellule, où
[
0<N_{min}le A_Nle N_{max},
qquad M_{min}le A_Mle M_{max}<0,
]
on a **nécessairement**
[
rac{N_{min}}{-M_{min}}
le-rac{A_N}{A_M}le
rac{N_{max}}{-M_{max}}.
]

La minimisation des bornes inférieures et la maximisation des bornes supérieures sur les **1 585 cellules**, par fractions exactes et comparaison croisée d'entiers, donnent :

[
oxed{
rac{299788821342512672157652732}{12067825969226896389389147905439}
 le -rac{A_N}{A_M} lerac{12100110164989551454170392062459}{870429215706122757278389599591}.
}
]

Pour lecture humaine, les extrêmes sont environ `2.484199×10^-5` et `13.9013144` ; ce sont les extrêmes des **bornes d'intervalle**, pas nécessairement les extrêmes physiques du quotient. Une conséquence stricte plus lisible est

[
oxed{
1/50000 < -A_N(r)/A_M(r) < 14,qquad
orall rin[1/32,17/20].
}
]

Cette borne est **large**, mais rigoureusement positive et finie. Elle ne confère aucune garantie `M/N≈0.519` à précision élevée sur le continuum ; ce nombre n'était que numérique sur des rayons testés.

### Normalisation des coefficients et rang de la SEULE équation temporelle

On obtient aussi, par cellule en utilisant les **deux extrémités rationnelles du rayon**, les inégalités strictes, valables pour tous les rayons couverts :

[
oxed{
A_N(r)/r^2>7/20,qquad A_M(r)/r^2<-546.
}
]

La ligne algébrique `[A_N(r),A_M(r)]` de la **SEULE** équation temporelle secondaire réduite (dot C=A_NN+A_MM) est donc de **rang ponctuel 1**, uniformément séparée de la ligne nulle après normalisation, sur cet anneau. Si les identités de disparition des coefficients des dérivées de lapses (Steps68h/68j) et toutes les contraintes spatiales sont imposées, choisir un `N(r)>0` suffisamment régulier et poser `M(r)=-A_N(r)N(r)/A_M(r)` donne un **couple de lapses positifs satisfaisant CETTE équation locale**, avec rapport borné comme ci-dessus. Ceci ne résout PAS les autres contraintes temporelles, les conditions de bord, ni l'existence d'une évolution 4D.

Les bornes exactes cellule par cellule et les cellules extrémales sont inscrites dans `research/reports/gate2b-step68w-rational-ratio-audit.json`.

## Périmètre du contrôle indépendant

L'indépendance de cette étape concerne l'**audit des archives rationnelles** : la cohérence des bornes, l'authenticité Git SHA, les jointures du recouvrement, les inégalités obtenues par des divisions rationnelles et le statut des preuves. **Elle ne représente PAS un deuxième oracle dynamique non-IBP** et ne recalcule pas indépendamment les intervalles (A_N,A_M) depuis le Hamiltonien six-paires. Les certificats physiques de Steps68p/q/s restent des hypothèses en amont pour la conclusion dynamique.

Le vérificateur autonome en Python standard `scripts/hr_step68w_archived_lapse_ratio_audit.py` peut être exécuté sur un clone complet :
```bash
python scripts/hr_step68w_archived_lapse_ratio_audit.py research/reports
```
Il exige les trois Git blobs EXACTS ; toute altération d'un octet échoue. Il ne dépend ni de SymPy ni de NumPy. Une vérification complète sur les trois contenus GitHub réels a été effectuée **dans l'environnement connecté avec entiers `BigInt`**, tandis que la version Python a été validée localement par **sept tests synthétiques** (7 PASSED, 0.04s, sous timeout 8s), dont refus de faux statuts, trous, mauvais signes et falsification SHA. **Ne pas prétendre que le clone complet Python a été exécuté localement dans cette session** : la session Python a été réinitialisée et n'a pas les fichiers volumineux GitHub montés.

Artifacts :
- `scripts/hr_step68w_archived_lapse_ratio_audit.py` — Git blob `93109dd8da5e524876a19340382d88ff4c077629`.
- `tests/test_hr_step68w_archived_lapse_ratio_audit.py` — blob `6cd0be37ef7a8ac5dac734b518f794216d4d250b`.
- `research/reports/gate2b-step68w-rational-ratio-audit.json` — blob `d644f0f02df36987ffb4d2d11c567509ffcdeca8`.
- `research/reports/gate2b-step68w-pytest.log` — blob `a4bcf9a3a9aea2ff4659ff3a08f4ceb622b55cec`.

## Prochaine vraie frontière — étape 68x

Le verrou physique reste la **normalisation des coefficients temporels AU CENTRE** (r	o0) sur la branche analytique, c'est-à-dire `A_N/r²` et `A_M/r²` pour `0le r<1/32`. Le Step68v a désormais certifié `|U-Ustar|≤10^-7 s³` sur `s≤1/64`, amélioration énorme sur l'ancien tube constant `10^-6` à rayon petit. À `r=1/32`, la borne est **(1/10737418240000000approx9.31×10^{-17})** contre (10^{-6}). C'est cette barrière **variable** qu'il faut brancher dans l'évaluateur temporel original Step58, avec normalisation analytique des facteurs radiaux, conservation de toute la poussière et des dérivées du shift, puis certifier `[0,1/32]` et la limite de ratio au centre.

Les bords, la jauge, l'oracle Poisson NON-IBP indépendant et le rang de Dirac complet restent non prouvés. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
