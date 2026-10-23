# JANUS — Étape 65 : monotonie EXACTE de la courbure du véritable \(G(s,U)\) et meilleure borne globale

**23 octobre 2026 — branche scientifique :** `research/gate2b-nonhomothetic-transfer` uniquement. **Gate 2B OUVERT ; JANUS-R NON VALIDÉ.** Cette avancée concerne exclusivement la solution radiale initiale benchmark ; elle ne résout pas le système temporel complet des lapses.

## Origine : véritable équation physique, source Git authentifiée

La fonction \(G(s,U)\) est réellement importée de l'équation secondaire à six couples canoniques de la formulation sphérique Hassan–Rosen, deux poussières mobiles et deux actions Einstein–Hilbert de signe positif. Les modules physiques originaux sont byte-identical aux blobs GitHub, et leur identité est vérifiée à l'exécution :

| Fichier original | SHA Git |
|---|---|
| `numerics/hr_step45_exact_physical_ward.py` | `66aa43841dccfe4a5d586a49be9c10af3a67a10e` |
| `numerics/hr_step46_exact_secondary_ode.py` | `bac025c28dbe1561c0c36c56dbfda46dc326f804` |
| `numerics/hr_step55_normalized_secondary.py` | `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` |

La preuve analytique Step62 déjà publiée, `numerics/hr_step62_physical_G_curvature.py` (Git `d2040a4bde9672933eac9bbab91b792005227f40`), a établi à partir de ces vrais modules que \(G\) est **quadratique en \(U\)**, \(G_{UUU}=0\), et que \(G_{UU}\) est indépendant de \(U\). Elle avait certifié \(0\le G_{UU}<337/500\) pour tout \(s\in[0,289/400]\) sur les paramètres du benchmark.

L'étape 65 va plus loin : prouver **le signe strict de la dérivée radiale \(G_{sUU}\)** sur TOUT l'intervalle continu, et en déduire une borne plus serrée, obtenue à une seule extrémité.

