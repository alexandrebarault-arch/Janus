# JANUS — 68ad-C2d2b : vérification exacte de la coquille du shift Step55/68o

**Statut : LEMME CONDITIONNEL DÉMONTRÉ ; Step58/60 PHYSIQUES NON EXÉCUTÉS ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance et portée

Lecture directe GitHub, branche `research/gate2b-nonhomothetic-transfer` :
- `numerics/hr_step55_global_barrier.py` : blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.
- `numerics/hr_step68o_temporal_interval_annulus.py` : blob `c99caebc17f243784450ddff94fb061767e6d8e7`.
- `numerics/hr_step58_temporal_operator.py` : blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`.

Le script nouveau **rejoue indépendamment les formules algébriques** des deux premiers fichiers. Il n'importe PAS le Hamiltonien original et n'exécute PAS le Step58/60 temporel. Le lemme est structurel : il s'applique au profil canonique prescrit, indépendamment de la preuve d'existence globale de la solution radiale.

## Preuve

Poser `s=r²`, `Lg=a(1+cg*s)²`, `Lf=b(1+cf*s)²`, `Sg=r*Lg`, `pSg=r*Psg`, `pLg=s*Gmom`, `pg=s*Rhog`, `tg'=r*kg*Lg`. Dans Step55/68o :

`Sgr = d(r Lg)/dr = a(1+cg*s)(1+5cg*s)`,

`Gprime = (d(s Gmom)/dr)/r = 2pg0(1+5cg*s)`,

`Psg=(s*Dbar+Lg*Gprime-s*Rhog*kg*Lg)/Sgr`.

Le `Dg` exact du Step58 est `pSg*Sg' - Lg*pLg' + pg*tg'`. En substituant les expressions précédentes, les contributions en `Gprime` et en `Rhog` s'annulent **identiquement**, d'où

`Dg=r³ Dbar`.

Avec `T=b1*Lg²+2*b2*Lg*Lf+b3*Lf²` et `k=m²*mg*Lg*Lf*T`, l'interaction exacte du Step58 donne

`K=r² k`, `Dbar=k*z1/sqrt(1-z1²*r²)`.

Par conséquent,

`(Dg²+K²)*(1-z1²*r²)=r⁴*k²`.

Sous les conditions **r>0, k>0, 1-z1²*r²>0**, la racine principale est `sqrt(Dg²+K²)=r²*k/sqrt(1-z1²*r²)`, donc le shift stationnaire `z=Dg/sqrt(Dg²+K²)=r*z1`. On obtient `z'=z1`, `z''=0`, `z'''=0` et `Fz=Dg-K*z/sqrt(1-z²)=0`.

**Importance :** les quatre jets du shift insérés dans le vrai Step68o (`R*Z1,Z1,0,0`) sont algébriquement compatibles avec la coquille stationnaire du profil canonique original. Ceci n'établit pas les signes temporels ni le rang de Dirac. La positivité de `k` est une hypothèse indispensable ; un contre-exemple `k<0` inverse le signe de `Dg/sqrt(Dg²+K²)`.

## Exécution et non-régression

`cd /mnt/data/janus_shift_shell && PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2d2b_exact_step68o_shift_shell.py` → **10 PASS, 0 FAIL (21,26 s)**. Exécution supplémentaire du manifeste symbolique `python -m numerics.hr_step68ad_c2d2b_exact_step68o_shift_shell` → PASS (15,12 s).

Code testé blob `3a996c87fd832d927066e0a68f17279df50ac84c` ; tests blob `7746ca04e8c46c34f17a8bf35c4f90cdd71b251b`. Les deux fichiers ont été publiés sur la seule branche autorisée et relus byte-identiques.

## Limites et prochaine action

**0/14 nouveaux coefficients temporels certifiés.** Le véritable Step58 sur les sept cellules `[1/64,1/32]` et le quotient Step60 restent NON EXÉCUTÉS. Le conteneur de calcul ne possède pas les sources authentifiées et trois rapports dans un checkout commun ; le DNS GitHub direct y échoue, même si le connecteur lit et écrit. Il faut résoudre ce transfert, exécuter Step58, puis Step60 et les gardes C2d2b ; si un intervalle contient zéro, rester INCOMPLETE. Les contraintes Dirac complètes, les lapses admissibles, les conditions aux bords, la dynamique 4D, la stabilité et les observables restent ouvertes.
