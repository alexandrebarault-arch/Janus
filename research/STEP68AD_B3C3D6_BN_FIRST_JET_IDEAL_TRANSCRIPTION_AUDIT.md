# b3c3d6 — Annulation exacte du résidu de premiers jets B_N sur transcription indépendante (2026-10-31)

**Statut : preuve algébrique exacte sur la transcription des formules Step45/58, sous réserve du rejeu authentique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Théorème et preuve calculatoire

Sur la carte régulière `K=m2*Mg2*Lg*Lf*At>0`, `Lg,Lf,Sg,Mg2>0`, `|z|<1`, définir `h=sqrt(1-z²)` et
`R=B_N-z*C/Lg+(1-z²)/(Lg*Lf)*D_r(Hg)`. Le théorème précédent vérifie exactement que les dérivées de `R` par rapport à `Sg_rrr,pLg_rr,Lg_rr,tg_rr` sont multiples de `Fz`, que les autres hauts jets canoniques sont absents et que `R` est affine en `Sg_rr`. Ce nouveau contrôle vérifie également l'absence de `zrr,zrrr`.

Élimination algébrique **sans fixer les jets physiques** :

```text
pLg_r* = (pSg*Sg_r+pg*tg_r-K*z/h)/Lg
A0 = beta0*Sg²+2*beta1*Sg*Sf+beta2*Sf²
At = beta1*Sg²+2*beta2*Sg*Sf+beta3*Sf²
kg = Lg*pLg²/(4*Mg2*Sg²)-pLg*pSg/(2*Mg2*Sg)
dustg = pg*sqrt(1+tg_r²/Lg²)
Sg_rr* = Lg/(2*Mg2*Sg)*[-kg-dustg+Mg2*Lg-Mg2*Sg_r²/Lg
          +2*Mg2*Sg*Sg_r*Lg_r/Lg²-m2*Mg2*(Lg*A0+Lf*At/h)]
```

Les substitutions `pLg_r=pLg_r*` et `Sg_rr=Sg_rr*` annulent respectivement `Fz` et `Hg` **identiquement**. Après suppression des seuls hauts jets dont les coefficients sont déjà prouvés proportionnels à `Fz`, le calcul rationnel exact `sympy.cancel(sympy.together(R.subs(...)))` retourne **zéro** sans imposer `Fz_r=0`, `Hg_r=0`, `Hf=0`, `C=0`, ni un profil Step55. Ainsi, **sur `Fz=Hg=0`**, la transcription vérifie :

```text
B_N = z*C/Lg - (1-z²)/(Lg*Lf)*D_r(Hg).
```

Corollaire **conditionnel au transfert sur les originaux** : sur la coquille holonome `Fz=Fz_r=Hg=Hg_r=C=0`, `B_N=0`. Avec le facteur antérieur de `B_M` et `E_N=E_M=0`, l'opérateur temporel se réduit à `A_N*N+A_M*M=0`, **sans conclure à l'existence ou à l'impossibilité du BVP**. La relation terminale `N(R)=M(R)>0` imposerait alors `A_N(R)+A_M(R)=0` : ce signe **n'est pas certifié physiquement**.

## Falsification, provenance et exécution

Contrôle négatif exact, sur transcription : `Fz=0`, `Hg=2`, `R=244/125 ≠0`. Il empêche de présenter l'annulation comme une identité hors coquille.

Les sources originales Step45 et Step58 ont été **lues via le connecteur GitHub**, blobs `66aa43841dccfe4a5d586a49be9c10af3a67a10e` et `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Le conteneur n'a pas pu résoudre `raw.githubusercontent.com` ni `api.github.com` : **les octets originaux n'ont PAS été exécutés localement**. Le rejeu utilise les mêmes formules dans une transcription indépendante. Le test publié importe les originaux par défaut et vérifie leurs SHA ; `JANUS_TRANSCRIPTION_ONLY=1` ne doit jamais être décrit comme un rejeu original.

**Exécuté :** `JANUS_TRANSCRIPTION_ONLY=1 python -m unittest -v test_hr_b3c3d6_bn_full_ideal` : **6 PASS, 1 SKIP, 0 FAIL** ; `python -m compileall -q` : PASS. Source blob `bc9b371c3d66f6b2491009e631fa4ed4a29a676f` ; test blob `5862735ecc5c7c43e71ee3f6fec558fbab71a6a5` (octets exécutés). Le certificat est une preuve algébrique de la transcription, **pas encore une preuve d'identité sur moteur original exécuté**.

## Suite

1. Rejouer le test en mode original SHA-authentifié et vérifier l'identité universelle sur les vrais moteurs.
2. Sur la vraie solution Step55, certifier les six enclosures `A_N,A_M,B_N,B_M,E_N,E_M` aux quatre rayons exacts `1/4,1/2,7/10,17/20`, puis la condition terminale `A_N+A_M`.
3. BVP de deux lapses strictement positifs aux deux vrais bords, puis Dirac complet, 4D, stabilité et observables.

**Aucune enclosure des six coefficients, aucun BVP positif deux bords, aucun rang Dirac/4D certifié.**
