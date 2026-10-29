# b3c3d6 — écran exact de compatibilité centrale pour une annulation partielle du symbole Step57 (29 octobre 2026)

**Portée strictement restreinte :** géométrie prescrite Step55, carte stationnaire `Fz=0`, `K>0` pour `0<r<=R=17/20`, deux coefficients du symbole *smeared* Step57 (`eta''*M` et `eta''*N'`), et sous-famille supplémentaire `M(r)=1`, `N(R)=M(R)=1`. Le coefficient Step57 `eta''*N` n'est **pas** annulé ni même évalué ici ; le résultat ne concerne donc **pas** l'annulation du symbole complet, et encore moins le Step58 original, la tangence Dirac ou un no-go physique.

Sur Step55, `c_M=-K sqrt(1-z²)/(Lg Lf²)` et `c_N'=-2 Mg2 Sg Sg' (1-z²)/Lg²`. Les deux sont strictement négatifs hors centre (certificat antérieur : `c_M<-10r²`). Avec `s=r²`, `Lg=A(1+cg s)²`, `Lf=B(1+cf s)²`, `T=Lg²+2b2 Lg Lf+b3 Lf²`, `K=m2 Lg Lf T r²`, `z=r/250`, leur quotient est exactement

`q(r)=c_M/c_N' = m2*r*T*(1+cg*r²)/(2*Lf*(1+5cg*r²)*sqrt(1-r²/62500))`.

Le coefficient `c_N'/r=-2*(1+5cg*s)/(1+cg*s)*(1-s/62500)` vérifie `|c_N'|<201r/100` sur `(0,R]` puisque `cg=3/2000`, `s<=289/400`, et `2(1+4cg*289/400)<201/100`. En utilisant **explicitement** le certificat antérieur `|c_M|>10r²`, il en résulte la borne rigoureuse `q(r)>1000r/201`.

La sous-famille annulant **seulement la combinaison de deux termes** `c_M*M+c_N'*N'=0` avec `M=1` et `N(R)=1` est unique : `N(r)=1+integral_r^R q(t)dt`. Elle est strictement positive, paire et régulière au centre (`q(r)=r f(r²)` analytique), mais impose `N(0)>1+1445/804=2249/804`, donc `M(0)/N(0)<804/2249<1037/2000`. Or le coefficient central b3c2 de Step58, **sous ses propres hypothèses de préservation temporelle et de régularité**, impose `M(0)/N(0)>1037/2000`. Ces deux exigences sont donc incompatibles **uniquement dans cette sous-famille**. La quadrature illustrative donne `integral q≈1.9478840253`, `M(0)/N(0)≈0.3392263710` ; elle ne participe pas à la preuve.

Cela établit simultanément qu'un signe uniforme négatif de chacun des deux coefficients Step57 n'empêche pas leur annulation par un jet `N'<0`, et qu'une telle annulation dans le cas `M=constante`, `N(R)=M(R)` ne peut respecter la condition centrale b3c2. **Ne pas extrapoler :** le coefficient `eta''*N` subsiste, `M(r)` peut varier, les autres termes de l'opérateur temporel et les vrais bords Step55 n'ont pas été imposés, et le probe original Step58 à `R=17/20` n'a pas été exécuté.

Sources originales identifiées : Step55 blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step57 blob `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`, Step58 blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Tests locaux : `PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_two_term_cancellation` (6 résidus symboliques nuls, 7 gardes rationnelles PASS) et `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_two_term_cancellation.py' -v` (4 tests PASS, non indépendants). Aucune exécution originale Step45/55/57/58/Step68o/b3c2. Git direct bloqué par DNS ; connecteur GitHub fonctionnel.

**État : `b3c3d6 PARTIAL` ; `GATE_2B OPEN` ; `JANUS_R NOT_VALIDATED`.** Prochaine action prioritaire inchangée : probe original Step58 sur Step55 à `R=17/20`, `A_N/A_M/B_N/B_M/E_N/E_M`, signes, zéros et dérivées, raccord central, BVP des lapses positifs avec vrais bords, puis Dirac/charges/jauge temporelle/six couples/K=0/J=0/4D/stabilité/observables.
