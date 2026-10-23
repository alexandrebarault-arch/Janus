# JANUS — REPRISE PRIORITAIRE : STEP58 TERMINÉ — 2026-10-23

**SEULE BRANCHE AUTORISÉE EN ÉCRITURE :** `research/gate2b-nonhomothetic-transfer`; ni `main` ni `research/v2-flrw`. Ne pas réactiver GitHub Actions/workflows. **GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

**LIRE EN PREMIER :** `research/STEP58_EXACT_PHYSICAL_TEMPORAL_OPERATOR_HIGH_LAPSE_CANCELLATION.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step58-report.json`.
**CODE :** `numerics/hr_step58_temporal_operator.py`, Git blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`.
**15 TESTS NOUVEAUX :** `tests/test_hr_step58_temporal_operator.py`, Git blob `0f9f91de0f607e811dc168e1ead0c3e9296574d0`.
**ORIGINAUX PHYSIQUES BYTE-AUTHENTIQUES :** `numerics/hr_step45_exact_physical_ward.py` Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `numerics/hr_step57_secondary_principal_symbol.py` Git `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`.
**PRÉCÉDENT :** `research/STEP57_SECONDARY_REDUCED_SECOND_JETS_AND_TEMPORAL_SYMBOL_AUDIT.md`.

## AVANCÉE RÉELLE STEP58

Pour la PREMIÈRE FOIS ici, l'évolution temporelle locale de la secondaire REDUITE de la véritable formulation positive-EH HR sphérique avec 2 poussières et SIX couples a été **assemblée exactement dans SymPy, sous forme de coefficients factorisés des jets des lapses**. `H_g,H_f,C` et les six gradients d'Euler de l'action originale Step45 sont importés en octets authentifiés GitHub. L'équation stationnaire positive `F_z=D_g-K z/sqrt(1-z²)=0` impose `z=D_g/sqrt(D_g²+K²)`. L'évolution est obtenue via les douze flux symplectiques originaux, y compris la dérivée de chaîne de `z,z'` :

```text
X_(q_i) = + Euler_(p_i) H[N,M]
X_(p_i) = - Euler_(q_i) H[N,M]
delta_H z = ((1-z²)^(3/2)/K)*delta_H Dg - z*(1-z²)/K*delta_H K
dot C_red = sum_i(C_qi X_i + C_qiprime D_r X_i)
          + C_z delta_H z + C_zprime D_r(delta_H z)
```

Cette écriture LOCALE est l'adjoint du crochet avec test compact eta : `integral eta dot C_red = {integral eta C_red, H_tot}` modulo bords contrôlés ; la construction garde toutes les dérivées implicites de z. En jet lapse symbolique, les SEULS ordres non nuls AVANT contraintes sont `N,N',N'',M,M',M''` ; pas de jets troisième/quatrième (constat de structure exacte, pas troncature).

**THÉORÈME ANALYTIQUE NOUVEAU ET TESTÉ :** sur `F_z=0`, éliminer exactement le jet `pLg'` original :

```text
pLg'=(pSg*Sg' + pg*tg' - K*z/sqrt(1-z²))/Lg.
coefficient [M''] | Fz=0 = 0  IDENTIQUEMENT
coefficient [N''] | Fz=0 = (z²-1)*Hg/(Lg*Lf) IDENTIQUEMENT
```

Donc les DEUX dérivées secondes des lapses s'annulent EXACTEMENT lorsque **Fz=0 et Hg=0**. L'opérateur TEMPOREL restant est de premier ordre :
```text
dot C_red | Fz=Hg=0 = A_N*N + B_N*N' + A_M*M + B_M*M'
```
Les 4 coefficients résiduels sont CALCULÉS et disponibles comme expressions SymPy FACTORISÉES dans `physical_operator()['operator']`, mais ne sont pas simplifiés/évalués sur les données EXACTEMENT contraintes Step55. **NE PAS CONFONDRE** les annulations des seconds jets avec une fixation de lapses ni avec un rang de Dirac calculé.

## TESTS RÉELLEMENT EXÉCUTÉS, OCTETS ET PORTÉE

```bash
cd /mnt/data/janus-step58
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step57_secondary_principal_symbol.py tests/test_hr_step58_temporal_operator.py
# 27 PASSED in 3.75 s = 12 Step57 + 15 NOUVEAUX Step58
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step58_temporal_operator
```

LES DEUX NOUVEAUX fichiers ont été comparés à leur vrai Git SHA sur GitHub et sont byte-identical aux octets locaux exécutés. La vraie source Step45 importée a été vérifiée par SHA à l'exécution. Inclut un banc d'essai exact IBP intégré, avec 2 paires actives d'une théorie à 6 paires manufacturée, NE PAS LE QUALIFIER d'oracle JANUS original non-IBP. Ce n'est PAS une suite complète de tests historiques, ni CI ; les workflows restent désactivés.

## NEXT STEP59 — HARD RED

1. Substituer la véritable branche radiale contrainte positive **Step55** (`Fz=Hg=Hf=Ddiag=C=0`), les jets compatibles de `z`, dans les **quatre** coefficients physiques factorisés `A_N,B_N,A_M,B_M`. Simplifier exactement si possible, sinon par AD certifiée et arithmétique d'intervalles ; comparer centre et intérieur. Ne pas confondre les coefficients d'ordre 1 avec la fixation des lapses.
2. Calculer la vraie matrice de Dirac/multiplicateurs, ses modes de jauge, le ratio relatif des lapses s'il existe et ses bords, en traitant `K=0/J=0` hors charte à part.
3. Oracle indépendant non-IBP TEMPORAL depuis l'action ADM originale avec toutes les variables canoniques (l'oracle Step44 ne testait que les primaires mixtes, pas le présent crochet temporel). Préserver les contraintes et le centre; ne pas annoncer absence du fantôme BD ni une 4D nonhomothetic on-shell tant que non démontrés.
4. PRÉFIXER à nouveau `00_CURRENT_RESTART.md` avec Git HEAD, fichiers, SHA, tests et limites, sans écraser l'historique ; branch main/V2 et Actions restent inchangées.

