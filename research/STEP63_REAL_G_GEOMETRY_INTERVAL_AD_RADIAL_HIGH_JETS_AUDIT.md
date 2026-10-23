# JANUS — Étape 63 : bornes différentielles par intervalles du véritable G physique, avec géométrie variable

**23 octobre 2026.** Seule branche de recherche : `research/gate2b-nonhomothetic-transfer`. **Gate 2B OPEN ; JANUS-R NOT VALIDATED.** Il s’agit d’un résultat de régularité de données radiales initiales, pas de la préservation complète de Dirac ni d’une preuve d’absence de fantôme.

## 1. Rapport avec l'étape 62 déjà enregistrée par une autre session

Il existait au moment de la sauvegarde un **autre travail complet Step62**, `research/STEP62_AUTHENTIC_G_QUADRATIC_CURVATURE_CERTIFICATE.md`, avec une identité EXACTE `deg_U(G)=2`, `G_UUU=0`, et une borne analytique de signe stricte `0<=G_UU<337/500` sur le benchmark. **Ce travail est préservé, non écrasé.**

Notre calcul est complémentaire : `numerics/hr_step62_original_interval_ad.py` a été exécuté séparément, puis inscrit au rapport scientifique de **l'étape 63**. Contrairement au contrôle de courbure de Step62, nous reconstruisons et vérifions **QUATRE** sources historiques originales byte-identiques, en incluant le **vrai code de géométrie et de barrière globale** `hr_step55_global_barrier.py`, que le rapport Step62 déclarait seulement retranscrit en rationnels.

Empreintes Git des sources réellement importées et exécutées :

| Source | Git SHA-1 |
|---|---|
| `numerics/hr_step45_exact_physical_ward.py` | `66aa43841dccfe4a5d586a49be9c10af3a67a10e` |
| `numerics/hr_step46_exact_secondary_ode.py` | `bac025c28dbe1561c0c36c56dbfda46dc326f804` |
| `numerics/hr_step55_normalized_secondary.py` | `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` |
| `numerics/hr_step55_global_barrier.py` | `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` |

Le certificat ORIGINAL des **256 cellules** a été **réexécuté** et fournit EXACTEMENT les bornes rationnelles strictes du rapport Step55 : `max Fplus=-1480966474499367232302129/10^28<0` et `min Fminus=295653233337826329055403/(2*10^27)>0`. Toutes les dérivées découlent donc bien de l'expression physique \(G\) sur sa branche initiale déjà certifiée.

## 2. NOUVEAU CALCUL : dérivée totale en s de la géométrie ET du vrai G

La fonction symbolique réelle `normalized_symbolic()`, calculée depuis la secondaire sphérique à six couples de l’action positive-EH HR et deux poussières, possède des paramètres géométriques `Lg0(s),Lf0(s),Sgr0(s),...`. Ainsi,

\[
\frac{d}{ds}G(s,U;\gamma(s))
=G_s\big|_{\gamma\ \mathrm{fixe}}+\sum_a G_{\gamma_a}\gamma_a'(s).
\]

**Prendre seulement la dérivée partielle à paramètres fixés donne une réponse physique erronée.** Un test négatif compare les deux procédures sur la véritable expression originale et distingue leurs intervalles sans recouvrement au point \(s=0.2\).

Le module utilise une arithmétique de Taylor à deux variables et ordre total deux :
\[
G+G_s\,\delta s+G_U\,\delta U+
\tfrac12G_{ss}(\delta s)^2+G_{sU}\delta s\,\delta U+
\tfrac12G_{UU}(\delta U)^2.
\]
Chacun des coefficients est calculé en arithmétique d'intervalles à **arrondi entier extérieur** à l'échelle \(10^{-28}\), y compris les racines, les inverses et les produits. L'évaluation est effectuée sur les **256 cellules continues**, pas en un ensemble de points échantillonnés, avec \(s\in[0,289/400]\) et \(U\in[U_\star(s)-10^{-4},U_\star(s)+10^{-4}]\) comme certifié exactement Step55.

Tous les intervalles ci-dessous proviennent du rapport machine avec les bornes rationnelles exactes (les décimaux ci-dessous sont volontairement élargis) :

| Observable original | Encadrement sûr sur l'intervalle |
|---|---|
| \(G_s\) total | \(0.003704<G_s<0.004085\) |
| \(G_U\) | \(-1.003<G_U<-0.992\) |
| \(G_{ss}\) total | \(-0.000161<G_{ss}<-0.000138\) |
| \(G_{sU}\) | \(0.00318<G_{sU}<0.00705\) |
| \(G_{UU}\) (intervalle AD seul) | \(-0.020<G_{UU}<0.655\) |

