# JANUS — Étape 62 : vraie secondaire physique, courbure quadratique et certificat global sur le tube Step55

**23 octobre 2026. Branche : research/gate2b-nonhomothetic-transfer uniquement.** Gate 2B **OUVERT** ; JANUS-R **NON VALIDÉ**. Ce résultat concerne les données initiales contraintes sphériques, pas la préservation temporelle complète ni l'absence du fantôme de Boulware–Deser.

## 1. Retour au G physique et provenance vérifiée

Nous avons effectivement reconstruit, importé ET comparé en octets avec GitHub les trois fichiers originaux :

| Source réelle | Blob Git SHA-1 |
|---|---|
| numerics/hr_step45_exact_physical_ward.py | 66aa43841dccfe4a5d586a49be9c10af3a67a10e |
| numerics/hr_step46_exact_secondary_ode.py | bac025c28dbe1561c0c36c56dbfda46dc326f804 |
| numerics/hr_step55_normalized_secondary.py | a54a6acf2f7ad2f64c500faecfa1406ecbf7b862 |

La fonction normalized_symbolic() du véritable Step55 a été exécutée ; elle repose sur l'action positive-EH Hassan–Rosen sphérique, **six couples canoniques et deux poussières mobiles**. L'expression originale G(s,U) a 1 048 opérations SymPy et n'est PAS un noyau inventé. Le nouveau code refuse tout changement d'une des trois empreintes.

**Restriction de provenance :** les valeurs numériques des métriques et phases utilisées pour le certificat d'intervalle ont été retranscrites **exactement en nombres rationnels** depuis le code historique hr_step55_global_barrier.py consulté sur GitHub ; ce quatrième fichier n'a pas encore été copié et authentifié octet pour octet dans l'environnement Step62. Les tests du G physique, eux, importent réellement les trois sources historiques ci-dessus.

## 2. Nouvelle identité algébrique EXACTE

La normalisation radiale physique des étapes 45–55 est :

\[
s=r^2,\quad P=p_{L_f}=r^2U(s),\quad
2sU_s=G(s,U)-2U,\quad P'/r=G(s,U).
\]

La véritable expression de la secondaire livre symboliquement :

\[
\boxed{\deg_U G=2,\qquad G_{UUU}=0,\qquad G_{UU}(0,U)=0.}
\]

Écrire l=L_f0, g=L_g0, t=t_f0, h=\sqrt{1-sz_1^2}, μ_f=M_f², ainsi que

\[
A_t=l^2\beta_3+2lg\beta_2+g^2\beta_1,
\]
\[
T=(3l^2\beta_3+2lg\beta_2-g^2\beta_1)h
+4lg\beta_2+4g^2\beta_1.
\]

Alors l'expression calculée à partir de la véritable fonction G est

\[
\boxed{G_{UU}(s,U)=
-\frac{s\,t\,T}{2l\,\mu_f\,\sqrt{l^2+st^2}\,h\,A_t}.}
\]

La différence entre cette forme compacte et la dérivée seconde de l'expression originale complète est **exactement zéro dans SymPy**. En outre \(G_U(0,U)=-S_{fr0}/L_{f0}\), soit -1 au centre pour le profil original prescrit. Le signe de cette courbure change lorsque l'on inverse seulement la pente de phase de la poussière f, toutes les autres variables étant fixées.

## 3. Certificat rationnel sur l'ENTIER intervalle radial

Paramètres décimaux interprétés exactement en Fraction du benchmark Step55 :

\[
a=0.4,\quad y=0.5787707228025044,\quad
g=a(1+0.0015s)^2,\quad l=ay(1-0.0012s)^2,
\]
\[
t=-0.0016l,\quad z_1=0.004,\quad \mu_f=(0.10879548725)^2,
\]
\[
\beta_1=1,\quad\beta_2=-4.2383993109,\quad
\beta_3=13.6801214252.
\]

Pour tout \(s\in[0,289/400]\), les racines sont enveloppées par des rationnels dont les inégalités se prouvent en élevant au carré :

