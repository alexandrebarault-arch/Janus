# JANUS-005 — extension rationnelle de la boîte Z1 au 14 novembre 2026

**Source fixée :** main b933f9f4df2d67a95f9c963bfdcc7bf6d51028bd. **Résultat :** preuve algébrique conditionnelle, aucune certification physique.

## Hypothèse et test falsifiable
Dans la carte prescrite Step55, à constantes géométriques et M2 positives fixées, vérifier J=det(d(Wfbar,Dbar)/d(M2,Z1))<0 pour tout s dans [0,289/400] et Z1 dans [-9/50,9/50]. Une borne supérieure Qhi >= 0 invaliderait cette preuve (sans nécessairement réfuter le signe).

Source authentifiée : numerics/hr_step55_global_barrier.py (blob a6e7004120d0a166a3a8973c2fbe1487a8eb70fe). Script précédent : research/repro/janus005_one_box_rational_sign_20261114.py (blob 09ef33f702321d99886ef00d64df3c18ccd153a2). Rejeu local du script **octet pour octet**, git hash-object 09ef33f702321d99886ef00d64df3c18ccd153a2, PASS. Le présent élargissement est une substitution rationnelle nouvelle, non un calcul physique.

## Preuve
A=2/5, Y=0.5787707228025044, B=A*Y, cg=0.0015, cf=-0.0012, b2=-4.2383993109, b3=13.6801214252, b4=-38.5117901844 (toutes décimales traitées comme fractions exactes).
smax=289/400, zmax=9/50.
Lg0=A, Lg1=A*(1+cg*smax)^2, Lf0=B*(1+cf*smax)^2, Lf1=B.
Tlo=Lg0^2+2*b2*Lg1*Lf1+b3*Lf0^2.
Thi=Lg1^2+2*b2*Lg0*Lf0+b3*Lf1^2.
Tfhi=b2*Lg0^2+2*b3*Lg1*Lf1+b4*Lf0^2.
Qhi=Lf0*Tfhi+Lg1*Thi*(1+smax*zmax^2).

Monotonie terme à terme : T>=Tlo>0, T<=Thi, Tf<=Tfhi<0, et Q=Lf*Tf+Lg*T*sqrt(1-Z1^2*s)*(1+s*Z1^2)<=Qhi<0. Radicande >= 1-smax*zmax^2 = 0.976591 >0. La formule exacte du déterminant Step55 est J=M2*MG^2*Lg*Lf*T*Q/(1-Z1^2*s)^(3/2), donc J<0 sur la boîte entière.

Contrôle Python exact : Fraction, assertions Tlo>0, Tfhi<0, Qhi<0 et radicande>0 : PASS. Affichages décimaux **non utilisés pour la décision** : Tlo≈0.10397953086758126, Tfhi≈-0.19593238750389178, Qhi≈-0.00004021437439038968. Contrôle contradictoire : la condition suffisante Qhi<0 n'est pas démontrée pour Z1 au-delà de sqrt((-Lf0*Tfhi/(Lg1*Thi)-1)/smax)≈0.1834641572 ; aucune extrapolation au-delà.

## Commandes reproductibles
```bash
python research/repro/janus005_one_box_rational_sign_20261114.py
python - <<'PY'
from fractions import Fraction as F
A=F('0.4'); B=A*F('0.5787707228025044'); s=F('0.7225'); z=F(9,50)
cg=F('0.0015'); cf=F('-0.0012')
b2=F('-4.2383993109'); b3=F('13.6801214252'); b4=F('-38.5117901844')
g0=A; g1=A*(1+cg*s)**2; f0=B*(1+cf*s)**2; f1=B
tlo=g0**2+2*b2*g1*f1+b3*f0**2
thi=g1**2+2*b2*g0*f0+b3*f1**2
tfhi=b2*g0**2+2*b3*g1*f1+b4*f0**2
qhi=f0*tfhi+g1*thi*(1+s*z*z)
assert tlo>0 and tfhi<0 and qhi<0 and 1-s*z*z>0
print('PASS', float(qhi))
PY
```

**Limites :** carte algébrique à coefficients prescrits ; M2/Z1 ne sont pas prouvés physiquement indépendants. Pas de test Dirac, lapses, deux vrais bords, dynamique 4D ou observables. Cellules physiques Step55/58 évaluées/certifiées/inconclusives : 0/0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

**NEXT_ACTION_EXACT :** reconstruire et authentifier les dépendances JANUS-001, neuf tests puis pilote une cellule ; JANUS-005 déterminer les tangentes admissibles M2/Z1/PG selon Step45/49/55 et les deux vrais bords/Dirac. Ne pas élargir encore Z1 sans pertinence physique.
