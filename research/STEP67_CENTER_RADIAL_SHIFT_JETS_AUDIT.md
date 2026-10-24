# JANUS — Étape 67 : dérivées radiales du déplacement relatif

**24 octobre 2026. Branche scientifique exclusive : research/gate2b-nonhomothetic-transfer.**
**GATE 2B OPEN ; JANUS-R NOT VALIDATED.**

## Hypothèses et portée

La véritable équation algébrique du déplacement relatif identifiée dans les travaux antérieurs est :

    Fz = Dg - K*z/sqrt(1-z²) = 0
    s=r², Dg=r³*d(s), K=r²*k(s), z=r*w(s)
    Fhat = d-k*w/sqrt(1-sw²) = 0
    W(s,d,k)=d/sqrt(k²+s*d²), pour k>0

Sur la branche initiale positive particulière du Step55 : 0<=s<=289/400, k(s)>229/1000, et w(s)=w0=1/250. Les prémisses physiques Step45/55 ont été consultées antérieurement et sont **supposées** : aucune réexécution des sources physiques historiques ni de leurs certificats d'intervalles dans ce calcul autonome. Les chartes K=0 et J=0 sont exclues.

## Résultat A — les dérivées jusque l'ordre deux à s variable

En plus des dérivées d,k de Step66, à d,k fixés :

    W_s  = -w³/2
    W_ss = 3w⁵/4
    W_sd = -3w²*(1-sw²)^(3/2)/(2k)
    W_sk = 3w³*(1-sw²)/(2k)

Les bornes par fractions rationnelles exactes sur les coefficients du benchmark sont :

    |W_s| = 1/31250000 < 1/30000000
    |W_ss| = 3/3906250000000 < 1/1000000000000
    |W_sd| < 3/28625 < 1/9000
    |W_sk| < 3/7156250 < 1/2000000

Ces quatre bornes concernent les dérivées partielles **au point du profil Step55** et NON les dérivées totales d(s),k(s) le long de familles arbitraires. Aucune borne globale de d_s,k_s,d_ss,k_ss n'est revendiquée ici.

## Résultat B — règle de chaîne radiale complète

Pour les fonctions normalisées lisses d(s),k(s), les dérivées de w=W(s,d(s),k(s)) sont :

    w_s = W_s + W_d*d_s + W_k*k_s
    w_ss = W_ss + 2*W_sd*d_s + 2*W_sk*k_s
           + W_dd*d_s² + 2*W_dk*d_s*k_s + W_kk*k_s²
           + W_d*d_ss + W_k*k_ss

Et les jets du shift physique z(r)=r*w(r²) :

    z'(r)  = w + 2s*w_s
    z''(r) = 2r*(3*w_s + 2s*w_ss)

La forme est régulière au centre si d,k possèdent la régularité normalisée requise.

## Résultat C — compatibilité exacte avec le profil fixé Step55

Le profil prescrit w(s)=w0 constant et la stationnarité imposent :

    t = 1-s*w0²
    d(s) = k(s)*w0/sqrt(t)
    d_s = w0*k_s/sqrt(t) + k*w0³/(2*t^(3/2))
    d_ss = w0*k_ss/sqrt(t) + w0³*k_s/t^(3/2)
           + 3*k*w0⁵/(4*t^(5/2))

Substitution dans les deux règles de chaîne : **w_s=0, w_ss=0** exactement, y compris au centre. Ainsi :

    z(r)=r/250 ; z'(r)=1/250 ; z''(r)=0.

La nouveauté opérationnelle n'est PAS de dériver une fonction linéaire : c'est la compatibilité algébrique vérifiée entre les deux jets de la racine implicite et les jets des données normalisées d,k. Omettre la dérivée explicite W_s produit le **faux terme +w³/2** ; ce contrôle négatif est testé.

## Preuve exécutable et provenance

- Script : numerics/hr_step67_radial_shift_jets.py — Git blob 9368df2289756feb2e47a86917e5466c2a90ab75.
- Tests : tests/test_hr_step67_radial_shift_jets.py — Git blob 92dcdbc0cebbab2f5fccf98c5a62ff1c7d7da592.
- Rapport machine : research/reports/gate2b-step67-report.json — Git blob 7dfdccf13f549b51e12b90d18ec584c5d2a9aa2c.

Les trois empreintes Git ont été vérifiées égales aux empreintes des fichiers locaux exécutés ou générés, via relecture du connecteur GitHub.

Commande de test réellement exécutée dans le workspace autonome /mnt/data/janus-step67 :

    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m pytest -q tests/test_hr_step67_radial_shift_jets.py
    20 passed in 1.21s

Commande de génération réellement exécutée :

    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python -m numerics.hr_step67_radial_shift_jets > research/reports/gate2b-step67-report.json

Vérifications : dérivées exactes, racine positive à échantillons rationnels, annulations symboliques de profils, contre-exemples négatifs et majorants Fraction exacts. Les tests antérieurs, la suite complète et GitHub Actions ne sont PAS relancés. Cette étape **ne** prouve **ni** la préservation temporelle **ni** l'absence du fantôme de Boulware–Deser.

## Priorité de reprise — Step68

1. Reconstituer un worktree cohérent à partir des vrais fichiers GitHub byte-exact Steps45/46/55/57/58/59/60/63–65 et dépendances, puis rejouer leurs tests ciblés.
2. Substituer au vrai opérateur de préservation temporelle le profil Step55, les jets physiques P',P'',P''', les contraintes prolongées et les jets z,z',z'' compatibles ci-dessus.
3. Calculer les coefficients des lapses A_N,B_N,A_M,B_M ; confronter un oracle original indépendant non intégré par parties, les conditions de bord et le rang Dirac des six couples, puis la fixation des lapses.
4. Traiter séparément K=0 et J=0 et ne passer aux tests 4D/stabilité/observations qu'après cela.

**Conclusion :** étape algébrique Step67 vérifiée sous prémisses Step55 ; le verrou temporel fondamental reste **OUVERT**, et JANUS-R demeure **NON VALIDÉ**.
