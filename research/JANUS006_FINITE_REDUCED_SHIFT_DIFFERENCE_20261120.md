# JANUS-006 — différence finie exacte des Hamiltoniens réduits en z (2026-11-20)

Source canonique au HEAD f9a9df9a459978adbee07361f939fab8dd582321 : numerics/hr_step45_exact_physical_ward.py, blob 66aa43841dccfe4a5d586a49be9c10af3a67a10e. Hypothèses : Lg,Lf non nuls, |z|<1 ; les autres coordonnées canoniques, leurs jets, At et D sont fixés, et pLg' est éliminé par Fz=0. Cette carte algébrique n'impose pas l'intégrabilité radiale ni les deux bords.

Les dérivées réduites déjà démontrées donnent, par intégration exacte de z/(1-z²)^(3/2),

Hg_red(z)-Hg_red(0)=m2*Mg2*Lf*At*(1/sqrt(1-z²)-1),
Hf_red(z)-Hf_red(0)=m2*Mg2*Lg*At*(1/sqrt(1-z²)-1).

Si m2*Mg2*Lf*At et m2*Mg2*Lg*At sont non nuls, aucune valeur z non nulle avec |z|<1 ne conserve séparément les mêmes valeurs des deux Hamiltoniens que z=0 **sur cette tranche figée**. La différence finie est paire en z, strictement de signe du préfacteur pour z non nul. À z=0, les dérivées premières s'annulent mais les dérivées secondes valent respectivement m2*Mg2*Lf*At et m2*Mg2*Lg*At ; un jacobien du premier ordre seul manque cette obstruction finie. Lg*Hg_red-Lf*Hf_red reste constant en z. **Aucun NO-GO physique** : At peut s'annuler, les autres champs peuvent varier, et la contrainte complète de Dirac/holonomie/bords reste ouverte.

## Reproduction exécutée (Python, SymPy 1.14.0)

```python
import sympy as s
z,Lg,Lf,m2,mg,At=s.symbols('z Lg Lf m2 mg At',real=True)
q=1/s.sqrt(1-z*z)-1
for lapse in (Lf,Lg):
 f=m2*mg*lapse*At*q
 assert s.simplify(s.diff(f,z)-m2*mg*lapse*At*z/(1-z*z)**s.Rational(3,2))==0
 assert s.simplify(f.subs(z,0))==0
print('PASS')
```

Contrôle analytique indépendant : dérivée de (1-z²)^(-1/2) égale z(1-z²)^(-3/2) ; pour 0<|z|<1, sqrt(1-z²)<1. Calcul symbolique PASS, preuve physique non effectuée. Tests b3c3d9 SKIP, pilote SKIP ; cellules physiques demandées/tentées/évaluées/certifiées/inconclusives = 0/0/0/0/0.

**NEXT_ACTION_EXACT :** réduire C_exact et les Hamiltoniens à partir de la source Step45 authentifiée ; calculer le jacobien conjoint sur variations radialement intégrables, vérifier les deux traces de bord. JANUS-001 : transférer les dépendances historiques authentifiées Step45/46/55/58, comparer les blobs Git, lancer neuf tests puis pilote à une cellule. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
