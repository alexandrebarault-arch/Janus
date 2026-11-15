# JANUS-001 — Recursion des jets centraux et resonances Step55 (2026-11-15)

**Source:** equation Step55 examinee au HEAD `f879adfe7713c0d0b88318a3a6294ad4cb813a26` : `2*s*U_s=G(s,U)-2*U`. Ceci est une consequence symbolique **conditionnelle** de cette equation, pas une verification de la fonction G du depot ni un certificat physique. **GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**

## Derivation exacte

Poser `u_k=(d^k U/ds^k)(0)`, `g_{ij}=(partial_s^i partial_U^j G)(0,u_0)`, avec G et U au moins C3 pres du centre. Deriver l'equation 0, 1, 2 et 3 fois, puis evaluer s=0 :

```text
g00 = 2*u0
(4-g01)*u1 = g10
(6-g01)*u2 = g20 + 2*g11*u1 + g02*u1^2
(8-g01)*u3 = g30 + 3*g21*u1 + 3*g12*u1^2 + g03*u1^3
                 + 3*(g11+g02*u1)*u2
```

Ces identites ont ete controlees par differentiation SymPy 1.14.0 de `2*s*diff(U(s),s)-G(s,U(s))+2*U(s)` jusqu'a l'ordre 3, avec coefficients 4,6,8 verifies independamment par le developpement de Taylor `U=sum(u_k*s^k/k!)`.

## Criteres falsifiables / contre-exemples

Si `g01=4` et `g10 != 0`, aucune solution C1 ne satisfait l'ODE au centre. Si `g01=4` et `g10=0`, u1 n'est pas determine par la seule equation d'ordre 1 : il faut des contraintes supplementaires. Meme principe pour `g01=6` au second jet et `g01=8` au troisieme, avec le membre droit correspondant. Ces resonances sont des conditions **necessaires** et ne prouvent ni existence globale ni non-existence d'une solution moins reguliere.

Contre-exemple explicite a l'inference abusive de non-existence en resonance : `G(s,U)=2*u0+4*(U-u0)` donne `U(s)=u0+c*s` pour tout c, avec `g01=4,g10=0`. A l'inverse `G(s,U)=2*u0+4*(U-u0)+s` impose `0=1` a l'ordre 1 : pas de solution C1 au centre.

## Reproduction

```python
import sympy as sp
s=sp.symbols('s')
U=sp.Function('U')(s)
G=sp.Function('G')(s,U)
F=2*s*sp.diff(U,s)-G+2*U
for k in range(4):
    print(k, sp.diff(F,s,k).subs(s,0))
```

**Limites:** pas de valeur de `g01` calculee depuis le G authentique, pas de test Step45/46/58, pas de certification d'intervalle, pas de condition Dirac ou aux deux vrais bords. Tests b3c3d9 SKIP, pilote SKIP, cellules physiques evaluees/certifiees/inconclusives 0/0/0.

**NEXT_ACTION_EXACT:** calculer `G_U(0,U0)` et les membres droits des trois recurrences a partir de `numerics/hr_step55_global_barrier.py` authentifie au HEAD fixe, puis verifier les ecarts a 4,6,8 par calcul exact ou intervalles. Reprendre transfert authentifie des sources JANUS-001 et lancer neuf tests et pilote ; si toujours bloque, JANUS-005/006 Dirac et vrais bords.
