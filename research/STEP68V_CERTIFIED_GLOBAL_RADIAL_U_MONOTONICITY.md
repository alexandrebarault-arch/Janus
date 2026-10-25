# JANUS — Étape 68v : monotonie radiale U_s > 0 certifiée SUR TOUT le domaine Step55

**25 octobre 2026 ; écriture seule sur `research/gate2b-nonhomothetic-transfer`. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Nouvelle jonction des deux théorèmes spatiaux

La nouvelle preuve Step68u démontrait, conditionnellement aux anciennes récurrences analytiques exactes Step49/67b et à l'existence Step68l, `|U-Ustar|<=kappa*s³` près de `r=0`, mais la première certification ne portait que jusqu'à `r=1/32`.

Le programme nouveau `numerics/hr_step68v_global_monotone_U.py` authentifie les **quatre vrais originaux Step45/46/55** et les deux fournisseurs intermédiaires 68u/68m, puis relance les dérivées troisièmes du véritable résidu de barrière

\[
F_\pm(s)=G(s,U_*(s)\pm\kappa s^3)-2(U_*(s)\pm\kappa s^3)
-2s(U_*'(s)\pm3\kappa s^2),
\qquad \kappa=10^{-7},
\]

mais cette fois pour **TOUT le domaine** `0<=s<=1/64` (`0<=r<=1/8`). Les **bornes rationnelles extérieures** de leurs dérivées trois, à partir de l'algèbre d'intervalle originale Step55 `I,S=10^28`, sont

\[
-\frac{6459335014235568976637}{5000000000000000000000000000}
\le F_+'''/6\le
-\frac{3664994635715032685663}{5000000000000000000000000000}<0
\]

et

\[
0<\frac{1270413128798157440287}{2500000000000000000000000000}
\le F_-'''/6\le
\frac{5334540011257620607023}{5000000000000000000000000000}.
\]

Comme \(F_\pm,F_\pm',F_\pm''\) sont exactement nuls au centre par la récurrence analytique originelle U0/U1/U2, la formule de Taylor-Lagrange et l'inclusion stricte `|U3|<kappa` (Step67b) imposent l'orientation et le premier contact des deux barrières. Cela étend la borne cubique spatiale :
\[
\boxed{|U(s)-U_*(s)|\le10^{-7}s^3
\quad\forall s\in[0,1/64],\quad r=\sqrt{s}.}
\]

**Nouvel ingrédient :** un encadrement dirigé de la vraie dérivée \(G_U(s,u)\), calculée par différentiation automatique du vrai original \(G\) sur tout le nouveau tube physique, est
\[
-\frac{80486828173226613100871119}{80000000000000000000000000}
\le G_U\le
-\frac{496930963235322352562534863}{500000000000000000000000000}.
\]

Définir le résidu central \(F_0(s)=G(s,U_*)-2U_*-2sU_*'\). Ses trois premiers jets au centre sont **EXACTEMENT** nuls en raison de la vraie récurrence Step49/67b. Le théorème de Taylor donne donc \(|F_0(s)|\le s^3R_0\), avec \(R_0\) majorant le module de sa troisième dérivée divisée par six, directement calculé par des jets d'intervalles.

Pour la vraie solution \(U=U_*+\Delta\) avec \(|\Delta|\le\kappa s^3\), l'ODE et le théorème des accroissements finis impliquent exactement :
\[
2s(U_s-U_*')=F_0(s)+G(s,U)-G(s,U_*)-2\Delta,
\]
\[
\boxed{|U_s-U_*'|\le\frac{s^2}{2}\big(R_0+(L_G+2)\kappa\big)},
\]
où \(L_G\) est la majoration rigoureuse de \(|G_U|\) sur le tube.

Avec \(s\le1/64\), la borne de dérivée originale \(U_*'=U_1+2U_2s\) et les intervalles vers l'extérieur donnent
\[
\boxed{\frac{3947151372926460534852373}{5000000000000000000000000000}
\le U_s(s)\le
\frac{7897452509337401302640553}{10000000000000000000000000000}}.
\]
La borne inférieure est strictement **positive**, y compris au centre \(s=0\) par \(U_s(0)=U_1>0\).

La preuve originale Step68m a, elle, déjà signé \(U_s>0\) sur **toute la bande fermée \([1/64,289/400]\)**. Il n'existe donc aucun trou entre les deux domaines, et la continuité donne la conclusion spatiale générale :

\[
\boxed{
U_s(s)>0\quad\text{pour CHAQUE }s\in[0,289/400],
\quad \text{équivalemment } 0\le r\le17/20.
}
\]

Il s'agit d'un **théorème de monotonie SPATIALE sur la véritable branche normalisée de l'EDO Step55**, construit à partir des certificats historiques, PAS une preuve de la préservation temporelle des contraintes.

## Reproductibilité

- Source réellement exécutée : `numerics/hr_step68v_global_monotone_U.py`, Git blob `9b6a2f93271a96af97d62648201c163282758c08`.
- Tests réellement exécutés : `tests/test_hr_step68v_global_monotone_U.py`, Git blob `6bdff3937051dd40719eb1d0f1441065eecb4b54`.
- Rapport arithmétique de toutes les bornes : `research/reports/gate2b-step68v-global-monotone-radial-U.json`, Git blob `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`.
- État/log du test : `research/reports/gate2b-step68v-pytest-state.json` et `...-pytest.log`, blobs comparés aux fichiers exécutés.

**6 tests passés en 2.27s**, sous timeout dur 22 secondes, avec authenticité, bornes signées, majoration de \(G_U\), jonction exacte avec l'anneau Step68m, refus de paramètres non prouvés et contrôle des limites scientifiques.

**Limite importante :** les relations exactes des coefficients U0..U2 proviennent de Step49/67b et l'intervalle strict pour U3 provient de Step67b ; le nouveau programme atteste leurs SHA/provenance et leur utilisation, **sans recommencer de zéro la preuve analytique centrale**. Son résultat est conditionnel aux preuves originales citées.

## Verrou temporel toujours ouvert

La monotonie `U_s>0` est désormais globale **pour les données SPATIALES certifiées**. En revanche, le vrai `A_N,A_M` du crochet temporel à six couples n'est signé uniformément que sur `r∈[1/32,17/20]`. Un essai temporel sur `r∈[1/64,1/32]` existe sur GitHub avec statut `INCOMPLETE` (247 cellules, 7 en attente) ; cette zone **n'est PAS certifiée temporellement**. Le nouveau tube cubique étroit évite une grande partie de la perte de précision en U, mais l'évaluation brute des gradients Step58 gonfle encore les intervalles : la suite doit normaliser `A_N/r²` et `A_M/r²`, puis reconstruire les jets hamiltoniens à partir du centre en conservant les contraintes.

Rang complet de Dirac, jauge et bords des lapses, oracle Poisson NON-IBP six-couples, chartes K0/J0 et fantôme BD **toujours ouverts**.

**VERDICT : monotonie spatiale globale certifiée, pas de validation JANUS-R.**
