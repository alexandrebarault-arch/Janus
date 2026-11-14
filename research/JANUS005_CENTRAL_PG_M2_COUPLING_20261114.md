# JANUS-005 — Contrainte centrale PG–M2 (2026-11-14)

Source : `numerics/hr_step55_global_barrier.py` au HEAD `c31312ba7be9081f453a561cc6d2137bc778f1df`. Domaine : famille initiale prescrite, autres paramètres fixés, branche PG négative, H2>0.

Poser A=2/5, Y=0.5787707228025044, B=A Y, MF=0.10879548725², et C=b0+3b1Y+3b2Y²+b3Y³, où (b0,b1,b2,b3)=(0,1,-4.2383993109,13.6801214252). H2=0.9/(3A³)+M2 C/3 ; PG=-2A² sqrt(H2) ; U0=MF B(PG/A-2Z1).

**Identités exactes :** dPG/dM2=-A² C/(3sqrt(H2))=PG C/(6H2), dU0/dM2=(MF B/A)dPG/dM2, dU0/dZ1=-2MF B, dPG/dZ1=0. Par conséquent PG et M2 ne sont pas indépendants sur cette famille prescrite si C≠0 ; une variation de M2 à PG fixe est impossible à géométrie fixée.

**Exécution :** Python/SymPy, constantes décimales en Rational ; simplify(dPG-PG*C/(6*H2)) == 0 PASS. Valeurs à M2=23.3348939346 : C=0.12925217432668358184 ; H2=5.6928619262431968510 ; PG=-0.76351100925088392437 ; dPG/dM2=-0.0028891577835134484013 ; dU0/dM2=-0.000019792450960027962047 ; dU0/dZ1=-0.0054804763029477050342. Contrôle contradictoire : C>0, H2>0 et donc dPG/dM2<0, sans supposer l'indépendance de PG.

Reproduction :
```python
import sympy as s
A=s.Rational(2,5); Y=s.Rational('0.5787707228025044'); M=s.Rational('23.3348939346'); B=A*Y
b=[s.Rational(x) for x in ['0','1','-4.2383993109','13.6801214252']]
C=b[0]+3*b[1]*Y+3*b[2]*Y**2+b[3]*Y**3
H=s.Rational('0.9')/(3*A**3)+M*C/3
PG=-2*A**2*s.sqrt(H); dPG=-A**2*C/(3*s.sqrt(H))
MF=s.Rational('0.10879548725')**2
assert s.simplify(dPG-PG*C/(6*H))==0
assert C>0 and H>0 and dPG<0
for x in [C,H,PG,dPG,MF*B/A*dPG,-2*MF*B]: print(s.N(x,20))
```

**Portée limitée :** ce calcul n'établit ni le rang Dirac ni les deux conditions aux vrais bords ni la dynamique 4D. Aucune cellule physique b3c3d9 évaluée/certifiée (0/0), aucun nouveau test moteur. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

**NEXT_ACTION_EXACT :** intégrer la différentielle de PG à la carte tangentielle Step45/49/55 puis filtrer par les deux bords et Dirac. JANUS-001 : transférer les 18 modules authentifiés et fichiers de provenance, comparer git hash-object, exécuter neuf tests puis pilote une cellule.
