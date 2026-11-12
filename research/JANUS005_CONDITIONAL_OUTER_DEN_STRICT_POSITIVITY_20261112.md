# JANUS-005 — exclusion conditionnelle du zéro du dénominateur extérieur f (2026-11-12)

## Source et portée
HEAD de lecture `ce1445c78e34e7a76902f8cf42fa9b85a8348390`. Sources originales `scripts/hr_step68ad_c2d2e5b3b2c2b3c2a_f_boundary_jacobian.cjs` (fonction `physicalChiBounds`) et `numerics/hr_step55_global_barrier.py` (`geometry`). Cette preuve concerne **uniquement la carte physique conditionnelle déjà encadrée** à `R=17/20`, pas toutes les solutions de JANUS ni une variation M2 libre.

## Hypothèses et calcul
Poser `s=R²`, `mf=(0.10879548725)²>0`, `kf=-0.0016<0`, `B=(2/5)*0.5787707228025044`, `cf=-0.0012`, `Sfr=B*(1+cf*s)*(1+5*cf*s)>0`. La source Step46 emploie `den=beta+kf*s*U/(2*mf*Sfr)` ; dans la carte prescrite Step55, `beta=sqrt(1+kf²*s)`. L'archive source fournit les bornes conditionnelles
`ulo=-10707594192153122134265173/2000000000000000000000000000`,
`uhi=-1146420876631433922729177/250000000000000000000000000`,
avec `ulo<=U<=uhi<0`.

Puisque `kf<0` et `U<0`, `kf*s*U/(2*mf*Sfr)>0` ; puisque `s>0`, `sqrt(1+kf²*s)>1`. Donc **den>1** sur cette carte, et le cas `den=0` de la trichotomie précédente est exclu sous ces hypothèses.

Une enclosure rationnelle conservatrice, utilisant `1<=sqrt(1+x)<=1+x/2` pour `x>=0`, donne
`1+kf*s*uhi/(2*mf*Sfr) <= den <= 1+kf²*s/2+kf*s*ulo/(2*mf*Sfr)`.
Les bornes exactes obtenues avec `fractions.Fraction` sont :
- borne inférieure `4961171375838248413974326042705331557265839/4956352239353208640830053575025331557265839` (~1.00097231517) ;
- borne supérieure `17056817171030000183558594831621142233630342110602181/17037460822776654702853309164149577228101321562500000` (~1.00113610522).

## Exécution indépendante
Python 3, `fractions.Fraction`, commande reproductible :

```python
from fractions import Fraction as F
R=F(17,20);s=R*R;B=F(2,5)*F('0.5787707228025044')
mf=F('0.10879548725')**2;cf=F('-0.0012');k=F('-0.0016')
Sfr=B*(1+cf*s)*(1+5*cf*s)
ulo=F('-10707594192153122134265173/2000000000000000000000000000')
uhi=F('-1146420876631433922729177/250000000000000000000000000')
assert ulo<uhi<0 and Sfr>0 and k<0
lo=1+k*s*uhi/(2*mf*Sfr)
hi=1+k*k*s/2+k*s*ulo/(2*mf*Sfr)
assert 1<lo<hi
print(lo,hi)
```

Assertions PASS ; contrôle indépendant de la conclusion par les signes `kf*U>0`, `sqrt(1+kf²*s)>1`. Il s'agit d'une nouvelle exploitation des **bornes archivées**, pas d'un rejeu Step55.

## Limites / falsification
La preuve n'établit pas que les bornes archivées restent valables pour une famille à M2 variable, ni la compatibilité aux deux vrais bords, ni la fermeture Dirac. Pour une famille qui sort de la carte `U<0`, l'exclusion peut échouer ; il faut alors encloser directement `den`. Aucun test du moteur Step55/58, aucune cellule physique évaluée/certifiée dans cette session. `GATE_2B=OPEN`, `JANUS_R=NOT_VALIDATED`.

**NEXT_ACTION_EXACT :** vérifier dans Step45/46/49/55 les hypothèses de variation M2 et la préservation de `U<0`, puis borner `den` sur la vraie famille au bord extérieur et au second vrai bord ; confronter les conditions de Dirac. JANUS-001 : reconstruire les dépendances authentifiées et exécuter les neuf tests puis le pilote.
