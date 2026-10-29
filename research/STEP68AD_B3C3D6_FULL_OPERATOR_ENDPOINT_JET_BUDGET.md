# JANUS b3c3d6 — borne exacte conditionnelle sur les jets de lapses au bord (29/10/2026)

**Statut : lemme algébrique exact, NON preuve physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Source authentique et portée

L'opérateur Step58 original `numerics/hr_step58_temporal_operator.py` a été **lu via GitHub** au blob `802c23aebd41780d8c462f1aa1711707fe4ee88f` ; la version du probe cubique `numerics/hr_b3c3d6_corrected_step58_point_probe_candidate.py` a été lue au blob `9eb5167bec74fc427307a262faaa6a1f785785a8`. **Aucun de ces moteurs originaux n'a été exécuté dans cette session.** La formule ci-dessous concerne la forme complète à six coefficients, sans supposer l'annulation des termes de dérivées secondes.

Au bord `R>0`, si `N(R)=M(R)=u>0`, l'opérateur local est
`T=(A_N+A_M)u+B_N N'+B_M M'+E_N N''+E_M M''`.
Posons `d=|A_N+A_M|u`, `b=|B_N|+|B_M|`, `e=|E_N|+|E_M|`.
Pour `|T|<=tau`, `tau>=0`, et les budgets `P=max(|N'|,|M'|)`, `Q=max(|N''|,|M''|)`, l'inégalité triangulaire donne **nécessairement**
`d<=tau+bP+eQ`.
Si un seul budget commun `H>=P,Q` est supposé, `H>=max(0,d-tau)/(b+e)` lorsque `b+e>0`. Si `b=e=0` et `d>tau`, l'équation est impossible. L'inégalité est **optimale au sens algébrique** pour des jets indépendants, mais une solution globale, les parités et les contraintes peuvent réduire l'espace admissible.

**Application au témoin jouet antérieur :** à `R=17/20`, `epsilon=10^-8`, `A_N=R²,A_M=-2R²,B_N=-epsilon R⁴,B_M=E_N=E_M=0`, le lapse positif `N=2-exp((1/R-1/r)/epsilon)` a `N'(R)=-1/(epsilon R²)=-40000000000/289`. La borne est atteinte exactement. Donc les petites valeurs des coefficients ne suffisent pas sans budget de pente.

**Échelle indicative, NON certifiée :** le rapport de probe original publié précédemment indiquait à `R=17/20` `A_N≈2437.0939964`, `A_M≈-4676.6472342` et chacun des quatre `B_N,B_M,E_N,E_M` de module `<2e-44` au calcul numérique. Si — hypothèse non prouvée — ces valeurs étaient de véritables bornes avec `tau=0,u=1`, il faudrait `H>2.79e46`. **Ce nombre n'est PAS une borne physique :** coefficients et résidus proviennent de calculs ponctuels, l'ODE est intégrée en double précision et les jets cubiques corrigés n'ont pas été rejoués. Le budget `H` est dépendant de la coordonnée radiale ; aucune borne a priori de régularité physique n'est fournie.

## Tests et reproductibilité

`PYTHONPATH=/mnt/data/janus_endpoint_guard python -m unittest discover -s /mnt/data/janus_endpoint_guard/tests -v` : **5 tests PASS, 0 FAIL**, sur le code exact publié (arithmétique `fractions.Fraction`), `python -m compileall -q` PASS. Contrôles : saturation jouet, dérivées première/seconde, cas B=E=0, tolérance de résidu et entrées invalides, inégalité avec contrôle négatif. Tests non indépendants de la dérivation ; aucune preuve Dirac.

## Prochaine étape

1. Reconstituer localement les cinq sources originales SHA-authentifiées Step45/46/55/58 et rejouer **le candidat cubique** à `r=1/4,1/2,7/10,17/20`, comparer six coefficients affine/cubique, vérifier les résidus.
2. Produire factorisations exactes ou enclosures **rigoureuses** des six coefficients et une borne admissible sur les jets des lapses au bord ; ne pas convertir `~10^-44` en zéro exact.
3. Traiter le centre, le BVP positif à deux vrais bords, le pullback Dirac six couples, charges/jauge temporelle, `K=0/J=0`, dynamique 4D, stabilité et observables.

Aucun changement sur `main`, `research/v2-flrw` ou les workflows.
