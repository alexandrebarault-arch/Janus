# JANUS b3c3d6 — rejeu physique Step55 et certificat de défaut DOP853 corrélé (30 octobre 2026)

**Résultat : certificat conditionnel de l'erreur de l'EDO spatiale Step55, pas validation JANUS. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance et exécution réelle

Quatre sources originales ont été matérialisées **octet pour octet** depuis GitHub, puis contrôlées par Git blob SHA-1 :
- `numerics/hr_step45_exact_physical_ward.py` : `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
- `numerics/hr_step46_exact_secondary_ode.py` : `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
- `numerics/hr_step55_normalized_secondary.py` : `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`.
- `numerics/hr_step55_global_barrier.py` : `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.

La barrière originale Step55 a été **réexécutée sur 256 cellules : PASS**, avec les marges rationnelles originales :
`Fplus_max=-1480966474499367232302129/10000000000000000000000000000` et
`Fminus_min=295653233337826329055403/2000000000000000000000000000`.
La preuve concerne la solution analytique régulière centrale Step49 et le tube `|U-Ustar|<=1/10000` sur `0<=s<=289/400`.

Un **nouveau candidat physique DOP853** a été généré en évaluant le membre droit de l'EDO original `G` par le milieu de son intervalle sortant `I` aux arguments binary64 de SciPy. Il ne s'agit **pas** du rejeu byte-identique d'un ancien script d'intégration DOP853 : le candidat est néanmoins vérifié *a posteriori* par le résidu physique continu de `G`, indépendamment de la méthode numérique ayant produit ses coefficients.

Paramètres : `solve_ivp(method='DOP853',rtol=1e-12,atol=1e-15,dense_output=True)`, de `float(1e-4)` à `float(Decimal('0.85')**2)`, 28 pas, 482 évaluations RHS. Le polynôme dense est reconstruit en fractions exactes à partir des coefficients binary64 de SciPy. Les 28 domaines sont ceux des **vrais** temps binary64, y compris `xmax=(t-t_old)/h`.

## Certificat rationnel du même tube et de l'erreur

Le garde Bernstein **corrélé** `P(s)-Ustar(s)` passe sur **28×256=7 168 sous-cellules**, sans utiliser les anciennes enveloppes indépendantes incorrectes. Le défaut continu `H=2sP'-G(s,P)+2P` est enclos sur les mêmes 7 168 sous-cellules avec l'arithmétique originale `I` (échelle `10^28`). Tous les sauts entre polynômes sont reconstruits exactement ; un saut non nul est détecté, de module `3.2108574423042794e-23` (affichage flottant).

**Nouveau contrôle indépendant de G_U sur exactement le tube Step55 :** dérivée symbolique `diff(G,U)` du moteur Step45/46, réévaluée par intervalles sortants sur les 256 cellules physiques. Résultat rationnel :
`-10010994328099382599714479353/10000000000000000000000000000 <= G_U <= -4969858031286385533119896427/5000000000000000000000000000`,
soit approximativement `[-1.001099433,-0.993971606]`. La borne supérieure est strictement négative, sans supposer le rapport historique Step63.

Au premier temps binary64, la barrière originale et le garde corrélé donnent
`E0 <= 5444517870735025903485243327742866201270407163729562725577373537/54445178707350154154139937189082913832960000000000000000000000000000`,
soit `0.0001000000000000002` en affichage flottant. Ce budget est grossier mais certifié ; aucun résidu central cubique `C` n'est requis.

Le registre rationnel avec `G_U<=0` (affaiblissement conservateur du contrôle plus fort ci-dessus) fournit :
- contribution initiale : `1.3840830449827016e-8` ;
- défaut continu : `4.835706173052662e-6` ;
- sauts : `3.0056739039330554e-26` ;
- **erreur terminale totale `|U(sR)-P(sR-)| < 1/200000 = 5e-6`**, valeur calculée `4.849547003502489e-6`. L'inégalité `<1/200000` a été vérifiée directement sur la fraction exacte, pas seulement par arrondi flottant.

La formule employée est `sR|eR| <= s0 E0 + (1/2) sum_i Ri (bi-ai) + sum_i bi |Ji|`, sous le tube commun et `G_U<=0`. Le certificat est **spatial Step55**, conditionnel à la branche centrale régulière déjà postulée/démontrée dans Step49 et reprise par la barrière Step55 ; il n'est ni une preuve de convergence générale de DOP853 ni un résultat Dirac.

## Tests et audit de portée

`PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_physical_correlated_replay.py' -v` : **3 PASS, 0 FAIL**, dont **1 intégration physique complète avec 7 168 gardes et résidus**, plus un contrôle indépendant `G_U` et les quatre SHA. `python -m compileall -q` des deux nouveaux fichiers : **PASS**. L'exécution séparée `python -m numerics.hr_b3c3d6_physical_correlated_replay` a aussi terminé et produit la fraction terminale exacte. Les nouveaux code et tests sont publiés avec octets identiques à ceux exécutés.

**Ce qui reste NON certifié :** le transport de la borne `U` vers les jets physiques Step58 et les **six enclosures A_N/A_M/B_N/B_M/E_N/E_M** ; l'annulation exacte éventuelle de B/E ; le BVP global des deux lapses strictement positifs aux deux vrais bords ; la chaîne Dirac six couples, rang, tertiaires, charges et jauge temporelle ; la dynamique 4D, la stabilité et les observables. Aucun original Step58 n'a été exécuté dans cette session. Une erreur de `U` de 5e-6 ne constitue **pas** une borne des coefficients Step58.

**Prochaine étape prioritaire :** propager rigoureusement les erreurs de `U,U_s,U_{ss}` depuis ce certificat jusqu'aux six coefficients Step58, avec contrôle de dépendances et factorisation, puis tester le BVP des lapses positifs aux deux vrais bords. Ne pas transformer des valeurs numériques B/E proches de zéro en identités exactes.
