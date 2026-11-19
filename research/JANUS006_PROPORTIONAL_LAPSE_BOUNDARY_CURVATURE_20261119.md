# JANUS-006 — obstruction de fermeture sur une tranche de lapses proportionnels (2026-11-19)

**Portée : contre-exemple algébrique sur espace ambiant de jets de bord ; PAS un NO-GO physique.** Source examinée au HEAD `ac0e9a2631ac59d017ab9079f5c210264cd7e22f` : `numerics/hr_step68ad_b3c3d2_full_dirichlet_boundary.py`, blob `6898c88760cc0766e949f9bade4908b9bc176c58`. La source donne le coefficient de `dp` de la forme de bord non intégrée par parties : `theta_p=-z*(N+M*Lg/Lf)-V*Lg` avec `z=Z=D/sqrt(D²+K²)` après stationnarité du shift. `D` ne dépend pas du moment `p` (il dépend notamment de `pr`).

## Hypothèses et résultat exact

Fixer `Lg,Lf,V,D,K`, les autres jets et paramètres ; permettre à `N>0` et `p` de varier et imposer `M=rho*N` avec `rho>0` constant. Prendre `K>0` et `D≠0`, donc `Z≠0` constant sur cette tranche. La forme de bord restreinte vaut `theta= [-Z*N*(1+rho*Lg/Lf)-V*Lg] dp` ; elle n'a pas de composante `dN` dans la forme originale. Par conséquent,

`d theta = -Z*(1+rho*Lg/Lf) dN wedge dp ≠ 0`.

Le témoin rationnel `Z=3/5, rho=1, Lg=2, Lf=3` donne `(d theta)_{N,p}=-1`. Une intégration autour du rectangle `[N0,N1]×[p0,p1]` donne `-Z*(1+rho*Lg/Lf)*(N1-N0)*(p1-p0)`. Même lorsque `dZ=0` (donc `dP wedge dZ=0`), la fermeture à lapses fixés ne s'étend pas automatiquement à cette tranche de lapses proportionnels. La proportionnalité positive seule ne suffit pas.

## Contrôle indépendant exécuté

Python 3, SymPy 1.14.0 ; commande `python /tmp/janus_boundary_countercheck.py` : différentiation symbolique, simplification identique à zéro de `curvature+Z*(1+rho*Lg/Lf)`, contrôle indépendant par circulation exacte autour du rectangle, témoin rationnel `-1` : **PASS**. Script local utilisé :

```python
import sympy as s
N,p,rho,Lg,Lf,Z,V=s.symbols('N p rho Lg Lf Z V', positive=True)
q=1+rho*Lg/Lf
thp=-Z*N*q-V*Lg
assert s.simplify(s.diff(thp,N)+Z*q)==0
N0,N1,p0,p1=s.symbols('N0 N1 p0 p1')
circ=s.expand((thp.subs(N,N1)-thp.subs(N,N0))*(p1-p0))
assert s.simplify(circ+Z*q*(N1-N0)*(p1-p0))==0
assert s.diff(thp,N).subs({Z:s.Rational(3,5),rho:1,Lg:2,Lf:3,V:0})==-1
```

**Limites cruciales :** source lue via connecteur GitHub, non exécutée intégralement dans ce cycle ; la transcription réduite ci-dessus est vérifiable mais n'est pas un rejeu octet-authentifié de la source. Les contraintes de Dirac, la stationnarité complète, les deux vrais bords et la régularité globale peuvent interdire cette tranche tangentielle. Ne pas en déduire une obstruction physique. Aucun test moteur b3c3d9, aucune cellule Step55/58 exécutée ou certifiée. `GATE_2B=OPEN` ; `JANUS_R=NOT_VALIDATED`.

**NEXT_ACTION_EXACT :** construire le jacobien total des contraintes canoniques et des deux vrais bords, puis déterminer si une direction `dN∧dp` admissible subsiste après restriction à son noyau ; ne pas inférer ce noyau de la seule proportionnalité `M=rho N`. JANUS-001 : reconstruire les imports historiques octet-authentifiés avant tests et pilote.
