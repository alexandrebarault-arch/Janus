# JANUS — Étape 68d : formule exacte du shift hamiltonien et origine de l'annulation des dérivées secondes des lapses

**25 octobre 2026. Branche de recherche unique :** `research/gate2b-nonhomothetic-transfer`. **Gate 2B ouvert ; JANUS-R non validé.** Ce résultat concerne le secteur positif `K>0`, `F_z=0` et, pour l'annulation finale de `N''`, la primaire `H_g=0`.

## 1. Provenance physique authentique

Cette fois, les **TROIS originaux GitHub** ont été reconstitués octet pour octet et **exécutés dans un même runtime** :

| Module | Git blob SHA-1 vérifié |
|---|---|
| `numerics/hr_step45_exact_physical_ward.py` | `66aa43841dccfe4a5d586a49be9c10af3a67a10e` |
| `numerics/hr_step57_secondary_principal_symbol.py` | `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f` |
| `numerics/hr_step58_temporal_operator.py` | `802c23aebd41780d8c462f1aa1711707fe4ee88f` |

Les 12 coordonnées des six couples (gravitations et deux poussières) sont conservées. Le programme `hr_step68d_exact_shift_lapse_symbol.py` vérifie lui-même les trois Git blobs, appelle l'original `physical_operator()` et le certificat original `highest_lapse_certificate()`, ainsi que `physical_principal_symbol()` pour le test. Toute mutation des trois originaux est explicitement refusée par un contrôle négatif.

## 2. NOUVELLE simplification algébrique de l'opérateur ORIGINAL (pas un noyau fabriqué)

Notons \(\mathcal Z_N^{(1)}\) et \(\mathcal Z_M^{(1)}\) les coefficients multiplicatifs respectifs de `N'` et `M'` dans la variation \(\delta_H z\), pas dans la secondaire \(\dot C\). Sur l'équation de stationnarité originale

\[
F_z=D_g-\frac{Kz}{\sqrt{1-z^2}}=0,\qquad K>0
\]

et sans encore imposer `H_g=0`, la réduction symbolique **exacte** des longues expressions des 12 champs de l'original Step58 donne

\[
\boxed{\mathcal Z_N^{(1)}=
\frac{(1-z^2)^{3/2}}{K}\,H_g-\frac{1-z^2}{L_g}},
\qquad
\boxed{\mathcal Z_M^{(1)}=\frac{1-z^2}{L_f}}.
\]

Le signe de chacun des termes est vérifié par `SymPy factor/cancel`, sur le vrai `F_z=0` où `p'_{L_g}` a été éliminé, mais où `H_g` demeure **indépendant**. Il ne s'agit donc pas d'une identité imposée en mettant la primaire à zéro pour la fabriquer.

C'est le lien direct recherché entre le **déplacement relatif dynamique** de Step68c et l'opérateur de Dirac temporel **complet** Step58.

## 3. Théorème de compensation, AVEC termes directs et variation du shift

L'original Step45 donne sur la même stationnarité :

