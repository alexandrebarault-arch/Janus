# JANUS b3c3d6 — récupération corrélée du résidu Step55 de Taylor (31 octobre 2026)

**Portée : quatre rayons exacts seulement, certificat rationnel dérivé d'une archive physique antérieure.** État inchangé : `GATE_2B OPEN` ; `JANUS_R NOT_VALIDATED`.

## Résultat et démonstration

L'archive physique Step55 `research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json`, blob Git `e74057dcf741bcdb655c7d9be48c6a9650d7ff3f`, donne à chaque rayon `s=r²` les bornes sortantes `glo<=G(s,Ustar+δ)` et `G(s,Ustar−δ)<=ghi`, avec `δ=1/10000`, et une borne de dérivée `G_U<=gu_hi<0` sur tout le tube. **Il est indispensable que les deux évaluations soient réellement celles des extrémités monotones**, comme le précise le code physique original `numerics/hr_b3c3d6_monotone_physical_four_radii.py` (blob `c68eba7cf5eba4679c437b8d6c82d00455e2dbfa`).

Par le théorème des accroissements finis, sans échantillonnage :
`glo−gu_hi*δ <= G(s,Ustar) <= ghi+gu_hi*δ`.
Ce rétrécissement exploite la corrélation des deux extrémités avec le **même** `Ustar`. On reconstruit indépendamment `U0` par encadrement entier exact de la racine carrée, puis `Vstar=2U0+4U1*s+6U2*s²` ; `Rstar=G(s,Ustar)−Vstar`.

Le calcul `fractions.Fraction` vérifie aux quatre vrais rayons `r=1/4,1/2,7/10,17/20` : **`|Rstar|<s/4000000`**, soit respectivement `1/64000000`, `1/16000000`, `49/400000000`, `289/1600000000`. La largeur de l'enclosure `G(s,Ustar)` est réduite de **plus de 900 fois** par rapport à l'ancienne boîte `G_monotone` pour chacun des quatre rayons. Les bornes exactes sont dans le rapport JSON et recalculables par le module.

## Ce qui n'est pas démontré

**Aucun signe de `Rstar` n'est fixé** : les quatre boîtes contiennent zéro. Il s'agit du résidu du polynôme de Taylor de référence, **pas** du défaut d'une intégration DOP853 ni de l'erreur `U−Ustar`. Quatre points ne donnent **aucune borne continue** entre ces points et ne prouvent pas une barrière plus fine. Aucune enclosure des six coefficients Step58 `A_N,A_M,B_N,B_M,E_N,E_M`, aucune factorisation des `B/E`, aucun BVP de lapses strictement positifs à deux vrais bords, aucun résultat Dirac/4D/stabilité/observables. Aucun moteur physique original Step45/46/55/58 ni DOP853 rejoué dans cette session.

## Provenance, tests et prochaine étape

À la reprise, HEAD GitHub `c235176a63fb5cc13ed6e61183bea6bc0cfad161`. Archive physique complète de 4 640 octets reconstruite localement et SHA Git **identique** à l'archive publiée. Source nouvelle `numerics/hr_b3c3d6_step55_taylor_residual_endpoint_recovery.py` blob `4e86b446a017178b5b4062e81b7b92c90328e543` ; tests `tests/test_hr_b3c3d6_step55_taylor_residual_endpoint_recovery.py` blob `582cb9afdd5ab03bf33a5f52d9b7b6190198c528` ; rapport `research/reports/gate2b-b3c3d6-step55-taylor-residual-endpoint-recovery.json` blob `5f846ef72b6341ee5c544d2a48e3b9dd8228b968`. Les trois blobs publiés sont **identiques aux octets locaux exécutés**. **7 unittest PASS, 0 FAIL, 0 SKIP** ; `python -m compileall -q numerics tests` PASS ; module de certificat exécuté PASS.

**Prochaine étape effective inchangée** : exécuter et encloser le vrai Step58 original aux quatre rayons à partir des jets Step55 authentifiés, factoriser exactement les annulations B/E, affiner le résidu continu DOP853 sur le tube si nécessaire, résoudre ensuite le BVP positif aux deux vrais bords, puis Dirac/4D/stabilité/observables. Une future barrière Step55 plus étroite doit être prouvée sur **tout l'intervalle**, pas extrapolée de ce certificat ponctuel.
