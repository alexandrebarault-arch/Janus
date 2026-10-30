# JANUS b3c3d6 — certificat rationnel de défaut d'EDO (30 octobre 2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** b3c3d6 demeure PARTIELLE. Résultat mathématique exact **conditionnel**, sans rejeu physique Step58 ni enclosure des six coefficients.

## Théorème exact sur une cellule

Pour U'=f(s,U), soit v une approximation différentiable, d=v'-f(s,v), h=b-a>0. Supposons l'existence de U sur [a,b], une erreur initiale certifiée |U(a)-v(a)|<=e, une borne continue |d|<=D, et |f(s,U(s))-f(s,v(s))|<=L|U(s)-v(s)| sur un tube certifié contenant U et v, avec L>=0 et Lh<1.

La forme intégrale donne sup|U-v|<=e+hD+Lh sup|U-v|, donc

    |U(b)-v(b)| <= (e+h D)/(1-L h).

Cette borne est rationnelle exacte lorsque e,D,L,a,b sont rationnels. Les cellules contiguës se chaînent ; toute cellule avec Lh>=1 est refusée. Le résultat **ne prouve pas** que le tube contient U : existence et invariance du tube doivent être démontrées indépendamment ou par un bootstrap rigoureux.

## Enclosure Bernstein et témoin de non-certification par échantillonnage

Si le défaut complet d est un polynôme à coefficients rationnels exacts, sa conversion en coefficients Bernstein sur [a,b] fournit sup|d|<=max_i|beta_i|. Code purement rationnel : numerics/hr_b3c3d6_rational_defect_certificate.py.

Contre-exemple exact : v=s²(1-s)², f=0, d=2s-6s²+4s³. Le défaut est nul aux trois points 0, 1/2, 1, mais non nul entre eux. Un test par échantillonnage seul ne peut donc certifier l'erreur DOP853. L'enclosure Bernstein révèle ce défaut.

## Vérifications réellement effectuées

Commande locale : cd /mnt/data/janus_defect && PYTHONPATH=. python -m unittest discover -s tests -v : **8 PASS, 0 FAIL final** ; python -m compileall -q numerics tests : **PASS**. Un résultat attendu erroné dans le test de chaînage (1/4 au lieu de 5/18) a été corrigé avant le passage final. Tests jouets non indépendants. Sources et tests publiés avec blobs correspondant exactement aux octets testés.

Sources originales Step45/46/55/58 et candidat cubique consultés par le connecteur GitHub ; **aucun moteur physique original ni candidat cubique exécuté dans cette session**, car DNS GitHub direct du conteneur inaccessible. L'EDO Step55 réelle n'est pas polynomiale : le helper Bernstein exige une représentation ou enclosure certifiée de son défaut continu ; aucun tel défaut, aucune erreur initiale ni aucun tube/L physique n'est établi. Aucune borne epsilon physique, aucun coefficient A/B/E certifié.

**Prochaine étape inchangée :** cinq originaux SHA-authentifiés, rejeu affine/cubique aux quatre rayons 1/4, 1/2, 7/10, 17/20, convergence et six coefficients, enclosures du résidu continu et de la sensibilité, centre/BVP lapses positifs deux bords, Dirac/4D/stabilité/observables.
