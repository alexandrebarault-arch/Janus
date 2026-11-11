# JANUS-005 — Audit de la famille Pg et de la géométrie f (2026-11-11)

**HEAD source fixé :** `7b8656818fba85cb49464b218a4a34f043720ea2`. Audit statique des sources authentiques, **pas** rejeu physique ni certificat de contraintes. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

## Observation vérifiable
Dans `numerics/hr_step55_global_barrier.py` (blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`), `geometry(s)` calcule `Lf,Sfr,Dbar,Wfbar,Rf` à partir de `A,B,CG,CF,MG,MF,M2,B0..B4,Z1` et `s`, **sans dépendance de PG**. `KF` est également fixé. Les variables `Gmom,Gprime,Rhog,Psg0` du secteur g dépendent en revanche de `PG`. La fonction `G(s,u)` utilise ces reconstructions.

Dans `numerics/hr_step68ad_c2d2e5b3b2c2b3c2b2b_authentic_variational.py`, la famille explicitement calculée modifie `b.PG=old_pg+[-radius,radius]` et `b.U0`, tout en conservant les autres constantes. Le calcul de `G_Pg` propage les variations dans `Gmom,Gprime,Rhog,Psg0` (lignes de `original_g_dual`), mais pas dans les neuf coefficients f de la différentielle géométrique.

**Conclusion circonscrite :** pour la famille paramétrique *artificiellement restreinte* qui fait varier PG seul et tient les autres constantes fixes, à s fixé, les neuf dérivées géométriques f `(beta,Dbar,Wfbar,Rf,z1,mf,Lf,Sfr,kf)` par rapport à lambda sont nulles (où `beta` désigne le coefficient f reconstruit depuis kf, U, etc., sa dépendance en U étant déjà comprise dans le jacobien : ne pas confondre beta f total avec sa part géométrique fixe). Plus précisément, le `beta` de la reconstruction f peut dépendre de U ; son **terme explicite de géométrie à U fixé** ne varie pas avec PG. Par conséquent la somme de dérivées géométriques de JANUS005_FULL_OUTER_F_GEOMETRIC_CHAIN_RULE est nulle dans cette famille **si** les neuf paramètres de cette somme désignent leurs valeurs indépendantes à U,V fixés.

**Contrôle contradictoire / limite majeure :** `PG` modifie bien les données g, donc la famille n'est pas une variation où *toute* la géométrie g est fixe. Surtout, le code ne démontre pas qu'une variation de PG seule conserve les deux vrais bords, les contraintes de Dirac et la fixation cohérente des lapses. Une famille de solutions pleinement admissibles pourrait obliger d'autres paramètres à varier ; les termes géométriques réapparaîtraient. Le contre-exemple algébrique antérieur reste donc pertinent pour une famille physique générale. Ne pas extrapoler la nullité conditionnelle à JANUS global.

## Prochain test falsifiable
1. Authentifier et exécuter le moteur variational original avec ses quatre dépendances SHA et les tests associés, puis vérifier la dépendance effective des coefficients f par différentiation symbolique/dual à U,V fixés.
2. Vérifier explicitement la définition de `beta` dans la reconstruction f, et séparer sa variation induite par U de toute variation géométrique indépendante (risque de double comptage).
3. Soumettre cette famille PG-only aux deux vrais bords et aux contraintes Dirac. Si elle n'est pas admissible, retirer toute interprétation de tangent physique global.
4. JANUS-001 : transférer les modules originaux, authentifier les SHA, tests puis pilote à une cellule.

**Exécution de cette session :** lecture statique GitHub des trois modules, aucune commande Python physique, aucune cellule Step55/58 calculée/certifiée. Résultat = audit de dépendances du code, pas démonstration d'existence.
