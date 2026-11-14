# JANUS-005 — Deuxième coefficient radial après compensation par KG (2026-11-14)

HEAD des formules source consultées : `6df57efafb424a3bcd829081ec74c80d208d5b3a`. Reprise de la transcription de `rho_g(s)` dans `research/repro/janus005_center_radial_density_jet_20261114.py` (blob Git `bdb3eaabb2bd9afea3ec8856134920fde1d5c51d`) ; remplacement de KG constant par un paramètre différentiable. **Ce n'est pas une exécution du moteur physique.**

## Hypothèse falsifiable

La direction tangentielle `dA=1`, `dM2/dA=-(4*A**3*M2*C+0.9)/(A**4*C)`, `dZ1/dA=-Z1/A`, `dCG/dA=-CG/A` conserve les données centrales ; choisir `dKG/dA` pour annuler la variation du premier coefficient de Taylor en `s=r²`. Tester si cette unique compensation annule également le coefficient de `s²` de `rho_g(s)`.

## Calcul réellement exécuté

Python avec mpmath 1.3.0, précision `mp.mp.dps=60`. Formule de `rho_g` copiée depuis la transcription Step55 susmentionnée, avec `betag=sqrt(1+KG**2*s)+s*fac*KG*Lg`. Définir `a_n=[s^n]rho_g(s)=diff(rho_g,s,n)|s=0/n!`, puis `D=partial_A+Mprime*partial_M2-(Z1/A)*partial_Z1-(CG/A)*partial_CG`.

| Quantité | Valeur (60 décimales de travail) |
|---|---:|
| `D a1` à KG fixé | -0.0861285079500553599464593576622 |
| `partial_KG a1` | +0.844143967240728504277694572661 |
| `k=-D a1/partial_KG a1` | +0.102030591098797355215448471894 |
| `D a2` à KG fixé | +0.0000952896031870313987917319253487 |
| `partial_KG a2` | +0.0042771372847821492474124612269 |
| **`D a2+k*partial_KG a2`** | **+0.000531688448564059244385291354039** |

Paramètres : A=0.4, M2=23.3348939346, Z1=0.004, CG=0.0015, KG=0.0012, Y=0.5787707228025044, CF=-0.0012, b1=1, b2=-4.2383993109, b3=13.6801214252. Les décimales sont traitées comme valeurs exactes d'entrée mpmath.

## Contrôle contradictoire indépendant

Différences finies centrées sur le coefficient `a2`, en faisant varier linéairement les cinq paramètres suivant la tangente :

- `t=1e-5` : +0.00053168844197261588901 ;
- `t=1e-7` : +0.00053168844856340010005.

Les deux valeurs convergent vers la dérivée analytique +0.0005316884485640592444. Le premier jet est annulé par construction ; le second ne l'est pas. **NO-GO circonscrit** pour la conservation de la densité radiale complète par cette seule variation de KG dans cette famille à coefficients restants figés. D'autres paramètres/champs peuvent compenser ; aucune incompatibilité physique universelle démontrée.

## Reproduction et limites

Construire `rho_g` avec les expressions du script de provenance, remplacer `KG=Rational('.0012')` par `KG=symbols('KG')`, puis calculer `a1=diff(rho_g,s).subs(s,0)`, `a2=diff(rho_g,s,2).subs(s,0)/2` et leurs dérivées directionnelles `D`. Pour un contrôle indépendant, utiliser `mpmath.diff` imbriqué avec `mp.dps=60` et différences finies centrées `(a2(t)-a2(-t))/(2*t)`.

Les valeurs sont des dérivées ponctuelles du modèle algébrique prescrit, non des certificats d'intervalle. Tests du runner b3c3d9 : SKIP ; pilote : SKIP ; cellules physiques évaluées/certifiées/inconclusives : **0/0/0**. La commande `git ls-remote https://github.com/alexandrebarault-arch/Janus.git HEAD` a échoué dans ce conteneur avec `Could not resolve host: github.com` ; les sources ont été consultées via le connecteur GitHub. Ne pas confondre ce blocage CLI avec une absence d'accès au dépôt.

**NEXT_ACTION_EXACT :** transférer les 18 modules authentiques et dépendances historiques JANUS-001, vérifier `git hash-object`, exécuter `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v`, puis `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`. Ensuite tester la liberté des jets radiaux, contraintes Dirac et deux vrais bords.

**GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**