**Ne pas interpréter la borne inférieure négative du seul AD comme un signe négatif réel de \(G_{UU}\)** : elle est une borne d'intervalle peu serrée. L'identité analytique plus forte de l'autre audit Step62 a déjà démontré \(0\le G_{UU}<0.674\) pour le benchmark. Les deux certificats ne se contredisent pas ; celui de Step62 est plus fort pour le signe, tandis que Step63 fournit les dérivées en \(s\) de la géométrie complète.

## 3. Jets physiques d'ordre deux et trois du moment f

Avec le changement de variables réellement utilisé Step55,
\[
s=r^2,\qquad P(r)=p_{L_f}(r)=r^2U(s),\qquad
2s U_s=G(s,U)-2U,
\]
le résultat exact de Step61 permet de définir
\[
H(s,U)=G+2sG_s+(G-2U)G_U,\qquad P''=H.
\]

En injectant les jets physiques obtenus par AD à l'intérieur de chaque cellule, on certifie **sur tout \(0\le r\le0.85\)** :
\[
\boxed{-0.014708<P''(r)<0.000685.}
\]

Pour \(s>0\), écrire
\[
P'''=2r\left(H_s+H_U\frac{G-2U}{2s}\right).
\]
Sur les **255 cellules intérieures**, c.-à-d. \(s\in[289/(400\cdot256),289/400]\), on obtient :
\[
\boxed{-0.117<P'''(r)<0.120.}
\]

**La première cellule, qui touche \(s=0\), reste OUVERTE pour cette dernière borne.** L'expression contient \((G-2U)/s\), et le tube fixe de Step55 \(U_\star\pm10^{-4}\) seul ne permet pas de l'envelopper par une simple division d'intervalles au centre. L'existence antérieure d'une solution analytique paire au centre ne suffit pas à elle seule à transposer la borne \(-0.117,0.120\) à ce premier segment ; il faut une estimation propre à l'EDO.

Le prochain verrou raisonnable est une inégalité d'intégration exacte pour \(W=U-U_0\), \((2sW_s+3W)=sA(s,U)\), en contrôlant \(A(s,U)=\{G(s,U)-(3U_0-U)\}/s\) par un \(\sup|G_s|\) sur une **boîte uniforme couvrant les U évalués à toutes les abscisses intermédiaires**. Une dérivée sur le seul tube variable \(U_\star(s)\pm10^{-4}\) n'y suffit pas. Il faut ensuite dériver un majorant de \(P'''\) régulier au centre. Cette étape est une piste Step64, **PAS encore un résultat du présent rapport**.

## 4. Preuves exécutées, négatifs et limites

Source nouvelle (fichier nommé `step62` car préparé parallèlement à l'autre Step62, enregistré formellement ici comme Step63) :

- `numerics/hr_step62_original_interval_ad.py`, blob Git **`a93bcd10cd54eec3b478ab0e02ff24fe592e4b8c`**.
- `tests/test_hr_step62_original_interval_ad.py`, blob Git **`ce270b88c8731e61ed71bf4949ba1686b7a5b69b`**.

Ces deux empreintes ont été comparées aux octets locaux effectivement testés et sont **identiques**.

```bash
cd /mnt/data/janus-step62
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
    tests/test_hr_step62_original_interval_ad.py
# RÉELLEMENT REJOUÉ : 15 passed in 11.42s.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. \
  python -m numerics.hr_step62_original_interval_ad 256 \
  > research/reports/gate2b-step62-raw-intervals.json
# SHA256 du fichier brut généré :
# 4b5dbf232cea21cb92a59b095da2026eedbbdfdf379db180d6c3e3b080930e88
```

Les tests couvrent : vérification des 4 SHA sources, reproduction EXACTE du certificat Step55 256-cellules, règles de Taylor polynomiales et racines rationalisées comparées à SymPy, vraie fonction G sur trois sites, différence avec géométrie incorrectement figée, tous les encadrements globaux, refus des chartes invalides, et fermeture « fail-closed » sur fichier historique altéré. **Ceci n'est PAS une réexécution du véritable Dirac temporel Step57–60**, ni une suite complète du dépôt, ni un résultat de GitHub Actions (désactivé).

Les fractions des neuf encadrements sont archivées exactement dans `research/reports/gate2b-step63-original-interval-report.json` ; l'ancien `research/reports/gate2b-step62-report.json` reste **intact**.

**BILAN : fonction physique originale et géométrie complète réellement différentiées et bornées par intervalles sur l'intervalle initial radial ; P'' certifié jusque r=0, P''' seulement sur les 255 cellules intérieures. Rang de Dirac, fixation des lapses, évolution 4D et absence du fantôme BD toujours NON ÉTABLIS. GATE_2B OPEN ; JANUS-R NOT VALIDATED.**
