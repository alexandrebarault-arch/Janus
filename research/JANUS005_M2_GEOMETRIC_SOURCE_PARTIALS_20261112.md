# JANUS-005 — dérivées partielles exactes des sources géométriques en M2 (2026-11-12)

## Provenance et question
HEAD fixé `e13607e4aca2d9e8c2f762cacaf79c2bad24ff0b`; source authentique `numerics/hr_step55_global_barrier.py`, blob Git `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, fonction `geometry(s)`. Examiner le chemin explicite M2 vers les trois sources Dbar, Wgbar, Wfbar à s=(17/20)^2, **à PG tenu fixe pour la dérivée partielle**. Cela n'est pas la dérivée totale le long de Friedmann, où PG dépend de M2.

## Identités exactes
Pour Lg=A(1+CG s)^2, Lf=A Y(1+CF s)^2, T=B1 Lg²+2 B2 Lg Lf+B3 Lf², T0=B0 Lg²+2 B1 Lg Lf+B2 Lf², Tf=B2 Lg²+2 B3 Lg Lf+B4 Lf², q=sqrt(1-Z1²s), MG=1 :

- ∂Dbar/∂M2 = MG Lg Lf T Z1/q.
- ∂Wgbar/∂M2 = MG (Lg T0 + Lf T q).
- ∂Wfbar/∂M2 = MG (Lf Tf + Lg T q).

La différentiation est exacte car Lg,Lf,T,T0,Tf,q sont indépendants de M2 dans `geometry(s)` à s fixe. Les trois dérivées ne sont pas nulles au bord de la carte prescrite. Par conséquent **tenir ces trois sources fixes lors d'une variation M2 est une hypothèse additionnelle**, non une conséquence des formules Step55. Ce constat ne prouve pas que M2 soit un degré de liberté physique admissible.

## Certification rationnelle locale des signes
Au point s=289/400, toutes les décimales sont interprétées comme rationnels exacts. Poser x=Z1²s, 0<x<1. Les inégalités élémentaires 1-x <= sqrt(1-x) <= 1 et 1 <= 1/sqrt(1-x) <= 1/(1-x) permettent des bornes rationnelles exactes, puisque T>0 et Lg,Lf,Z1>0 :

- D : [Lg Lf T Z1, Lg Lf T Z1/(1-x)] = approximativement [0.0000392947529556, 0.0000392952072082] : strictement positif.
- Wg : [Lg T0+Lf T(1-x), Lg T0+Lf T] = [0.00803484051858,0.00803512380881] : strictement positif.
- Wf : [Lf Tf+Lg T(1-x), Lf Tf+Lg T] = [-0.00447234609087,-0.00447185470886] : strictement négatif.

Les décimales ci-dessus sont des affichages arrondis ; la preuve utilise les fractions exactes et les tests de signe sur les bornes rationnelles.

## Reproduction (Python 3, bibliothèque standard uniquement)
```python
from fractions import Fraction as F
a=F('0.4'); y=F('0.5787707228025044'); b=a*y; s=F(289,400); z=F('.004')
lg=a*(1+F('.0015')*s)**2
lf=b*(1-F('.0012')*s)**2
b0,b1,b2,b3,b4=map(F,['0','1','-4.2383993109','13.6801214252','-38.5117901844'])
T=b1*lg**2+2*b2*lg*lf+b3*lf**2
T0=b0*lg**2+2*b1*lg*lf+b2*lf**2
Tf=b2*lg**2+2*b3*lg*lf+b4*lf**2
x=z*z*s
assert 0<x<1 and T>0 and lg>0 and lf>0
D=(lg*lf*T*z,lg*lf*T*z/(1-x))
Wg=(lg*T0+lf*T*(1-x),lg*T0+lf*T)
Wf=(lf*Tf+lg*T*(1-x),lf*Tf+lg*T)
assert 0<D[0]<=D[1] and 0<Wg[0]<=Wg[1] and Wf[0]<=Wf[1]<0
print([(name,float(v[0]),float(v[1])) for name,v in [('D',D),('Wg',Wg),('Wf',Wf)]])
```
Exécution locale : assertions PASS. Contre-vérification indépendante via `decimal.Decimal` à précision 50 chiffres, calculant directement sqrt(1-x), retrouve respectivement 0.000039294980081272..., 0.008034982163286319..., -0.004472100400570523..., toutes dans les enclosures.

## Limites et suite
Ce résultat concerne **uniquement des dérivées partielles de sources prescrites au point extérieur**, et non une intégration physique, un certificat de signe radial ou une variation admissible. La dérivée totale doit aussi inclure PG(M2), donc Gmom, Gprime, Rhog et Psg, ainsi que la réponse U(s,M2). Les signes des trois dérivées partielles ne fixent pas les signes des traces ni les deux vrais bords. Aucune cellule Step55/58 exécutée ou certifiée.

NEXT_ACTION_EXACT : dériver dPG/dM2 depuis H2 et propager exactement dans Gmom,Gprime,Rhog,Psg, puis dans G(s,U); calculer la sensibilité de l'ODE radiale et vérifier une barrière paramétrique par intervalles, avant toute affirmation de signe extérieur. JANUS-001 : reconstruire les sources originales authentifiées, tests ciblés puis pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
