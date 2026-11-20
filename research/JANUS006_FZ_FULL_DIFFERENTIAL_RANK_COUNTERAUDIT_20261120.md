# JANUS-006 — Contre-audit du rang complet de Fz (2026-11-20)

Source authentifiée : `numerics/hr_step45_exact_physical_ward.py` au HEAD `51b572004a626f041275c16940a33dcd0d657559`.

Posons `D=pSg*Sg_r-Lg*pLg_r+pg*tg_r`, `K=m2*Mg2*Lg*Lf*At`, `Fz=D-K*z/sqrt(1-z²)`, avec `|z|<1`.

**Rectification scientifique :** le mineur `partial_z Fz=-K/(1-z²)^(3/2)` s'annule sur `K=0`, mais le rang de la différentielle *complète* de `Fz` ne chute pas nécessairement. Sur `K=D=0`, `dFz=dD-z/sqrt(1-z²)*dK`. À jets indépendants, `partial_(pLg_r)Fz=-Lg`, donc pour `Lg!=0`, le jacobien à une ligne de Fz garde le rang 1. L'élimination locale de `pLg_r` reste valide, tandis que celle de `z` échoue. La « perte de rang » du rapport précédent est exclusivement celle du mineur de shift, pas celle de la contrainte complète.

**Contrôle SymPy exécuté** :
```python
import sympy as s
D,K,z,Lg,p=s.symbols('D K z Lg p',real=True)
F=D-K*z/s.sqrt(1-z*z)
print(s.diff(F,z),s.diff(F,D),s.diff(F,K))
print(s.Matrix([[s.diff(F,D),s.diff(F,K),s.diff(F,z)]]).subs({D:0,K:0}).rank())
print(s.Matrix([[-Lg,s.diff(F,z)]]).subs({K:0,D:0}).rank())
```
Rang `(D,K,z)` = 1 sur la strate ; rang `(pLg_r,z)` = 1 sous `Lg!=0` : PASS. Contre-vérification analytique indépendante par coefficient affine `-Lg` : PASS.

Portée : jets ambiants uniquement ; aucun rang conjoint Dirac, holonomie, deux bords ni liberté physique supplémentaire démontrés. Tests b3c3d9 et pilote SKIP ; cellules physiques demandées/tentées/évaluées/certifiées/inconclusives 0/0/0/0/0.

**NEXT_ACTION_EXACT :** calculer les mineurs du jacobien conjoint `(Hg,Hf,C_exact,Fz)` sur `K!=0` et `K=D=0` sans diviser par K, puis holonomie et deux vrais bords. JANUS-001 : reconstruire dépendances authentiques Step45/46/55/58, neuf tests puis pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
