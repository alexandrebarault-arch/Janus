# JANUS — Étape 68x : enveloppe centrale rigoureuse à erreur décroissante de U et U_s

**25 octobre 2026 ; branche exclusive `research/gate2b-nonhomothetic-transfer`. GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

## Nouvel encadrement dérivé des données originales, exact et prêt pour l'opérateur temporel

L'étape 68v, fondée sur la VRAIE EDO Step45/46/55 et les coefficients analytiques centraux Step49/67b, a certifié sur `0≤s≤1/64`, `s=r²` :

[
|U(s)-U_*(s)|lekappa s^3,qquad kappa=10^{-7},qquad
U_*(s)=U_0+U_1s+U_2s^2 .
]

À partir du **rapport machine original Step68v octet identique** `research/reports/gate2b-step68v-global-monotone-radial-U.json`, Git blob `d83a3b80862a2e990a4c4879ec8745a4e91c8b34`, nous récupérons une borne R0 du résidu central

[
F_0(s)=G(s,U_*)-2U_*-2sU_*',quad |F_0(s)|le R_0s^3
]

et une borne L de (|G_U(s,u)|) couvrant toute l'enveloppe physique centrale. Les coefficients d'ordres 0 à 2 de (F_0) sont EXACTEMENT nuls par la récurrence analytique originale (hypothèse Step49/67b). Le rapport certifie le troisième jet du résidu, ce qui permet la borne ci-dessus par Taylor.

La vraie EDO est
[
2sU_s=G(s,U)-2U.
]
En soustrayant la même équation évaluée sur (U_*(s)) et en utilisant le théorème des accroissements finis en (u), on obtient, pour (s>0),
[
2s(U_s-U_*')=F_0(s)+G(s,U)-G(s,U_*)-2(U-U_*).
]
Par les deux encadrements exacts et la continuité analytique au centre :

[
oxed{orall sin[0,1/64]:quad
|U_s(s)-U_*'(s)|le Cs^2},
]

[
oxed{
C=rac{R_0+(L+2)kappa}{2}
=rac{551901551914723209073991119}{1600000000000000000000000000000000}
approx3.4493846995	imes10^{-7}.
}
]

Il s'agit d'un **corollaire analytique exact** des deux enclosures originales de Step68v, sans dérivation numérique supplémentaire ni division incontrôlée par (s=0).

### Valeurs certifiées utiles pour le prochain calcul temporel

Au raccord (r=1/32), donc (s=1/1024) :

[
oxed{|U-U_*|lerac1{10737418240000000}
approx 9.3132257462	imes10^{-17},}
]

[
oxed{|U_s-U_*'|le
rac{551901551914723209073991119}
{1677721600000000000000000000000000000000}
approx 3.2895895953	imes10^{-13}.}
]

La largeur maximale de (U) est **10 737 418 240 fois plus petite** que le tube constant (10^{-6}) employé par le calcul temporel extérieur Steps68n–s au même rayon. Au bord (r=1/8), l'amélioration est encore **2 621 440 fois**.

Ces gains répondent à la source principale d'inflation de la méthode radiale proche du centre. Ils ne donnent cependant PAS encore des bornes sur les jets canoniques d'ordres supérieurs, ni sur (A_N/r^2,A_M/r^2) eux-mêmes.

## Reproductibilité

Le nouveau programme Python pur-Fraction `numerics/hr_step68x_normalized_center_ode_envelope.py` authentifie **octet pour octet** le rapport original Step68v et vérifie son domaine, sa largeur (kappa), les deux intervalles signés, ses statuts scientifiques, puis calcule exactement (C), les enveloppes à (r=1/32), (r=1/8) et la limite (s=0). Il refuse une source dont le blob Git change.

- Code source localement exécuté, Git blob `720a893ed8e0321fdf2b84aaff881b904c08e9fd`.
- Tests ciblés localement exécutés, Git blob `a98fefbf13e391a3ea11dfcbb9b27997e6eb38f8` : `tests/test_hr_step68x_center_corollary.py` (5 PASSED en 0.03s).
- Rapport machine exact : `research/reports/gate2b-step68x-center-normalized-envelope.json` Git blob `22a9c0014c717e8422b575f0ebd731069af29850`.
- Deux suites publiées 68w + 68x : **12 PASSED en 0.04s** sous `timeout --signal=TERM --kill-after=2s 8s`.

Commandes avec deadline :
```bash
cd /mnt/data/janus-step68w
PYTHONPATH=. timeout --signal=TERM --kill-after=2s 8s \
  python -m numerics.hr_step68x_normalized_center_ode_envelope research/reports
PYTHONPATH=. timeout --signal=TERM --kill-after=2s 8s \
  python -m pytest -q tests/test_hr_step68w_archived_lapse_ratio_audit.py tests/test_hr_step68x_center_corollary.py
```

**Précaution indispensable :** cette étape renormalise SEULEMENT la vraie solution radiale (U) et sa dérivée (U_s), par corollaire des certificats Step68v ; elle n'a pas réexécuté localement le vrai Step58 dans la session présente (espace Python réinitialisé). Ne pas confondre les 12 tests du corollaire arithmétique avec un certificat temporel près du centre.

## Prochaine vraie étape 68y

Substituer dans le moteur Step68o/Step58, sur `0<r≤1/8`, la borne (kappa s^3) à la place de l'ancienne erreur uniforme (10^{-6}). Propager **avec dépendances analytiques et cancellations exactes** les dérivées spatiales nécessaires jusqu'à l'ordre 3, puis normaliser les coefficients (A_N/r^2,A_M/r^2) pour éviter la perte d'intervalles près de (r=0).

Tester d'abord une bande `[1/64,1/32]`, dont le précédent scan brut incomplet Step68u a gardé sa file de sept cellules non résolues, puis une bande `[1/128,1/64]`. Exiger un certificat complet et sans trous avant de revendiquer des signes, et traiter (r=0) par séries centrales. Tous les jobs sous timeout avec checkpoint atomique, comme `scripts/janus_bounded_job.py`.

Enfin seulement traiter jauge, bords, rang de Dirac, oracle Poisson indépendant non-IBP à six couples, chartes exceptionnelles et 4D. **JANUS_R NOT_VALIDATED ; GATE_2B OPEN**.
