# JANUS-001 — contre-exemple exact de complétude du jet d'ordre 2 (17 novembre 2026)

## Portée et provenance
Audit algébrique **indépendant** de la fermeture locale des jets, fondé sur la transformation utilisée par `numerics/hr_b3c3d6_boundary_ANAM_interval_certificate.py` et `numerics/hr_b3c3d9_annular_direct_enclosure.py` au HEAD `a14220eaeb3f31199f1b44062b4c83354449fefe`. Il ne s'agit **pas** d'une exécution physique Step55/58 et aucune contrainte de Dirac ni condition de bord n'est imposée.

## Hypothèse falsifiable
Au rayon arbitraire `r0>0`, soient `s0=r0**2` et deux fonctions analytiques `U_A(s)=u0+u1(s-s0)+u2(s-s0)**2/2` et `U_B(s)=U_A(s)+epsilon*(s-s0)**3`. Elles ont exactement les mêmes valeurs `U,U_s,U_ss` en `s0`. Le jet de `pLf(r)=r**2*U(r**2)` à l'ordre 3 serait-il entièrement déterminé par ces trois données ?

## Calcul exact et contrôle contradictoire
Leur différence est `delta_pLf=epsilon*r**2*(r**2-r0**2)**3`. Différentiation symbolique SymPy 1.14.0 :

| Ordre k | d^k(delta_pLf)/dr^k évaluée en r0 |
|---|---|
| 0 | 0 |
| 1 | 0 |
| 2 | 0 |
| 3 | `48*epsilon*r0**5` |
| 4 | `672*epsilon*r0**4` |

Commande reproductible :

```bash
python - <<'PY'
import sympy as s
r,r0,e=s.symbols('r r0 e',real=True,positive=True)
d=e*r**2*(r**2-r0**2)**3
for k in range(5):
    print(k,s.factor(s.diff(d,r,k).subs(r,r0)))
PY
```

Contrôle indépendant : règle de Leibniz appliquée à `r²(s-s0)^3` ; le coefficient du terme `(r-r0)^3` vaut `8*r0**5`, donc la dérivée troisième vaut `3!*8*epsilon*r0**5=48*epsilon*r0**5`. Le coefficient du terme `(r-r0)^4` vaut `28*r0**4`, donc la dérivée quatrième vaut `4!*28*epsilon*r0**4=672*epsilon*r0**4`.

## Verdict limité
**NO-GO algébrique pour l'affirmation inconditionnelle** selon laquelle `(U,U_s,U_ss)` fixe `pLf'''` ou `pLf''''` à `r0>0`. Le `physical_jet` existant utilise le Taylor quadratique de U et fixe implicitement le jet supérieur de cette extension à zéro. Cela ne démontre **pas** une erreur dans les coefficients Step58 : il faut encore vérifier si leurs dépendances effectives aux jets supérieurs s'annulent sur la coquille physique Step55. Les deux fonctions construites ne sont pas nécessairement des solutions de l'ODE Step55.

**NEXT_ACTION_EXACT :** sur sources authentifiées, calculer `diff(op['operator']['N'][0], op['qppp'][index_pLf])` et l'analogue M, puis vérifier les coefficients des autres jets induits par `U_sss` après réduction sur `Fz=Hg=Hf=C=0`. Si non nuls, dériver `U_sss` à partir de l'ODE authentique et refaire les enclosures. Ensuite neuf tests et pilote une cellule. En cas d'indisponibilité des sources, poursuivre JANUS-005/006 Dirac et deux vrais bords.

Tests moteur : SKIP ; pilote : SKIP ; cellules physiques évaluées/certifiées/inconclusives : 0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
