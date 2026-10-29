# JANUS b3c3d6 — écran exact d'analyticité centrale pour le contre-exemple des petits B (29/10/2026)

**Portée : modèle JOUET uniquement, pas Step55/Step58. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Question et résultat

La session précédente a construit pour tout ε>0 un lapse positif C∞ satisfaisant les deux bords malgré B_N=-εr⁴ arbitrairement petit. La présente vérification montre exactement ce que cette construction perd si l'on exige **l'analyticité du lapse au centre**, hypothèse plus forte que la régularité C∞ ou la parité.

Avec M=1, A_N=r², A_M=-2r², B_N=-εr⁴ et B_M=0, l'équation est

r²(N-2)-εr⁴ N'=0, soit εr² N'=N-2 pour r>0.

Toutes ses solutions sur (0,R] sont N(r)=2+C exp(-1/(εr)). Imposer N(R)=1 donne C=-exp(1/(εR)), donc N(r)=2-exp((1/R-1/r)/ε). Pour 0<r<=R, **1<=N(r)<2** (avec N(R)=1) et N(0)=2 par prolongement C∞. Les dérivées de N-2 de tout ordre tendent vers zéro au centre, bien que N ne soit pas identiquement 2. L'extension paire par |r| est aussi C∞ : la seule parité régulière n'élimine donc pas le mode plat.

**Théorème exact restreint :** si N est analytique réelle en r au centre, écrivons N(r)=Σ a_k r^k. L'identité εr²N'=N-2 donne a_0=2, a_1=0, et a_k=ε(k-1)a_(k-1)=0 pour tout k>=2. Donc N=2 près du centre, puis partout sur (0,R] par unicité de l'EDO ; la condition N(R)=1 est impossible dans cette classe analytique. Le contre-exemple C∞ de la session précédente n'est donc **pas** un contre-exemple à une hypothèse d'analyticité centrale.

La pente terminale reste N'(R)=-1/(εR²), divergente quand ε→0+. Une borne uniforme |N'(R)|<=K rend la construction impossible dès que ε<1/(KR²). Cela ne fournit aucune borne de pente physique pour Step58.

## Contrôles et provenance

- Calcul symbolique SymPy de l'équation pour tout C, de la condition terminale, de cinq dérivées plates au centre, de 13 coefficients de la récurrence analytique et de la pente terminale.
- **5 unittest locaux PASS, 0 FAIL**, non indépendants ; `PYTHONPATH=. python -m unittest discover -s tests -v` et `python -m compileall -q numerics tests` PASS, répertoire `/mnt/data/janus_analytic_center`.
- Code testé : `numerics/hr_b3c3d6_analytic_center_small_B_guard.py` blob Git `9b16a93e258c7600d215f4c7eef23c69fbd76e74`.
- Tests testés : `tests/test_hr_b3c3d6_analytic_center_small_B_guard.py` blob Git `5b63928c33ea5cbaa4a7e5e9891fe77b65c17fc2`.
- Sources originales Step45/46/55/58 lues par connecteur dans cette session (blobs originaux attendus 66aa4384…, bac025c2…, a54a6acf…, a6e70041…, 802c23ae…) mais **NON exécutées**. Rejeu du candidat cubique à quatre rayons **NON effectué**.

## Limite essentielle et action suivante

Ni l'analyticité des lapses Step55/58 ni la réduction exacte B_N=B_M=0 ne sont prouvées. L'EDO temporelle peut être singulière au centre et la régularité géométrique ne suffit pas à imposer l'analyticité des multiplicateurs. Ce résultat ne tranche donc pas le BVP physique.

Priorité inchangée : exécuter les cinq moteurs SHA-authentifiés et le candidat cubique Step58 à r=1/4,1/2,7/10,17/20, comparer affine/cubique les six coefficients, puis factorisation/enclosures et vraie régularité centrale des lapses avec deux bords, enfin Dirac/4D/stabilité/observables. Ne toucher ni main, ni research/v2-flrw, ni workflows.
