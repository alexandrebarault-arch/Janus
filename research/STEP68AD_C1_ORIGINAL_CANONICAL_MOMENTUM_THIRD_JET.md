# JANUS — Step68ad-C1 : troisième jet canonique central original

26 octobre 2026. Branche exclusivement research/gate2b-nonhomothetic-transfer.
**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**

## Résultat mathématique nouveau et précisément limité

À partir des tubes originaux certifiés sur le continuum 0 <= s=r² <= 1/1024 (Step68v pour U_s, Step68ad-B2 pour U_ss et U_sss, Step68ac pour U0), la règle de chaîne appliquée au véritable moment radial f, pLf(r)=r² U(r²), fournit EXACTEMENT :

    pLf'/r  = 2(U+s U_s)
    pLf''   = 2U+10s U_s+4s² U_ss
    pLf'''/r= 24 U_s+36s U_ss+8s² U_sss
    (d³/dr³ U(r²))/r = 12 U_ss+8s U_sss

Toutes ces identités ont été vérifiées symboliquement avec SymPy pour une fonction U arbitraire, et non seulement pour un polynôme de Taylor.

**NOUVELLES BORNES RATIONNELLES SUR TOUT 0 <= r <= 1/32, incluant les quotients prolongés régulièrement en r=0 :**

| Quantité | Min approximatif | Max approximatif | Signe |
|---|---:|---:|---|
| pLf'/r | -0.010504853794 | -0.010501768851 | NÉGATIF |
| pLf'' | -0.010504853794 | -0.010495598966 | NÉGATIF |
| pLf'''/r | **0.018945615724** | **0.018953886023** | **POSITIF** |
| (d³/dr³ U(r²))/r | -0.000242642608 | -0.000240911976 | NÉGATIF |

Les fractions exactes sont publiées dans le JSON machine, pas ces décimales arrondies. pLf''(0)=2U0<0, pLf'''(0)=0 mais pLf'''/r a une limite strictement positive. Ainsi pLf'' est strictement croissante sur r>0 tout en restant négative sur le domaine.

## Preuve d'inclusion sans division par zéro

Soit S=1/1024 et U0∈[u0-,u0+], U_s∈[a,b] avec a>0, U_ss∈[c,d] avec d<0, U_sss∈[e,f] avec f<0. Ces quatre intervalles sont ceux des rapports originaux SHA-pinnés, sur le même domaine fermé. Intégrer U_s donne U∈[u0-,u0++S*b]. Par substitution dans les IDENTITÉS (et non en dérivant des inégalités) :

    pLf'/r ∈ [2u0-, 2(u0+ + 2Sb)] < 0
    pLf'''/r ∈ [24a+36Sc+8S²e, 24b] > 0
    (d³/dr³ U(r²))/r ∈ [12c+8Se, 12d] < 0
    pLf'' ∈ [2u0-, 2u0+ + 12Sb] < 0

La borne inférieure plus serrée de pLf'' utilise le fait D_r(pLf'')=pLf'''>0 pour r>0. Le facteur r est extrait ANALYTIQUEMENT avant tout encadrement. Aucune division d'un intervalle contenant zéro.

## Sources authentifiées et exécution honnête

Trois rapports originaux lus via le connecteur GitHub et leurs SHA blob vérifiés :

- Step68v : d83a3b80862a2e990a4c4879ec8745a4e91c8b34
- Step68ac : 16ae8dab3563c17134e4e20f886fb7306dc2e4ba
- Step68ad-B2 : ac961b5b83667a83497497d22a701c24584cb561

Les sources originales de l'opérateur temporel Steps57/58/60/68o ont été lues et leur SHA identifié, respectivement bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f, 802c23aebd41780d8c462f1aa1711707fe4ee88f, 9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509, c99caebc17f243784450ddff94fb061767e6d8e7. **Ces sources temporelles n'ont PAS été exécutées localement** : le container n'a pas le checkout et son réseau externe est indisponible ; le connecteur GitHub fonctionne en lecture/écriture.

**15 tests réellement exécutés : 15 PASS, 0 FAIL, en 0,61 s** avec Fraction exact et SymPy sur les champs rationnels lus des rapports originaux, ainsi que des tests de refus de signes/provenance erronés. Ces tests ne sont PAS une réexécution des 16 tests B2 ni du Step58. La fonction de production read_pinned refuse les octets non conformes aux SHA originaux ; le test local a vérifié son rejet de fichiers altérés, pas la lecture complète des trois rapports dans un clone.

Fichiers GitHub publiés et relus avec les SHA des fichiers locaux effectivement exécutés :

- numerics/hr_step68ad_c1_center_momentum_jet.py — blob 08f6d13b2f799705328f10f12d80433617f16ef8
- tests/test_hr_step68ad_c1_center_momentum_jet.py — blob a367c80566a6bec9119201a23136f597619ee3a7
- research/reports/gate2b-step68ad-C1-original-canonical-pLf-third-jet.json — blob 62f98abd0fe18004b2a6654e1d422d02cfe025aa

Reproduction dans un checkout complet :

    PYTHONPATH=. python -m numerics.hr_step68ad_c1_center_momentum_jet research/reports
    PYTHONPATH=. pytest -q tests/test_hr_step68ad_c1_center_momentum_jet.py

## NEXT EXACT : Step68ad-C2

**C1 certifie UN seul des douze jets canoniques et AUCUN signe temporel.** Les sept cellules temporelles PENDING dans [1/64,1/32] restent non résolues.

1. Reconstituer localement et SHA-authentifier les sources physiques originales Steps45/46/55/57/58/59/60/68n/68o et les rapports 68v/68ac/B2/C1.
2. Remplacer la récurrence _ode_coeff(si) de Step68o, qui divise par s et explose en intervalles près du centre, par le jet exact en r fondé sur B2 : U(r)=Jet([U,2r Us,Us+2s Uss,2r Uss+(4/3)r³ Usss]). Vérifier que le troisième jet de pLf reproduit exactement la formule C1, puis comparer à l'ancienne méthode là où elle reste stable.
3. Reconstruire TOUS les douze jets et la réponse du shift non gelé ; évaluer le véritable opérateur Step58/60 et factoriser avant de normaliser A_N/r² et A_M/r² sur les sept cellules, l'anneau intérieur, puis le centre.
4. Si les intervalles sont indécis, identifier la première expression ou le premier dénominateur responsable et documenter le blocage ; ne pas transformer un échantillon en preuve.
5. Maintenir ouverts rang Dirac, lapses/bords/jauge, K=0/J=0, oracle NON-IBP, stabilité BD et cosmologie 4D.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
