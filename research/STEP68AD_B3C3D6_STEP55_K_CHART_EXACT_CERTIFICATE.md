# JANUS — b3c3d6 : certificat rationnel du domaine géométrique K>0 de Step55

29 octobre 2026. **Résultat exact limité à la géométrie prescrite Step55.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Provenance et portée

Lecture authentifiée via le connecteur GitHub de `numerics/hr_step55_global_barrier.py`, blob Git `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, et de `numerics/hr_step58_temporal_operator.py`, blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Les constantes ci-dessous proviennent de la fonction originale `geometry(s)` et de la définition originale `K=m2*mg*Lg*Lf*(b1*Sg²+2*b2*Sg*Sf+b3*Sf²)` de Step58. **La transcription est contrôlée par inspection du blob, mais le moteur Step55/Step58 original n'a pas été exécuté dans cette session** (DNS du conteneur indisponible). Un contrôle facultatif du blob original est inclus dans le script.

## Théorème exact sur le domaine radial

Sur `0 <= r <= 17/20`, poser `s=r²`, `A=2/5`, `Y=0.5787707228025044`, `B=A*Y`, `cg=0.0015`, `cf=-0.0012`, `Lg=A(1+cg*s)^2`, `Lf=B(1+cf*s)^2`. Step55 impose `Sg=r*Lg`, `Sf=r*Lf`, avec `b1=1`, `b2=-4.2383993109`, `b3=13.6801214252`. Alors

`K(r) = r² * m2 * mg * Lg(s) * Lf(s) * T(s)`, avec `m2=23.3348939346`, `mg=1`, `T(s)=Lg(s)^2+2*b2*Lg(s)*Lf(s)+b3*Lf(s)^2`.

Sur `s∈[0,289/400]`, le polynôme `T(s)` est de degré 4. En le représentant dans la base de Bernstein après `s=(289/400)t`, **ses cinq coefficients sont strictement positifs et ses quatre différences consécutives strictement négatives**, vérifiés en arithmétique rationnelle SymPy. Donc `T` est strictement décroissant et

`53/500 < T(s) < 109/1000` (les bornes sont strictes également aux extrémités).

`Lg(s)>=A>0`, `Lf(s)>=Lf(289/400)>0`, et l'évaluation rationnelle donne

`K(r)/r² > 9/40` pour `0<r<=17/20`.

En outre le shift prescrit `z(r)=r/250` vérifie `0<=z<=17/5000<1`. Sur la coquille stationnaire `Fz=0`, `D=K*z/sqrt(1-z²)` ; `K` s'annule exactement à l'ordre `r²` au centre et `D` à l'ordre `r³`, avec coefficients dominants positifs. **La carte stationnaire K>0, |z|<1 est donc valable sur tout l'anneau ouvert `0<r<=17/20`, mais dégénère au centre r=0**. La dégénérescence centrale ne démontre aucune singularité physique.

## Ce que le certificat ne démontre pas

Cette preuve est indépendante de l'inconnue dynamique `U(s)` et du calcul des coefficients temporels `A_N,A_M,B_N,B_M,E_N,E_M`. Elle ne certifie **aucun** signe de `B_N` ou `B_M`, aucune absence de zéro commun de ces coefficients, aucun raccord régulier des lapses, aucune condition de bord temporelle ni aucune tangence Dirac. Elle ne remplace pas le probe original Step58 à `R=17/20`. Elle fournit seulement une borne rationnelle indépendante qui écarte les zéros de `K` **pour le profil géométrique Step55 prescrit hors centre**, donc une condition de carte préalable au futur probe. La positivité de `K` était déjà connue dans le programme Step54/55 ; la contribution ici est un certificat Bernstein court, quantitatif et autonome, non une nouvelle validation de JANUS.

## Tests réellement exécutés

`PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_step55_k_chart` : 14 assertions groupées SymPy/rationnelles PASS, dont 5 signes de Bernstein et 4 différences, limites centrales et bornes ; 0 échec. `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_step55_k_chart.py' -v` : 4 cas PASS, non indépendants, 0 échec. Le JSON est la sortie directe du module exécuté. Aucun test original Step45/55/58/Step68o/b3c2 n'a été rejoué.

## Prochaine action impérative

Exécuter `python -m numerics.hr_step68ad_b3c3d5_temporal_boundary_jet_rank --probe-original` dans un environnement complet aux blobs authentifiés, puis étudier les coefficients et les vrais jets de lapses aux deux bords, les éventuels zéros de `B_N,B_M`, la compatibilité des conditions physiques et le raccord central ; ensuite pullback Dirac, charges/générateurs, quotient jauge temporelle, six couples, `K=0/J=0`, dynamique 4D, stabilité, observables. `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.
