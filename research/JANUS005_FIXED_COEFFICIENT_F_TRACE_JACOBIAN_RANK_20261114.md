# JANUS-005 — Rang algébrique local des deux traces f (2026-11-14)

**Statut : résultat algébrique exact, NON physique.** HEAD source `6d46c9d286885de484f5f9e4a3c6d44cfd6534e4`. Définitions reprises du rapport authentifié `research/JANUS005_FULL_OUTER_F_TOTAL_DIFFERENTIAL_IDENTITY_20261112.md` (blob `f0f0377eae671bb542abb49d5f0df99ac7d97585`). Aucune hypothèse sur l'admissibilité physique des variations n'est ajoutée.

À rayon R fixe, s=R², m,L,T,beta,k,D,rf,z,w constants non nuls là où les dénominateurs l'exigent, poser
`den=beta+k*s*U/(2*m*T)`,
`num=U**2/(4*m*L)-U*(V-s*D/L)/(2*m*T)-m*L**3*rf/2+s*z*D/L+w`,
`rho=-num/den`,
`pSf=R*(L*V-s*D-s*k*L*rho)/T`.

**Identité nouvelle vérifiée :** pour le jacobien `J=∂(rho,pSf)/∂(U,V)` à géométrie et sources figées,
`det(J)=(R*L/T)*∂rho/∂U`.
Ceci résulte directement de l'annulation des termes croisés en `rho_U*rho_V`. De plus,
`rho_V=U/(s*U*k+2*T*beta*m)`,
`(pSf)_V=2*L*R*beta*m/(s*U*k+2*T*beta*m)`.
La condition de singularité de cette carte de traces est donc `rho_U=0` lorsque `R*L*T*m*den != 0`; un dénominateur nul est une **sortie de carte**, pas une preuve de rang physique déficient.

**Contrôle exécuté réellement :** Python/SymPy, définition des quatre expressions ci-dessus, `J=Matrix([rho,pSf]).jacobian([U,V])`; `simplify(det(J)-R*L/T*diff(rho,U))` retourne exactement `0`. Vérification supplémentaire : `factor(diff(rho,V))` et `factor(diff(pSf,V))` retournent les deux expressions annoncées. Contrôle rationnel ponctuel indépendant de l'identité symbolique : `R=17/20,m=2,L=3,T=4,beta=5,k=6,U=1/7,V=2/9,D=1/11,rf=1/13,z=1/17,w=1/19` donne `den=112867/22400`, `det(J)=-14216414704483/1038352604250390`. Ces valeurs sont des données algébriques arbitraires, **pas** une cellule physique JANUS.

**Interprétation critique :** ce calcul isole un critère de rang pour la carte **à coefficients figés**. Il ne permet pas de conclure au rang de la famille physique, où m,L,T,beta,k,D,rf,z,w varient sous Step45/46/49/55, ni aux contraintes de Dirac, ni aux deux vrais bords. Aucune certification de signe, aucun NO-GO physique.

Tests moteur nouveaux : 0 ; cellules physiques Step55/58 évaluées : 0 ; certifiées : 0. `GATE_2B=OPEN`; `JANUS_R=NOT_VALIDATED`.

**NEXT_ACTION_EXACT :** construire le jacobien **total** des traces en substituant les dérivées physiques des neuf coefficients figés, puis évaluer rang et deux conditions de bord sur la solution Step55 authentique ; en parallèle, reprendre JANUS-001 seulement après transfert et vérification Git des dépendances originales.
