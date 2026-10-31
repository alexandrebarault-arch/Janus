# JANUS b3c3d6 — factorisation universelle de B_M sur Fz=0 (31 octobre 2026)

**Avancée exacte, partielle : GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Le vrai opérateur Step58 a été exécuté sur les sources originales Step45 et Step58, blobs Git `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et `802c23aebd41780d8c462f1aa1711707fe4ee88f`, reconstruits octet pour octet. Seul l'import Step57 a été remplacé par un shim minimal ; le Step57 complet n'a pas été exécuté.

## Théorème exact sur le vrai Step58

Sur la carte régulière `K>0, Lg>0, Lf>0, |z|<1`, en imposant **seulement** `Fz=0` par
`pLg_r=(pSg*Sg_r+pg*tg_r-K*z/sqrt(1-z²))/Lg`, l'identité suivante est universelle pour les autres jets canoniques et paramètres de l'opérateur :

`B_M = -3*z*(1-z²)/(Lg*Lf²) * D_r(Fz)`.

Ainsi, **`Fz=Fz_r=0 => B_M=0`**, sans hypothèse `Hg=Hg_r=Hf=C=0`. Le résidu complet, et non une simple dérivée de plus haut jet, est ramené exactement à zéro par expansion symbolique puis `cancel`. Un contrôle de degré établit que le résidu avant substitution est quadratique au plus en `pLg_r`. Cela ne démontre pas que `B_M=0` hors de la coquille, ni que les lapses sont admissibles.

## Réduction triangulaire de B_N, encore incomplète

Poser `Delta=B_N-z*C/Lg`, `v=pLg_rr`, `w=Sg_rrr`, `R=sqrt(1-z²)` et `J=K/R+z*Fz`. Trois dérivées exactes **hors coquille** du vrai Step58 sont prouvées par simplification symbolique ; sur `Fz=0`, elles donnent :

`partial_v B_M=3*z*(1-z²)/Lf²`

`partial_v Delta=z*(1-z²)/(Lg*Lf)`

`partial_w Delta=-2*Mg2*Sg*(1-z²)/(Lg²*Lf)`.

De plus, `partial_v Fz_r=-Lg`, `partial_v Hg_r=-z`, `partial_w Hg_r=2*Mg2*Sg/Lg`, `partial_w B_M=0`. Avec `beta=-(1-z²)/(Lg*Lf)`, le résidu `Delta-beta*Hg_r` est indépendant de **ces deux jets supérieurs** sur `Fz=0`. **Son annulation pour tous les jets inférieurs n'est PAS démontrée** : il serait faux d'en déduire déjà `B_N=z*C/Lg` universellement. Les familles exactes précédentes restent des témoins locaux, non un certificat d'idéal global.

## Reproductibilité et limites

Commande réellement exécutée : `PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_step58_B_jet_triangular.py' -q` : **8 PASS, 0 FAIL, 0 SKIP** ; `python -m compileall -q numerics tests` : **PASS** ; CLI du module : **PASS**. Un premier essai de test a échoué sur une coquille de test `S.One` inexistante, corrigée avant les huit tests finaux. Les tests ne sont pas une revue mathématique indépendante du code source original.

Code : `numerics/hr_b3c3d6_step58_B_jet_triangular.py`, blob `e5e65b04fdb20a0348174fa183c56a46d0662f5f`. Tests : `tests/test_hr_b3c3d6_step58_B_jet_triangular.py`, blob `a241ac64b79c180d5845f1e8c9bef720ea60c618`. Rapport CLI : `research/reports/gate2b-b3c3d6-Step58-universal-BM-factor-and-BN-principal-jets.json`, blob `1869abc7c406fa76bed68140ab1bb232246e13da`.

**Prochaine étape :** terminer ou réfuter la factorisation de `B_N-z*C/Lg` sur `Fz,Fz_r,Hg,Hg_r` en traitant le résidu des jets inférieurs ; imposer ensuite `C=0` sur le véritable Step55, encloser les six `A_N,A_M,B_N,B_M,E_N,E_M` aux quatre rayons exacts `1/4,1/2,7/10,17/20` ; DOP853 si besoin, BVP positif deux vrais bords, Dirac/4D/stabilité/observables. Aucun de ces derniers objectifs n'est certifié ici.
