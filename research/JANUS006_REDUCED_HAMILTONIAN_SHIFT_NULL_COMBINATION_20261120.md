# JANUS-006 — Combinaison hamiltonienne insensible au shift réduit (2026-11-20)

Source canonique authentifiée au HEAD `548352a4587f4a2dad1686127ba715585625ddd3` : `numerics/hr_step45_exact_physical_ward.py`, blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. Référence antérieure : `research/JANUS006_REDUCED_SHIFT_CHAIN_RULE_20261120.md`.

## Proposition exacte et portée

Dans la carte de jets canoniques avec Lg,Lf non nuls et |z|<1, fixer les autres jets et paramètres et éliminer `plgr` par `Fz=0` : `plgr*=D/Lg-m2*mg*Lf*At*z/sqrt(1-z²)`. Les identités originales donnent `∂z Hg=Fz/Lg`, `∂z Hf=Fz/Lf`, `∂plgr Hg=-z`, `∂plgr Hf=-z*Lg/Lf`. Par règle de chaîne, `∂z Hg_red=m2*mg*Lf*At*z/(1-z²)^(3/2)` et `∂z Hf_red=m2*mg*Lg*At*z/(1-z²)^(3/2)`. Donc **`∂z (Lg*Hg_red-Lf*Hf_red)=0`**. En fait les mêmes dérivées à jets fixés montrent que `Lg*Hg-Lf*Hf` est indépendant à la fois de z et de plgr, avant réduction, sur cette carte (Lg,Lf fixés lors des dérivées). Cela n'implique pas `Hg=Hf=0` et ne donne pas le rang du système de Dirac. La colonne z du jacobien réduit des deux Hamiltoniens a la direction `(Lf,Lg)` et ne fournit qu'une direction scalaire ; une combinaison transverse ne peut fixer z. Si At*z=0 elle peut s'annuler entièrement. La dérivée radiale des profils, C_exact et les deux vrais bords restent à imposer.

## Contrôle reproductible exécuté

```bash
python - <<'PY'
import sympy as s
z,Lg,Lf,m2,mg,At,D,p=s.symbols('z Lg Lf m2 mg At D p',nonzero=True,real=True)
root=s.sqrt(1-z*z)
F=D-Lg*p-m2*mg*Lg*Lf*At*z/root
ps=D/Lg-m2*mg*Lf*At*z/root
hg=s.simplify((F/Lg).subs(p,ps)-z*s.diff(ps,z))
hf=s.simplify((F/Lf).subs(p,ps)-z*Lg/Lf*s.diff(ps,z))
assert s.simplify(Lg*hg-Lf*hf)==0
print(s.__version__,hg,hf,'COMBINATION_PASS')
PY
```

Exécution réelle : SymPy 1.14.0, `COMBINATION_PASS`. Contre-contrôle analytique indépendant : `Lg*(Fz/Lg)-Lf*(Fz/Lf)=0` et `Lg*(-z)-Lf*(-z*Lg/Lf)=0`, sans substitution, ce qui prouve directement l'indépendance de la combinaison en z et plgr. **Ce résultat est une conséquence structurelle des identités déjà établies, pas une nouvelle preuve de viabilité ni un NO-GO.** Aucun calcul physique Step55/58 exécuté ; cellules évaluées/certifiées/inconclusives 0/0/0.

**NEXT_ACTION_EXACT :** depuis les expressions authentiques `exact_physical_ward()['Hg']`, `['Hf']`, `['C_exact']`, substituer `plgr*`, former les dérivées de `(Hg_red,Hf_red,C_exact_red)` par rapport aux jets intégrables et vérifier si la combinaison indépendante de z est compatible avec le noyau conjoint, puis les deux véritables traces de bord. JANUS-001 : transférer/authentifier les dépendances Step45/46/55/58 avant tests et pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
