# JANUS-006 — Dérivée de décalage après élimination exacte de Fz (2026-11-20)

HEAD source fixé : `97376ea0798c1b737a50c2cd5a597e9b5e402d2b`. Source authentifiée : `numerics/hr_step45_exact_physical_ward.py`, fonction `exact_physical_ward()`. Hypothèses : Lg,Lf non nuls, |z|<1, différentiabilité, paramètres et autres jets fixés dans la dérivée partielle. On note `D=psg*Sgr+pg*tgr` et `At=beta1*Sg**2+2*beta2*Sg*Sf+beta3*Sf**2`.

La source donne exactement `Fz=D-Lg*plgr-m2*mg*Lg*Lf*At*z/sqrt(1-z**2)`, ainsi que les identités Ward `partial_z Hg=Fz/Lg` et `partial_z Hf=Fz/Lf` à jets canoniques fixés. La construction `Hg=Ag-d_r Bg`, `Hf=Af-d_r Bf` donne directement `partial_plgr Hg=-z` et `partial_plgr Hf=-z*Lg/Lf`.

Après élimination `plgr_star=D/Lg-m2*mg*Lf*At*z/sqrt(1-z**2)`, la règle de chaîne **ne permet pas** de remplacer la dérivée en z de Hg/Hf par zéro : `partial_z Hg_reduced=(partial_z Hg)|Fz=0-z*partial_z plgr_star`, et de même pour Hf avec le facteur Lg/Lf. Ainsi :

- `partial_z Hg_reduced=m2*mg*Lf*At*z/(1-z**2)**(3/2)`;
- `partial_z Hf_reduced=m2*mg*Lg*At*z/(1-z**2)**(3/2)`.

Ces expressions ne sont généralement pas nulles. **Résultat circonscrit :** la stationnarité Ward à jets fixés ne peut pas être interprétée comme la stationnarité en z de la fonction réduite après substitution de la solution de Fz. Il ne s'agit ni d'une nouvelle équation de contrainte ni d'un NO-GO physique. Le calcul est local dans l'espace des jets ; intégrabilité radiale, Dirac, C_exact et les deux véritables bords ne sont pas résolus.

## Reproduction exacte

Python/SymPy (exécuté dans la session) :
```python
import sympy as s
z,Lg,Lf,m2,mg,At,D,p=s.symbols('z Lg Lf m2 mg At D p',nonzero=True,real=True)
root=s.sqrt(1-z*z)
pstar=D/Lg-m2*mg*Lf*At*z/root
F=D-Lg*p-m2*mg*Lg*Lf*At*z/root
for a in (1/Lg,1/Lf):
    derivative=s.simplify((a*F).subs(p,pstar)+(-z*Lg*a)*s.diff(pstar,z))
    expected=s.simplify(m2*mg*Lf*At*z*Lg*a/(1-z*z)**s.Rational(3,2))
    assert s.simplify(derivative-expected)==0
print("PASS")
```
Résultat PASS pour Hg et Hf. Contrôle analytique indépendant : `d[z/sqrt(1-z**2)]/dz=(1-z**2)**(-3/2)`, puis règle de chaîne. La source Step45 a été lue au HEAD fixé ; pas de replay intégral du module source dans cette session.

Tests b3c3d9 SKIP, pilote SKIP, cellules physiques demandées/tentées/évaluées/certifiées/inconclusives 0/0/0/0/0.

**NEXT_ACTION_EXACT :** calculer les contraintes réduites `Hg,Hf,C_exact` avec les expressions canoniques complètes ; former le jacobien holonome conjoint et ses deux vraies traces de bord, sans confondre les dérivées partielles à jets fixes avec les dérivées de la sous-variété Fz=0. JANUS-001 : authentifier Step45/46/55/58, neuf tests puis pilote.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
