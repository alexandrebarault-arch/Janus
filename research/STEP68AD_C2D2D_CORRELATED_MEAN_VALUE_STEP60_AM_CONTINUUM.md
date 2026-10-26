# JANUS — 68ad-C2d2d : Step60 `A_M` strictement négatif sur sept cellules (certificat conditionnel)

**26 octobre 2026 — branche exclusive `research/gate2b-nonhomothetic-transfer`.**

## Résultat exact, portée et conditions

Sur la branche stationnaire positive de Step68o (`r>0`, `Lg>0`, `K>0`, `F_z=0`, `Sf=r Lf`, `Sg=r Lg`), avec les encadrements physiques continus `U,U_s,U_ss,U_sss` des trois rapports originaux SHA-épinglés Step68v, Step68ac et Step68ad-B2, **le représentant inférieur `A_M` original de Step60 est strictement négatif sur tout `r∈[1/64,1/32]`**. Il ne s'agit ni d'une évaluation ponctuelle, ni de la preuve d'un lapse négatif, ni d'une preuve de rang de Dirac.

Le représentant est `full_constraint_prolongation()['third_free_AM_on_Fz']` de l'original Step60, après élimination *exactement vérifiée* des jets canoniques d'ordre trois. Son dénominateur CSE d'interaction est remplacé uniquement par la factorisation sur coquille `T=Sg²*(beta1+2 beta2 Lf/Lg+beta3(Lf/Lg)²)`, déjà vérifiée contre l'expression originale ; aucun Hamiltonien n'est changé.

## Méthode rigoureuse et corrélation

Pour chaque sous-cellule fermée rationnelle `[a,b]`, poser `m=(a+b)/2` et `h=(b-a)/2`. Le moteur Step68o original reconstruit les jets canoniques jusqu'à l'ordre trois avec le jet de `U(s)` provenant de l'encadrement original. Une différentiation automatique *en mode direct* (valeur et dérivée radiale, toutes deux intervalles à arrondi extérieur entier `10^-28`) propage :

- `d(q)/dr=q'`, `d(q')/dr=q''`, `d(q'')/dr=q'''` ;
- `z=r Z1`, `z'=Z1`, `z''=0` sur la coquille vérifiée ;
- dérivées des produits, inverses, puissances, racines et valeurs absolues (ces dernières sont refusées si le signe traverse zéro).

Pour toute solution radiale réelle couverte par les rapports originaux, le théorème des accroissements finis implique l'inclusion **continue**

`A_M([a,b]) ⊆ A_M(m) + [-h,h] · (dA_M/dr)([a,b])`.

Le calcul préserve donc la corrélation radiale via un centre commun et une borne de dérivée ; il ne se contente pas de substituer indépendamment les intervalles de toutes les variables dans l'expression brute. Toutes les bornes publiées sont des fractions exactes issues de l'arithmétique à arrondi extérieur.

## Certificat calculé

La partition couvre exactement les **7 cellules originales × 32 sous-cellules = 224 sous-cellules fermées**, avec raccordement exact des bornes et sans trou. **224/224 bornes supérieures sont strictement négatives.** Sur les 224 inclusions :

- plus grande borne supérieure : `-12463417589607208432272964557/10000000000000000000000000000` (environ `-1,2463417589607208`) ;
- plus petite borne inférieure : `-6,696149147239292...` (la fraction exacte figure dans le JSON).

Le certificat machine `research/reports/gate2b-step68ad-C2d2d-Step60-AM-mean-value-compact.json` contient les 224 intervalles rationnels et les SHA des originaux. Le programme `numerics/hr_step68ad_c2d2d_correlated_mean_value.py` régénère le résultat sans utiliser les fragments de calcul intermédiaires.

## Tests réellement exécutés

`PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2d2d_correlated_mean_value.py` → **9 PASS, 0 FAIL** (20,37 s). Vérifications : algèbre duale et différentiation des puissances/racines/inverses, refus de domaines non différentiables, théorème des accroissements finis sur polynôme indépendant, contre-exemple aux signes ponctuels, SHA des originaux, intégrité rationnelle et couverture 7×32 du certificat, inclusion de la valeur physique originale Step60 à un milieu, reproduction indépendante de la première sous-cellule.

L'évaluation complète des 224 sous-cellules a été effectuée en quatre lots bornés de cellules originales (0–1, 2–3, 4–5, 6), avec contrôle de continuité et consolidation exacte ; elle n'est **pas** comptée comme 224 tests pytest supplémentaires. Les sources physiques originales restent intactes.

## Limites et prochaine recherche

**Step60 `B_N` : INCOMPLETE** (les enclosures précédentes contiennent zéro). **Step58 `A_N` et `A_M` sur le continuum : INCOMPLETE**. Le signe de ce représentant Step60 ne détermine pas à lui seul les signes des lapses, le rang de l'opérateur de Dirac, la préservation des contraintes, la stabilité, la dynamique 4D ni les observables cosmologiques. L'étape suivante doit traiter le représentant `B_N` (chercher une identité exacte sur la coquille ou une enclosure corrélée) et les deux coefficients Step58, puis examiner les conditions aux bords et les lapses admissibles.

**Statut scientifique : `GATE_2B OPEN` ; `JANUS_R NOT_VALIDATED`.**
