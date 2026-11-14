# JANUS-005 — Wfbar prescrit : restriction du noyau algébrique (2026-11-14)

**HEAD source fixé :** `eff739a3411300fb2c33a40b5970acb522b0bf83`. **Statut : résultat algébrique conditionnel, pas de preuve de rang physique.** Source originale inspectée : `numerics/hr_step55_global_barrier.py`, blob Git `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, fonction `geometry(s)`; `numerics/hr_step55_normalized_secondary.py`, blob `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, substitution `d['Wf']:r*r*Wfbar`.

## Hypothèse testée
Le contre-exemple algébrique du rapport `JANUS005_EXTENDED_TRACE_KERNEL_COUNTEREXAMPLE_20261114.md` utilise une variation libre `dw=-num_U-rho*den_U` à `dU=1,dV=0`. Cette variation est-elle disponible **dans la famille Step55 à paramètres géométriques et sources prescrits fixés** ?

## Source et calcul
La fonction `geometry(s)` fixe exactement
`Wfbar=M2*MG*(Lf*Tf+Lg*T*sqrt(1-Z1**2*s))`,
avec `Tf=B2*Lg**2+2*B3*Lg*Lf+B4*Lf**2` et `T=B1*Lg**2+2*B2*Lg*Lf+B3*Lf**2`. Les facteurs `Lg,Lf` sont prescrits par `A,B,CG,CF,s` et ne dépendent pas de la variable inconnue `U`. Ainsi, à `s,M2,MG,A,B,CG,CF,B_i,Z1` fixés, **`dWfbar/dU=0`**. Il n'est donc pas permis de choisir `dw` indépendamment pour annuler `d rho` dans cette sous-famille.

Contrôle Python/SymPy exécuté :
```python
import sympy as S
M,Lg,Lf,Tf,T,z,R,U=S.symbols('M Lg Lf Tf T z R U')
w=M*(Lf*Tf+Lg*T*R)
assert S.diff(w,U)==0
assert S.simplify(S.diff(w,M)-(Lf*Tf+Lg*T*R))==0
```
PASS 2/2. Contrôle supplémentaire sur les expressions rationnelles du rapport précédent : `den=b+k*s*u/(2*m*t)`, `num=u**2/(4*m*l)-u*(v-s*d/l)/(2*m*t)-m*l**3*rf/2+s*z*d/l+w`, `rho=-num/den`. Au point rationnel `(u,v,w,b,k,s,m,t,l,d,z,rf)=(1,2,3,1,1,1,1,2,1,0,0,0)`, SymPy donne `den=5/4`, `rho_U=11/25` et `dw_required=11/20`. Donc la direction `dU=1,dV=0` n'annule **pas** `d rho` lorsque `dw=0`. PASS 3/3 vérifications rationnelles.

## Verdict limité
**NO-GO circonscrit :** le noyau du contre-exemple antérieur, fondé sur `dw` libre, n'est pas une variation de la famille Step55 à paramètres prescrits fixés. Le contre-exemple reste correct sur l'espace algébrique étendu ; il ne doit pas être effacé. **Aucune conclusion** pour les variations physiques où `M2`, `Z1`, la géométrie, les sources ou les données de bord peuvent changer : dans ce cas `dw` est induit par leur différentielle totale et non choisi librement. L'exemple rationnel est une vérification algébrique et **n'est pas** une cellule physique JANUS.

**NEXT_ACTION_EXACT :** calculer la différentielle totale de `Wfbar` par rapport aux paramètres admissibles de `geometry(s)`, en particulier `M2`, puis confronter cette variation induite à `-num_U-rho*den_U` et aux équations Step45/46/49/55 et aux deux vrais bords. JANUS-001 : reconstruire les modules authentiques, neuf tests, pilote une cellule.

Tests moteur nouveaux : 0 ; cellules physiques évaluées : 0 ; certifiées : 0. **GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**
