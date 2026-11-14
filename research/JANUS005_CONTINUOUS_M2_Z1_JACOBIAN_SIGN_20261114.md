# JANUS-005 — Signe continu du jacobien (M2,Z1) sur l'anneau Step55 (2026-11-14)

**Statut : résultat algébrique certifié par arithmétique rationnelle d'intervalles ; NON preuve d'admissibilité physique.** Source : `numerics/hr_step55_global_barrier.py` au HEAD `0120aa63b3e4871e105b15ff27a77ce2edc6667f`, blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Précédent : `research/JANUS005_M2_Z1_WFBAR_DBAR_JACOBIAN_20261114.md` (blob `317a12f64e9c61001d3af049494eac78e5050e39`).

## Proposition et portée
Sur la carte à coefficients `MG,Lg,Lf,T,Tf,s` figés, avec `MG=1`, `M2=23.3348939346`, `Z1=0.004` et les fonctions géométriques prescrites Step55, le déterminant `det(d(Wfbar,Dbar)/d(M2,Z1))` est **strictement négatif pour tout s dans [0,0.7225]**. Cela étend le signe central ponctuel au domaine radial complet de cette carte, mais **ne prouve pas** que `M2,Z1` sont des paramètres physiques indépendants, ni que les deux vrais bords, Dirac ou la dynamique 4D sont satisfaits.

Formule symbolique originale déjà vérifiée et indépendamment recontrôlée avec SymPy :
`J=M2*MG**2*Lg*Lf*T*Q/r**3`, `r=sqrt(1-Z1**2*s)`, `Q=Lf*Tf+Lg*T*r*(1+s*Z1**2)`.
Les constantes originales sont `A=2/5`, `Y=0.5787707228025044`, `B=A*Y`, `CG=0.0015`, `CF=-0.0012`, `B1=1`, `B2=-4.2383993109`, `B3=13.6801214252`, `B4=-38.5117901844`. Les fonctions : `Lg=A*(1+CG*s)**2`, `Lf=B*(1+CF*s)**2`, `T=B1*Lg**2+2*B2*Lg*Lf+B3*Lf**2`, `Tf=B2*Lg**2+2*B3*Lg*Lf+B4*Lf**2`.

## Calcul effectivement exécuté
Commande `python /mnt/data/janus_sign/check.py` (Python standard library `fractions.Fraction` et `math.isqrt`). La partition exacte est `s_k=(289/400)*k/256`, `k=0,...,256`. Toutes les entrées décimales sont construites comme fractions exactes. Chaque opération sur intervalle est arrondie vers l'extérieur par fractions ; `sqrt(q)` est bornée par `floor(sqrt(q)*10**22)/10**22` et cette borne plus `10**-22`, avec `isqrt(floor(q*10**44))`. L'arithmétique des intervalles traite chaque sous-intervalle entier, sans échantillonnage. La formule de J est évaluée directement en intervalles sur chaque cellule ; chaque dénominateur r est strictement positif.

Résultat de l'exécution : `T positive all: True`, `Q negative all: True`, `det negative all: True`. Enveloppes globales affichées (décimales arrondies pour lecture, NON bornes à réutiliser comme certificats exacts) :
- `T` : [0.1060297323982009, 0.10822935875319159]
- `Q` : [-0.005011798920083653, -0.004458340344540431]
- `J` : [-0.0011721273453854024, -0.0010219379115121653]

**Contre-contrôle :** `sympy.simplify(det(Matrix([W,D]).jacobian([m,z]))-m*g*g*b*a*t*Q/r**3)==0` : PASS indépendamment du calcul d'intervalles. Le fichier Python effectivement exécuté avait le Git blob local `794400b08c4e88b8a4fbbc83dd2194bb73680844` (`git hash-object check.py`), et `python -m py_compile check.py` : PASS. Ce script n'est pas encore transféré dans le dépôt : la reproduction complète nécessite de le conserver/publier avec ses octets ; ne pas prétendre que les seules décimales sont un certificat portable.

**Tests moteur Step55/58 nouveaux : 0 ; cellules physiques Step55/58 évaluées : 0 ; certifiées : 0.** Les 256 subdivisions ci-dessus sont des cellules de contrôle du **jacobien algébrique**, pas des cellules physiques du moteur b3c3d9.

**NEXT_ACTION_EXACT :** publier le script exact avec son empreinte et refaire le calcul depuis une copie authentifiée ; puis filtrer les variations M2/Z1/PG par les contraintes Step45/49/55, Dirac et les deux vrais bords. JANUS-001 : transférer les dépendances originales et exécuter les neuf tests puis le pilote physique. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
