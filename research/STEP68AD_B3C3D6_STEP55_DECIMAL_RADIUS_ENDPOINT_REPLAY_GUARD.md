# JANUS b3c3d6 — garde d'extrémité décimale du rejeu Step55 → Step58 (29/10/2026)

**Résultat : correction numérique reproductible, PAS preuve physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Problème identifié dans le candidat original

Le candidat `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py` (blob antérieur `9eb5167bec74fc427307a262faaa6a1f785785a8`) définissait `sf=radius**2` en arithmétique binaire Python, alors que `sr=F(radius)**2`, `F(x)=mp.mpf(str(x))`, et `gr=G(F(radius)**2,ur)` interprétaient le rayon **décimal**. L'intégration `solve_ivp` et l'évaluation du jet radial n'étaient donc pas exactement au même point pour deux des quatre rayons.

Différences **rationnelles exactes** `float(radius)**2 - Decimal(str(radius))**2`, mesurées avec `Fraction.from_float` :
- `r=1/4` : 0 ; `r=1/2` : 0.
- `r=7/10` : `-29/450359962737049600` ≈ `-6.439293542825907e-17`.
- `r=17/20` : `-9/112589990684262400` ≈ `-7.993605777301127e-17`.

**Correctif publié :** `sf,s_exact=endpoint_s(radius)` avec `endpoint_s` utilisant `Decimal(str(radius))**2` puis un unique arrondi final en float. La représentation décimale du float obtenu est `0.49` et `0.7225` aux deux rayons concernés. La garde `abs(F(sf)-F(radius)**2)<1e-40` est **tolérante à l'arrondi mpmath à 45 décimales** ; une égalité binaire stricte serait erronée (différence mpmath ≈ `4.38e-47` pour `r=0.7`). Le flottant reste une approximation du rayon exact, mais le décalage d'une unité de dernier rang du produit binaire est évité.

## Contrôles effectivement exécutés

Commande : `cd /mnt/data/janus_endpoint_radius && PYTHONPATH=. python -m unittest discover -s tests -v` : **6 unittest PASS, 0 FAIL**, dont 4 rayons, deux différences rationnelles exactes, arrondi non aggravé, invalides rejetés et garde mpmath à 45 chiffres. `python -m compileall -q numerics tests` : PASS. Tests du petit module exécutés localement ; **tests d'intégration du candidat complet NON exécutés**, car les cinq moteurs originaux, bien que leurs blobs aient été relus et SHA-authentifiés via le connecteur GitHub, n'ont pas été matérialisés dans le runtime Python.

Sources authentifiées en lecture : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55-normalized `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55-barrier `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`.

Livrables : `numerics/hr_b3c3d6_decimal_radius_endpoint.py` blob `db129eb0fad5357e686710e3d3f2ee911b85c939` ; `tests/test_hr_b3c3d6_decimal_radius_endpoint.py` blob `d32b016f356f79259b2be62326b3945207ebf348` ; candidat Step58 corrigé blob `8162e35deed964a5ec2cbca53bc32cc5c875e420`. Code/tests relus et octets testés concordants pour les deux premiers ; candidat complet **NON exécuté**.

## Portée scientifique et priorité

Ce défaut d'extrémité est **petit** devant l'incertitude potentielle de `solve_ivp(rtol=1e-12,atol=1e-14)` et ne permet **ni** de réfuter les coefficients antérieurs `B/E~1e-44` **ni** de les certifier. Il n'y a toujours **aucune** borne rigoureuse d'erreur sur l'intégration Step55, aucune enclosure des six coefficients physiques et aucun BVP positif à deux bords. Le test holonomique des jets est interne à la reconstruction et ne remplace pas une validation indépendante de l'intégrateur.

**Prochaine étape inchangée :** matérialiser les cinq originaux SHA-authentifiés, exécuter le candidat cubique corrigé et l'ancien affine aux rayons `1/4,1/2,7/10,17/20`, comparer six coefficients et défauts, réaliser un contrôle de convergence de l'EDO, puis factorisation/enclosures, centre/BVP positif aux deux vrais bords, Dirac/charges/jauge/six couples/K=0/J=0/4D/stabilité/observables. Ne toucher ni `main`, ni `research/v2-flrw`, ni workflows.
