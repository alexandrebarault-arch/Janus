# JANUS-005 — Compensation simultanée des deux premiers jets radiaux par KG et CF (2026-11-15)

**HEAD source :** `82c6023758efef80e007eb06aae0eea4ca97e578`. Formule `Rhog` retranscrite dans `research/repro/janus005_center_radial_density_jet_20261114.py` (blob `bdb3eaabb2bd9afea3ec8856134920fde1d5c51d`), en rendant `KG` et `CF` variables. Calcul local authentique avec Python 3, mpmath 1.3.0, 45 décimales. Ce calcul est **algébrique local**, pas une exécution Step55/58 ni une preuve de liberté physique de CF ou KG.

## Hypothèse et test

On conserve la tangente antérieure `dA=1`, `dM2/dA=-(4*A**3*M2*C+0.9)/(A**4*C)`, `dZ1/dA=-Z1/A`, `dCG/dA=-CG/A`, et on cherche `k=dKG/dA`, `f=dCF/dA` annulant simultanément `D a1` et `D a2`, où `a_n=(d^n Rhog/ds^n)(0)/n!`, `s=r²`.

À paramètres Step55 (A=0.4, M2=23.3348939346, Z1=0.004, CG=0.0015, KG=0.0012, CF=-0.0012, Y=0.5787707228025044, b1=1, b2=-4.2383993109, b3=13.6801214252), les dérivées mpmath calculées sont :

| | KG | CF | Direction initiale D |
|---|---:|---:|---:|
| a1 | +0.84414396724072850428 | -3.50781356722028028250 | -0.08612850795005535995 |
| a2 | +0.00427713728478214925 | +0.06577999869905038026 | +0.00009528960318703140 |

Le déterminant de la matrice des deux colonnes KG/CF est **+0.0705311892633288825986689031316**, non nul au point prescrit. La résolution linéaire donne :

`dKG/dA=+0.0755874817043977411888280492553`

`dCF/dA=-0.00636344858203444131023741494235`

Résidus des deux jets : `-1.10e-47` et zéro à la précision de travail.

## Contrôle contradictoire

Différences finies centrées sur les cinq paramètres de base et les deux compensations, avec la formule Rhog d'origine :

- pas 1e-4 : dérivées résiduelles de a1 = -6.414114945697547e-8 ; de a2 = +2.284665570509915e-10 ;
- pas 1e-6 : a1 = -6.414114682412496e-12 ; a2 = +2.284663554899e-14.

La décroissance quadratique avec le pas confirme l'annulation **au premier ordre** des deux jets. Ce n'est pas une conservation finie exacte.

## Verdict et limites

**Contre-exemple à une généralisation du NO-GO précédent :** le second jet non compensé par KG seul **peut** être compensé algébriquement si CF varie également. Cela ne démontre ni la conservation des jets d'ordre supérieur, ni du profil entier, ni l'admissibilité de KG/CF sous contraintes de Dirac et aux deux vrais bords. Les paramètres sont des décimales d'entrée exactes mpmath ; aucun certificat d'intervalle. Aucune cellule physique évaluée, certifiée ou inconclusive (0/0/0). Tests b3c3d9 non exécutés.

**Reproduction :** reprendre exactement la définition `Rhog` du script de provenance, remplacer ses constantes KG et CF par deux variables ; calculer `a1=mp.diff(lambda s: Rhog(s,...),0,1)` et `a2=mp.diff(...,0,2)/2` ; calculer les dérivées partielles mpmath de ces deux fonctions en A,M2,Z1,CG,KG,CF ; former la direction D ci-dessus et résoudre le système 2x2. Contrôler avec des différences finies centrées sur les sept paramètres. La transcription locale complète a été exécutée, mais son fichier temporaire n'est **pas** archivé sur GitHub : ce rapport documente le protocole et les sorties, non un script exact publiquement rejoué.

**NEXT_ACTION_EXACT :** tester l'indépendance physique de CF et KG dans Step45/49/55, les contraintes de Dirac linéarisées et les deux vrais bords ; calculer le troisième jet avec les compensations ci-dessus. Pour JANUS-001, transférer les 18 sources et fichiers historiques authentifiés, vérifier les SHA Git, exécuter neuf tests puis le pilote à une cellule.

**GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**