Le calcul prend les paramètres du benchmark à leurs **valeurs rationnelles décimales exactes**, transcrites de `hr_step55_global_barrier.py` : \(L_g(s)=a(1+c_gs)^2\), \(L_f(s)=b(1+c_fs)^2\), \(t'_f=k_fL_f\), \(z(r)=z_1r\), \(a=0.4\), \(b=0.4\times0.5787707228025044\), \(c_g=0.0015\), \(c_f=-0.0012\), \(k_f=-0.0016\), \(z_1=0.004\), \(M_f^2=0.10879548725^2\), \((\beta_1,\beta_2,\beta_3)=(1,-4.2383993109,13.6801214252)\). **Limite de provenance :** `hr_step55_global_barrier.py` a été consulté sur GitHub mais **n'est pas importé octet pour octet dans ce nouveau worktree** ; cette transcription de géométrie est contrôlable dans le code.

## Théorème exact : croissance stricte sur toute la branche

Par l'identité symbolique authentique du Step62, sur la branche stationnaire régulière \(K>0\),

\[
G_{UU}(s,U)=s\,F(s),\qquad
F(s)=-\frac{k_f\,T(s)}
 {2L_f(s)M_f^2\sqrt{1-z_1^2s}\sqrt{1+k_f^2s}\,A_t(s)}
\]

où

\[
A_t=\beta_3L_f^2+2\beta_2L_fL_g+\beta_1L_g^2,
\]

\[
T=(3\beta_3L_f^2+2\beta_2L_fL_g-\beta_1L_g^2)\sqrt{1-z_1^2s}
  +4\beta_2L_fL_g+4\beta_1L_g^2.
\]

Les intervalles rationnels de la preuve garantissent \(L_f>0\), \(A_t>0\), \(T>0\), \(k_f<0\) sur tout le continuum \(0\le s\le289/400\), d'où \(F>0\).

Le calcul logarithmique exact donne

\[
\frac{F'}{F}
=\frac{T'}T-\frac{L_f'}{L_f}
-\frac{(\sqrt{1-z_1^2s})'}{\sqrt{1-z_1^2s}}
-\frac{(\sqrt{1+k_f^2s})'}{\sqrt{1+k_f^2s}}
-\frac{A_t'}{A_t}.
\]

Chaque ratio est encadré par **arithmétique d'intervalles à bornes Fraction exactes** sur UN SEUL intervalle total, avec les racines entourées par des fractions décimales dont les puissances secondes sont vérifiées exactement. Aucune hypothèse de monotonie n'est introduite dans l'évaluation de \(F'/F\) ; son signe résulte des inégalités de fractions.

Le quotient \(F'/F\) est strictement positif sur le continuum, et

\[
\boxed{\frac45<G_{sUU}(s,U)=F(s)\Bigl(1+s\frac{F'}F\Bigr)<1}
\]

pour **chaque \(s\in[0,289/400]\), indépendamment de \(U\)**, sur ces seuls paramètres benchmark.

En bornes décimales illustratives (les bornes exactes sont dans le code/rapport régénérable) :

\[
0.8239432487\ldots <G_{sUU}<0.9353760452\ldots .
\]

Ainsi \(G_{UU}\) est **strictement croissante** de sa valeur \(G_{UU}(0)=0\) jusqu'au bord du benchmark.

## Nouvelle borne maximale globale, plus serrée que Step62

Comme la monotonie est prouvée, on peut évaluer \(G_{UU}\) à **l'unique extrémité \(s=289/400\)**, avec encadrement extérieur rationnel des deux radicaux à \(10^{-14}\) (racines positives, carrés exacts). Résultat :

\[
0.6338791317425377\ldots
<G_{UU}(289/400,U)
<0.6338791317425752\ldots.
\]

D'où le **nouveau certificat continu global** :

\[
\boxed{0\le G_{UU}(s,U)<\frac{317}{500}=0.634,\quad
          0\le s\le289/400.}
\]

Cela améliore strictement le certificat de l'étape 62 \(G_{UU}<337/500=0.674\). Le changement du signe de la pente de phase de la poussière \(f\), à géométrie fixée, inverse le signe de \(G_{UU}\) : la présente monotonie **n'est PAS une propriété universelle de toute la théorie Hassan–Rosen**, mais un théorème de la famille initiale prescrite.

Pour le tube exact Step55 \(|U-U_\star|\le1/10000\), la dépendance strictement quadratique en \(U\) donne, globalement,

\[
\boxed{|G_U(s,U)-G_U(s,U_\star)|<
\frac{317}{5\,000\,000}=0.0000634}
\]

et, par l'identité de Taylor **exacte** d'un polynôme de degré deux,

\[
\boxed{
|G(s,U)-G(s,U_\star)-G_U(s,U_\star)(U-U_\star)|
<\frac{317}{100\,000\,000\,000}
=3.17\times10^{-9}.
}
\]

La précédente borne sur ce reste était \(3.37\times10^{-9}\). Ces quantités constituent des certificats robustes de sensibilité spatiale de l'EDO, **pas** des valeurs de lapses ou de stabilité cosmologique.

## Tests réellement exécutés et source reprise

Nouveaux fichiers :

- `numerics/hr_step65_monotone_physical_curvature.py` — Git blob `046a58e5c118ac269fc68d4020e1d192349dc28f`.
- `tests/test_hr_step65_monotone_physical_curvature.py` — Git blob `e4d1d002f8d5176cda1057dc194e744a6518bd6d`.

Les deux nouveaux fichiers sont **byte-identical** aux octets locaux réellement exécutés ; les quatre valeurs Git ci-dessus sont consultées avec le connecteur officiel GitHub. L'environnement local est `/mnt/data/janus-step62`, contenant les originaux Steps45/46/55 ainsi que le module Step62 authentique.

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
 tests/test_hr_step62_physical_G_curvature.py \
 tests/test_hr_step65_monotone_physical_curvature.py
# RÉELLEMENT EXÉCUTÉ : 32 PASSED in 2.88 s (17 Step62 + 15 NOUVEAUX Step65).

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step65_monotone_physical_curvature \
 > research/reports/gate2b-step65-local-manifest.json
```

Le manifeste brut a été généré LOCALLEMENT et contient les fractions exactes parfois longues. SHA-256 : `a9969377a56936b960a987c8b3d8e6958d9ef64e2c528c486ed650e009e6b7d3`. **Ce fichier brut n'est pas uploadé séparément** ; les résultats, la provenance, les SHA et la commande sont archivés dans `research/reports/gate2b-step65-report.json`. Les tests Step63/64, 57–61, le dépôt complet et GitHub Actions N'ONT PAS été réexécutés dans ce worktree.

Les nouveaux tests comportent les contrôles de mauvais radical, d'emploi de la certification hors de \(s\in[0,289/400]\), et de changement de signe de pente de phase \(f\). Le domaine accepté par le programme est explicitement bloqué à la vraie charte du benchmark.

## Verrou restant — Étape 66

**Le travail de réduction temporelle à six couples n'est toujours pas accompli.** Il faut importer dans UN SEUL worktree authentifié l'ensemble historique Steps45/46/55/57/58/59/60 et les outils AD à géométrie totale Steps63–64. Utiliser les valeurs cohérentes de \(P'',P'''\) certifiées jusqu'au centre par Step64, \(z=Z(D_g,K)\), \(z'=Z_1\) et \(z''=Z_2\) avec la correction cohérente Step61, puis évaluer et réduire les quatre vrais coefficients \(A_N,B_N,A_M,B_M\) sur la solution exactement contrainte Step55.

Ensuite seulement calculer le rang du système différentiel de lapses, ses conditions de bord et ses secteurs exceptionnels \(K=0,J=0\), et valider le crochet temporel par un **oracle indépendant non-IBP à six couples**. Le gain de borne sur \(G_{UU}\) n'est pas une preuve de l'absence du fantôme Boulware–Deser ni de l'évolution nonhomothétique 4D.

**État final :** borne globale physique améliorée, monotonie exacte démontrée, 32 tests ciblés passés, vrais auteurs des équations authentifiés. **GATE_2B OPEN ; JANUS-R NOT VALIDATED.**
