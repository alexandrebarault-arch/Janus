# JANUS-005 — Tangente de Friedmann élargie à M2 (2026-11-11)

Source authentique examinée au HEAD `51293e58ca1447f58d2b9494a6766493d0645ca1`: `numerics/hr_step55_global_barrier.py` (blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`). Le code prescrit `A=0.4`, `Y=0.5787707228025044`, `M2=23.3348939346`, `B0=0`, `B1=1`, `B2=-4.2383993109`, `B3=13.6801214252`, `H2=0.9/(3*A**3)+M2*(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3`, `PG=-2*A**2*sqrt(H2)`, `U0=MF*B*(PG/A-2*Z1)` et `B=A*Y`.

## Hypothèse falsifiable

On autorise **formellement** M2 à varier, en maintenant A, Y, MF, Z1, la densité 0.9 et les coefficients B0..B3 fixes. Posons K(Y)=(B0+3 B1 Y+3 B2 Y²+B3 Y³)/3, C=U0-MF Y(PG-2 A Z1), F=PG²-4 A⁴[0.9/(3 A³)+M2 K]. Le jacobien dans l'ordre (PG,U0,M2) vaut

`J=[[-MF*Y,1,0],[2*PG,0,-4*A**4*K]]`.

Si K != 0, il possède le vecteur tangent non nul `t=(1,MF*Y,PG/(2*A**4*K))` et `J*t=(0,0)`. Le mineur des colonnes (U0,M2) vaut `-4*A**4*K != 0`: rang 2, noyau de dimension 1 dans cet espace à 3 paramètres. En revanche, à M2 fixé, le mineur (PG,U0) vaut `-2*PG != 0` sur PG<0, confirmant le NO-GO précédent pour la sous-famille restreinte.

La valeur rationnelle exacte de K issue des décimales écrites dans le code est `5048913059636077415740439637123108264582160674322161103/117187500000000000000000000000000000000000000000000000000`, soit environ 0.0430840581088945273 > 0.

## Rejeu et contradiction

Commande réellement exécutée localement : `python /mnt/data/janus_run11/expanded_friedmann.py` avec SymPy. **5 assertions PASS**, vérifiant Jt=0, les deux mineurs, la dérivée de F en M2 et K>0. Le script est un calcul indépendant reconstruit à partir des formules du fichier source ; il n'exécute pas le moteur Step55/58.

**Contre-contrôle :** si M2 reste fixé, dF=2 PG dPG implique dPG=0 sur la branche PG<0 ; le résultat antérieur est conservé exactement. Si M2 varie, une tangente algébrique existe, mais les équations radiales, la géométrie, les deux vrais bords, les contraintes de Dirac, les lapses et la dynamique 4D ne sont pas vérifiés. M2 n'est pas ici établi comme paramètre physiquement libre. Il serait incorrect de conclure à une famille de solutions physiques.

## NEXT_ACTION_EXACT

Examiner la provenance physique de M2 dans Step45/49/55 et ses dépendances géométriques ; calculer les dérivées totales de la contrainte radiale et des deux vraies conditions aux bords le long de t. Si M2 n'est pas libre, rechercher un autre paramètre réellement admissible ou conserver le NO-GO de la carte fixe. JANUS-001 : transférer les sources authentifiées et lancer les neuf tests puis le pilote à une cellule. Cellules physiques nouvelles évaluées/certifiées : 0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
