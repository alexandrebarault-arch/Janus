# JANUS-001 — résonances centrales à tout ordre (15 novembre 2026)

**Portée : théorème formel conditionnel, pas une preuve sur le G physique.** On suppose G(s,U) analytique près de (0,u0), G(0,u0)=2u0, et une solution U(s)=u0+Σ_{n≥1}u_n s^n analytique. Dans 2sU'=G(s,U)-2U, le coefficient de s^n vaut

(2(n+1)-a)u_n = R_n(u0,...,u_{n-1}), avec a=∂_U G(0,u0),

où R_n est le coefficient de s^n de G(s,u0+Σ_{k<n}u_k s^k) (le terme linéaire a u_n en est exclu). Preuve : le membre gauche apporte 2n u_n ; -2U apporte -2u_n au membre droit ; le seul terme de G dépendant de u_n à cet ordre est a u_n. Ainsi les résonances possibles de la récurrence formelle sont a=2(n+1), n≥1, soit 4,6,8,10,... . À résonance, R_n=0 est nécessaire, et u_n reste non fixé à cet ordre. Hors résonance, u_n est déterminé récursivement. Cela ne démontre ni convergence de la série ni existence d'une solution globale.

**Contre-épreuve exacte SymPy** : choisir G=2u0+a(U-u0)+c s^4. Pour U=u0+u1 s+...+u4 s^4, les cinq coefficients de 2sU'-G+2U sont [0,(4-a)u1,(6-a)u2,(8-a)u3,(10-a)u4-c]. À a=10, c≠0, aucune solution C^4 au centre ne satisfait l'équation ; à a=10, c=0, u4 est libre au niveau de la récurrence. À a=11, u4=-c. Le contrôle a été exécuté sous Python/SymPy dans la session ; ces G sont des modèles analytiques de contrôle et non le G physique JANUS.

**Commande de reproduction** :
```python
import sympy as S
x,a,u0,c=S.symbols('x a u0 c')
U=u0+sum(S.Symbol('u'+str(i))*x**i for i in range(1,5))
G=2*u0+a*(U-u0)+c*x**4
R=S.expand(2*x*S.diff(U,x)-G+2*U)
print([S.factor(R.coeff(x,i)) for i in range(5)])
```

**Limites et action** : la valeur a=G_U(0,u0) de Step55 authentique n'a pas été calculée. L'absence de résonance à tous les ordres exige a∉{4,6,8,...}; même dans ce cas, la convergence et la validité physique restent à démontrer. Reprendre l'évaluation exacte de G_U à partir de normalized_symbolic(), puis les tests et le pilote authentiques, et JANUS-005/006 Dirac et bords. Cellules physiques évaluées/certifiées/inconclusives : 0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
