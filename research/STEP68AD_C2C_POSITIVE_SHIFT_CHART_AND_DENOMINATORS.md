# JANUS — Step68ad-C2c : certification rationnelle de la carte du shift au centre

Date : 2026-10-26. **Résultat local de dénominateurs et de régularisation, pas de certification temporelle.** `GATE_2B OPEN`, `JANUS_R NOT_VALIDATED`.

## Sources originales et authentification

Les **six fichiers complets** ont été lus via le connecteur GitHub sur `research/gate2b-nonhomothetic-transfer` et leurs octets UTF-8 ont été comparés à un SHA-1 Git blob recalculé indépendamment dans un programme JavaScript (SHA-1 vérifié sur le vecteur `abc`). **6/6 PASS** : Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7`, rapports Step68v `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`, Step68ac `16ae8dab3563c17134e4e20f886fb7306dc2e4ba`, Step68ad-B2 `ac961b5b83667a83497497d22a701c24584cb561`. Cela **résout l'authentification positive des trois rapports via le connecteur** ; ce n'est pas une relecture locale d'un clone intégral.

## Nouveau lemme exact (branche physique historique, 0 ≤ r ≤ 1/32)

Dans le véritable Step58 : `K=m2*mg*Lg*Lf*(b1*Sg²+2*b2*Sg*Sf+b3*Sf²)` ; Step68o impose `Sg=r*Lg`, `Sf=r*Lf`, `z=r*Z1`. Avec `s=r²`, `Lg=A*(1+CG*s)²`, `Lf=A*Y*(1+CF*s)²`, il vient **exactement** :

```
y=Lf/Lg = Y*((1+CF*s)/(1+CG*s))²
q(y)=b1+2*b2*y+b3*y²
K/r² = m2*mg*Lg³*Lf*q(y)           (r>0 ; prolongement continu en r=0)
Z_D=(1-z²)^(3/2)/K, Z_K=-z*(1-z²)/K.
```

Les constantes décimales sont les fractions exactes du Step55 original : `A=.4, Y=.5787707228025044, CG=.0015, CF=-.0012, Z1=.004, m2=23.3348939346, mg=1, b1=1, b2=-4.2383993109, b3=13.6801214252`.

Puisque `s∈[0,1/1024]`, on a `y_min=Y*((1+CF/1024)/(1+CG/1024))² > 1/2`, `y≤Y` et `q'(y)=2*b2+2*b3*y≥2*b2+b3=5.2033228034>0`. Ainsi `q(y)≥q(y_min)>0` **sans échantillonnage**. Par bornes rationnelles monotones des facteurs positifs :

```
0.23384592478391242 < K/r² < 0.23385629318172435   (bornes inclusives exactes dans JSON)
|z| ≤ 1/8000 ; 1-z² ≥ 1-1/64000000 > 0.
4.276130247104033 < r² Z_D < 4.27631997831076      (bornes inclusives exactes)
|r² Z_K| < 0.000534539997289.
```

Pour `r² Z_D`, on a employé l'inégalité rationnelle `x² ≤ x^(3/2) ≤ 1` pour `0<x≤1`, avec `x=1-z²` ; aucun arrondi flottant dans le certificat. Ces bornes valent **pour tout le continuum**, y compris le prolongement des expressions *rescalées* à `r=0`.

Autre conséquence du vrai Step68o : le dénominateur de `rho_f` est `beta_f+s*Ffac*KF*Lf`, où `beta_f=sqrt(1+KF²*s)≥1`, `Ffac=U/(2*MF*Lf*Sfr)<0`, `KF=-.0016<0`, `Lf,Sfr,MF>0`. La borne `U<0` sur ce domaine découle des intervalles authentifiés Step68ac (`U0`) et Step68v (`U_s`) : `U(s)≤U0_hi+Us_hi/1024<0`. Donc **le dénominateur de `rho_f` est ≥1**, strictement >1 pour `r>0`.

**Attention :** `K(0)=0` exactement. La formule *non rescalée* `Z_D=(1-z²)^(3/2)/K` diverge comme `r^-2` au centre. C'est une singularité de représentation de la dérivée de shift, **pas** une preuve de singularité physique ni d'inconsistance de la théorie. Le vrai Step58/60 doit exhiber les annulations avec les variations `δD,δK` avant de prendre la limite `r→0`. Sur les sept cellules `r≥1/64`, `K>0` est prouvé et cette singularité de centre ne bloque pas l'évaluation directe.

## Reproductibilité et limites

`PYTHONPATH=. pytest -q tests/test_hr_step68ad_c2c_shift_chart.py` : **12 tests exécutés, 12 PASS, 0 FAIL** en arithmétique `Fraction` exacte. Les tests couvrent le signe de U, le ratio y, q croissant, les bornes de K, trois points physiques (contrôles supplémentaires, non utilisés comme preuve du continuum), les sensibilités du shift, la positivité du dénominateur f-dust, le centre K=0 et le rejet de données incohérentes. Le module `numerics/hr_step68ad_c2c_shift_chart.py` offre une CLI qui, dans un clone complet, vérifie les trois sources originales puis charge et authentifie les trois rapports via `load_pinned` ; **cette CLI intégrée n'a pas été exécutée localement**, car le conteneur n'a pas accès au dépôt complet.

**Aucun des sept signes temporels Step58/60 n'est calculé dans cette étape ; ils restent PENDING.** Ce lemme n'établit ni rang de Dirac, ni lapses admissibles, ni absence du fantôme BD, ni validation JANUS.

## NEXT : Step68ad-C2d

Construire le nouvel adaptateur des jets Step68o sans modifier Step68o : `Jet([U,U_s,U_ss/2,U_sss/6])` à partir des sept cellules C2b, conversion `old.I.hull` vers l'extérieur, vérification `K>0` avec les bornes ci-dessus, et évaluation **effective** du Step58 non-frozen-shift puis du quotient Step60. Si le terme `1/K` élargit trop les intervalles, factoriser explicitement les puissances de `r` dans `δD,δK` avant la division ; ne pas fixer le shift artificiellement et ne pas prétendre à un signe certifié si l'intervalle contient zéro. Ensuite seulement étudier le centre, la structure des contraintes, le rang, les lapses, les bords et les observables.
