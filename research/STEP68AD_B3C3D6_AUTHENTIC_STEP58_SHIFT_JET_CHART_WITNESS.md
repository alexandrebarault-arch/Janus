# b3c3d6 — témoin rationnel exact sur l'opérateur ORIGINAL Step58 (28 octobre 2026)

## Portée et provenance

Cette session a **réellement exécuté** les sources originales SHA-authentifiées `numerics/hr_step45_exact_physical_ward.py` (blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`) et `numerics/hr_step58_temporal_operator.py` (blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`). La reconstruction locale du premier import `authenticated_step45` est un *shim minimal*, et **non** le fichier Step57 original : il vérifie le blob exact Step45. Les moteurs Step55, Step68o et b3c2, ainsi que le probe original au rayon `R=17/20`, n'ont PAS été exécutés. Les deux fichiers originaux ont été vérifiés par calcul local du SHA Git blob, octet pour octet.

Le témoin n'est **pas** une solution radiale Step55 et n'est **pas** une direction tangente à la totalité de la chaîne Dirac. Son utilité est de tester directement, et non plus avec des jouets, l'hypothèse de non-annulation de `B_M` sur une tranche ponctuelle de l'opérateur original.

## Témoin exact

Sur les douze coordonnées canoniques, fixer `Lg=Lf=Sg=Sf=1`, `pg=3/4`, `pf=311/100`, et toutes les autres valeurs de coordonnées nulles. Fixer les jets de premier ordre `Sg'=1`, `Sf'=4/5`, `pLg'=-3/4`, les autres à zéro. Fixer `Lf''=42/25`, `Lf'''=4476/625`, les autres jets d'ordre 2 et 3 à zéro, et tous les jets d'ordre 4 à zéro. Prendre `z=3/5`, `z'=-96/125`, `z''=z'''=0`; `Mg2=Mf2=m2=1`, `(beta0,beta1,beta2,beta3,beta4)=(-4,1,0,0,-4)`.

**Résidus exacts nuls :** `Fz=0`, `Fz'=0`, `Fz''=0`, `Fz'''=0`, `Hg=0`, `Hf=0`, `C_exact=0`. Le secteur est algébriquement régulier : `K=1>0`, `z=3/5>0`, `sqrt(1-z²)=4/5>0`, les deux densités de poussière `pg=3/4` et `pf=311/100` sont strictement positives, et `Lg,Lf,Sg,Sf>0`.

L'opérateur temporel original au point, sur cette tranche, est **exactement** :

```text
(1293/250) N + (224/125) N' - (79093/12500) M = 0
B_N = 224/125 > 0
B_M = 0
E_N = E_M = 0
```

Il est donc **faux** de déduire la non-annulation de `B_M` de la seule combinaison `Fz=Hg=Hf=C=0`, de la positivité de `K,z` et des poussières, même en imposant les trois jets radiaux de `Fz` ci-dessus. L'usage de la carte `q=B_N/B_M` exige une preuve de `B_M != 0` sur la solution authentique Step55, ou une autre carte/raccord si un zéro survient. Ce témoin ne démontre PAS que `B_M` s'annule sur Step55 : les dérivées radiales de `Hg,Hf,C`, les équations spatiales globales, les conditions au centre et au bord externe et la tangence Dirac complète ne sont pas imposées.

## Rejeu et non-régression réellement exécutés

- `python -m numerics.hr_step58_temporal_operator` : succès, certificat original `M''=0` sur `Fz=0` et `N''=(z²-1)Hg/(Lg Lf)` sur `Fz=0`, donc les deux s'annulent sur `Fz=Hg=0`.
- `exact_certificate_summary()` original Step45 : neuf résidus Ward exacts nuls.
- `python -m numerics.hr_step68ad_b3c3d6_authentic_shift_jet_chart_witness` : sept résidus de contraintes/jets exacts nuls, six coefficients `A/B/E` comparés aux fractions attendues, conditions de signe vérifiées.
- `python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_authentic_shift_jet_chart_witness.py' -v` : **4 tests PASS**, non indépendants du calcul, zéro échec.
- Exécution locale du témoin : ~9,44 s, SymPy, source authentifiée. Le clone Git direct échoue toujours sur DNS `Could not resolve host: github.com`; la publication passe par le connecteur GitHub.

## Priorité suivante

Rejouer le **vrai** probe Step58 à `R=17/20` avec Step45/55/58+b3c2 et Step68o, certifier les enclosures de `B_N,B_M`, rechercher leurs zéros sur les anneaux originaux et les cartes de raccord au centre, déterminer `b,d` et résoudre le problème global des lapses positifs avec les véritables conditions Step55. Ensuite seulement : vrai pullback Dirac, générateurs/charges, quotient de jauge temporelle, six couples, `K=0`, `J=0`, dynamique 4D, stabilité et observables.

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
