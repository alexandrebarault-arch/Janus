# b3c3d6 — Courbure centrale du ratio des lapses : lemme conditionnel (28 octobre 2026)

**Portée : algèbre formelle locale, pas un calcul numérique de Step58 et pas une preuve Dirac.**

Considérons l'opérateur complet `A_N N+A_M M+B_N N'+B_M M'+E_N N''+E_M M''=0` avec les expansions `A_N=a r²+b r⁴+o(r⁴)`, `A_M=c r²+d r⁴+o(r⁴)`, `B_i=O(r⁴)`, `E_N=e r⁴+o(r⁴)`, `E_M=f r⁴+o(r⁴)`, et `N=N0+N2 r²+o(r²)`, `M=M0+M2 r²+o(r²)`, lapses pairs C², `N0>0`, `c != 0`. Poser `rho=M/N=rho0+rho2 r²+o(r²)`. L'ordre r² impose `rho0=-a/c`.

**Nouveau corollaire sur la coquille primaire exacte `E_N=E_M=0` sur tout le voisinage :**
`rho2=-(b+d*rho0)/c`, donc **`rho''(0)=-2(b+d*rho0)/c`**, indépendamment du coefficient libre `N2`. Cela ne détermine la courbure physique que lorsque les coefficients authentiques `b,d,c` de Step58 ont été calculés et certifiés sur la vraie coquille Step55.

**Sans réduction exacte des dérivées secondes :** si `c+2f != 0`,
`rho2=-[(b+d*rho0)+2(e+f*rho0)N2/N0]/(c+2f)`.
En particulier `E_i=O(r⁴)` ne suffit pas pour utiliser la formule de la coquille. Si `c+2f=0`, aucune division n'est licite ; l'équation r⁴ peut contraindre `N2` ou devenir identiquement nulle. Les termes `B_i N_i'` sont `O(r⁵)` par parité.

**Témoins exacts JOUETS positifs sur `[0,17/20]` :** `A_N=2r²+r⁴`, `A_M=-4r²`, `B_i=0`. Avec `E_i=0`, `N=1+u r²`, `M=N(1/2+r²/4)`, `u=0,1`, résidu identiquement nul, `rho''(0)=1/2` malgré `N2` distincts. Avec `E_N=r⁴`, `E_M=0`, `M=[(2+r²)N+r² N'']/4`, résidu identiquement nul, `rho''(0)=1/2+u`. Toutes les fonctions ont des coefficients polynomiaux non négatifs et une constante strictement positive. Ces exemples ne sont pas la géométrie Step55.

**Rejeu réel :** `python center_ratio_curvature.py` : 11 assertions symboliques exactes + 2 familles positives vérifiées ; `python -m unittest -v test_center_ratio_curvature.py` : 4 tests PASS, non indépendants ; 0 FAIL. Sources originales lues via connecteur : `numerics/hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f` ; `numerics/hr_step68o_temporal_interval_annulus.py` blob `c99caebc17f243784450ddff94fb061767e6d8e7`. Clone Git local DNS bloqué ; probe Step58 R=17/20 et moteurs Step45/55/58+b3c2 non rejoués.

**Action scientifique prioritaire inchangée :** calculer les coefficients originaux `B_N,B_M,b,d`, vérifier `E=0` sur la coquille authentique, raccorder centre et anneaux, puis tester les vrais lapses positifs et conditions Step55 avant toute inférence Dirac/physique. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
