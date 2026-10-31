# JANUS b3c3d6 — budget rationnel global de sensibilité du coefficient A_M (31/10/2026)

**Statut : b3c3d6 PARTIELLE ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Ceci **n'est pas** une enclosure du coefficient A_M lui-même, ni des six coefficients Step58, ni une preuve de BVP.

## Résultat physique conditionné aux certificats originaux déjà acquis

La dérivée exacte de l'opérateur temporel Step58 original sur Fz=Hg=0, déjà dérivée dans `numerics/hr_b3c3d6_original_step58_minimum_jet.py`, est

`dA_M/dU_ss = -2*r^4*z*sqrt(1-z^2)*K*beta/(Lg*Lf*Mf2*Sf*Sfr*den)`.

Sur la géométrie Step55 : `s=r^2`, `z=Z1*r`, `Sf=r*Lf`, `K=m2*Mg2*Lg*Lf*r^2*T(s)`, `beta=sqrt(1+KF^2*s)`, `den=beta+s*U*KF/(2*Mf2*Sfr)` et `T=beta1*Lg^2+2*beta2*Lg*Lf+beta3*Lf^2`. Ainsi, pour `0<r<=17/20`,

`-dA_M/dU_ss = C(r)*sqrt(1-Z1^2*s)/(1+q)`, avec `C(r)=2*Z1*m2*Mg2*r^6*T/(Mf2*Lf*Sfr)` et `q=s*U*KF/(2*Mf2*Sfr*beta)`.

En utilisant uniquement les constantes rationnelles Step55 et **la barrière globale U déjà certifiée**, `-67/12500<U<-229/50000<0`, l'arithmétique rationnelle donne `1/10<T(s)<1/9`, `0<=q<1/500`, `Sfr>0` sur `0<=s<=289/400` (et `q>0` si `s>0`). Donc **globalement**, pour `0<r<=17/20`, `dA_M/dU_ss<0` et

`C(r)*(1-Z1^2*s)/(1+qmax(s)) < -dA_M/dU_ss < C(r)`, où `qmax(s)=s*(-67/12500)*KF/(2*Mf2*Sfr(s))`.

Aux quatre vrais rayons `1/4,1/2,7/10,17/20`, en important **comme hypothèses déjà certifiées** les limites `|U_ss|<1/10,1/160,1/590,1/1200` de l'archive Step55 (blob `e74057dcf741bcdb655c7d9be48c6a9650d7ff3f`), la contribution **isolée** de U_ss à `A_M`, à U et U_s fixés, vérifie respectivement `|delta A_M|<1/1000,1/300,1/150,1/100`. Ce sont des bornes strictes exactes, non des erreurs totales du calcul Step58. La sensibilité est négative et d'ordre `r^6` au centre, mais cela ne garantit ni l'annulation exacte des B/E, ni les signes physiques des A, ni un BVP à deux bords.

## Exécution, provenance et limites

Code : `numerics/hr_b3c3d6_step58_am_uss_sensitivity_bound.py`. Tests : `tests/test_hr_b3c3d6_step58_am_uss_sensitivity_bound.py`. Commandes réellement exécutées dans un environnement local autonome : `PYTHONPATH=. python -m unittest discover -s tests -v` (**6 PASS, 0 FAIL, 0 SKIP**) ; `python -m compileall -q numerics tests` (**PASS**) ; `python -m numerics.hr_b3c3d6_step58_am_uss_sensitivity_bound` (**PASS** après correction d'une commande initiale qui ajoutait à tort `.py` au nom du module). Les calculs de cette session sont rationnels, sans nouveau rejeu des moteurs originaux Step45/46/55/58, de la barrière 256 cellules, ni du DOP853 physique. Les blobs originaux Step58 (`802c23aebd41780d8c462f1aa1711707fe4ee88f`) et Step55-barrière (`a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`) ont été lus en direct via le connecteur GitHub, non exécutés.

**Prochaine étape inchangée :** véritables six enclosures physiques `A_N,A_M,B_N,B_M,E_N,E_M` du Step58 original aux quatre rayons exacts, factorisation, raffinement DOP853 si nécessaire, BVP strictement positif aux deux vrais bords, puis Dirac/4D/stabilité/observables. Ne pas utiliser ces bornes de sensibilité comme un certificat des coefficients eux-mêmes.
