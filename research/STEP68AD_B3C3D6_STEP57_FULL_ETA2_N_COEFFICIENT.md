# b3c3d6 — coefficient manquant eta''*N du Step57 sur Step55 (29 octobre 2026)

**Nouveau résultat exact mais restreint :** le coefficient de `eta''*N` dans le crochet smeared Step57 est maintenant explicité et encadré rationnellement sur la géométrie prescrite Step55, `0<r<=17/20`, `Fz=0`, `K>0`. Il s'ajoute aux deux coefficients `eta''*M` et `eta''*N'`, dont ce dernier conserve impérativement le facteur original `1/Lf`. Il ne s'agit **ni** du crochet temporel local complet Step58 **ni** de la condition Dirac intégrée, du problème aux deux bords ou d'un no-go JANUS.

## Déduction à partir des expressions originales

Sources lues directement sur la branche : Step45 `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ; Step55 `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` ; Step57 `numerics/hr_step57_secondary_principal_symbol.py` blob `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f` ; Step58 `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`.

La ligne originale Step57 renvoie `eta2_N_coefficient=Bbase*contractions['N0']` avec `Bbase=-K²/(Lg*Lf*R²)=-(1-z²)/(Lg*Lf)` sur `Fz=0,K>0,R=sqrt(D²+K²)`. La contraction originale `T_N0=Lg*eg[0][Lg]+pSg*eg[0][pSg]+pg*eg[0][pg]` se simplifie exactement en

`T_N0=kg+pg/sqrt(1+tg'^2/Lg²)-Mg2*Lg+Mg2*Sg'^2/Lg+m2*Mg2*Lg*(beta0*Sg²+2*beta1*Sg*Sf+beta2*Sf²)`,

avec `kg=Lg*pLg²/(4*Mg2*Sg²)-pLg*pSg/(2*Mg2*Sg)`. **Tous les termes explicites en z se compensent dans cette contraction**, mais le facteur global `1-z²` demeure. Le calcul de `T_N0` a été effectué par dérivation symbolique de la densité Step45, pas par rejeu du module Step45 original. Sur Step55 : `Sg=r*Lg`, `Sf=r*Lf`, `pLg=r²*Gmom`, `pSg=r*Psg`, `pg=r²*Rhog`, `tg'=r*KG*Lg`, `z=r/250`. La formule régulière `T_N0/r²` est utilisée, avec identité exacte `Sg'^2/Lg-Lg=A*r²*(8*CG+24*CG²*r²)`.

## Enclosure globale reproductible

Le code `numerics/hr_step68ad_b3c3d6_step57_full_eta2_N.py` utilise un intervalle entier sortant sur le réseau `10^-28`, des racines carrées encadrées par `isqrt`, et **256 cellules fermées recouvrant exactement** `s=r² in [0,289/400]`. Pour chaque cellule, les quantités intermédiaires `Rhog`, `betag` et `K/r²` sont strictement positives, et les trois coefficients vérifient les signes uniformes

- `c_N/r²>6` et `c_N/r²<7` ;
- `c_M/r²<-10` ;
- `c_Nprime/r<-17/2`.

Enclosure exacte `c_N/r²` : `[31368160802458321801214531607/5000000000000000000000000000, 4012205757806882889885031099/625000000000000000000000000]`, soit environ `[6.2736,6.4196]`. Il s'agit d'une preuve par inclusion rationnelle des formules **transcrites** et des données Step55 prescrites, non d'une validation indépendante du moteur original.

## Raccord central : rôle essentiel de la courbure du lapse

Pour `N(r)=N0+N2*r²+o(r²)`, `M(r)=M0+M2_lapse*r²+o(r²)`, les coefficients du symbole `eta''` ont `c_N=cN2*r²+o(r²)`, `c_M=cM2*r²+o(r²)`, `c_Nprime=cNp1*r+o(r)`. Leur somme `c_N*N+c_M*M+c_Nprime*N'` n'a donc **pas** seulement les deux premiers termes à l'ordre `r²` : le terme `c_Nprime*N'=2*cNp1*N2*r²+o(r²)` compte aussi. Son annulation formelle impose

`cN2*N0+cM2*M0+2*cNp1*N2=0`.

En utilisant **conditionnellement** la bande centrale Step58 b3c2 `1037/2000<M0/N0<2593/5000`, le certificat sortant donne `1/25<N2/N0<1/20` pour satisfaire cette seule égalité d'ordre `r²`. Ainsi **aucune incompatibilité centrale ne peut être déduite des deux seuls coefficients Step57 ni du symbole eta'' complet sans contrôler la courbure N2**. Cela ne prouve pas qu'un lapse global positif satisfaisant Step58 et les vrais bords existe. Le coefficient `eta''` ne peut pas être imposé séparément sans justifier les intégrations par parties et l'équation temporelle locale.

## Exécution, provenance, limites

Exécuté localement : `PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_step57_full_eta2_N` : **3 résidus SymPy nuls**, **1795 gardes rationnelles** sur 256 cellules et au centre, zéro échec ; `PYTHONPATH=. python -m unittest discover -s tests -v` : **5 unittest PASS, non indépendants**, zéro échec. Un contrôle négatif interdit d'imposer `N2=0` avec le ratio central Step58, et un test vérifie le rejet d'une division par un intervalle contenant zéro.

Fichiers : `numerics/hr_step68ad_b3c3d6_step57_full_eta2_N.py`, `tests/test_hr_step68ad_b3c3d6_step57_full_eta2_N.py`, `research/reports/gate2b-step68ad-b3c3d6-step57-full-eta2-N.json`. **Aucun moteur original Step45/55/57/58 n'a été exécuté localement** ; l'accès Git local échoue par DNS. Les blobs sources ont été lus et les formules comparées aux originaux via le connecteur GitHub. Le probe original Step58 à `R=17/20`, les six coefficients et leurs dérivées, les zéros et le raccord global, les deux vrais bords, les lapses positifs, Dirac/charges/jauge temporelle/six couples/K=0/J=0/4D/stabilité/observables restent **NON ÉVALUÉS**.

**b3c3d6 PARTIELLE ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Priorité : véritable exécution Step58 original sur Step55 et problème global des lapses, sans confondre ce symbole smeared avec la contrainte temporelle locale.
