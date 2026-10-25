# JANUS — Étape 68u : barrière cubique au centre du profil original Step55

**25 octobre 2026. Branche d'écriture :** `research/gate2b-nonhomothetic-transfer`. **GATE_2B OPEN — JANUS-R NOT_VALIDATED.**

## Théorème conditionnel exact, sur la vraie branche analytique du centre

Le vrai profil spatial non homothétique satisfait l'EDO originale Step45/46/55 :
\[
2sU_s=G(s,U)-2U,\qquad s=r^2.
\]

Les coefficients U0,U1,U2 de son polynôme Taylor `Ustar(s)=U0+U1*s+U2*s²` obéissent **exactement** à la récurrence analytique centrale prouvée antérieurement dans Step49/67b. La borne rationnelle de Step67b établit strictement `|U3|<1e-7`. En conservant ces résultats originaux, définir deux barrières `Uplus=Ustar+kappa*s³`, `Uminus=Ustar-kappa*s³`, avec `kappa=1/10^7`.

Le nouveau programme `numerics/hr_step68u_cubic_center_barrier.py` authentifie octet pour octet les quatre fournisseurs physiques originaux Step45/46/55 puis évalue le **VRAI** résidu
\[
F_\pm(s)=G(s,U_\pm)-2U_\pm-2s\,U'_\pm
\]
sur le continuum `0<=s<=1/1024` par arithmétique entière à arrondis externes `I, S=10^28` et jets Taylor d'ordre 3 centrés sur tous les s de l'intervalle.

Il en résulte les encadrements rationnels uniformes exacts :
\[
-\frac{2575583792061894700823}{2500000000000000000000000000}
\le F_+'''(s)/6\le
-\frac{4976590240016531320049}{5000000000000000000000000000}<0,
\]
\[
0<\frac{1924421421164366052919}{2500000000000000000000000000}
\le F_-'''(s)/6 \le
\frac{2011690220837250529}{2500000000000000000000000}.
\]

Les résidus exacts F±(0), F±'(0), F±''(0) valent **zéro par la récurrence analytique originale** (ne pas confondre cela avec la seule appartenance de 0 à un intervalle d'arrondi). Le théorème de Taylor donne alors `F±(s)=s³*F±'''(xi)/6`, donc `Fplus<0<Fminus` pour chaque s>0 dans le domaine. La valeur exacte U3 est strictement dans les deux barrières au voisinage perforé de s=0 ; l'argument de premier contact de Step49–55 et la régularité des vrais dénominateurs sur le tube global Step68l permettent de prolonger cette inclusion jusqu'à la borne.

**Nouvelle conclusion SPATIALE rigoureuse, conditionnée à Step49 et Step67b :**
\[
\boxed{|U(r^2)-U_*(r^2)|\le10^{-7}r^6\quad
\forall\,0\le r\le1/32.}
\]

À `r=1/32`, l'erreur est <= `10^-7/1024^3 ≈ 9.31e-17`, bien plus serrée que le tube uniforme Step68l `10^-6`. Le problème restant est de l'intégrer aux **jets temporels**, et non de réclamer déjà la positivité de A_N,A_M au centre.

## Sources et tests

- `numerics/hr_step68u_cubic_center_barrier.py` — Git blob `4249c1a8c1f60071612c52d756d9f4ff753f22e3`.
- `tests/test_hr_step68u_cubic_center_barrier.py` — Git blob `d055a1a2aef67f8117ba3baa451c946044e2af83`.
- `research/reports/gate2b-step68u-center-cubic-barrier.json` — Git blob `aaacd0064e04cb0f5d596aa3df042a4c9a4c751d`.
- `research/reports/gate2b-step68u-pytest-state.json` et `...-pytest.log`.

**6 tests ont réellement réussi en 2.20 secondes**, sous un timeout dur de 22 secondes, incluant l'échec contrôlé d'un tube `kappa=10^-8` trop étroit et le rejet d'un domaine non authentifié. Les 3 nouvelles empreintes Git du code, des tests et du rapport JSON correspondent exactement aux fichiers exécutés.

La preuve du centrage analytique U0/U1/U2 et du U3 original est **réutilisée** de Step49/67b, et non redémontrée dans ce programme. Aucune preuve de suppression du fantôme BD, de fixation des lapses ou de rang de Dirac ne peut être déduite de cette seule inclusion spatiale.

## Échec honnêtement enregistré de la méthode temporelle brute

Deux jobs sous timeout 24s ont tenté la bande `r in [1/64,1/32]` via la **méthode temporelle précédente** utilisant le tube uniforme Step68l : 500 nœuds, 247 feuilles signées, 7 cellules non résolues. **Statut INCOMPLETE, PAS un certificat de l'anneau.** Cet état brut est publié dans `research/reports/gate2b-step68u-incomplete-1over64-to-1over32-checkpoint.json`, Git blob `fbbeeb09fb397abf14d77fb0bce22d8a44172b79`, SHA256 local `ab4f0314647fa39ba6d93d374f3f307486223939180fe6748e9196175f1ea5b4`.

Un premier essai exploratoire a remplacé ce tube uniforme par `kappa*s³` dans le calcul de l'ODE. À un point fixe `r=1/64`, les coefficients temporels gardent les bons signes, mais sur une cellule large l'arithmétique d'intervalles continue de s'élargir, indépendamment de l'incertitude très faible sur U. **Il faudra normaliser les annulations des coefficients temporels eux-mêmes**, plutôt que multiplier à l'infini les cellules.

**Prochaine étape :** construire et certifier par intervalles le système normalisé au centre, comprenant `U_s,U_ss,U_sss`, puis les coefficients du vrai six-pair original Step58 `A_N/r²,A_M/r²`, sans division non régularisée par `s`. Après quoi : bords, lapse gauge, oracle Poisson NON-IBP, rang global, K=0/J=0. **GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**
