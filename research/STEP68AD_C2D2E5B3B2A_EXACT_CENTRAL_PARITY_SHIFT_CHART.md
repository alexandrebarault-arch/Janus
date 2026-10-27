# JANUS — 68ad-C2d2e5b3b2a : critère exact de régularité centrale du shift réduit

27 octobre 2026. **Étape PARTIELLE du programme Dirac. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance et portée

Formules originales relues sur GitHub (SHA blobs contrôlés, **moteurs non réexécutés**) : `numerics/hr_step45_exact_physical_ward.py` = `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ; `numerics/hr_step55_global_barrier.py` = `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe` ; `numerics/hr_step68o_temporal_interval_annulus.py` = `c99caebc17f243784450ddff94fb061767e6d8e7`. Le calcul est une **classification algébrique de la régularité du shift** sur une classe de parité analytique, **pas** une classification des variations qui préservent les contraintes hamiltoniennes, et **pas** un oracle de Dirac.

## Théorème conditionnel exact

Sur une classe de champs analytiques en `s=r²`, prendre `Lg=L(s)`, `Sg=r H(s)`, `pSg=r P(s)`, `pLg=r² G(s)`, `pg=r² rho(s)`, `tg'=r Tdust(s)`, `Lf=Lf(s)`, `Sf=r F(s)`. Les autres variables du secteur f peuvent suivre leur parité centrale mais leurs moments n'entrent pas directement dans `D`. La formule originale Step45 est `D=pSg Sg'-Lg pLg'+pg tg'`, `K=m2 Mg2 Lg Lf (beta1 Sg²+2 beta2 Sg Sf+beta3 Sf²)`.

Par dérivation radiale **sans gel du shift**, on obtient exactement

`D=r C(s)` où `C(s)=P(H+2s H_s)-2L(G+s G_s)+s rho Tdust`.

`K=r² k(s)` où `k(s)=m2 Mg2 L Lf (beta1 H²+2 beta2 H F+beta3 F²)`.

Supposons `k(0)>0` et les fonctions analytiques/bornées dans un voisinage du centre. La solution réduite `z*=D/sqrt(K²+D²)` pour `r>0` satisfait **`z*=O(r)` si et seulement si**

`c0=C(0)=P(0)H(0)-2L(0)G(0)=0`.

Preuve : si `c0 != 0`, `D=r(c0+O(r²))`, `K=r²(k0+O(r²))`, donc `z* -> sign(c0)` (pas `O(r)`). Si `c0=0`, l'analyticité donne `C(s)=s d(s)`, puis exactement `z*=r d(s)/sqrt(k(s)²+s d(s)²)`, qui est `O(r)`. Cette propriété concerne le shift réduit **sur cette charte**, pas l'admissibilité aux contraintes et aux bords.

La condition tangentielle linéarisée est `H0 δP0 + P0 δH0 - 2G0 δL0 - 2L0 δG0=0`. Si `H0=L0>0`, `P0=2G0`, et `δH0=δL0`, elle devient `δP0=2δG0`. La vraie géométrie Step55/68o appartient à cette sous-classe centrale, mais cela ne prouve **pas** que toutes ces directions satisfont `δHg=δHf=δC=0`.

Sur une famille **finie** restant exactement dans `c0(ε)=0`, on a `K=r² k(s,ε)`, `D=r³ d(s,ε)` et
`δz*=r k(k δd-d δk)/(k²+s d²)^(3/2)`,
`δ² F_red=r⁴ (k δd-d δk)²/(k²+s d²)^(3/2)`.
Sous bornes uniformes sur `k>0`, ces termes sont respectivement `O(r)` et `O(r⁴)`. `δ²F_red` est ici la forme quadratique de la Hessienne algébrique en `(K,D)`, **pas** la matrice de Dirac.

## Contre-exemple non linéaire, hors coquille

Prendre au centre `H=L=1`, `P_ε=2+ε+ε²`, `G_ε=1+ε/2`, et fixer les autres coefficients appropriés. Alors `c0(ε)=ε²`, avec `c0(0)=c0'(0)=0`, mais pour tout `ε≠0` fixé, `z_ε(r)->+1` lorsque `r->0+`. La famille corrigée `P_ε=2+ε`, `G_ε=1+ε/2` possède **la même tangente non nulle** et conserve exactement `c0(ε)=0`, donc le shift régulier. La seule condition linéarisée **ne garantit pas** qu'une famille finie reste dans la charte centrale. Exemple purement algébrique, **non démontré tangent aux contraintes physiques**.

## Exécution

Programme BigInt publié `scripts/hr_step68ad_c2d2e5b3b2a_center_parity_chart.cjs` : **18 assertions PASS** dans V8. Wrapper adversarial publié `tests/test_hr_step68ad_c2d2e5b3b2a_center_parity_chart.cjs` : **14 assertions PASS** dans V8, dont trois profils rationnels et des tests négatifs. Contrôle SymPy indépendant : **8 identités PASS** après correction d'un premier brouillon de contrôle où `s` et `r` avaient été traités indépendamment dans le terme de poussière ; cet échec préliminaire n'est pas dissimulé. Total final : **40 vérifications réussies, 0 échec** (18+14+8), sans prétendre qu'il s'agit de 40 tests unitaires Python. Les moteurs physiques originaux et un clone Node complet **n'ont pas été exécutés**.

Empreintes Git des deux sources exécutées : programme `63b84e9fad6051c45961247ac00f5abd23e6a1e8`, wrapper `062e028ac9e88977add283f57775dbab861e07f6`. Le rapport JSON conserve les témoins rationnels.

## Verrous et prochaine étape

**Non démontré :** espace tangent aux contraintes linéarisées `Hg,Hf,C` avec bords, véritable oracle fonctionnel non-IBP sur la solution Step55/68o, rang complet de Dirac, tertiaires, lapses globaux, charte `J=0`, dynamique 4D, stabilité et observables. **Prochaine étape effective : 68ad-C2d2e5b3b2b**, tester les contraintes linéarisées sur la charte centrale avant de construire le crochet de Poisson/Dirac à six couples. Éviter toute conclusion de validation cosmologique à partir de cette régularité algébrique.
