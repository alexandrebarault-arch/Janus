# JANUS — Étape 68c : réponse du déplacement relatif aux jets de lapses, calculée avec le VRAI Step45

**24 octobre 2026 — branche unique d'écriture :** `research/gate2b-nonhomothetic-transfer`.

**GATE_2B OPEN ; JANUS-R NOT_VALIDATED.** Le résultat est un théorème de **jets CENTRAUX** conditionnel à la famille sphérique analytique et aux primaires indiquées. Il n'établit pas la conservation temporelle de la secondaire, le rang de Dirac ou l'absence de fantôme BD.

## 1. Progrès de provenance : le vrai noyau Step45 est exécuté, pas seulement transcrit

Le fichier historique **original** `numerics/hr_step45_exact_physical_ward.py` a été reconstitué en local depuis le connecteur GitHub et authentifié **octet par octet** par son véritable Git blob SHA-1 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`. Le nouvel audit `numerics/hr_step68c_authentic_center_hamiltonian.py` **importe ce fichier** et calcule ses gradients d'Euler `eg,ef` sur les SIX couples canoniques, avec les poussières. Les NEUF résidus Ward de Step45 ont été réellement évalués et sont exactement nuls. Le test de provenance « fail closed » injecte une modification d'octets et vérifie qu'elle est rejetée.

Cette réexécution **confirme indépendamment l'étape 68b** : les flots générés séparément par les lapses `N` et `M` préservent les relations de parité métrique et de moments canoniques **au centre**, à condition de poser la primaire de moment du secteur `f`. Le contrôle négatif reste
\[
\lim_{r\to0}\left(\delta_M L_f-\frac{\delta_M S_f}{r}\right)
=\frac{M_0(2U-V)}{2bM_f^2},
\quad V=\lim_{r\to0}p_{S_f}/r .
\]
Il n'est pas nul hors de `V=2U`. La source 68b a également été corrigée ce tour : le gradient de poussière `tf'` y comportait une occurrence résiduelle du coefficient d'interaction `b2` à la place du coefficient métrique `bf2`. **Les tests 68b antérieurement publiés ne constituent donc pas une régression post-correction ; les 29 tests du VRAI Step45 présentement exécutés valident le résultat central indépendamment.**

## 2. Jets de l'initial-data chart et stationnarité au centre

On pose `a=L_g(0)`, `b=L_f(0)`, `w=z/r=1/250` sur le benchmark prescrit. La famille analytique autour de `r=0` utilisée par le calcul est

```text
Lg=a+a2*r²+O(r⁴),   Sg=r*Lg,
Lf=b+bf2*r²+O(r⁴), Sf=r*Lf,
pLg=G*r²+G2*r⁴+..., pSg=2G*r+P3*r³+...,
pLf=U*r²+...,       pSf=2U*r+...  [primaire f],
pg=rhog*r²+...,     pf=rhof*r²+...,
theta'g=kg0*r*Lg, theta'f=kf0*r*Lf,
z=w*r, z'=w,
N=N0+N2*r²+N4*r⁴+..., M=M0+M2*r²+M4*r⁴+....
```

Les `N0,N2,N4,M0,M2,M4` sont indépendants. Le coefficient `bf2` n'est **pas** le paramètre d'interaction Hassan–Rosen `beta2` : ils restent des symboles distincts.

Avec `T=\beta_1 a^2+2\beta_2ab+\beta_3b^2` et `k_0=m^2M_g^2abT`, l'équation du déplacement stationnaire `F_z=0` donne, au premier ordre non trivial :
\[
D_g=r^3d_0+O(r^5),\qquad K=r^2k_0+O(r^4),\qquad d_0=k_0w.
\]
La vraie expression canonique `D_g=p_{S_g}S'_g-L_gp'_{L_g}+p_g\theta'_g` impose
\[
d_0=4Ga_2+aP_3-4aG_2+a k_{g0}\rho_g,
\]
d'où `P3=(k0*w-4G*a2+4*a*G2-a*kg0*rhog)/a`. Ce jet est calculé **depuis la densité originale**, non choisi pour annuler arbitrairement un terme d'évolution.

## 3. Résultat NOUVEAU : e_d(0), e_k(0) depuis les douze champs, puis δ_H z'(0)

Pour chaque lapse pris séparément, le nouveau code calcule exactement les SIX contributions à la variation complète de `D_g` :
\[
\delta_H D_g=(\delta p_{S_g})S_g'
+p_{S_g}(\delta S_g)'
-(\delta L_g)p_{L_g}'
-L_g(\delta p_{L_g})'
+(\delta p_g)\theta_g'+p_g(\delta\theta_g)'.
\]
Il **ne supprime pas** les termes de poussière, les dérivées des flots canoniques ni les dérivées des lapses. Les séries symboliques obtenues possèdent un coefficient de `r` **exactement nul** dans les deux secteurs, et fournissent un coefficient `e_d(0)=\lim\delta_H D_g/r^3` calculable et non supposé nul.

