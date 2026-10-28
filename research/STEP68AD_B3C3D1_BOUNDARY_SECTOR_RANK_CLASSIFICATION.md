# JANUS — b3c3d1 : critère de rang du secteur de bord lié au shift (28/10/2026)

**Statut : théorème cinématique exact, limité au secteur de bord en z' ; pas de tangence Dirac, pas de condition de bord physique certifiée. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Source authentifiée et calcul

La densité Step45 originale (blob Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e`) contient `z' pLg` dans Ag et `z' pLg Lg/Lf` dans Af. Pour les lapses N,M, le coefficient de variation de bord `delta z` provenant de ces dérivées est donc `P=pLg*(N+M*Lg/Lf)`. Sur la carte stationnaire K>0, `Z=z*=D/sqrt(D^2+K^2)` avec `D=pSg*Sg'−Lg*pLg'+pg*tg'`. **Le secteur concerné** de la forme de bord est exactement `alpha_shift=P dZ`. Sa courbure est `d alpha_shift=dP wedge dZ`.

Pour toute sous-variété lisse S de données de bord, `i_S^*(d alpha_shift)=0` **si et seulement si** le différentiel de l'application `(P,Z)|_S` a rang au plus un. Ce critère est ponctuel et ne suppose aucune condition physique de bord. Sur la tranche libre (pLg,pLg') avec autres jets et lapses fixes, le déterminant vaut `−Lg*(N+M*Lg/Lf)*K^2/(D^2+K^2)^(3/2)`, strictement négatif pour Lg,Lf,N,M,K>0 : on retrouve le témoin rationnel NON Step55 `−32/375`.

## Contre-exemples constructifs à une obstruction universelle

Le secteur devient intégrable sur une condition `Z=const` (il s'annule), ou `P=const` (primitive `P*Z`). Plus généralement, sur `Z=F(P)` avec `F(P)=c0+c1*P+c2*P^2` et `|F(P)|<1`, `alpha_shift=P F'(P)dP=dB` avec `B=c1*P^2/2+2*c2*P^3/3`. Ces conditions sont algébriquement réalisables au niveau des jets : `D=K*F(P)/sqrt(1-F(P)^2)`, donc `pLg'=(pSg*Sg'+pg*tg'−D)/Lg`. Cela **ne prouve absolument pas** qu'elles sont compatibles avec primaires, C(r)=0, préservation temporelle, conditions de régularité ou générateurs différentiables.

**Attention à la portée :** `alpha_shift` n'est PAS la forme de bord non-IBP complète. Les autres termes en dérivées radiales de Step45 peuvent fournir d'autres contributions à la variation de bord. Le critère de rang ne garantit ni contreterme global ni annulation de `dTheta` sur le véritable espace physique. La classification n'est ni une validation ni un no-go de JANUS.

## Exécution et reproductibilité

Sources originales Step45/55/58 relues par le connecteur GitHub, blobs `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Les imports originaux et le unittest b3c2 ne sont PAS rejoués : `git ls-remote` échoue sur `Could not resolve host: github.com` dans le conteneur. En revanche le calcul autonome du secteur a été exécuté en structure numerics/tests : **16 assertions SymPy exactes PASS ; 4 unittest PASS, non indépendants ; 0 FAIL**.

Code : `numerics/hr_step68ad_b3c3d_boundary_sector_rank.py` (blob `ac359aed8e3fadf465c328b2e5a7d7d559665eb5`). Tests : `tests/test_hr_step68ad_b3c3d_boundary_sector_rank.py` (blob `de0aa6e3529f4e26e80f9fba44f8dc4f26d90c0a`). Ces SHA correspondent aux octets exécutés localement et relus sur GitHub.

## Suite prioritaire

**b3c3d2 :** obtenir un rejeu complet des vrais imports Step45/55/58 et du test b3c2 ; calculer la forme de bord complète originale non-IBP, puis classifier les sous-espaces tangents aux primaires, secondaire, préservation temporelle et conditions aux bords ; seulement ensuite générateurs améliorés, charges, quotient de jauge temporelle, rang/tertiaires Dirac six couples, cartes K=0/J=0, 4D, stabilité, observables.

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
