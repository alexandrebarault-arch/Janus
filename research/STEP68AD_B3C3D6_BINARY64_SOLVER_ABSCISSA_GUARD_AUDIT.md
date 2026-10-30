# JANUS b3c3d6 — abscisses binaires réelles de Step55/58 (30/10/2026)

**Statut : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Audit exact d'arithmétique IEEE-754 sur le candidat `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py` (blob `8162e35deed964a5ec2cbca53bc32cc5c875e420`), lu via le connecteur GitHub. Aucune intégration Step58 originale ni BVP physique n'a été exécuté.

## Défaut du contrôle de précision existant

Le candidat intègre l'EDO par `solve_ivp(..., (s0, sf), ...)`, avec `sf=float(Decimal(str(radius))**2)`, donc l'abscisse effectivement fournie au solveur est **le rationnel binary64 exact** `Fraction.from_float(sf)`. Mais la garde `abs(F(sf)-F(radius)**2)<1e-40` utilise `F=lambda x:mp.mpf(str(x))` : elle retransforme le binary64 en sa **représentation décimale courte**. À `r=0.7` et `r=0.85`, la garde est satisfaite (différence décimale zéro) alors que le temps de fin du solveur n'est **pas** le carré décimal exact. Cette garde ne certifie donc pas une précision d'abscisse de `1e-40`.

Écarts rationnels exacts `sf_binary64 - r_decimal²` :

- `r=1/4` : **0**.
- `r=1/2` : **0**.
- `r=7/10` : **-1/112589990684262400** ≈ `-8.881784197001253e-18`.
- `r=17/20` : **7/225179981368524800** ≈ `+3.1086244689504386e-17`.

À l'initialisation, `float(1e-4)-1/10000 = 221/46116860184273879040000` ≈ `4.79217360238593e-21` ; l'initialisation Taylor utilise `F(s0)` décimal alors que `solve_ivp` reçoit le temps initial binary64. Les écarts sont inférieurs à 1/2 ulp et donc attendus ; ils ne sont **pas** des erreurs du solveur. Le problème est de les masquer dans une prétendue garde `1e-40`.

## Portée et action

Les deux écarts ne bornent **aucune** erreur de `U(R)`, des coefficients `A_N,A_M,B_N,B_M,E_N,E_M` ou de leur annulation : il faut une borne sur `U_s` et la propagation de l'erreur, ainsi que la sensibilité de l'opérateur temporel. Le contrôle numérique devra séparer explicitement les abscisses binary64 et les cibles décimales, et comparer des intégrations en précision augmentée. Ne pas présenter `F(sf)==r²` comme preuve d'égalité des temps réellement intégrés.

Tests isolés réellement exécutés : `cd /mnt/data/janus_binary_endpoint && python -m unittest discover -s tests -v` : **6 PASS, 0 FAIL** ; `python -m compileall -q numerics tests` : PASS. Les tests rationnels vérifient quatre rayons, la demi-ulp, le décalage initial et un contrôle négatif explicite. Aucune des cinq sources physiques originales n'a été exécutée ici. La connexion GitHub par connecteur fonctionne ; le DNS direct du container est indisponible.

**Suite prioritaire inchangée :** cinq originaux SHA-authentifiés, Step58 affine/cubique aux quatre rayons, convergence ODE/abscisses/précision, six coefficients, factorisation/enclosures, centre/BVP positif deux bords, Dirac/4D/stabilité/observables.
