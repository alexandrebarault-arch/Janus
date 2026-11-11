# JANUS-005 — Différentielle totale de la reconstruction f au bord (2026-11-11)

**Provenance :** `scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs` au HEAD `06445e214f4ff3511648222a84af9fd53d3f6ba1`. Calcul local SymPy 1.14.0, Python 3.13, à rayon extérieur **fixe** `R=17/20`. Résultat algébrique, **pas** une solution des contraintes physiques.

Notations : `s=R²`, `T=Sfr`, `m=mf`, `L=Lf`, `k=kf`, `b=beta`, `D=Dbar`, `w=Wfbar`, `rf=Rf`, `z=z1`, `den=b+k*s*U/(2*m*T)` et
`num=U²/(4*m*L)-U*(V-s*D/L)/(2*m*T)-m*L³*rf/2+s*z*D/L+w`.
On suppose `m,L,T,den != 0`. Alors `rho=-num/den`, `pf=s*rho`, `pSf=R*(L*V-s*D-s*k*L*rho)/T`.

## Identité exacte : variation complète

Pour `x=(b,D,w,rf,z,m,L,T,k)` et une famille différentiable, à R fixé :
```
dpf/dlambda = H*s*Udot + chi*R*Vdot + sum_x (partial_x pf)*xdot
dpSf/dlambda = (L/T)*R*Vdot - (R*k*L/T)*dpf/dlambda
               + sum_x [partial_x pSf + (R*k*L/T)*partial_x pf]*xdot
```
où `H=partial_U rho`, `chi=R*U/(2*m*T*den)`. Les dérivées partielles sont prises avec toutes les autres variables indépendantes fixées. **La deuxième somme est indispensable** : elle contient notamment les variations directes de `L/T`, `D`, `k`, `T`, etc. Elle n'est pas égale en général à zéro.

Quelques contributions exactes vérifiées :
```
partial_w pf = -s/den
partial_rf pf = s*m*L³/(2*den)
partial_b pf = -pf/den
partial_D pf = -s²*(U/(2*m*T)+z/L)/den
partial_z pf = -s²*D/(L*den)
partial_w pSf = R*s*k*L/(T*den)
partial_rf pSf = -R*s*k*m*L⁴/(2*T*den)
partial_D pSf = -R*s/T - (R*k*L/T)*partial_D pf
```
Ces termes sont exacts sans hypothèse de signe ou de petitesse des variations géométriques.

## Contrôle indépendant et portée

Un script local SymPy a reconstruit `num,den,rho,pf,pSf` à partir de la source JS et testé **8 identités symboliques exactes PASS** : les deux chaînes totales, les quatre dérivées en `w,rf`, la dérivée en `b` et celle en `D` de `pSf`. La sortie console annonçait par erreur « 7 assertions » ; le comptage effectif du script est huit. Aucune cellule physique Step55/58 n'a été exécutée.

**Conséquence :** le signe conditionnel de `dpf/dlambda` issu de `H*s*Udot+chi*R*Vdot` ne peut être promu à une dérivée totale sans prouver que la somme géométrique s'annule (ou la borner). Même une borne de H ne suffit pas si les coefficients varient. Cette identité ne prouve ni qu'ils varient réellement ni qu'ils sont libres sous les contraintes JANUS.

**NEXT_ACTION_EXACT :** inspecter les sources authentiques de la famille Step49/55 pour établir `xdot` (ou leur nullité) sous contraintes au vrai bord ; si la famille fixe réellement `x`, expliciter la portée du tangent partiel. Ensuite seulement borner la différentielle totale et confronter les conditions aux deux vrais bords. JANUS-001 : reconstruction des sources et pilote physique toujours en attente. **GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**
