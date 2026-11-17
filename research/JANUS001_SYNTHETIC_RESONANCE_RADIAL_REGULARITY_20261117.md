# JANUS-001 — transfert de régularité du contre-exemple logarithmique vers la variable radiale (2026-11-17)

## Portée
Contrôle mathématique **synthétique**, sans substitution des sources physiques Step55/58, sans Dirac ni conditions aux deux vrais bords. Il complète le contre-exemple publié le 2026-11-16 ; ce n'est pas une obstruction établie pour JANUS.

## Hypothèses et construction
Pour s>0, c>0 et C,u0 réels, considérer
`U(s)=u0+s^4(C+(c/2)log(s))`.
Elle vérifie exactement `2s U_s=8(U-u0)+c s^4`. La variable radiale de l'ansatz est `s=r^2` et `pLf(r)=r^2 U(r^2)`, d'où, pour r≠0,
`pLf(r)=u0 r^2+C r^10+c r^10 log|r|`.
On prolonge la partie logarithmique par 0 en r=0.

## Vérification indépendante et verdict limité
Les dérivées radiales d'ordre k≤9 du terme `r^10 log|r|` tendent vers 0 en r→0 des deux côtés, tandis que la dérivée d'ordre 10 contient `10! log|r|` et diverge vers -∞. Ainsi `pLf∈C^9` mais `pLf∉C^{10}` si c≠0. En revanche `U∈C^3` mais `U∉C^4` en s=0. Le changement s=r² **décale l'ordre de régularité** : il serait incorrect de conclure directement que pLf n'est pas C4 parce que U n'est pas C4.

Commande exécutée (Python 3, SymPy 1.14.0) :
```python
import sympy as s
r,c,C,u0=s.symbols('r c C u0',real=True,nonzero=True)
p=r**2*(u0+r**8*(C+c*s.log(r**2)/2))
for k in [8,9,10]:
    d=s.expand(s.diff(p,r,k))
    print(k,s.simplify(d),s.limit(d,r,0,dir='+'))
```
Résultats : limites k=8 et 9 égales à 0 ; à k=10, `-oo*sign(c)` (c>0 donc -∞). Le contrôle analytique bilatéral découle de la parité de `r^10 log|r|` et des limites de ses dérivées.

## Conséquence pour la recherche
Aucune cellule physique b3c3d9 exécutée ou certifiée : 0/0/0. Avant d'inférer une perte de régularité d'un champ physique ou de la géométrie, évaluer le véritable coefficient `G_U(0,U0)` et le forcing Step55, puis propager le développement vers **chaque variable géométrique** et son ordre de dérivation requis. La régularité d'un champ reparamétré ne suffit pas à établir celle de la métrique ni celle des contraintes temporelles.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
