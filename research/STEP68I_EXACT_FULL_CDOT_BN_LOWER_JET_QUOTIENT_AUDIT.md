# JANUS — Étape 68i : dernier coefficient de dérivée première du lapse réduit à des jets d'ordre inférieur

**25 octobre 2026. Branche exclusive :** `research/gate2b-nonhomothetic-transfer`. **GATE_2B OPEN, JANUS-R NOT_VALIDATED**.

## 1. Objectif exact

Après la preuve analytique de Step68h, `B_M=[dot C]_(Mprime)=0` sur `Fz=Fzprime=0`. Le terme de dérivée première du lapse `N` est
\[
B_N=[\dot C_{\mathrm{red}}]_{N'}.
\]
L'original Step60 avait déjà démontré que
\[
\widetilde B_N=B_N+\frac{1-z^2}{L_gL_f}H_g'
\]
était **indépendant des douze dérivées radiales canoniques troisièmes** sur `F_z=0`, à condition de conserver la **dérivée complète** de `H_g`.

Le nouveau calcul Step68i cherche à supprimer les jets seconds restants SANS les mettre arbitrairement à zéro et SANS encore supposer un rapport de lapses.

## 2. Nouveau quotient physique EXACT

Depuis les cinq originaux physiquement authentifiés Step45/57/58/59/60, le module `numerics/hr_step68i_BN_lower_jet_quotient.py` importe **effectivement** `full_constraint_prolongation()` de Step60 et ses expressions à six couples canoniques. Le coefficient \(\widetilde B_N\) comporte formellement des jets
\[
L_g'',\ p_{L_g}'',\ S_g'',\ \theta_g''.
\]

La différentiation symbolique exacte montre :

\[
\partial_{L_g''}\widetilde B_N=
\partial_{p_{L_g}''}\widetilde B_N=
\partial_{\theta_g''}\widetilde B_N=0,
\]
tandis que \(\partial_{S_g''}\widetilde B_N\) est **généralement non nulle**.

Or, dans la vraie primaire `H_g` originale :
\[
\frac{\partial H_g}{\partial S_g''}=\frac{2M_g^2S_g}{L_g}.
\]

Sur la charte régulière \(L_gS_gM_g^2\neq0\), définir, **sans approximation**,
\[
\boxed{\beta=
\frac{\partial_{S_g''}\widetilde B_N}{2M_g^2S_g/L_g}},
\qquad
\boxed{R_{B_N}=\widetilde B_N-\beta H_g}.
\]

Les **douze** dérivées \(\partial R_{B_N}/\partial q_i''\) sont exactement nulles sur la stationnarité `F_z=0`, et les **douze** jets canoniques d'ordre 3 n'y figurent pas. Le représentant `R_BN` est véritablement construit sans aucun jet d'ordre 2/3 APRÈS la démonstration d'indépendance de ceux-ci. Un mauvais signe devant \(\beta H_g\) laisserait un coefficient non nul de \(S_g''\), ce qui a été testé.

Ainsi, **sur les contraintes complètes `F_z=H_g=H_g'=0` et hors du centre** :

\[
\boxed{
B_N=R_{B_N}(q,q',z,z'),
\quad R_{B_N}\ \text{sans aucun}\ q_i'',q_i'''.
}
\]

L'expression de \(\beta\) est compliquée (725 opérations SymPy avant simplification poussée). Son SHA256 `srepr` est sauvegardé au rapport machine afin de permettre une comparaison fidèle : `dfdc84fd8cf3b29ede2f2c320a901abd8239325bf0dc8ca6893d394f2824c095`.

## 3. Ce qui N'EST PAS encore démontré

Contrairement au résultat exact Step68h sur \(B_M\), **le représentant \(R_{B_N}\) N'EST PAS une identité nulle hors des autres contraintes**. Des assignations génériques de variables canoniques produisent une valeur clairement non nulle (contrôle négatif). Sur un jet **physiquement contraint** de la référence radiale Step55 à `r=0,4`, il revient numériquement à zéro à la précision disponible, conformément au calcul temporel complet Step68f.

Ce contraste signifie qu'il reste à imposer et réduire les **primaires et secondaire supplémentaires** `H_f,Ddiag,C` et leurs prolongations : on ne peut pas déclarer `B_N=0` sur toutes les solutions régulières.

**Autre précaution :** \(\beta\) comporte \((S_g)^{-1}\) sous cette forme et `S_g≈r L_g` au centre sphérique. La présente étape n'a **pas encore établi une normalisation régulière en \(r=0\)** pour ce quotient ; il serait faux de l'affirmer.

L'éventuelle équation algébrique restante \(\dot C=A_NN+A_MM\) est donc toujours une **conjecture étayée numériquement**, pas une réduction globale prouvée.

## 4. Reproductibilité

Les originaux Step45/57/58/59/60 sont vérifiés octet pour octet, et le nouveau code et ses tests sont rechargés de GitHub avec les mêmes vrais Git blobs que les versions exécutées :

- `numerics/hr_step68i_BN_lower_jet_quotient.py` — `2ffc0f4bb65615836c25c5af83d905bd8b94783a`.
- `tests/test_hr_step68i_BN_lower_jet_quotient.py` — `94253af441672db15387f7dc6d6c049c5c4c8e4d`.
- `research/reports/gate2b-step68i-BN-lower-jet-quotient.json` — rapport machine de \(\beta\) et des résidus nuls.

**9 tests spécifiques PASSED en 13,51s** dans `/mnt/data/janus-step68f`. Ils couvrent source authentique, mutation négative, vraie dérivée complète `H_g'`, suppression de tous les q'' et q''', mauvaise soustraction, comparaison au benchmark contraint et non-nullité sur des points canoniques génériques.

Une tentative de faire passer 58 tests Step68e/f/g/h/i dans un seul processus a expiré à 180 secondes sans résultat final ; **ce n'est PAS annoncé comme une suite passée**. Les 49 tests Steps68e/f/g/h ont indépendamment **PASSED en 31,86s**, puis les 9 nouveaux tests 68i **PASSED séparément en 13,51s**. Aucun workflow GitHub Actions activé.

## 5. Prochaine priorité — Step68j

1. Démontrer ou réfuter \(R_{B_N}=0\) **modulo les primaires, la secondaire et leurs prolongations**, à partir du représentant exact maintenant sans jets supérieurs. Essayer l'élimination de variables linéaires une à une plutôt qu'une substitution géante : une tentative directe a explosé en temps de calcul. Ne pas oublier les termes de poussières et les bords.
2. Certifier uniformément `A_N>0`, `A_M<0` et la limite centrale du rapport de lapse sur la **vraie trajectoire globale unique** issue de Step55, non sur la simple famille de jets locaux Step68f.
3. Oracle indépendant de Poisson NON-IBP avec les six couples, conditions aux bords, contraintes temporelles, rang de Dirac et secteurs `K=0,J=0`. Until then `GATE_2B OPEN`, `JANUS-R NOT_VALIDATED`.

**VERDICT : suppression exacte de TOUS les jets q'' et q''' de B_N après quotients par H_g,H_g' sur F_z=0 ; annulation complète de B_N et rang des lapses ENCORE OUVERTS.**
