# b3c3d6 — Élimination universelle des hauts jets du résidu B_N (31 octobre 2026)

**Statut : théorème algébrique formel partiel ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Énoncé exact

Sur la carte du shift stationnaire `K=m2*Mg2*Lg*Lf*At>0`, `Lg,Lf,Sg,Mg2>0`, `|z|<1`, noter `h=sqrt(1-z²)`, `Fz=D-K*z/h` et
`R=B_N-z*C/Lg+(1-z²)/(Lg*Lf)*D_r(Hg)`.
Ici `B_N` est le coefficient du premier jet du lapse N dans l'opérateur temporel **complet** Step58, et `C,Hg,Fz` sont les expressions Step45. Les dérivées de jets suivantes sont des identités **hors coquille**, sans hypothèse Step55 ni fixation des autres variables :

```text
dR/d(Sg_rrr) = -2*Mg2*Sg*z*h^3/(Lf*Lg^2*K) * Fz
dR/d(pLg_rr) = z^2*h^3/(Lf*Lg*K) * Fz
dR/d(Lg_rr)  = 2*Mg2*Sg*Sg_r*z*h^3/(Lf*Lg^3*K) * Fz
dR/d(tg_rr)  = -pg*z*h^3/(Lf*Lg^2*K)
               *[z*(Lg^2+tg_r^2)+Lg*tg_r*sqrt(1+tg_r^2/Lg^2)]
               /(Lg^2+tg_r^2) * Fz
```

Le seul autre jet d'ordre >=2 présent dans R est `Sg_rr`, et `d²R/d(Sg_rr)²=0`. De plus `dHg/d(Sg_rr)=2*Mg2*Sg/Lg != 0`. Ainsi, **sur Fz=Hg=0, R se réduit exactement à une expression algébrique de jets d'ordre 0–1**, sans dépendance cachée aux jets radiaux 2–4. Sur `Fz=Fz_r=Hg=Hg_r=0`, cette expression est égale à `B_N-z*C/Lg`.

**Limite essentielle :** l'annulation du résidu inférieur restant n'est NI prouvée NI réfutée. Les identités ne prouvent pas `B_N=z*C/Lg` universellement, ne constituent pas une enclosure physique Step55 et n'impliquent aucun BVP positif ou rang Dirac. Le test de non-annulation hors `Fz=0` évite de confondre une identité de coquille et une identité hors coquille.

## Provenance, reproductibilité, contrôle négatif

Sources originales **lues sur GitHub** : `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` ; `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Le conteneur local n'a pas de DNS GitHub : les calculs SymPy ont été **réellement exécutés sur une transcription indépendante des deux moteurs**, recoupée avec les formules publiées, mais **PAS sur les octets originaux**. Le module publié accepte les dictionnaires d'expressions et les tests publiés importent les originaux par défaut avec contrôle SHA Git. Le mode `JANUS_TRANSCRIPTION_ONLY=1` est explicitement identifié comme transcription et saute le contrôle SHA original.

Commande locale réellement exécutée : `JANUS_TRANSCRIPTION_ONLY=1 python -m unittest -v test_hr_b3c3d6_bn_high_jet_elimination` : **4 PASS, 1 SKIP, 0 FAIL** ; `python -m compileall -q` sur code/test : **PASS**. Quatre facteurs contrôlés par `sympy.cancel(diff(R,jet)-facteur*Fz)==0`, support de jets, affinité et pente de Hg contrôlés exactement. Un contrôle hors coquille confirme qu'un coefficient ne s'annule pas identiquement sans Fz=0. Aucun test physique Step55/58 original n'a été exécuté dans cette session.

## Fichiers et suite

- `numerics/hr_b3c3d6_bn_high_jet_elimination.py` — blob `086b6bae543c0ee497ca9154c5a055921f018423`.
- `tests/test_hr_b3c3d6_bn_high_jet_elimination.py` — blob `bb78fc93db3ad66fd8dd25c3a627220297974adb`.
- `research/reports/gate2b-b3c3d6-BN-high-jet-elimination.json` — blob `dc507b43c5fc69368bbdcc0325d3f89427d37efd`.

**Prochaine action prioritaire :** exécuter le test en mode original SHA-authentifié ; calculer ou réfuter le **résidu de premiers jets** après élimination exacte de `pLg_r` par `Fz=0` et de `Sg_rr` par `Hg=0`, sans substitution de profils gelés ; puis seulement les six enclosures physiques Step58 aux rayons `1/4,1/2,7/10,17/20`, BVP des deux lapses positifs aux deux vrais bords, Dirac/4D/stabilité/observables. Ne pas extrapoler la tranche non physique à Step55.
