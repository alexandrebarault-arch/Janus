# b3c3d6 — Obstruction algébrique exacte de fermeture radiale sur une tranche à trois paramètres (31 octobre 2026)

**Verdict : résultat exact mais STRICTEMENT RESTREINT. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Périmètre et provenance

Les sources Step45 et Step58 du dépôt ont été lues par le connecteur GitHub, blobs respectifs `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et `802c23aebd41780d8c462f1aa1711707fe4ee88f`. **Le moteur original GitHub n'a PAS été exécuté localement pendant cette session** : le clone Git est inaccessible par DNS. Les polynômes ont été recalculés avec une transcription indépendante des formules Step45/58, testée localement. Le test publié appelle directement les deux modules originaux lorsqu'il est exécuté dans le dépôt ; son exécution locale a utilisé des wrappers explicitement identifiés comme transcription. Ne pas confondre ces deux niveaux de vérification.

Tranche locale : `Lg=Lf=Sg=Sf=Mg2=Mf2=m2=1`, `beta0=-5,beta1=1,beta2=beta3=0,beta4=-2`, `z=3/5`, poussières `pg=7/4,pf=1` strictement positives, `a=z_r,b=Sf_r,c=Lf_r`. Les autres jets sont gelés comme dans le module. `K=1>0`. La résolution triangulaire de `Fz=Hg=Fz_r=Hg_r=0` donne :

```text
pLg_r   = 1/4
Sg_rr   = 0
pLg_rr  = -(125*a+48*c+96)/64
Sg_rrr  = -(75*a+128*b+80*c-360)/128
```

Sur cette famille, les calculs symboliques donnent `C=-(25a+24b+12)/20`, `Hf=b²-2bc-1`, `B_N=3C/5`, `B_M=E_N=E_M=0`. Les dérivées radiales calculées avec les jets restants gelés sont :

```text
Fz_rr = -(5625*a²+4000*a*c+8600*a+1024*b+3712*c-1344)/1024
C_r   = -(375*a²+640*a*b+920*a-384*b*c+192*b-128*c+160)/320
Hf_r  = (75*a-192*b²*c+256*b*c²-256*b-176*c+160)/64
```

## Preuve exacte de non-fermeture sur cette tranche

`C=0` impose `a=-(24b+12)/25`. `Hf=0` impose `b≠0` puis `c=(b²-1)/(2b)`. Dans les deux numérateurs précédents, après substitution :

```text
Frr = 16*P(b)/b,     P(b)=204b³-72b²-141b-56
Cr  = -16*T(b)/(5b), T(b)=144b³+224b²+b-20
```

Le **certificat de Bézout intégral** est :

```text
U(b)=4708409040b²+5217306528b-2808576443
V(b)=-6670246140b²+5338958712b+2939061345
U(b)*P(b)+V(b)*T(b)=98499053908 ≠ 0.
```

Donc `P=T=0` est impossible même sur les nombres complexes. Contrôles indépendants de cette identité : `resultant(P,T)=4727954587584 ≠ 0`, et base de Gröbner de l'idéal `<C,Hf,Frr,Cr>` égale à `[1]`. **Aucun triplet complexe `(a,b,c)` de cette tranche gelée ne satisfait simultanément `C=Hf=Fz_rr=C_r=0` après les quatre contraintes primaires et leurs premières dérivées.** La condition `Hf_r=0` n'est même pas nécessaire à cette exclusion.

## Limites et suite

C'est une obstruction à **cette fermeture de jets gelés**, pas à la prolongation radiale générale : les autres jets libres peuvent être ajustés. Cela ne réfute ni l'identité universelle candidate `B_N=z*C/Lg` modulo `Fz,Fz_r,Hg,Hg_r`, ni l'existence de solutions Step55. Aucun des six coefficients physiques Step58 aux quatre rayons, BVP de lapses positifs à deux bords, Dirac, dynamique 4D, stabilité ou observables n'est certifié.

Exécution locale : **6 unittest PASS, 0 FAIL, 0 SKIP**, `compileall` PASS, CLI certificat PASS ; **reconstruction indépendante**, non replay original. Les octets des deux fichiers Python publiés ont été comparés à leurs blobs Git, de même pour le JSON. Prochaine priorité : calcul universel du résidu inférieur `B_N-z*C/Lg-beta*Hg_r` sur la coquille complète holonome, puis enclosures physiques Step55/58 et BVP positif aux vrais bords.
