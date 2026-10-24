# JANUS — Étape 67b : coefficient physique \(U_3\) rigoureusement encadré et reprise authentique de l'étape 55

**24 octobre 2026.** Branche d'écriture : `research/gate2b-nonhomothetic-transfer` uniquement. **Gate 2B OUVERT ; JANUS-R NON VALIDÉ.**

**Coexistence importante :** un rapport `research/reports/gate2b-step67-report.json` existait déjà dans le dépôt au moment de cette publication, avec une étude différente des jets du déplacement relatif. Il est **préservé sans modification**. Le présent travail complémentaire, avec son propre code, ses tests et son rapport, porte le nom **67b** pour éviter toute collision.

## 1. Sources physiques originales réellement exécutées ensemble

Contrairement aux derniers modules autonomes de l'étape 66, ce calcul importe et exécute les QUATRE fichiers historiques originaux, reconstitués octet pour octet dans un même environnement à partir du connecteur GitHub :

| Fichier | SHA-1 Git blob comparé au véritable dépôt |
|---|---|
| `numerics/hr_step45_exact_physical_ward.py` | `66aa43841dccfe4a5d586a49be9c10af3a67a10e` |
| `numerics/hr_step46_exact_secondary_ode.py` | `bac025c28dbe1561c0c36c56dbfda46dc326f804` |
| `numerics/hr_step55_normalized_secondary.py` | `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` |
| `numerics/hr_step55_global_barrier.py` | `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` |

Ces empreintes ont été vérifiées par `git hash-object` sur les OCTETS réels, puis par le code avant le calcul. Une modification d'un seul fichier historique provoque une erreur explicite. Le programme vérifie également toutes les identités de Ward d'origine du modèle sphérique positif-EH, Hassan–Rosen, deux poussières à **six couples canoniques** et la reconstruction exacte de sa secondaire radiale primaire-réduite.

La vraie expression `G(s,U)`, importée par `hr_step55_normalized_secondary.normalized_symbolic()`, possède **22 symboles libres avant fixation des données du benchmark** et est exactement de degré 2 en `U`, avec `G_{UUU}=0`. Ceci confirme directement le résultat précédent de l'étape 62.

**Important :** les modules temporels Step57/58/59/60, la preuve temporelle de Dirac et les équations d'évolution 4D ne sont **pas encore réunis** dans ce même environnement. Ne pas assimiler ce nouvel audit radial à leur exécution.

## 2. Preuve nouvelle par séries de Taylor à coefficients d'intervalles ENTIERS

Sur la branche radiale analytique régulière de l'étape 49, déjà certifiée dans les étapes 52/53/55, la réduction physique impose

\[
s=r^2,\qquad P(r)=p_{L_f}(r)=r^2U(s),\qquad
2s\,U_s=G(s,U)-2U.
\]

La dernière égalité se lit bien \(2sU_s=G(s,U)-2U\). Au centre, \(\partial_U G(0,U_0)=-1\), ce qui donne la récurrence non résonante

\[
(2n+3)U_n=[s^n]G(s,U_0+\cdots+U_{n-1}s^{n-1}).
\]

Le module `numerics/hr_step67_true_center_taylor_certificate.py` construit une nouvelle algèbre de polynômes tronqués à l'ordre \(s^3\), avec **chaque coefficient représenté par la classe d'intervalles entière à arrondis extérieurs de l'ORIGINAL Step55**, échelle \(10^{28}\). Il implémente addition, multiplication, puissance entière, inverse et racine carrée sur la branche positive, avec récurrences exactes des coefficients.

Tous les paramètres du benchmark ainsi que les données \(U_0,U_1,U_2\) sont extraits du **véritable module original `hr_step55_global_barrier.py`**, sans les remplacer par des nombres flottants. La géométrie exprimée dans l'algèbre des séries reprend les opérations du fournisseur historique ; les termes constants de ses variables physiques sont vérifiés comme englobant les valeurs calculées indépendamment par la fonction historique `geometry(0)`.

Les coefficients \(s^0,s^1,s^2\) du résidu de l'EDO, calculés avec les anciennes bornes de \(U_0,U_1,U_2\), contiennent tous exactement zéro. Le nouveau coefficient \(U_3\) est défini par le facteur EXACT \(9=2(3)+3\). L'évaluation entière extérieure fournit l'encadrement rationnel rigoureux :

\[
\boxed{
-\frac{31325163121998456229}{2500000000000000000000000000}
\le U_3 \le
-\frac{62650326243996887233}{5000000000000000000000000000}.
}
\]

La borne supérieure est STRICTEMENT négative, d'où

