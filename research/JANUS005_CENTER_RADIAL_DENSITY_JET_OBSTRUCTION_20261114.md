# JANUS-005 — dérivée radiale au centre de la tangente compensée (2026-11-14)

Source fixée : `790b8eaaeebfee5601e5d75689551ed29cdbb497`. Formule de `Rhog(s)` et paramètres repris de `numerics/hr_step55_global_barrier.py` (blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`), conformément au rapport `research/JANUS005_RADIAL_CG_COMPENSATION_COUNTERCHECK_20261114.md`.

## Hypothèse réfutable

La tangente à paramètres `(A,M2,Z1,CG)` qui préserve `PG,U0,rho_g(0)` peut-elle aussi préserver le **premier jet radial** `d rho_g/ds |_(s=0)` à `Y,CF,KG,b_i` fixés ?

Définir `C=3*b1*Y+3*b2*Y**2+b3*Y**3` et l'opérateur directionnel
`D=partial_A - (4*A**3*M2*C+9/10)/(A**4*C)*partial_M2 - (Z1/A)*partial_Z1 - (CG/A)*partial_CG`.
Appliquer `D` à la formule originale `Rhog(s)` du module Step55.

## Calcul exécuté

Python 3 + SymPy 1.14.0, à partir de la retranscription exacte des expressions de `geometry(s)` du module Step55, avec constantes rationnelles décimales de la source. Commande réellement exécutée : `python /mnt/data/janus_audit/check.py` (script local non encore publié, donc la reproduction autonome nécessite la retranscription ci-dessous).

Le script construit `ug=1+CG*s`, `uf=1+CF*s`, `Lg=A*ug**2`, `Lf=A*Y*uf**2`, `Sgr=A*ug*(1+5*CG*s)`, `T=b1*Lg**2+2*b2*Lg*Lf+b3*Lf**2`, `T0=2*b1*Lg*Lf+b2*Lf**2`, `root=sqrt(1-Z1**2*s)`, `Dbar=M2*Lg*Lf*T*Z1/root`, `Wgbar=M2*(Lg*T0+Lf*T*root)`, `Rg=-48*CG/(A**2*ug**5)`, `Gmom=PG*(1+5*CG*s/2)`, `Gprime=2*PG*(1+5*CG*s)`, `fac=Gmom/(2*Lg*Sgr)`, `betag=sqrt(1+KG**2*s)+s*fac*KG*Lg` et `Rhog=-(Gmom**2/(4*Lg)-fac*(s*Dbar+Lg*Gprime)-Lg**3*Rg/2+s*Z1*Dbar/Lg+Wgbar)/betag`, avec `PG=-2*A**2*sqrt(3/(10*A**3)+M2*C/3)`.

SymPy calcule `D(Rhog.subs(s,0))` et `D(diff(Rhog,s).subs(s,0))`, puis substitue `A=.4, M2=23.3348939346, Z1=.004, CG=.0015, Y=.5787707228025044, CF=-.0012, KG=.0012, b1=1, b2=-4.2383993109, b3=13.6801214252`.

Résultats :
- `D Rhog(0) = 0` exactement (contrôle symbolique).
- `D (d Rhog/ds)(0) = -0.08612850795005535994645936` (évaluation SymPy 25 chiffres de l'expression analytique).
- Prédiction linéaire à `s=0.1` : `-0.00861285079500554`, proche du calcul non linéaire ponctuel indépendant précédent `-0.008611882626807962`. La différence est attendue à l'ordre `s²`.

## Verdict et limites

**NO-GO circonscrit :** à coefficients Step55 restants fixés, la tangente compensée ne préserve pas même le premier jet radial de la densité g, malgré la conservation exacte de sa valeur centrale. C'est une obstruction au maintien du **profil imposé** et non une obstruction physique tant que le profil radial n'est pas démontré comme une donnée fixe. Le coefficient est une évaluation analytique au point de référence, non un certificat sur un intervalle de paramètres, ni une contrainte de Dirac. Les équations aux deux vrais bords, lapses et dynamique 4D ne sont pas traitées.

Tests physiques b3c3d9 : non exécutés. Cellules physiques évaluées/certifiées/inconclusives : 0/0/0.

**NEXT_ACTION_EXACT :** identifier dans Step45/46 les conditions de bord et le statut de la variation de `Rhog'(0)`; dériver les contraintes linéarisées de Dirac sur les champs radiaux autorisés. Pour JANUS-001 : reconstruire les imports et sources historiques authentiques avant de relancer tests et pilote.

GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
