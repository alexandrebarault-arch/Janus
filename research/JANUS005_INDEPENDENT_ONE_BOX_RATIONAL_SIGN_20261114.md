# JANUS-005 — contre-vérification analytique indépendante en une boîte (2026-11-14)

**Statut : PASS algébrique conditionnel ; aucune certification physique.** HEAD source `632fdd72dbdb046272af6bcff6a9682833e0eae0`. Source Step55 `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Script de contrôle `research/repro/janus005_one_box_rational_sign_20261114.py` blob `09ef33f702321d99886ef00d64df3c18ccd153a2`.

## Hypothèse falsifiable et méthode

Contrôler sans partition radiale, sans arithmétique d'intervalles personnalisée et sans évaluation de racine que le signe de `J=d(Wfbar,Dbar)/d(M2,Z1)` reste strictement négatif pour `s in [0,289/400]`, `Z1 in [-1/100,1/100]`, et les autres constantes Step55 fixées. Utiliser seulement les signes des coefficients et des bornes rationnelles obtenues par monotonie terme à terme.

Avec `Lg=A(1+cg*s)^2`, `Lf=A*Y(1+cf*s)^2`, les extrêmes rationnels `Lg0<=Lg<=Lg1` et `Lf0<=Lf<=Lf1` sont exacts. Pour `T=Lg^2+2*b2*Lg*Lf+b3*Lf^2` et `Tf=b2*Lg^2+2*b3*Lg*Lf+b4*Lf^2`, les signes `b2<0,b3>0,b4<0` donnent les bornes explicites du script. Il en résulte `Tlo>0`, `Tfhi<0`. Puis `0<sqrt(1-Z1^2*s)<=1` et `1+s*Z1^2<=1+(289/400)/10000` impliquent :

`Q=Lf*Tf+Lg*T*sqrt(1-Z1^2*s)*(1+s*Z1^2) <= Lf0*Tfhi+Lg1*Thi*(1+smax*zmax^2)=Qhi<0.`

Avec `M2>0,Lg>0,Lf>0,T>0` et dénominateur positif, la formule de déterminant publiée donne `J<0`. Il s'agit d'une preuve sur un continuum dans cette carte prescrite, non d'un échantillonnage.

## Exécution et contrôle contradictoire

Une implémentation indépendante équivalente a été exécutée localement par `python /mnt/data/janus_one_box_check.py` : **PASS**. Bornes décimales indicatives : `Tlo=0.10397953086758126`, `Thi=0.11027662537489809`, `Tfhi=-0.19593238750389178`, `Qhi=-0.0010718460211195725`. Les assertions utilisent `Fraction` exact, pas ces affichages arrondis. Le script GitHub de même algorithme a été publié et son blob relu ; **le fichier GitHub exact n'a pas été rejoué octet pour octet dans ce conteneur**. Commande de rejeu persistante : `python research/repro/janus005_one_box_rational_sign_20261114.py`.

Cette preuve indépendante de la partition 256 cellules réduit le risque d'erreur du moteur d'intervalles précédent, mais partage ses coefficients et sa formule algébrique. Aucun nouveau test du moteur b3c3d9 ; cellules physiques évaluées/certifiées/inconclusives = **0/0/0**. La liberté de M2/Z1/PG, les deux vrais bords, les contraintes de Dirac, la dynamique 4D et les observables restent ouverts.

**NEXT_ACTION_EXACT :** JANUS-001 reconstruire les dépendances originales et les sources historiques, comparer les blobs Git aux octets locaux, puis exécuter `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v` et le pilote `--cells 256 --max-cells 1`. JANUS-005 : dériver le sous-espace tangent physiquement admissible à partir de Step45/49/55, des deux vrais bords et des contraintes de Dirac. **GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**
