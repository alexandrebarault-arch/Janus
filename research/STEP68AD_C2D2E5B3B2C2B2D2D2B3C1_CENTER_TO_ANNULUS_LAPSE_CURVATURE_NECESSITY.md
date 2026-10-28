# JANUS — 68ad-C2d2e5b3b2c2b2d2d2b3c1 : condition nécessaire de couche centrale pour les lapses

28 octobre 2026. **THÉORÈME CONDITIONNEL, PAS DE LIMITE STEP58 AU CENTRE CERTIFIÉE. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Données authentifiées et résultat nouveau

Le certificat original Step58 `research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json` (blob `0c688d6648e16064b1eb4e8ad9c55e7b44a95947`) couvre 225 feuilles sur `[1/64,1/32]`. L'intervalle initial `[1/64,449/28672]` donne, par calcul rationnel exact sur `A_N>0,A_M<0`, **`rho(1/64)=M/N=-A_N/A_M<17/25`**, sous l'hypothèse non encore vérifiée que les coefficients de dérivées des lapses s'annulent sur la coquille complète. Il ne certifie PAS `rho(0)` et ne démontre pas l'existence de lapses globaux.

La géométrie Step55 authentique (blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`) impose `tg'=kg*r*Lg`, `tf'=kf*r*Lf`, `z=r/250`, `kg=3/2500`, `kf=-1/625`, `Lg(0)=2/5`, `Lf(0)=(2/5)*q`, `q=5787707228025044/10^16`. En notant `rho=M/N`, le shift instantané préservant la différence des horloges est
`Vrel/N=[rho*sqrt(1+kf²r²)-sqrt(1+kg²r²)-(r/250)*(1/Lg+rho/Lf)*kg*r*Lg]/[r*(kg*Lg-kf*Lf)]`.

**Développement analytique indépendant vérifié avec SymPy (trois identités exactes) :** si `rho=rho0+rho1*r+rho2*r²+...`, `d0=kg*Lg(0)-kf*Lf(0)>0`, alors `r*Vrel/N -> (rho0-1)/d0`. Si `rho0=1`, `Vrel/N -> rho1/d0`. Si en outre `rho1=0` et la parité analytique des champs est satisfaite, `Vrel/N=r*(rho2-ccrit)/d0+O(r³)`, avec les constantes exactes
`d0=3321926807006261/3906250000000000000` et `ccrit=226687120771331833/18086585087578262500000>0`.

Si `N(0)>0` et `Vrel` reste fini, il faut **`rho(0)=1`**. Si le shift radial est lisse au centre (`V=O(r)`) et les lapses sont des scalaires sphériques lisses, alors `rho'(0)=0`; la pente de `V/N` est déterminée par `rho2`, sans obstruction automatique.

## Nouveau critère quantitatif conditionnel

Si `rho` est `C²` sur `[0,1/64]`, `rho(0)=1`, `rho'(0)=0`, et si l'équation réduite Step58 est réellement valide à `r=1/64`, alors `rho(1/64)<17/25` entraîne, par le théorème des accroissements finis et Taylor-Lagrange, l'existence de `eta,xi∈(0,1/64)` tels que

`rho'(eta)<-512/25` et **`rho''(xi)<-65536/25`**.

Ainsi une borne physique indépendante `rho''(r)>=-65536/25` sur tout `[0,1/64]` serait incompatible avec ces hypothèses. **Une courbure aussi forte n'est pas une singularité en soi**, et aucune borne Step58 correspondante n'a été démontrée. Il n'existe donc PAS de no-go physique ici.

## Vérifications et portée

921 assertions rationnelles exactes BigInt V8 PASS, 0 FAIL, couvrant la totalité des 225 feuilles, la borne renforcée au premier point, les fractions centrales et les seuils MVT. Quatre données volontairement falsifiées ont été rejetées. Trois identités limites ont été vérifiées séparément par SymPy (pas un oracle physique indépendant). Les sources originales Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`, Step55 et le certificat ont été relus et leurs SHA authentifiés. **Moteurs Python originaux Step58/Step55 non réexécutés ; Node CLI non exécuté dans ce passage.**

La vraie limite `-A_N/A_M` à `r=0`, l'annulation des coefficients des jets de lapses, la préservation temporelle complète, le générateur amélioré, le quotient temporel, le rang Dirac six couples, les chartes K=0/J=0, la dynamique 4D, stabilité et observables restent **NON CERTIFIÉS**.

**Prochaine étape b3c2 :** calculer les premiers coefficients centraux des `A_N,A_M` originaux Step58 sur la branche Step55 avec jets cohérents et réduction des `N',M'`, puis certifier `rho(0)` et, si `rho(0)=1`, borner `rho''` sur `[0,1/64]`. Ne pas extrapoler la borne annulaire jusqu'au centre.
