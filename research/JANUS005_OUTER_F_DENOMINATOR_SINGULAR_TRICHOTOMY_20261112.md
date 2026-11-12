# JANUS-005 — singularité du dénominateur de la trace f extérieure (2026-11-12)

**Portée :** conséquence algébrique exacte des définitions du rapport `research/JANUS005_FULL_OUTER_F_TOTAL_DIFFERENTIAL_IDENTITY_20261112.md`, au bord fixé R=17/20, s=289/400. Ce n'est **pas** une solution physique de Step45/46/55, ni une preuve de présence d'une singularité dans le domaine admissible.

Poser `q=rho`, `den=beta+k*s*U/(2*m*T)` et
`num=U**2/(4*m*L)-U*(V-s*D/L)/(2*m*T)-m*L**3*rf/2+s*z*D/L+w`, avec `m*L*T != 0`.
L'équation non divisée est `F(q)=num+den*q=0`.

**Trichotomie exacte :**
1. Si `den != 0`, l'unique solution est `q=-num/den`.
2. Si `den == 0` et `num != 0`, aucune valeur finie de `q` ne satisfait F=0 (NO-GO **local à cette équation algébrique**, non au modèle).
3. Si `den == 0` et `num == 0`, F=0 pour tout q : cette équation perd le rang en q, et il faut d'autres contraintes pour fixer q. Les traces `pf=s*q` et `pSf=R*(L*V-s*D-s*k*L*q)/T` ne sont pas en général uniques. En particulier `d(pf)/dq=s=289/400` et `d(pSf)/dq=-R*s*k*L/T=-4913*k*L/(8000*T)`.

**Contrôle exécuté** avec Python 3 / SymPy : expansion de F, dérivée `diff(F,q)==den`, substitution `beta=-k*s*U/(2*m*T)` donnant F=num, puis substitution simultanée de `w=-(num-w)` donnant F=0, et dérivation de pSf en q. Les quatre identités symboliques ont été observées directement. Cette substitution est un **contrôle algébrique**, pas une famille physique admissible.

**Conséquence méthodologique :** toute enclosion du jacobien extérieur qui divise par den doit démontrer que 0 n'appartient pas à son intervalle sur le domaine physique ciblé. Si une boîte contient 0, la division et les signes stricts des traces ne sont pas certifiés : subdiviser, prouver une séparation, ou traiter directement F=0 et les autres contraintes. Une boîte contenant 0 ne prouve pas que den s'annule réellement.

**NEXT_ACTION_EXACT :** extraire les contraintes physiques Step45/46/49/55 sur beta,k,m,T,U et établir une borne rationnelle de den excluant zéro au bord extérieur ; si impossible, tester les conditions de compatibilité num=0 sur la variété den=0 et vérifier les deux vrais bords. JANUS-001 : reconstruction authentifiée, neuf tests, pilote une cellule. Cellules physiques évaluées/certifiées : 0/0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
