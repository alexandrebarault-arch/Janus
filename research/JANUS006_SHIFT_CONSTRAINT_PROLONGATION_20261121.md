# JANUS-006 — prolongement exact de la contrainte de shift (21 novembre 2026)

## Source et statut
Lecture GitHub de `main` au SHA `626a9ff117999c5651fc195ab56ccd4aba4fcfea`, `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. La source définit exactement `Fz=Dg-interaction*z/sqrt(1-z*z)`, `Dg=pSg*Sgr-Lg*pLgr+pg*tgr`, `interaction=m2*Mg2*Lg*Lf*At`. L'algèbre ci-dessous est exécutée indépendamment en SymPy sur cette expression lue ; le module complet Step45 n'a pas été importé dans l'environnement de calcul. Il ne s'agit pas d'un rejeu authentifié de tout Step45, ni d'une preuve de Dirac.

Poser `D=Dg`, `K=interaction`, `f(z)=z/sqrt(1-z²)` et `|z|<1`. Alors `Fz=D-K*f(z)` et les prolongements holonomes imposent :

`D_r Fz = D' - K'*z/sqrt(1-z²) - K*z'/(1-z²)^(3/2) = 0`.

`D_r² Fz = D'' - K''*z/sqrt(1-z²) - 2*K'*z'/(1-z²)^(3/2) - 3*K*z*(z')²/(1-z²)^(5/2) - K*z''/(1-z²)^(3/2) = 0`.

Sur la strate `K≠0`, cette seconde équation détermine formellement `z''` en fonction de `D'',K'',z,z',K'`. Le coefficient exact est `∂(D_r²Fz)/∂z''=-K/(1-z²)^(3/2)`. Sur la strate `K=0`, le coefficient disparaît ; il est **interdit** de diviser par K. Si simultanément `z=0`, Fz=0 impose D=0, et D_r Fz=0 impose D'=0 (sans déterminer z' par cette équation). Les dérivées `D''` comportent des jets d'ordre supérieur des variables canoniques, notamment ceux de `pLg`; les tenir fixes n'est pas une réduction Dirac.

## Contrôle exact effectué
Commande Python/SymPy effectivement exécutée :

```python
import sympy as s
z,K,D,zr,zrr,z3,Kr,Krr,Dr,Drr=s.symbols('z K D zr zrr z3 Kr Krr Dr Drr',real=True)
F=D-K*z/s.sqrt(1-z*z)
def der(e):
    return (s.diff(e,z)*zr+s.diff(e,zr)*zrr+s.diff(e,zrr)*z3+
            s.diff(e,K)*Kr+s.diff(e,Kr)*Krr+s.diff(e,D)*Dr+s.diff(e,Dr)*Drr)
F1=s.simplify(der(F)); F2=s.simplify(der(F1))
assert s.simplify(s.diff(F1,zr)+K/(1-z*z)**s.Rational(3,2))==0
assert s.simplify(s.diff(F2,zrr)+K/(1-z*z)**s.Rational(3,2))==0
assert s.diff(F2,z3)==0
```

Les dérivations symboliques et le coefficient ci-dessus ont été obtenus ; les trois assertions sont une transcription reproductible des identités calculées, pas une prétention à l'exécution de ce bloc exact dans cette session. Contrôle indépendant : règle de chaîne `f'= (1-z²)^(-3/2)`, `f''=3z(1-z²)^(-5/2)`.

## Portée contradictoire
Le rapport antérieur `JANUS006_SHIFT_SECOND_JET_COMPATIBILITY_20261121.md` établit conditionnellement `∂R/∂z''=-4*Sg²*Mg2*q/(Lg*(1+q²*z²))`. Les deux coefficients non nuls ne démontrent **aucune** incompatibilité : les deux équations peuvent fixer le même jet et la seconde peut contraindre les jets canoniques d'ordre supérieur. Le test falsifiable suivant est d'éliminer `z''` entre `R=0` et `D_r²Fz=0` après substitution des relations holonomes, puis de tester la compatibilité avec `Hg,Hf,C_exact`, la matrice de Dirac, les lapses et les deux véritables traces de bord. Attention aux strates `K=0` et `z=0`.

JANUS-001 : tests b3c3d9 SKIP ; pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives 0/0/0. **GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**
