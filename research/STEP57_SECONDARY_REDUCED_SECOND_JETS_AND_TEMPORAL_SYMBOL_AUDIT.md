# JANUS — Étape 57 : seconde dérivée spatiale de la secondaire réduite et premier symbole physique du crochet de Dirac temporel

**23 octobre 2026 — branche `research/gate2b-nonhomothetic-transfer`.** Calcul exact sur les vrais coefficients de la formulation sphérique ADM positive-EH + Hassan–Rosen + deux poussières, SIX couples canoniques, fournis par la **source originale octet-identique** `numerics/hr_step45_exact_physical_ward.py` (Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`). **Gate 2B OUVERT ; JANUS-R NON VALIDÉ.** Le crochet temporel complet et le rang de Dirac restent à calculer.

## 1. Résultat inédit, exactement dérivé de la vraie secondaire

L'original Step45 donne `C_exact=K00-∂rK01`, construit à partir des gradients d'Euler de l'action sur TOUS les six couples, pour un déplacement `z` tenu externe dans la PREMIÈRE variation. Cette expression dépend de `(q,q',z,z')`, mais ne contient AUCUN `q''` canonique explicite.

Écrivons les densités exactes de l'action :

\[
D_g=p_{S_g}S'_g-L_g p'_{L_g}+p_g\theta'_g,\qquad
K=m^2M_g^2 L_gL_f(\beta_1S_g^2+2\beta_2S_gS_f+\beta_3S_f^2),
\quad F_z=D_g-\frac{Kz}{\sqrt{1-z^2}}.
\]

**Identité symbolique EXACTE**, dérivée dans SymPy directement de `C_exact` original, sans différences numériques ni données manufacturées :

\[
\boxed{
\frac{\partial C_{\rm exact}}{\partial z'}
=-\frac{K\sqrt{1-z^2}+D_g z}{L_gL_f}
=-\frac{K}{L_gL_f\sqrt{1-z^2}}-\frac{zF_z}{L_gL_f}.
}
\]

La dépendance en `z'` est AFFINE et son coefficient n'est PAS nul. Sur la charte `K>0`, `R=\sqrt{D_g^2+K^2}>0`, `F_z=0`, on élimine EXACTEMENT :

\[
z=D_g/R,\quad \sqrt{1-z^2}=K/R,
\quad\boxed{\left.C_{z'}\right|_{F_z=0}=-\frac{R}{L_gL_f}.}
\]

Mais `D_g` contient `-L_g p'_{L_g}`, `p_{S_g}S'_g` et `p_g\theta'_g`. En remplaçant correctement `z'=d[z(D_g,K)]/dr` dans la secondaire, on introduit des champs **DÉRIVÉS DEUX FOIS**. Les trois seuls coefficients de dérivée seconde canoniques non nuls deviennent :

\[
\boxed{\begin{aligned}
\frac{\partial C_{\rm red}}{\partial p''_{L_g}}
&=\frac{K^2}{L_fR^2}=\frac{1-z^2}{L_f},\\
\frac{\partial C_{\rm red}}{\partial S''_g}
&=-\frac{p_{S_g}K^2}{L_gL_fR^2},\\
\frac{\partial C_{\rm red}}{\partial\theta''_g}
&=-\frac{p_gK^2}{L_gL_fR^2}.
\end{aligned}}
\]

Les NEUF autres dérivées secondes des 12 champs canoniques sont absentes. Ce constat est un résultat **algébrique pour le représentant précis de la secondaire Step45** sur `F_z=0, K>0`. Il ne prouve pas, à lui seul, que d'autres choix de représentants modulo contraintes aient exactement la même forme.

## 2. Variation fonctionnelle correcte et fonction test `eta''`

Pour un champ canonique arbitraire `u` et une fonction test compacte `eta`, poser `Z=Z(q,q')` et `C=C(q,q',z,z')` AVANT élimination de `z`. Notant `D=∂r` la **dérivée totale sur les jets** et tous les indices de `C` les dérivées partielles à `z,z'` fixés, on obtient l'identité exacte :

\[
\begin{aligned}
T_\eta &=\eta\,C_z-D(\eta\,C_{z'}),\\
\boxed{
\mathcal E_u[\eta C_{\rm red}]
=\eta C_u-D(\eta C_{u'})
+ Z_u T_\eta-D(Z_{u'}T_\eta).
}
\end{aligned}
\]

Cette formule contient jusqu'à `eta''` ! Son coefficient est EXACTEMENT `Z_{u'}C_{z'} = \partial C_{\rm red}/\partial u''`, ce qui manque à une variation artificielle qui fige `z`. Le module calcule également les coefficients complets de `eta^0, eta^1, eta^2` en tant que **formules abstraites**, et une vérification indépendante les compare à l'Euler d'ordre deux explicitement différentié sur un problème non trivial couplant deux champs. Toutes les différences symboliques sont ZERO.

Il faut encore substituer ces coefficients abstraits à TOUS les douze champs physiques et les contracter contre les Hamiltoniens réels pour les dérivées `eta^0` et `eta^1`. Cette opération est précisément la prochaine étape 58.

## 3. Un terme EXACT du véritable crochet physique à SIX couples

L'original Step45 donne les six gradients d'Euler du Hamiltonien `H[N,M]` pour les six couples canoniques. Grâce à l'enveloppe `F_z=0` déjà établie Step56, la PREMIÈRE variation de `H_{\rm red}` emploie les gradients à `z` externe, et la variation de `C_{\rm red}` emploie TOUTE la dérivée de chaîne précédente. La contraction Poisson réelle du terme en `eta''` vaut

\[
C_{z'}\,Z_{D_g}\left(
L_g\mathcal E_{L_g}H
+p_{S_g}\mathcal E_{p_{S_g}}H
+p_g\mathcal E_{p_g}H\right),
\qquad Z_{D_g}=\frac{K^2}{R^3}.
\]

**Identités EXACTES des vrais jets hamiltoniens Step45** (pour N et M, jusqu'à leur deuxième dérivée) :

\[
\begin{array}{ll}
T_{N'}=2M_g^2S_gS'_g/L_g, & T_{N''}=0,\\
T_M=(K\sqrt{1-z^2}+D_gz)/L_f=R/L_f \quad (F_z=0),\\
T_{M'}=0, &T_{M''}=0.
\end{array}
\]

Le coefficient de `eta'' M`, c'est-à-dire le terme `eta''(r)M(r)` de l'intégrande du crochet `{∫eta C_red,H[N,M]}`, est ainsi démontré **NON NUL** :

\[
\boxed{\Gamma_{\eta''M}
=-\frac{K^2}{L_g L_f^2 R}
\quad (K,L_g,L_f,R>0).}
\]

Le coefficient de `eta'' N'` est lui aussi explicitement :

\[
\boxed{\Gamma_{\eta''N'}
=-\frac{2M_g^2 S_gS'_g K^2}{L_g^2 L_f R^2}.}
\]

Les coefficients `eta''N''`, `eta''M'`, `eta''M''` sont exactement nuls, tandis que `eta''N` reste stocké sous forme symbolique sans simplification terminale.

**Attention essentielle :** un terme non nul dans l'intégrande AVANT intégrations par parties ne prouve PAS un multiplicateur de lapse non nul dans l'opérateur FINAL. Les parties venant de `eta'` et `eta` peuvent contribuer aux mêmes dérivées après adjoint formel. Il serait faux de déclarer ici une fixation des lapses, un rang de Dirac ou l'absence du fantôme de Boulware–Deser.

## 4. Exécution, source authentique, artefacts et tests

Fichier original authentifié localement avec `git hash-object` : `numerics/hr_step45_exact_physical_ward.py`, blob **`66aa43841dccfe4a5d586a49be9c10af3a67a10e`**, puis **importé effectivement** dans le nouveau calcul physique ; le module refuse toute modification de ses octets. Cela améliore la provenance de l'étape 56, qui reconstruisait les formules sans importer l'original.

Nouveaux fichiers publiés et byte-identiques au code exécuté :

- `numerics/hr_step57_secondary_principal_symbol.py` — `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`.
- `tests/test_hr_step57_secondary_principal_symbol.py` — `1c97b1764ef4180deec48da8c68e138ed59b254a`.

Exécution **réelle** dans l'environnement isolé `/mnt/data/janus-step57` :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step57_secondary_principal_symbol.py
# 12 PASSED in 1.62s

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step57_secondary_principal_symbol
# Manifest step57, full temporal and rank still NOT COMPUTED.
```

Un test était initialement FAUX en raison d'un simple facteur 2 dans sa valeur numérique attendue (`-9/160` au lieu de `-9/320` pour `K=3/2,R=5/2,Lg=2,Lf=4`). Le test a été CORRIGÉ, puis **TOUS** les 12 tests ont été exécutés avec succès, et SEULE cette version corrigée a été enregistrée sur GitHub. Le manifeste JSON local complet est reproductible, SHA256 `d69b2245e37eb5057dd96bebe325cc6f3869166d16d83a88b0607a6c66198af3` ; il n'est PAS enregistré comme fichier GitHub indépendant. Résultats scientifiques essentiels dans `research/reports/gate2b-step57-report.json`.

Ce n'est PAS la suite de tests entière du dépôt et ne comprend pas la réexécution des étapes 47–56. GitHub Actions/workflows restent volontairement désactivés.

## 5. Verrous impératifs à partir de l'étape 58

1. **Contraction TEMPORELLE COMPLÈTE :** calculer les termes physiques `eta^0` et `eta^1` à partir de `abstract_pullback_coefficients` sur CHAQUE champ canonique ; inclure TOUTES les dérivées des jets de `z=z(D_g,K)`, `z'`, et les vraies variations d'Euler de `H[N,M]` Step45. Intégrer les dérivées de `eta` par parties et contrôler explicitement les bords.
2. **Rang / lapses :** calculer les coefficients réellement survivants de l'opérateur différentiel sur `N,M`, et ses rangs sur les données EXACTEMENT contraintes et positives certifiées Step55. Ne pas déduire un rang d'un symbole partiel.
3. **Oracle externe :** comparer au crochet original non-IBP sur des données qui satisfont la secondaire exactement, au besoin via jets/AD plutôt que différences finies. Traiter la charte `K=0` séparément.
4. Continuer à préfixer le point de reprise GitHub **`00_CURRENT_RESTART.md`** ; ne jamais écraser les étapes précédentes, ne pas modifier `main`/V2.

**BILAN : la secondaire réduite de la VRAIE action JANUS possède trois dérivées secondes canoniques non nulles ; le premier symbole temporel à six couples est analytique et audité. Préservation complète, rank et fixation des lapses NON CALCULÉS. Gate 2B OPEN ; JANUS-R NOT VALIDATED.**