À partir du véritable `K=m^2 M_g^2 L_gL_f(\beta_1S_g^2+2\beta_2S_gS_f+\beta_3S_f^2)`, ses variations produisent séparément `e_k(0)=\lim\delta_H K/r^2`. **Les quatre expressions complètes** `e_d(N),e_d(M),e_k(N),e_k(M)` sont enregistrées en clair dans `research/reports/gate2b-step68c-authentic-center-report.json` et reproductibles par le code à partir de Step45.

Sur la branche `k_0\neq0`, la variation fonctionnelle correcte du déplacement à `r=0` donne
\[
\boxed{\delta_H z'(0)=\frac{e_d(0)-w e_k(0)}{k_0}.}
\]
Les jets quatrièmes `N_4,M_4` **s'éliminent** de ce coefficient central, sans qu'il soit nécessaire de les figer.

Le nouveau **certificat exact de sensibilité aux lapses** est
\[
\boxed{\frac{\partial\,\delta_H z'(0)}{\partial M_2}=\frac{2}{b}},
\qquad
\boxed{\frac{\partial\,\delta_H z'(0)}{\partial N_2}
=\frac{2H_{g,0}}{k_0}-\frac{2}{a}},
\]
où `H_{g,0}=\lim_{r\to0}H_g/r^2` est calculé directement depuis la densité primaire de l'**original Step45**. Ces identités ont été vérifiées par annulation symbolique exacte, sans estimation numérique.

**Sur la primaire `H_g=0` au centre**, elles se réduisent à
\[
\boxed{\partial_{N_2}\delta_H z'(0)=-2/a,\qquad
       \partial_{M_2}\delta_H z'(0)=2/b.}
\]
Comme `N''(0)=2N_2`, `M''(0)=2M_2`, les réponses aux lapses dérivés deux fois sont donc respectivement `-1/a` et `+1/b` **pour la variation du shift `z'`**, et NON pour le crochet de la secondaire `C`. Ce dernier peut connaître d'autres annulations par les termes directs et les contraintes, comme établi aux étapes 57–60. **Ne surtout pas conclure que le rang du Dirac est non nul sur la foi de ces deux coefficients isolés.**

## 4. Exécution reproductible, SHA Git vérifiés

```bash
OPENBLAS_NUM_THREADS=1 PYTHONPATH=/mnt/data/janus-step68c \
python -m pytest -q \
/mnt/data/janus-step68c/tests/test_hr_step68c_authentic_center_hamiltonian.py
# RÉELLEMENT : 29 passed in 8.79s

OPENBLAS_NUM_THREADS=1 PYTHONPATH=/mnt/data/janus-step68c \
python -m numerics.hr_step68c_authentic_center_hamiltonian
```

- **Source nouvelle réellement exécutée et uploadée identique :** `numerics/hr_step68c_authentic_center_hamiltonian.py`, Git blob `8d91d69cd1712f09cbc2f6fe8217f73ee52bede5`.
- **Tests exécutés et uploadés identiques :** `tests/test_hr_step68c_authentic_center_hamiltonian.py`, Git blob `4d4cdab8e3a56691a5d60ced8bbc4f49efe85265`.
- **Noyau historique original effectivement reconstitué et authentifié :** `numerics/hr_step45_exact_physical_ward.py`, Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`.
- **Rapport machine :** `research/reports/gate2b-step68c-authentic-center-report.json`. Le manifeste brut local, distinct du JSON GitHub enrichi de provenance, a pour SHA-256 `81aae685a21c00f02860d5fe5600f0af9bf51bbebea1b2899ba97fa9ae8e3e3f`.

Les 29 contrôles portent sur les neuf identités Ward physiques, le rejet d'une source modifiée, les parités métriques et canoniques des deux secteurs, la primaire f indispensable, les jets complets de `D_g`, la stationnarité `F_z` du coefficient `r^3`, la réponse `e_k` et les coefficients universels des dérivées secondes des lapses. **Ce n'est PAS toute la suite du dépôt**, et aucune CI ni GitHub Action n'a été activée.

## 5. Limites et prochaine étape 68d

**Prouvé :** les contraintes de parité centrales et les coefficients exacts `e_d(0),e_k(0),\delta_Hz'(0)` du VRAI Step45, y compris la dépendance non nulle aux secondes dérivées des lapses sous `F_z`, la primaire f et la primaire g centrale.

**Non prouvé :** la parité sur tout l'intervalle `r\in[0,0.85]`, le raccordement du vrai `U(s)` radial Step55 jusqu'au bord, les coefficients COMPLETS `A_N,B_N,A_M,B_M` sur l'ensemble des primaires et leurs prolongations, l'oracle Poisson indépendant **non intégré par parties**, les conditions aux bords, le rang de Dirac, la fixation des lapses, la régularité 4D et la validation JANUS-R.

**NEXT STEP68d :** reconstituer byte-authentiquement Step45/46/55/57/58/59/60 (+ Steps63–65 et leurs tests) dans un seul runtime ; reproduire les gradients du présent audit puis y injecter `e_d,e_k` et leurs dérivées dans le **vrai** opérateur temporel `Cdot` original, sans figer `delta z'` ni confondre la cancellation des lapses de Step58 avec la réponse du shift. Calculer rang/bords et secteur `J=0,K=0` ensuite. Archiver immédiatement chaque résultat et préfixer `00_CURRENT_RESTART.md`.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
