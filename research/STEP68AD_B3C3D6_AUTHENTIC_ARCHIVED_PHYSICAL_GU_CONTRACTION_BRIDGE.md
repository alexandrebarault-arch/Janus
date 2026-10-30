# JANUS — b3c3d6 : raccord physique authentifié Step63 → borne d'erreur Step55 (30 octobre 2026)

**Statut : b3c3d6 PARTIELLE. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Ce raccord exploite un certificat physique **déjà publié et exécuté historiquement** ; il ne constitue **pas** un nouveau rejeu de l'EDO physique Step55 ou du moteur Step58.

## Fait physique déjà certifié, retrouvé dans le dépôt

Le rapport original `research/reports/gate2b-step63-original-interval-report.json` a été relu via le connecteur GitHub ; blob Git SHA-1 `8a6ff87fdde3efbf26fa81d20ddb2623c161c9c1`. Sa copie locale intégrale est identique octet par octet à ce blob. Il provient de l'AD d'intervalles rationnels à arrondi extérieur sur **256 cellules continues**, pour `0<=s<=289/400` et `U` dans le tube Step55 `Ustar(s)±1/10000`. Les quatre sources historiques épinglées sont Step45 `66aa4384`, Step46 `bac025c2`, Step55 normalisé `a54a6acf`, barrière Step55 `a6e70041`. Ce rapport est un résultat historique du 23/10/2026 ; **son calcul par les originaux n'a pas été réexécuté pendant cette session**.

Le rapport donne exactement :

`-2505544668941123497720438919/2500000000000000000000000000 <= G_U <= -2482092799488383772425301393/2500000000000000000000000000 < -99/100 < 0`.

La borne physique `G_U<=1` requise par le lemme de contraction précédent n'est donc **pas un verrou encore ouvert sur le tube historique** : la borne archivée est plus forte. Cela n'établit **aucune** borne sur un segment entre la solution physique et un candidat numérique qui sortirait du tube. Une preuve de confinement du candidat reste obligatoire.

## Nouveau corollaire mathématique, exact mais conditionnel sur l'approximation

Pour `2s U_s=G(s,U)-2U`, avec `s=r²`, on a `f_U=(G_U-2)/(2s)`. Si la solution exacte et une approximation `v` restent dans le **même tube certifié Step55** à chaque abscisse, et si `|v_s-f(s,v)|<=D` est certifié **continûment** sur `[ra²,rb²]`, `0<ra<rb<=17/20`, avec `|U(ra²)-v(ra²)|<=e_a`, alors `G_U<0` entraîne `f_U<=-1/s`. L'inégalité de Dini et le facteur intégrant `s` donnent, **exactement** :

`e_b <= (ra/rb)^2 e_a + (D/2)*(rb²-ra^4/rb²)`.

En utilisant la borne historique plus précise `G_U<-99/100`, `f_U<=-299/(200s)` et le facteur intégrant `s^(299/200)` donnent la variante plus forte :

`e_b <= (ra/rb)^(299/100)*e_a + (200*D/499)*(rb²-ra^(499/100)/rb^(299/100))`.

Ces deux estimations ne requièrent **pas** `Lh<1` et s'enchaînent aux quatre rayons historiques `1/4,1/2,7/10,17/20` depuis `1/100`. Le premier facteur d'amortissement initial est `1/7225` dans la variante rationnelle, contre environ `1.7023051464e-6` dans la variante forte. Ces nombres ne sont **pas** des erreurs numériques mesurées ni des certificats DOP853.

**Contrepoint indispensable :** si `v` quitte `Ustar±1/10000`, la borne `G_U` archivée ne s'applique pas automatiquement à l'intervalle entre `v` et `U` ; ni le défaut continu `D`, ni l'erreur initiale, ni le confinement du dense output DOP853 ne sont certifiés. On ne peut donc pas conclure à une enclosure des six coefficients physiques `A_N,A_M,B_N,B_M,E_N,E_M` de Step58. Le caractère physique est limité à la prémisse `G_U` déjà certifiée sur le tube.

## Exécution locale et provenance

- `numerics/hr_b3c3d6_archived_physical_gu_bridge.py` : contrôle SHA du rapport Step63, des quatre empreintes sources déclarées, des 256 cellules et du signe, puis deux estimateurs exacts.
- `tests/test_hr_b3c3d6_archived_physical_gu_bridge.py` : 15 tests, dont copie authentifiée du vrai rapport, falsifications rejetées, saturation exacte par deux EDO jouets, chaînage et gardes.
- Commande réellement exécutée : `cd /mnt/data/janus_bridge && PYTHONPATH=. python -m unittest discover -s tests -v` → **15 PASS, 0 FAIL** ; `python -m compileall -q numerics tests` → **PASS**. Tests de raccord/algèbre, **pas** d'exécution indépendante des quatre moteurs physiques.

## Prochaine étape effective, inchangée

Matérialiser et exécuter ensemble les **cinq** originaux SHA-authentifiés Step45/46/55/58 et le candidat cubique corrigé, quatre rayons, six coefficients affine/cubique et convergence ; certifier un tube numérique et le défaut continu DOP853 ainsi que l'erreur initiale ; encloser les six coefficients, résoudre le BVP positif aux deux vrais bords, puis reprendre Dirac six couples, charges, 4D, stabilité et observables. Ne pas toucher `main`, `research/v2-flrw` ni les workflows désactivés. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
