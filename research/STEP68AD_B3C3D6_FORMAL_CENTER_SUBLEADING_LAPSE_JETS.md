# JANUS — b3c3d6 : compatibilité des jets centraux au second ordre (conditionnelle)

28 octobre 2026. **Théorème formel de Taylor, pas une évaluation de l'opérateur original Step58 et pas une preuve Dirac.** GATE_2B OPEN ; JANUS_R NOT_VALIDATED.

## Hypothèses et identité exacte

Soit l'opérateur temporel **complet** de lapses
`F=A_N N+A_M M+B_N N'+B_M M'+E_N N''+E_M M''`.
Au centre régulier, supposons les développements suivants (coefficients symboliques et non mesurés ici) :
`A_N=a r²+b r⁴+o(r⁴)`, `A_M=c r²+d r⁴+o(r⁴)`,
`B_N,B_M=O(r⁴)`, `E_N=e r⁴+o(r⁴)`, `E_M=f r⁴+o(r⁴)`,
et des lapses pairs C² `N=N0+N2 r²+o(r²)`, `M=M0+M2 r²+o(r²)`.

L'équation `F=0` implique **deux conditions nécessaires distinctes** :

`[r²]F = a N0+c M0=0` ;

`[r⁴]F = (a+2e)N2+(c+2f)M2+b N0+d M0=0`.

Les termes `B_i L_i'` sont `O(r⁵)` pour des lapses pairs C², mais `E_i L_i''` contribuent déjà à l'ordre `r⁴` : les supprimer à partir du seul constat `E_i=O(r⁴)` serait **incorrect**. Sur la coquille authentique `F_z=H_g=0`, le résultat algébrique Step58 antérieur annonce l'annulation **identique** des deux coefficients `E_i`; si cette réduction est effectivement imposée, alors `e=f=0` et l'équation de courbure devient `aN2+cM2+bN0+dM0=0`. La coquille et les coefficients `b,d` n'ont pas été évalués dans ce travail.

## Contre-exemple exact : la valeur centrale ne fixe pas la courbure

Trois opérateurs **jouets**, à `a=2,c=-4,N0=1,M0=1/2`, possèdent des solutions analytiques paires positives `N=1` :
(1) `A_N=2r²,A_M=-4r²,E_M=0`, solution `M=1/2` ;
(2) `A_N=2r²+3r⁴,A_M=-4r²,E_M=0`, solution `M=1/2+3r²/4` ;
(3) `A_N=2r²+3r⁴,A_M=-4r²,E_M=r⁴`, solution `M=1/2+3r²/2`.
Dans les trois cas `B_N=B_M=E_N=0`, l'équation complète est exactement satisfaite, mais `M2` vaut respectivement `0,3/4,3/2`. Le seul rapport central `M0/N0=-a/c` ne permet donc de déduire **aucune** valeur de courbure.

Ces exemples ne sont **pas** des configurations Step55 ni des solutions JANUS.

## Provenance, tests et verrous

Lecture directe via le connecteur GitHub des sources originales de la branche :
- `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f` ;
- `numerics/hr_step68ad_c2d2e5b3b2c2b2d2d2b3c2_center_operator.py` blob `9a77f749a040aaec37e7c3f01368013154fdb562` ;
- `numerics/hr_step55_global_barrier.py` blob `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`.

Exécuté localement : `python -m numerics.hr_step68ad_b3c3d6_center_subleading_jet` (8 contrôles de résidus SymPy nuls, dont plusieurs contrôles élémentaires et non indépendants ; 3 modèles exacts positifs), puis `python -m unittest -v tests.test_hr_step68ad_b3c3d6_center_subleading_jet` (4 tests PASS, non indépendants), zéro échec. SHA des octets testés : programme `340d05c76db1f9ae25fdbc1fc7167e65b4a6867a`, tests `70a3376e9f9a173d75a0f214274a0d8094c0625d`.

`git ls-remote` a échoué : `Could not resolve host: github.com`. **Aucun rejeu** des imports originaux Step45/55/58, du certificat b3c2, ni du probe externe Step58 à R=17/20. L'hypothèse `A_i=a_i r²+b_i r⁴+o(r⁴)` est un prolongement formel des valuations publiées b3c2, **pas** une certification nouvelle des coefficients `b,d,e,f` du modèle physique.

## Prochaine action b3c3d6 (inchangée)

Exécuter le probe original Step58 à R=17/20 et le rejeu b3c2 sur les imports authentiques, calculer les vrais coefficients `A,B,E` et leurs jets centraux, prouver la réduction `E=0` sur les primaires, certifier les cartes `B_M≠0` et les raccords au centre, puis résoudre la compatibilité **globale** des lapses positifs avec les véritables bords Step55 et le quotient de jauge temporelle. Seulement ensuite examiner pullback Dirac, générateurs/charges, six couples, K=0/J=0, dynamique 4D, stabilité et observables.

**b3c3d6 PARTIEL ; GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