\[
\boxed{U_3\approx -1{,}253006524879938\times10^{-8}<0.}
\]

La largeur de l'intervalle est environ \(5{,}045\times10^{-24}\). La condition d'existence analytique au centre et les bornes initiales de \(U_0,U_1,U_2\) sont les résultats historiques des étapes 49/52/53 ; elles ne sont pas prouvées à nouveau ici.

En termes du moment canonique \(P(r)\),

\[
P(r)=U_0r^2+U_1r^4+U_2r^6+U_3r^8+\cdots,
\]
\[
\frac{P'''(r)}{r}
=24U_1+120U_2r^2+336U_3r^4+\cdots.
\]

Ainsi la correction en \(r^4\) de \(P'''/r\) vaut \(336U_3\approx -4{,}210101923596592\times10^{-6}\). Cette information enrichit les jets réguliers du centre requis pour le calcul temporel ; elle ne fixe pas les lapses à elle seule.

## 3. Vérification indépendante : ancien certificat GLOBAL relancé

Dans **le même** environnement des quatre originaux, j'ai réellement relancé la fonction `hr_step55_global_barrier.certify_global_barrier(cells=256)`. Les résultats correspondent aux fractions déjà publiées par l'étape 55 :

\[
\max F_+
=-\frac{1480966474499367232302129}{10000000000000000000000000000}<0,
\]

\[
\min F_-
=\frac{295653233337826329055403}{2000000000000000000000000000}>0.
\]

Cette vérification couvre les 256 intervalles du domaine continu prescrit \(0\le s\le289/400\), soit \(0\le r\le17/20\), avec arithmétique entière dirigée et signes stricts. C'est le **certificat spatial initial**, pas un théorème de conservation des contraintes en temps.

## 4. Tests, dépôt GitHub et périmètre

Nouveaux fichiers ajoutés, avec SHA GitHub vérifiés **identiques octet pour octet** aux fichiers exécutés :

- `numerics/hr_step67_true_center_taylor_certificate.py` — `d73e74089b9a2437aa6ba9cd011e5b4819dcb339`.
- `tests/test_hr_step67_true_center_taylor_certificate.py` — `681f667b3d1f3a066471efc89c43133dcc78ac12`.

Commande exécutée :

```bash
cd /mnt/data/janus-step67
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step67_true_center_taylor_certificate.py
# RÉELLEMENT EXÉCUTÉ : 16 PASSED in 3.20s

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step67_true_center_taylor_certificate > research/reports/gate2b-step67-local-manifest.json
```

Manifeste brut local SHA256 `aada56f82452eb67a5fc43c4808df0731cad6c8cfae3915c6ee6d77504b55cf3`, non téléversé séparément. Les chiffres essentiels, les bornes rationnelles, la provenance, les résultats et les commandes sont inscrits dans `research/reports/gate2b-step67b-original-center-u3-report.json`.

Les 16 tests comprennent la provenance fail-closed, le refus de racines invalides, la compatibilité des séries rationnelles tronquées avec multiplication/inversion/racine, les identités physiques à six couples, le certificat authentique sur 256 cellules, les anciens coefficients du centre et le nouveau \(U_3\), ainsi qu'un contrôle indépendant du facteur de récurrence \(9\). Il ne s'agit PAS d'une réexécution de la suite entière du dépôt ou des tests du Dirac temporel Step57–60. GitHub Actions restent désactivés.

## 5. Prochaine priorité : raccordement au Dirac temporel

La nouvelle base reconstituée fournit maintenant les véritables sources 45/46/55 et leur preuve globale de benchmark dans un même workspace. La prochaine étape consiste à :

1. Y ajouter les sources originales 57/58/59/60 **octet-authentiques**, et celles des bornes de dérivées physiques 63/64/65.
2. Calculer les quatre vrais coefficients du crochet temporel \(A_N,B_N,A_M,B_M\) avec \(z,z',z''\) cohérents, les contraintes radiales et leurs dérivées ; traiter le centre avec \(U_0,\ldots,U_3\).
3. Examiner le rang de l'opérateur et les lapses seulement lorsque ces réductions auront été faites ; vérifier indépendamment par l'action originale non-IBP à six couples, avec les bords.
4. Préserver la branche `main` et la branche `research/v2-flrw` inchangées et ne pas réactiver de workflows.

**Conclusion :** un nouveau coefficient du développement radial physique est rigoureusement encadré et la preuve Step55 est réellement reproduite à partir des sources originales. **Le rang de Dirac, la fixation des lapses, l'absence du fantôme de Boulware–Deser et la validation JANUS-R restent NON établis.**
