# JANUS — Étape 64 : certification de \(P'''\) JUSQU'AU CENTRE sur la vraie branche radiale Step55

**23 octobre 2026 — branche `research/gate2b-nonhomothetic-transfer` seulement. Gate 2B OPEN, JANUS-R NOT VALIDATED.**

## Résultat nouveau

L'étape 63 a authentifié quatre fichiers physiques originaux (Steps45/46/55 et le vrai certificateur global `hr_step55_global_barrier.py`) et démontré par arithmétique d'intervalles à arrondi extérieur \(10^{-28}\) les bornes de \(G,G_s,G_U,G_{ss},G_{sU},G_{UU}\) sur les **256 cellules continues** du tube Step55. Elle a certifié \(P''\) sur l'intervalle radial total, mais **pas \(P'''\) dans la première cellule qui contient \(r=0\)**, à cause d'un quotient \((G-2U)/s\) dans la dérivation de l'EDO. Cette lacune vient d'être comblée sans diviser par zéro et sans simulation temporelle.

Nous considérons la **branche analytique régulière** déjà établie conditionnellement aux Steps49/55, avec \(s=r^2\), \(P=p_{L_f}=r^2U(s)\), \(U(0)=U_0\) et
\[
2sU_s=G(s,U)-2U,\qquad G(0,U)=3U_0-U.
\]
Cette dernière identité au centre provient du développement antérieur et est vérifiée à nouveau dans le vrai calcul par intervalles en \(s=0\) pour trois valeurs admissibles de \(U\). **Le présent audit ne remplace pas la preuve antérieure d'existence locale régulière** ; il la prend comme hypothèse exacte de départ.

Poser \(W=U-U_0\) et
\[
A(s,U)=\frac{G(s,U)-G(0,U)}s=\int_0^1G_s(ts,U)\,dt.
\]
Alors
\[
2sW_s+3W=sA(s,U(s)).
\]
La solution bornée au centre a nécessairement la représentation par facteur intégrant
\[
W(s)=\frac1{2s^{3/2}}\int_0^s t^{3/2}A(t,U(t))\,dt,\qquad s>0.
\]
Si \(|A|\le B\), il s'ensuit **sur tout le continuum**, et pas seulement aux points échantillonnés,
\[
\boxed{\left|\frac{W(s)}s\right|\le\frac B5,\qquad |U_s(s)|\le\frac{4B}{5}.}
\]
Ces estimations s'étendent au centre par continuité de la solution régulière.

## Le point de rigueur : une boîte U uniforme, pas le tube déplacé

Pour borner \(A(t,U(s))\), la valeur \(U(s)\) est maintenue fixe pendant que \(t\) parcourt \([0,s]\). Par conséquent, le tube mobile \(U_\star(t)\pm10^{-4}\) de Step55 **ne suffit pas**. Le calcul construit UNE SEULE enveloppe rationnelle \(U_{\rm all}\) de toutes les valeurs \(U_\star(s)\pm10^{-4}\) possibles pour \(0\le s\le289/400\), puis calcule \(\sup|G_s(t,u)|\) par le vrai AD géométrique de Step63, sur **toutes les 256 cellules \(t\)** et \(u\in U_{\rm all}\).

Le coefficient rationnel extérieur obtenu est
\[
B=\frac{21885092944341379217378943}{5000000000000000000000000000}
\approx 0.004377018589.
\]
Ceci entraîne \(|U_s|\le4B/5\approx0.003501615\) sur toute la branche régulière, centre inclus.

