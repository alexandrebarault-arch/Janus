# JANUS — b3c3d3 : annulation cubique de la forme de bord non-IBP au centre régulier

28 octobre 2026. **Lemme exact cinématique sur la parité centrale, non preuve Dirac.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Provenance et statut du rejeu

Les dix coefficients de bord proviennent de la densité originale non-IBP Step37 (`numerics/hr_step37_original_nonibp_oracle.py`, blob `005449ade6e3582e3b9a5c3374a881a77e73e3f6`) et de l'audit symbolique b3c3d2 (`numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py`, blob `6898c88760cc0766e949f9bade4908b9bc176c58`). Step45 `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` a été relu. Les expressions sont transcrites et recalculées dans un script autonome ; **les imports originaux Step45/55/58, le test b3c2 et le profil Step55 complet n'ont pas été rejoués** : `git ls-remote` échoue sur `Could not resolve host: github.com`. Aucun nouveau résultat de tangence Dirac n'est revendiqué.

## Lemme et preuve

Considérer des familles lisses analytiques en `r²` autour du centre `r=0`, avec `Lg=L0+L2 r²`, `Lf=F0+F2 r²`, `Sg=r(L0+H2 r²)`, `Sf=r(F0+I2 r²)`, `N=N0+N2 r²`, `M=M0+M2 r²`, `z=z1 r`, `V=v1 r`, `pLg,pLf,pg,pf=O(r²)`, `pSg,pSf=O(r)` et `tg',tf'=O(r)`, avec `L0,F0>0`. Les variations respectent ces mêmes parités, **y compris** `δSg'(0)=δLg(0)` et `δSf'(0)=δLf(0)` ; les valeurs constantes des horloges peuvent varier. Les lapses peuvent varier au sein de cette famille lisse et paire. La régularité de `z` est supposée, pas déduite des contraintes ; le critère Step68ad-b3b2a reste une condition distincte.

La forme complète non-IBP a dix termes : coefficients de `δSg'`, `δSf'`, `δSg`, `δSf`, `δLg`, `δLf`, `δpLg`, `δpLf`, `δtg`, `δtf`. Les dix contributions sont impaires en `r`. Seuls quatre termes possèdent a priori un coefficient linéaire :

`(2 Mg2 N0 r) δSg' + (-2 Mg2 N0 r) δLg + (2 Mf2 M0 r) δSf' + (-2 Mf2 M0 r) δLf`.

Les relations de régularité `δSg'(0)=δLg(0)` et `δSf'(0)=δLf(0)` annulent exactement ces termes. Les autres contributions commencent en `r³`. Par conséquent **le pullback de la forme complète vaut `Theta_center=O(r³)`**, et, sur une famille lisse uniforme de paramètres, **`dTheta_center=O(r³)`**. Il s'agit d'une estimation d'ordre au centre, pas d'une charge de bord globale ni d'un contreterme au bord extérieur.

La borne est optimale sur l'espace cinématique : la variation `δL2=1` et les autres coefficients de variation nuls donne `lim_{r→0} Theta/r³=−2 Mg2 N0`. Une variation non régulière `δSg'(0)=δH0 ≠ δLg(0)` laisse au contraire `lim Theta/r=2 Mg2 N0(δH0−δLg0)`. La condition de tangence à la **parité géométrique** est donc essentielle. Le coefficient mixte libre `dN∧dSg'` de b3c3d2 n'est pas une obstruction au centre régulier : son terme linéaire se compense avec `dN∧dLg` lorsque `δSg'(0)=δLg(0)`. Les variations de lapses ne sont pas des paires canoniques ; la preuve n'établit pas leur compatibilité temporelle Step58.

## Tests et limites

`python -m numerics.hr_step68ad_b3c3d3_center_boundary_parity` : **25 assertions symboliques SymPy PASS**, dont dix contrôles de parité, dix coefficients linéaires, une annulation, un témoin cubique, un témoin adversarial, et deux contrôles mixtes de lapse. `python -m unittest -v tests.test_hr_step68ad_b3c3d3_center_boundary_parity` : **4 cas PASS**, rejouant les mêmes identités (non indépendants). Un premier test attendait 24 assertions alors que 25 étaient effectivement exécutées ; le compteur a été corrigé et les quatre cas ont été rejoués. **0 FAIL final.**

**Non prouvé :** tangence aux primaires, à `C(r)=0`, à la préservation temporelle Step58, admissibilité du bord extérieur `R=17/20`, existence de générateurs améliorés, charges physiques, rang après quotient de jauge temporelle, six couples de Dirac, `K=0/J=0`, dynamique 4D, stabilité et observables. Ce lemme recentre l'audit de différentiabilité sur le bord extérieur, sans supprimer les contraintes au centre sur les lapses et les horloges.

**Prochaine étape b3c3d4 :** réexécuter les moteurs originaux Step45/55/58 et b3c2 dès accès complet ; construire des variations admissibles au bord extérieur Step55 et tester leur pullback de `dTheta`, charges/générateurs améliorés et quotient de jauge temporelle, puis Dirac et 4D. `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.
