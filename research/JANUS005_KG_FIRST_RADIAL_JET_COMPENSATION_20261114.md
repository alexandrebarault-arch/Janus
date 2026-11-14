# JANUS-005 — Sensibilité du premier jet de poussière au paramètre KG (2026-11-14)

## Provenance et reproduction
HEAD source: `04faee8ece2377e3407ad1af296dc0fc6c2f3194`. Source authentifiée : `research/repro/janus005_center_radial_density_jet_20261114.py`, blob Git `bdb3eaabb2bd9afea3ec8856134920fde1d5c51d`. Script transféré sans modification puis exécuté sous Python 3.13 / SymPy 1.14.0 : `python jet.py` PASS, `git hash-object jet.py` retourne le même blob. Résultats : `D rho_g(0)=0` et `D rho'_g(0)=-0.08612850795005535994645936`. Ce sont des calculs ALGÉBRIQUES, non des cellules physiques.

## Nouvelle dérivation indépendante
Dans le script Step55, `betag(s)=sqrt(1+KG**2*s)+s*fac(s)*KG*Lg(s)`, avec `fac(0)=PG/(2*A**2)`, `Lg(0)=A`. Ainsi `betag(0)=1` et `betag'(0)=KG**2/2+PG*KG/(2*A)`. Comme `rho_g(s)=-N(s)/betag(s)`, et que le numérateur N ne dépend pas de KG, on obtient **exactement**
```
partial_KG rho_g'(0) = -rho_g(0) * (KG + PG/(2*A)).
```
Pour la famille prescrite, `rho_g(0)=9/10-24*A*CG`. À `A=0.4, CG=0.0015, KG=0.0012, M2=23.3348939346, Z1=0.004`, les calculs SymPy donnent `PG=-0.76351100925088392437` et `partial_KG rho'_g(0)=+0.8441439672407285042776946`. Si l'on **autorise** une variation supplémentaire de KG, l'équation linéarisée `D rho'_g(0) + (partial_KG rho'_g(0))*dKG/dA=0` admet `dKG/dA=+0.1020305910987973552154485`. Le coefficient n'est pas nul au point étudié.

## Interprétation et limites
La non-conservation du premier jet radial par la tangente à KG fixé n'est donc **pas** une obstruction universelle lorsque KG est un paramètre ajustable. Ceci est une compensation infinitésimale d'une seule donnée locale. Ni la liberté physique de KG, ni la conservation du profil radial entier, ni les contraintes de Dirac, ni les deux vrais bords ne sont démontrés. Aucun calcul de cellule Step55/58, aucune certification physique. Le nouveau calcul est une dérivation analytique évaluée avec SymPy, et non un nouveau test moteur.

## NEXT_ACTION_EXACT
1. Auditer dans Step45/49/55 la nature de KG (donnée de jauge, donnée libre, ou imposée), puis insérer la tangente élargie dans les contraintes de Dirac linéarisées et les deux vrais bords.
2. JANUS-001 : reconstruire les imports authentiques et les sources historiques, comparer chaque blob, puis exécuter `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v` et `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
