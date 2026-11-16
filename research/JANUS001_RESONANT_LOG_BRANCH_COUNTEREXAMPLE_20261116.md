# JANUS-001 — Résonance centrale : branche logarithmique explicite (2026-11-16)

**Portée : contre-exemple analytique générique, NON évaluation du G physique Step55.**

Considérons l'ODE centrale `2s U'(s)=G(s,U)-2U`, avec `G(s,U)=2u0+10(U-u0)+c s^4`, où `c>0`, `s>0`. Au centre `G(0,u0)=2u0` et `G_U(0,u0)=10`, soit la résonance n=4 de la récurrence déjà prouvée dans `research/JANUS001_ALL_ORDER_CENTRAL_RESONANCES_20261115.md`.

**Solution exacte :** `U(s)=u0+s^4(C+(c/2)log(s))` pour tout C réel. En effet, `2sU'-G+2U=0` identiquement. Elle se prolonge en `C^3` au centre en posant `U(0)=u0`, avec dérivées d'ordres 1,2,3 nulles ; pour c non nul la dérivée d'ordre 4 diverge logarithmiquement, donc pas de solution `C^4` sur cette branche. Le terme homogène `C s^4` ne peut éliminer le logarithme. La compatibilité `R_4=0` est donc une véritable condition de régularité dans ce modèle témoin, et non seulement une indétermination de coefficient.

**Contrôle indépendant exécuté localement :** Python/SymPy, commande ci-dessous ; sortie `residual=0`, limites des dérivées 0..3 égales à `u0,0,0,0` et limite de la dérivée 4 égale à `-oo` pour c>0.

```python
import sympy as s
x,c,u0=s.symbols('x c u0',positive=True)
U=u0+c*s.Rational(1,2)*x**4*s.log(x)
G=2*u0+10*(U-u0)+c*x**4
print('residual=',s.simplify(2*x*s.diff(U,x)-G+2*U))
for k in range(5):
    print(k,s.limit(s.diff(U,x,k),x,0,dir='+'))
```

**Contradiction recherchée :** ceci ne prouve PAS que Step55 est en résonance, ni qu'il existe une obstruction physique. Le G ci-dessus est un témoin synthétique. Pour appliquer ce diagnostic à JANUS, calculer authentiquement `G_U(0,U0)` puis, si la valeur atteint un entier pair résonant, calculer exactement le terme de compatibilité `R_n`. Le fait qu'une branche non analytique existe pour le témoin n'est pas une validation physique. Tests b3c3d9 SKIP ; pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives : 0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

**NEXT_ACTION_EXACT :** transférer Step45/46/55/58 authentiques et dépendances, vérifier chaque blob Git par `git hash-object`, calculer `G_U(0,U0)`, lancer `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d9_annular_direct_enclosure.py' -v` puis le pilote `PYTHONPATH=. python -m numerics.hr_b3c3d9_annular_direct_enclosure --cells 256 --max-cells 1 --out /tmp/janus_b3c3d9_pilot.json`. Si transfert toujours bloqué, poursuivre JANUS-005/006 Dirac et deux vrais bords.
