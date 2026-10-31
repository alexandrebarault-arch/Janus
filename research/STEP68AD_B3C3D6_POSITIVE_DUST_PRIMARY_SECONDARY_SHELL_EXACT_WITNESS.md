# JANUS b3c3d6 — témoin exact Step58 avec deux poussières positives (31 octobre 2026)

**Statut : PARTIEL. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** Le prochain verrou reste la factorisation **universelle** des B du véritable Step58, puis les six enclosures physiques A/B/E Step55. Ce document apporte un témoin local exact supplémentaire, pas la résolution de ce verrou.

## Provenance et exécution

Sources originales Step45 et Step58 lues sur la branche de recherche et reconstruites octet pour octet, SHA Git blobs respectifs `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Le vrai `physical_operator()` Step58 a été exécuté, avec le shim d'import Step57 **minimal** ; Step57 complet et les moteurs Step46/55/DOP853 physiques n'ont pas été rejoués. Ne pas confondre cette famille avec la solution Step55.

## Témoin rationnel, puis famille exacte

Choisir les métriques locales `Lg=Lf=Sg=Sf=1`, `Mg2=Mf2=m2=1`, `beta0=-5,beta1=1,beta2=beta3=0,beta4=-2`, `z=3/5`, `K=1`, poussières `pg=7/4>0,pf=1>0` et pentes `tg_r=tf_r=0`. Les autres jets non spécifiés sont nuls, sauf `Sg_r=Sf_r=pSg=pLf=pSf=1`, `pLg_r=1/4` et les jets suivants, où `a=z_r` reste un symbole réel :

```text
pLg_rr = -3/2 - (125/64) a
Sg_rrr = 29/16 - (75/128) a
```

La substitution exacte dans le **vrai opérateur** et les contraintes originales donne, identiquement pour tout `a` :

```text
Fz = Fz_r = Hg = Hg_r = Hf = 0
C = -9/5 - 5a/4
B_M = 0
B_N = -27/25 - 3a/4 = (z/Lg) C
E_N = E_M = 0
```

Ainsi `a=0` donne un **contre-exemple exact à l'inférence** « primaires et leurs premiers jets ⇒ B_N=0 » : `C=-9/5`, `B_N=-27/25`. En imposant aussi la secondaire `C=0`, `a=-36/25`, les quatre coefficients `B_N,B_M,E_N,E_M` s'annulent sur ce témoin local. Deux contrôles négatifs rompent respectivement `Fz_r` et `Hg_r` et détruisent les identités B correspondantes. Cela montre concrètement pourquoi les contraintes dérivées et la secondaire sont nécessaires.

**Portée rigoureuse :** identité exacte sur une famille de jets locaux avec poussières positives, non factorisation universelle dans l'idéal des contraintes ; elle ne construit pas une solution radiale satisfaisant les contraintes sur un intervalle. Les dérivées de shift d'ordre supérieur et la compatibilité globale ne sont pas certifiées. Aucun ratio de lapses physique, aucune condition aux deux vrais bords, aucune conclusion Dirac ou cosmologique ne suit.

## Reproductibilité

`PYTHONHASHSEED=0 PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_step58_positive_dust_shell_v2.py' -q` : **9 tests PASS, 0 FAIL, 0 SKIP** ; `python -m compileall -q numerics/hr_b3c3d6_step58_positive_dust_shell_v2.py tests/test_hr_b3c3d6_step58_positive_dust_shell_v2.py` : **PASS** ; exécution CLI du module : **PASS**. Ces tests réutilisent les moteurs originaux, ils ne constituent pas une vérification physique indépendante.

Fichiers : `numerics/hr_b3c3d6_step58_positive_dust_shell_v2.py` blob `814c62f2c37baea304bb64863c73fdf176a84fb2` ; `tests/test_hr_b3c3d6_step58_positive_dust_shell_v2.py` blob `90753aa949bb9e70424d551b31d00510307f7887` ; rapport JSON `research/reports/gate2b-b3c3d6-original-Step58-positive-dust-primary-secondary-family.json` blob `3127649e141849b7ec187584452845eeb30ba727`.

**Étape suivante inchangée :** démontrer ou réfuter l'appartenance universelle `B_M` et `B_N-zC/Lg` à l'idéal de `Fz,Fz_r,Hg,Hg_r` dans la carte `K>0`, avec un certificat algébrique explicite ; imposer `C=0` sur Step55 et produire six enclosures A/B/E aux quatre rayons exacts, puis BVP de lapses positifs aux deux vrais bords, Dirac/4D/stabilité/observables.
