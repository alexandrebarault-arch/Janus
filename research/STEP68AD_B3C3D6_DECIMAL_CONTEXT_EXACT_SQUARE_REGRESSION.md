# JANUS b3c3d6 — précision du carré décimal (30 octobre 2026)

**Statut scientifique : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Audit de reproductibilité du candidat Step55→Step58, **sans rejeu physique Step58**.

## Défaut reproduit

Les deux helpers publiés utilisaient le produit `Decimal(str(radius))**2` ou `r*r` sous le contexte `decimal` ambiant (précision usuelle 28 chiffres). Pour une abscisse décimale ayant plus de 14 chiffres significatifs, ce produit peut être **arrondi avant** la conversion en `float` ou `Fraction`. Le qualificatif « carré décimal exact » était donc faux dans le cas général.

Témoin indépendant, `r=0.1234567890123456` : sous contexte décimal de précision 28, `Fraction(r*r) - Fraction(r)**2 = 1/1562500000000000000000000000000` (écart exact positif, non nul). La valeur cible du transport était donc dépendante du contexte.

## Correction

- `numerics/hr_b3c3d6_decimal_radius_endpoint.py` : carré `Decimal` dans un `localcontext` de précision >= deux fois le nombre de chiffres de l'opérande + 2 ; API `endpoint_s` inchangée (float, Decimal). Les fonctions d'erreur calculent désormais le carré cible par `Fraction(r)**2`.
- `numerics/hr_b3c3d6_exact_binary_rhs_transport.py` : `decimal_square_target` calcule `Fraction(Decimal(str(radius)))**2`, donc exactement et indépendamment du contexte. Transport d'ordre 1 inchangé.

Pour les **quatre rayons demandés** `1/4,1/2,7/10,17/20`, les carrés décimaux tiennent déjà dans la précision précédente : **aucun changement de valeur physique n'est démontré**, et les coefficients A/B/E ne sont pas recalculés.

## Exécution locale réellement effectuée

`cd /mnt/data/janus_decimal && PYTHONPATH=. python -m unittest discover -s tests -v` : **6 tests PASS, 0 FAIL**, avec sous-tests de précision 6,7,16,28,50 ; témoin négatif de l'ancien comportement, rayons historiques, transport, entrées invalides. `python -m compileall -q numerics tests` : PASS. Les octets des deux helpers et du test ont été vérifiés par les blobs Git publiés (SHA ci-dessous). Tests isolés, non indépendants des helpers ; **les cinq moteurs originaux Step45/46/55/58 et le candidat complet n'ont PAS été exécutés localement** (réseau direct GitHub indisponible).

## Authentification et limites

Les cinq sources originales ont été relues par le connecteur GitHub sur la branche de recherche : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55-normalized `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55-barrier `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`. **Lecture SHA, pas exécution**.

Blobs publiés et relus : endpoint `28ded430d6140c26beb5c4040cfed3241a9cf086`, transport `61b35afbef4a7939bb15481b2ec92487a47b7c37`, test `df083975e2b5fe31fda7983208b9e2dce39943d7`.

## Prochaine étape physique inchangée

Matérialiser les cinq originaux SHA-authentifiés, rejouer le vrai Step58 affine/cubique aux quatre rayons et vérifier convergence ODE `s0/rtol/atol` ; comparer les **six** coefficients `A_N,A_M,B_N,B_M,E_N,E_M`, factorisation/enclosures, centre et BVP des lapses strictement positifs aux deux vrais bords ; ensuite contraintes Dirac, générateurs/charges, jauge temporelle, six couples, K=0/J=0, 4D, stabilité, observables. Aucune conclusion physique nouvelle.
