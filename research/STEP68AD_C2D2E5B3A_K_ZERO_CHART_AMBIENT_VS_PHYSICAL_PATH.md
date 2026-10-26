# JANUS — 68ad-C2d2e5b3a : K=0, dégénérescence du shift réduit et chemin physique

27 octobre 2026. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Audit exact **ponctuel**, non oracle fonctionnel de Poisson/Dirac. L'étape 68ad-C2d2e5b3 reste inachevée : aucun rang complet ni contrainte tertiaire calculés.

## Provenance

Formules relues sur GitHub dans `numerics/hr_step55_global_barrier.py` (blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`) et `numerics/hr_step68o_temporal_interval_annulus.py` (blob `c99caebc17f243784450ddff94fb061767e6d8e7`). Les **modules originaux n'ont pas été exécutés** dans cette session. Les constantes décimales sont traitées comme fractions rationnelles exactes, et non comme flottants. L'EDO Step55 et le profil U(s) n'ont pas été intégrés.

## Théorème algébrique et contre-exemples

Pour le terme de shift `F(z)=D*z+K*sqrt(1-z²)`, `|z|<1`, sa stationnarité est `F_z=D-K*z/sqrt(1-z²)=0`. Si `K>0`, la racine intérieure unique est `z*=D/sqrt(K²+D²)` ; si `K<0`, elle est `z*=-D/sqrt(K²+D²)`. Le contrôle négatif `K=-3,D=4,z=4/5` donne `F_z=8` : le signe de branche ne peut pas être ignoré. À `K=0,D≠0`, aucune racine intérieure. À `K=D=0`, **tous** les shifts intérieurs sont stationnaires et `∂F_z/∂z=0` : perte de rang de l'équation algébrique du shift, **pas** démonstration du rang de Dirac.

La carte réduite n'a **aucune extension continue ambiante** en `(K,D)=(0,0)` : sur `K=epsilon,D=0`, `z*=0`, tandis que sur `K=3epsilon,D=4epsilon`, `z*=4/5` pour `epsilon>0`. De plus, `∂z*/∂D=K²/(K²+D²)^(3/2)=9/(125 epsilon)` sur le second rayon, ce qui diverge. Cela interdit d'employer naïvement le théorème des fonctions implicites à l'origine. **Ce n'est pas une obstruction définitive à la formulation non réduite.**

## Garde rationnelle sur la géométrie Step55

Poser `s=r²`, `0≤r≤17/20`, `Lg=A(1+cg*s)²`, `Lf=A*Y(1+cf*s)²`, `A=0.4`, `Y=0.5787707228025044`, `cg=0.0015`, `cf=-0.0012`. Avec `T=b1*Lg²+2*b2*Lg*Lf+b3*Lf²` et `K=r²*k`, `k=M2*MG*Lg*Lf*T`, les inégalités rationnelles `ylo≤Lf/Lg≤Y`, `b2<0`, `b3>0` impliquent `T/Lg²≥1+2*b2*Y+b3*ylo²>0`. L'exécution donne la **borne rationnelle exacte** `k≥klo`, où `klo` est enregistré sans arrondi dans le certificat JSON, et `float(klo)≈0.221156881156`. C'est une borne élémentaire valable sur tout l'intervalle, pas une extrapolation de quatre échantillons. Ainsi `K>0` pour tout `0<r≤17/20` sur cette géométrie prescrite ; `K(0)=0`.

Sur le **chemin algébrique Step68o** `D=r³*k*Z1/sqrt(1-r²*Z1²)`, `Z1=0.004`, la racine positive donne exactement `z=r*Z1`, `z'=Z1`, `z''=0` et `|z|≤17/5000=0.0034`. Donc le shift admet **une extension continue le long de ce chemin particulier** jusqu'au centre, malgré l'absence d'extension continue pour toutes les directions ambiantes `(K,D)`. Cela ne prouve ni l'EDO Step55 ni la différentiabilité du Hamiltonien réduit sur un voisinage fonctionnel du centre.

## Tests et limites

Commande réellement exécutée : `cd /mnt/data/janus_e5b3 && python -m unittest -v test_hr_step68ad_c2d2e5b3_k0_chart.py` → **15 tests PASS, 0 FAIL** après correction d'un premier essai échoué (simplification SymPy sans hypothèse de signe sur K). `python hr_step68ad_c2d2e5b3_k0_chart.py > report.json` → **16 identités symboliques exactes PASS**, quatre évaluations rationnelles de contrôle, et borne rationnelle globale. Les 16 identités sont des sous-contrôles, pas 16 tests supplémentaires.

**NON DÉMONTRÉ :** matrice fonctionnelle de Poisson/Dirac à six couples sur l'authentique solution Step55/68o, rang complet, tertiaires, conditions aux bords/lapses, charte J=0, 4D, stabilité et observables. La preuve de K>0 concerne cette géométrie prescrite, pas tout l'espace des phases. **Prochaine étape : 68ad-C2d2e5b3b**, construire et tester le véritable oracle sur coquille et ses variations transverses, en conservant les bords et les chartes singulières.
