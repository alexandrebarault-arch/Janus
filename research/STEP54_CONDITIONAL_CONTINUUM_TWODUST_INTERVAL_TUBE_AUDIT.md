# JANUS — Étape 54 : positivité CONTINUE CONDITIONNELLE des deux poussières et de J/K

**Date : 23 octobre 2026. Branche de recherche EXCLUSIVE : `research/gate2b-nonhomothetic-transfer`. GATE 2B OPEN. JANUS-R NOT VALIDATED.**

## 1. Nouveau résultat rigoureux : enlever l'échantillonnage des signes

L'étape 53 avait produit les coefficients algébriques exacts (U_0,U_1,U_2) des données sphériques radiales à contraintes primaires f imposées, sur la calibration décimale rationnelle de référence. Les calculs de poussée radiale (`solve_ivp`) montraient les deux poussières positives sur un nombre FINI de rayons, mais ne pouvaient certifier leurs signes entre ces points.

L'étape 54 établit une **proposition rigoureuse de positivité conditionnelle SUR LE CONTINUUM [0,0,85]**, dans une famille explicite de profils canonico-radiaux *proches du polynôme central*, plutôt qu'un nouveau tableau d'échantillons.

Posons
[
s=r^2,quad P=p_{L_f}(r),quad U=P/r^2,quad V=P'(r)/r,
]
avec les limites régulières au centre, et les polynômes
[
U_*(s)=U_0+U_1s+U_2s^2,qquad V_*(s)=2U_0+4U_1s+6U_2s^2.
]
Les coefficients (U_0,U_1,U_2) ne sont pas arbitraires : (U_0) est une expression algébrique de l'équation régulière du centre (Step48), (U_1,U_2) sont les nombres algébriques du benchmark des Steps52/53, chacun rigoureusement contenu dans une paire de **fractions exactes** enregistrées. Les constantes d'action, de poussière et de métrique sont les décimales déclarées traitées comme des rationnels finis, et (H=sqrt{H^2}>0) est encadrée par des entiers.

