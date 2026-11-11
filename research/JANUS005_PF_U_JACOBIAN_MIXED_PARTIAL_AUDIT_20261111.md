# JANUS-005 — audit indépendant de la dérivée en U du moment f (2026-11-11)

HEAD source fixé : `3c06630e0b3924652b0abb911edc49c0602c2039`. Source du jacobien : `scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs`, blob Git `7615cdb1624748dac56ab1d969c401b258f8cdaa`. Comparaison aux formules documentées dans `research/JANUS005_FULL_OUTER_F_GEOMETRIC_CHAIN_RULE_20261111.md`. **Audit algébrique conditionnel, aucune exécution de cellule physique.**

Notations indépendantes à rayon fixé : `s,U,V,b,D,w,rf,z,m,L,T,k` ; `den=b+k*s*U/(2*m*T)` ; `num=U**2/(4*m*L)-U*(V-s*D/L)/(2*m*T)-m*L**3*rf/2+s*z*D/L+w` ; `rho=-num/den` ; `pf=s*rho` ; `H=-(diff(num,U)+rho*diff(den,U))/den`. Hypothèses : `m,L,T,den != 0`, géométrie f prescrite. Cette définition de H est celle de la source JS (`dnum.add(rho.mul(dden)).neg().div(den)`).

## Calcul indépendant et contrôles

Commande exécutée dans Python/SymPy : définition des symboles et expressions ci-dessus puis `sympy.simplify` sur chacune des six différences suivantes. **6/6 PASS** (toutes égales à zéro) :
1. `diff(rho,U)-H`.
2. `diff(pf,U)-s*H`.
3. `diff(pf,V)-s*U/(2*m*T*den)`.
4. `diff(H,w)-k*s/(2*m*T*den**2)`.
5. `diff(H,V)-b/(2*m*T*den**2)`.
6. `diff(H,V)-diff(U/(2*m*T*den),U)` (commutation des dérivées mixtes de rho).

Le contrôle (6) est indépendant de l'expression directe de H : `rho_V=U/(2*m*T*den)`, donc `rho_UV= b/(2*m*T*den**2)`. Le coefficient `b=beta_f` est fixe en U dans cette carte, mais `den` ne l'est pas. Le coefficient `chi=R*U/(2*m*T*den)` du code vérifie `pf_V=R*chi` lorsque `s=R**2`. L'identité `pf_U=s*H` est ainsi cohérente avec le jacobien Step46 à géométrie f fixée.

## Contrôle contradictoire et limites

Si `b` était incorrectement remplacé par `den` dans `H_V`, l'écart serait `(b-den)/(2*m*T*den**2)=-k*s*U/(4*m**2*T**2*den**2)`, non nul génériquement. Ceci est un test de cohérence des dérivées, pas une solution des équations de champ. Aucune vérification de l'admissibilité de la famille `P_g`-only par Dirac et les deux vrais bords n'a été réalisée. La formule `H` ne donne aucun signe strict sans enclosures corrélées de ses entrées. Tests du moteur Step55/58 non rejoués ; nouvelles cellules physiques évaluées 0, certifiées 0.

**NEXT_ACTION_EXACT :** depuis les sources authentiques Step45/55, établir les contraintes linéarisées et les véritables conditions aux deux bords sur la famille `P_g`-only ; tester si le vecteur tangent calculé appartient à leur noyau. Si oui, construire une enclosure corrélée de `H` et des quatre traces ; sinon consigner le NO-GO sous ses hypothèses. JANUS-001 : transférer et authentifier toutes les dépendances originales, puis exécuter la suite ciblée et le pilote une cellule.

**GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.**
