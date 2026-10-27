# JANUS — 68ad-C2d2e5b3b2c2b2d2c : courbure non nulle sur une sous-variété de contraintes PRIMAIRES ponctuelles

27 octobre 2026. **Théorème exact, témoin analytique positif en poussières, mais interaction témoin NON Step55 et contraintes SECONDAIRES/FONCTIONNELLES NON imposées. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Provenance et question

Formules des contraintes primaires et de la réduction du shift vérifiées sur les sources GitHub originales :
- `numerics/hr_step37_original_nonibp_oracle.py`, blob `005449ade6e3582e3b9a5c3374a881a77e73e3f6`.
- `numerics/hr_spherical_adm_primary.py`, blob `c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41`.
- `numerics/hr_spherical_mixed_hamiltonian_bracket.py`, blob `6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81`.
- Forme de bord dérivée et contrôlée à l'étape d2a, courbure ambiante contrôlée à d2b.

La question est de savoir si la courbure ambiante de d2b peut déjà disparaître en imposant les **quatre contraintes primaires ponctuelles** `H_g=H_f=D_g+D_f=F_z=0`. Ce n'est pas le test des variations tangentes à la **surface complète des contraintes de Dirac**. Le présent témoin démontre que les contraintes primaires ponctuelles seules ne suffisent PAS à rendre la forme fermée sur toutes leurs directions tangentes.

## Construction exacte d'une sous-variété à deux paramètres

Fixer `N=M=1, V=0, m²=M_g²=M_f²=1`, les coordonnées `L_g=2,L_f=3,S_g=5,S_f=7`, les dérivées `S'_g=S'_f=1,S''_g=S''_f=-2,t'_g=t'_f=0`, les moments `p_{S_g}=4,p_{L_f}=3,p_{S_f}=0`. Choisir les paramètres d'interaction **témoins** `beta_1=1/50` et `beta_0=beta_2=beta_3=beta_4=0`. Cette interaction n'est pas revendiquée comme celle de la solution Step55.

Il vient exactement `A_0=7/5, A_t=1/2, A_s=0, K=m² M_g² L_g L_f A_t=3>0`, `R_g=23/50` et `R_f=8/49`. Paramétrer les deux jets de moment libres par `x=p_{L_g}`, `y=p'_{L_g}`. Définir

```
D_g=4-2y, T=sqrt(9+(4-2y)^2), z*=D_g/T, sqrt(1-z*²)=3/T,
p'_{L_f}=D_g/3,
H_g^0=Lg*x²/(4*Mg²*Sg²)-x*pSg/(2*Mg²*Sg)
      -Mg²*Lg*Sg²*Rg/2 + z*Dg/Lg + m²*Mg²*(Lg*A0+Lf*At*3/T),
H_f^0=Lf*pLf²/(4*Mf²*Sf²)-pLf*pSf/(2*Mf²*Sf)
      -Mf²*Lf*Sf²*Rf/2 + z*Dg/Lf + m²*Mg²*(Lf*As+Lg*At*3/T),
p_g=-H_g^0, p_f=-H_f^0.
```

Les deux poussières sont de type original `p_t sqrt(1+(t'/L)^2)` ; avec `t'=0`, leur contribution aux contraintes hamiltoniennes est exactement `p_t`. Par construction algébrique, **pour tout x,y réels** les deux contraintes hamiltoniennes ponctuelles `H_g=H_f=0` sont satisfaites, la contrainte de difféomorphisme `D_g+D_f=0` l'est par le choix de `p'_{L_f}`, et `F_z=0` par `z*=D_g/T` avec `K=3>0`.

Au point `x=2,y=0`, on a `D_g=4,z*=4/5,p'_{L_f}=4/3` et **`p_g=173/25>0, p_f=5995/588>0`**. La continuité garantit un ouvert à deux dimensions autour du témoin où les deux poussières restent positives et la charte `K>0` régulière.

## Tiré-en-arrière exact de la forme de bord

La forme ambiante de d2b, à coordonnées et multiplicateurs fixés, est

```
Theta_D=(2 Mg² N Sg/Lg) dSg' +(2 Mf² M Sf/Lf) dSf'
        -(A z*+V Lg) dpLg - V Lf dpLf,
A=N+M Lg/Lf=5/3.
```

Sur la sous-variété de contraintes primaires ci-dessus, `dSg'=dSf'=dpLf=0` et `dpLg=dx`. Ainsi le tiré-en-arrière vaut exactement

```
i*Theta_D = -(5/3) (4-2y)/sqrt(9+(4-2y)^2) dx.
d(i*Theta_D) = 30/[9+(4-2y)^2]^(3/2) dy∧dx.
```

Cette 2-forme est **strictement positive dans la base orientée (∂y,∂x)**, et vaut exactement **6/25** au témoin. Aucun contreterme scalaire local `C(x,y)` ne peut annuler la forme sur un ouvert de cette sous-variété : `d²C=0` contredirait la courbure non nulle.

Il s'agit d'une **obstruction plus forte que d2b au sens logique**, car elle subsiste sur une sous-variété de contraintes primaires ponctuelles avec poussières positives, et pas seulement sur l'espace ambiant. Elle n'est **pas** une obstruction sur la surface fonctionnelle complète : les équations secondaires, la préservation temporelle, les conditions de régularité radiale et les paramètres physiques Step55 n'ont pas été imposés. Une restriction ultérieure peut supprimer les directions `∂x,∂y`.

## Vérifications et limites

Commande exécutée : `python numerics/hr_step68ad_c2d2e5b3b2c2b2d2c_primary_tangent.py` — **19 assertions SymPy exactes PASS, 0 FAIL**, dont les contraintes primaires identiques, la dérivée de la forme de bord, la valeur rationnelle 6/25 et la positivité des poussières. Rejeu : `python -m unittest discover -s tests -p 'test_hr_step68ad_c2d2e5b3b2c2b2d2c_primary_tangent.py' -v` — **1 unittest PASS**, rejouant les mêmes 19 assertions (non indépendant). Code/test et certificat JSON relus après publication, SHA Git comparés aux fichiers exécutés.

**Limites décisives :** témoin algébrique d'interaction non Step55 ; contraintes seulement ponctuelles et primaires ; pas de tangence prouvée à `C(r)=0`, pas de résolution fonctionnelle des contraintes, ni de conditions aux bords physiques, ni de rang Dirac, tertiaires, lapses déterminés, chartes `K=0/J=0`, dynamique 4D, stabilité ou observables. Les sources originales ont été relues et SHA authentifiés, leurs moteurs non réexécutés pendant cette étape.

**Prochaine étape :** imposer la secondaire fonctionnelle et les jets radiaux nécessaires sur la famille physique Step55, construire une base de variations tangentes à toutes les contraintes et tester `i^*dTheta` ; vérifier séparément les conditions de bord et les variations des lapses. Ne jamais confondre l'obstruction primaire du témoin avec une réfutation de JANUS.