\[
C_{z'}=-\frac{K}{L_gL_f\sqrt{1-z^2}}.
\]

Les contributions aux dérivées secondes des lapses dans \(\dot C\) se décomposent de manière exacte :

| Source | Terme en `N''` | Terme en `M''` |
|---|---|---|
| Variation canonique **directe** de `C` à `z,z'` fixés | \(-K\sqrt{1-z^2}/(L_g^2L_f)\) | \(+K\sqrt{1-z^2}/(L_gL_f^2)\) |
| Variation fonctionnelle du **vrai** shift, \(C_{z'}(\delta_H z)'\) | \(- (1-z^2)H_g/(L_gL_f)+K\sqrt{1-z^2}/(L_g^2L_f)\) | \(-K\sqrt{1-z^2}/(L_gL_f^2)\) |
| **TOTAL vrai** | \(- (1-z^2)H_g/(L_gL_f)\) | **\(0\)** |

Le terme \(C_z\delta_Hz\) ne fournit pas de dérivée seconde du lapse puisque les vecteurs \(\delta_Hz\) originaux s'arrêtent à la première dérivée de chaque lapse. Les égalités ci-dessus ont été vérifiées **directement** contre les coefficients d'ordre 2 retournés par l'opérateur complet historique `physical_operator()['operator']`.

Ainsi, **sur `F_z=H_g=0`**, \([\dot C]_{N''}=[\dot C]_{M''}=0\), par une compensation de termes **non nuls individuellement**. Ne jamais faire disparaître \(\delta_Hz\) artificiellement : le test négatif `direct_Msecond != 0` montrerait alors une fausse obstruction. Cela clarifie, sans l'étendre, le résultat historique Step58.

## 4. Lien normalisé au centre avec Step68c

Supposons les jets sphériques analytiques du benchmark positif Step55, `s=r²,z=rw,Lg→a>0,Lf→b>0,K=r² k0+O(r⁴)` avec `k0>0`, et `Hg=r² h0+O(r⁴)`. La nouvelle formule d'opérateur a les limites régulières

\[
\mathcal Z_N^{(1)}(0)=\frac{h_0}{k_0}-\frac1a,\qquad
\mathcal Z_M^{(1)}(0)=\frac1b.
\]

Pour des lapses sphériques pairs `N=N0+N2r²+...`, `M=M0+M2r²+...`, **la contribution des seules voies `N'` et `M'`** aux coefficients de \(\delta_H z'(0)\) associés à `N2,M2` vaut \(2h_0/k_0-2/a\) et \(2/b\). Sur la primaire `H_g=0` cela devient \(-2/a\) et \(2/b\). Ces valeurs correspondent au **résultat complet obtenu indépendamment par le véritable noyau Step45 à l'étape 68c**. Le programme Step68d contrôle ici la voie `N',M'`, et **ne prétend pas redémontrer** que la voie `N,M` n'apporte rien au centre : voir Step68c pour cette vérification.

Une vérification rationnelle isolée sur les constantes décimales publiées dans Step55 donne `k0>229/1000`. Le **vrai module Step55 et son certificat global de 256 cellules n'ont PAS été réimportés** durant cette étape.

## 5. Exécution et sauvegarde vérifiées

Commande réellement exécutée :

```bash
cd /mnt/data/janus-step68d
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. \
  pytest -q tests/test_hr_step68d_exact_shift_lapse_symbol.py
# 16 passed in 11.01s
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. \
  python -m numerics.hr_step68d_exact_shift_lapse_symbol
```

- **Nouveau script exécuté, Git blob identique :** `numerics/hr_step68d_exact_shift_lapse_symbol.py` — `6af0322b0ba5c39ab014874455d4f380f6ea66fa`.
- **16 tests exécutés, Git blob identique :** `tests/test_hr_step68d_exact_shift_lapse_symbol.py` — `9f1b9bfef4c573fa8fa365a37bf83e4d6307684b`.
- **Rapport structuré** : `research/reports/gate2b-step68d-exact-shift-lapse-bridge.json`.
- **Manifeste brut local SHA256** : `866746017010c856db29e0f3c77ef40fabdff30070939913fd69955dd0d95625` (reproductible ; son contenu est repris dans le rapport structuré).

Tous les hachages originaux et les deux nouveaux Git blobs ont été vérifiés. Il ne s'agit ni d'une CI ni d'une suite intégrale de tests. GitHub Actions demeure désactivé.

## 6. Frontière scientifique encore OPEN et chemin exact Step68e

Cette étape a **réduit analytiquement les deux symboles de réponse de \(\delta_Hz\) aux premières dérivées des lapses** et expliqué la compensation des dérivées secondes dans \(\dot C\). Elle **ne résout pas** les quatre coefficients **d'ordre inférieur** \(A_N,B_N,A_M,B_M\) du crochet temporel sur la solution physique Step55. Elle ne calcule ni l'opérateur quotient par toutes les contraintes `Hg,Hf,Ddiag,Fz,C,Hg',C'`, ni sa condition aux bords, son noyau ou son rang, ni les chartes exceptionnelles `J=0,K=0`.

**Prochaine étape 68e :** réunir de façon authentifiée les originaux Step45/46/55/57/58/59/60/63–65 dans un environnement unique ; reproduire les tests historiques, puis substituer les véritables données `U(s)` de Step55 et leurs jets prolongés dans les coefficients `A_N,B_N,A_M,B_M`. Confronter le résultat à un oracle Poisson NON intégré par parties sur les six couples et aux conditions aux bords. Traiter `K=0,J=0` dans leurs chartes propres. Ne PAS conclure au rang de Dirac à partir de la seule disparition des dérivées secondes.

**VERDICT : GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
