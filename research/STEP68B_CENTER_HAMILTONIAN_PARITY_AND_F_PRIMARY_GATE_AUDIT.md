# JANUS — Étape 68b : condition de parité centrale sous les DEUX flots hamiltoniens

**24 octobre 2026 — branche exclusivement autorisée :** `research/gate2b-nonhomothetic-transfer`.

**GATE 2B OPEN, JANUS-R NOT VALIDATED.** Résultat physique limité à l'ordre DOMINANT près de `r=0`. Il ne s'agit ni d'un calcul du rang de Dirac ni d'une preuve que la secondaire est conservée en temps.

## 1. Objet : lever une hypothèse non contrôlée de l'étape 68a

L'étape 68a a établi le pullback régulier du shift

```text
delta z = r*(A*e_d+B*e_k)
Dg=r³d(s), K=r²k(s), s=r²,
e_d=delta Dg/r³, e_k=delta K/r²,
A=t^(3/2)/k, B=-w*t/k, t=1-sw².
```

Mais il restait à déterminer si les **vraies variations hamiltoniennes** de `Dg,K`, et non des variations d'essai arbitraires, conservent ces puissances près du centre. Cette étape traite ce point au **premier ordre non trivial** en reprenant indépendamment les quatre densités locales **post-IBP** `Ag,Bg,Af,Bf` telles qu'elles sont écrites dans l'original GitHub `numerics/hr_step45_exact_physical_ward.py` (Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`).

**Provenance explicite :** le nouveau programme TRANSCRIT les formules du Step45 et redérive indépendamment leurs gradients d'Euler avec les 12 coordonnées canoniques présentes. Il ne charge **pas** et ne réexécute **pas** l'original binaire GitHub Step45 dans ce nouvel environnement. Les identités qu'il certifie sont donc des identités de la reconstruction, dont la correspondance physique doit être revérifiée par import original à l'étape suivante.

## 2. Hypothèses centrales de la vraie famille Step55

Avec `a=L_g(0)`, `b=L_f(0)`, les champs analytiques respectent

```text
Lg=a+a2*r²+O(r⁴),   Sg=r*Lg,
Lf=b+bf2*r²+O(r⁴), Sf=r*Lf,
pLg=G*r²+O(r⁴),    pSg=2G*r+O(r³),
pLf=U*r²+O(r⁴),    pSf=2U*r+O(r³),
pg,pf=O(r²),       theta'_g,theta'_f=O(r),
z=w*r, z'=w, w=1/250.
N=N0+N2*r²+O(r⁴), M=M0+M2*r²+O(r⁴).
```

Les quatre variables `N0,N2,M0,M2` sont **indépendantes**. Les puissances de parité sont celles de la charte radiale analytique, **et non** des hypothèses de régularité pour toutes les variations canoniques hors de cette charte.

La relation centrale `pSg/r=2G` résulte de `Dg=pSg*Sg'-Lg*pLg'+pg*theta'_g=O(r³)` et `Sg'(0)=Lg(0)=a`. Son maintien est à vérifier, pas à supposer.

**Autre condition essentielle :** la primaire radiale f de l'original Step46 contient

```text
pSf=(-Dg+Lf*pLf'-pf*theta'_f)/Sf'.
```

Elle impose `lim_(r→0) pSf/r=2U`. Ne pas oublier cette contrainte : l'argument complet échoue si on laisse le coefficient central `V=lim pSf/r` arbitraire.

La source distingue maintenant explicitement le coefficient de profil métrique `bf2` du paramètre d'interaction Hassan–Rosen `beta2` (identificateur Python `b2`). Une première ambiguïté de nom a été découverte puis corrigée ; source, tests et rapport définitifs ont été régénérés.

## 3. Théorème algébrique exact — conservation de la parité CENTRALE par chaque lapse

Les variations sont calculées à l'aide des gradients d'Euler d'une densité `N Ag+N' Bg+M Af+M' Bf` et des équations hamiltoniennes avec les paires `(Lg,pLg),(Sg,pSg),(tg,pg),(Lf,pLf),(Sf,pSf),(tf,pf)`. Aucune valeur ou rapport entre `N,M` n'est imposé.

Pour **chacun** des deux termes de lapse, individuellement et sans somme qui cacherait une annulation artificielle, le calcul SymPy exact donne, après la contrainte primaire centrale f,

```text
lim delta(Sg)/r = lim delta(Lg),
lim delta(pSg)/r = 2 lim delta(pLg)/r²,
lim delta(Sf)/r = lim delta(Lf),
lim delta(pSf)/r = 2 lim delta(pLf)/r².
```

En posant `Delta a=lim delta Lg`, `Delta G=lim delta pLg/r²`, `Delta P=lim delta pSg/r`, la variation de la densité originale `Dg=pSg*Sg'-Lg*pLg'+pg*theta'_g` possède au premier ordre :

```text
lim delta Dg/r = a*(Delta P-2*Delta G)
                +2G*(lim delta Sg/r-Delta a) = 0.
```

