# JANUS-006 — stratification exacte de Fz et perte de rang (2026-11-20)

Source authentifiée : `numerics/hr_step45_exact_physical_ward.py`, blob lu au HEAD initial `160d6e993ccc46397b7bc18c5b80f2a975115708`. Le modèle définit `D=psg*Sgr-Lg*plgr+pg*tgr` et `K=m2*Mg2*Lg*Lf*At`, `At=b1*Sg²+2*b2*Sg*Sf+b3*Sf²`. À `|z|<1`, `Fz=D-K*z/sqrt(1-z²)`.

**Branche régulière K≠0.** La fonction `z/sqrt(1-z²)` est une bijection strictement croissante de (-1,1) vers R. Donc Fz=0 possède exactement une racine `z=sign(K)*D/sqrt(D²+K²)`. Le mineur `partial_z Fz=-K/(1-z²)^(3/2)` est non nul ; le théorème des fonctions implicites fixe localement z en fonction de D,K. Ce résultat n'impose aucune condition de bord ni la fermeture de Dirac.

**Strate K=0.** Alors Fz=D, indépendante de z. Si D≠0, aucune racine ; si D=0, tout |z|<1 satisfait Fz, et le mineur en z est nul. Attention : cela ne prouve pas un degré de liberté physique supplémentaire, car les autres contraintes peuvent fixer z ou éliminer la strate. La formule de racine régulière ne doit jamais être prolongée à D=K=0 ; la limite dépend de la direction d'approche. En particulier, un calcul de rang de Dirac qui divise par At ou K perd cette strate et doit expliciter son domaine.

**Contrôle exécuté** : Python 3, SymPy 1.14.0, `python /tmp/janus_shift.py` PASS ; substitution exacte pour K>0 et K<0, dérivée et cas K=0. Contrôle indépendant : monotonie analytique de la bijection et limites aux extrémités. Le script local était :

```python
import sympy as s
D,K,z=s.symbols('D K z',real=True)
F=D-K*z/s.sqrt(1-z*z)
for sign in [1,-1]:
 k=s.symbols('k',positive=True)
 Z=sign*D/s.sqrt(D**2+k**2)
 assert s.simplify(F.subs({K:sign*k,z:Z}))==0
 assert s.simplify(s.diff(F,z).subs(K,sign*k)+sign*k/(1-z*z)**s.Rational(3,2))==0
assert s.simplify(F.subs(K,0)-D)==0
print('PASS')
```

**Portée** : identité algébrique Step45, pas une cellule Step55/58 ni une preuve de rang Dirac complet. Tests b3c3d9 SKIP, pilote SKIP ; cellules physiques demandées/tentées/évaluées/certifiées/inconclusives : 0/0/0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

**NEXT_ACTION_EXACT** : étudier les solutions physiques et le rang de `(Hg,Hf,C_exact,Fz)` séparément sur K≠0 et sur K=D=0, puis vérifier les deux vraies traces de bord et l'holonomie. Pour JANUS-001, reconstruire les imports authentifiés et exécuter neuf tests puis pilote.
