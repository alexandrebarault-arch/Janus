# JANUS b3c3d6 — comparaison physique conditionnelle Step58 au centre (31 octobre 2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Nouvelle conséquence exacte **sur le continuum restreint** `0<r<=1/32`, obtenue par composition de **deux certificats physiques antérieurs**, sans rejeu des moteurs originaux dans cette session.

## Théorème conditionnel, et définition précise du comparateur

Sur la famille physique Step55, sous les hypothèses de régularité/centre Step49 et les certificats Step68v/Step68ad-B2, l'archive Step68ad-B2 prouve pour **tout** `0<=s=r²<=1/1024` :

`-1414170375015186192017477/69938619264706447051250697260 <= U_ss(s) <= -281308311835510868820846/14012170704330665327521777975 < 0`.

Le certificat de sensibilité du **Step58 original** sur `Fz=Hg=0` donne `dA_M/dU_ss=-r^6 c(r)`, avec `c(r)>0` et

`c(r)=2 Z1 m2 Mg2 T(s) sqrt(1-Z1²s)/(Mf2 Lf Sfr (1+q))`, `q=s U KF/(2 Mf2 Sfr beta)`, `beta=sqrt(1+KF²s)`.

La dépendance est **affine** en `U_ss` lorsque `r,U,U_s` et tous les autres jets de la coquille sont fixés (audit exact du coefficient de `pSf'` du Step58 original). Comparons donc `A_M^{phys}` à `A_M^{affine-hol}` : le second utilise **au même point les mêmes U et U_s**, mais le prolongement holonome `U_ss=0`. Il ne faut surtout **pas** le confondre avec l'« affine » historique **mixte** qui utilise déjà `pLfr=rG` et reproduit les coefficients du quadratique/cubique.

Alors, **à chaque** `0<r<=1/32`, le calcul en fractions strictes donne :

`63/100000 < (A_M^{phys}(r)-A_M^{affine-hol}(r))/r^6 < 13/20000`.

Autrement dit `A_M^{affine-hol}<A_M^{phys}`, et la différence est **strictement d'ordre au plus r^6**, avec un encadrement non nul du quotient. Les bornes rationnelles internes calculées sont environ `0.000639303810905 < quotient < 0.000643952358586`. À `r=1/32`, la différence est comprise approximativement entre `5.954e-13` et `5.998e-13`. Ces décimales sont **indicatives** : les fractions et les deux seuils simples stricts font foi.

## Calcul exact et couverture du continuum

On utilise `S=1/1024`, `Lg=A(1+CG*s)^2`, `Lf=B(1+CF*s)^2`, `Sfr=B(1+CF*s)(1+5 CF*s)` et les constantes décimales Step55 **traitées comme fractions exactes**. Les bornes monotones sur `Lg,Lf,Sfr` et les bornes de produit signées de `T=B1 Lg²+2 B2 Lg Lf+B3 Lf²` donnent `1/10<T_lo<=T_hi<1/9`. La barrière globale antérieure `-67/12500<U<-229/50000` donne `0<q<qmax<1/500` pour `r>0`. Enfin `sqrt(1-Z1²s)>1-Z1² S` et `beta>=1`. Ces inégalités enferment `c(r)` uniformément, sans échantillonner les rayons. Multiplier par les bornes **négatives** de `U_ss` avec le bon ordre produit le sandwich ci-dessus.

**Portée :** ce résultat est une **comparaison conditionnelle entre deux prolongements** du seul coefficient `A_M`, et non une enclosure de `A_M` lui-même, encore moins des six coefficients `A_N,A_M,B_N,B_M,E_N,E_M`. Il ne donne aucun signe de `A_M`, aucune annulation exacte des B/E et aucune solution globale de lapses positifs. Il ne s'étend **pas** aux quatre rayons `1/4,1/2,7/10,17/20`, car le certificat continu de signe de `U_ss` utilisé ne couvre que `r<=1/32`.

## Provenance, tests et limites de reproduction

Sources antérieures **lues sur GitHub et SHA blobs authentifiés dans cette session** :
- Archive physique Step68ad-B2 `research/reports/gate2b-step68ad-B2-original-G-Uss-Usss.json` : `ac961b5b83667a83497497d22a701c24584cb561`.
- Source Step68ad-B2 `numerics/hr_step68ad_b2_physical_center_higher_jets.py` : `89ce02af12145eb8ab6bdcc354649571dd5da179`.
- Original Step58 `numerics/hr_step58_temporal_operator.py` : `802c23aebd41780d8c462f1aa1711707fe4ee88f`.
- Sensibilité Step58 `numerics/hr_b3c3d6_step58_am_uss_sensitivity_bound.py` : `d7530900082696d7b4fc6f1bd720010da71c37f0`.

**Tests exécutés cette session** dans `/mnt/data/janus_20261031_center` : `PYTHONPATH=. python -m unittest discover -s tests -v` : **6 PASS, 0 FAIL, 0 SKIP** ; `python -m compileall -q numerics tests` : **PASS** ; `PYTHONPATH=. python -m numerics.hr_b3c3d6_center_step58_affine_gap` : **PASS**. Trois contrôles négatifs : signe U_ss non démontré, intervalle inversé et rayon hors domaine. Ces tests vérifient la **recombinaison rationnelle** des certificats antérieurs, pas un rejeu physique original. **Aucun** Step45/46/55/58, DOP853, BVP ou Dirac physique n'a été rejoué.

Nouveaux fichiers : `numerics/hr_b3c3d6_center_step58_affine_gap.py` blob `2643747e9cbfc12110de444d5237adf465ed7f6c` ; `tests/test_hr_b3c3d6_center_step58_affine_gap.py` blob `f028193f27351f5b26d5fe81c9ec8d9baf367ec6`. Ces blobs sont égaux **aux octets locaux testés**.

**Prochaine difficulté INCHANGÉE :** exécuter le vrai Step58 original sur les jets physiques exacts aux quatre rayons, certifier les six enclosures A/B/E et leurs factorisations ; DOP853 au rayon exact si nécessaire ; BVP lapses strictement positifs à deux vrais bords, puis Dirac six couples, jauge temporelle, dynamique 4D, stabilité et observables. Ne pas promouvoir JANUS.
