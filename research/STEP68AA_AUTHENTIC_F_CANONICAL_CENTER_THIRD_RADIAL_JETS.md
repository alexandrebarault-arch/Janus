# JANUS — STEP68aa : dérivées radiales originales du moment canonique f au centre

**25 octobre 2026.** `GATE_2B OPEN` ; `JANUS_R NOT_VALIDATED`. Écriture exclusivement sur `research/gate2b-nonhomothetic-transfer`, jamais `main` ou `research/v2-flrw`, Actions désactivées intactes.

## 1. Ce que l'étape 68aa prouve réellement

Sur **la solution radiale analytique** de Step49, assujettie à l'EDO originale Steps45/46/55, noter `s=r²` et :

```
U(s)=U0+U1*s+U2*s²+U3*s³+O(s⁴)
Ustar=U0+U1*s+U2*s²
pLf(r)=s*U(s)          (variable canonique f originale)
pLf_prime(r)/r=G(s,U)=2*(U+s*U_s)  (sur l'EDO originale)
Vstar(s)=2*U0+4*U1*s+6*U2*s²
```

La vraie borne rationnelle signée `U3<0` du Step67b, déjà conservée dans le rapport ORIGINAL Step68u (empreinte certifiée), permet les **LIMITES EXACTES AU CENTRE** :

```
lim_{s->0+} (U-Ustar)/s³ = U3
lim_{s->0+} (U_s-Ustar_s)/s² = 3*U3               <0
lim_{s->0+} (U_ss-2*U2)/s = 6*U3                 <0
U_sss(0)=6*U3                                      <0

lim_{r->0+} (pLf-r²*Ustar)/r^8 = U3
lim_{r->0+} (pLf_prime/r - Vstar)/s³ = 8*U3      <0
lim_{r->0+} (pLf_doubleprime-(2*U0+12*U1*s+30*U2*s²))/s³
    =56*U3                                          <0
lim_{r->0+} (pLf_tripleprime/r - (24*U1+120*U2*s))/s²
    =336*U3                                         <0
(d^8 pLf/dr^8)(0)=40320*U3                        <0
```

**La nouvelle jonction utile à Step68o est précisément la limite normalisée du TROISIÈME jet radial `pLf_tripleprime`**, calculée sans quotients `1/s` numériquement instables et sans dériver les simples bornes de Step68z. Les limites d'ordre 0/1 concordent avec les inclusions CONTINUES Step68z : `3U3` appartient à l'intervalle signé de `(U_s-Ustar_s)/s²`, `8U3` appartient à `(G-Vstar)/s³`. Le rapport machine fournit des fractions exactes pour les 9 quantités, et non des arrondis flottants.

Coefficient physique d'entrée certifié, lu des originaux :

```
U3 in [
 -31325163121998456229/2500000000000000000000000000,
 -62650326243996887233/5000000000000000000000000000
]  approx -1.253006524879938e-8.
```

Par exemple le 3e jet normalisé possède la limite dans `336*U3`, approximativement `-4.210102e-6`, et la dérivée d'ordre 8 de `pLf` au centre vaut approximativement `-5.05212e-4`. Cette précision est celle des fractions source, PAS une comparaison temporelle.

## 2. Vérification indépendante et dépendances

Le programme crée symboliquement `pLf(r)=r²*(U0+U1*r²+U2*r⁴+U3*r⁶+U4*r⁸)`, puis **différentie véritablement en r** avec SymPy, forme 9 quotients normalisés, annule les puissances, et compare les limites à `1,3,6,6,1,8,56,336,40320` fois `U3`. Le coefficient `U4` libre est un **contrôle négatif de dépendance** : il doit disparaître de ces neuf limites. Les différents ordres sont ainsi vérifiés et non uniquement recopiés.

Les entrées sont authentifiées par empreintes blob Git :

