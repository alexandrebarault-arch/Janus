# JANUS — Étape 56 : réponse fonctionnelle du déplacement relatif et premier verrou de Dirac temporel

**23 octobre 2026. Branche exclusivement autorisée :** `research/gate2b-nonhomothetic-transfer`. **Gate 2B OUVERT. JANUS-R NON VALIDÉ.** Cette étape ne prétend pas calculer le crochet temporel complet : elle dérive et vérifie un opérateur qu'il serait incorrect d'omettre de ce calcul.

## 1. Résultat mathématique exact et provenance de l'action

Partant des expressions publiées dans l'original sphérique ADM/HR à **deux termes Einstein–Hilbert positifs, deux poussières mobiles et six couples canoniques**, l'équation algébrique de stationnarité du déplacement relatif est :

[
F_z=D_g-rac{Kz}{sqrt{1-z^2}}=0,qquad
D_g=p_{S_g}S_g'-L_g p_{L_g}'+p_g	heta_g',
]
[
K=m^2M_g^2 L_g L_f
(eta_1S_g^2+2eta_2S_gS_f+eta_3S_f^2).
]

Les sources historiques exactes auxquelles ces expressions correspondent sont :

- `numerics/hr_step45_exact_physical_ward.py` — blob Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
- `numerics/hr_step46_exact_secondary_ode.py` — blob Git `bac025c28dbe1561c0c36c56dbfda46dc326f804`.

Dans la charte (K>0), (|z|<1), la racine carrée positive donne la solution **unique** :

[
oxed{z=rac{D_g}{sqrt{D_g^2+K^2}}.}
]

Sa différentielle de Fréchet canonique est exactement :

[
oxed{delta z=
rac{K^2}{(D_g^2+K^2)^{3/2}},delta D_g
-rac{D_gK}{(D_g^2+K^2)^{3/2}},delta K.}
]

Les variations de chacune des expressions sont :

[
delta D_g=S_g'delta p_{S_g}+p_{S_g}delta S_g'
-p_{L_g}'delta L_g-L_gdelta p_{L_g}'
+	heta_g'delta p_g+p_gdelta	heta_g',
]

[
delta K=m^2M_g^2left[
L_fA_tdelta L_g+L_gA_tdelta L_f+
2L_gL_fleft(
(eta_1S_g+eta_2S_f)delta S_g+
(eta_2S_g+eta_3S_f)delta S_f
ight)ight],
]

où (A_t=eta_1S_g^2+2eta_2S_gS_f+eta_3S_f^2).

