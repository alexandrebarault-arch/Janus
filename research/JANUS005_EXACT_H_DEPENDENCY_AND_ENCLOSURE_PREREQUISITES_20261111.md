# JANUS-005 — Identité exacte de H et données nécessaires à sa certification (2026-11-11)

**Source figée :** main `596a5d67043774522c9ec80d1dfac80a75664385`; `scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs`, blob `7615cdb1624748dac56ab1d969c401b258f8cdaa`. **Statut :** audit algébrique exact du jacobien, pas un calcul Step55 ni une certification du H physique.

## Identité et contrôle

Noter `s=R², m=mf, L=Lf, T=Sfr, k=kf, b=beta, D=Dbar, w=Wfbar, rf=Rf, z=z1`. Le code définit

`den=b+k*s*U/(2*m*T)`,

`numer=U²/(4*m*L)-U*(V-s*D/L)/(2*m*T)-m*L³*rf/2+s*z*D/L+w`,

`rho=-numer/den`, et `H=-(dnum+rho*dden)/den` avec `dnum=partial_U numer`, `dden=partial_U den` (V et géométrie fixés).

Par élimination exacte de rho :

```
H = [-4*D*b*m*s + 4*D*k*m*s²*z - 2*L⁴*k*m²*rf*s
     + 4*L*V*b*m + 4*L*k*m*s*w - 4*T*U*b*m - U²*k*s]
    / (8*L*T*m²*den²).
```

Deux dérivées partielles exactes, à autres variables fixées :

`partial_w H = k*s/(2*m*T*den²)` et `partial_V H = b/(2*m*T*den²)`.

**Exécution réelle :** Python SymPy, `sympy.cancel(H-H_explicit)==0`, `sympy.cancel(diff(H,w)-k*s/(2*m*T*den**2))==0`, `sympy.cancel(diff(H,V)-b/(2*m*T*den**2))==0` : **3 PASS, 0 FAIL**. Contrôle exact supplémentaire à `U=-1/200,V=1/10,s=289/400,m=1/100,L=2/5,T=1/5,k=-1/625,b=1,D=1/100,rf=z=0` : `H(w=0)=844393062500/40115683521`, `H(w=1)=832833062500/40115683521`; différence `-11560000000/40115683521` (PASS). Les paramètres de ce contrôle sont **illustratifs, non physiques**.

## Conclusion contradictoire et portée

Si `k*s != 0` et `m*T*den != 0`, la valeur de H varie avec `w` lorsque les autres arguments formels sont fixés. Il est donc **impossible de déduire une borne finie sur H des seules bornes de U,V,chi,dP,dQ**, sans bornes supplémentaires sur les variables géométriques et sources (au minimum w, ou une identité physique qui l'élimine). Ce n'est PAS une preuve que w soit libre dans le modèle physique : les équations de contrainte peuvent le corréler aux autres données. Les contre-exemples numériques ne sont pas des solutions JANUS.

**NEXT_ACTION_EXACT :** rechercher dans les sources Step45/46/55 les expressions authentiques de `Wfbar,Dbar,Rf,z1,beta,mf,Lf,Sfr,kf` au bord `R=17/20`, établir leurs dépendances/corrélations sur la famille paramétrique et certifier `den != 0`; encloser ensuite H et calculer `dpf=H*dP+chi*dQ` et `dpSf=(Lf/Sfr)*dQ-(R*kf*Lf/Sfr)*dpf`. Ne pas substituer des valeurs illustratives comme preuve physique. JANUS-001 : reconstruire les sources authentifiées puis exécuter le pilote.

**Tests Step55/58 de cette session : 0 ; cellules physiques évaluées : 0 ; certifiées : 0. GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.**
