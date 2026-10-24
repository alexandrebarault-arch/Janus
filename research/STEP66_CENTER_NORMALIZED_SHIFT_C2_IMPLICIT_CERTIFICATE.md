# JANUS — Étape 66 : inversibilité de l'équation du déplacement relatif, NORMALISÉE jusqu'au centre

**24 octobre 2026 — branche scientifique exclusive :** `research/gate2b-nonhomothetic-transfer`. **GATE 2B OUVERT ; JANUS-R NON VALIDÉ.** Cette étape fournit une nouvelle preuve analytique locale-uniforme de conditionnement du déplacement relatif sur le **benchmark initial radial fixé de Step55**. Elle ne calcule PAS l'évolution temporelle de la secondaire ni le rang des contraintes de Dirac.

## 1. Données physiques et portée véritable des sources

On repart de l'équation originale du déplacement relatif dans la formulation sphérique Hassan–Rosen à deux poussières et deux termes Einstein–Hilbert positifs (action physique Step45, six couples canoniques) :

\[
F_z = D_g-\frac{Kz}{\sqrt{1-z^2}}=0.
\]

Les résultats antérieurs Steps54–55, déjà audités sur l'action originale, établissent sur la branche analytique positive et prescrite, \(0\le r\le17/20\), des signes stricts et la parité radiale

\[
D_g=r^3d(s),\quad K=r^2k(s),\quad k(s)>\frac{229}{1000},\quad
z=r\,w(s),\quad w(s)=\frac1{250},\quad s=r^2.
\]

L'inégalité \(k>229/1000\) est celle du **certificat antérieur** dans `research/reports/gate2b-step55-report.json` (associé au rapport Step54). L'existence de la branche analytique régulière et le prolongement positif de \(k\) au centre sont des **hypothèses externes déjà certifiées**, pas redémontrées ici.

**Provenance honnête :** les sources originales Steps45/55 ont été consultées sur GitHub et leurs assertions de Step55 ont été utilisées comme hypothèses. Le nouveau module Step66 est un calcul mathématique autonome ; il **n'importe pas** l'original Step45/55 ni ne rejoue leur calcul d'intervalles. Cette distinction est explicitement codée dans le manifeste et testée. Les preuves nouvelles sont les identités algébriques et les bornes en fractions rationnelles ci-dessous, *conditionnelles* au benchmark certifié.

## 2. Une équation régulière là où l'équation non normalisée dégénère

Pour \(r>0\), la division par \(r^3\) donne exactement

\[
\boxed{
\widehat F_z(s,d,k,w)
=d-\frac{k w}{\sqrt{1-sw^2}}=0.
}
\]

Cette expression se prolonge analytiquement à \(s=0\) lorsque \(k>0\). Sur la branche positive, sa racine unique est

\[
\boxed{w(d,k;s)=\frac{d}{\sqrt{k^2+s d^2}}.}
\]

Le calcul exact donne

\[
\boxed{\partial_w\widehat F_z
=-\frac{k}{(1-sw^2)^{3/2}}.}
\]

Sur \(0\le s\le289/400\), \(w=1/250\), le facteur \(t=1-sw^2\) satisfait

\[
\boxed{
\frac{24999711}{25000000}\le t\le1.
}
\]

Il en découle, **en tout point et jusqu'au centre compris**,

\[
\boxed{|\partial_w\widehat F_z|>\frac{229}{1000}.}
\]

L'inversion implicite **normalisée** reste donc uniforme à \(s=0\) sur cette branche. Il ne faut pas affirmer que l'Hessienne brute \(\partial_zF_z\) serait non nulle au centre : elle est proportionnelle à \(r^2\), et la variable \(w=z/r\), avec la densité normalisée \(F_z/r^3\), est précisément ce qui élimine cette singularité apparente dans la classe de perturbations radiales respectant la parité.

## 3. Résultat nouveau : toutes les dérivées premières et SECONDES de la racine sont contrôlées

En posant \(t=1-sw^2\), on dérive EXACTEMENT :

\[
\boxed{
w_d=\frac{t^{3/2}}k,\qquad
w_k=-\frac{w\,t}{k}.
}
\]

La matrice Hessienne complète (avec \(s\) fixé) est :

\[
\boxed{\begin{aligned}
w_{dd}&=-\frac{3sw\,t^2}{k^2},\\
w_{dk}=w_{kd}&=\frac{(3sw^2-1)t^{3/2}}{k^2},\\
w_{kk}&=\frac{w(2-3sw^2)t}{k^2}.
\end{aligned}}
\]

Ces identités sont obtenues de la racine explicite et testées indépendamment contre les dérivées directes de \(d/\sqrt{k^2+s d^2}\). La symétrie de Hessienne est également testée.

Grâce aux bornes strictes \(k>229/1000\), \(w=1/250\), \(0\le s\le289/400\), toutes les comparaisons suivantes utilisent exclusivement des **fractions exactes** sur l'intervalle continu complet :

