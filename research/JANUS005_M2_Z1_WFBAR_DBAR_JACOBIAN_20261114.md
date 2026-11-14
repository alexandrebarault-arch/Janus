# JANUS-005 — Jacobien exact (M2,Z1) des coefficients Wfbar/Dbar (2026-11-14)

**Source authentique :** `numerics/hr_step55_global_barrier.py`, blob Git `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, fonction `geometry(s)`, HEAD initial `a48a825aeb2651cf6626ca672e22ce04159f6d49`. **Portée :** jacobien algébrique à `MG,Lg,Lf,T,Tf,s` fixés, et non tangent physique admissible.

Poser `r=sqrt(1-Z1**2*s)>0`, `m=M2`, `g=MG`, `a=Lf`, `b=Lg`, `t=T`, `u=Tf`, `z=Z1`, `x=s`. Les sources originales donnent
```
W = m*g*(a*u+b*t*r)
D = m*g*b*a*t*z/r
```
Le déterminant exact est
```
det(d(W,D)/d(m,z)) =
 m*g**2*b*a*t*(a*u+b*t*r*(1+x*z**2))/r**3
```
Le terme `1+x*z**2` ne peut être omis. Ainsi, sur `m,g,a,b,t,r != 0`, la carte locale (m,z)->(W,D) est inversible si et seulement si `a*u+b*t*r*(1+x*z**2) != 0`. C'est un test algébrique **conditionnel**, pas une preuve de liberté physique de m ou z.

**Contrôle exact au centre s=0** avec les constantes décimales *rationnelles exactes* de Step55 (`A=.4`, `Y=.5787707228025044`, `B=A*Y`, `B1=1`, `B2=-4.2383993109`, `B3=13.6801214252`, `B4=-38.5117901844`, `M2=23.3348939346`, `MG=1`): `T=0.108221332359334984...` strictement positif, `Lf*Tf+Lg*T=-0.00499853487086803544...` strictement négatif, donc `det=-0.00116892856241697110...` strictement négatif au centre. Le signe est établi par comparaisons rationnelles exactes, les décimales sont indicatives. **Aucune extrapolation du signe sur l'anneau ni aux deux vrais bords**.

## Commande réellement exécutée (Python/SymPy)
```python
import sympy as S
m,g,a,b,t,u,z,x=S.symbols('m g a b t u z x',real=True)
r=S.sqrt(1-z*z*x)
w=m*g*(a*u+b*t*r); d=m*g*b*a*t*z/r
j=S.Matrix([w,d]).jacobian([m,z]).det()
f=m*g*g*b*a*t*(a*u+b*t*r*(1+x*z*z))/r**3
assert S.simplify(j-f)==0
assert S.simplify(j.subs(x,0)-m*g*g*b*a*t*(a*u+b*t))==0
A=S.Rational(2,5); Y=S.Rational('0.5787707228025044'); B=A*Y
B1=1; B2=S.Rational('-4.2383993109')
B3=S.Rational('13.6801214252'); B4=S.Rational('-38.5117901844')
Lg=A; Lf=B
T=B1*Lg**2+2*B2*Lg*Lf+B3*Lf**2
Tf=B2*Lg**2+2*B3*Lg*Lf+B4*Lf**2
assert T>0 and Lf*Tf+Lg*T<0
```
**Résultat :** deux identités symboliques PASS, deux comparaisons rationnelles PASS. Contrôle contradictoire : le déterminant s'annule si `a*u=-b*t*r*(1+x*z**2)` (avec les autres facteurs non nuls), donc une inversion universelle n'est pas démontrée. Les paramètres `M2,Z1` peuvent être contraints par Friedmann, le centre, Dirac et les deux bords ; aucun de ces filtres n'a été résolu.

**Tests moteur nouveaux : 0 ; cellules physiques Step55/58 évaluées : 0 ; certifiées : 0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**

**NEXT_ACTION_EXACT :** établir à partir de Step45/49/55 les variations admissibles de `M2,Z1,PG` et de la géométrie, puis appliquer le jacobien total aux traces et aux deux vrais bords ; poursuivre JANUS-001 uniquement après transfert authentifié de toutes les dépendances, puis neuf tests et pilote une cellule.
