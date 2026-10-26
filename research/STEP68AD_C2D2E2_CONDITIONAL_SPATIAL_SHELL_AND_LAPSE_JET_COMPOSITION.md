# JANUS — 68ad-C2d2e2 : fermeture conditionnelle des contraintes spatiales et des jets de lapse

**26 octobre 2026.** Branche unique : `research/gate2b-nonhomothetic-transfer`. **`GATE_2B OPEN` — `JANUS_R NOT_VALIDATED`.**

## 1. Portée et provenance

Ce contrôle **reconstruit indépendamment** les formules authentifiées de Step45, Step46, Step55 et Step68o et les compose avec les théorèmes antérieurs Step58, Step68h et Step68j. Il ne prétend **pas** avoir importé et réexécuté les modules originaux en Python : leurs fichiers ont été relus en direct sur GitHub et leurs SHA blobs enregistrés dans le certificat. Les identités Step46 et Step68j sont des prémisses historiques déjà démontrées, non de nouvelles preuves.

## 2. Identité exacte des contraintes primaires

Pour chaque secteur `a=g,f`, l'expression **originale** `H_a=A_a-dB_a/dr` se réduit algébriquement à

`H_a = kinetic_a + dust_a − M_a² L_a S_a² R_a/2 + W_a + z D_g/L_a`,

avec `D_g=pSg Sg'−Lg pLg'+pg tg'` et `R_a=2/S_a²[1−(S_a'/L_a)²−2S_a S_a''/L_a²+2S_a S_a' L_a'/L_a³]`. La reconstruction a vérifié les deux annulations symboliques exactement, sans supposer les contraintes.

Sur la géométrie Step55 `S_a=r L_a`, `L_a=a(1+c_a r²)²`, l'identité de courbure donne `R_a=−48 c_a/[a²(1+c_a r²)^5]`. Les formules originales `rho_g`, `Psg`, `rho_f`, `Psf` ont été substituées symboliquement avec leurs dénominateurs de poussière non nuls :

`H_g/r²=0`, `H_f/r²=0` **identiquement**, indépendamment de la valeur de `U` et de `V` tant que les définitions de poussière sont appliquées. Cela ne garantit ni positivité de la poussière ni existence d'une branche globale : ces hypothèses proviennent des certificats antérieurs Step54/55.

La définition originale `Psg=(s Dbar+Lg Gprime−rho_g s KG Lg)/Sgr` impose exactement `D_g=r³ Dbar`, avec `s=r²`. Puis `Dbar=k z1/sqrt(1−s z1²)` et `K=r² k`, `z=r z1` donnent **`F_z=D_g−K z/sqrt(1−z²)=0`** sur `r>0`, `k>0`, `|z|<1`. Le signe de la racine et la non-nullité des dénominateurs sont indispensables.

## 3. Secondaire C et prolongations

Step46 (déjà démontré) donne `C=C0+C1 V`, `V=pLf'`, avec `C1 ≠ 0` sur la charte régulière. Step55 définit `G(s,U)=V_rhs/r`, `V_rhs=−C0/C1`, et la branche physique satisfait `2s U_s=G−2U`. Pour `pLf=r² U(r²)` :

`pLf'=r(2U+2s U_s)=rG=V_rhs`, donc **`C=0`** exactement sur la solution de l'EDO, pas pour une boîte `U` arbitraire. Un contrôle négatif `U_s→U_s+epsilon` produit `C=2r s C1 epsilon`, généralement non nul.

Sur un **intervalle ouvert** où le profil est suffisamment régulier et ces identités sont vraies comme fonctions, `H_g'=H_f'=C'=F_z'=0` (et leurs dérivées ultérieures existantes) par dérivation de zéro. **Une annulation à des points isolés n'implique pas ces prolongations** : ce point est explicitement testé.

## 4. Composition avec les identités historiques de lapse

Les identités déjà démontrées sur `F_z=0` sont :

- Step58 : `N''` a pour coefficient `(z²−1) H_g/(Lg Lf)` et `M''` a pour coefficient zéro ;
- Step68j : `B_N=−(1−z²)/(Lg Lf) H_g'+beta H_g+(z/Lg) C` ;
- Step68h : `B_M=3z(z²−1)/(Lg Lf²) F_z'`.

La composition algébrique avec la coquille spatiale régulière et ses prolongations annule **les quatre coefficients de `N'',M'',N',M'`**. Le contrôle négatif `H_g=C=0` avec `H_g'≠0` donne `B_N=−alpha H_g'≠0` : les prolongations ne peuvent pas être omises.

Il reste **`dot C_red = A_N N + A_M M` au niveau de ce noyau sphérique local**, sous toutes les hypothèses de charte, sans garantie de signe continu des coefficients originaux Step58, de lapses admissibles, de rang Dirac, de conditions aux bords ou de théorie 4D stable.

## 5. Précaution : champs de poussière et jets locaux

Step68o utilise `tg=Jet([0,tg',tg''/2,tg'''/6])` et pareil pour `tf`. La valeur `t=0` choisie **à chaque point** est une origine locale de champ, pas une fonction globale identiquement nulle : une fonction identiquement nulle ne peut avoir une dérivée non nulle. Leurs jets sont néanmoins intégrables. Pour `L=a(1+c r²)²` et `t'=k r L`, un champ global admissible (à constante additive près) est

`t(r)=ka(r²/2+c r⁴/2+c² r⁶/6)+const`.

Les jets d'ordres 1, 2 et 3 sont exactement ceux de Step68o. Les Hamiltoniens originaux Step45 ne dépendent que de `t'`, et non de l'origine additive de `t`. Ce point clarifie la **cohérence locale/globale de la représentation des poussières**, sans résoudre leur dynamique 4D.

## 6. Exécution, limites et prochaine étape

Commande réellement exécutée dans le sous-ensemble autonome :

`PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2e2_spatial_shell_closure.py`

**14 PASS, 0 FAIL**, et manifeste généré par `python -m numerics.hr_step68ad_c2d2e2_spatial_shell_closure`. Ces tests couvrent les deux réductions primaires, les deux annulations de poussière, la courbure, `D_g`, `F_z`, la composition secondaire/EDO, le contrôle négatif hors EDO, les prolongations, la composition des quatre coefficients de dérivées de lapses et les primitives des poussières. Ils **ne** sont **pas** les 36 tests historiques, qui n'ont pas été rejoués dans cette session.

**Résultat nouveau :** composition exacte, explicite et testée des conditions du profil Step68o avec les identités de lapse antérieures ; clarification de l'origine locale des champs de poussière. **Pas de nouveau signe temporel certifié.** Le calcul n'exécute pas les modules originaux Step58/60 et ne valide pas JANUS.

**Prochaine étape effective : `68ad-C2d2e3`** : obtenir des enclosures corrélées rigoureuses des **deux coefficients originaux** `A_N,A_M` Step58 sur les sept cellules continues, puis résoudre ou réfuter l'équation de lapses avec rang de Dirac, conditions aux bords et chartes singulières. Vérifier indépendamment la chaîne complète de contraintes dans le vrai moteur si un environnement de sources authentifiées redevient disponible.

**Verdict : `GATE_2B OPEN` ; `JANUS_R NOT_VALIDATED`.**
