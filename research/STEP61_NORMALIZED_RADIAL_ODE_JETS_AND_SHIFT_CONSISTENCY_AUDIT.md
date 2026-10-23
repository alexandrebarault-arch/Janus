# JANUS — Étape 61 : jets radiaux compatibles avec l’EDO exacte et cohérence du déplacement relatif

**23 octobre 2026. Branche seule autorisée en écriture :** `research/gate2b-nonhomothetic-transfer`. **Gate 2B OPEN ; JANUS-R NOT VALIDATED.** Aucun workflow GitHub n’a été réactivé.

## Objectif et limitation de provenance

L’étape 60 a établi, à partir de la véritable action sphérique ADM Hassan–Rosen avec **six couples canoniques et deux poussières**, que certains termes contenant des dérivées canoniques troisièmes de la préservation temporelle disparaissent après soustraction des contraintes radiales **complètes**. Mais elle n’a pas encore évalué les résidus de plus bas ordre sur la solution continue exacte de l’étape 55.

La présente étape 61 fournit un **pont mathématique exact et testé** entre la formulation radiale normalisée de Step55 et les jets requis par Step60 ; elle révèle aussi une substitution de déplacement `z'` indispensable avant tout calcul numérique physique. **Important : ce module est autonome. Il reproduit la forme d’EDO et les bornes publiées par Step55, mais n’importe PAS la véritable fonction \(G(s,U)\) historique ni le calculateur Step60 original lors de ses nouveaux 15 tests.** Ne pas annoncer que le crochet temporel physique a été évalué, ni que toute la chaîne ancienne a été revalidée.

Sources vérifiées SUR LE DÉPÔT comme points d’entrée pour la suite :

- `numerics/hr_step55_normalized_secondary.py`, vrai blob Git `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`.
- `numerics/hr_step60_full_constraint_prolongation.py`, vrai blob Git `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`.
- `research/reports/gate2b-step55-report.json` décrit les vraies bornes certifiées par intervalles ; nous utilisons ces valeurs rationnelles exactes.

## 1. Nouvelle expression exacte des jets \(p_{L_f}\)

Step55 normalise \(s=r^2\), \(P(r)=p_{L_f}(r)=r^2U(s)\) et démontre l’EDO radiale locale/continue