On revient alors à la véritable dérivée troisième du moment \(P\) par
\[
H=G+2sG_s+(G-2U)G_U,\quad
H_s=3G_s+2sG_{ss}+G_sG_U+(G-2U)G_{sU},
\]
\[
H_U=G_U^2-G_U+2sG_{sU}+(G-2U)G_{UU},\qquad
P'''=2r\,(H_s+H_UU_s).
\]
Le calcul par intervalles remplace maintenant **\(U_s\) par son encadrement uniforme fini**, au lieu de la division incorrecte de \((G-2U)\) par \(s\). Chaque \(\sqrt{s}=r\) est évalué avec des bornes rationnelles extérieures, y compris dans la cellule \(s\in[0,289/(400\cdot256)]\).

**CERTIFICAT NOUVEAU sur TOUT l'intervalle \(0\le r\le0.85\) :**
\[
\boxed{
-\frac{157117705762868039310811}{625000000000000000000000000}
\le P'''(r)\le
\frac{128641166369078726897489771}{5000000000000000000000000000}
}
\]
En bornes décimales volontairement élargies :
\[
\boxed{-0.000252<P'''(r)<0.025729\quad\text{sur tout }[0,0.85].}
\]
La première cellule, **centre compris**, possède l'encadrement exact \([0,\,16458628607489610074397529/10^{28}]\) (≈ \([0,0.001645862861]\)), cohérent avec \(P'''(0)=0\) sur la branche paire.

Ces bornes sont strictement plus serrées que les précédents encadrements intérieurs larges du Step63, et n'ont pas de trou au centre. Elles sont **conditionnelles à la branche radiale positive et régulièrement analytique Step49/55**, aux paramètres du benchmark original et à la validité déjà établie de son certificat de barrière. Ce sont des propriétés de données INITIALALES sphériques, non un théorème d'évolution en temps de la cosmologie.

## Provenance, tests et limites

Les QUATRE modules d'origine (Git SHA-1 byte-identiques) sont les mêmes que ceux du rapport Step63 :
`hr_step45_exact_physical_ward.py` `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ;
`hr_step46_exact_secondary_ode.py` `bac025c28dbe1561c0c36c56dbfda46dc326f804` ;
`hr_step55_normalized_secondary.py` `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862` ;
`hr_step55_global_barrier.py` `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.
Le Step62 analytique concurrent, notamment son certificat `0<=G_UU<0.674`, est conservé intact.

Nouveau module `numerics/hr_step64_center_third_jet.py` Git blob `07d80d70636952bcabf61bd8eb7da88cc8bc6c72` ; 12 nouveaux tests `tests/test_hr_step64_center_third_jet.py` Git blob `1db2c2c9cb7bad57cf2ffbb895b198ec61432d28`. **Les empreintes des deux sont vérifiées BYTE-IDENTIQUES aux fichiers exécutés localement.**

```bash
cd /mnt/data/janus-step62
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step64_center_third_jet.py tests/test_hr_step62_original_interval_ad.py
# RÉEL : 27 PASSED en 23.56 s = 12 nouveaux Step64 et 15 Step63.

OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step64_center_third_jet 256 > research/reports/gate2b-step64-center-full-Pthird.json
# SHA256 du brut local: 19bc8c6633714e99582e0f41a3e3a88782d0edccd479e537f7a3ee27554cc7f3
```

Les 12 nouveaux tests incluent : enveloppe uniforme de tous les 257 points de contrôle couvrant les tubes mobiles, borne globale sur \(G_s\), identité symbolique indépendante du facteur intégrant, compatibilité centrale réelle de \(G(0,U)\), cellule centrale contenant zéro, borne totale \(-0.000252,0.025729\), comparaison au Step63, et **contrôle négatif** montrant pourquoi la bande mobile \(U_\star(t)\pm\delta\) ne suffit pas lorsqu'on intègre à \(U(s)\) fixe. Il ne s'agit pas d'un recalcul complet du Dirac temporel ou de tous les tests historiques.

La sortie brute locale a été générée ; sa partie scientifique et ses fractions EXACTES sont archivées dans `research/reports/gate2b-step64-center-full-third-report.json`. Le fichier brut n'a pas été uploadé séparément sur GitHub.

**PROCHAINE ÉTAPE 65 :** reconstituer les vraies sources physiques six-couples Steps57–60 avec le profil exact positif Step55, substituer les jets \(P'',P'''\) désormais encadrés globalement, corriger la substitution des jets du déplacement \(z,z',z''\) (Step61), réduire les quatre coefficients de lapses \(N,N',M,M'\) et déterminer la structure/rang du crochet temporel. Construire un oracle original indépendant NON-IBP avec les conditions de bord. **L'absence du fantôme BD, la fixation des lapses et la validité dynamique 4D sont TOUJOURS NON ÉTABLIES. GATE_2B OPEN ; JANUS-R NOT_VALIDATED.**