Le code nouveau `numerics/hr_step56_shift_response.py` vérifie ces identités exactement dans SymPy, **sans différences numériques**. Il démontre aussi (delta(z')=(delta z)') si l'on conserve les jets de champs, y compris les variations des dérivées.

## 2. Pourquoi ceci est nécessaire au véritable crochet temporel

Pour (Z_D=partial z/partial D_g=K^2/(D_g^2+K^2)^{3/2}), la dépendance (D_gsupset-L_g p_{L_g}') donne le noyau distributionnel non nul :

[
rac{delta z(r)}{delta p_{L_g}(x)}
=-L_g(r)Z_D(r),partial_rdelta(r-x).
]

Par conséquent, pour une fonction test compacte (eta), on a EXACTEMENT :

[
oxed{
rac{delta}{delta p_{L_g}(x)}
int dr,eta(r)z(r)
=partial_xigl[eta(x)L_g(x)Z_D(x)igr].}
]

Cette variation comporte nécessairement la dérivée de la fonction test (et, selon le crochet considéré, du lapse). **Sur un intervalle sans support compact**, l'intégration par parties produit en outre le bord (-[eta L_gZ_D,delta p_{L_g}]) qui doit être conservé ou soumis à des conditions explicites.

On vérifie également l'identité d'« enveloppe stationnaire » pour la partie dépendant de (z) des Hamiltoniens primaires originaux :

[
partial_zigl(NH_g+MH_figr)
=left(rac{N}{L_g}+rac{M}{L_f}ight)F_z=0
quad	ext{lorsque }F_z=0.
]

Ainsi, **la variation du Hamiltonien réduit** peut utiliser la dérivée à (z) fixé sur cette surface ; cela **n'autorise pas** à figer (z) dans la variation de la contrainte secondaire réduite (C_{m red}). Celle-ci exige la dérivée de chaîne en (z,z') et, si présents, dans les jets spatiaux supérieurs.

La préservation temporelle de **la stationnarité algébrique du déplacement** se traduit par l'identité exacte

[
oxed{
dot z=rac{K^2dot D_g-D_gKdot K}
{(D_g^2+K^2)^{3/2}}.
}
]

Cette équation suit de (dot F_z=0), mais **elle ne constitue pas** le calcul de (dot C), du rapport des lapses ou du rang de la matrice de Dirac.

Un banc d'essai symbolique distinct, utilisant exactement **six couples canoniques** mais **pas les Hamiltoniens JANUS**, démontre que ({C(z(q,p)),H}) diffère d'un calcul artificiellement réalisé à (z) fixé, par le terme (C_z{z,H}), effectivement non nul dans ce banc d'essai. **Ce test prouve la nécessité de la méthode, pas une propriété de fantôme de JANUS.**

## 3. Réponse régulière normalisée au centre

La précédente étape 55 a établi (K/r^2=k(s)>0.229) sur le secteur radial prescrit, (s=r^2in[0,0.7225]). Avec (D_g=r^3d(s)), l'équation de stationnarité devient

[
w(s)=rac{z}{r}=rac{d(s)}{sqrt{k(s)^2+s d(s)^2}}.
]

Pour le fond prescrit (z=z_1r), (z_1=0.004), on obtient (d=kz_1/sqrt{1-sz_1^2}). La différentiation exacte donne :

[
rac{partial w}{partial d}=rac{(1-sz_1^2)^{3/2}}{k},qquad
rac{partial w}{partial k}=-rac{z_1(1-sz_1^2)}{k}.
]

Par les **inégalités rationnelles strictes** antérieures (k>229/1000) et (0<1-sz_1^2le1) :

[
oxed{
0<partial_dw<1000/229<4.367,qquad
|partial_kw|<4/229<0.0175.
}
]

Ainsi la réponse linéaire **normalisée** du déplacement reste finie au centre de ce secteur, même si les dérivées non normalisées en (D_g,K) présentent les facteurs attendus de puissance radiale. Ces bornes de sensibilité ne sont **pas** un théorème de régularité 4D en temps.

## 4. Reproductibilité réelle, sans affirmation excessive

Les **14 tests ciblés** ont été réellement exécutés :

```bash
cd /mnt/data/janus-step56
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step56_shift_response.py
# 14 PASSED en 2.00 secondes.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step56_shift_response
```

**Les deux nouveaux fichiers GitHub sont byte-identiques aux versions locales exécutées** :

- `numerics/hr_step56_shift_response.py` — Git blob `71bc56d3433e146c5671351e6ea21468ee5149ca`.
- `tests/test_hr_step56_shift_response.py` — Git blob `75efdc7b99af067f3f7c2b1bc4947cb5a7c9e48f`.

Les 14 tests portent sur : élimination algébrique unique pour (K>0), dérivées de (z(D_g,K)), variation de tous les champs et jets de (D_g,K), commutation (delta(z')=(delta z)'), dérivation de la fonction test dans la variation intégrée, présence du terme de bord, règle de l'enveloppe sur (F_z=0), conséquence (dot F_z=0), normalisation et bornes rationnelles au centre, perte de détermination de (z) à (D_g=K=0), contre-exemple à six couples, et refus explicite de prétendre le Dirac complet déjà résolu.

**Limite de provenance :** le programme est une **reconstruction symbolique autonome** des formules de stationnarité **lues dans les fichiers historiques GitHub authentiques**, il n'a pas importé leurs octets originaux dans son exécution locale. Ne pas décrire ces 14 tests comme une régression de toute la chaîne historique Step45–55, ni comme calcul original complet de ({C,H_{m total}}). Les tests de source exacte des tours précédents sont conservés séparément. Pas de GitHub Actions ni suite complète du dépôt.

Le manifeste brut local `/mnt/data/janus-step56/research/reports/step56_shift_local.json`, SHA256 `7541d626330d4cc8589bbc264ede472b8b81b1a92efdf054bf97fbcf29f3341e`, a été réellement créé, mais pas uploadé indépendamment ; les formules et résultats sont enregistrés dans `research/reports/gate2b-step56-report.json`.

## 5. Prochaine étape 57 — ce qui reste impérativement à calculer

1. **Importer les vraies expressions originales intégrales** (H_g,H_f,C_{m exact}) et les douze champs canoniques, ainsi que (z[D_g,K]) et ses dérivées spatiales, dans une implémentation fonctionnelle de la **préservation temporelle**. Utiliser les équations canoniques sur les **six couples**, y compris les poussières, pas seulement la sous-famille (D_g,K).
2. Calculer le crochet (dot C_{m red}={C_{m red},H_{m total,red}}), en gardant (delta z,delta z',ldots) dans (C_{m red}), et appliquer l'identité d'enveloppe au Hamiltonien sur (F_z=0) sans compter deux fois ses contributions ; contrôler les dérivées des lapses et les termes de bord. **Ce calcul n'a pas encore été exécuté.**
3. Évaluer ensuite la matrice des multiplicateurs, les contraintes secondaires/tertiaires éventuelles, son rang et la fixation (ou obstruction) du rapport des lapses sur la branche radiale positive Step55, les secteurs exceptionnels (J,K=0) à part. Confronter à un calculateur non intégré par parties de l'action originale.
4. Conserver et relire en priorité `00_CURRENT_RESTART.md` sur la branche active, déposer code, tests et rapport, ne pas réactiver Actions.

**STATUT FINAL : un terme canonique distributionnel indispensable au Dirac temporel est dérivé et vérifié. FULL DIRAC/TIME PRESERVATION, RANG ET LAPSUS TOUJOURS OUVERTS. GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

**Branches GitHub :** les anciens commits `main` et `research/v2-flrw` sont déjà protégés dans l'ascendance de la branche active grâce au commit `4f7a3a1`, PR historique #1 fermée sans fusion. Toujours **trois refs GitHub visibles** et `main` comme défaut ; le connecteur n'offre pas la modification de branche par défaut ni la suppression des refs, qui nécessitent l'interface du propriétaire.
