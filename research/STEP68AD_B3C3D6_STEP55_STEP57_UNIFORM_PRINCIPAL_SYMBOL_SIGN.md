# JANUS — b3c3d6 : non-annulation quantitative du symbole `eta''` de Step57 sur Step55

29 octobre 2026. **Théorème exact, limité au symbole fonctionnel de Step57 évalué sur la géométrie prescrite Step55.** `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.

## Sources et hypothèses

Sources originales inspectées en direct par le connecteur GitHub, branche `research/gate2b-nonhomothetic-transfer` : `numerics/hr_step55_global_barrier.py` (blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`), `numerics/hr_step57_secondary_principal_symbol.py` (blob `bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`) et, à titre de contexte distinct, `numerics/hr_step58_temporal_operator.py` (blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`). Les expressions Step57 sont **transcrites et simplifiées**, sans exécuter les moteurs originaux : ce contrôle n'est pas une vérification indépendante du calcul de la parenthèse canonique Step57. La borne rationnelle `K/r²>9/40` est reprise du certificat Bernstein b3c3d6 antérieur, elle n'est pas recalculée ici.

Sur la coquille de shift `Fz=0`, `K>0`, avec `z=r/250`, `Q=sqrt(D²+K²)=K/sqrt(1-z²)`, les coefficients originaux Step57 de `eta''*M` et `eta''*N'` dans la parenthèse **smeared** `{int eta C_red, H_tot}` sont :

`c_M=-K²/(Lg*Lf²*Q)=-K*sqrt(1-z²)/(Lg*Lf²)` ;

`c_Nprime=-2*Mg2*Sg*Sg'*K²/(Lg²*Q²)=-2*Mg2*Sg*Sg'*(1-z²)/Lg²`.

**Attention : ce ne sont pas les coefficients `B_M,B_N` de l'opérateur temporel local Step58.** Le smearing `eta''` et les intégrations par parties empêchent cette identification directe.

## Certificat uniforme sur l'anneau physique prescrit

Sur `0<r<=17/20`, `s=r²`, Step55 donne `Lg=(2/5)(1+0.0015s)²`, `Lf=(2/5)*0.5787707228025044*(1-0.0012s)²`, `Sg=r*Lg`, `Mg2=1`. On a `Lg<=Lg(289/400)`, `Lf<=Lf(0)`, `1-z²>=1-(17/5000)²` et `sqrt(1-z²)>99999/100000` (dernière inégalité vérifiée après élévation au carré). En utilisant `K/r²>9/40`, l'arithmétique rationnelle donne

`-c_M/r² > (9/40)*(99999/100000)/(Lg(289/400)*Lf(0)²) > 10`.

De plus `Sg'/Lg=(1+5*0.0015s)/(1+0.0015s)>=1`, donc

`-c_Nprime/r >= 2*(1-(17/5000)²) = 24999711/12500000 > 19999/10000`.

Les deux coefficients sont donc **strictement négatifs et non nuls en tout point de l'anneau ouvert**, avec les bornes quantitatives `c_M < -10 r²` et `c_Nprime < -(19999/10000) r`. Au centre, `lim(c_M/r²)≈-10.90817664306727` (valeur décimale illustrative, fraction exacte dans le rapport) et `lim(c_Nprime/r)=-2`. Les coefficients eux-mêmes s'annulent respectivement à l'ordre `r²` et `r` en `r=0` : **aucun rang uniforme jusqu'au centre n'est établi**.

## Portée et verrou

Le résultat exclut une annulation accidentelle de ces **deux coefficients du symbole principal fonctionnel** sur la géométrie Step55 hors centre. Il est indépendant de l'inconnue radiale `U(s)` et ne démontre ni l'indépendance physique de directions canoniques après quotient de jauge, ni la tangence Dirac, ni les signes `B_N,B_M` de Step58, ni l'existence de lapses positifs satisfaisant les vrais bords. Le vrai probe original Step58 à `R=17/20` reste **NON EXÉCUTÉ** : le conteneur local ne résout pas `github.com`, bien que le connecteur GitHub lise et écrive correctement. Ne pas présenter ce lemme comme une solution de b3c3d6.

## Reproductibilité

`PYTHONPATH=. python -m numerics.hr_step68ad_b3c3d6_step55_dirac_principal_sign` : 14 assertions `assert` exactes PASS (identités, bornes rationnelles, limites), 0 FAIL après correction locale d'une substitution `s=r²` détectée lors du premier essai. `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_step68ad_b3c3d6_step55_dirac_principal_sign.py' -v` : 5 cas PASS, non indépendants, dont une garde négative de SHA. Le rapport JSON est la sortie directe du module. Le code contient une vérification SHA Git blob facultative pour les sources originales lorsqu'elles sont présentes dans un checkout complet.

**Prochaine étape inchangée :** exécuter réellement `python -m numerics.hr_step68ad_b3c3d5_temporal_boundary_jet_rank --probe-original` avec Step45/55/57/58/Step68o/b3c2 authentiques, certifier les coefficients `A_N,A_M,B_N,B_M,E_N,E_M`, dérivées et zéros, raccord central, lapses positifs et vrais bords ; ensuite pullback Dirac, charges/générateurs, quotient jauge temporelle, six couples, `K=0/J=0`, 4D, stabilité et observables. `GATE_2B OPEN ; JANUS_R NOT_VALIDATED`.
