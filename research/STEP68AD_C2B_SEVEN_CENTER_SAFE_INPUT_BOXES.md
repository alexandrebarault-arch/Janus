# JANUS — 68ad-C2b : sept boîtes rationnelles régulières pour le vrai U(s)

Date : 2026-10-26. Branche unique : `research/gate2b-nonhomothetic-transfer`.

**Résultat spatial conditionnel, PAS de certification temporelle. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Nouveauté vérifiée

Le code original `hr_step68o_temporal_interval_annulus.py` (Git blob `c99caebc17f243784450ddff94fb061767e6d8e7`) calcule `_ode_coeff` par `(G-2U)/(2s)`. Sur les petites cellules `s≈0`, la division d'intervalles fortement corrélés produit une surestimation. **Ne pas interpréter un intervalle qui traverse zéro comme une instabilité physique.**

Nous construisons maintenant, sans division par `s`, des boîtes rationnelles exactes pour **(U,U_s,U_ss,U_sss)** sur les sept cellules fermées qui couvrent `r∈[1/64,1/32]`. Entrées : le vrai rapport physique Step68v (barrière cubique), Step68ac (coefficients U0,U1,U2) et Step68ad-B2 (dérivées globales U_ss et U_sss). Les trois rapports sont épinglés à leurs SHA Git et `load_pinned()` rejette toute altération des octets.

Pour `s∈[a,b]⊂[0,1/1024]` :

```
U*(s) = U0 + U1*s + U2*s²
|U(s)-U*(s)| <= (1/10^7)*s³                  [Step68v]
U_s ∈ [us_min,us_max], U_ss ∈ [uss_min,uss_max],
U_sss ∈ [usss_min,usss_max]                    [Step68v et B2]
U(s) ∈ (U0+U1*[a,b]+U2*[a,b]²)
       +[-b³/10^7,+b³/10^7]                   [arithmétique Fraction]
U(s) ∈ [U0_min+us_min*a,U0_max+us_max*b]      [monotonie U_s>0]
=> intersection des deux boîtes rigoureuses.
```

Les opérations `Q` utilisent des `Fraction` exactes (aucun arrondi flottant). Les huit extrémités `r` sont `1/64, 1/56, 9/448, 5/224, 11/448, 3/112, 13/448, 1/32` ; toutes les cellules se touchent, sans lacune.

**Mesures sur les sept cellules, issues des champs rationnels exacts lus sur GitHub :**

- Largeur maximale de la boîte U : **1,0624409173110848 × 10^-7**, exactement `5349668327184482945967454922219/50352619520000000000000000000000000000`.
- Erreur maximale de la barrière cubique : **9,313225746154785 × 10^-17**, exactement `1/10737418240000000`.
- `U<0`, `U_s>0`, `U_ss<0`, `U_sss<0` dans chacune des sept cellules. Les bornes des dérivées sont **importées des certificats antérieurs**, jamais obtenues en différentiant une boîte sur U.
- La même routine admet une cellule commençant à `r=0` sans division par le rayon.
- Coefficients Taylor s pour le moteur original Step68n : `Jet([U,U_s,U_ss/2,U_sss/6])`. Pour passer aux dérivées radiales, utiliser le lemme exact 68ad-C2a.

## Observation structurelle qui réduit le problème

Dans le **vrai** Step68o, les huit profils géométriques et g-dust sont donnés explicitement par `jet_geometry(s)`. Les deux profils f-dust `rho_f` et `pSf` sont des compositions algébriques des champs `s,U,G(s,U)` et de cette géométrie. Par la règle de chaîne et la différentiabilité des dénominateurs sur le domaine physique, **aucune dérivée U d'ordre 4 n'est nécessaire** pour obtenir les jets d'ordre 3 de ces dix profils. Cela ne garantit PAS que leurs enclosures soient assez étroites pour déterminer les signes temporels : la dépendance d'intervalles demeure.

Le Step60 original (`hr_step60_full_constraint_prolongation.py`, blob `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`) offre également un quotient du coefficient `A_M` par la contrainte `C' = 0` sur la branche : à exploiter **après** vérification des substitutions de shift, pour réduire la dépendance aux troisièmes jets plutôt que de mettre arbitrairement `q'''=0`.

## Tests et traçabilité

Exécution réelle : `PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2b_center_boxes.py` : **16 PASS, 0 FAIL, 2,18 s** dans `/mnt/data/janus_c2b`. Les tests couvrent l'arithmétique exacte, la partition, les signes, le centre, le rejet de rapports et bornes invalides, la règle de chaîne symbolique et une composition f-dust générique. Source et tests publiés sont **octet-identiques** aux fichiers exécutés (Git blobs vérifiés).

**Limite de provenance locale explicite :** le conteneur n'a pas de DNS GitHub ; les tests ont utilisé des champs rationnels fidèlement retranscrits des rapports consultés via le connecteur, et non les trois fichiers complets matérialisés localement. Le chemin `load_pinned()` a été testé en rejet d'altération, mais **pas en authentification positive de rapports complets** dans cette session. La commande CLI, dans un clone complet, doit être rejouée pour authentifier les trois SHA avant toute affirmation plus forte.

- `numerics/hr_step68ad_c2b_center_boxes.py` — Git blob `94928e285f7e04deaf546abbeb9d3f05db33b213`.
- `tests/test_hr_step68ad_c2b_center_boxes.py` — Git blob `ae95668d5401df63c74fe22380b00fdc561fb426`.
- `research/reports/gate2b-step68ad-C2b-center-safe-input-summary.json` — Git blob `a131c60c221a9f54f9437b932dd44e04eddd2398`.

## NEXT 68ad-C2c — opération physique réellement bloquante

1. Dans un clone complet, lancer `python -m numerics.hr_step68ad_c2b_center_boxes research/reports` avec vérification SHA positive des trois rapports. Convertir les quatre intervalles rationnels en `old.I` sortants.
2. Remplacer `_ode_coeff(si)` de Step68o **uniquement dans un nouveau module**, sans altérer la source originale, par le `Jet([U,U_s,U_ss/2,U_sss/6])` certifié. Réutiliser `jet_geometry(s)`, `jet_G(s,u)`, les expressions originales `rho_f,pSf` et les douze jets.
3. Évaluer le vrai `physical_operator()` Step58 **non-frozen-shift** sur les sept cellules ; tester le quotient complet Step60 pour `A_M` en imposant `F_z=0,H_g=C=0` et leurs dérivées, sans mettre `q'''=0` prématurément. En cas d'intervalles trop larges, rapporter `INCOMPLETE`, raffiner et vérifier les corrélations.
4. Puis étendre au centre et traiter rang Dirac, lapses/bords/jauge, singularités J/K, oracle NON-IBP et cosmologie 4D.

**Aucun coefficient temporel A_N/r² ou A_M/r² n'a été exécuté/certifié dans cette session. Sept signes PENDING. JANUS non validé.**