\[
2s\,U_s=G(s,U)-2U,\qquad V:=\frac{P'}r=G(s,U).
\]

En différentiant **le long de cette EDO** — et non en faisant comme si \(U_s\) était une donnée canonique libre —, on obtient exactement

\[
\boxed{P'=rG(s,U)}
\]

\[
\boxed{P''=H(s,U):=G+2sG_s+(G-2U)G_U.}
\]

Et, pour \(s>0\),

\[
\boxed{
P'''=2r\left[H_s+H_U\,\frac{G-2U}{2s}\right],
}
\]

avec les dérivées partielles \(G_s,G_U,H_s,H_U\) prises à variables \(s,U\) **indépendantes**. La limite au centre doit être calculée par l’expansion régulière, sans évaluer directement un quotient \(0/0\). Les identités ont été vérifiées algébriquement, notamment sur une solution polynomiale analytique manufacturée qui satisfait exactement l’EDO correspondante ; ce témoin manufacturé n’est PAS la solution physique JANUS.

**Conséquence pour le véritable calcul temporel :** les deuxième et troisième jets canoniques de \(p_{L_f}\) ne peuvent pas être choisis librement au moment de calculer les quatre coefficients de lapse. Ils proviennent de l’EDO physique et requièrent les dérivées partielles de son **vrai** membre de droite \(G\).

## 2. Centre régulier : une récurrence non résonante

La source physique Step55 donne la structure au centre

\[
G(0,U)=3U_0-U.
\]

Écrivons donc \(G(s,U)=3U_0-U+sA(s,U)\), puis

\[
U(s)=U_0+\sum_{n\ge1}U_ns^n.
\]

Les coefficients satisfont la récurrence exacte

\[
\boxed{
(2n+3)U_n=[s^{n-1}]\,A(s,U(s)),\quad n\ge1.
}
\]

À chaque ordre le membre de droite dépend uniquement des \(U_j\), \(j<n\). Les dénominateurs \(5,7,9,\ldots\) sont strictement positifs ; aucune résonance à un ordre entier positif ne vient de cet opérateur linéaire radial. Ceci est une **récurrence formelle**, pas la preuve autonome de convergence analytique (traitée conditionnellement par les étapes précédentes).

En particulier,

\[
U_1=\frac{G_s(0,U_0)}5,\qquad
U_2=\frac{G_{sU}(0,U_0)U_1+\tfrac12G_{ss}(0,U_0)}7.
\]

La régularité paire de \(P=r^2U(r^2)\) impose

\[
P''(0)=2U_0,\quad P'''(0)=0,\quad
\lim_{r\to0}\frac{P'''(r)}r=24U_1.
\]

Ces formules permettent un traitement adapté du centre pour la future évaluation temporelle, plutôt qu’une division numérique instable par \(s\).

## 3. Ce que les certificats d’intervalles de Step55 permettent réellement de borner

Pour \(0\le r\le17/20\), \(0\le s\le289/400\), Step55 certifie sur sa branche exacte :

\[
|U-U_\star|\le\frac1{10\,000},
\qquad
|V-V_\star|<\frac{41}{20\,000}.
\]

Ces preuves entraînent immédiatement, **en arithmétique rationnelle exacte** :

\[
\boxed{
|P-P_\star|\le\frac{289}{4\,000\,000}=0.00007225
}
\]

\[
\boxed{
|P'-P'_\star|<\frac{697}{400\,000}=0.0017425.
}
\]

Attention : on ne peut PAS en déduire une borne sur \(P''\) ni \(P'''\) en différentiant simplement ces inégalités. Un contre-exemple mathématique analytique, avec petites différences de fonction et de première dérivée mais dérivée seconde arbitrairement grande à un point intérieur, a été vérifié symboliquement. **Ce contre-exemple ne satisfait pas nécessairement la même EDO physique.** Il montre seulement que les deux bornes de tube, considérées seules, ne fournissent pas l’information différentielle recherchée.

La bonne démarche consiste à **compiler la vraie fonction Step55 \(G(s,U)\)**, puis à borner \(G_s,G_U,G_{ss},G_{sU},G_{UU}\) sur le tube certifié, en contrôlant les limites au centre. Les expressions \(H\) et \(P'''\) ci-dessus fourniront alors les bornes utiles au Dirac temporel.

## 4. Nouveau contrôle exact : `z'` EXTERNE de Step60 doit être replacé sur sa racine

Dans Step60, le jet second du déplacement a été construit en maintenant provisoirement `zr=z'` comme un symbole externe :

\[
Z_D=\frac{(1-z^2)^{3/2}}K,\qquad
Z_K=-\frac{z(1-z^2)}K,\quad
Z_1=Z_DD'_g+Z_KK'.
\]

Son expression `Z2=ZD Dg''+ZK K''+(D_r ZD)Dg'+(D_r ZK)K'` est correctement FORMÉE, et a permis l’annulation des termes en jets canoniques troisièmes. Mais l’évaluation physique des résidus d’ordre inférieur exige **`zr=Z1` partout**, y compris dans les dérivées `D_r Z_D,D_r Z_K`.

La différence exacte entre `Z2` avec `zr` libre et `Z2` avec `zr=Z1` vaut

\[
\boxed{
\Delta Z_2=(zr-Z_1)
\frac{-3z\sqrt{1-z^2}\,D'_g+(3z^2-1)K'}{K}.
}
\]

Cette différence est exactement zéro sur le jet stationnaire, mais **généralement non nulle** si l’on laisse `zr` libre ou qu’on le fige à zéro. Un contrôle négatif numérique exact le confirme. L’identité des dérivées **troisièmes** prouvée à Step60 reste intacte : ce défaut ne porte que sur les jets d’ordre inférieur, ceux qui restent précisément à analyser.

Ne PAS appeler cette observation une réfutation de Step60 ; elle définit une condition de substitution supplémentaire obligatoire avant l’évaluation du rang.

## 5. Reproductibilité et portée des tests

Nouveau module :

`numerics/hr_step61_normalized_jet_lift.py` — Git blob **`b345169d8806ce524527229c794ace71cf5d540e`**.

Nouveaux tests :

`tests/test_hr_step61_normalized_jet_lift.py` — Git blob **`08da0dba3aac34a5cd631a48ba6258d3ecfd01c2`**.

Ces deux blob SHA GitHub ont été vérifiés et correspondent octet pour octet aux fichiers testés localement.

```bash
cd /mnt/data/janus-step61
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
    tests/test_hr_step61_normalized_jet_lift.py
# RÉELLEMENT EXÉCUTÉ : 15 passed in 1.13s

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step61_normalized_jet_lift
```

Le manifeste brut local `research/reports/gate2b-step61-local-manifest.json`, SHA256 `6ae2f7f56ebb790f7be501ea72a528e216d5798fae6212ec7483d5584d88ef94`, est présent dans le workspace isolé mais n’a pas été uploadé comme fichier GitHub autonome. Ce rapport et `research/reports/gate2b-step61-report.json` rendent ses conclusions reproductibles. **Ne pas amalgamer ces 15 tests nouveaux avec les 56 tests exécutés dans l’autre environnement de l’étape 60 : les 56 n’ont pas été rejoués dans ce nouveau workspace.**

## 6. Prochaine étape 62 : condition avant toute conclusion de Dirac

1. Reconstruire et vérifier octet pour octet dans **un même environnement** les vrais modules Steps45/46/55/57/58/59/60 ; importer le **vrai \(G(s,U)\)** de `hr_step55_normalized_secondary.normalized_symbolic()`.
2. En dériver les jets requis, puis obtenir les bornes d’intervalles de \(G_s,G_U,G_{ss},G_{sU},G_{UU}\), spécialement près de \(s=0\). Utiliser les nouvelles formules exactes de \(P'',P'''\) sur la vraie solution radiale Step55.
3. Dans Step60, substituer rigoureusement **`z=Z`, `zr=Z1`, `zrr=Z2`**, puis toutes les contraintes primaires/secondaires et leurs dérivées radiales, et enfin évaluer et réduire les quatre coefficients des lapses. N’utiliser le mot « rang » qu’après ce contrôle.
4. Valider par un vrai oracle temporel indépendant depuis l’action originale non intégrée par parties, et examiner les bords et les chartes \(K=0,J=0\).

**Bilan : des identités nécessaires et un contrôle de cohérence exact ont été établis. L’opérateur temporel de Dirac JANUS évalué sur la vraie branche positive, le rang et la fixation des lapses sont toujours NON CALCULÉS. Gate 2B OPEN ; JANUS-R NOT VALIDATED.**
