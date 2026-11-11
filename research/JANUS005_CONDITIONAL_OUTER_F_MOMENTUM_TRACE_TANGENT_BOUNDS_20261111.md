# JANUS-005 — Deux traces de moment f au vrai bord extérieur : tangent paramétrique conditionnel (2026-11-11)

**Source HEAD fixée :** `6534aa3b9c0408201ff432c40bacb55294161565`. **Statut :** corollaire mathématique exact des bornes physiques Step49/55 antérieures ; pas un rejeu des équations, ni une nouvelle preuve des quatre traces ou des conditions aux limites.

## Hypothèses et identités authentiques

Sur la famille analytique Step49, `s=r²`, `pLf(r,lambda)=s U(s,lambda)`, `V(s,lambda)=G(s,U(s,lambda),Pg+lambda)`, et l'ODE normalisée originale `2s U_s=G-2U` impliquent **exactement** `pLf'(r,lambda)=r V(s,lambda)`. Ces identités sont compatibles avec `numerics/hr_step46_exact_secondary_ode.py` et `scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs`. À rayon fixe, poser `v=partial_lambda U` et `dV=G_U*v+G_Pg`. Alors

`partial_lambda pLf(R,lambda)=R² v(R²,lambda)` et
`partial_lambda pLf'(R,lambda)=R dV(R²,lambda)`.

Les bornes déjà publiées et **non réexécutées** ici, sous le tube Step55 et `|lambda|<=1/5000`, sont `681/100000<v<689/100000` et `0.01353783698071681<dV<0.01380949877341742`. Les bornes de `dV` sont celles de `research/JANUS005_CONDITIONAL_PHYSICAL_G_PARAMETER_TOTAL_VARIATION_SIGN_20261111.md`.

## Calcul exact au vrai bord R=17/20

Pour `R²=289/400`, la multiplication de fractions rationnelles strictement positives donne :

`196809/40000000 < partial_lambda pLf(R,lambda) < 199121/40000000`
(soit `0.004920225 < ... < 0.004978025`).

`23014322867218577/2000000000000000000 < partial_lambda pLf'(R,lambda) < 11738073957404807/1000000000000000000`
(soit `0.0115071614336092885 < ... < 0.011738073957404807`).

Par division de quantités positives, le rapport des deux dérivées satisfait :

`1353783698071681/585650000000000 < (partial_lambda pLf')/(partial_lambda pLf) < 690474938670871/289425000000000`,
soit approximativement `2.31159 < ratio < 2.38568`.

**Conséquence circonscrite :** sur cette famille et sous les hypothèses Step49/55, les deux composantes `(pLf,pLf')` du tangent au vrai bord extérieur sont strictement positives et leur rapport est borné. En particulier ce tangent n'est pas nul. Ceci ne démontre pas la compatibilité des quatre traces `(pLf,pLf',pf,pSf)` avec des conditions aux limites physiques ; le tangent d'une famille à un paramètre a rang au plus un et n'est pas le rang de Dirac.

## Vérification reproductible et contradictoire

Calcul réellement exécuté avec Python `fractions.Fraction` (rationnels exacts), sans SymPy ni arrondi flottant pour les comparaisons :

```python
from fractions import Fraction as F
R=F(17,20); s=R*R
vlo,vhi=F(681,100000),F(689,100000)
glo,ghi=F('0.01353783698071681'),F('0.01380949877341742')
assert (s*vlo,s*vhi)==(F(196809,40000000),F(199121,40000000))
assert (R*glo,R*ghi)==(F(23014322867218577,2000000000000000000),F(11738073957404807,1000000000000000000))
assert (R*glo/(s*vhi),R*ghi/(s*vlo))==(F(1353783698071681,585650000000000),F(690474938670871,289425000000000))
assert s*vlo>0 and R*glo>0
```

L'exécution arithmétique précédente a produit les trois couples de fractions attendus. Les assertions ci-dessus explicitent les mêmes valeurs pour un rejeu indépendant. La contre-épreuve logique est que `dV>0` seul ne fixe **pas** les signes de `partial_lambda pf` et `partial_lambda pSf` : leurs expressions exactes font intervenir `H`, `chi`, `Lf/Sfr` et `kf`. Une conclusion sur ces deux traces sans leurs bornes serait injustifiée.

**Nouveaux tests authentiques du moteur Step55/58 : 0. Cellules physiques nouvellement évaluées : 0 ; certifiées : 0.** Les bornes de départ sont des résultats conditionnels antérieurs, pas recalculés ici.

## NEXT_ACTION_EXACT

Sur les mêmes sources physiques authentifiées, encloser `H` et les coefficients du jacobien Step46 au vrai bord `R=17/20` pour calculer `partial_lambda pf=H*R²*v+chi*R*dV` et `partial_lambda pSf=(Lf/Sfr)*R*dV-(R*kf*Lf/Sfr)*partial_lambda pf`. Contrôler ensuite les quatre traces avec les **conditions aux deux vrais bords**, et distinguer tangent paramétrique formel et espace des solutions admissibles. JANUS-001 reste prioritaire pour le pilote physique authentique.

**GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.**