L'identité est vérifiée **séparément dans le secteur N et dans le secteur M**. Avec les parités analytiques de la famille elle implique `delta Dg=O(r³)` au centre. De même `K=m² Mg² Lg Lf*(beta1 Sg²+2 beta2 Sg Sf+beta3 Sf²)` et la parité des variations métriques impliquent `delta K=O(r²)`.

C'est donc une **validation de la condition d'entrée centrale** de la formule Step68a pour les champs hamiltoniens de cette reconstruction, à l'ordre dominant. Elle **ne** calcule PAS encore les coefficients finis complets `e_d(r),e_k(r)`, ni leurs dérivées en s, ni la préservation temporelle de la secondaire.

Les termes des dérivées secondes des lapses restent actifs :

```text
∂(delta pLg/r²)/∂N2 = -4 Mg²,
∂(delta pSg/r)/∂N2 = -8 Mg²,
∂(delta pLf/r²)/∂M2 = -4 Mf²,
∂(delta pSf/r)/∂M2 = -8 Mf².
```

Le calcul **ne** fixe donc aucun rapport `M/N` ; il constate seulement la compatibilité kinematique centrale des flux sous les contraintes indiquées.

## 4. Contrôle négatif non trivial : la primaire f est indispensable

Si, avant de la réimposer, on écrit `pSf=V*r+O(r³)`, les dérivées exactes donnent pour la contribution de lapse M

```text
lim (delta Lf - delta Sf/r) =
    M0*(2U-V)/(2 b Mf²),

lim (delta pSf/r - 2 delta pLf/r²) =
    M0*U*(2U-V)/(2 b² Mf²).
```

Ce résidu est **généralement non nul** si `V != 2U`. Le programme et les tests conservent explicitement cette obstruction hors de la primaire : l'annulation centrale ne doit jamais être présentée comme automatique hors des contraintes.

Ce contrôle négatif est aussi une protection contre la confusion entre deux effets différents : compatibilité locale de centre sous l'équation primaire d'une part, absence du fantôme BD ou existence de lapses temporels positifs d'autre part.

## 5. Exécution réellement effectuée et empreintes authentifiées

Nouveau calcul indépendant :

- `numerics/hr_step68b_center_hamiltonian_parity.py`, Git blob **`e8c7e932994f340933521ac6f48b46f8a53d1bf6`** ;
- `tests/test_hr_step68b_center_hamiltonian_parity.py`, Git blob **`c35fef4551fc68c860147e51cccf5b8069bc4fb1`** ;
- `research/reports/gate2b-step68b-center-parity-report.json`, manifest GitHub archivé.

Les SHA des **deux nouveaux fichiers finaux** sont relus sur GitHub et identiques octet pour octet aux scripts effectivement exécutés localement. Résultat ciblé **23 PASSED en 7.22s** ; exécution commune Step68a+68b **44 PASSED en 12.85s**. Cette dernière est une suite algébrique ciblée, **pas** le test de tout le dépôt.

```bash
PYTHONPATH=/mnt/data/janus-step68a OPENBLAS_NUM_THREADS=1 \
 python -m pytest -q \
 /mnt/data/janus-step68a/tests/test_hr_step68a_normalized_shift_variations.py \
 /mnt/data/janus-step68a/tests/test_hr_step68b_center_hamiltonian_parity.py
# 44 passed in 12.85s
```

SHA256 du manifeste brut local régénéré après correction : `c556154cc6b72266df7143c94f5cce2ba5cb5e2ac4a370ef5df79be37f46c19b`. Les fichiers historiques Step45/46/55/57–60 **ne sont pas relancés ENSEMBLE** dans ce workspace. Actions/CI restent désactivés conformément à la demande.

## 6. Prochain verrou exact — Step68c

1. Reconstituer l'action Step45 octet-authentique dans un environnement unique avec Step46/55/57/58/59/60/63–65, et comparer directement le résultat hamiltonien du présent programme aux gradients d'Euler ORIGINAUX pour les huit composantes, tous les jets de lapses et les termes de poussière nécessaires. Ne jamais confondre transcription mathématique et import physique authentifié.
2. Sur le vrai profil Step55, calculer les coefficients NON TRIVIAUX suivants : `e_d=delta Dg/r³` et `e_k=delta K/r²`, y compris leurs dérivées radiales ; vérifier leurs bornes avec l'EDO `U(s)` et les jets centraux `U0..U3`.
3. Injecter la variation Step68a du déplacement `delta z,delta z'`, **sans la figer**, dans les quatre coefficients résiduels `A_N,B_N,A_M,B_M` du vrai Step58/60, après réduction complète de `Fz,Hg,Hf,Ddiag,C,C'`, et vérifier les conditions aux bords.
4. Exécuter l'oracle temporel Poisson original NON IBP à SIX couples, déterminer rang, fixation des lapses et chartes `K=0,J=0`. Aucun de ces calculs ultérieurs n'est déclaré accompli.

**BILAN :** deux flots hamiltoniens compatibles au centre avec la charte normalisée sous les deux primaires ; obstruction off-primaire f explicitement conservée. Le rang de Dirac temporel reste **OUVERT**. **GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