\[
99999/100000\le\sqrt{1-s(0.004)^2}\le1,
\]
\[
1\le\sqrt{1+s(0.0016)^2}\le100001/100000.
\]

L'arithmétique des intervalles **exclusivement en fractions exactes** prouve simultanément \(A_t>0\), \(T>0\), l'absence de zéro dans le dénominateur, puis

\[
\boxed{\forall(s,U),\ 0\le s\le289/400:\quad
0\le G_{UU}(s,U)<337/500=0.674.}
\]

Pour \(s>0\), la borne inférieure est strictement positive. L'encadrement calculé possède une borne supérieure d'environ 0.6736978758 ; cette valeur décimale n'intervient PAS dans la preuve. Les fractions exactes de tous les encadrements sont disponibles dans le rapport machine gate2b-step62-report.json et le code exécutable.

**Ces propriétés ne sont démontrées que pour le profil radial fixe de référence**, pas pour une autre branche ou une autre cosmologie.

## 4. Reste de Taylor certifié sur la véritable solution Step55

L'étape 55 a démontré sur cette branche continue exactement contrainte \(|U-U_\star|\le1/10000\). Comme G est exactement quadratique, pour chaque s la formule de Taylor est **une égalité**, non une approximation :

\[
G(s,U)-G(s,U_\star)-G_U(s,U_\star)(U-U_\star)
=\tfrac12G_{UU}(s)(U-U_\star)^2.
\]

Il en découle rigoureusement, sur tout l'intervalle radial :

\[
\boxed{|G_U(s,U)-G_U(s,U_\star)|<337/5\,000\,000
=6.74\times10^{-5},}
\]

\[
\boxed{|G(s,U)-G(s,U_\star)-G_U(s,U_\star)(U-U_\star)|
<337/100\,000\,000\,000=3.37\times10^{-9}.}
\]

Ces inégalités ne bornent pas automatiquement les dérivées **totales** en s, ni \(P''\), \(P'''\), ni les coefficients du système temporel des lapses.

## 5. Code, tests, audit et provenance

- numerics/hr_step62_physical_G_curvature.py — blob Git **d2040a4bde9672933eac9bbab91b792005227f40**.
- tests/test_hr_step62_physical_G_curvature.py — blob Git **b8e432ff4afe4a53b7d54150f174706a5b65460b**.
- **17 / 17 tests réussis**, dernière exécution locale : 2,57 secondes.
- Les DEUX nouveaux fichiers ont été confirmés sur GitHub avec des empreintes **identiques aux fichiers réellement exécutés**.
- Workspace ciblé : /mnt/data/janus-step62 ; commande de reprise : OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step62_physical_G_curvature.py
- Manifeste brut créé localement, SHA256 **2e99f43bda32edbbf47380d1806f913a99fca2203de21da8de63174bd0ccb814**, non téléversé séparément. Rapport machine durable : research/reports/gate2b-step62-report.json.
- Contrairement à Step61, le G physique ORIGINAL est réellement importé ici ; toutefois Steps57–61 n'ont pas été rejouées ensemble dans cet environnement réduit. Aucune suite complète ni GitHub Actions n'a été lancée.

## 6. Étape 63 — problème majeur TOUJOURS ouvert

Importer aussi en octets vérifiés le véritable fichier de géométrie et de certificat Step55. Construire les dérivées totales de G lorsque **toutes les données primaires dépendent de s**, puis certifier par intervalles \(G_s,G_U,G_{ss},G_{sU}\) et les limites au centre. En déduire \(P''\) et \(P'''\) sur la vraie solution de l'EDO. Seulement alors réduire sur cette solution les quatre coefficients du véritable crochet temporel Step60, incluant les substitutions \(z=Z,z'=Z_1,z''=Z_2\), et étudier la préservation temporelle, les multiplicateurs, leurs conditions de bord et le rang de Dirac. Comparer à un oracle indépendant original non-IBP. Traiter K=0/J=0 à part.

**VERDICT : progrès physique exact, certificat global positif de G_UU et erreur de Taylor contrôlée. FULL DIRAC, FIXATION DES LAPSES, RANG ET ABSENCE DU FANTÔME BD PAS ÉTABLIS. GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**
