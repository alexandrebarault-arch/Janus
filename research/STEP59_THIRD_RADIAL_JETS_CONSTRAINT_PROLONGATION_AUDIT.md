# JANUS — Étape 59 : dérivées radiales troisièmes du véritable Dirac temporel et identité avec les contraintes prolongées

**23 octobre 2026.** Branche de recherche : `research/gate2b-nonhomothetic-transfer` uniquement. **Gate 2B ouvert ; JANUS-R non validé.** Ne pas modifier `main`/V2 ni réactiver Actions.

## Provenance et objectif

L'étape 58 a construit la dérivée temporelle locale de la secondaire réduite `C_red` à partir du Hamiltonien original sphérique positif-EH, Hassan–Rosen, deux poussières mobiles, **SIX couples canoniques** :

\[
\dot C_{\rm red}=A_N N+B_N N'+C_N N''+A_M M+B_M M'+C_M M''.
\]

Les coefficients `C_N,C_M` s'annulent exactement sur les primaires `F_z=H_g=0`. Les quatre coefficients restants sont cependant des fonctions de nombreux **jets canoniques**, incluant jusqu'à la dérivée radiale troisième `q'''`. Il serait incorrect de les évaluer sur un ensemble de valeurs ponctuelles des champs `q,q'` sans imposer aussi les dérivées spatiales des contraintes.

**Cette étape dérive des identités exactes pour ces jets, et NON encore le rang de l'opérateur de lapses.**

Sources physiques vérifiées octet pour octet :

- `numerics/hr_step45_exact_physical_ward.py` — SHA Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e` : vraie action, vrais `H_g,H_f,C` et leurs 12 gradients canoniques.
- `numerics/hr_step57_secondary_principal_symbol.py` — SHA Git `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`.
- `numerics/hr_step58_temporal_operator.py` — SHA Git `802c23aebd41780d8c462f1aa1711707fe4ee88f`.

## 1. Symboles d'ordre trois à six couples sur `F_z=0`

On élimine exactement le jet `p'_{L_g}` de la stationnarité du déplacement relatif :

\[
D_g=p_{S_g}S'_g-L_gp'_{L_g}+p_g\theta'_g,\quad
F_z=D_g-\frac{Kz}{\sqrt{1-z^2}}=0,\quad K>0.
\]

Puis on différentie les **vrais coefficients Step58**, symboliquement, par rapport aux douze jets de troisième ordre `q'''`, sans prendre de valeurs numériques particulières. Tous les dérivés sont identiquement nuls à l'exception de :

\[
\boxed{\frac{\partial B_N}{\partial S'''_g}
=-\frac{2M_g^2S_g(1-z^2)}{L_fL_g^2}.}
\]

\[
\boxed{\begin{aligned}
\frac{\partial A_M}{\partial p'''_{L_g}}&=\frac{z(1-z^2)}{L_f^2},\\
\frac{\partial A_M}{\partial S'''_g}&=-\frac{p_{S_g}z(1-z^2)}{L_gL_f^2},\\
\frac{\partial A_M}{\partial\theta'''_g}&=-\frac{p_gz(1-z^2)}{L_gL_f^2}.
\end{aligned}}
\]

Les coefficients `A_N` et `B_M` ne dépendent d'aucune dérivée canonique troisième **après élimination algébrique de `F_z`**. Ceci découle d'annulations algébriques exactes, pas de petites valeurs flottantes.

Ces coefficients peuvent être non nuls dans la charte `L_g,L_f,S_g>0,\ |z|<1`. Ils n'impliquent pourtant PAS à eux seuls une équation supplémentaire ni une fixation des lapses.

## 2. Résultat principal : les dérivées troisièmes correspondent aux CONTRAINTES différentiées

On a déjà exactement, pour le vrai Hamiltonien initial :

\[
\frac{\partial H_g}{\partial S''_g}
=\frac{2M_g^2S_g}{L_g},
\]

les autres coefficients en dérivées secondes canoniques de `H_g` étant nuls.

La secondaire réduite authentique de l'étape 57 possède :

\[
\frac{\partial C_{\rm red}}{\partial p''_{L_g}}
=\frac{1-z^2}{L_f},\quad
\frac{\partial C_{\rm red}}{\partial S''_g}
=-\frac{p_{S_g}(1-z^2)}{L_gL_f},\quad
\frac{\partial C_{\rm red}}{\partial\theta''_g}
=-\frac{p_g(1-z^2)}{L_gL_f}.
\]

**NOUVELLES IDENTITÉS EXACTES DES PARTIES PRINCIPALES D'ORDRE TROIS** :

\[
\boxed{
(B_N)_{q'''}=-\frac{1-z^2}{L_gL_f}\,(H'_g)_{q'''},
\qquad
(A_M)_{q'''}=\frac{z}{L_f}\,(C'_{\rm red})_{q'''}.
}
\]

