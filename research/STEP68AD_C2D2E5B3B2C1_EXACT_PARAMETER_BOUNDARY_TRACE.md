# JANUS — 68ad-C2d2e5b3b2c1 : trace extérieure exacte de la famille paramétrique P_g (27 octobre 2026)

**Résultat partiel, conditionnel à la reconstruction spatiale Step55 ; aucune condition aux limites physique n'est présumée. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources authentifiées
Lecture directe sur la branche de recherche des sources originales Step45 (blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`), Step46 (`bac025c28dbe1561c0c36c56dbfda46dc326f804`), Step49 (`d570948912885d45a625fa2db31c6a5435b6a654`) et Step55 barrier (`a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`). Le moteur original `G(s,U,P_g)` et la certification de barrière Step55 **n'ont pas été réexécutés**.

## Théorème exact de trace, pour la famille spécifique Step55
La reconstruction g prescrit `pLg(r;P_g)=r² P_g (1+(5/2)c_g r²)`, avec `c_g=0.0015`, géométrie et shift inchangés. Pour `P_g→P_g+lambda` et `R=17/20`, les traces exactes sont :

- `∂lambda pLg(R)=R²(1+(5/2)c_g R²)=92730563/128000000=0.7244575234375>0`.
- `∂lambda pLg'(R)=2R(1+5c_g R²)=2734739/1600000=1.709211875>0`.
- Au centre, la relation Step49 `U0=Mf² b(P_g/(Mg² a)−2z1)` donne `∂lambda U0=Mf² b/(Mg² a)=274023815147385251710689588080861/40000000000000000000000000000000000>0`.

Il s'agit d'identités rationnelles exactes (pas d'approximation par différences finies). **Si** le problème physique fixe la valeur extérieure de `pLg(R)`, ou celle de `pLg'(R)`, **ou** impose `U0` constant au centre, alors **aucun lambda non nul n'est admissible dans cette famille uniparamétrique**. Cela ne signifie pas qu'aucune autre direction tangentielle ne puisse satisfaire ces conditions : des perturbations compensatrices sont possibles. De plus, ni ces conditions ni leur combinaison ne sont imposées par les sources consultées comme conditions aux limites physiques définitives. Une condition mixte pourrait annihiler la trace de cette direction. L'obstruction est donc **conditionnelle au choix des bords**, pas un no-go JANUS.

La reconstruction g Step55 implique exactement `pSg*Sgr=r(s Dbar+Lg Gprime−s rho kg Lg)`, `pLg'=r Gprime`, `pg=s rho`, `tg'=r kg Lg`, d'où `Dg=pSg*Sgr−Lg pLg'+pg tg'=r³ Dbar` pour toute valeur de `P_g` dans la famille algébrique. Cette identité a été vérifiée rationnellement sur quatre témoins ; elle ne prouve pas la résolution de l'EDO f.

## Exécution réelle et limites
Programme Python standard-library exécuté depuis un environnement isolé, puis **11 tests unittest PASS, 0 FAIL** en exécution depuis la racine d'un paquet `numerics/` et `tests/` ; commande `python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c1_boundary_trace.py' -v`. Rapport JSON généré par le programme et publié. Le programme et le test ont été relus après publication et leurs SHA Git comparés aux octets exécutés. Les quatre sources historiques ont été lues et leurs blobs Git vérifiés, mais non exécutées. Aucun voisinage quantitatif `lambda0`, aucune positivité f, aucune admissibilité de bord réelle, aucun crochet fonctionnel de Dirac, aucune contrainte tertiaire, aucune stabilité 4D ou observable cosmologique n'est démontré.

## Priorité
Exécuter **le véritable** `normalized_symbolic()` et `G(s,U,P_g)` de Step45/46/55 avec reconstruction g paramétrique, produire une enclosure de sensibilité et de `lambda0`, puis déterminer explicitement le domaine des variations autorisées par les conditions aux limites. Ne pas confondre ce critère de trace avec une obstruction globale. Ensuite seulement : oracle Poisson/Dirac non-IBP à six couples, rang/tertiaires, chartes K=0/J=0, lapses, 4D, stabilité et observables.
