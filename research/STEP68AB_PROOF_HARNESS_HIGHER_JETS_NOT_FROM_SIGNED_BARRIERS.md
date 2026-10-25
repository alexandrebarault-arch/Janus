# JANUS — STEP68ab : contre-modèle exact à la déduction illégitime des jets temporels

**25 octobre 2026 — uniquement la branche research/gate2b-nonhomothetic-transfer.**  
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## 1. Diagnostic scientifique précis

Les étapes 68u/v/y/z/aa ont réellement certifié, pour la branche **radiale physique ORIGINALE** Step45/46/55, sur \`0≤s=r²≤1/1024\`, des résidus de barrières cubiques, \`G_U<0\`, \`U3<0\`, la borne du cône \`h=(U-Ustar)/s³\`, et les écarts de \`U_s\`, \`G(s,U)-Vstar\`, etc. Step68aa fournit en outre des **limites de jets à s=0**, PAS leurs bornes uniformes pour \`s>0\`.

La question était : peut-on **déduire les bornes de U_sss sur l'anneau intérieur** uniquement à partir de ces certificats d'amont, sans recalculer les dérivées de la fonction physique particulière \`G(s,U)\` ?

**Réponse mathématique : NON.** L'étape 68ab construit **des équations analytiques ALTERNATIVES** \`G_n\` et de vraies solutions analytiques \`U_n\`, avec tous les encadrements de référence signés publiés, et qui ont cependant \`U_n'''(smax)→−∞\` pour \`smax=1/1024\`.

Il ne s'agit **pas d'un contre-exemple à JANUS** : le \`G\` de Step55 est FIXE et pourrait parfaitement posséder les bornes nécessaires. C'est une preuve de **non-déductibilité à partir des seuls résumés d'intervalles**, qui interdit un raccourci numérique incorrect.

## 2. Construction analytique qui conserve les trois résidus de référence

Définir \`smax=1/1024\`, \`kappa=1/10^7\`, \`epsilon=1/10^11\`, et \`c\` le **milieu rationnel exact de l'intervalle original Step67b U3**. Pour chaque fréquence réelle \`n≥1\`, écrire :

\`\`\`
Ustar(s)=U0+U1*s+U2*s²
h_n(s)=c + epsilon*(s/smax)^6*sin(n*s)/n
U_n(s)=Ustar(s)+s³*h_n(s)
Vstar(s)=2*(Ustar+s*Ustar_s)

A_n(s)=epsilon*(21*sin(n*s)/n+2*s*cos(n*s))
       /(smax^6*h_n(s)*(h_n(s)^2-kappa²))

G_n(s,u)=Vstar(s)+9*c*s³ -(u-Ustar(s))
         +A_n(s)*(u-Ustar(s))*((u-Ustar(s))²-kappa²*s^6).
\`\`\`

\`h_n\` reste strictement entre \`-kappa\` et zéro ; ainsi \`A_n\` a un dénominateur non nul. Toute expression est analytique en \`s\`, y compris au centre ; il n'y a **pas de division résiduelle par s** dans la formule retenue.

Vérifications symboliques indépendantes avec SymPy :

\`\`\`
2*s*(U_n)_s == G_n(s,U_n)-2*U_n               EXACT
G_n(s,Ustar)-Vstar =9*c*s³                    EXACT
Fplus=G_n(s,Ustar+kappa*s³)-2*(barrière+s*barrière_s)
      =(9*c-9*kappa)*s³                      EXACT
Fminus=(9*c+9*kappa)*s³                      EXACT
\`\`\`

La correction cubique de \`G_n\` s'annule sur **chacune des trois courbes** \`Ustar\`, \`Ustar+kappa*s³\` et \`Ustar-kappa*s³\`. Le **troisième ordre de tous leurs résidus est donc exactement constant**, malgré la haute fréquence interne. Les valeurs \`F0'''/6=9c\`, \`Fplus'''/6=9c-9kappa\`, \`Fminus'''/6=9c+9kappa\` sont **strictement intérieures** aux intervalles originaux effectivement relus et SHA-authentifiés des rapports Step68u/68v.

En utilisant \`|sin(ns)|≤n*s\` et \`|cos(ns)|≤1\`, pour **tous les réels n≥1, simultanément** :

\`\`\`
|h_n-c| ≤ epsilon*smax
|h_n'(s)| ≤ 7*epsilon
|2*s*h_n'+9*(h_n-c)| ≤ 23*epsilon*smax

|G_n_U+1| ≤ [23*epsilon*smax*2*kappa²] /
             [(|c|-epsilon*smax)*(kappa²-(|c|+epsilon*smax)²)]
< 0.001.
\`\`\`

Toutes ces bornes sont vérifiées en **Fraction rationnelle exacte** ; la dérivée \`G_n_U\` est sur tout le tube \`|u-Ustar|≤kappa*s³\` à l'intérieur des véritables bornes publiées de \`G_U\` (Step68v). Les bornes de Step68z pour \`h\`, \`f=F0/s³\`, \`(U_s-Ustar_s)/s²\`, \`(G-Vstar)/s³\` et le terme auxiliaire \`(G(U)-G(Ustar))/s³\` restent également strictement satisfaites par la construction.

**Non-bornitude certifiée** : aux fréquences \`n=2*pi*k/smax\`, avec \`k\` entier positif, \`sin(n*smax)=0\` et \`cos(n*smax)=1\`. La dérivation **explicite** de \`U_n\` donne

\`\`\`
U_n'''(smax)-6*c = epsilon*smax*(216-4*pi²*k²).
\`\`\`

Le membre droit tend rigoureusement vers \`-∞\`, tout en conservant les intervalles précédents. Le coefficient \`U3=c\` est le même pour toute la famille, et la limite centrale de Step68aa est respectée.

**Distinction capitale** : les certificats d'amont de JANUS décrivent des PROPRIÉTÉS du véritable \`G\`. Les modèles \`G_n\` construits ici ont ces mêmes propriétés, mais **ne sont pas le \`G\` spécifique du Hamiltonien Step55**. Rien ici n'affirme que cette famille appartient aux solutions physiques de JANUS.

## 3. Récurrence correcte U4 pour la vraie fonction G

L'équation \`2sU_s=G(s,U)-2U\` donne sans résonance au centre :

\`\`\`
U4 = [s^4]G(s,U0+U1*s+U2*s²+U3*s³) / (10-G_U(0,U0)).
\`\`\`

Avec \`gij=[s^i (u-U0)^j]G(s,u)\` :

\`\`\`
num(U4) = g40 + g31*U1 + g21*U2 + g11*U3
        + g22*U1² + g12*2*U1*U2
        + g02*(2*U1*U3+U2²)
        + g13*U1³ + g03*3*U1²*U2 + g04*U1⁴.
U4=num(U4)/(10-g01).
\`\`\`

L'oracle symbolique a confirmé le facteur \`10-g01\` en remplaçant directement \`U=Ustar+U3*s³+U4*s⁴\` dans la série de \`G\`. Sur la vraie branche, Step68v assure \`G_U<0\`, donc le dénominateur est strictement positif. **Cependant aucun des coefficients \`gij\` du véritable G Step55 n'a été évalué ici**, et \`U4\` NUMÉRIQUE N'EST PAS CERTIFIÉ.

## 4. Reproductibilité et statut d'audit

Source **exécutée et Git blob authentifié** : \`numerics/hr_step68ab_derivative_data_obstruction.py\`, SHA **\`32c3a2172155bad361bc6c3d73bdec63fc27423d\`**.

Tests **exécutés et Git blob authentifié** : \`tests/test_hr_step68ab_derivative_data_obstruction.py\`, SHA **\`5a790953779c81db7eb729948f078c9d3b682956\`**.

Rapport machine **exécuté et Git blob authentifié** : \`research/reports/gate2b-step68ab-derivative-data-obstruction.json\`, SHA **\`fcef873c8d565bc9c326043906fb4efaa613d395\`**.

Les sources précédentes 68z/68aa et les trois rapports 68u/68v/68y ont été SHA-vérifiés à nouveau avant le calcul. Le **code/test/JSON publiés sont identiques aux fichiers locaux testés par Git blob**. Une erreur intermédiaire de simplification symbolique (le symbole \`k\` doit être **entier** pour \`sin(2πk)=0\`) a été détectée par les tests et corrigée AVANT la publication.

**Exécution finale effective : 29 tests PASSED en 3.21 s**, soit **12 nouveaux tests Step68ab** et les **17 tests Step68aa+68z** précédents, zéro skip. Le JSON complet a été regénéré par la vraie entrée de commande et comparé octet à octet au fichier publié.

\`\`\`bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
  tests/test_hr_step68ab_derivative_data_obstruction.py \
  tests/test_hr_step68aa_canonical_center_radial_jets.py \
  tests/test_hr_step68z_invariant_center_cone.py

PYTHONPATH=. python -m numerics.hr_step68ab_derivative_data_obstruction research/reports
\`\`\`

## 5. Reprise impérative — HARD RED STEP68ac

1. **Recharger ET SHA-vérifier la vraie fonction normalisée** \`G\` dans \`hr_step55_normalized_secondary.py\`, son compilateur \`hr_step55_global_barrier.py\`, le \`Jet\` d'ordre 3 Step68n et l'opérateur temporel six-paires authentique Step58/68o.
2. Calculer les coefficients \`gij\` du G SPÉCIFIQUE pour \`i+j≤4\`, **non** ceux des modèles alternatifs \`G_n\`. Première cible : un encadrement rationnel authentique de \`U4\` ; vérifier les limites Step68aa.
3. Encadrer par dérivation du **G fixe et original** les restes de \`U_{ss},U_{sss}\` sur \`0<s≤1/1024\`. Ne pas utiliser le raccourci impossible réfuté ici, ni diviser directement des intervalles larges par \`s\`.
4. Alimenter les douze jets canoniques originaux dans Step68o/58, normaliser \`A_N/r²\`, \`A_M/r²\`, et prouver des cellules jointives sur \`[1/64,1/32]\` (7 en attente), puis descendre au centre.
5. **En parallèle** conserver l'obligation de rang Dirac complet, contraintes de lapses/bords/jauge, cas \`J=0,K=0\`, oracle NON-IBP et dynamique cosmologique 4D.

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Aucune borne du véritable \`U_{sss}\`, aucun nouveau signe temporel \`A_N/A_M\` n'a été revendiqué.
