# JANUS — 68ad-C2d2e5b3b2c2b1 : charte non dégénérée du coefficient Step46 sur le domaine radial

**27 octobre 2026. Résultat exact mais CONDITIONNEL à |U(s)|<=1. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources physiques et portée

Sources originales authentifiées par lecture du connecteur GitHub :
- `numerics/hr_step45_exact_physical_ward.py` — Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
- `numerics/hr_step46_exact_secondary_ode.py` — `bac025c28dbe1561c0c36c56dbfda46dc326f804`.
- `numerics/hr_step55_normalized_secondary.py` — `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`.
- `numerics/hr_step55_global_barrier.py` — `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.

La formule de coefficient affine de la contrainte secondaire, après élimination des deux primaires de poussière f, est exactement celle de Step46 :
`C_V = -m2*Mg2*At*sqrt(1-z²)*Lf*beta_f/(2*Mf2*Sf*Sfr*(beta_f+fac*tfr))`,
où `V=pLf'`, `fac=pLf/(2*Mf2*Sf*Sfr)`, `beta_f=sqrt(1+tfr²/Lf²)`. Ce coefficient **n'est pas** le `J=∂B_N/∂pSf` temporel des audits Step60.

Avec la géométrie Step55, `s=r²`, `R=17/20`, `Lg=a(1+cg*s)²`, `Lf=b(1+cf*s)²`, `Sf=r*Lf`, `Sfr=b(1+cf*s)(1+5cf*s)`, `tfr=r*kf*Lf`, `z=r*z1`, `pLf=r² U`, `At=r² T(s)`, et
`T=beta1*Lg²+2*beta2*Lg*Lf+beta3*Lf²`.
Les paramètres décimaux Step55 sont traités comme fractions EXACTES, pas comme flottants.

La substitution exacte donne
`beta_f+fac*tfr=sqrt(1+kf²*s)+kf*s*U/(2*Mf2*Sfr)`,
et, pour `r>0`,
`C_V/r=-m2*Mg2*T(s)*sqrt(1-z1²*s)*beta_f/(2*Mf2*Sfr*(beta_f+fac*tfr))`.

## Certificat sur un continuum, pas un échantillonnage

La positivité de `T(s)` sur tout `s∈[0,289/400]` résulte des cinq coefficients rationnels exacts de sa représentation de Bernstein de degré 4 : **chacun est >1/10 et <11/100**. Aucun découpage numérique ni extrapolation de points n'est requis. Les expressions de `Sfr` donnent exactement `Sfr>23/100` et `Sfr<b<1/4`.

Pour **tout** `U` tel que `|U|<=1`, indépendamment de sa dérivée ou de `Pg`, les encadrements élémentaires `1<=sqrt(1+kf²*s)<=1+kf²*S` et `sqrt(1-z1²*s)>=1-z1²*S>999/1000` impliquent
`beta_f+fac*tfr >= 1-S*|kf|/(2*Mf2*Sfr_min) >3/4`.
Le majorant analogue du dénominateur, avec les minorants de `T` et de la racine du shift, donne **`C_V/r < -372` pour `0<r<=17/20`**. Les bornes exactes, sans arrondi, figurent dans le JSON.

Valeurs décimales purement indicatives : `T∈[0.106037774505...,0.108221332359...]`, dénominateur f `>0.787967230705...`, `-C_V/r>372.501551686...`. Au centre `C_V=O(r)` : le résultat concerne le **coefficient normalisé** `C_V/r` et ne transforme pas la charte centrale en une charte régulière ambiante.

## Reproductibilité et limites

`PYTHONPATH=. python -m unittest discover -s tests -v` : **13 tests Python unittest PASS, 0 FAIL**, dont deux tests d'identités SymPy indépendantes (déjà inclus dans 13). `python numerics/hr_step68ad_c2d2e5b3b2c2b1_f_chart_coefficient.py` génère le JSON exact. SHA Git des trois fichiers testés/générés : code `d16150475c4d3ac38162c8be06c07d8734efa4c2`, tests `c608333536783b0c67a1c842b0ba94253939331d`, certificat `24d9f2cefa001b1fabd3634b87556cbab6c90b42`.

**NON PROUVÉ :** `|U(s,lambda)|<=1` pour la solution physique paramétrée ; existence/continuation de cette solution ; positivité de la densité de poussière f ; sensibilité `G_Pg` du véritable moteur ; conditions aux bords ; rang complet Dirac, tertiaires, lapses, `J=0` temporel, `K=0`, dynamique 4D, stabilité et observables. Les sources historiques ont été lues et SHA-authentifiées mais **leurs moteurs n'ont pas été réexécutés dans cette étape**. La marge g antérieure `|lambda|<=1/1000` n'est pas promue en marge f ou en solution complète.

**Prochaine étape effective 68ad-C2d2e5b3b2c2b2 :** exécuter réellement le `G(s,U,Pg)` original avec paramètre, établir une borne uniforme de `U` et de `rho_f` sur un voisinage `lambda`, puis conditions aux bords et oracle fonctionnel non-IBP à six couples, rang/tertiaires/chartes singulières. Ne pas confondre ce contrôle de coefficient avec la matrice Dirac.
