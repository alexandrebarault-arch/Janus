# JANUS-006 — rang 3 des contraintes (Hg,Hf,Fz) sur jets seconds ambiants — 2026-11-20

## Provenance et hypothèses
Source canonique `numerics/hr_step45_exact_physical_ward.py`, blob Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, HEAD initial `2c692d2d0f258e67c2545ddbc8306760a5d16610`. Définitions exactes : `Hg=Ag-d_r Bg`, `Hf=Af_full-d_r Bf`, `Fz=psg*Sgr-Lg*plgr+pg*tgr-m2*Mg2*Lg*Lf*At*z/sqrt(1-z²)`. `Bg=-2*Mg2*Sg*Sgr/Lg+z*pLg`, `Bf=-2*Mf2*Sf*Sfr/Lf+z*Lg*pLg/Lf`. Les densités Ag et Af_full ne contiennent pas les seconds jets. Variables ambiantes indépendantes `(Sgrr,Sfrr,plgr)`, avec `Lg,Lf,Sg,Sf,Mg2,Mf2` non nuls, et `|z|<1`.

## Mineur exact et résultat
Par dérivation directe des expressions de Step45 :
```
             Sgrr             Sfrr             plgr
Hg        2 Mg2 Sg/Lg          0                -z
Hf             0          2 Mf2 Sf/Lf       -z Lg/Lf
Fz             0               0                -Lg
```
D'où `det = -4*Mg2*Mf2*Sg*Sf/Lf`. Ce déterminant est indépendant de z, K=m2*Mg2*Lg*Lf*At et des valeurs des contraintes. Il est non nul sous les hypothèses. Ainsi le jacobien ambiant de (Hg,Hf,Fz) possède **rang 3**, y compris sur z=0 et K=0, dans le domaine régulier. Le rang 1 observé pour les seules colonnes (plgr,z) n'est donc pas une perte de rang de ces trois contraintes dans l'espace de tous les jets.

## Contrôle et contre-audit
Commande réellement exécutée dans Python/SymPy :
```python
import sympy as s
mg,mf,Sg,Sf,Lg,Lf,z,K=s.symbols('mg mf Sg Sf Lg Lf z K',nonzero=True)
J=s.Matrix([[2*mg*Sg/Lg,0,-z],[0,2*mf*Sf/Lf,-z*Lg/Lf],[0,0,-Lg]])
print(s.factor(J.det()))
```
Sortie exacte : `-4*Sf*Sg*mf*mg/Lf`. Vérification indépendante : matrice triangulaire, produit des trois éléments diagonaux. PASS.

## Portée scientifique / limitations
Il s'agit du **rang dans l'espace ambiant des jets**, et non du rang du système de Dirac sur les profils holonomes, ni d'un théorème d'existence global. Les seconds jets Sgrr et Sfrr sont des dérivées de profils et ne peuvent pas être ajustés librement point par point lors d'un problème aux deux bords. La quatrième contrainte `C_exact` n'est pas incluse ; Step45 affirme qu'elle ne contient pas de seconds jets, mais sa différentielle sur les autres coordonnées doit être étudiée. Aucun test des lapses, de la dynamique 4D, de la stabilité ni des observables. Tests b3c3d9 SKIP, pilote SKIP ; cellules physiques demandées/tentées/évaluées/certifiées/inconclusives = 0/0/0/0/0.

**NEXT_ACTION_EXACT :** calculer un mineur 4×4 de (Hg,Hf,Fz,C_exact) en ajoutant une colonne canonique indépendante aux trois jets, puis imposer l'holonomie et les deux véritables conditions de bord. Si le mineur s'annule, analyser ses facteurs et ses strates sans divisions injustifiées. JANUS-001 reste à reconstruire authentiquement avant tests/pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
