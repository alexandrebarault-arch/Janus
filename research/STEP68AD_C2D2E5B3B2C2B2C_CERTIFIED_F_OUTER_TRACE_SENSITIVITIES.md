# JANUS — 68ad-C2d2e5b3b2c2b2c : sensibilités extérieures des quatre traces f

**27 octobre 2026. Certificat rationnel spatial, à géométrie et shift fixes. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Théorème certifié et hypothèses

Sur la famille sphérique Step55/68o certifiée par les modules physiques originaux Step45/46/55 (certificats b2 et b2b), pour `s=r²∈[0,289/400]`, `|lambda|≤1/5000`, et au bord `R=17/20`, on dispose de `681/100000<v=∂lambda U<689/100000`. Les encadrements de `G_U`, `G_Pg`, `U`, `V=G`, `rho_f` et `Dbar(R)` sont repris **tels quels** des certificats antérieurs, dont les SHA sont épinglés dans le programme. La présente étape ne réexécute pas les moteurs Python originaux ; elle propage leurs bornes rationnelles déjà publiées.

La chaîne exacte de différentiation est :
```
delta V = G_U*v + G_Pg
delta pLf = R²*v
delta pLf' = R*delta V
delta pf = H*delta pLf + chi*delta pLf'
delta pSf = (Lf/Sfr)*delta pLf' - (R*kf*Lf/Sfr)*delta pf
```
où `H=-(A_U+rho_f*D_U)/D`, `chi=R*U/(2*Mf2*Sfr*D)`, `D=sqrt(1+kf²s)+kf*s*U/(2*Mf2*Sfr)`, `D_U=kf*s/(2*Mf2*Sfr)`, `A_U=U/(2*Mf2*Lf)-(V-s*Dbar/Lf)/(2*Mf2*Sfr)`. Ce sont les identités exactes de la primaire originale Step46 et du jacobien formel précédemment audité. La borne `1≤sqrt(1+x)≤1+x/2` pour `x≥0` est utilisée ; toutes les autres opérations sont des fractions rationnelles exactes et des intervalles fermés avec propagation extérieure des dépendances.

**Résultats stricts uniformes**, les bornes ci-dessous étant moins serrées que celles du JSON (fractions dirigées vers l'extérieur au pas `10^-12`) :

| Dérivée au bord | Borne démontrée |
|---|---|
| `∂lambda V(R)` | `0.0135 < ∂lambda V < 0.0139` |
| `∂lambda pLf(R)` | `0.0049 < ∂lambda pLf < 0.0050` |
| `∂lambda pLf'(R)` | `0.0115 < ∂lambda pLf' < 0.0118` |
| `∂lambda pf(R)` | `-0.020 < ∂lambda pf < -0.011` |
| `∂lambda pSf(R)` | `0.0115 < ∂lambda pSf < 0.0118` |

Le calcul certifie aussi `-2<H<-0.6`, `-0.84<chi<-0.71`, `1<D<1.01`. Les bornes sont uniformes sur l'intervalle entier de lambda, pas une différence finie ni un échantillonnage. L'intervalle `V` provient du tube b2 ; `G_U/G_Pg/v` du certificat b2b. Les dépendances négligées élargissent les intervalles, sans invalider leurs signes.

## Conséquence de bord, soigneusement limitée

Chacune des quatre traces canoniques f considérées est strictement monotone en lambda sur la famille à un paramètre : `pLf`, `pLf'`, `pSf` croissent et `pf` décroît. **Si une seule de ces traces est imposée égale à sa valeur à lambda=0, alors cette famille impose lambda=0** (théorème des accroissements finis). Ce n'est **pas** un théorème d'obstruction générale JANUS : d'autres familles, conditions mixtes, contretermes dépendant des lapses et espaces de bords peuvent exister.

Cette preuve ne choisit aucune condition de bord physique, n'établit aucune différentiabilité fonctionnelle du Hamiltonien original et ne calcule pas le rang de Dirac. Le rang 2 du jacobien formel Step46 est distinct du rang de Dirac.

## Reproductibilité et verrous

Exécution : `node tests/test_hr_step68ad_c2d2e5b3b2c2b2c_f_outer_sensitivities.cjs` ou exécution V8 du même fichier avec le module CJS chargé. **PASS 37 exact rational assertions; FAIL 0**. Le certificat `research/reports/gate2b-step68ad-C2d2e5b3b2c2b2c-f-outer-sensitivities.json` est produit par `certificate()` ; chaque fraction affichée est un encadrement rationnel extérieur de la valeur calculée. Le certificat et le programme sont relus après publication pour vérifier leur identité octet par octet et leurs SHA Git.

**Prochaine étape :** sélectionner et tester des conditions physiques de bord avec variations indépendantes des lapses, déterminer des contretermes autorisés et construire l'oracle fonctionnel original non-IBP à six couples (rang, tertiaires, K=0/J=0), puis dynamique 4D, stabilité et observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
