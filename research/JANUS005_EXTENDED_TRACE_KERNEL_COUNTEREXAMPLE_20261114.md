# JANUS-005 — Contre-exemple algébrique à l'extrapolation du rang figé (2026-11-14)

**Portée : identité exacte dans la carte Step46, NON variation physique démontrée.** HEAD source `2993c15d2a8cbed4c8ab71594467506205f32ccb`. Définitions authentifiées dans `research/JANUS005_FULL_OUTER_F_TOTAL_DIFFERENTIAL_IDENTITY_20261112.md` et `research/JANUS005_FIXED_COEFFICIENT_F_TRACE_JACOBIAN_RANK_20261114.md`.

À R fixé, s=R², `den=beta+k*s*U/(2*m*T)`, `num=U**2/(4*m*L)-U*(V-s*D/L)/(2*m*T)-m*L**3*rf/2+s*z*D/L+w`, `rho=-num/den`, `pSf=R*(L*V-s*D-s*k*L*rho)/T`.

**Contre-exemple exact :** faire varier U avec `dU=1`, `dV=0`, tous les coefficients constants SAUF `w`, et imposer
`dw= -partial_U(num)-rho*partial_U(den)`.
Alors `d(num)+rho*d(den)=0`, donc `d(rho)=0` et `d(pSf)=0` exactement, même lorsque le jacobien figé `partial(rho,pSf)/partial(U,V)` est inversible. `d(pf)=s*d(rho)=0` également. Ce noyau est une direction algébrique de l'espace étendu, **pas** une solution admissible de Step45/46/49/55 : w peut être prescrit et la variation pourrait être interdite. Il réfute uniquement l'inférence « rang 2 à coefficients figés implique absence de tangente lorsque les coefficients varient ».

**Vérification exécutée :** Python 3 / SymPy, calcul exact des dérivées des expressions ci-dessus. Quatre simplifications à zéro : `rho_w+1/den`, `pSf_w-R*s*k*L/(T*den)`, `rho_U+rho_w*dw`, `pSf_U+pSf_w*dw`. PASS 4/4. Contrôle indépendant : différentielles `d(rho)=-(d(num)+rho*d(den))/den` et `d(pSf)=R/T*(L*dV-s*k*L*d(rho))` pour les seules variations U,w, d'où zéro directement. Domaine `m*L*T*den != 0`.

**Limites :** aucune preuve que w soit libre, aucune solution de contraintes, aucun bord physique, aucun rang de Dirac. Tests moteur nouveaux : 0 ; cellules physiques Step55/58 évaluées : 0, certifiées : 0. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.

**NEXT_ACTION_EXACT :** lire la définition et le statut de `Wfbar` dans Step45/46/49/55, déterminer si `dw` est prescrit ou libre ; substituer uniquement les variations autorisées et les deux conditions réelles de bord au jacobien total. JANUS-001 : reconstruire les sources authentifiées et lancer les neuf tests puis le pilote à une cellule.