**Proposition (positivité dans le tube).** Si un profil (P(r)) différentiable possède la parité régulière en (r=0) et satisfait, à TOUS les rayons (0<rle0.85),
[
oxed{
|U(r^2)-U_*(r^2)|le 0.01,qquad
|V(r^2)-V_*(r^2)|le0.01,
}
]
alors le calcul exact des Hamiltoniens sphériques primaires de l'action positive-EH + HR + deux poussières donne, sur tout l'intervalle :
[
oxed{rac{p_g}{r^2}>0.8854,quad rac{p_f}{r^2}>0.063,quad
J>0.659,quad rac{K}{r^2}>0.229.}
]
Les normalisations au centre sont entendues au sens des limites continues. Les deux dénominateurs des poussières, (S'_f) et (sqrt{1-z^2}) sont également strictement positifs ; leurs marges inférieures sont enregistrées dans le rapport machine.

Avec la condition beaucoup plus stricte (delta=0.0001), le certificat donne (ho_f=p_f/r^2>0.1111), les autres facteurs étant inchangés.

**L'énoncé NE DÉMONTRE PAS que la solution exacte de l'EDO secondaire (P'=-C_0/C_1) reste dans ce tube.** Il s'agit d'une **implication mathématique vérifiée**, et non d'une existence globale ou d'une preuve d'élimination du fantôme BD. La tâche pour l'étape 55 devient donc très précise : établir une borne de trajectoire exacte et de dérivée normalisée ((U,V)) autour de ((U_*,V_*)) compatible avec (delta=0.01).

## 2. Réduction des primaires originales sans singularité fictive en r=0

Le programme `numerics/hr_step54_interval_tube.py` réexprime les DEUX contraintes de poussières sphériques ORIGINALES en variables paires (s=r^2), sans diviser numériquement par une très petite valeur de (r).

Pour les fonctions spatiales prescrites (L_g=a(1+c_gs)^2), (L_f=b(1+c_fs)^2), (S_i=rL_i), (	heta_i'=k_i rL_i), (z=z_1r), poser
[
T=eta_1L_g^2+2eta_2L_gL_f+eta_3L_f^2,quad
T_0=eta_0L_g^2+2eta_1L_gL_f+eta_2L_f^2,quad
T_f=eta_2L_g^2+2eta_3L_gL_f+eta_4L_f^2,
]
[
widehat D_g=m^2M_g^2 L_gL_fTz_1/sqrt{1-z_1^2s},
quad widehat W_g=m^2M_g^2(L_gT_0+L_fTsqrt{1-z_1^2s}),
quad widehat W_f=m^2M_g^2(L_fT_f+L_gTsqrt{1-z_1^2s}),
]
donc (D_g=r^3widehat D_g), (W_i=r^2widehat W_i). Dans la f primaire et l'impulsion radiale originales, le facteur (F_f=U/(2M_f^2L_fS'_f)) et la phase (	heta'_f=k_f rL_f) donnent
[
oxed{
ho_f(s;U,V)=-
rac{U^2/(4M_f^2L_f)
-F_f(-swidehat D_g+L_fV)
-rac12 M_f^2 L_f^3,{}^{(3)}R_f
+s z_1widehat D_g/L_f+widehat W_f}
{sqrt{1+k_f^2s}+sF_fk_fL_f}.
}
]
La formule analogue du g-secteur conserve les moments g primaires prescrits, sans dépendre de ((U,V)). **Il n'y a AUCUNE division résiduelle par (r)**, d'où un contrôle du rayon zéro aussi bien que des intervalles intérieurs.

Les coefficients originaux de (J=T/L_g^2) et (K/r^2=m^2M_g^2 L_gL_fT) proviennent de l'interaction. Toutes les expressions sont évaluées avec racines/dénominateurs par intervalles.

## 3. Pourquoi les bornes sont rigoureuses et reproductibles

L'intégralité de ([0,0.85^2]=[0,0.7225]) est couverte par 256 cellules **rationnelles**, incluant exactement les deux bords. Dans chacune, toutes les décimales, les coefficients algébriques (U_0,U_1,U_2) et les deux perturbations (pmdelta) sont des INTERVALLES contenant certainement leurs valeurs réelles. L'arithmétique `I` stocke deux **entiers** `lo,hi` représentant un ensemble réel ([mathrm{lo}/10^{30},mathrm{hi}/10^{30}]). Toute somme, soustraction, multiplication, division à intervalle non nul et racine carrée positive procède avec des arrondis SORTANTS par `//`, `ceil_div` et `math.isqrt`. Le système échoue lorsque dénominateur ou racine ne permettent pas une opération sûre ; rien ne dépend de tolérances flottantes pour la preuve du signe. Les centres sont réguliers en variables normalisées.

Au tube (delta=0.01), les **MINIMA INFÉRIEURS RATIONNELS EXACTS** de l'ensemble des 256 cellules comprennent :

| Quantité | Borne inférieure rationnelle exacte |
| --- | --- |
| (p_g/r^2) | `885449518212857928681650684127/1000000000000000000000000000000` |
| (p_f/r^2) | `3975264472969728977824962611/62500000000000000000000000000` |
| (J) | `41238803182898789792808800157/62500000000000000000000000000` |
| (K/r^2) | `114607699435882633639640746711/500000000000000000000000000000` |
| Dénominateur poussière f | `199774878963432060741537666411/200000000000000000000000000000` |
| (S'_f) | `287881066390207517784924829/1250000000000000000000000000` |
| (sqrt{1-z^2}) | `999994219983295703449026418611/1000000000000000000000000000000` |

Le rapport `research/reports/gate2b-step54-report.json` contient aussi la marge g, le tube (delta=0.0001), la provenance, les limites et le plan d'étape suivant.

La diminution de la largeur des cellules resserre les bornes tout en restant sûre. Un contrôle a aussi comparé **indépendamment la primaire f symbolique originale de Step46** à l'expression paire de Step54, par `mpmath` à 75 chiffres, à quatre rayons ; chaque valeur originale se trouve dans l'intervalle calculé.

## 4. Tests et authentification

Pour la première fois depuis plusieurs étapes, les deux sources physiques historiques importées par la nouvelle suite sont des copies **OCTET POUR OCTET** des vrais fichiers GitHub :
- `numerics/hr_step45_exact_physical_ward.py` — Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ;
- `numerics/hr_step46_exact_secondary_ode.py` — Git blob `bac025c28dbe1561c0c36c56dbfda46dc326f804`.

Le nouveau programme vérifie ces hachages et **refuse** tout décalage. Les DEUX nouveaux fichiers GitHub sont également identiques aux octets locaux exécutés :
- `numerics/hr_step54_interval_tube.py` — Git blob `c2db1e6a4888194fc6f79aaee866efdad479dbfb` ;
- `tests/test_hr_step54_interval_tube.py` — Git blob `d1dc7407ae1781aa742cab09cff0fc5a24bce66e`.

Exécution effective dans `/mnt/data/janus-step54` :
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step54_interval_tube.py
# RÉELLEMENT : 9 PASSED en 2,03 secondes.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -c 'import json;from numerics.hr_step54_interval_tube import certify;print(json.dumps(certify(256,"0.01"),indent=2))'
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step54_interval_tube
```
Une première version des tests a signalé qu'un appel isolé à `profiles` acceptait un (s<0) non physique. Cette faille de garde a été **corrigée**, puis les neuf tests ont réussi. Il n'y a pas de tests globaux de l'ancien dépôt, ni de CI, ni de modèle cosmologique en évolution temporelle.

Les deux traces JSON complètes ont été produites **localement** dans `/mnt/data/janus-step54/research/reports`, mais pas uploadées séparément ; les bornes essentielles, les codes et les commandes sont préservés sur GitHub.

## 5. Vrai verrou restant et prochaine étape 55

1. **PRIORITÉ : PROUVER L'APPARTENANCE AU TUBE.** À partir de l'EDO normalisée exacte (2sU_s=G(s,U)-2U) et de la solution analytique locale (U(0)=U_0), dériver une borne de l'erreur (U-U_*) **et de sa dérivée normalisée (V-V_*)** sur ([0,0.7225]). Explorer une barrière différentielle scalaire, une EDO validée par intervalles, ou un théorème de contraction a posteriori sur le résidu polynomial exact. Ne pas confondre cette étape avec le certificat conditionnel de signes déjà achevé.
2. Refaire un contrôle indépendant non intégré par parties sur la nouvelle trajectoire **après** certifier son encadrement ; ne pas déduire (C=0) indépendamment du fait de l'avoir imposé par construction.
3. Calculer ENFIN le vrai crochet de préservation temporelle ({C,H_{m total}}) avec tous six couples canoniques, le rang de Dirac, la fixation des lapses, et les secteurs exceptionnels (J/K) et frontières. Le certificat Step54 ne démontre aucun de ces points.
4. Continuer à sauvegarder les commits, tests, résultats et pointeur dans `00_CURRENT_RESTART.md`. Travailler uniquement sur `research/gate2b-nonhomothetic-transfer`. Les historiques des anciennes branches sont préservés (`4f7a3a1`) et l'ancienne PR V2 est fermée sans fusion, mais supprimer deux références GitHub et changer le défaut reste une opération administrative non prise en charge par le connecteur.

**VERDICT : PREUVE RIGOUREUSE DE POSITIVITÉ SUR UN TUBE DU CONTINUUM `[0,0.85]`, **CONDITIONNELLE** À L'APPARTENANCE DE LA SOLUTION EXACTE ; APPARTENANCE ET PRÉSERVATION DIRAC TEMPORELLES TOUJOURS OUVERTES. GATE_2B OPEN, JANUS-R NOT VALIDATED.**