Ici `(X)_{q'''}` désigne exclusivement la somme des termes de `X` linéaires dans les douze dérivées canoniques troisièmes. La même partie principale de `A_M` s'exprime également en `(D''_g)_{q'''}` :

\[
(A_M)_{q'''}=-\frac{z(1-z^2)}{L_gL_f^2}(D''_g)_{q'''}.
\]

**Portée exacte :** lorsqu'une donnée vérifie les contraintes comme équations sur un INTERVALLE radial, elle satisfait bien `H'_g=0` et `C'_{\rm red}=0`. Cependant, les termes `q'''` ne peuvent être éliminés du crochet temporel qu'en soustrayant les **dérivées de contraintes complètes**, y compris tous leurs termes de plus bas ordre. Nos identités n'établissent PAS que `B_N=-[(1-z²)/(L_gL_f)]H'_g` ni que `A_M=(z/L_f)C'_{\rm red}` en totalité. Cette réduction intégrale reste à faire.

Cette distinction empêche une conclusion artificielle sur le rang de Dirac à partir de seuls coefficients principaux.

## 3. Stationnarité spatiale prolongée à l'ordre deux

Avec `R=\sqrt{D_g^2+K^2}>0`, `K>0`, `z=D_g/R`, la dérivation totale EXACTE donne

\[
\boxed{
z'=\frac{K^2D'_g-D_gKK'}{R^3}
}
\]

et

\[
\boxed{
z''=
\frac{K^2D''_g+KK'D'_g-D_g(K')^2-D_gKK''}{R^3}
-\frac{3(K^2D'_g-D_gKK')(D_gD'_g+KK')}{R^5}.
}
\]

Le programme confirme dans SymPy : `z'=D_r z`, `z''=D_r z'`, puis `F_z=F'_z=F''_z=0` sur la bonne branche. Cela identifie les dépendances de troisième jet canoniques introduites par `D''_g`.

La parité centrale antérieure `D_g=r^3d(s)`, `K=r^2k(s)>0`, `s=r^2` implique `z=r w(s)`, `w=d/\sqrt{k^2+s d^2}`, donc

\[
z'=w+2s\,w_s,\qquad
z''=r(6w_s+4s\,w_{ss}).
\]

Ainsi `z''=O(r)` si `d,k` possèdent deux dérivées régulières en `s` et si `k>0` ; il s'agit d'une conséquence de parité de la charte radiale, PAS d'un théorème global de régularité dynamique 4D.

## 4. Tests réellement exécutés et sauvegarde

Nouvelle source : `numerics/hr_step59_third_jet_gate.py`, Git blob `ae26a79cbfa7bb50fbb398d7d6c18478adf7627e`.

17 nouveaux tests : `tests/test_hr_step59_third_jet_gate.py`, Git blob `ee6dd8f99e963c60a78c3b4f5a52000273b929c4`. Ces deux empreintes sont vérifiées sur GitHub et correspondent EXACTEMENT aux octets exécutés localement.

Sur le poste de calcul isolé `/mnt/data/janus-step58`, avec les originaux Steps45/57/58 byte-authentiques :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
 tests/test_hr_step57_secondary_principal_symbol.py \
 tests/test_hr_step58_temporal_operator.py \
 tests/test_hr_step59_third_jet_gate.py
# RÉEL : 44 PASSED in 5.12 s = 12 Step57 + 15 Step58 + 17 NOUVEAUX Step59.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step59_third_jet_gate
```

Manifest JSON local généré, SHA256 `c2bbd8c3829c2333f61f586170502b0dbd0b0a1b7e8e4d71e0d38be12fe70012`, mais NON uploadé comme artefact autonome ; `research/reports/gate2b-step59-report.json` contient le résultat durable. **Aucune CI / suite complète du dépôt / véritable oracle original non-IBP du Dirac temporel** exécuté ce tour.

## 5. Blocage restant — étape 60

1. Réduire **les coefficients complets** `A_N,B_N,A_M,B_M` modulo `F_z,H_g,H_f,D_{\rm diag},C_{\rm red}` et leurs prolongations nécessaires. La bonne première opération est de soustraire les multiples complets de `H'_g` de `B_N` et de `C'_{\rm red}` de `A_M`, et de vérifier que les résidus ne contiennent plus `q'''`. Ne jamais simplement mettre les dérivées troisièmes à zéro.
2. Introduire le profil spatial EXACT et strictement positif Step55 et ses jets cohérents, y compris les données du centre ; déterminer la dimension du noyau des multiplicateurs des lapses et la possibilité de temps réel nonhomothétique.
3. Valider le résultat par variation fonctionnelle INDÉPENDANTE à partir de l'action originale non intégrée par parties, traiter bords et secteurs `K=0`/`J=0` hors charte.

**VERDICT : l'organisation exacte des jets d'ordre trois par dérivées de contraintes est désormais démontrée. Le système de Dirac temporel complet, le rang des multiplicateurs et la fixation des lapses restent NON DÉTERMINÉS. GATE_2B OUVERT, JANUS-R NON VALIDÉ.**
