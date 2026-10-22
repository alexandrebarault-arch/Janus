# JANUS — Étape 52 : coefficient central U1 **exactement algébrique** (et non plus extrapolé)

**Date : 22 octobre 2026 — branche EXCLUSIVE : `research/gate2b-nonhomothetic-transfer`.** **Gate 2B OUVERT. JANUS-R NON VALIDÉ.** La validation temporelle de Dirac et les degrés de liberté physiques demeurent totalement à établir.

## 1. Le verrou précis levé par cette étape

L'étape 48 avait trouvé la condition centrale nécessaire pour le profil sphérique régulier (p_{L_f}=r^2 U(s)), (s=r^2),
[
U_0=M_f^2 bleft(rac{P_g}{M_g^2 a}-2z_1ight).
]
L'étape 49 avait établi, sous les hypothèses analytiques et de charte régulière, l'existence/unicité **locale** d'une solution secondaire (C=0) au centre, avec
[
2s,partial_s U=G(s,U)-2U,qquad
G(0,U)=3U_0-U,qquad U_1=rac15,partial_sG(0,U_0).
]
L'étape 51 avait seulement estimé (U_1) en calculant numériquement (G) à (r=10^{-k}) avec `mpmath` jusqu'à 120 chiffres. **L'étape 52 établit le coefficient (U_1) exactement, dans la calibration rationnelle explicite.**

## 2. Construction mathématique reproductible — corps quadratique et jets

Le programme `numerics/hr_step52_exact_center_taylor.py` importe **les sources historiques Step45/46 exactes** de l'action sphérique ADM + interaction Hassan–Rosen + **deux poussières**. Il vérifie **en refusant tout écart** leurs blobs GitHub :
- `numerics/hr_step45_exact_physical_ward.py` : `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
- `numerics/hr_step46_exact_secondary_ode.py` : `bac025c28dbe1561c0c36c56dbfda46dc326f804`.

Leurs équations fournissent exactement la contrainte secondaire analytique `C=K00-(K01)'`, puis, sur les deux primaires f, le second membre `pLf_prime_rhs=-C0/C1`.

Tous les paramètres de référence sont lus comme **rationnels décimaux terminants**. Le facteur d'expansion central (H) est la racine **positive** d'un rationnel calculé depuis l'équation de Friedmann de la calibration :
[
H^2=rac{1111887094969374384953162712427069073394495655204338071814597909773}
 {195312500000000000000000000000000000000000000000000000000000000000}.
]

Les champs radiaux (L_g,L_f,S_g,S_f,p_{L_g},	heta'_g,	heta'_f,z), leur dérivée canonique nécessaire, (p_g,p_{S_g}) reconstruits à partir des vraies contraintes primaires g et les potentiels (D_g,W_f,R_f) sont construits directement en séries de Laurent exactes à coefficients dans (mathbb Q(H)), (H^2inmathbb Q). Aucun coefficient n'est arrondi en binaire. La multiplication est effectuée par convolution ; la division par récurrence exacte des coefficients de série ; les racines spatiales/dust sont développées par récurrence de Taylor autour de leur valeur centrale **positive égale à 1**. Toute opération conserve une borne conservative du premier ordre inconnu de la série, y compris lorsqu'il existe des puissances négatives intermédiaires de (r).

La formule physique symbolique de `pLf_prime_rhs` (environ **125 nœuds distincts** après partage des sous-expressions) est évaluée par ces jets **sans différences finies, limites numériques ni extrapolation de petit rayon**. Pour (p_{L_f}=U_0r^2), on vérifie exactement :
[
p'_{L_f}ig|_{U=U_0}=2U_0r+c_3r^3+O(r^5),
quad c_3inmathbb Q(H),
]
et, du fait de (partial_U G(0,U_0)=-1), la solution régulière a précisément (U_1=c_3/5) (et non (c_3/4), car le second membre est évalué en gelant (U=U_0)).

Les jets d'ordre **14, 20 et 26** donnent les **MÊMES FRACTIONS exactes** pour les deux coefficients algébriques de (U_1), sans comparaison flottante. La borne conservative des premiers termes inconnus de `pLf_prime_rhs` n'apparaît qu'à (r^9,r^{15},r^{21}) respectivement, strictement après le coefficient (r^3) visé. Les coefficients (r^0,r^2,r^4) sont exactement nuls et le coefficient (r^1=2U_0) est exact, offrant des contrôles structurels.

## 3. Résultat algébrique exact et certificat de signe rationnel

Le résultat est de la forme exacte
[
oxed{U_1=A+Bsqrt{H^2}},qquad A,Binmathbb Q,quad H>0.
]

**Les trois fractions exactes (A), (B) et (H^2) sont enregistrées in extenso** dans `research/reports/gate2b-step52-report.json`, sans perte de chiffres. Leur longueur rend peu pertinente leur copie dans ce texte. L'évaluation décimale d'affichage est :
[
U_1simeq0.0007897451667202464909325108904961683602148118201690678340070842162469409899ldots
]

La borne du radical utilise **uniquement des entiers** : (L=lfloor 10^{90}sqrt{H^2}floor/10^{90}), calculé par `isqrt(floor(H²*10^180))`; les inégalités rationnelles (L^2le H^2le(L+10^{-90})^2) sont vérifiées, puis propagées exactement par les fractions (A,B), avec changement de sens si (B<0). Le certificat résultant a une largeur d'environ (8.3067	imes10^{-96}), nécessairement plus petite que (10^{-80}). En bornes **décimales rationnelles strictes** lisibles :
[
oxed{
0.0007897451667202464909325108904961683602148118201690
<U_1<
0.0007897451667202464909325108904961683602148118201692.
}
]

