# JANUS — Étape 53 : deuxième coefficient central algébrique exact et raccordement radial amélioré

**22 octobre 2026. Branche de recherche active :** `research/gate2b-nonhomothetic-transfer`. **Gate 2B OUVERT ; JANUS-R NON VALIDÉ.**

## 1. Progrès analytique réellement obtenu

Dans la réduction sphérique à deux termes Einstein–Hilbert positifs, interaction Hassan–Rosen et DEUX poussières canoniques en mouvement, les étapes 45–46 avaient dérivé le secondaire (C=K_{00}-K'_{01}) sur les six couples canoniques et l'équation primaire-réduite (p'_{L_f}=-C_0/C_1) sans différences finies. Les étapes 48–49 avaient trouvé la condition de régularité locale au centre et Step52 le coefficient suivant (U_1) EXACTEMENT algébrique, pour l'étalonnage décimal traité comme rationnel.

Step53 étend cet ordre exact : en posant (s=r^2),

[
p_{L_f}(r)=r^2igl(U_0+U_1s+U_2s^2+O(s^3)igr).
]

Noter (G(s,U)=p'_{L_f}(r,p_{L_f}=sU)/r) (fonction analytique dans la charte régulière). L'identité centrale précédemment démontrée est (G(0,U)=3U_0-U). Dans l'équation exacte (2sU_s=G(s,U)-2U), les coefficients de Taylor donnent successivement

[
5U_1=partial_sG(0,U_0),
]

et **nouvelle récurrence exacte** :

[
oxed{7U_2=rac12partial_{ss}G(0,U_0)
       +partial_{sU}G(0,U_0),U_1
       +rac12partial_{UU}G(0,U_0),U_1^2.}
]

Cette récurrence a été réalisée sans dérivées numériques : l'évaluateur `numerics/hr_step53_exact_center_u2.py` procède par deux passages sur le même second membre physique, exprimé en jets de Laurent à coefficients dans (mathbb Q(H)), (H=sqrt{H^2}>0), (H^2inmathbb Q). Premier passage avec (p_{L_f}=r^2U_0) : terme en (r^3=5U_1). Deuxième passage avec (p_{L_f}=r^2(U_0+U_1r^2)) : terme en (r^3=4U_1) **vérifié exactement** et terme en (r^5=7U_2). Les racines et inverses sont développés par récurrences EXACTES en fractions rationnelles ; les premières puissances inconnues sont suivies conservativement.

## 2. Nouveau résultat algébrique exact U2

Pour les constantes de référence de JANUS-R imprimées et traitées comme **rationnels décimaux exacts**, le résultat est

[
oxed{U_2=A_2+B_2sqrt{H^2}},qquad A_2,B_2,H^2inmathbb Q.
]

**Les trois fractions exactes** figurent sans arrondi dans `research/reports/gate2b-step53-report.json`, avec (A_2<0), (B_2<0) et (H^2>0). Affichage :

[
oxed{U_2simeq-0.000010073853486743828175736890952863935933883641943763773429699704274}.
]

L'inégalité de signe **ne dépend pas** de cet affichage : une approximation du radical bornée extérieurement par `isqrt` sur une grille de (10^{-100}), et des opérations `Fraction` exactes, fournit deux rationnels enveloppants de largeur strictement inférieure à (10^{-100}). Par exemple ces bornes décimales rationnelles strictes encadrent le résultat :

[
-0.00001007385348674382817573689095286393593388364194376377344
<U_2<
-0.00001007385348674382817573689095286393593388364194376377342.
]

La cohérence avec le certificat **exact** Step52 est contrôlée en égalité stricte des deux fractions (A_1,B_1), et non en doubles flottants. Quatre ordres de troncature des jets `12,14,18,22` produisent **identiquement les mêmes fractions (A_2,B_2)**. Le premier coefficient inconnu peut entrer à l'ordre (r^7,r^9,r^{13},r^{17}) respectivement, toujours **au-delà du coefficient utile (r^5)**.

Ce certificat couvre un **coefficient local de données initiales** pour le système primaire-réduit et l'étalonnage rationnel. Il ne prouve ni une évolution temporelle globale ni la suppression du fantôme de Boulware–Deser.

## 3. Vérification numérique distincte : tir depuis le centre

Le programme `numerics/hr_step53_outward_compare.py` reconstruit indépendamment les fonds sphériques prescrits, la primaire g et le second membre physique de Step46, puis intègre radialement avec `scipy.solve_ivp`, méthode **DOP853**, `rtol=2e-12`, `atol=1e-18`, pas maximal 0,012. La référence interne est une intégration initiée à (r=0.001) avec les trois coefficients centraux ; (p_{L_f}(0.85)=-0.0033864293564879076).

| Rayon de départ | Écart final en ne gardant que U0+U1 | Écart final avec U0+U1+U2 |
| ---: | ---: | ---: |
| 0,05 | 9,270795936489051e−15 | 4,336808689942018e−19 |
| 0,025 | 8,109832250191573e−17 | 3,0357660829594124e−18 |
| 0,0125 | 1,0842021724855044e−17 | 8,239936510889834e−18 |
| 0,00625 | 2,168404344971009e−18 | 9,974659986866641e−18 |

L'effet principal est **une forte amélioration à départ (r=0.05)** ; à plus petit rayon le plancher numérique et la référence elle-même peuvent limiter ou inverser le gain. Les écarts présentés sont **relatifs à la référence NUMÉRIQUE**, et ne sont en aucun cas des bornes mathématiques d'erreur globale. L'EDO est celle du secondaire, donc obtenir (C) faible par substitution ne constitue pas un test indépendant de l'action Poisson non intégrée. Les précédentes vérifications indépendantes Step48 demeurent séparées.

## 4. Tests, publication et provenance exacte

Les **9 nouveaux tests** de `tests/test_hr_step53_exact_center_u2.py` ont **effectivement réussi**, à partir des fichiers locaux dans `/mnt/data/janus-step53` :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step53_exact_center_u2.py
# 9 PASSED in 12.62 seconds.

for j in 12 14 18 22; do
    JANUS_JET_ORDER=$j OPENBLAS_NUM_THREADS=1 PYTHONPATH=. \
      python -m numerics.hr_step53_exact_center_u2
done
```

Les tests vérifient : identité exacte des fractions U1 avec Step52, identité des coefficients U2 sur les quatre troncatures et contrôle des puissances inconnues, intervalle rationnel U2 strictement négatif, inverses et racines de séries formelles sur exemples négatifs, dénominateur de récurrence égal à 7, et rapprochement numérique d'une référence DOP853.

**Les trois nouveaux fichiers de ce tour sont byte-identiques aux octets effectivement exécutés, vérification par comparaison de leurs Git blob SHA :**

- `numerics/hr_step53_exact_center_u2.py` — `ee4515190e5b1733fb94641e6344e4ee96cdef6c`;
- `numerics/hr_step53_outward_compare.py` — `7a445614167a4cb7304aec7d19f38295d32a8890`;
- `tests/test_hr_step53_exact_center_u2.py` — `4e1848157c6ec95c7a0d6e73c0921573605f7117`.

**Réserve importante d'authenticité des dépendances :** les deux modules historiques Step45/46 locaux ont été **reconstitués en reproduisant leurs équations exactes**, mais ne sont **PAS des fichiers byte-identiques** aux blobs GitHub historiques dans cet environnement isolé. Sur GitHub, les trois nouveaux fichiers importent directement les vraies dépendances publiées ; néanmoins **la réexécution combinée avec ces octets originaux n'a PAS eu lieu dans ce tour**. Il serait donc faux d'appeler cette exécution une validation exhaustive de la chaîne historique. Des tests antérieurs (Steps 51–52) avaient établi séparément l'authenticité de sources originales ; ils n'ont pas tous été relancés ensemble ici. GitHub Actions/workflows restent désactivés.

Fichiers JSON détaillés générés en local (pas uploadés séparément) : `research/reports/step53-u2-raw.json` SHA256 `44244e855f6f0cd8b7fdbe53c145fdab6e9c7aa872e61a6dd72232177ffd445c`, et `research/reports/step53-shoot-raw.json` SHA256 `d7d7b1c68e28b36859322b7efc19ddbce01b5279717829d729013fa368e6b573`. Les **fractions algébriques exactes et valeurs de tir essentielles** sont sauvegardées dans le rapport machine GitHub.

## 5. Le verrou réel inchangé : Gate 2B

L'amélioration des données de départ ne certifie PAS : (i) la prolongation de la véritable solution C=0 de (r=0) à (0.85) avec erreur rigoureusement bornée ; (ii) la positivité **continue** des deux poussières sur cette branche non polynomiale et la non-annulation des chartes J/K ; (iii) la **préservation temporelle** ({C,H_{m total}}) avec tous SIX couples canoniques, rang de la matrice de Dirac, fixation des lapses, termes de bord et secteurs exceptionnels. Ces tests sont nécessaires avant toute conclusion « ghost-free ».

**Prochaine étape 54 :** reconstituer une chaîne Step45→53 de **fichiers originaux strictement byte-identiques** et relancer tous les tests ciblés ; utiliser (U_0,U_1,U_2) pour une continuation radiale **validée** par intervalles, et dériver la préservation temporelle de la secondaire, au lieu de multiplier seulement les précisions d'initialisation. Le dépôt a encore trois refs tant que l'administration GitHub n'a pas changé la branche par défaut et supprimé `main` et `research/v2-flrw`; leurs historiques ont déjà été préservés par `4f7a3a1` sans modification de l'arbre scientifique.

**VERDICT : U2 EXACT ALGÉBRIQUE ET NÉGATIF POUR LE BENCHMARK DÉCLARÉ, TIR NUMÉRIQUE AMÉLIORÉ ; GLOBAL/PHYSIQUE/DIRAC OUVERTS ; GATE_2B OPEN ; JANUS-R NOT VALIDATED.**
