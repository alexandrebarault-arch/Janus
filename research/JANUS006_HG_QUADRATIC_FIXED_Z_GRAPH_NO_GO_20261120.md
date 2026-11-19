# JANUS-006 — Obstruction quadratique Hg sur le graphe compensateur fixe-Z (2026-11-20)

## Sources authentifiées
HEAD initial main `766fbb5def84a0b7ab29dea1b9263adbb97e920d`. Sources lues : `numerics/hr_step45_exact_physical_ward.py` (Hamiltonien Hg), `numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py` (forme de bord), et `research/JANUS006_FIXED_Z_RADIAL_JET_COMPENSATION_20261119.md` (graphe). Contrôle indépendant sur les expressions explicitement transcrites, **pas** un rejeu du moteur complet.

## Question falsifiable
Le graphe de compensation du rapport précédent, qui rend `dTheta=0` et conserve `D,Z`, peut-il conserver aussi `Hg=0` pour un intervalle non trivial de la variable canonique `p=pLg`, **si tous les autres champs et jets restent figés** (sauf `Sgr` et `plgr` compensés) ?

## Calcul exact
Dans le Hamiltonien original Step45, `Hg=Ag-Dr(Bg)`, les termes dépendant de `p,Sgr,plgr`, après fixation de `D=psg*Sgr-Lg*plgr+pg*tgr=D0` et `z=Z0`, sont
```
Hg = Lg*p**2/(4*mg*Sg**2) - p*psg/(2*mg*Sg)
     + mg*Sgr**2/Lg - 2*mg*Sg*Sgr*Lgr/Lg**2
     + z*D0/Lg + [termes indépendants de p,Sgr].
```
Les termes omis incluent `2*mg*Sg*Sg2/Lg`, poussière, potentiel et constante de courbure, tous fixes sur cette tranche. Le graphe précédent impose `M=rho*N`, `q=1+rho*Lg/Lf`, `Sgr=h0+c*p`, `c=z*q*Lg/(2*mg*Sg)`, `plgr=(psg*Sgr+pg*tgr-D0)/Lg`. Ainsi le coefficient de `p²` est exactement
```
a2 = Lg/(4*mg*Sg**2) + mg*c**2/Lg
   = Lg*(1+z**2*q**2)/(4*mg*Sg**2).
```
Pour `Lg>0,mg>0,Sg>0`, `a2>0`, indépendamment de `psg,Lgr,D0,h0`. Par conséquent `Hg(p)` ne peut être identiquement nul sur aucun intervalle ouvert de `p` sur **ce graphe à autres jets figés**. Un éventuel zéro ponctuel ne suffit pas. Cela invalide la lecture du graphe comme famille finie de solutions `Hg=0` à paramètres restants figés.

## Exécution et contre-vérification
Python 3 / SymPy 1.14.0, exécution locale `python /tmp/janus006_hg.py` PASS : expansion et identification symbolique de `a2`, seconde dérivée `d²Hg/dp²=2*a2` PASS ; seconde différence finie exacte `[Hg(1)+Hg(-1)-2Hg(0)]/2=a2` PASS pour un témoin rationnel, `a2=160973/9316125`. Script reproduisible :
```python
import sympy as s
p,ps,Lg,Sg,Lgr,Sg2,mg,z,D0,N,M,Lf,h0=s.symbols('p ps Lg Sg Lgr Sg2 mg z D0 N M Lf h0')
q=1+M*Lg/(N*Lf)
c=z*q*Lg/(2*mg*Sg)
h=h0+c*p
Hg=Lg*p**2/(4*mg*Sg**2)-p*ps/(2*mg*Sg)+mg*h**2/Lg+2*mg*Sg*Sg2/Lg-2*mg*Sg*h*Lgr/Lg**2+z*D0/Lg
a2=Lg*(1+z*z*q*q)/(4*mg*Sg**2)
assert s.simplify(s.diff(Hg,p,2)-2*a2)==0
```

## Portée et limites
**NO-GO circonscrit au graphe fini fixe-Z, avec les autres champs/jets fixés et la contrainte originale Hg=0 imposée sur un intervalle de p.** Il ne réfute pas la tangence infinitésimale à Hg=0 en un point : la dérivée première peut s'annuler par choix de données. Il n'exclut pas une compensation plus large via Sg2, autres jets ou champs, ni une solution complète de Dirac et des deux vrais bords. Il ne démontre ni la fermeture ni la non-fermeture sur l'espace physique admissible. Tests b3c3d9 et pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives : 0/0/0.

**NEXT_ACTION_EXACT :** calculer `dHg/dp` sur le graphe à un point de coquille, puis tester simultanément `dHf`, `dC_red`, `dFz` et les traces des deux vrais bords, avec les variations des jets libres. Si des compensations supplémentaires existent, établir leur rang et leur admissibilité plutôt que généraliser ce NO-GO. JANUS-001 reste BLOCKED jusqu'au transfert authentifié Step45/46/55/58, neuf tests puis pilote.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