La précédente valeur Step51 issue de Richardson à rayons (10^{-10},10^{-11}) diffère d'environ (6.6	imes10^{-50}), cohérente avec un reste d'extrapolation à échelle finie. La nouvelle valeur est **certifiée dans le modèle à constantes rationnelles déclarées**. Cela ne certifie pas la sémantique des anciens calculs flottants Step33g exécutés avec des arrondis intermédiaires.

## 4. Tests **effectivement exécutés** et empreintes GitHub

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step52_exact_center_taylor.py
# EFFECTIVEMENT : 8 PASSED in 11.01 seconds.

# Vérifie A,B et borne des restes à 3 ordres dans 3 processus distincts :
for order in 14 20 26; do
  JANUS_JET_ORDER=$order OPENBLAS_NUM_THREADS=1 PYTHONPATH=. \
    python -m numerics.hr_step52_exact_center_taylor
done
```

- `numerics/hr_step52_exact_center_taylor.py` — Git blob `b7da7e5272e08819fc89053fdf15852fcf4cc536` ;
- `tests/test_hr_step52_exact_center_taylor.py` — Git blob `cf9416641583de47ab0d60f4527bca7ce60d2806`.

Les deux fichiers NEW sont **octet pour octet identiques** aux sources et tests exécutés dans `/mnt/data/janus-step52`, et les deux providers Step45/46 historiques également. Les huit tests comprennent : tests de SHA historique et leur échec forcé en cas de dérive, identité dans le corps quadratique, coefficients centraux requis, borne par `Fraction`/racine rationnelle, accord avec un oracle numérique haute précision Step51 et comparaison EXACTE de (A,B) à trois ordres séparés.

Le JSON brut de l'ordre 20 a effectivement été généré dans `/mnt/data/janus-step52/research/reports/step52-u1-jet-20.json`, SHA-256 `069191a6e92c7474677c3b5a004de0affba94c1ede63f1debfe253d09d3fca6f`. Ce JSON brut local n'a PAS été uploadé comme fichier séparé, mais ses fractions algébriques et bornes essentielles sont dans le rapport machine GitHub. Ce sont des tests ciblés, **pas la suite intégrale du dépôt** ; GitHub Actions restent désactivées.

## 5. Limites scientifiques toujours bloquantes

L'exactitude de ce **coefficient local d'une solution régulière** ne démontre en rien :
- la continuation exacte et sans singularité de la solution (U(s)) du centre jusqu'à (r=.85) ;
- l'existence d'une borne d'erreur validée pour les solutions numériques sur cet intervalle ;
- la positivité **continue** des deux densités de poussières le long de la nouvelle solution non polynomiale ou la non-dégénérescence de tous les facteurs de chartes (J/K) ;
- le crochet secondaire **TEMPOREL** ({C,H_{m tot}}) pour l'ensemble des SIX couples canoniques, la fixation des lapses, le rang des contraintes et l'absence éventuelle du fantôme Boulware–Deser ;
- une cosmologie réellement non homothétique **sur les équations d'évolution** avec contrôles de perturbations De Felice/Aoki ou une adéquation empirique.

Les anciens deux imports Step33g `hr_curved_moving_dust_primary.py` et `hr_curved_primary_mixed_kernel.py` n'ont pas encore été réunis **dans le même checkout** que l'ensemble des sources de tests Step45–48 ; cette tâche de reproductibilité intégrale reste dans le backlog. Une reproduction fidèle mathématique ne doit pas être appelée clonage byte-identical.

## 6. Branches Git — l'autre demande encore administrative

L'histoire de `main` et de `research/v2-flrw` est conservée dans l'ascendance de `research/gate2b-nonhomothetic-transfer` grâce au commit de préservation `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7` à arbre inchangé. L'ancienne PR #1 est fermée **sans fusion**. **Trois refs sont encore visibles** et `main` reste la branche GitHub par défaut. Ce connecteur ne propose ni suppression de branche ni changement du défaut : cette étape nécessite toujours la modification de la branche par défaut dans GitHub UI, suivie des suppressions de V2 et de main. Ne pas supprimer l'arbre scientifique des anciennes branches comme ersatz de suppression de refs.

## 7. NEXT STEP53 — plan autonome pour reprendre après interruption

1. Incorporer le **vrai coefficient algébrique (U_1)** et sa borne rationnelle au tir régulier depuis le centre ; poursuivre les séries exactes pour (U_2) en gardant le contrôle des puissances de Laurent, puis vérifier leur influence sur le raccordement et le signe des poussières.
2. Remplacer les deux imports Step33g complémentaires par leurs **octets historiques authentiques** et relancer intégralement la suite Step48/49/51/52, pas seulement les sous-tests.
3. Construire une méthode de continuation **certifiée** (EDO à intervalles ou résidu spectral + borne a posteriori) sur ([0,.85]), avec preuve stricte de (p_g/r^2,p_f/r^2,J,K/r^2>0) et contrôle du centre/bord.
4. Calculer la véritable préservation temporelle ({C,H_{m tot}}), la fixation du rapport des lapses et le rang de la matrice de Dirac. Ce verrou est **non négociable avant toute affirmation de modèle sain/ghost-free**.
5. Conserver le fichier `00_CURRENT_RESTART.md` à jour sur la branche active après chaque résultat ; ne modifier ni anciennes refs ni CI. Si le propriétaire termine le ménage GitHub, recontrôler d'abord les noms de branches distants.

**VERDICT STEP52 : le coefficient (U_1) de la branche centrale régulière est désormais exactement algébrique, avec certificat rationnel strict, pour l'étalonnage déclaré. VALIDATION GLOBALE/DIRAC TOUJOURS OUVERTE. GATE_2B=OPEN ; JANUS-R NON VALIDÉ.**