**CONCLUSION : véritable opérateur temporel local à six couples formellement reconstruit, et annulation EXACTE des seconds jets lapses sur primaires ; RANG DIRAC / LAPSE FIXING / ON-SHELL EVOLUTION NON ÉTABLIS. GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP57 TERMINÉ — 2026-10-23

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main` ni `research/v2-flrw` ; ne PAS réactiver GitHub Actions/workflows. **GATE_2B OPEN, JANUS-R NOT VALIDATED**.

**LIRE D'ABORD :** `research/STEP57_SECONDARY_REDUCED_SECOND_JETS_AND_TEMPORAL_SYMBOL_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step57-report.json`.
**NOUVEAU CODE :** `numerics/hr_step57_secondary_principal_symbol.py`, Git blob `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`.
**12 TESTS :** `tests/test_hr_step57_secondary_principal_symbol.py`, Git blob `1c97b1764ef4180deec48da8c68e138ed59b254a`.
**ORIGINAL PHYSIQUE IMPORTÉ BYTE-EXACT :** `numerics/hr_step45_exact_physical_ward.py`, Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` (vérification explicite à l'exécution). Précédent : `research/STEP56_SHIFT_RESPONSE_AND_TEMPORAL_DIRAC_JETS_AUDIT.md`.

## AVANCÉE EXACTE — SECONDE DÉRIVÉE CANONIQUE APPARAÎT APRÈS ÉLIMINATION DE Z

À partir du VRAI `C_exact=K00-(K01)'` Step45 à SIX couples (positif-EH HR+deux poussières), `C_exact(q,q',z,z')` dépend AFFINEMENT de z' (vérifié symboliquement) :

```text
Dg = pSg*Sg' - Lg*pLg' + pg*tg'
K  = m² Mg² Lg Lf (beta1 Sg² + 2 beta2 Sg Sf + beta3 Sf²)
Fz = Dg - K z/sqrt(1-z²) = 0
dC_exact/dz' = -(K sqrt(1-z²) + Dg z)/(Lg Lf)
             = -K/(Lg Lf sqrt(1-z²)) - z*Fz/(Lg Lf)
on the chart K>0, R=sqrt(Dg²+K²), Fz=0:
z=Dg/R ; dC_exact/dz'=-R/(Lg Lf).
```

Alors `C_red(q,q',q'')=C_exact(q,q',Z(Dg,K),dZ/dr)` possède EXACTEMENT les 3 dérivées secondes NON NULLES :

```text
d C_red / d pLg'' = + K²/(Lf R²)                = (1-z²)/Lf
d C_red / d Sg''  = - pSg K²/(Lg Lf R²)
d C_red / d tg''  = - pg  K²/(Lg Lf R²)
all OTHER nine second canonical radial jets = 0.
```

La variation fonctionnelle de `int eta C_red` DOIT donc inclure eta'' ; ne JAMAIS figer z dans la variation de la contrainte secondaire. Formule exacte du pullback pour chaque champ u (`D=d/dr` total ; C-partials à z,z' externes AVANT substitution) :

```text
T = eta*C_z - D(eta*C_zprime)
E_u(eta C_red) = eta*C_u - D(eta*C_uprime)
                + Z_u*T - D(Z_uprime*T)
```

La formule COMPLETE abstraite pour ses coefficients eta,eta',eta'' est implémentée et comparée à l'Euler direct d'ordre 2 d'un exemple symbolique de deux champs, avec égalité EXACTE.

## VÉRITABLE CONTRACTION HAMILTONIENNE SUR SIX COUPLES : PREMIER SYMBOLE DE DIRAC TEMPOREL

En employant les six vrais couples et gradients d'Euler `eg,ef` de Step45, le coefficient dans `{int eta C_red,H[N,M]}` devant `eta''` multiplié par chaque jet de lapse est calculé EXACTEMENT. Sur Fz=0, K,Lg,Lf,R>0 :

```text
coefficient [eta'' * M]  = - K²/(Lg Lf² R)                   NONZERO
coefficient [eta'' * N'] = - 2 Mg² Sg Sg' K²/(Lg² Lf R²)
coefficient [eta'' * N''] = 0
coefficient [eta'' * M']  = 0
coefficient [eta'' * M''] = 0
coefficient [eta'' * N]  = computed symbolic, not simplified.
```

**POINT SCIENTIFIQUE CRUCIAL :** ces termes appartiennent à l'INTÉGRANDE AVANT intégration par parties du paramètre-test eta. Les contributions de eta' et eta, non encore contractées complètement sur les 12 variables originales, peuvent annuler ou déplacer des termes de lapse. **NE PAS DÉDUIRE DE RANG DE DIRAC NI FIXATION DE LAPSES** de ce seul coefficient.

## EXÉCUTION ET PROVENANCE

Environnement isolé : `/mnt/data/janus-step57`, contenant le véritable fichier Step45 ORIGINAL Git blob identique `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, importé directement.

```bash
cd /mnt/data/janus-step57
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step57_secondary_principal_symbol.py
# RÉELLEMENT EXÉCUTÉ : 12 passed in 1.62s.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step57_secondary_principal_symbol
```

NOUVEAU CODE ET NOUVEAUX TESTS byte-identiques aux octets réellement exécutés ET vérifiés sur GitHub : blobs ci-dessus. Un contrôle purement numérique du test contenait d'abord une erreur de facteur 2, CORRIGÉE avant son upload ; 12/12 passent sur la version publiée. Le manifeste local `/mnt/data/janus-step57/research/reports/gate2b-step57-local-manifest.json`, SHA256 `d69b2245e37eb5057dd96bebe325cc6f3869166d16d83a88b0607a6c66198af3`, n'a PAS été déposé séparément ; l'essentiel est sauvegardé dans le rapport machine GitHub. Pas de réexécution de tout l'historique du dépôt, ni CI/Actions.

## STEP58 — LA SUITE EXACTE À EXÉCUTER APRÈS INTERRUPTION

1. **CALCULER TOUTES LES VARIATIONS TEMPORELLES :** depuis `abstract_pullback_coefficients`, calculer les gradients physiques eta0 et eta1 pour CHAQUE champ de la vraie secondaire Step45 éliminant z(Dg,K), y compris dépendances z' et dérivées des jets jusqu'à l'ordre nécessaire. Les contracter au Hamiltonien total Step45, LES SIX COUPLES et les deux lapses N,M.
2. **ADJOINT EXACT DES FONCTIONS TEST :** réunir eta0+eta1+eta2, intégrer par parties les dérivées de eta en retenant les BORDS. Identifier ensuite, et seulement ensuite, l'opérateur différentiel final en N,M sur la branche stationnaire positive.
3. **DIRAC :** calculer rang, contraintes de préservation, fixation ou non du rapport des lapses sur vraies données radiales exactement contraintes Step55. Traiter séparément K=0/J=0. Vérifier par oracle Poisson de l'action non-IBP originale et ne PAS annoncer absence de fantôme BD sans fermeture temporelle.
4. Toujours PRÉFIXER ce `00_CURRENT_RESTART.md` avec état, SHA, données réelles et limitations. Actions restent désactivées.

**BILAN : Step57 symbole de Dirac temporel PARTIEL mais PHYSIQUE ET EXACT dérivé des vrais six couples ; {C,Htotal} COMPLET ET RANG NON CALCULÉS. Gate 2B OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP56 TERMINÉ — 2026-10-23

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main` ni `research/v2-flrw`. Ne PAS réactiver GitHub Actions/workflows. **GATE_2B=OPEN, JANUS-R=NOT_VALIDATED**.

**LIRE EN PREMIER :** `research/STEP56_SHIFT_RESPONSE_AND_TEMPORAL_DIRAC_JETS_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step56-report.json`.
**NOUVEAU CODE :** `numerics/hr_step56_shift_response.py` SHA Git `71bc56d3433e146c5671351e6ea21468ee5149ca`.
**14 TESTS :** `tests/test_hr_step56_shift_response.py` SHA `75efdc7b99af067f3f7c2b1bc4947cb5a7c9e48f`.
**PROVENANCE FORMULES ORIGINALES :** GitHub `numerics/hr_step45_exact_physical_ward.py` SHA `66aa43841dccfe4a5d586a49be9c10af3a67a10e`; `numerics/hr_step46_exact_secondary_ode.py` SHA `bac025c28dbe1561c0c36c56dbfda46dc326f804`. Ces fichiers furent lus depuis GitHub pour construire ce **module algébrique autonome**, mais n'ont PAS été importés en octets originaux dans le test local Step56. Ne pas prétendre entière chaîne historiquement réexécutée.

## NOUVELLE AVANCÉE MATHÉMATIQUE EXACTE — OPÉRATEUR DE DÉPLACEMENT RELATIF POUR LE DIRAC TEMPOREL

Le Step55 a certifié le profil radial initial contraint et positif sur r∈[0,.85] dans les données prescrites, mais n'a PAS traité l'évolution en TEMPS. L'étape 56 repart de la VRAIE équation de stationnarité algébrique de l'action positive-EH sphérique à SIX couples canoniques :

```text
Dg = pSg*Sg' - Lg*pLg' + pg*theta_g'
K  = m² Mg² Lg Lf (beta1*Sg²+2 beta2*Sg Sf+beta3*Sf²)
Fz = Dg - K*z/sqrt(1-z²)=0
sur la branche K>0 :
z = Dg/sqrt(Dg²+K²)
delta_z = (K² delta_Dg - Dg*K delta_K)/(Dg²+K²)^(3/2)
dot_z   = (K² dot_Dg - Dg*K dot_K)/(Dg²+K²)^(3/2)
```

La variation `delta_Dg` comprend ABSOLUMENT `-Lg delta(pLg')`. Pour un test radial compact `eta(r)`, il en résulte le noyau Poisson fonctionnel DISTRIBUTIONNEL exact :

```text
Z_D = K²/(Dg²+K²)^(3/2)
delta z(r)/delta pLg(x) = -Lg(r)*Z_D(r)*partial_r delta(r-x)
delta/delta pLg(x) [ integral eta(r)*z(r) dr ]
    = +partial_x[eta(x)*Lg(x)*Z_D(x)]
```

Pour des variations non compactes, garder EXPLICITEMENT le bord `-[eta Lg Z_D delta pLg]`. Cette dérivée de fonction test est une contribution importante au véritable crochet secondaire temporel et peut introduire dérivées des lapses. L'identité exacte `delta(z')=(delta z)'` a également été vérifiée avec les jets radiaux. Le Hamiltonien réduit satisfait l'enveloppe stationnaire `partial_z(N Hg+M Hf)=(N/Lg+M/Lf)Fz=0` sur Fz=0, MAIS la variation de `C_red` **DOIT** inclure ses dépendances implicites à `z,z',...` ; figer z dans les deux variations est incorrect. Un exemple symbolique à SIX couples indépendants prouve que cette omission donne un crochet différent, mais cet EXEMPLE n'est PAS le Dirac physique JANUS.

**CENTRE NORMALISÉ :** `Dg=r³ d(s), K=r² k(s)>0, w=z/r=d/sqrt(k²+s d²)`. Sur le benchmark stationnaire `z=.004r`, `partial_d w=(1-s*.004²)^(3/2)/k` et `partial_k w=-.004*(1-s*.004²)/k`. La borne certifiée Step55 `k>0.229` donne les nouvelles marges rationnelles EXACTES `0<partial_d w<1000/229<4.367` et `|partial_k w|<4/229<.0175` sur s∈[0,.7225]. Ceci est une sensibilité de shift, PAS une preuve dynamique 4D.

## EXÉCUTION RÉELLE ET LIMITES

```bash
cd /mnt/data/janus-step56
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step56_shift_response.py
# 14 PASSED in 2.00s.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step56_shift_response
```

Les DEUX nouveaux fichiers CODE/TEST sont Git blob BYTE-IDENTICAL aux octets exécutés (vérifiés DIRECTEMENT dans GitHub). Le test local est AUTONOME et ne contient PAS tout l'ancien dépôt : pas de full-suite/CI, pas de vrai `{C,Htotal}` calculé. JSON brut local `/mnt/data/janus-step56/research/reports/step56_shift_local.json` SHA256 `7541d626330d4cc8589bbc264ede472b8b81b1a92efdf054bf97fbcf29f3341e`, NOT uploaded as standalone GitHub file ; éléments essentiels et tests dans `research/reports/gate2b-step56-report.json`.

## STEP57 — LE VÉRITABLE VERROU PHYSIQUE RESTE OUVERT

1. Reconstituer l'ORIGINAL COMPLET `Hg,Hf,C_exact` à six couples depuis les vrais sources GitHub, avec `z[Dg,K]`, `z'` et jets, et calculer réellement `{C_red,H_total,red}` par équations canoniques et variations fonctionnelles. Utiliser les dérivées de shift, dérivées des fonctions test et bords démontrés ici. Ne pas doubler les termes de chaîne dans H grâce au théorème d'enveloppe.
2. Résoudre/simplifier l'OPÉRATEUR SUR LES LAPSUS et déterminer le rang de Dirac, la conservation secondaire, la fixation du rapport des lapses, les branches exceptionnelles K/J, tous sur le profil initial positif Step55. Ne pas supposer d'avance une élimination du fantôme BD.
3. Vérifier le résultat avec un oracle Poisson indépendant sur l'action d'origine non intégrée par parties, et la régularité tensorielle du centre.
4. Continuer à PREPENDRE ce fichier GitHub après chaque étape. Actions toujours désactivées.

**STATUT SCIENTIFIQUE : opérateur de réponse du déplacement relatif établi EXACTEMENT ; VRAI CROCHET TEMPORAL ET RANG DIRAC NON CALCULÉS. GATE 2B OPEN ; JANUS-R NOT VALIDATED.**

**ADMIN GITHUB :** historiques des anciennes branches main/V2 préservés en ascendance active via commit `4f7a3a1`; PR V2 #1 fermée sans fusion ; mais GitHub garde TROIS références et le défaut `main`. Le connecteur ne possède toujours pas les actions de changement du défaut/suppression de ref ; propriétaire doit effectuer Settings > Default branch -> active, puis supprimer V2/main dans Branches. Ne jamais annoncer « une branche » avant contrôle.

---

# JANUS — REPRISE PRIORITAIRE : STEP55 TERMINÉ — 2026-10-23

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE AUX ÉCRITURES : research/gate2b-nonhomothetic-transfer. NE PAS RÉACTIVER GITHUB ACTIONS. Gate 2B OPEN ; JANUS-R NOT VALIDATED.**

**LIRE D'ABORD :** research/STEP55_GLOBAL_RADIAL_BARRIER_AND_POSITIVE_TWODUST_AUDIT.md
**RAPPORT MACHINE EXACT :** research/reports/gate2b-step55-report.json.
**NOUVEAU CODE NORMALISÉ :** numerics/hr_step55_normalized_secondary.py, Git blob a54a6acf2f7ad2f64c500faecfa1406ecbf7b862.
**NOUVEAU CODE D'INTERVALLES :** numerics/hr_step55_global_barrier.py, Git blob a6e7004120d0a166a3a8973c2fbe1487a8eb70fe.
**12 TESTS :** tests/test_hr_step55_global_barrier.py, Git blob 5dfb8036c66c9b2774847b0989be15ea41c65408.
**ORIGINAL PHYSIQUE BYTE-IDENTIQUE :** numerics/hr_step45_exact_physical_ward.py Git 66aa43841dccfe4a5d586a49be9c10af3a67a10e ; numerics/hr_step46_exact_secondary_ode.py Git bac025c28dbe1561c0c36c56dbfda46dc326f804.
**TOUR PRÉCÉDENT :** research/STEP54_CONDITIONAL_CONTINUUM_TWODUST_INTERVAL_TUBE_AUDIT.md, certificat rationnel conditionnel à |U-Ustar|,|V-Vstar|<=.01.

## GRANDE AVANCÉE : TUBE STEP54 DÉSORMAIS PROUVÉ POUR LA VRAIE SOLUTION RADIALE CONTRAINTE

Au centre sphérique la branche analytique locale unique satisfaisant C=0 était garantie conditionnellement par le théorème Step49. Étapes52/53 fournissent U1/U2 algébriques exacts pour paramètres rationnels décimaux. Step55 part de l'équation de la secondaire physique construite depuis les SIX couples canoniques originales Steps45/46 et élimine symboliquement les facteurs factices en r :

    s=r², U(s)=pLf(r)/r², V(s)=pLf'(r)/r
    Ustar(s)=U0+U1*s+U2*s²
    Vstar(s)=2*U0+4*U1*s+6*U2*s²
    V=G(s,U) ; 2s U_s = G(s,U)-2U ; G(0,U)=3U0-U

**NOUVEAU THÉORÈME DE BARRIÈRES INVARIANTES CONTINUES.** Sur EXACTEMENT tout s∈[0,.7225], recouvert par 256 cellules rationnelles et arithmétique d'intervalles entière arrondie vers l'extérieur à l'échelle 10^-28, on démontre pour les murs Ustar±delta, delta=1/10000 :

    Fplus(s)=G(s,Ustar+delta)-2(Ustar+delta)-2s Ustar'(s)
           <= -1480966474499367232302129/10000000000000000000000000000 <0
    Fminus(s)=G(s,Ustar-delta)-2(Ustar-delta)-2s Ustar'(s)
           >= 295653233337826329055403/2000000000000000000000000000 >0.

La solution analytique centrale commence strictement entre les murs, le théorème de premier-contact empêche toute sortie à s>0 et l'EDO lisse sur la charte compacte non dégénérée s'étend jusqu'à .7225. Donc **SUR LA VRAIE BRANCHE RADIALE EXACTE** :

    |U-Ustar| <= .0001   sur r∈[0,.85].

La dérivée V doit être bornée distinctement ; la même évaluation d'intervalles sur toutes les valeurs U du tube donne EXACTEMENT :

    -10209601928354599272595789/5000000000000000000000000000
       <= V-Vstar <=
     20404447710211286903383733/10000000000000000000000000000.

Donc **-0.00205<V-Vstar<0.00205<0.01** partout. Les deux hypothèses du CERTIFICAT CONTINU Step54 sont désormais démontrées pour la solution radiale RÉELLE, pas simplement une famille hypothétique.

**CONSÉQUENCE (SUR DONNÉES SPHÉRIQUES RADIALES PRESCRITES SEULEMENT) :**
    pg/r² > .8854 ; pf/r² > .063 ; J > .659 ; K/r² > .229,
avec les deux dénominateurs de poussière, Sf', sqrt(1-z²) strictement positifs sur tout [0,.85], centre normalisé compris. **Le verrou radial d'existence/positivité de CES DONNÉES INITIALES est désormais clos sur le benchmark explicite.**

**INTERDICTION ABSOLUE D'EN DÉDUIRE ABSENCE FANTÔME BD.** Il ne s'agit ni de véritable évolution en temps 4D, ni de rang de Dirac, ni de fixation des lapses, ni de preuve de régularité tensorielle complète au centre. Gate2B reste OPEN ; JANUS-R non validé.

## PROVENANCE, COMMANDES, TESTS RÉELLEMENT EXÉCUTÉS

    cd /mnt/data/janus-step55
    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step55_global_barrier.py
    # 12 PASSED in 3.85 s, EFFECTIVEMENT EXECUTED.
    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step55_global_barrier

Les 3 nouveaux fichiers CODE/TEST et les 2 véritables sources historique Steps45/46 sont **OCTET POUR OCTET IDENTIQUES** aux blobs GitHub ci-dessus et ont été relus de GitHub. Tests : SHA originals fail-closed, intervalle exact négatif/positif/radical, centres, couverture 256 cellules, barrières strictes, bornes V, raffinement 512, cas large delta_U=.001 REFUSÉ car V non certifié, RHS physique ORIGINAL NON-SIMPLIFIÉ évalué indépendamment à r=.05,.35,.85 contient les bornes normalisées, garde faux positif Dirac. Il n'y a PAS de suite historique GitHub TOTALE, ni CI/workflows, ni Dirac temporel.

Résultat brut local /mnt/data/janus-step55/research/reports/step55-global-barrier-local.json SHA256 4f22328452d36ee252f966fbe6a1fa476e7aaba8daee43ec9d555b11619f0cfd ; PAS uploadé séparément. Résultats exacts sauvegardés dans rapport GitHub machine.

## NEXT STEP56 — PRIORITÉ MAINTENANT DIRAC TEMPOREL, PLUS LE RADIAL

1. Décomposer précisément l'action sphérique ORIGINAL non intégrée par parties pour calculer la **VRAIE PRÉSERVATION TEMPORELLE {C,Htot}**, six couples canoniques, deux lapses et déplacement relatif éliminé en respectant ses variations. Évaluer rang de Dirac et fixation des lapses pour la branche positive maintenant certifiée ; étudier J/K branches exceptionnelles/bords.
2. Vérifier indépendamment le crochet Poisson complet original non-IBP sur le profil exact radial construit avec barrières, sans confondre le résidu algébrique C=0 par construction avec une vraie vérification fonctionnelle.
3. Analyser la régularité sphérique CARTÉSIENNE/TENSORIELLE complète du centre et des évolutions 4D. Aucun résultat Step55 ne vaut absence de fantôme ni validité cosmologique.
4. Continuer à committer code/tests/rapport et PREPENDRE ce point de reprise après chaque avancée. Ne réactiver aucune GitHub Action.
5. ADMINISTRATIF : historique main/V2 déjà préservé dans branche active grâce au commit à double-parent 4f7a3a1, PR V2 #1 fermée non-fusionnée, mais Github a encore **3 branches NOMMÉES / défaut main**. Le connecteur ne donne pas changer défaut/supprimer des branches ; seul le propriétaire peut dans Github UI désigner active comme défaut puis supprimer V2/main. Ne jamais prétendre que l'unification des noms est faite.

**VERDICT : Step55 solution C=0 radiale du benchmark analytique régulier étendue jusque .85 avec deux poussières positives SUR LE CONTINUUM ; mais FULL DIRAC/TEMPORAL GATE2B OPEN et JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP54 TERMINÉ — 2026-10-23

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE POUR LES ÉCRITURES :** `research/gate2b-nonhomothetic-transfer`. Ne PAS réactiver GitHub Actions/workflows. Ne PAS modifier le `main` historique ni `research/v2-flrw`. **GATE 2B OUVERT ; JANUS-R NON VALIDÉ.**

**À LIRE ABSOLUMENT EN PREMIER :** `research/STEP54_CONDITIONAL_CONTINUUM_TWODUST_INTERVAL_TUBE_AUDIT.md`.
**RAPPORT MACHINE / FRACTIONS EXACTES :** `research/reports/gate2b-step54-report.json`.
**CODE D'INTERVALLES :** `numerics/hr_step54_interval_tube.py`, Git blob `c2db1e6a4888194fc6f79aaee866efdad479dbfb`.
**9 TESTS :** `tests/test_hr_step54_interval_tube.py`, Git blob `d1dc7407ae1781aa742cab09cff0fc5a24bce66e`.
**FOURNISSEURS ORIGINAUX OCTET-IDENTIQUES GITHUB :** `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et `numerics/hr_step46_exact_secondary_ode.py` blob `bac025c28dbe1561c0c36c56dbfda46dc326f804`. Ces deux copies originales ont été effectivement vérifiées par le programme de Step54 en local.
**PRÉCÉDENT CENTRE :** `research/STEP53_EXACT_CENTER_U2_AND_SHOOTING_AUDIT.md` et `research/reports/gate2b-step53-report.json` (U0,U1,U2 exacts dans corps quadratique rationnel du benchmark).

## AVANCÉE STEP54 : POSITIVITÉ *CONTINUE* POUR UNE CLASSE CONDITIONNELLE DE PROFILS

Nouvelle preuve de **signes continus sur TOUT `r∈[0,.85]`** grâce à 256 cellules d'intervalles exacts en `s=r²∈[0,.7225]`, chacune couvrant tous les réels de sa cellule (AUCUN échantillonnage flottant pour les signes). Arithmétique par entiers à grille `1e-30`, arrondis sortants sur TOUS `+,-,*,/,sqrt`, `math.isqrt`, bornes RATIONNELLES certifiées pour U1/U2 des étapes52/53. Le centre r=0 est compris par normalisation analytique.

Pour le benchmark sphérique prescrit, posons `P(r)=pLf(r)`, `U=P/r²`, `V=P'/r`, `Ustar(s)=U0+U1*s+U2*s²` et `Vstar(s)=2U0+4U1*s+6U2*s²`.

**THÉORÈME DE SIGNES CONDITIONNEL :**
```text
SI POUR TOUT r in [0,.85], (par prolongement régulier en r=0) :
   |U(r²)-Ustar(r²)| <= 0.01
   |V(r²)-Vstar(r²)| <= 0.01
ALORS SUR TOUT CE CONTINUUM :
   pg/r² > 0.8854
   pf/r² > 0.063
   J > 0.659
   K/r² > 0.229
   both dust lapse coefficients >0.998
   Sf' >0.230
   sqrt(1-z²)>0.9999
```

Les fractions inférieures EXACTES sont sauvegardées in extenso dans rapport machine. Tube plus fin `delta=0.0001` permet `pf/r²>0.1111`. Source de poussière f vérifiée indépendamment en mpmath 75 chiffres sur quatre rayons contre l'expression symbolique ORIGINALE `hr_step46_exact_secondary_ode.py:p_f`.

**TRÈS IMPORTANT : NOUS N'AVONS PAS PROUVÉ QUE LA SOLUTION RADIALE EXACTE DE `pLf'=-C0/C1` APPARTIENT À CE TUBE.** Donc encore AUCUNE preuve d'existence globale exacte ou de positivité positive de la vraie trajectoire, malgré la preuve continue CONDITIONNELLE. Le prochain verrou est désormais **UNE INÉGALITÉ DE PROXIMITÉ SUR LA SOLUTION ET SA DÉRIVÉE NORMALISÉE**, pas un nouveau simple tableau d'échantillons.

## TESTS RÉELLEMENT PASSÉS ET REPRODUCTION

```bash
# Depuis checkout contenant scripts Github authentiques
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step54_interval_tube.py
# EFFECTIVEMENT EXÉCUTÉ EN LOCAL /mnt/data/janus-step54 : 9 PASSED en 2.03s.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -c 'import json;from numerics.hr_step54_interval_tube import certify;print(json.dumps(certify(256,"0.01"),indent=2))'
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step54_interval_tube
```

Les deux nouveaux blobs GitHub CODE/TEST = EXACTEMENT OCTETS EXÉCUTÉS. Deux vrais sources physiques historiques Step45/46 aussi byte-identical aux blobs GitHub. Ne pas affirmer une exécution complète des historiques Step33g→53 : tests ciblés 9, pas suite entière, pas CI. Une première version a échoué sur une garde de `profiles(s<0)` : bug CORRIGÉ puis les neuf tests RÉUSSIS.

JSON des 256 cellules locales : `/mnt/data/janus-step54/research/reports/gate2b-step54-tube_001.json`, SHA256 `708fad17c8e88520a0eb0122a49c60caaa22daeb09be543a0e513ef08dc2c378` ; `gate2b-step54-tube_0001.json`, SHA256 `c60f48da3569ec40e7e8a1c024af061eb35e2e8d5234f5dce130fc9b36b24212`. Les traces n'ont PAS été uploadées séparément mais leurs minima rationnels, le code régénérateur et toutes données essentielles figurent dans `research/reports/gate2b-step54-report.json`.

## NEXT STEP55 : DERNIER VERROU RADIAL FORMALISÉ

1. **CERTIFIER L'APPARTENANCE DE LA VRAIE SOLUTION AU TUBE** : à partir de `2s U_s=G(s,U)-2U`, `G(0,U)=3U0-U`, et des U1/U2 algébriques exacts, construire des bornes d'EDO a posteriori à intervalles (barrières haute/basse, contraction Picard ou Chebyshev). Prouver `|U-Ustar|<=0.01` ET `|V-Vstar|<=0.01` de s=0 à .7225. La preuve de signes Step54 s'appliquera alors AUTOMATIQUEMENT à la véritable solution. Chercher des seuils plus fins si utile.
2. Après cela relancer un oracle Poisson NON-IBP original pour la trajectoire enveloppée ; ne pas compter le résidu C par construction comme contrôle indépendant.
3. **TOUJOURS MAJEUR :** calculer le vrai crochet de PRÉSERVATION TEMPORELLE `{C,H_total}` de l'action originale avec SIX couples canoniques, bords, fixation des lapses, rang de Dirac, chartes J/K exceptionnelles. Rien de cela n'est établi par Step54.
4. Enfin éventuelle évolution cosmologique non homothétique on shell et stabilité même action ; manuscrit externe JHR de signe f-EH opposé reste voie d'audit distincte.
5. **ADMIN GITHUB** : les anciens commits main/V2 sont déjà ancêtres de la branche active par `4f7a3a1`, la PR brouillon historique #1 est fermée sans fusion. GitHub affiche encore TROIS branches avec défaut `main`. Le connecteur ne sait toujours PAS modifier le défaut ni supprimer refs. Propriétaire via Settings > Default branch choisir active, puis supprimer V2/main dans Branches. Ne pas prétendre suppression faite avant vérification.

**STATUT FINAL : PROPOSITION DE POSITIVITÉ RIGOUREUSE SUR TOUT LE CONTINUUM SOUS HYPOTHÈSE DE TUBE, HYPOTHÈSE NON ENCORE PROUVÉE POUR LA VRAIE EDO ; CONSERVATION TEMPORELLE DIRAC NON CALCULÉE ; GATE_2B=OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP53 TERMINÉ — 2026-10-22

**LIRE CETTE SECTION EN PREMIER.** Branche scientifique ACTIVE UNIQUEMENT : `research/gate2b-nonhomothetic-transfer`. Ne PAS réactiver GitHub Actions/workflows ni modifier `main`/V2. **Gate 2B OUVERT, JANUS-R NON VALIDÉ.**

**AUDIT SCIENTIFIQUE :** `research/STEP53_EXACT_CENTER_U2_AND_SHOOTING_AUDIT.md`.
**RAPPORT MACHINE AVEC FRACTIONS EXACTES :** `research/reports/gate2b-step53-report.json`.
**CODE U2 :** `numerics/hr_step53_exact_center_u2.py`, Git blob `ee4515190e5b1733fb94641e6344e4ee96cdef6c`.
**CODE TIR DOP853 :** `numerics/hr_step53_outward_compare.py`, Git blob `7a445614167a4cb7304aec7d19f38295d32a8890`.
**TESTS :** `tests/test_hr_step53_exact_center_u2.py`, Git blob `4e1848157c6ec95c7a0d6e73c0921573605f7117`.
**BASE :** Step52 `research/STEP52_EXACT_CENTER_U1_RATIONAL_TAYLOR_AUDIT.md`, vraies équations physiques de Step45/46.

## NOUVELLE AVANCÉE ANALYTIQUE DÉMONTRÉE : SECOND COEFFICIENT CENTRAL U2

Pour la même famille de données canoniques sphériques primaires-réduites et les paramètres du benchmark traités comme rationnels décimaux EXACTS,

```text
pLf(r)=r² [U0+U1 r²+U2 r⁴+O(r⁶)],
s=r², G(s,U)=pLf'(sqrt(s),pLf=sU)/sqrt(s), G(0,U)=3U0-U
5U1 = partial_s G(0,U0)
7U2 = (1/2)partial_ss G(0,U0) + partial_sU G(0,U0)*U1
     + (1/2)partial_UU G(0,U0)*U1².
U2=A2+B2*sqrt(H²), H²,A2,B2 EXACTEMENT RATIONNELS,
U2≈-0.000010073853486743828175736890952863935933883641943763773429699704274
```

**EXACT U2 EST CERTIFIÉ NÉGATIF** dans le modèle rationnel : `rational_interval(...,digits=100)` sur la racine positive `sqrt(H²)` utilise `isqrt` et des fractions exactes, donne largeur < `1e-100`. Le rapport machine conserve IN EXTENSO les trois fractions A2, B2, H² ; aucune perte de précision dans le dépôt.

Le programme évalue deux fois le SECOND MEMBRE de `C=0` construit depuis les VRAIES FORMULES sphériques Step45/46 : au premier passage `pLf=r²U0` il retrouve exactement les fractions de U1 du Step52 ; au second `pLf=r²(U0+U1r²)`, le terme r³ est EXACTEMENT `4U1`, r⁵ est `7U2`. Jets de Laurent quadratiques `Q(sqrt(H²))` avec inverses/racines par récurrences EXACTES et propagation conservative des premières puissances inconnues. Les ordres tronqués **12,14,18,22 donnent A2 et B2 IDENTIQUES bit-à-bit**, et les premiers termes inconnus ne peuvent entrer qu'en r^7,r^9,r^13,r^17 > r⁵. Ce certificat est LOCAL, il n'établit aucune existence globale.

## CONTRÔLE NUMÉRIQUE DU GAIN SUR LE TIR DEPUIS LE CENTRE

Même équation physique `pLf'=-C0/C1` évaluée sur les données de fond courbes/DEUX poussières/non-comobiles du benchmark ; solveur `scipy solve_ivp DOP853`, `rtol=2e-12`, `atol=1e-18`, pas max `.012`. Référence interne depuis `eps=.001` avec les trois coefficients : `pLf(.85)=-.0033864293564879076`.

```text
eps     |fin avec U0+U1 - référence|    |fin avec U0+U1+U2 - référence|
.05          9.270795936489051e-15             4.336808689942018e-19
.025         8.109832250191573e-17             3.0357660829594124e-18
.0125        1.0842021724855044e-17            8.239936510889834e-18
.00625       2.168404344971009e-18            9.974659986866641e-18
```

**Ces écarts sont des COMPARAISONS à une référence NUMÉRIQUE, PAS bornes d'erreur certifiées.** Les chiffres se saturent au plancher binaire pour les petits rayons. Les poussières positives sur tout le CONTINUUM et une solution exacte prolongée jusqu'à .85 restent NON démontrées. Le C calculé de l'EDO est petit PAR CONSTRUCTION, distinct des contrôles du Poisson original Step48.

## TESTS EFFECTIVEMENT EXÉCUTÉS ET PROVENANCE

```bash
cd /mnt/data/janus-step53
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step53_exact_center_u2.py
# 9 PASSED IN 12.62s.

for j in 12 14 18 22; do
  JANUS_JET_ORDER=$j OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step53_exact_center_u2
done
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step53_outward_compare
```

**Les TROIS nouveaux fichiers sont BYTE-IDENTICAL aux fichiers locaux qui ont été réellement exécutés**, blobs GitSHA ci-dessus. Les sources historiques Step45/46 du PETIT ENVIRONNEMENT LOCAL ont été reconstituées fidèlement par leurs équations, **MAIS ne sont PAS octet pour octet les fichiers originaux GitHub dans ce tour**. Le dépôt GitHub importe les véritables sources historiques et la réexécution intégrale U2 avec les octets originaux reste **PENDING**. Il serait FAUX de compter cette session comme full original-provider regression. La suite complète et CI non exécutées ; Actions désactivées.

JSON détaillés générés localement, NON uploadés séparément : `research/reports/step53-u2-raw.json` SHA256 `44244e855f6f0cd8b7fdbe53c145fdab6e9c7aa872e61a6dd72232177ffd445c`, `research/reports/step53-shoot-raw.json` SHA256 `d7d7b1c68e28b36859322b7efc19ddbce01b5279717829d729013fa368e6b573`. A2/B2/H² et tous les chiffres principaux sont dans rapport GitHub.

## STEP54 — VERROUS À TRAITER APRÈS INTERRUPTION

1. **REPRODUCTIBILITÉ** : constituer un checkout original entier Step33g→53 sans adaptateurs et re-exécuter le module U2 + tests ainsi que les deux contrôles historiques Step48 complets.
2. **RIGUEUR GLOBALE** : à partir du vrai U0,U1,U2, construire une continuation EDO VALIDÉE par intervalles depuis r=0 jusqu'à r=.85, avec preuve de `pg/r²,pf/r²,J,K/r²>0` sur TOUT L'INTERVALLE du nouveau profil et bords sphériques réguliers. Pas seulement des échantillons ni des écarts entre solveurs.
3. **THÉORIE DYNAMIQUE** : dériver/calculer `{C,H_total}` temporel avec TOUS les 6 couples canoniques, régler fixation lapses/rapport lapses, matrice de Dirac, J/K exceptionnels et bords. C'est le verrou physique fondamental ; Ward et EDO spatiale seuls n'éliminent PAS un fantôme.
4. Ensuite seulement évolution non homothétique on-shell, stabilité même action De Felice/Aoki et confrontations empiriques.
5. **ADMIN GITHUB** : histoire `main`+V2 déjà préservée dans l'ascendance active par `4f7a3a1`, ancienne PR#1 fermée sans fusion. Mais GitHub affiche encore TROIS refs ; défaut `main`. Aucune fonction disponible pour supprimer ces refs/changer défaut ; propriétaire doit via UI changer défaut vers active, PUIS supprimer V2 et main. Ne pas prétendre 1 branche avant vérification réelle.

**VERDICT : U2 EXACT ALGÉBRIQUE CERTIFIÉ LOCAL SUR BENCHMARK RATIONNEL, TIR AMÉLIORÉ ; GATE_2B OPEN, JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP52 TERMINÉ — 2026-10-22

**BRANCHE SCIENTIFIQUE AUTORISÉE UNIQUEMENT :** `research/gate2b-nonhomothetic-transfer`. Ne pas écrire dans `main`, `research/v2-flrw`, ne pas réactiver Actions/workflows. **NE PAS AFFIRMER JANUS-R VALIDÉ**.

**LIRE D'ABORD :** `research/STEP52_EXACT_CENTER_U1_RATIONAL_TAYLOR_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step52-report.json` contient les fractions EXACTES A,B,H² et les bornes.
**NOUVEAU CODE :** `numerics/hr_step52_exact_center_taylor.py`, Git blob `b7da7e5272e08819fc89053fdf15852fcf4cc536`.
**NOUVEAUX TESTS :** `tests/test_hr_step52_exact_center_taylor.py`, Git blob `cf9416641583de47ab0d60f4527bca7ce60d2806`.
**DÉPENDANCES PINNÉES EXACTES :** `numerics/hr_step45_exact_physical_ward.py` SHA `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `numerics/hr_step46_exact_secondary_ode.py` SHA `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
**PRÉCÉDENT :** `research/STEP51_AUTHENTIC_CENTER_U1_AND_BRANCH_ADMIN_AUDIT.md`.

## AVANCÉE PRINCIPALE : COEFFICIENT U1 EXACTEMENT ALGÉBRIQUE ET BORNÉ

Au lieu de l'estimation non rigoureuse de Step51, calcul par jets de LAURENT avec coefficients `A+B*sqrt(H²)` dans le corps quadratique rationnel de la calibration sphérique Step41, à partir du SECOND MEMBRE PHYSIQUE de l'EDO `pLf'=-C0/C1` dérivée du vrai noyau de Poisson sphérique à six couples canoniques.

```text
pLf(r) = r² (U0 + U1*r² + ...)
U0 = Mf²*b*(Pg/(Mg²*a)-2*z1)
G(s,U) = pLf'(sqrt(s), pLf=s*U)/sqrt(s) ; G(0,U)=3U0-U
U1 = (partial_s G)(0,U0)/5
U1 = A + B*sqrt(H²)   ;   A,B,H² EXACTEMENT RATIONNELS
0.0007897451667202464909325108904961683602148118201690
   < U1 <
0.0007897451667202464909325108904961683602148118201692
```

Le programme calcule les deux fractions A,B exactement avec `Fraction` (et H²). Radicaux et dénominateurs développés en jets formels avec propagation conservatrice de la première puissance inconnue. Les TRONCATURES 14,20,26 donnent EXACTEMENT les mêmes A,B ; les termes omis ne peuvent atteindre les puissances r^0..r³ (leurs ordres d'inconnu : r^9,r^15,r^21). La racine positive sqrt(H²) est encadrée par `isqrt` sur grille 10^-90, puis A+B sqrt(H²) par EXACTES fractions. Largeur réelle de l'encadrement ≈8.30667e-96, donc <1e-80. AUCUNE extrapolation numérique utilisée pour la preuve de cette valeur centrale.

**Limite** : le certificat vaut pour les paramètres de l'étalonnage imprimé traités comme fractions décimales exactes, et pour l'action sphérique primaire-réduite. Pas une borne sur les arrondis binary64 du logiciel historique, ni une solution radiale complète.

## TESTS ET PROVENANCE — RÉELLEMENT EXÉCUTÉS

```bash
cd /mnt/data/janus-step52
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step52_exact_center_taylor.py
# ACTUELLEMENT EXÉCUTÉ : 8 PASSED in 11.01s

JANUS_JET_ORDER=14 OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step52_exact_center_taylor
JANUS_JET_ORDER=20 OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step52_exact_center_taylor
JANUS_JET_ORDER=26 OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step52_exact_center_taylor
```

Les deux nouveaux fichiers code/tests ont des Git blobs EXACTEMENT IDENTIQUES aux octets locaux exécutés ; les deux fournisseurs historiques Step45/46 sont eux aussi bit-identiques GitHub. Contrôles : SHA fail-closed, corps quadratique, coefficients centraux/termes absents, reste jet >r³, même A,B à 3 ordres, bornes fractions strictes et oracle haute précision Step51 indépendant. C'est une suite ciblée, pas le dépôt entier.

Le JSON brut local réellement généré `/mnt/data/janus-step52/research/reports/step52-u1-jet-20.json` a SHA256 `069191a6e92c7474677c3b5a004de0affba94c1ede63f1debfe253d09d3fca6f` mais n'a PAS été uploadé séparément ; les fractions exactes A,B,H² et les bornes sont enregistrées dans le rapport GitHub `research/reports/gate2b-step52-report.json`.

## BRANCHES — RÉDUCTION NOMINALE ENCORE NON RÉALISÉE

Commits des 3 branches déjà préservés sans changement de tree dans l'ascendance active grâce au commit `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7`. PR brouillon historique #1 **FERMÉE SANS FUSION**. Mais GitHub a TOUJOURS `default=main`, trois refs `main`, `research/v2-flrw`, `research/gate2b-nonhomothetic-transfer`. Le connecteur n'offre pas modifier branche par défaut ni supprimer des refs. Propriétaire : changer Default branch à `research/gate2b-nonhomothetic-transfer` dans Settings, PUIS supprimer V2 et main dans Branches, puis vérifier liste réelle. Ne pas mentir sur cette opération.

## NEXT STEP53 : PRIORITÉ SCIENTIFIQUE

1. Utiliser CE VRAI U1 (exact) dans le tir régulier depuis r≈0 ; développer éventuellement U2 avec jets à reste contrôlé. Évaluer les différences de raccordement sans les présenter comme borne d'erreur globale.
2. Réunir en un SEUL checkout tous les imports upstream historiques Step33g/37/45/46/47/48 strictement byte-identiques ; relancer sans filtre la suite Step48 puis tests Step49/51/52. Deux imports antérieurs encore adaptateurs sont à remplacer.
3. Construire un vrai certificat continu de prolongement régulier U(s) sur [0,.85], densités poussières `pg/r²,pf/r²>0`, chartes J,K/r², et bornes de résidu/EDO.
4. Calculer la VRAIE préservation temporelle `{C,Htot}` des six couples canoniques avec bords, rang de Dirac et fixation des lapses. Ne pas déduire ghost-free du calcul du coefficient central.
5. Veiller à tenir `00_CURRENT_RESTART.md` et GitHub à jour à chaque interruption.

**VERDICT : U1 ANALYTIQUE EXACT POUR BENCHMARK RATIONNEL = CERTIFIÉ ; SOLUTION RADIALE GLOBALE ET DIRAC TEMPOREL NON ÉTABLIS ; GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

---

# CORRECTION D'AUTORISATIONS GITHUB — VÉRIFIÉ 2026-10-22

**Fait établi :** le compte GitHub authentifié `alexandrebarault-arch` possède `permission=admin` sur `alexandrebarault-arch/Janus` (outil GitHub `get_repo_collaborator_permission`). Les affirmations antérieures laissant entendre que l'UTILISATEUR n'avait pas les droits sont ERRONÉES. Il possède bien l'administration du dépôt.

**Limite DISTINCTE :** la connexion disponible dans CETTE conversation est une installation GitHub App aux permissions restreintes et aux fonctions explicitement limitées : elle peut créer/mettre à jour fichiers, commits et pointer une ref vers un commit, **mais NE FOURNIT NI modification de `default_branch` NI `DELETE git/refs/heads/...`**. La fonction de lecture générique GitHub `fetch` n'autorise que `GET` et sa documentation indique que les installations d'app n'ont pas l'accès `administration`. Le terminal local possède `git` mais ne dispose ni de `gh`, ni de credential GitHub configuré, ni de résolution DNS valide vers `api.github.com`. Ne pas confondre cette impossibilité *du connecteur* avec un manque de droits du compte.

**État distant vérifié :** branche par défaut = `main`; 3 refs toujours présentes (`main`, `research/gate2b-nonhomothetic-transfer`, `research/v2-flrw`). Les anciennes pointes sont préservées dans l'ascendance active via commit `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7`, sans changement d'arbre scientifique. PR historique #1 fermée non fusionnée. **Suppression NON FAITE** et aucune promesse d'avoir ramené effectivement le dépôt à une branche.

**Action admin restante quand un vrai client GitHub avec autorisation d'administration est disponible :** PATCH default_branch vers `research/gate2b-nonhomothetic-transfer`, puis DELETE ref `heads/research/v2-flrw` et DELETE ref `heads/main`; vérifier qu'une seule ref reste. Ne pas tenter de simuler la suppression en effaçant les fichiers ou en forçant `update_ref` vers un autre SHA. Via interface GitHub : Settings > General > Default branch, puis page Branches pour suppression.

**Reprise scientifique :** inchangée, étape 52 selon le bloc d'étape 51 ci-dessous. Gate2B OPEN, JANUS-R NOT VALIDATED.

---

# JANUS — REPRISE STEP51 : ADDENDUM SOURCE-AUTHENTIC (2026-10-22)

**REPRENDRE ICI AVANT LE TEXTE PRÉCÉDENT.** Dernier audit : `research/STEP51_AUTHENTIC_CENTER_U1_AND_BRANCH_ADMIN_AUDIT.md` section 5. Rapport : `research/reports/gate2b-step51-report.json`.

## NOUVELLE AVANCÉE DEPUIS LE PREMIER CHECKPOINT STEP51

La chaîne Step48 à CINQ providers historiques strictement byte-identiques est effectivement reconstituée et vérifiée `check_git=True` : `hr_step37_original_nonibp_oracle.py` `005449ade6`, `hr_step45_exact_physical_ward.py` `66aa43841`, `hr_step45_secondary_point_certificate.py` `6ab94dacb`, `hr_step46_exact_secondary_ode.py` `bac025c28`, `hr_step47_interior_ivp.py` `c558a827`. Le programme Step48 original `hr_step48_original_ivp_oracle.py` `dc5101d4` est LUI AUSSI identique octet pour octet. L'ancienne obstruction de vérification des 5 hash est donc levée.

Crochet Poisson ORIGINAL NON-IBP à 12 champs / 6 couples sur nouvel IVP et DEUX lapses : `N=161 A=-5.909466451194632e-7 B=-9.466192080859973e-7` ; `N=321 A=-1.4770852485167414e-7 B=-2.3664938826562995e-7` ; `N=641 A=-3.6925374684076886e-8 B=-5.916200850443823e-8`. Ces crochets FINIS ne sont PAS nuls exactement, mais diminuent comme ~h². Cette session utilise encore 2 **adaptateurs d'IMPORT SEULEMENT** dans les sources upstream `hr_curved_moving_dust_primary.py` (constantes/R) et `hr_curved_primary_mixed_kernel.py` (ordre Q) ; **pas de régression totale intégralement authentifiée**. Les anciens tests du fichier Step48 complet ne sont pas relancés, mais leurs deux fonctionnalités en attente ont été exercées par des tests NEW.

**TESTS RÉELLEMENT EXÉCUTÉS :**
```bash
cd /mnt/data/janus-step51
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step51_highprecision_center.py tests/test_hr_step51_original_chain.py
# 13 PASSED, 14.54s (7 Step51 centre haute précision + 6 véritable chaîne Step48)
```
NOUVEAU TEST GITHUB : `tests/test_hr_step51_original_chain.py` Git blob `2687e7279ddda3c1b0bc8ea2ba340cab0ce3499d`, identique à l'exécuté.

## BRANCHES — DEMANDE UTILISATEUR ENCORE PARTIELLEMENT ADMINISTRATIVE

Préservation des commits des 3 branches dans une SEULE ascendance active : commit `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7` arbre inchangé. PR historique #1 FERMÉE et NON fusionnée. **MAIS default=main, 3 refs demeurent** : `main`, `research/v2-flrw`, `research/gate2b-nonhomothetic-transfer`. Connector GitHub ne fournit pas la modification de branche par défaut ni la suppression de refs. Pour terminer : utilisateur via GitHub Settings > General > Default branch sélectionner `research/gate2b-nonhomothetic-transfer`, puis Branches supprimer `research/v2-flrw` et `main`. Vérifier réel affichage une seule branche. Ne PAS prétendre suppression faite.

## NEXT STEP52

1. Reconstituer les DEUX sources upstream `hr_curved_moving_dust_primary.py` et `hr_curved_primary_mixed_kernel.py` exactement ; relancer la suite complète Step48 originelle sans filtre et tests Step49/51.
2. U1 actuellement NUMÉRIQUE 120 chiffres `0.00078974516672024649093251089049616836021481...`, original Step45/46 strict byte-identical ; DERIVER / CERTIFIER U1 algébriquement par jets Taylor et intervalle.
3. Certifier l'EDO régulière du centre jusque r=.85 et densités poussières positives EN CONTINU ; les échantillons restent insuffisants.
4. VRAIE PRÉSERVATION TEMPORELLE de C, rang de Dirac, fixation des lapses et chartes exceptions J/K sont TOUJOURS NON ÉTABLIS. **Gate2B OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP51 TERMINÉ — 2026-10-22

**SEULE BRANCHE SCIENTIFIQUE AUTORISÉE AUX ÉCRITURES :** `research/gate2b-nonhomothetic-transfer`. **NE PAS RÉACTIVER GitHub Actions/workflows.** Ancien `main` et V2 ne doivent plus recevoir de commits scientifiques.

**DOCUMENT PRINCIPAL :** `research/STEP51_AUTHENTIC_CENTER_U1_AND_BRANCH_ADMIN_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step51-report.json`.
**NOUVEAU CALCULATEUR :** `numerics/hr_step51_highprecision_center_coefficient.py` SHA Git blob `97fe8f78a5daa91a8c74b14382470857c9ce29e2`.
**NOUVEAUX TESTS :** `tests/test_hr_step51_highprecision_center.py` SHA `da85a6e4da8c7202da6d1d5e81fd1aeb8a964e3e`.
**SOURCE HISTORIQUE STEP45 :** `numerics/hr_step45_exact_physical_ward.py` SHA `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
**SOURCE HISTORIQUE STEP46 :** `numerics/hr_step46_exact_secondary_ode.py` SHA `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
**BRANCHES/PR :** `research/BRANCH_CONSOLIDATION_2026-10-22.md`.

## LE POINT DEMANDÉ : UNE SEULE BRANCHE — HISTORIQUES PRÉSERVÉS, DEUX RÉFÉRENCES ENCORE À SUPPRIMER

- Avant : `main` HEAD `aead63f4`, `research/v2-flrw` HEAD `dfa497cc` avec 203 commits divergents, actif `research/gate2b-nonhomothetic-transfer`. Le commit `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7` a fusionné leur ASCENDANCE (deux parents) en laissant l'arbre de fichiers actifs **STRICTEMENT IDENTIQUE**. Vérification GitHub : `behind=0` pour les deux anciennes pointes par rapport à l'actif. AUCUN commit perdu, AUCUN fichier ancien V2 écrasant les nouveaux.
- La **pull request brouillon historique #1 est FERMÉE sans fusion** via le connecteur, état GitHub `closed/merged=false`.
- **TOUJOURS 3 BRANCHES NOMMÉES SUR GITHUB** : défaut actuel `main`, plus `research/gate2b-nonhomothetic-transfer`, plus `research/v2-flrw`. Ne PAS déclarer avoir réellement réduit à une branche.
- **L'OUTIL GITHUB DISPONIBLE NE PERMET PAS** changer `default_branch` ou supprimer une ref. **OPÉRATION RESTANTE POUR LE PROPRIÉTAIRE VIA UI** : dans repo Settings > General > Default branch, choisir `research/gate2b-nonhomothetic-transfer` ; puis dans Branches supprimer `research/v2-flrw`, ensuite `main`, APRES avoir changé la branche par défaut ; contrôler que liste = 1. Ancienne PR n'a plus besoin d'être traitée.
- Ne pas tenter une destruction artificielle du contenu des anciennes branches : cela ne supprimerait pas les refs et risquerait de corrompre l'historique.

## PROGRÈS SCIENTIFIQUE STEP51 — VRAIES SOURCES GITHUB, U1 PLUS PRÉCIS

Cette session a reconstitué en local les VRAIS fichiers historiques STEP45 et STEP46 octet par octet (empreintes ci-dessus, confirmées par `git hash-object`). Le nouveau programme refuse une modification de leur SHA. Dans le modèle sphérique Hamiltonien positif-EH HR à DEUX poussières et calibration décimale rationnelle, avec les g primaires reconstruites et `pLf=r² U0`, il calcule le second membre exact de la contrainte secondaire `pLf'=-C0/C1` à précision `mpmath` **100–120 chiffres**, pour extraire numériquement

```text
s = r², pLf=r² U(s)
G(s,U0) = pLf'(sqrt(s), pLf=s U0)/sqrt(s)
U1 = partial_s G(0,U0)/5   [FORMULE EXACTE si G analytique dans la charte]
U1 ≈ 0.0007897451667202464909325108904961683602148118202349246798
U1 de Step49 en double : 0.0007897451669079507
écart ancien - nouveau ≈ +1.877042090674891095e-13.
```

Quatre paires de rayons décroissants `(10^-7,10^-8)` jusqu'à `(10^-10,10^-11)` et extrapolation principale `O(r²)` donnent les mêmes 35 premiers chiffres environ ; stabilité vérifiée à 80 et 120 chiffres. **N'EST PAS UN ENCADREMENT RIGOUREUX DE U1**, car le reste d'extrapolation en rayon n'est pas mathématiquement borné.

## TESTS RÉELLEMENT EXÉCUTÉS — PAS ENTIÈRE SUITE

```bash
cd /mnt/data/janus-step51
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step51_highprecision_center.py
# ACTUELLEMENT : 7 PASSED en 1.85 s ; fichiers NEW et vrais providers45/46 byte-exacts.
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step51_highprecision_center_coefficient
```

Deux nouveaux blobs GitHub vérifiés égal aux OCTETS exécutés; sources Step45/46 strictement égales à GitHub. Les historiques complémentaires `hr_step45_secondary_point_certificate.py`, Step47/Step48 sont toujours à reconstituer ensemble pour débloquer les DEUX tests Step48 authentiques encore en attente. Aucun contrôle sur la vraie évolution Dirac, aucune borne global ODE, aucun CI/workflow.

## NEXT — STEP52

1. Dériver **EXACTEMENT** `U1=∂_s G(0,U0)/5` comme expression algébrique, ou une borne rationnelle certifiée par jets/Taylor, sans extrapolation non contrôlée.
2. Reconstituer la CHAÎNE AUTHENTIQUE COMPLÈTE Step45/46/47/48 et relancer les 2 tests Step48 longtemps désélectionnés, en plus des nouveaux tests ; ne pas appeler ce résultat complet avant exécution.
3. Construire une continuation par EDO à intervalles ou barrière analytique jusqu'à `.85`, certifier en continu `pg/r²>0,pf/r²>0,J>0,K/r²>0` pour les nouvelles données initiales régulières au centre.
4. Ensuite le VERROU MAJEUR : calculer `{C,Htot}` temps avec TOUS six couples canoniques et bords, rang Dirac et fixation des lapses. Ni Ward ni intégration radiale ne démontrent absence du fantôme BD.
5. Quand le propriétaire a exécuté changement défaut et deux suppressions des refs, vérifier sur GitHub qu'il ne reste vraiment qu'UNE branche ; ne pas modifier `main` tant qu'elle existe.

**STATUT : HISTORIQUES GIT CONSOLIDÉS ET PR BROUILLON FERMÉE ; MAIS 3 REFS GITHUB ENCORE EXISTANTES. STEP51 U1 120 CHIFFRES TRÈS STABLE NUMÉRIQUEMENT AVEC SOURCES 45/46 ORIGINALES ; GATE2B OPEN, JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP50 TERMINÉ — 2026-10-22

**BRANCHE SCIENTIFIQUE ACTIVE UNIQUE POUR TOUTES LES ÉCRITURES :** `research/gate2b-nonhomothetic-transfer`.

**ATTENTION : LE DÉPÔT GITHUB A ENCORE TROIS NOMS DE BRANCHES !** Le travail de préservation est effectif, mais leur suppression et le changement de défaut doivent se faire dans l'interface GitHub (le connecteur ne possède pas les actions d'administration). NE PAS AFFIRMER QU'IL NE RESTE QU'UNE BRANCHE AVANT LE CONTRÔLE DISTANT.

**LIRE EN PREMIER :** `research/STEP50_BRANCH_CONSOLIDATION_AND_SOLVER_CROSSCHECK_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step50-report.json`.
**CONSOLIDATION GIT DÉTAILLÉE :** `research/BRANCH_CONSOLIDATION_2026-10-22.md`.
**NOUVEAU PROGRAMME :** `numerics/hr_step50_solver_crosscheck.py`, Git blob `608222f9071c217d477951c8ed1ae81f5507b095`.
**NOUVEAUX TESTS :** `tests/test_hr_step50_solver_crosscheck.py`, Git blob `c96c44c24a5b2a9293d127a77e99dadd6c629125`.
**ANCIEN CONTRÔLE CENTRE :** `research/STEP49_ANALYTIC_CENTER_AND_OUTWARD_SHOOTING_AUDIT.md`.

## CONSOLIDATION SANS PERTE D'HISTORIQUE EFFECTIVEMENT FAITE

- Ancien `main` SHA `aead63f4098f0d15a849e579105af034b6317b30` était déjà ancêtre de la branche active.
- Ancien `research/v2-flrw` SHA `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb` avait 203 commits divergents.
- Commit de préservation `4f7a3a112e392c9c8e6e9256b11ef3c4cbacc3c7` à DEUX PARENTS, ajouté sur la branche active, avec Git TREE EXACTEMENT IDENTIQUE `e5da02813be6b378398520d9d129209fc5caf5c2` : aucun fichier ancien V2 importé/écrasé.
- Contrôle GitHub après opération : `behind=0` pour `main` ET `research/v2-flrw` par rapport à la branche active. Leurs commits sont préservés dans l'ascendance ; PR historique brouillon [#1](https://github.com/alexandrebarault-arch/Janus/pull/1) **FERMÉE le 22 octobre sans fusion** via le connecteur ; ancien code V2 NON fusionné.
- **PENDING INTERVENTION UI GITHUB** : (1) changer branche par défaut `main` → `research/gate2b-nonhomothetic-transfer`, (2) PR brouillon #1 déjà FERMÉE sans fusion, (3) supprimer refs `research/v2-flrw` et `main`, (4) vérifier que GitHub affiche réellement **une seule branche**. Changer le défaut AVANT de supprimer `main`. NE PAS réactiver Actions/workflows.

## AVANCÉE SCIENTIFIQUE STEP50 — TROIS SOLVEURS INDÉPENDANTS, PAS TROIS THÉORIES

Les programmes RK45, DOP853 et Radau intègrent depuis `eps=.00625` vers `r=.85` la même équation d'EDO analytique `pLf'=-C0/C1` déduite des primaires f aux étapes 45/46, avec l'initialisation régulière de Step49 `pLf(eps)=U0 eps² + U1_est eps⁴`. `U1_est≈0.0007897451669079507` est NUMÉRIQUE NON CERTIFIÉ. Pour `rtol=2e-11`, `atol=1e-17`, pas max `.012` et **2049 rayons** sur `[.01,.85]` :

```text
méthode    RHS       pLf(.85)                 min_pf/r² (2049 échantillons)
RK45       824       -0.003386429356487892   0.11186483299522024
DOP853     1376      -0.0033864293564879015  0.11186483299522028
Radau      2647      -0.0033864293564881253  0.11186483299522033
```

Max écart pLf sur la TRAJECTOIRE ÉCHANTILLONNÉE par rapport RK45 : DOP853 `4.020178287489351e-14`, Radau `4.0734668242670136e-14`. Les deux poussières positives SUR CES POINTS ; g normalisée min `0.8856008128827202`. `C` par substitution algébrique max `3.8e-14` est faible **PAR CONSTRUCTION**, pas un contrôle indépendant de l'action originale non intégrée (déjà mené séparément au Step48).

**AUCUNE borne d'erreur CONTINUE/INTERVALLE**, ni positivité continue sur [0,.85], ni préservation temporelle du Dirac n'ont été établies en Step50.

## TESTS ET PROVENANCE HONNÊTES

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step49_regular_center_shoot.py tests/test_hr_step49_analytic_center.py tests/test_hr_step50_solver_crosscheck.py
# EFFECTIVEMENT EXÉCUTÉ : 29 PASSED en 6.09 s ; 21 anciens Step49 et 8 nouveaux Step50.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step50_solver_crosscheck
```

Les DEUX nouveaux fichiers source/test sont Git blob BYTE-IDENTICAL aux fichiers réellement testés ; les sources antérieures Step45/46/47 dans l'environnement local `/mnt/data/janus-step50` sont encore des adaptateurs mathématiques NON OCTET-IDENTIQUES à GitHub. Les deux tests originaux Step48 nécessitant 5 providers authentiques n'ont donc PAS été vérifiés ; pas de suite entière ni de CI. Le JSON local complet a SHA256 `a0c76ddc29560df063ba3b83e63e57a3ef4d9becc912d4f37775cc08ed039a45` et les valeurs essentielles sont enregistrées dans `research/reports/gate2b-step50-report.json`.

## PRIORITÉS STEP51 POUR REPRISE APRÈS INTERRUPTION

1. **OPÉRATION GITHUB ADMINISTRATIVE restante** — changer le défaut et supprimer les 2 refs via UI, sans perte d'historique grâce au commit `4f7a3a1`. Ne jamais déclarer suppression réalisée sans preuve depuis GitHub.
2. **REGRESSION HISTORIQUE AUTHENTIQUE** — reconstituer les véritables fichiers Step45/46/47 byte-identiques et lancer les deux tests Step48 désélectionnés puis les tests Step49/50 sans adapters.
3. **CERTIFICAT MATHÉMATIQUE GLOBAL** — dériver U1 exact ou rationnellement borné, puis prouver continuité/existence/signes des deux poussières pour la SOLUTION NON POLYNOMIALE RÉGULIÈRE jusqu'à .85 avec une EDO validée par intervalles, en conservant J>0,K/r²>0.
4. **DIRAC TEMPOREL** — calculer réellement `{C,Htot}` pour les SIX couples canoniques, rang, fixation des lapses, bords, chartes exceptionnelles. Ward exact et ODE radiale ne prouvent PAS l'absence BD. Vraie cosmologie on-shell et De Felice/Aoki après seulement.

**VERDICT : historique scientifique désormais préservé dans une seule ascendance active, MAIS TROIS REFS GITHUB ENCORE VISIBLES ; contrôle numérique Step50 PASS ; GLOBAL/Dirac Gate 2B OPEN ; JANUS-R NON VALIDÉ.**

---

# JANUS — REPRISE PRIORITAIRE : STEP49 TERMINÉ — 2026-10-22

**BRANCHE AUTORISÉE EXCLUSIVE :** `research/gate2b-nonhomothetic-transfer`. NE modifier NI `main` NI `research/v2-flrw`. NE PAS réactiver GitHub Actions/workflows.

**LIRE D'ABORD :** `research/STEP49_ANALYTIC_CENTER_AND_OUTWARD_SHOOTING_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step49-report.json`.
**CODE CENTRE ANALYTIQUE :** `numerics/hr_step49_analytic_center.py`, Git blob `d570948912885d45a625fa2db31c6a5435b6a654`.
**TESTS CENTRE ANALYTIQUE :** `tests/test_hr_step49_analytic_center.py`, blob `8f14de90a296f53f372dde4a29fc63149473644b`.
**CODE TIR FROBENIUS :** `numerics/hr_step49_regular_center_shoot.py`, blob `ef1316505f03ee030b29b91e0edfaa5e480132cc`.
**TESTS TIR :** `tests/test_hr_step49_regular_center_shoot.py`, blob `2db400a4b41541983dd49a5fab2d4d0777789aa4`.
**PRÉCÉDENT STEP48 :** `research/STEP48_ORIGINAL_POISSON_AND_CENTER_FROBENIUS_AUDIT.md`.

## NOUVEAU THÉORÈME CENTRE LOCAL, CONDITIONNEL AUX DONNÉES ANALYTIQUES

À partir du VRAI (C=K00-(K01)') du Hamiltonien sphérique ADM-HR positif et DEUX poussières canoniques (Step45), après élimination des deux primaires f (Step46), posons `s=r²`, `pLf(r)=r² U(s)`, `W=pLf'/r`. Une substitution PARITAIRE générale dans l'expression physique donne EXACTEMENT `C/r²` PAIR et analytique en r au centre dans la charte régulière avec autres fonctions canoniques analytiques paires en s, racines et dénominateurs non nuls.

La dérivée implicite CENTRALE exacte est `d(C/r²)/dW = -m² Mg² (a² beta1+2ab beta2+b² beta3)/(2 Mf² b)`, non nulle si `Astar>0`. Ainsi `W=G(s,U)` analytique locale, avec `G(0,U)=3U0-U`, où

```text
U0=Mf²*b*(Pg/(Mg²*a)-2*z1) ;
2*s*U_s=G(s,U)-2U ;
s*U_s=-(3/2)*(U-U0) + (s/2)*R(s,U) ; R analytique.
```

Une équation intégrale de Volterra contractive pour petit s assure l'UNIQUE solution ANALYTIQUE LOCALE régulière dans cette famille de DONNÉES INITIALES prescrites analytiques ; le mode `U-U0=C*s^(-3/2)`, donc `pLf=C/r`, est écarté. Ce résultat n'est PAS une preuve de l'existence globale sur `r∈[0,.85]` ni de la préservation temporelle par les lapses.

Une vérification RATIONNELLE EXACTE indépendante des formules de poussières au centre avec racine `H=sqrt(H²)` encadrée par `isqrt` donne `pg/r²|0=1107/1250=0.8856` et `pf/r²|0>0.1242` (approx `0.1242700002620524`), `J(y)>0.65`. Les sources restent strictement positives dans un CERTAIN voisinage du centre, par analyticity/continuité. Taille de ce voisinage NON bornée ici.

## INTÉGRATIONS VERS L'EXTÉRIEUR ET DONNÉES EFFECTIVEMENT TESTÉES

`U(s)=U0+U1*s+...`, `U1=(∂_s G)(0,U0)/5` exactement en formalisme; `U1≈0.0007897451669079507` ESTIMÉ numériquement par Richardson, PAS dérivé avec borne d'erreur rationnelle. Tir numérique `solve_ivp` à partir de rayon `eps>0`, données `pLf(eps)=U0 eps²` ou `U0 eps²+U1 eps⁴`, jusqu'à `.85`; référence `eps=.001`, `pLf(.85)=-.003386429356487895`, proche de Step47.

```text
eps      |endpoint order0 - reference|     |endpoint order1 - reference|
.05       2.9086971547e-10                 9.2725306600e-15
.025      9.0899401721e-12                 7.0689981646e-17
.0125     2.8406357128e-13                 1.7347234760e-18
.00625    8.8783147500e-15                 4.3368086899e-18
```

L'erreur de coupure d'ordre0 chute ≈32 par division du rayon par deux : signature numérique attendue `O(eps^5)`; ordre1 cohérent au départ avec amélioration `O(eps^7)`, puis plancher flottant. **CE NE SONT PAS DES BORNES CERTIFIÉES SUR L'EDO CONTINUE.**

129 rayons [.05,.85] : `min(pg/r²)≈.8856203219`, `min(pf/r²)≈.1118648330`, `max|C_algebraically_substituted|≈1.74e-14`. Ce sont des ÉCHANTILLONS POSITIFS, PAS un certificat continu le long du nouvel IVP.

## TESTS ET PROVENANCE RÉELS

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step49_regular_center_shoot.py tests/test_hr_step49_analytic_center.py
# EFFECTIVEMENT EXÉCUTÉ : 21 PASSED en 4.41 s, depuis /mnt/data/janus-step49.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step49_regular_center_shoot
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step49_analytic_center
```

Les QUATRE nouvelles sources/tests sont OCTET POUR OCTET IDENTIQUES aux blobs GitHub vérifiés. MAIS les dépendances HISTORIQUES Step45/46/47 du runtime local ont été reconstruites fidèlement par des adaptations mathématiques et NE SONT PAS les fichiers historiques GitHub strictement byte-identiques. Donc une régression authentique de toutes les dépendances est ENCORE BLOQUÉE ; les DEUX tests Step48 désélectionnés n'ont PAS été réexécutés. Ni suite entière du dépôt ni CI. Ne PAS dissimuler cette provenance.

JSON détaillés locaux générés : `/mnt/data/janus-step49/step49-local.json` SHA256 `45f59ca454ad1c9733d17049c72c175d94f54c663058ea47f79743ca8d9bc13a` ; `/mnt/data/janus-step49/step49-center-theorem.json` SHA256 `c197212b6c38e49a6f9d45694d3798dae5672f4c10d0acf0814981d6615c4be7`. Leurs résultats essentiels sont sauvegardés dans rapport GitHub; ces deux fichiers locaux JSON détaillés n'ont PAS été ajoutés au repo.

## PROCHAIN STEP50 — VERROUS OUVERTS

1. Recréer EN UN SEUL CHECKOUT les véritables Step45/46/47 bytes GitHub, lancer Step48 complet SANS DEUX tests désélectionnés + 21 tests Step49. Empreintes sources obligatoires.
2. Établir par ODE à intervalles, Chebyshev/résidus vérifiés ou bornes rigoureuses la CONTINUATION GLOBALE de la branche analytique régulière `U(s)` jusque `.85`, les erreurs numériques, la positivité CONTINUE des deux poussières et toutes marges de chartes J/K/coefficients de poussière. Prochaine extension utile: dériver `U1` SYMBOLIQUEMENT, pas Richardson.
3. Seulement sur données exactement contraintes, calculer la PRÉSERVATION TEMPORELLE `{C,Htotal}` pour les SIX couples canoniques, fixation des lapses et rang Dirac, bords et J/K exceptionnels. Ne pas déclarer absence BD avant cela.
4. Puis véritables cosmologies non homothétiques ON-SHELL, De Felice/Aoki même action, pli Candidate-C et observations. Critique du manuscrit JHR f-EH signe inversé = autre piste.

**STATUT : CENTRE ANALYTIQUE LOCAL CONDITIONNEL DÉMONTRÉ ; POUISSIÈRES POSITIVES STRICTES AU CENTRE CERTIFIÉES ; TIR NUMÉRIQUE VERS .85 TRÈS CONVERGENT ; CONTINUATION GLOBALE ET DIRAC TEMPOREL OUVERTS ; GATE_2B OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP48 TERMINÉ — 2026-10-22

**SEULE BRANCHE AUTORISÉE :** `research/gate2b-nonhomothetic-transfer`. Ne pas modifier `main`, `research/v2-flrw` ; GitHub Actions/workflows désactivés par l'utilisateur.

**LIRE D'ABORD :** `research/STEP48_ORIGINAL_POISSON_AND_CENTER_FROBENIUS_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step48-report.json`.
**CALCULATEUR POISSON ORIGINAL SUR IVP :** `numerics/hr_step48_original_ivp_oracle.py` blob `dc5101d4b0d1d5b8d0834aacff4a3ad3715a28db`.
**CONDITION DU CENTRE :** `numerics/hr_step48_center_compatibility.py` blob `aa181529d33fcfa7d1e61a4525cade3e1b0ca4c7`.
**TESTS :** `tests/test_hr_step48_center_and_original_ivp.py` blob `e1f2946eabb4e47335940c7ce010cfd7dbe2b505`.
**ORACLE HISTORIQUE :** `numerics/hr_step37_original_nonibp_oracle.py` blob ORIGINAL EXACT GITHUB `005449ade6e3582e3b9a5c3374a881a77e73e3f6`.
**ÉQUATION ORIGINE :** `numerics/hr_step45_exact_physical_ward.py`, `numerics/hr_step46_exact_secondary_ode.py`, `numerics/hr_step47_interior_ivp.py`.

## AVANCÉE SCIENTIFIQUE RÉELLE : CONTRÔLE POISSON INDÉPENDANT

Sur l'IVP NUMÉRIQUE de Step47 (r=.05→.85, données courbes non comobiles, DEUX poussières positives aux points contrôlés), reconstruction des 12 champs canoniques sur grille, y compris les horloges poussière `theta_i(r)=k_i*a_i*(r²/2+c_i*r⁴/2+c_i²*r⁶/6)`. Le vrai calculateur historique ORIGINAL NON-IBP `hamiltonians(q,r)` a été reconstruit OCTET POUR OCTET depuis GitHub (SHA ci-dessus), et ses sorties réelles et complexes ont été comparées à une autre implémentation indépendante des mêmes densités — matrices NumPy IDENTIQUES.

Dérivées fonctionnelles du Poisson de TOUTES les 12 variables par complex-step nodal, six couples contractés. Deux choix de lapses compacts indépendants A et B, 4 grilles :

```text
n      crochet A             crochet B
161    -5.909466422135e-7    -9.466192093556e-7
321    -1.477085211689e-7    -2.366493849189e-7
641    -3.692537306677e-8    -5.916200890277e-8
1281   -9.231239094041e-9    -1.479048690706e-8
```

Richardson R4 sur les trois grilles les plus fines, en ASSUMANT développement en puissances paires de h (NON démontré) : **A -8.0411576792e-15**, **B -8.19811039928889e-15**. **C'EST UN CONTRÔLE NUMÉRIQUE INDÉPENDANT FAVORABLE** à la contrainte imposée via l'ODE analytique, pas une preuve du crochet continu exactement nul. Les crochets originaux de grilles finies restent NON NULS négatifs; primaires discrètes max ~1.24e-9 à n1281. Source dans rapport machine et module régénérable.

Full JSON local effectivement généré `/mnt/data/janus-step48/research/reports/step48-local-nonibp-full.json`, SHA256 `dfc18acda78163dff61021f51429a06d6d2db4854d19655fb5dd939ab472b9a1` ; **PAS ENCORE UPLOADÉ** comme fichier GitHub séparé ; les données essentielles et les codes de reproduction sont PUBLIÉS.

## NOUVEAU VERROU CENTRE — CONDITION EXACTE ET MODE SINGULIER

En développant le **C PHYSIQUE EXACT de Step45** sur donnée sphérique régulière `Lg=a+O(r²), Lf=b+O(r²), pLg=Pg*r²+O(r⁴), pLf=Uf*r²+O(r⁴), pSg=2Pg*r+O(r³), pSf=Vf*r+O(r³), z=z1*r+O(r³)`, on obtient la relation exacte, avec `A*=a² beta1+2ab beta2+b² beta3` :

```text
lim C(r)/r² = -(m² A*)/(2 Mf² a b) *
      [6 Mf² Mg² z1 a b - 3 Mf² Pg b + Mg² a (Uf+Vf)].
```

La primaire radiale f impose `Vf=2Uf` au centre régulier. Par conséquent, pour `A*>0`, condition NÉCESSAIRE exacte :
```text
Uf(0) = Mf²*b*( Pg/(Mg²*a) - 2*z1 )
```
= environ `-0.005252426896760733` pour le benchmark. L'ancien coefficient numérique figé donne `-0.005252426896763941`, écart ~`-3.20837e-15`. **Proximité ne signifie PAS égalité exacte.**

L'équation linéarisée au centre donne `pLf'+pLf/r=3*Uf(0)*r+O(r³)`, d'où solution formelle `pLf=Uf(0)r²+Csing/r`. Une solution régulière doit éliminer `Csing/r` : l'IVP arrière n'est donc pas une preuve de régularité au centre. Essai de sensibilité : modifier `pLf(.05)` de `+1e-12` entraîne amplification mesurée ≈1.2499973 (r=.04), 2.4999873 (.02), 4.9999710 (.01), 9.9999401 (.005), 24.9998492 (.002), vs loi prédite `.05/r`. Ce mode est un développement FORMEL/LINÉARISÉ, non un théorème de singularité de la solution non linéaire.

## PROVENANCE ET TESTS — NE PAS SURVENDRE

NOUVEAUX trois fichiers exécutés localement ET byte-identiques à GitHub (blob SHA ci-dessus). Fichier oracle historique original également byte-identique. Les AUTRES dépendances historiques Step45–47, dans ce runtime local, sont des reproductions mathématiques/compatibilité et PAS les fichiers originaux bit-identiques. Ainsi, sur 12 tests du nouveau module :

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step48_center_and_original_ivp.py \
   -k 'not test_original_provider_source_pins_match_real_checkout and not test_interrupted_run_manifest_keeps_Dirac_red'
# ACTUELLEMENT 10 PASSED, 2 DESELECTED en 5.27 s.
```

Les 2 NON EXÉCUTÉS exigent les CINQ dépendances historiques authentiques dans UN checkout commun. Le module `numerics/hr_step48_original_ivp_oracle.py` vérifie les cinq Git blob SHAs **FAIL-CLOSED** en mode par défaut ; cette vérification a été contournée uniquement pour l'expérience locale, signalée `check_git=False` dans le JSON local, et NE DOIT PAS ÊTRE APPELÉE vérification complète GitHub. PAS de tests de tout dépôt ni de CI Actions.

## SUITE PRIORITAIRE STEP49

1. Obtenir dans UN environnement les CINQ vraies sources historiques SHA exactes, relancer `pytest -q tests/test_hr_step48_center_and_original_ivp.py` **sans filtre**, puis `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m numerics.hr_step48_original_ivp_oracle`. Enregistrer les résultats et tout échec. Ne pas débloquer CI.
2. Résoudre le problème **À DEUX BORDS** : paramétrer `pLf=r² U(r²)`, imposer `U(0)=Uf0` déduit exactement ci-dessus, annuler le mode (1/r), construire une solution régulière par séries/Frobenius ou tir analytique/numérique certifié. Vérifier poussières positives CONTINÛMENT le long de la vraie solution IVP, J>0,K/r²>0.
3. Calculer ensuite sur données exactement primaires+secondaires le VRAI Dirac temps `{C,Htotal}` avec six couples canoniques, rang, lapse fixing, secteurs exceptionnels J/K, bords; le contrôle Poisson spatial N,M ne remplace pas cela.
4. Puis seulement évolution non homothétique on-shell, De Felice/Aoki même action, pli Candidate-C et observations. Ne pas fusionner avec manuscrit JHR externe de signe f-EH inversé.

**VERDICT : STEP48 DEUX ORACLES POISSON CONCORDENT NUMÉRIQUEMENT SUR IVP; COMPATIBILITÉ AU CENTRE NÉCESSAIRE ANALYTIQUE DÉMONTRÉE ; CENTRE RÉGULIER GLOBAL NON DÉMONTRÉ ; PRÉSERVATION DIRAC / LAPSUS NON DÉRIVÉS ; GATE_2B=OPEN ; JANUS-R NON VALIDÉ.**

---

# JANUS — REPRISE PRIORITAIRE : STEP47 TERMINÉ — 2026-10-22

**BRANCHE AUTORISÉE UNIQUEMENT :** `research/gate2b-nonhomothetic-transfer` ; `main` et `research/v2-flrw` inchangées, Actions/workflows désactivés.

**LIRE EN PREMIER :** `research/STEP47_INTERIOR_SECONDARY_ODE_INTEGRATION_AUDIT.md`.
**RAPPORT :** `research/reports/gate2b-step47-report.json`.
**SOLVEUR INTÉRIEUR :** `numerics/hr_step47_interior_ivp.py` Git blob `c558a827939f2e1fffbfc0290f2b3cc88cb69ef9`.
**TESTS :** `tests/test_hr_step47_interior_ivp.py` Git blob `1e64b528bf87142f2d1059ac736b2d4ee7a79de5`.
**ÉQUATION EXACTE :** `numerics/hr_step46_exact_secondary_ode.py` + `numerics/hr_step45_exact_physical_ward.py`.

## RÉSULTAT SCIENTIFIQUE — PREMIÈRE INTÉGRATION NUMÉRIQUE DE L'EDO SECONDAIRE EXACTE

Les étapes45–46 ont démontré les identités physiques de Ward dans la réduction sphérique et dérivé EXACTEMENT `C=K00-(K01)'` sans différences finies, puis `pLf'=-C0/C1` par élimination des deux contraintes primaires f. Étape47 : INTÉGRATION numérique de cette EDO sur `r∈[.05,.85]` avec données g/métriques/poussières prescrites, poussières f recalculées de leurs primaires à chaque point, métriques courbes, phases de poussières non comobiles et déplacement relatif non nul.

- RK adaptatif `scipy.solve_ivp` : `rtol=1e-10,atol=1e-14,max_step=.02`, 338 RHS, `pLf(.05)=-1.3126131492021531e-05`, `pLf(.85)=-.0033864293564877215`.
- 33 points hors collocation : `min(pg/r²)=.8856203218885325`, `min(pf/r²)=.11186483299522221`, toutes DEUX poussières POSITIVES AUX POINTS TESTÉS.
- Contre-calcul primaire à partir des densités ADM sphériques ORIGINALES reconstruites : max `|Hg|≈1.11e-15`, `|Hf|≈1.39e-17`, `|Ddiag|≈1.37e-16`, `|Fz|≈1.37e-16`; résidu `|C|` de substitution analytique max `1.58e-14` (petit **PAR CONSTRUCTION**, donc pas un contrôle Poisson original indépendant).
- Trois tolérances donnent extrémités `-.0033864293564835235`, `-.0033864293564877215`, `-.0033864293564879007`; différences successives `4.20e-15`, `1.79e-16`. C'est une CONVERGENCE NUMÉRIQUE, PAS une erreur globale certifiée.
- À AUCUN MOMENT le r=0 centre n'est franchi, ni la positivité de la poussière continue du nouvel IVP démontrée. Les bornes Step40–42 du profil POLYNOMIAL figé ne sont PAS transférables sans preuve au nouveau profil non polynomial.

## EXACTE REPRODUCTION — TESTS EFFECTIVEMENT EXÉCUTÉS

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step45_exact_physical_ward.py tests/test_hr_step45_secondary_point_certificate.py tests/test_hr_step46_exact_secondary_ode.py tests/test_hr_step47_interior_ivp.py
# ACTUELLEMENT EXÉCUTÉ : 39 PASSED ~3.94 s, 12+12+8+7. Tous nouveaux fichiers exécutés byte-identical SHA GitHub.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step47_interior_ivp

# Si les 33 points complets sont nécessaires :
PYTHONPATH=. python -c "import json;from numerics.hr_step47_interior_ivp import integrate_interior;print(json.dumps(integrate_interior(),indent=2))"
```

Le JSON 33 points détaillé a été généré dans `/mnt/data/janus-step45/research/reports/gate2b-step47-interior-run.json` mais PAS uploadé en tant que tel sur Github. Le rapport condensé et code de régénération sont PUBLIÉS. CI/workflows désactivés. Suite complète GitHub d'avant Step45 NON réexécutée cette session.

## PROCHAIN STEP48 — VERROU RÉEL

1. Refaire le CROCHET POISSON INDEPENDANT **NON INTÉGRÉ PAR PARTIES** du modèle original sur le NOUVEL IVP nonpolynomial par interpolation/sampling, vérifier convergence 161/321/641/1281 à DEUX fonctions de lapses, sans substituer son algèbre C par construction.
2. **CERTIFIER** en continu par intervalles l'IVP radial (error enclosure et poussières positives) et analyser le point singulier/centre `r=0`. Chercher existence/unicité régulière ou obstruction. Contrôler J/K et conditions de bord.
3. Après une vraie donnée exactement contrainte vérifiée, dériver/calculer `{C,Htotal}` pour tous SIX couples canoniques, lapseratio et rang Dirac incluant branches exceptionnelles. Ne pas conclure BD à partir de Ward/ODE seuls.
4. Puis seulement vraie évolution cosmologique on-shell, critères De Felice/Aoki de même action, Candidate-C, observations.

**ÉTAT : Step45 WARD EXACT, Step46 ODE SECONDAIRE EXACTE, Step47 IVP INTÉRIEUR NUMÉRIQUE TRÈS BON (PAS CERTIFIÉ GLOBAL), GATE_2B=OPEN, JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP46 TERMINÉ — 2026-10-22

**BRANCHE ACTIVE UNIQUEMENT :** `research/gate2b-nonhomothetic-transfer`. Ne PAS toucher `main`, `research/v2-flrw` ; ne PAS réactiver Github Actions/workflows.

**LIRE EN PREMIER :** `research/STEP46_EXACT_AFFINE_SECONDARY_ODE_AUDIT.md`.
**RAPPORT :** `research/reports/gate2b-step46-report.json`.
**CODE :** `numerics/hr_step46_exact_secondary_ode.py`, Git blob `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
**TESTS :** `tests/test_hr_step46_exact_secondary_ode.py`, Git blob `f09e5205d5915d546cf83875ffcafe44232411e2`.
**SOURCE MATHÉMATIQUE REQUISE :** `numerics/hr_step45_exact_physical_ward.py` Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, avec audit `research/STEP45_EXACT_PHYSICAL_WARD_AND_ANALYTIC_SECONDARY_AUDIT.md`.

## RÉSULTAT DURABLE STEP46 : ODE EXACTE DE LA SECONDAIRE LOCALE

Sur les DEUX contraintes primaires f (Hamiltonienne et impulsion radiale) de l'action ADM sphérique Hassan–Rosen + deux poussières canoniques, choisir `P(r)=pLf(r)` et `V=P'(r)` ; éliminer les deux inconnues de poussière `pf,pSf`. Substituer dans la formule de `C=K00-(K01)'` dérivée exactement au Step45. Alors, **IDENTITÉ SYMBOLIQUE** :

```text
C(r;P,V) = C0(r;P) + C1(r;P)*V
C1 = -(m2*Mg2*At*sqrt(1-z²)/(2*Mf2*Sf)) * (Lf*beta_f)/(Sf_prime*dust_coef_f)
At = beta1*Sg² + 2 beta2*Sg Sf + beta3 Sf² = Sg² J(Sf/Sg)
beta_f = sqrt(1+(theta_f_prime/Lf)²)
dust_coef_f = beta_f + [P/(2 Mf2 Sf Sf_prime)]*theta_f_prime
pLf_prime = -C0/C1  => C=0 IDENTIQUEMENT.
```

Le coefficient C1 est STRICTEMENT NÉGATIF sur un intervalle intérieur `r>0` où les marges `At,Lf,Sf,Sf',beta_f,dust_coef_f>0` et `|z|<1` établies en étapes 40–42 persistent. Cela permet une formulation en problème de Cauchy LOCAL pour le moment radial f, sous prescription régulière des autres données. **AUCUNE SOLUTION GLOBALE SUR [0,.85] n'a encore été construite**. Une solution de l'EDO avec centre régulier et DEUX poussières positives est un VERROU OUVERT. La conservation temporelle et la fixation des lapses restent ENTIÈREMENT OUVERTES.

**Important :** cet outil n'est PAS un solveur de l'évolution cosmologique à deux métriques. Il ne donne pas encore une contrainte BD complète ni un comptage des degrés de liberté. Ne pas appeler cela « solution exacte JANUS-R ».

## TESTS RÉELLEMENT PASSÉS ET REPRISE

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step45_exact_physical_ward.py tests/test_hr_step45_secondary_point_certificate.py tests/test_hr_step46_exact_secondary_ode.py
# EFFECTIVEMENT EXÉCUTÉ : 32 PASSED en 2.04 s dans /mnt/data/janus-step45,
# comprenant 24 contrôles Step45 + 8 nouvelles identités Step46, SANS adaptations.
PYTHONPATH=. python -m numerics.hr_step46_exact_secondary_ode
```

Les SIX nouveaux fichiers source/test Step45–46 sont IDENTIQUES octet pour octet à leur version Github et exécutés en local. Tests ciblés sur équations hamiltoniennes symboliques / fractions exactes, **pas** suite entière, **pas** original Step33g→44 réexécuté intégralement cette session, **pas** CI.

## RAPPEL STEP45 CONFIRMÉ

- EXACT WARD: `K02=K12=K21=K22=0`, `K11=K20=2Mg2 Sg Sg' z/(Lg Lf)`, `W=K01-K10+(K20)'=z Hg/Lf`, donc `W=0` exactement sur `Hg=0`; shift `dHg/dz=Fz/Lg`, `dHf/dz=Fz/Lf` sur source originale. Hypothèses compact support, réduction sphérique et domaine régulier.
- `C(q,q',z,z')` calculé sans différence finie, sans aucune dérivée seconde des 12 champs ou de z.
- Pour le PROFIL POLYNOMIAL STEP41 FIGÉ et constantes décimales traitées comme fractions exactes, un encadrement rationnel exact prouve `6.5545288523431e-11 < C(r=.85) < 6.5545288523432e-11`. Ce PROFIL PARTICULIER n'est pas une solution exacte C=0 dans le modèle rationalisé ; cela ne réfute PAS l'existence d'autres solutions exactes. ATTENTION : source historique Step33g a des opérations flottantes ; ne pas confondre l'étalonnage rationnel avec toutes les instructions binary64.

## PROCHAIN VERROU STEP47

1. **INTÉGRER** l'EDO exacte `pLf'=-C0/C1` à partir d'un rayon intérieur r0>0, avec données de Step41 comme amorce, par une méthode contrôlée ; tester indépendamment `Hg,Hf,D_g+D_f,Fz,C` contre les Hamiltoniens originaux NON-IBP à des rayons hors ajustement.
2. Explorer prolongement sur `r∈(.0,.85]`, sphéricité régulière `pLf=r²*P_f(r²)`, conditions au centre, décroissance des marges de poussière `pg,pf>0`, non-dégénérescence `J, K/r²>0`, éventuelle obstruction ou preuve de continuation.
3. Une fois des données exactes ou certifiées : **PRÉSERVATION TEMPORELLE** `{C,Htotal}` avec tous SIX couples canoniques, fixation des lapses, matrice Dirac et branches exceptionnelles; ne jamais inférer ghost-free de Ward seul.
4. Après cela seulement : vraie évolution non homothétique on-shell, contrôles physiques De Felice/Aoki de même action, pli et observations. Manuscrit externe JHR avec mauvais signe f-EH = piste critique séparée.

**VERDICT : STEP45 IDENTITÉS WARD EXACTES ; STEP46 REFORMULATION EXACTE C=0 EN EDO LOCALE ; SOLUTION GLOBALE À DEUX POUSSIÈRES, DIRAC TEMPOREL ET LAPSES = OUVERTS ; GATE_2B=OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP45 TERMINÉ — 2026-10-22

**BRANCHE ACTIVE UNIQUE :** `research/gate2b-nonhomothetic-transfer` ; ne pas modifier `main`, `research/v2-flrw`, ni réactiver GitHub Actions/workflows.

**LIRE EN PREMIER :** `research/STEP45_EXACT_PHYSICAL_WARD_AND_ANALYTIC_SECONDARY_AUDIT.md`.
**RAPPORT MACHINE :** `research/reports/gate2b-step45-report.json`.
**CODE SYMBOLE :** `numerics/hr_step45_exact_physical_ward.py` (Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`).
**CERTIFICAT RATIONNEL :** `numerics/hr_step45_secondary_point_certificate.py` (Git blob `6ab94dacb0c6429bdce8d71311161a6b76ecc0e6`).
**TESTS :** `tests/test_hr_step45_exact_physical_ward.py` (Git blob `64c32464df011e87c11e7ca7ff0d9d101bb167aa`) et `tests/test_hr_step45_secondary_point_certificate.py` (Git blob `d2c04e5961cfb31867ea40b8d003c8e35ced9eb8`).
**HISTORIQUE :** Le commit initial Step45 `e960f774` ajoutait `research/STEP45_CHECKPOINT.txt` (identités annoncées SANS code); la présente session a indépendamment calculé les identités sur les Hamiltoniens originaux et publié les sources exactes et les contrôles rationnels.

## RÉSULTAT SCIENTIFIQUE IMPORTANT — IDENTITÉS WARD EXACTES, PAS SEULEMENT NUMÉRIQUES

Sur la DENSITÉ SPHÉRIQUE ADM+Hassan–Rosen à deux secteurs Einstein-Hilbert positifs et deux poussières canoniques en mouvement, le noyau Poisson mixte à SIX couples canoniques et à NEUF jets de lapses vérifie SYMBOLIQUEMENT :
```text
K02 = K12 = K21 = K22 = 0                   [IDENTIQUES HORS CONTRAINTES]
K11 = K20 = 2*Mg2*Sg*Sg'*z/(Lg*Lf)          [IDENTIQUES HORS CONTRAINTES]
W = K01-K10+(K20)' = z*Hg/Lf               [IDENTITÉ HORS CONTRAINTES]
d(Hg)/dz = Fz/Lg, d(Hf)/dz = Fz/Lf          [STATIONNARITÉ ALGÉBRIQUE Fz=0]
```
Sur `Hg=0`, **W=0 EXACTEMENT**, avec hypothèses de compacité des fonctions de lapses et dénominateurs réguliers. La réduction formelle du crochet complet à `int N M C`, `C=K00-(K01)'`, est donc désormais **JUSTIFIÉE EXACTEMENT DANS CETTE RÉDUCTION SPHÉRIQUE**, plutôt que conjecturée via ≈1e-15. Ne jamais étendre sans preuve à tout secteur tensoriel 4D ou au Dirac temporel.

## NOUVEAU CALCUL ANALYTIQUE DE C SANS DIFFÉRENCES FINIES

Le nouveau module dérive TOUTES les gradients d'Euler `N,N',N''` et `M,M',M''` directement en SymPy, puis simplifie `C=K00-d(K01)/dr` EXACTEMENT. Toutes les dérivées secondes des 12 champs et `z''` s'annulent, laissant `C(q,q',z,z')` algébrique. Ce C est NON NUL HORS CONTRAINTES. Cela supprime le biais numérique Step37/39 dans la définition locale, mais **ne résout pas C=0**.

## CONTRE-CONTRÔLE RIGOUREUX DU PROFIL NUMÉRIQUE FIGÉ STEP41

Pour les 9 vrais coefficients de correction Step41 traités comme fractions binaires exactes `Fraction.from_float`, avec les constantes de calibration imprimées considérées comme **rationnels décimaux exacts**, la reconstruction des DEUX poussières et la valeur analytique de C sont calculées par arithmétique d'intervalles rationnels (racines encadrées par `isqrt` à 10^-70, aucune dérivée finie). À `r=17/20=0.85` :

```text
6.5545288523431e-11 < C_frozen(0.85) < 6.5545288523432e-11
```

Borne STRICTE: le profil collocation Step41 FIGÉ n'est donc pas exactement sur `C=0` dans cette interprétation rationnelle de l'étalonnage. Six rayons rationnels (.11,.21,.43,.71,.83,.85) ont tous une valeur strictement non nulle certifiée. **Cette conclusion ne réfute PAS la possibilité d'un autre profil solution exacte.** Les opérations intermédiaires de l'ancienne source originale Step33g sont parfois en binary64 et `sp.Float`; cette preuve rationnelle sur les entrées décimales ne doit PAS être vendue comme une borne machine-bit-identical de chaque opération du programme historique. L'ancienne valeur double à .85 est cohérente à ~1e-14 près.

## TESTS EFFECTIVEMENT PASSÉS ET REPRODUCTION

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step45_exact_physical_ward.py tests/test_hr_step45_secondary_point_certificate.py
# EXÉCUTÉ : 24 PASSED, 1.30s, /mnt/data/janus-step45
PYTHONPATH=. python -m numerics.hr_step45_exact_physical_ward
PYTHONPATH=. python -m numerics.hr_step45_secondary_point_certificate
```

Les QUATRE nouveaux fichiers source/test ont été exécutés en local, puis leurs blob SHA vérifiés identiques à GitHub. C'est une suite ciblée autonome à partir des densités originelles RECOPIÉES littéralement ; la suite COMPLÈTE du dépôt et les fournisseurs historiques Step33g→44 ne sont pas relancés en totalité cette session. Les anciens tests physiques Step44 (33 passes) demeurent archivés. Aucun CI ni GitHub Actions.

## ÉTAPE46 — PRIORITÉ SCIENTIFIQUE RÉELLE

1. Utiliser la formule **EXACTE** `C(q,q',z,z')` pour construire une véritable solution `C(r)=0` sur un INTERVALLE CONTINU courbe, non comobile, avec deux poussières positives, centre et bord réguliers. Voir si elle définit une EDO/équation algébrique pour le générateur libre `pLf`; démontrer existence/unicité ou obstruction, et ne pas confondre collocation polynomiale avec solution exacte.
2. Tester indépendamment la correspondance avec le véritable Hamiltonien sous élimination de z, et la sémantique exacte rationnelle vs opérations sources binary64.
3. Puis ET SEULEMENT PUIS calculer la préservation temporelle `{C,H_total}` avec tous les SIX couples canoniques, le rang Dirac et la fixation des lapses. Ne PAS conclure fantôme BD supprimé sans cela.
4. Enfin étude réellement on-shell non homothétique, De Felice/Aoki de même action, pli Candidate-C, données observables.

**STATUT : STEP45 WARD EXACT = DÉMONTRÉ SOUS HYPOTHÈSES SPHÉRIQUES ; C EXACT ANALYTIQUE = DISPONIBLE ; PROFIL STEP41 FIGÉ PAS EXACTEMENT CONTRAINT ; EXISTENCE C=0 SUR INTERVALLE + PRÉSERVATION DIRAC + LAPSES = OUVERTS ; GATE_2B=OPEN ; JANUS-R NOT VALIDATED.**

---

# JANUS — AUTHORITATIVE RESTART: STEP44 COMPLETE — 2026-10-21

**ONLY ACTIVE BRANCH:** `research/gate2b-nonhomothetic-transfer`. **DO NOT MODIFY** `main`, `research/v2-flrw`. **DO NOT REENABLE** GitHub workflows/Actions.

**READ FIRST:** `research/STEP44_ACTUAL_PHYSICAL_WARD_AND_ORIGINAL_NONIBP_AUDIT.md`.
**MACHINE SUMMARY:** `research/reports/gate2b-step44-report.json`.
**NEW SOURCE:** `scripts/verify_gate2b_step44.py` Git blob `2d088b7734abfb2487da43bd5330d465f114a1ae`.
**NEW TEST:** `tests/test_hr_step44_original_physical_ward.py` Git blob `bb06f2f56911b9f5f8932184b650a90e21b73bdd`.
**PREVIOUS:** `research/STEP43_EXACT_WARD_ADJOINT_AND_PHYSICAL_GATE_AUDIT.md`.

## DURABLE KEY BREAKTHROUGH: ACTUAL PHYSICAL SOURCE RUN, NOT JUST A MOCK!

This session DIRECTLY EXECUTED `scripts/verify_gate2b_step43.py --physical` and a SECOND, genuinely independent ORIGINAL UNINTEGRATED spherical ADM-HR+two-dust canonical Poisson oracle at 161/321/641/1281 radial grid points for both independent compact lapse smearings A,B. This resolves the previous Step43 **"physical runner unexecuted"** red. The corrected Step39 witness has degree4 even f-momentum, 6 iterations, radial derivative h=.001.

Exactly SEVEN original Step33g/37/39/43 provider modules were reconstructed together as FILES BYTES IDENTICAL TO GITHUB and locally `git hash-object` verified. The NEW Step44 source + test are also Git-blob-identical to the local files actually executed. Full original source blob hashes are pinned in `scripts/verify_gate2b_step44.py`, and verification FAILS CLOSED before physics calculations if any source changes. This was a coherent targeted source worktree at `/mnt/data/janus-step44`, NOT a complete repository checkout; local shell GitHub clone DNS still unavailable.

Run on a fresh branch checkout:

```bash
# Run complete physical 7-provider verification and save regenerable FULL raw output:
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step44.py --full --output research/reports/gate2b-step44-physical-verification.json

# Confirm physical single test and original step43 regression jointly:
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step43_ward_operator.py tests/test_hr_step43_physical_ward_gate.py tests/test_hr_step44_original_physical_ward.py
# ACTUALLY EXECUTED: 33 PASSED, in 13.17 seconds. Step44 alone 10 PASSED twice, in 11.97 and 12.42 s.
```

### ACTUAL PHYSICAL OBSERVATIONS

- Seven physical radii r=.11,.21,.31,.43,.61,.71,.83: `max |W=K01-K10+K20'| = 1.0512424264419451e-15`, `max |D=K20-K11|=4.336808689942018e-19`, `K02=K12=K21=K22=0` **NUMERICALLY** at these points. `max |C=K00-K01'|=5.0185595262819405e-11`. This is NOT an exact pointwise C=0.
- Genuine independent `original_nonibp_extended` computes all six Poisson pairs from original 12-node-variable UNINTEGRATED Hamiltonians and re-solves relative shift. Original brackets:

```text
grid N       161              321             641              1281
Pair A    -5.9094656e-7    -1.4770844e-7   -3.6925290e-8   -9.2311575e-9
Pair B    -9.4661907e-7    -2.3664925e-7   -5.9161875e-8   -1.4790348e-8
```

- ASSUMING even spatial-error powers, highest-grid 2-level Richardson R4 estimates **A +7.30563757648e-14**, **B +1.324021139624889e-13**, vs independently integrated full nine-jet Gaussian 96-point brackets **A +7.911118062876338e-14**, **B +1.3162936854562068e-13**. Discrepancies A -6.054804863963382e-15 and B +7.727454168682165e-16. **This is empirical extrapolation, NOT a rigorous mathematical limit or error bound.** Raw original finite grids are NEGATIVE and have discrete primary errors ~1e-9 even at N1281; small extrapolated values must not be mistaken for exact zeros.
- Physical full-jet minus C-only Gaussian 96-point integral ~-1.09e-16 (pair A), ~-1.47e-16 (pair B). This directly checks Step43 C/W/D reduction on genuine ORIGINAL physical Kij at finite numerical precision.
- Three additional physically primary-satisfying but NON-secondary-fitted families, with max sampled |C|=.4286, .5820, .5215, still have max sampled |W| <=1.4e-15 and |D|~1e-19, high jets zero at tested radii. Strong indication W/D near-cancellation is structural, NOT just due to fitting C. Still no symbolic proof.
- New `research/reports/gate2b-step44-report.json` COMMITTED contains all essential site/pair/grid quantitative values. The generated 14.5k full raw JSON `gate2b-step44-physical-verification.json` was **ACTUALLY generated locally**, SHA256 `7ae03597e0ba95e9775d434274aa75ecb8264ba72a58157849687e09d2b05ab9`, but **not uploaded as a standalone Github file**: regenerate with checked-in `--full` command. Do not claim uploaded!

## ACTUAL TESTS / SCIENTIFIC SCOPE

- 10/10 NEW real-provider regression tests PASSED with all seven provider source blobs EXACT. Combined with 16 Step43 exact SymPy tests and 7 physical-instrument fabricated-negative-control tests, **33/33 PASSED IN ONE pytest PROCESS**. This is not a complete project suite; user-disabled GitHub CI remains inactive.
- **STEP44 PHYSICAL WARD STATUS: NUMERICALLY WELL SUPPORTED**, NOT ANALYTICALLY PROVED. **FULL CURVED SECONDARY C(r)=0 ON CONTINUUM: OPEN**. **TIME PRESERVATION {C,H_total}: NOT COMPUTED**. **LAPSE FIXING AND FULL DIRAC RANK: NOT COMPUTED**. **GATE_2B OPEN; JANUS-R NOT VALIDATED**.
- Step40/41/42 exact rational restricted two-dust positivity and spherical centre parity remain as previous, conditional on the fixed canonical initial-data family; they DO NOT show nonhomothetic on-shell time evolution or the physical absence of Boulware–Deser ghosts.

## NEXT RED: STEP45 — NOT OPTIONAL

1. Derive **SYMBOLIC / EXACT physical** W=0, D=0 and high-smearing cancellations directly from original six-pair HR+two-dust spherical canonical action (or exhibit obstruction); investigate whether equality is on entire phase space or only on the primary/relative-shift surface, and specify boundary terms.
2. Derive `K01'(r)` WITHOUT a finite h floor or implement a rigorous interval/spectral derivative. Establish exactly constrained `C_local(r)=0` for all r over a nontrivial curved, noncomoving two-positive-dust radial family, or honestly falsify.
3. On exact primary+secondary data calculate full `{C_local,H_total}` preservation, six-pair Dirac rank and physical lapse fixing including J/K exceptional charts and regular spherical center.
4. ONLY THEN physical nonhomothetic on-shell evolution and same-action De Felice/Aoki stability and first fold. Keep external opposite-sign-f-EH JHR audit distinct.

**VERDICT: Step44 genuine original-source physical two-oracle/3x3-Ward NUMERICAL AUDIT achieved; exact continuum secondary and full Dirac dynamics still OPEN.**

---

# JANUS — AUTHORITATIVE RESTART — STEP43 COMPLETED — 2026-10-21

**ACTIVE BRANCH ONLY:** `research/gate2b-nonhomothetic-transfer`; preserve `main` and `research/v2-flrw`.
**READ FIRST:** `research/STEP43_EXACT_WARD_ADJOINT_AND_PHYSICAL_GATE_AUDIT.md`.
**JSON REPORT:** `research/reports/gate2b-step43-report.json`.
**NEW EXACT MATH SOURCE:** `numerics/hr_step43_ward_operator.py`.
**NEW NUMERICAL REAL-PROVIDER HOOK:** `numerics/hr_step43_physical_ward_gate.py`.
**NEW RUNNER:** `scripts/verify_gate2b_step43.py`.
**NEW TESTS:** `tests/test_hr_step43_ward_operator.py`, `tests/test_hr_step43_physical_ward_gate.py`.
**PREVIOUS:** `research/STEP42_CENTER_PARITY_AND_SHARP_POSITIVE_DUST_AUDIT.md`.

## CHECKED GITHUB BEFORE WORK

Before Step43, branch HEAD `9da1a11b192150b4b55b0eb233423cdcb3769af0` was verified LIVE through the connected GitHub API. `main` remained `aead63f4098f0d15a849e579105af034b6317b30` and `research/v2-flrw` `dfa497ccb8ee28f7a0b4eceaefef5f922474c4bb`; don't edit them.

## ACTUAL EXECUTED TESTS AND PROVENANCE

In isolated `/mnt/data/janus-step43` (NOT a full Git clone):

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step42_center_regular_interval.py tests/test_hr_step43_ward_operator.py tests/test_hr_step43_physical_ward_gate.py
# 40 passed in 3.53 seconds: historical Step42 17, Step43 formal 16, new physical-instrument MOCK controls 7

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step43.py --selftest
# PASSED, polynomial manufactured reference only, not physical JANUS.
```

NEW scripts and tests actually EXECUTED in the container and byte-for-byte matched to GitHub Git blobs (verified by GitHub fetch and container git hash):
- `numerics/hr_step43_ward_operator.py`: `fd91411ad6cec88d88f0889ccf99a5f070ccbb54`
- `tests/test_hr_step43_ward_operator.py`: `04825a5034421fc1e12dd51ba361d81cfbd5b753`
- `numerics/hr_step43_physical_ward_gate.py`: `386febaa9b805cf423efd6feb7a8027a2069301b`
- `tests/test_hr_step43_physical_ward_gate.py`: `c9eea74b6b14eef81d0816d960b10f9744e0b8b9`
- `scripts/verify_gate2b_step43.py`: `98ae82adaad17e8be9240ceed51ddfe2e141a476`

Original historical Step42 source and tests were byte-authentic GitHub blobs and re-ran successfully; local Step41 report used COMPLETE GitHub schema and exact nine published coefficients + SHA, but was manually reserialized and its blob SHA does NOT equal actual Step41 GitHub report blob. It is a semantically faithful numerical reference, NOT a byte-equal complete checkout. Real Step33g/37/39 providers were NOT executed this session. No GitHub Actions and no full-repo tests. Previous source-authenticated Step39 numerical 32+5 passes remain historical, not reexecuted.

## SCIENTIFIC RESULT — EXACT FORMAL WARD/ADJOINT, NOT HR PHYSICS YET

Full 3x3 smearing-jet functional bracket `B[N,M]=int sum_ij N^(i) Kij M^(j) dr`, i,j=0..2. Exact formal adjoint: `A_p=sum_ij (-1)^i binom(i,p-j) derivative^(i+j-p) Kij` for 0<=p<=4, with valid indices only, requiring appropriate compact support/boundary terms.

In restricted five-coefficient support `{K00,K01,K10,K11,K20}`, define
```text
C=K00-(K01)'            (prior Step37/39 numerical near-secondary)
W=K01-K10+(K20)'        (derivative Ward obstruction)
D=K20-K11               (second-jet obstruction)
```
Then EXACTLY for compact smears `B[N,M]=int N [C*M + (W*M)' + (D*M')'] dr`. Therefore `C=0` alone **does not imply** vanishing bracket. EXACT checks of `W=D=0` and high-jet exclusions `K02=K12=K21=K22=0` (or full adjoint cancellations `A_p-δ_p0 C=0`) are required before interpreting C as the sole secondary coefficient.

16 SymPy tests include EXACT rational polynomial smeared integrals and separate counterexamples where C=0 but W, D, or K22 gives nonzero original bracket; compact boundary controls protect against IBP errors. A manufactured Ward-closed example gives both original and C-only bracket EXACT rational `10753/21358810497024000`. These are **NOT JANUS-specific proofs**.

A separate new instrument computes `C,W,D`, checks the four excluded jets using **all nine** coefficients of the actual `hr_step37_curved_solver.kernel_fast` if available, and compares actual full mixed compact-smear bracket to `int N M C` for two independent Step39 lapse pairs. 7 INJECTED POLYNOMIAL test cases and `--selftest` pass. The real physical mode exists but **WAS NOT RUN**:

```bash
# NEXT FIRST NON-OPTIONAL ACTION ON BYTE-IDENTICAL ORIGINAL GITHUB WORKTREE:
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step43.py --physical --output /tmp/gate2b-step43-physical.json
```

Do NOT call the synthetic `--selftest` a JANUS physical confirmation, or infer exact Ward from numerical five-point differences.

## STEP44 EXACT NEXT RED GATES

1. ASSEMBLE a coherent byte-authentic original Step33g/37/39 GitHub dependency worktree and RUN the above `--physical` mode. Print and commit actual seven-radii Kij/C/W/D/high jets and BOTH compact lapse-pair Gauss full-vs-C comparisons, scan h and quadrature. The normal shell cannot DNS-clone Github; do not fabricate a result.
2. Determine on the PHYSICAL original all-six-pair kernel whether high jets, `D=0`, `W=0` are exact identities or identify obstruction. Derive `(K01)'` analytically/certified, construct or refute exact continuous C=0 preserving both positive dust densities and center chart.
3. ONLY on exactly primary+secondary constrained data compute full canonical Dirac **time preservation**, rank, lapse fixing including exceptional K/J sectors and boundary.
4. Only after that genuine nonhomothetic on-shell evolution, same-action De Felice/Aoki controls, Candidate-C fold and observational validity. Keep independently audited sign-reversed-f-EH JHR manuscript separate.

**FINAL: STEP43 EXACT FORMAL WARD CRITERION PASSES AND FALSE-ZERO COUNTEREXAMPLES PROVED. PHYSICAL JANUS WARD/SECONDARY NOT VERIFIED. GATE_2B OPEN; JANUS-R NOT VALIDATED.**

---

# JANUS — REPRISE PRIORITAIRE : STEP42 COMPLETE — 2026-10-21

**BRANCH ACTIVE UNIQUE:** `research/gate2b-nonhomothetic-transfer`. Ne modifier ni `main` ni `research/v2-flrw`.

**LIRE EN PREMIER:** `research/STEP42_CENTER_PARITY_AND_SHARP_POSITIVE_DUST_AUDIT.md`.
**RAPPORT:** `research/reports/gate2b-step42-report.json`.
**SOURCE:** `numerics/hr_step42_center_regular_interval.py` — Git blob `e6f2b5da131d142c0d443e7077cb826125450b05`.
**TESTS:** `tests/test_hr_step42_center_regular_interval.py` — Git blob `5b63eaeb5135dd524f7ec1c5bd744541c95be6d7`.

REPRO SUR UN VRAI CHECKOUT DE LA BRANCHE:
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step42_center_regular_interval.py
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step42_center_regular_interval
```

## CE QUI A ETE REELLEMENT EXECUTE

- `17/17` nouveaux tests ciblés passés dans `/mnt/data/janus-step42` en ~2.08 s. Les NOUVEAUX fichiers source/test effectivement exécutés ont des Git blob SHAs strictement identiques aux fichiers déposés et reconsultés sur GitHub.
- Le test utilise un **MINI RAPPORT STEP41 LOCAL** contenant les NEUF vrais coefficients archivés et leur SHA256, pas le fichier original complet téléchargé. Le VRAI `research/reports/gate2b-step41-report.json` a été interrogé via le connecteur GitHub et les neuf coefficients, le SHA256, le chemin `status.GATE_2B` et le blob `16c8de6ee66725622c40ba2f327c8aafa99a5cb7` sont vérifiés. Pas de nouveau run avec les fournisseurs originaux Step33g/39/40 ou test de l'intégralité du dépôt. Git clone par shell bloqué par DNS, GitHub Actions toujours désactivés.
- Erreur de sérialisation corrigée par NORMALISATION EXACTEMENT CONFORME à Step41: le vrai rapport contient certains zéros JSON `0`, et le SHA `bff542954a2ddba0505223d0d08075e3714dcebed23cd3c9012bd67c91d28b2d` a été calculé en convertissant les coefficients en `float`, où leurs zéros deviennent `0.0`. Un contrôle naïf du JSON aurait échoué à tort.
- SUR TOUT LE CONTINUUM `0 <= r <= 0.85`, pour la configuration canonique Step41 CORRIGEE, bornes exactes via 256 intervalles rationnels `s=r²`: `p_g/r² > 0.8854`, `p_f/r² > 0.1114` (borne fixe largement plus serrée que l'ancienne boîte de corrections `>0.039`), `J(S_f/S_g)>0.659`, `K/r²>0.229`, avec coefficients poussière, dérivées `S'_i` et racine de déplacement strictement positives.
- NOUVEAU CONTROLE CENTRE: expansions algébriques `p_{L_i}=r² a_i(r²)`, `p_{S_i}=r b_i(r²)`, `p_i=r² d_i(r²)` avec `d_i>0`, `D_g=r³ e(r²)`, `K=r² k(r²)` avec `k>0`. Toutes les fonctions normalisées sont analytiques pour `s∈[0,0.85²]` car les dénominateurs et radicaux nécessaires sont contrôlés. Métriques spatiales conformes lisses en coordonnées cartésiennes, horloges poussière scalaires paires, vecteur déplacement radial linéaire; **PAS** encore une extension générale des densités tensorielles canoniques ni un espace-temps 4D évolué.
- Contrôle indépendant avec les ADM sphériques originaux non simplifiés et les deux poussières à 6 rayons non nuls, plus limites au centre et subdivision 64/128/256. C'est de l'évidence ciblée, pas la suite entière ni revue externe.

## PROCHAIN VRAI VERROU : STEP43

1. Reconstituer enfin la CHAINE COMPLETE DE DEPENDANCES EXACTEMENT IDENTIQUES AUX BLOBS GITHUB et relancer Step41+42 et les anciennes suites ciblées dans un checkout cohérent. Enregistrer SHA et résultats, ne pas substituer des reconstructions sans les étiqueter.
2. Dériver analytiquement (ou prouver par intervalles) `(K01)'(r)` du crochet Poisson mixte pour les SIX couples canoniques et donc `C_local(r)=K00-(K01)'` sans plancher de différences finies. Résoudre `C_local(r)=0` IDENTIQUEMENT sur un intervalle courbe non comobile à deux poussières strictement positives, ou réfuter honnêtement.
3. Seulement sur des données satisfaisant les contraintes secondaires EXACTES: calculer `{C_local,H_total}`, matrice de Dirac, lapses fixés, secteurs K/J exceptionnels et r=0 régulier.
4. Puis évoluer véritablement les deux métriques non homothétiques sur les équations du même lagrangien, recouper De Felice et Aoki et examiner le premier pli du Candidate-C. Signes f-EH inversés du JHR externe = piste CRITIQUE SEPAREE.

**ETAT FINAL:** Step42 centre et sources positifs PASS restreint, secondaire courbe exacte = OPEN; Dirac préservation/lapses = OPEN; `GATE_2B=OPEN`; `JANUS-R NOT VALIDATED`.

---

# JANUS — AUTHORITATIVE RESTART — STEP41 COMPLETE — 2026-10-21

**ACTIVE BRANCH ONLY:** `research/gate2b-nonhomothetic-transfer`. Do not modify `main` or `research/v2-flrw`.

**FIRST READ:** `research/STEP41_ACTUAL_PROFILE_CONTINUOUS_POSITIVE_TWODUST_AUDIT.md`.
**CODE:** `numerics/hr_step41_profile_bridge.py`.
**TESTS:** `tests/test_hr_step41_profile_bridge.py`.
**MACHINE REPORT:** `research/reports/gate2b-step41-report.json`.
**PREVIOUS THEOREM:** `research/STEP40_CURVATURE_BOX_AND_TWODUST_INTERVAL_AUDIT.md`.
**PREVIOUS PHYSICAL INITIAL DATA:** `research/STEP39_DUAL_SMEAR_AND_HIGHORDER_AUDIT.md`.

Targeted run:
```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step41_profile_bridge.py
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step41_profile_bridge
```

## DURABLE RESULT — CLOSED PREVIOUS STEP40→STEP39 BRIDGE

- On Step39 curved/noncomoving two-dust PRIMARY+numerically approximate-secondary profile `solve_five_point(scale=.1,degree=4,iterations=6,h=.001)`, the FULL computed f-momentum generator coefficients are:
```python
f_delta = (-2.1921905214999423e-05, 0.0, 0.0015479757723131573, 0.0,
           -2.0933708880890434e-05, 0.0, -1.757101536020765e-07, 0.0,
           -2.9380881416697167e-09)
```
- Canonical JSON coefficient SHA-256: `bff542954a2ddba0505223d0d08075e3714dcebed23cd3c9012bd67c91d28b2d`.
- **MAX |even f_delta|=0.0015479757723131573**, ALL odd = exactly 0, exact binary64 rational margin to the Step40 independent coefficient cap `1/200` is `397991296652400363/115292150460684697600` ≈0.0034520242276868426. This is strictly positive, hence the already PROVEN exact 256-cell Step40 interval certificate COVERS THE SPECIFIC Step39 corrected canonical initial data.
- Therefore for every r ∈[0,.85], **strict normalized continuum dust positivity**: `p_g/r²>0.885`, `p_f/r²>0.039`. For r>0 radial canonical p_i>0; at the spherical center p_i(0)=0 due to r². Fixed Step39 metric also satisfies Step40's exact uniform J(Sf/Sg)>.5039 and K/r²>.1596 (coordinate K(0)=0).
- Extra actual 73-point numerical check r=.03...85 (NOT itself a proof): max |C_local|=6.551957240641393e-11, max |C_local/r²|=9.068452928223382e-11, four primaries max 3.885780586188048e-16, sampled min pg/r²=.8856073159, pf/r²=.111864833.
- **11 new tests PASSED (~4.84 s)** on isolated reconstructed `/mnt/data/janus_step41/repo`. Both NEW source/test byte-matched GitHub blobs `26f4d5d24069dac469bf449da4c5997db6a15253`, `34fd411dad5bfa87ec30245cff949102a1328731`. CRITICAL: historical Step33g/39 source mathematical equations and Step40 exact interval arithmetic were independently reconstructed in this execution, NOT byte-identical to actual historical GitHub providers. A full authentic clean-provider Step41 rerun is still needed. Previous Step39/Step40 source-authenticated runs stand separately, not rerun today; no complete repo suite or GitHub Actions.
- Test boundary issue intentionally caught: Python binary64 `float(.005)` lies slightly ABOVE exact 1/200; strict Fraction membership rejects it, tests use `math.nextafter(.005,0.)` as passing just-inside control. Actual coefficient safety margin >0.00345, so not a borderline conclusion.

## NEW PRIORITY STEP42 (TRUE SCIENTIFIC RED)

1. Re-run new bridge **against byte-exact historical actual GitHub Step33g/37/39/40 providers in ONE worktree**, log hashes and actual tests.
2. Compute analytic / independently validated spectral `K01'(r)` and rigorously construct/verify `C_local(r)=0` as a **CONTINUUM** noncomoving curved condition (or establish an obstruction), preserving both positive dusts and genuine spherical regularity. Last best numerical local result ~1e-11 is NOT zero.
3. Compute full six-canonical-pair functional Dirac **TIME PRESERVATION of the secondary** and determine actual lapse fixing, Poisson rank, K/J exceptional branches. Generic Hassan–Rosen ghost-free lore alone is insufficient.
4. Only if above succeeds: genuinely nonhomothetic ON-SHELL evolution and both same-reduced-action De Felice finite-H mu→0 and Aoki nonlinear KS,cS² physical controls before Candidate-C first fold, then any observational tests.

**VERDICT: STEP41 specific corrected two-dust continuum positivity=PROVED CONDITIONAL ON FIXED INITIAL-DATA FAMILY; CURVED EXACT BD SECONDARY OPEN; FULL DIRAC OPEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.**

---

# JANUS — AUTHORITATIVE RESTART — STEP40 COMPLETED — 2026-10-20

**ACTIVE RESEARCH BRANCH:** `research/gate2b-nonhomothetic-transfer` ONLY; `main` and `research/v2-flrw` remain untouched.
**READ FIRST:** `research/STEP40_CURVATURE_BOX_AND_TWODUST_INTERVAL_AUDIT.md`.
**CURRENT REPORT:** `research/reports/gate2b-step40-report.json`.
**CODES:** `numerics/hr_step40_curvature_box.py`, `numerics/hr_step40_twodust_interval.py`.
**TESTS:** `tests/test_hr_step40_curvature_box.py`, `tests/test_hr_step40_twodust_interval.py`.

Reproduce from a branch checkout (only these four new Python files need numpy-free pure Python + pytest):

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step40_curvature_box.py tests/test_hr_step40_twodust_interval.py
# GENUINELY EXECUTED: 35 passed in 1.80 s on isolated /mnt/data/janus-step40
PYTHONPATH=. python -m numerics.hr_step40_curvature_box
PYTHONPATH=. python -m numerics.hr_step40_twodust_interval
```

ALL FOUR locally EXECUTED bytes correspond exactly to uploaded GitHub Git blob hashes, as recorded in the Step40 audit+report. Do NOT claim whole-repo suite, enabled GitHub CI, or joint Step39+40 run. Previous Step39 genuinely authenticated test groups were 32+5 separately, not reexecuted today.

## SCIENTIFIC RESULT — CONTINUUM, EXACT RATIONAL, BUT RESTRICTED

1. For EVERY independent spherical conformal curvature `|c_g|,|c_f|<=.015` and ALL r∈[0,.85] at benchmark a=.4,y=.5787707228025044: `J(Sf/Sg)>=0.5039461792087735` and `K(r)/r²>=0.15968997603142235`; the displayed figures are decimal renderings of **exact strict Fraction certificates**. A second uniform background box with a∈[.395,.405], y∈[.5787,.5789] retains J>=.5034934 and K/r²>=.1516989. These bounds concern ONLY the specified conformal spatial metric ansatz; no Dirac degrees-of-freedom result.
2. Exact negative control: antialigned `c_g=+c,c_f=-c` at r=.85 attains algebraic J=0 for c≈.07854905913576 (certified by rational bisection between .07854 and .07856), showing that unrestricted curvature positivity is false.
3. For the ACTUAL uncorrected curved/noncomoving Step37 primary family with two DISTINCT dust phase gradients and nonzero relative shift, exact outward **rational INTERVAL** arithmetic, partitioning s=r²∈[0,289/400] into 256 rational subintervals, proves `p_g(r)/r²>0.885`, `p_f(r)/r²>0.114` for ALL 0<=r<=.85. The canonical radial densities p_i(0)=0 because of r² spherical weight; positivity is strict for r>0 and normalized density remains strictly positive at r=0.
4. Robust perturbation guarantee: for ANY independent coefficients `|delta_(2k)|<=.005`, k=0..4, with all odd corrections ZERO in `Q_f=(pLf)'/(2r(1+5c_f*r²))`, exact interval arithmetic certifies `p_g/r²>0.885`, `p_f/r²>0.039` over the ENTIRE interval. These inequalities are certified even if all five corrections vary adversarially and independently; they do NOT yet establish that the specific Step39 corrected profile has coefficients within this ball. Check first!
5. Independent original unsimplified two-sector Hamiltonian formula was reconstructed in the tests and compared at several radii for baseline and nonzero perturbations. Exact interval pass is NOT based on floating-point sampling.

## NEXT SCIENTIFIC ACTION — STEP41 (HARD RED)

**FIRST:** Reconstruct/check original byte-authenticated Step33g/37/39 providers, RUN `solve_five_point(scale=.1,degree=4,iterations=6,h=.001)` and PERSIST ALL FINAL `f_delta` coefficients (they were missing from Step39 JSON summary), verifying `delta_odd=0` and `max |delta_even|<=.005` exactly with conservative float-to-rational conversion. If within ball, the Step40 theorem extends continuous dust positivity to the actual Step39 high-order **approximate-secondary** profile; otherwise enlarge or replace certificate and report. Do not silently claim this link has been made.
**SECOND:** Derive or cross-verify actual analytic/spectral derivative of K01 and solve local C(r)=0 **as a continuous constraint** with primary, two dusts, shift/center regularity.
**THIRD:** Calculate FULL six-canonical-pair Dirac `{C_local,H_T}` and lapse fixing, including K/J degeneracy. Generic HR background folklore alone is insufficient.
**FOURTH:** Only then physically nonhomothetic on-shell + both same-action De Felice/Aoki controls, Candidate-C fold and observational tests, positive-EH JANUS-R separate from external sign-reversed JHR audit.

**VERDICT: STEP40 CONTINUOUS EXACT RESTRICTED CHART+DUST POSITIVITY GREEN; CURVED EXACT SECONDARY OPEN; DIRAC TIME PRESERVATION/LAPSE FIXING OPEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.**

---

# JANUS — AUTHORITATIVE RESTART — STEP39 COMPLETED — 2026-10-20

**BRANCH TO CONTINUE ON:** `research/gate2b-nonhomothetic-transfer` ONLY. DO NOT modify `main`, `research/v2-flrw`.
**FIRST READ:** `research/STEP39_DUAL_SMEAR_AND_HIGHORDER_AUDIT.md`.
**MACHINE REPORT:** `research/reports/gate2b-step39-report.json`.
**ORIGINAL ACTION CROSS ORACLE:** `numerics/hr_step39_cross_oracle.py`.
**FOURTH-ORDER RADIAL SECONDARY:** `numerics/hr_step39_highorder_secondary.py`.
**TESTS:** `tests/test_hr_step39_cross_oracle.py` and `tests/test_hr_step39_highorder_secondary.py`.
**PREVIOUS:** `research/CONTINUOUS_SPATIAL_JK_AND_POISSON_EXTRAPOLATION_STEP38_AUDIT.md`, `research/CURVED_APPROX_SECONDARY_STEP37_AUDIT.md`.

## LATEST ACTUALLY EXECUTED, EXACT GITHUB BYTES

For the first time, **ALL historical Step33g/37/38 providers and current Step39 source/tests were reproduced with EXACT matching Git blob hashes in ONE coherent /mnt/data/janus-step39 isolated worktree, WITHOUT adapters**. Eleven source/test SHA values and full commands appear in Step39 audit/report. Shell Git clone DNS unavailable, and NOT a complete checkout/full repository suite. GitHub workflows disabled.

Run as TWO SEPARATE pytest processes due all-in-one time/memory issues:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step37_curved_solver.py tests/test_hr_step38_continuum_gate.py tests/test_hr_step39_cross_oracle.py
# independently executed 32 PASSED

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step39_highorder_secondary.py
# independently executed 5 PASSED

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step39_cross_oracle
# independently executed; emits two-smearing IBP Poisson and five-point h scan
```

**IMPORTANT PROVENANCE:** 32+5 = 37 TARGETED PASSES in TWO workers. The combined single-worker attempt TIMED OUT after ~34 dots. A subprocess aggregator also timed out after first group despite second group separately succeeding. Do NOT claim one successful combined 37-test suite. No full GitHub repo test run or external validation.

## NEW SCIENTIFIC RESULT

1. Frozen Step37 h=.001 degree4 five-correction curved two-positive-dust profile: two independent compact lapse pairs A (support .2-.7) and B (.25-.73). Direct original non-IBP six-pair bracket at N up to **2561** vs analytic IBP full Kij lapse-jet Gaussian integral give conditional continuum estimates **A +5.3617022e-9**, **B +3.3387069e-9**. Both methods agree under grid extrapolation, so do NOT call Step37 frozen profile an exact zero-secondary solution. Discrete original primary residual has floating-point roundoff increase at N2561.
2. Re-solving with three-point radial derivative step h halved from .001 to .0000625 yields pair A full-jet bracket **+5.3611625e-9 -> +2.1019511e-11**; local max sampled |C| **9.3489e-8 -> 4.1507e-10**. Strong O(h²) derivative floor explains much of the old residual.
3. New **FIVE-POINT O(h^4)** derivative with six iterations, even-degree4 f momentum generator: at h=.001 max sampled |C_local| ≈**5.02e-11**, pair A full-jet integral ≈**7.91e-14**, pair B ≈**1.32e-13**. Result plateaus under h refinement; may be polynomial fit/roundoff/physical, **NO proof C_local(r)=0 for all r**.
4. Improved 5-point baseline coefficient at r=.43 is **0.471663864165** rather than 3-point h=.005 **0.471665550745** (prior approximate reference had O(h²) bias). Tests explicitly updated instead of forcing agreement with old low-order reference.
5. At sampled radii both independent dust canonical momenta remain positive, exact curved primaries roundoff ≈2.2e-16. Continuous J(Sf/Sg), K/r² positivity for the fixed metric was PROVED at Step38. Two-dust continuous-interval positivity, exact central regularity and arbitrary deformations are NOT certified.

## NEXT HARD RED: STEP40

- Seek exact analytic/spectral radial derivative of K01 (independently check the ORIGINAL EH+HR+two-dust bracket), then degree4→6+ or a convergent spectral solver and direct, interval-wide |C(r)|/r² error and both positive dust bounds. Report a negative obstruction if encountered, do not force exact zero.
- On genuinely simultaneous primary+EXACT secondary data compute field-theory FULL DIRAC TIME PRESERVATION `{C_local,H_T}` across all six canonical pairs and lapse fixing; test K/J exceptional branches and r=0 coordinate factors carefully.
- Only after proving or refuting this: physically nonhomothetic ON-SHELL dynamics, SAME physical action De Felice finite-H mu→0 and Aoki nonlinear K_S,c_S² stable/unstable oracles; then fold and observations.

**VERDICT: STEP39 NUMERIC TWO-ORACLE IMPROVED SECONDARY; GENERAL BD/DIRAC CONSTRAINT PRESERVATION OPEN; GATE_2B OPEN; JANUS-R NOT VALIDATED.** Distinct external sign-reversed f-EH JHR manuscript track unchanged.

---

# JANUS — REPRISE PRIORITAIRE : STEP38 — 20 OCT 2026

**ACTIVE BRANCH ONLY:** `research/gate2b-nonhomothetic-transfer`. Do not touch `main` or `research/v2-flrw`.
**FIRST READ:** `research/CONTINUOUS_SPATIAL_JK_AND_POISSON_EXTRAPOLATION_STEP38_AUDIT.md`.
**SOURCE:** `numerics/hr_step38_continuum_gate.py` (`1e4874050d2a8e478cc2414580c737f69cee6309`).
**TESTS:** `tests/test_hr_step38_continuum_gate.py` (`cd9a7625c7a62beec0cc952b91d3b929ec1fce96`).
**NEW PERSISTED REPORT:** `research/reports/gate2b-step38-report.json`.
**REPRO COMMANDS:** `PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python -m pytest -q tests/test_hr_step38_continuum_gate.py` and `PYTHONPATH=. python numerics/hr_step38_continuum_gate.py` from repo root.

## ACTUALLY COMPLETED AT STEP38

- 11/11 new targeted tests PASS in isolated `/mnt/data/janus-step38` Python workspace (~0.08 seconds); **new source and test Git blobs exactly match the locally executed bytes and the current GitHub source**. The local workspace reused the four exact numerical PB data rows of the Step37 published JSON in a minimized fixture; NOT a full GitHub checkout or Step37 recomputation. The Step37 provider modules were NOT byte-exactly exercised this session, and CI remains disabled.
- **Continuous EXACT-RATIONAL interval proof, fixed Step37 metric ansatz only:** at a=.4,y=.5787707228025044, cg=.0015,cf=-.0012, and **every** radius 0<=r<=.85, J(Sf/Sg)>=0.6598708967925059, and K(r)/r²>=0.22774976204166372. For 0<r<=.85, K(r)>0; K(0)=0 from coordinate r². This is not a proof of central Dirac rank, arbitrary metric variation or continuous positivity of the dust densities.
- **Numerical correction to Step37 interpretation:** from exact four archived original non-IBP mixed-bracket records n=81,161,321,641, two-level Richardson (assumes even h² expansion) estimates **CONTINUUM B0≈+5.361704637064764e-9 after** five corrections and **B0≈+0.009387437474193680 uncorrected**. Two independent R4 windows differ 1.2721120e-13, but this is NOT a rigorous uncertainty bound, does NOT prove exact nonzero B0, and certainly does not prove B0=0. The n=641 negative bracket is affected by O(h²) discretization.
- Neither the exact curved local C(r)=0 **nor** its Dirac time preservation, two-dust lapse-fixing, the fully nonhomothetic Einstein-HR on-shell solution, De Felice/Aoki same-action physical oracles, fold regularity or observations are validated.

## NEXT NONNEGOTIABLE RED — STEP39

1. **REAL-PROVIDER CLEAN REPRODUCTION FIRST:** Assemble a coherent byte-identical GitHub worktree of original Step33g provider modules, modified Step37 builder, Step37 solver/tests and Step38 analyzer/tests; execute actual targeted suites and runner. Current shell DNS cannot directly clone GitHub; do not claim it has been done.
2. Recompute original non-IBP finite-grid Poisson bracket with stronger resolution (n>=1281 after efficiency changes) and at least two unrelated compact smearings; compare extrapolated B0 with integral of independent C_local(r) and derivative-stencil h scans. Reject any false apparent zero.
3. Establish continuous/controlled C_local=0 with certified two-dust positive densities and center/boundary regularity; independently handle J/K exceptional branches. Current Step37 finite points NOT SUFFICIENT.
4. Compute **full six-canonical-pair field-theory Dirac preservation** of secondary and lapse-fixing. If it fails, register the negative result.
5. Only then genuine nonhomothetic on-shell evolution, independent De Felice finite-H mu->0 and homothetic nonlinear Aoki kinetic/gradient oracles on SAME reduced action before first Candidate-C fold.

**VERDICT: STEP38 exact spatial J/K positivity conditional GREEN; Richardson PB limit DIAGNOSTIC only; GATE_2B OPEN; JANUS-R NOT VALIDATED.** The external negative f-EH-sign JHR manuscript audit remains a DIFFERENT project thread.

---

# JANUS — AUTHORITATIVE RESTART — 2026-10-20 — STEP37 (CURRENT)

ACTIVE BRANCH ONLY: research/gate2b-nonhomothetic-transfer. Preserve main and research/v2-flrw.

FIRST READ: research/CURVED_APPROX_SECONDARY_STEP37_AUDIT.md
CODE: numerics/hr_step37_curved_solver.py, numerics/hr_step37_original_nonibp_oracle.py, updated numerics/hr_curved_moving_dust_primary.py
TESTS: tests/test_hr_step37_curved_solver.py
RUNNER: scripts/verify_gate2b_step37.py
COMMITTED REPORT: research/reports/gate2b-step37-report.json

REPRODUCTION in a true, complete branch worktree:
  OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step37_curved_solver.py
  OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step37.py /tmp/gate2b-step37-repro.json

## LATEST VERIFIED

- Curved nonproportional and noncomoving two-dust spherical primary data, nonzero HR shift, two independent positive dust canonical momenta. Even-momentum parity near the center.
- Five iterative corrections applied to the ACTUAL CURVED local mixed Hamiltonian Poisson coefficient C_local=K00-(K01)' after radial smearing derivative cancellation. On NINE off-fit radii, max absolute local C decreases 0.801743553 -> 9.58445952e-8; all primary constraints at those sites have residual <=2.22e-16. Not a rigorous continuous exact solution.
- Independent ORIGINAL NON-IBP nodal six-canonical-pair bracket at 641 nodes decreases +.00938740055 -> -3.15636675e-8, with expected second-order grid residual decrease, not zero to machine precision.
- Real 12 NEW tests PASS (isolated reconstructed /mnt/data/janus-step37); NEW solver, oracle and test source Git blob SHAs match executed bytes. CRITICAL PROVENANCE: Step33g core modules were mathematical compatibility adapters in the fresh local workspace, NOT the literal GitHub original dependencies. Original provider clean regression PENDING. Earlier Step33/35/36 tests were not combined with the 10. GitHub Actions remain disabled.
- Implementation fix: polynomial momentum generator Q_f=(pLf)'/(2r) needs conversion (n+2)/2 to modify pLf/r²; omission caused a spurious residual plateau. Protected by flat controls.
- Parity regular at formal center by ansatz, but fully center-regular 4D evolution NOT SHOWN. Spherical K(r) coordinate factors vanish at r=0, and both positive dust values are NUMERICAL sample checks, not certified interval bounds.

## NEXT EXACT RED — STEP38

1. Run the Step37 test and regeneration runner with BYTE-EXACT real Step33g provider modules in a coherent complete Git checkout; fix any regressions.
2. Test radial fit-degree/h/support convergence and both dust positivity on an entire interval, ideally prove or find exact curved C_local=0. Nine-point near-zero is insufficient.
3. On simultaneous primary+secondary data calculate full Dirac time preservation brackets with ALL six canonical pairs, their rank, and solve the lapse-fixing condition. Handle J(Sf/Sg)=0 and K=0 separately from spherical coordinate r=0.
4. Only after that: genuinely nonhomothetic Einstein-HR two-dust on-shell evolution, same-action De Felice finite-H mu->0 and nonlinear Aoki K_S,c_S² controls, then test Candidate-C first fold a~0.0301646 and physics.

VERDICT: Step37 NUMERICAL APPROXIMATE secondary GREEN; GATE_2B OPEN; JANUS-R NOT VALIDATED. Distinct external wrong-sign-f-EH JHR critique is unchanged.

---

# JANUS — ACTIVE RESTART / 20 October 2026 — Step36 (CURRENT)

**WORK BRANCH:** `research/gate2b-nonhomothetic-transfer` ONLY. Do NOT touch `main` or `research/v2-flrw`.

**READ FIRST:** `research/CONTINUOUS_J_GATE_STEP36_AUDIT.md`
**SOURCE:** `numerics/candidate_c_continuous_j_certificate.py`
**TESTS:** `tests/test_candidate_c_continuous_j_certificate.py`
**REPORT:** `research/reports/gate2b-step36-report.json`

Run targeted reproduction:

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_candidate_c_continuous_j_certificate.py
python numerics/candidate_c_continuous_j_certificate.py
```

## What actually ran, and what is new

- Step36 `19/19` targeted exact-rational certificate tests PASS in **isolated reconstructed** `/mnt/data/janus-step36`. Source/test committed Git blob SHA byte-identical to local executed source/test: `375e6c3197fb9d82f19b35c66331bab2675cd506` and `5b2634d0ac8a99915617ba27785b728f03a1ec00`.
- A **continuous conditional algebraic proof**, replacing Step35's 30-point scan: for every DUST-only Candidate-C a∈[0.025,1], there is exactly one calibrated quartic branch root y∈(0.556,2.3), with **J(y)>1/2** throughout. Other quartic roots outside this interval not excluded. Decimal parameters are taken as exact terminating rationals for the proof, not universally exact physics constants.
- Independent 85-step strict rational bisection: at earlier proposed fold a≈0.0301646, y≈1.971261154529 and J≈37.4491969831. **Thus J=0 is NOT a cause of that fold within this DUST-only calibrated background**. This is NOT a kinetic/gradient/constraint regularity or physical fold-crossing verdict.
- **NEW JOINT REPRODUCTION:** `OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_regular_secondary_flat.py tests/test_candidate_c_continuous_j_certificate.py` -> **30 passed in 0.35 s**, one isolated reconstructed `/mnt/data/janus-step36` workspace. All FOUR Step35+36 Python source/test Git blobs match exactly. **Not** a full-repository suite or GitHub CI. The orphaned Step34 checkpoint remains unresolved.

## NEXT HARD RED (Step37) — do not confuse with previous algebraic proof

1. On the earlier exact curved/noncomoving TWO-dust primary family (`numerics/hr_curved_moving_dust_primary.py`) explicitly compute `C_local(r)=K00(r)-(K01)'(r)` from the actual mixed functional Poisson bracket, over a **radial interval**, not only r=.43.
2. Find an independent radial momentum/metric profile satisfying **BOTH** primary constraints, diagonal momentum and regular shift AND `C_local(r)=0` pointwise while BOTH dust densities stay strictly positive. A mere vanishing integrated smear bracket is insufficient. A useful linearized candidate for curvature source S is `delta X(r)=-int_0^r S(s) ds /(A r^3)`, A=m² Mg² a² J/2, ONLY after computing genuine source S and proving center regularity. No curved continuation is solved yet.
3. Then explicitly calculate the FULL Dirac preservation and local lapse-fixing bracket with all six canonical pairs, including curvature terms and `K=0,J=0` exceptional sectors. Distinguish the coordinate center r=0 (spherical r² factors) from physical degeneracy.
4. Finally genuinely nonhomothetic ON-SHELL two-dust Einstein-HR dynamics and **both** same-physical-action De Felice finite-H μ→0 and Aoki nonlinear K_S,c_S² stable/unstable oracles BEFORE first fold, then observational gates if justified.

**VERDICT: STEP36=PASS as restricted algebraic background certificate; GATE_2B=OPEN; JANUS-R NOT VALIDATED.** Opposite-EH-sign external JHR manuscript audit remains separate.

---

# JANUS — ACTIVE RESTART / 20 October 2026 — Step35

BRANCH: research/gate2b-nonhomothetic-transfer. Leave main and research/v2-flrw untouched.

**FIRST READ:** research/RESTRICTED_REGULAR_CENTER_SECONDARY_STEP35_AUDIT.md
**SOURCE:** numerics/hr_regular_secondary_flat.py
**TEST:** tests/test_hr_regular_secondary_flat.py
**REPORT:** research/reports/gate2b-step35-report.json
**REPRO:** OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_regular_secondary_flat.py

## Latest actually executed

11/11 targeted tests passed in isolated reconstructed /mnt/data/janus-step35 (Python with numpy and pytest), using source/test with Git blob SHAs d30281a11d854084270a4f536e24e2dc857d58fc and 6425b1c36c8d7e4401bfffe6dabf4f9b31f58cc6. Whole repository and other prior Step33/34 tests were NOT rerun. GitHub workflows disabled; full clone DNS unavailable.

## Scientific increment

On previously derived Step33f exact flat/comoving, nondegenerate-J local mixed Poisson bracket, C_flat = (m² Mg² a² J/2)*(r³ X)' with X=Pg/(Mg²a)-Pf/(Mf²b). Hence local C=0 implies r³ X=constant; CENTER REGULARITY forces X=0 everywhere. This NECESSITY (not just sufficiency) holds only in this restricted family.

An explicit radially varying positive TWO-dust primary+restricted-secondary witness at a=.4 has pg/r²>=.9, pf/r²>=.124128 on [0,1] for eps=.08; 5 eps cases including -.15 remain positive. Deliberately perturbing Pf separately retains the primaries but violates the secondary. Thirty dust-only Candidate-C points have J>.52; J=0 is an EXCLUDED degenerate relative-shift chart, not proven safe.

## WARNING: orphaned Step34 checkpoint

research/STEP34_CHECKPOINT.txt exists but referenced Step34 audit, test, runner and JSON do not appear in branch tree; only its source numerics/hr_original_discrete_pb.py exists. No new claim that historical Step34 tests can be rerun from this repository.

## HARD NEXT RED

Construct curved/noncomoving primary+LOCAL SECONDARY=0 on continuous radial interval using C_local=K00-(K01)' (not mere integral); preserve positivity of both dust densities, relative-shift K/J nondegeneracy, center regularity. THEN compute Dirac time preservation, full bracket rank and lapse fixing; THEN same-action nonhomothetic on-shell + De Felice/Aoki physical oracles before first fold. Distinct external JHR wrong-EH-sign audit stays separate.

VERDICT: STEP35 restricted rigidity tested; GATE_2B=OPEN; JANUS-R NOT VALIDATED. No physical ghost/gradient/fold/CMB viability conclusion.
