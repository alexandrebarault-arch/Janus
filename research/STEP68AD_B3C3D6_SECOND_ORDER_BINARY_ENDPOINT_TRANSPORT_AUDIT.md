# JANUS b3c3d6 — Transport holonome d'extrémité d'ordre 2 (30 octobre 2026)

**Statut : amélioration NUMÉRIQUE CONDITIONNELLE, PAS un rejeu physique Step58.**
**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Défaut et correction

Le candidat Step58 utilise l'état final binary64 de SciPy à l'abscisse
`sf=float(Decimal(str(radius))**2)`, tandis que la géométrie et les jets
sont évalués à `s*=Decimal(str(radius))**2` exactement. L'ancien transport
`y*=yf+delta*f(sf,yf)` laisse un reste de Taylor d'ordre `delta²`.

Pour `y'=f(s,y)`, le calcul **holonome** d'ordre deux est
`y*=yf+delta*f+delta²/2*(f_s+f_y*f)`.
Si la vraie solution est C3 et `sup|y'''|<=M3` sur le minuscule intervalle,
le reste de troncature (à état final exact) est borné par
`M3*|delta|³/6`. Cette condition **n'est pas certifiée pour Step55**.
Le calcul ne borne ni l'erreur accumulée par DOP853 ni la sensibilité de
l'opérateur temporel Step58 aux erreurs de l'état/aux jets.

Écarts rationnels exacts pour le solveur corrigé :
- r=1/4,1/2 : delta=0.
- r=7/10 : delta=+1/112589990684262400 ;
  delta²≈7.888609052210118e-35 ; |delta|³/6≈1.167748720270681e-52.
- r=17/20 : delta=-7/225179981368524800 ;
  delta²≈9.663546088957394e-34 ; |delta|³/6≈5.0067226381605446e-51.

Un jouet exact `y=s²`, `f=2s` démontre que le premier ordre manque
exactement `delta²` ; l'ordre deux corrige cette erreur, mais **ne corrige
pas** l'erreur préexistante de `yf`. Un jouet `y=s³` vérifie le reste
`delta³` de l'ordre deux. Le jouet `f=3y+s` vérifie le terme
`f_s+f_y*f` et non une simple dérivée partielle.

## Exécution et reproductibilité

Sur copie locale de l'helper GitHub initial, append identique au blob
publié, et du test publié :
`PYTHONPATH=. python -m unittest discover -s tests -v` :
**6 PASS, 0 FAIL final**. `python -m compileall -q numerics tests` :
**PASS**. Un premier test avait employé par erreur `float(r)**2`
(ancien chemin, double arrondi) au lieu de l'abscisse réelle
`float(Decimal(str(r))**2)` ; il a été corrigé avant la publication
et les six tests ont été rejoués. Ne pas interpréter ce FAIL intermédiaire
comme un échec du nouvel algorithme.

Fichiers :
- `numerics/hr_b3c3d6_exact_binary_rhs_transport.py` :
  nouvelle fonction `transport_endpoint_second_order`, blob
  `052f4949f15ef620aa672e70c7df93f22f955979`.
- `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py` :
  branchement sur la nouvelle fonction, blob
  `43a140cacfca81aaf41073facea3da4e47e64f5e`.
- `tests/test_b3c3d6_second_order_endpoint_transport.py` :
  six tests, blob `9133325fece76fa91adf57acb586b68cc3fa1ab7`.

Cinq originaux Step45/46/55/58 SHA authentifiés dans les sessions
précédentes, mais **aucun original ni candidat physique complet n'a été
exécuté dans cette session** (DNS GitHub direct indisponible au conteneur).
Le nouveau helper est testé indépendamment de l'opérateur physique mais
les tests sont des jouets non indépendants de l'implémentation.

## Prochaine expérience décisive

Matérialiser les cinq sources originales SHA-authentifiées et rejouer
Step58 affine/cubique à r=1/4,1/2,7/10,17/20, avec convergence
`s0/rtol/atol` et les six coefficients `A_N,A_M,B_N,B_M,E_N,E_M`.
Quantifier séparément l'erreur DOP853, le reste d'extrémité et la
sensibilité des coefficients ; ensuite factorisation/enclosures, centre,
BVP lapses positifs deux vrais bords, Dirac, 4D, stabilité, observables.