\[
\boxed{\begin{aligned}
|w_d|&<\frac{22}{5},&
|w_k|&<\frac1{50},\\
|w_{dd}|&<\frac15,&
|w_{dk}|&<20,&
|w_{kk}|&<\frac15.
\end{aligned}}
\]

Les majorants rationnels intermédiaires avant simplification sont \(1000/229\), \(4/229\), \(8670/52441\), \(1000000/52441\) et \(8000/52441\) respectivement. **Ces majorations sont uniformes en \(r\) au long de la branche de données initiales Step55, et concernent les dérivées au niveau des données physiques** ; elles ne sont PAS un certificat d'une grande boule arbitraire de perturbations hors de la branche.

Au centre \(s=0\), les limites exactes restent finies :

\[
(w_d,w_k,w_{dd},w_{dk},w_{kk})
=\left(\frac1k,-\frac wk,0,-\frac1{k^2},\frac{2w}{k^2}\right).
\]

## 4. Réponse fonctionnelle du déplacement compatible avec la parité

Pour une variation initiale respectant \(D_g=r^3 d\), \(K=r^2k\), \(z=rw\), la réponse implicite se réduit à

\[
\boxed{
\delta\!\left(\frac zr\right)
=\frac{t^{3/2}}k\,\delta d
-\frac{wt}k\,\delta k,\qquad
\delta z=r\,\delta w.
}
\]

Le coefficient en \(1/r^2\) de l'inversion non normalisée est donc compensé par les puissances radiales des variations admissibles. On obtient à chaque rayon du benchmark, pour la variation linéarisée,

\[
\boxed{
|\delta(z/r)|\le
\frac{1000}{229}\left(|\delta d|+\frac1{250}|\delta k|\right).
}
\]

Ce résultat renforce l'audit Step56 sur la sensibilité du déplacement relatif : **le conditionnement est maintenant vérifié jusqu'à l'ordre deux** dans les variables normalisées, y compris au centre. La charte \(K=0\) n'est PAS incluse : lorsque \(k=0\), la dérivée \(\partial_w\widehat F_z\) s'annule et l'argument de fonction implicite ne s'applique plus.

## 5. Tests, code exact, contrôle des limites et reprise

Nouveau programme : `numerics/hr_step66_center_shift_implicit_condition.py`, Git blob **`47231c568a7a08954dc3894c82552552da58fde5`**.

Nouveaux tests : `tests/test_hr_step66_center_shift_implicit_condition.py`, Git blob **`274837f216d3399540a3eb96e5836cb9d721add4`**.

Les DEUX empreintes correspondent octet pour octet aux fichiers réellement exécutés localement et ont été vérifiées par le connecteur GitHub. Exécution réellement effectuée :

```bash
cd /mnt/data/janus-step66
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q \
 tests/test_hr_step66_center_shift_implicit_condition.py
# 20 PASSED in 2.36s

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. \
 python -m numerics.hr_step66_center_shift_implicit_condition \
 > research/reports/gate2b-step66-local-manifest.json
```

SHA256 du manifeste brut local : `08ec605aea6ad09e9aa55b03c8ebcc832c970b80b702d47123d5885380b8bf19`. Il n'a PAS été téléversé comme fichier autonome ; le rapport machine `research/reports/gate2b-step66-report.json` et le programme permettant de le régénérer le sont. Des tests négatifs interdisent de réutiliser les conclusions si l'intervalle radial, la borne positive de \(k\) ou \(w\) ne sont pas ceux du benchmark ; ils vérifient aussi la perte d'inversibilité dans la charte \(k=0\). Il n'y a eu ni réexécution de la suite historique complète ni activation de CI/Actions.

## 6. Verrou dur restant — Étape 67

L'étape 66 **ne prétend pas avoir exécuté** la réduction temporelle complète. La prochaine étape doit impérativement reconstituer dans un environnement cohérent les **vrais** modules Steps45/46/55/57/58/59/60 et Steps63–65, authentifiés octet par octet. Puis imposer simultanément les jets contraints \(P',P'',P'''\), la racine du déplacement et ses dérivées \(z,z',z''\), les contraintes et leurs prolongations, en utilisant le conditionnement régulier de \(w=z/r\) fourni ici près du centre.

Seulement alors on pourra évaluer les quatre coefficients \(A_N,B_N,A_M,B_M\) de la préservation temporelle, vérifier les conditions de bord, analyser le rang des multiplicateurs et tester l'oracle Poisson indépendant **non intégré par parties** sur les SIX couples. Les chartes \(K=0\), \(J=0\) doivent être traitées séparément.

**CONCLUSION :** inversibilité et Hessienne de la racine relative normalisée certifiées en fractions exactes sur tout le benchmark radiale, avec 20 nouveaux tests. **Dirac temporel complet, fixation des lapses, fantôme BD et évolution cosmologique 4D restent OUVERTS ; GATE_2B OPEN — JANUS-R NOT VALIDATED.**