- Source Step68z **`8c3a46b44e5c55c7b8f464668f9e8dc7d17eae8b`**, contrôlée localement ; rapport Step68z **`38f55aabf7a7c47c812f32db684f50ffbaf16374`**.
- Original Step68u **`aaacd0064e04cb0f5d596aa3df042a4c9a4c751d`** ; Step68v **`d83a3b80862a2e990a4c4879ec8745a4e91c8b34`** ; Step68y **`04271c360f2245142e171a5979db139ac4bdaf79`**.
- Le certificat Step68z est recalculé partiellement depuis ces origines, et l'inclusion centrale `U3,3U3,8U3` est contrôlée en arithmétique exacte.
- **9 nouveaux tests Step68aa + 8 tests de régression Step68z = 17 PASSED, zéro skip (0.65s)**. Les premiers essais du nouvel oracle ont échoué car deux formules tests omettaient le carré de `s` dans le terme `U2*s²`. Les erreurs ont été corrigées avant publication ; **le test symbolique a bien détecté les omissions**.
- Nouveaux fichiers publiés et octet-identiques aux versions locales réellement testées :
  - `numerics/hr_step68aa_canonical_center_radial_jets.py` — blob **`924192725dc20597df96451e7f211eba91861b50`** ;
  - `tests/test_hr_step68aa_canonical_center_radial_jets.py` — blob **`f83d6f72570646e2cc04cb4a73f3213373425301`** ;
  - `research/reports/gate2b-step68aa-canonical-center-radial-jets.json` — blob **`1a536bd0ff9e7b2a95254b3b7cd883d6fd9c524c`**.

Reproduire dans un clone contenant tous les fichiers historiques originaux :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step68aa_canonical_center_radial_jets.py tests/test_hr_step68z_invariant_center_cone.py
PYTHONPATH=. python -m numerics.hr_step68aa_canonical_center_radial_jets research/reports
```

## 3. Identités de dérivation de l'EDO originale nécessaires aux intervalles

La vraie EDO `2sU_s=G(s,U)-2U` entraîne pour tout `s>0`, avec G différentiable, **sans figer la dépendance de G en U** :

```
2*s*U_ss = G_s + (G_U - 4)*U_s
2*s*U_sss = G_ss+2*G_sU*U_s+G_UU*(U_s)^2+(G_U-6)*U_ss
```

Les premiers membres et les membres droits ont des annulations au centre imposées par l'EDO ; évaluer séparément leurs grandes expressions en intervalles introduit une dépendance artificielle et des divisions par `s`. Les coefficients centraux `U_n` peuvent être calculés sans cette instabilité via l'égalité des coefficients de série :

```
(2*n+2-G_U(0,U0))*U_n
    = coeff_s^n G(s, U0+U1*s+...+U_(n-1)*s^(n-1)), n>=1.
```

L'ancienne preuve `G_U<0` assure `2*n+2-G_U(0,U0)>0` ; **mais aucun nouveau U4 ou reste dérivé fini n'est certifié dans 68aa**. La formule de récurrence est analytique ; elle ne calcule pas encore `G_{s^a U^b}` pour le véritable profil Step55.

## 4. Frontière de la preuve / blocage pour Step68ab

Ce certificat donne des **limites au point `r=0` et non des bornes sur `0<r<=1/32`**. Il serait incorrect de remplacer `pLf'''(r)/r` par sa série tronquée sur `[1/64,1/32]` sans un **vrai certificat de reste**, ou de différencier les bornes de `U` données en Step68z : cette différentiation est invalide.

Les **étapes indispensables** pour Step68ab :

1. Reconstituer ET SHA-vérifier les originaux Steps45,46,55,57,58,60,68n,68o (et tous leurs modules sources transitifs) dans un espace exécutable ; la présente exécution Step68aa n'a **PAS** importé ni exécuté de nouveau le Hamiltonien Step45 ou l'opérateur temporel Step58.
2. Calculer `U4` et des dérivées de `G` avec expressions réellement normalisées à `s=0`, en utilisant la récurrence exacte et une borne de reste, puis des intervalles `U_{ss},U_{sss}` sur `[1/64,1/32]`.
3. Injecter les jets corrélés réels dans les DOUZE variables originales de Step68o, normaliser `A_N/r²,A_M/r²` et obtenir certificats exhaustifs cellules JOINTIVES, queue vide, aucun intervalle PENDING.
4. Poursuivre `[1/128,1/64]` puis centre ; séparément vérifier rang Dirac **complet**, lapses, bord, jauge, chartes `J=0,K=0`, dynamique 4D et observables.

**Pas de validation physique JANUS : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
