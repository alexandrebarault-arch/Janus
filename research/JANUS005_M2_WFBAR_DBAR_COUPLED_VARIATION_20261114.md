# JANUS-005 — Variation couplée Wfbar / Dbar sous M2 (2026-11-14)

**Source figée :** main `ca111a4d37d65933747fc1b17e31731b7fefcf32`; `numerics/hr_step55_global_barrier.py`, blob Git `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, fonction `geometry(s)`. **Portée : identité exacte dans une sous-famille prescrite, pas une perturbation physique complète.**

## Hypothèse falsifiable

Le noyau algébrique du rapport `JANUS005_EXTENDED_TRACE_KERNEL_COUNTEREXAMPLE_20261114.md` fait varier `Wfbar` en gardant les autres coefficients, notamment `Dbar`, fixes. Peut-on réaliser cette variation par `M2` seul, avec `MG,Lg,Lf,T,Tf,Z1,s` fixes et `M2>0` ?

La source donne, en notant `R=sqrt(1-Z1**2*s)` :
```
Wfbar = M2*MG*(Lf*Tf + Lg*T*R)
Dbar = M2*MG*Lg*Lf*T*Z1/R
```
D'où les identités **exactes** `partial_M2(Wfbar)=Wfbar/M2` et `partial_M2(Dbar)=Dbar/M2`. Sur le domaine `Dbar != 0`, la condition `dDbar=0` avec `M2` seule variable impose `dM2=0`, puis `dWfbar=0`. **NO-GO conditionnel :** le contre-exemple à `dw != 0` et `dDbar=0` n'est pas engendré par une variation isolée de M2 dans cette sous-famille. Cela ne tranche pas les variations conjointes de géométrie, Z1, PG, les contraintes ou les bords.

Autre identité exacte à `M2,MG,Lg,Lf,T,Tf,s` fixes : `partial_Z1(Wfbar)=-s*Dbar/Lf`. Elle montre une variation induite, **pas** la liberté de choisir `dw` indépendamment.

## Rejeu SymPy exact

```python
import sympy as S
m,mg,lf,lg,tf,t,z,x=S.symbols('m mg lf lg tf t z x', positive=True)
r=S.sqrt(1-z*z*x)
w=m*mg*(lf*tf+lg*t*r)
d=m*mg*lg*lf*t*z/r
assert S.simplify(S.diff(w,m)-w/m)==0
assert S.simplify(S.diff(d,m)-d/m)==0
assert S.simplify(S.diff(w,z)+x*d/lf)==0
```

Exécution locale réelle : **3/3 PASS**, SymPy, sur les expressions de `geometry(s)`. Contrôle contradictoire : si `Dbar=0` (par exemple `Z1=0` ou `T=0`), l'argument d'injectivité via `Dbar` ne fonctionne plus ; ces cas sont explicitement exclus du NO-GO. De plus, lorsque M2 varie physiquement, PG et les autres traces peuvent varier : aucune conclusion de rang Dirac n'en découle.

**Tests moteur nouveaux : 0 ; cellules physiques évaluées : 0 ; certifiées : 0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**

**NEXT_ACTION_EXACT :** construire le jacobien total de `(Wfbar,Dbar,Rhog,Psg)` par rapport aux paramètres réellement libres de Step45/46/49/55, y compris PG et géométrie, puis imposer les deux vrais bords et les contraintes de Dirac ; JANUS-001 : reconstruire et authentifier les sources, neuf tests, pilote à une cellule.
