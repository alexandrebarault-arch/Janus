# JANUS — b3c3d6 : barrière physique robuste au défaut continu (30/10/2026)

**Résultat exact conditionnel ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Il ne s'agit ni d'un rejeu Step58 ni d'une borne effectivement mesurée du défaut DOP853.

## Provenance physique historique

Rapport Step63 authentifié, blob Git `8a6ff87fdde3efbf26fa81d20ddb2623c161c9c1`, 256 cellules continues sur `0<=s<=289/400`, `Ustar(s)±1/10000`, sources originales Step45 `66aa4384`, Step46 `bac025c2`, Step55 normalisé `a54a6acf`, barrière `a6e70041`. Le code Step55 original définit exactement `Fplus=G(s,Ustar+H)-2(Ustar+H)-2s Ustar'` et `Fminus=G(s,Ustar-H)-2(Ustar-H)-2s Ustar'`. Les marges archivées sont :

`Fplus <= -1480966474499367232302129/10^28 < 0` ;
`Fminus >= 295653233337826329055403/(2*10^27) > 0`.

Ces bornes proviennent de l'exécution **historique**, non reproduite ici.

## Nouveau certificat conditionnel utilisable sur le candidat numérique

Soit `v(s)` continue et C1 par morceaux, initialisée strictement dans le tube à `s_a=r_a²>0`, `0<r_a<r_b<=17/20`. Si le **défaut continu**, et non un échantillonnage, vérifie `|v_s-(G(s,v)-2v)/(2s)|<=D` sur chaque cellule, et si

`2*r_b²*D < min(-Fplus_max,Fminus_min)`,

alors `v(s)` reste strictement dans `Ustar(s)±1/10000` sur tout `[r_a²,r_b²]`. Preuve par premier contact : sur la frontière supérieure, `2s(v_s-Ustar')<=Fplus_max+2r_b²D<0`, impossible lors d'une première sortie vers le haut ; sur la frontière inférieure, `2s(v_s-Ustar')>=Fminus_min-2r_b²D>0`, impossible lors d'une première sortie vers le bas. Les discontinuités de dérivée aux raccords du dense output sont admises si `v` reste continue et C1 sur chaque cellule, avec contrôle des dérivées unilatérales.

Pour `r_b=17/20`, le **seuil rationnel exact strict** est :

`D < 295653233337826329055403/2890000000000000000000000000 ≈ 1.0230215686429977e-4`.

**Forme renforcée sans division par s :** si le résidu normalisé continu est directement certifié sous la forme `|2s*v_s-G(s,v)+2v|<=R`, il suffit de `R<295653233337826329055403/2000000000000000000000000000 ≈ 1.4782661666891316e-4`, sans hypothèse de borne uniforme sur `v_s-f` près du centre. La même preuve de premier contact s'applique. Ce seuil est historique/conditionnel et **aucun R physique n'a été mesuré**.\n\nC'est une borne suffisante, **pas** une valeur de défaut effectivement obtenue. Aux rayons inférieurs, remplacer `r_b` dans le seuil augmente la marge admissible. La barrière originale Step55 garantit séparément que la solution physique exacte reste dans ce tube ; une fois le candidat certifié de la sorte, la borne historique `G_U<-99/100` est applicable entre les deux et le pont d'erreur Step63 déjà publié devient utilisable **si** l'erreur initiale est bornée.

## Vérifications et limites

`PYTHONPATH=. python -m unittest discover -s tests -v` : **19 tests rationnels PASS, 0 FAIL** sur la copie locale isolée ; `python -m compileall -q numerics tests` : **PASS**. Tests non indépendants de l'archive, avec deux solutions jouets saturant la borne d'erreur, seuil strict, garde d'initialisation, et témoin de sortie lorsque le défaut est grand. Source et tests publiés séparément ; l'archive Step63 et les sources Step55 ont été **lues par le connecteur GitHub**, sans exécution physique cette session.

**Verrou concret :** aucun `D` continu pour le vrai dense output DOP853 Step55 n'a été calculé ou certifié, aucune erreur initiale certifiée, aucun vrai Step58 affine/cubique quatre rayons ni six coefficients A/B/E rejoués. Les valeurs historiques ne doivent pas être interprétées comme un certificat de la solution numérique actuelle. Prochaine étape : matérialiser les cinq originaux et le candidat corrigé, calculer `D` en enclosure continue et tester ce seuil ; ensuite six coefficients et BVP lapses positifs aux deux bords, Dirac/4D/stabilité/observables.
