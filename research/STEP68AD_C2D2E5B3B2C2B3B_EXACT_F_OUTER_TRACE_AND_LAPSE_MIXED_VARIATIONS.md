# JANUS — 68ad-C2d2e5b3b2c2b3b : traces f extérieures et variations des lapses

27 octobre 2026. **Résultat exact mais partiel, sans choix de conditions aux limites physiques. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources et calcul

Le certificat de tube original Step45/46/55 (blob `012e70e49b41cc3180da423c3962d279e3909a26`) borne uniformément `U=pLf/r²`, `V=pLf'/r` et `rho_f=pf/r²` pour tout `|lambda|<=1/5000` sur `0<=r<=17/20`. Ses bornes rationnelles ont été reprises **sans prétendre réexécuter les moteurs originaux**. À `R=17/20`, la reconstruction primaire originale Step46 donne exactement `pSf=(-R³ Dbar+Lf*R*V-(R²*rho_f)*R*kf*Lf)/Sfr`, où `Dbar=m² Mg² Lg Lf T z1/sqrt(1-z1² R²)`, `Sfr=b(1+cf R²)(1+5cf R²)`, `T=beta1 Lg²+2 beta2 Lg Lf+beta3 Lf²`. La racine est encadrée exactement par `99999/100000 < sqrt(1-z1² R²) < 1`, avec preuve par élévation au carré rationnelle.

Par propagation de fractions **exactes**, on obtient sur tout le tube : `pLf(R)<0`, `pLf'(R)<0`, `pSf(R)<0`, `pf(R)>0`. Les fractions de toutes les bornes sont dans le JSON ; les intervalles sont volontairement larges (ils ne certifient aucune dérivée en lambda). Ce sont des **traces canoniques f**, pas des conditions de bord sélectionnées.

## Lapses et contretermes

La différence `H_original-H_IBP=[B]_0^R` est héritée de l'audit b3a, avec `B=Ag N+Af M-z pLg(N+q M)`, `Ag=2 Mg² R Sgr`, `Af=2 Mf² R Sfr`, `q=Lg/Lf`. Pour une variation indépendante des multiplicateurs `N,M` et du paramètre `lambda`, à géométrie et shift fixes :

`delta B=(Ag-z pLg) delta N+(Af-z q pLg) delta M-z a(N+q M)delta lambda`, `a=partial_lambda pLg(R)>0`.

Les dérivées croisées `partial_lambda partial_N B=-z a<0` et `partial_lambda partial_M B=-z a q<0` sont **exactes et non nulles**. Donc aucun contreterme de bord ne dépendant **que de lambda** et indépendant des lapses ne peut annuler la variation `partial_lambda B` pour **toutes** les valeurs indépendantes de `N,M`. Un contreterme dépendant des lapses, une restriction des variations ou un espace de bord différent pourraient convenir. Ceci est un résultat de non-séparabilité du **B de différence original–IBP**, **pas** un théorème général de non-différentiabilité de l'Hamiltonien ni une interdiction des contretermes physiques. En particulier, des variations `delta N,delta M` ne doivent pas être traitées comme des variations canoniques sans définir le problème variationnel étendu.

## Vérification, portée et suite

Le programme `scripts/hr_step68ad_c2d2e5b3b2c2b3b_f_traces_lapses.cjs` et le wrapper `tests/test_hr_step68ad_c2d2e5b3b2c2b3b_f_traces_lapses.cjs` ont exécuté **25 assertions rationnelles BigInt PASS, 0 FAIL dans V8**. Certificat `research/reports/gate2b-step68ad-C2d2e5b3b2c2b3b-f-traces-lapses.json`. Les moteurs originaux Step45/46/55 ne sont **pas** réexécutés dans cette étape, mais leur certificat physique antérieur est vérifié par référence au blob.

**Non démontré :** dérivées réelles `partial_lambda U(R)`, `partial_lambda pSf(R)`, bords physiquement admissibles, fonctionnelle originale différentiable sur un espace de champs complet, matrice de Dirac à six couples, rang, tertiaires, lapses globaux, K=0/J=0, dynamique 4D, stabilité, observables. **Prochaine étape 68ad-C2d2e5b3b2c2b3c :** sensibilité variationnelle authentique `v=partial_lambda U` jusqu'au bord, carte différentielle des traces f, et choix de conditions de bord/contretermes avant le véritable oracle Dirac.
