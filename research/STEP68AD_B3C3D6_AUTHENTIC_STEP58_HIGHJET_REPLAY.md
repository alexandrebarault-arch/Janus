# b3c3d6 — REJEU ORIGINAL Step45 + Step58 : certificat des plus hauts jets (29 octobre 2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED ; b3c3d6 PARTIELLE.**

## Résultat réellement exécuté

Pour la première fois dans cette reprise, les **octets intégraux originaux** de `numerics/hr_step45_exact_physical_ward.py` (Git blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`) et `numerics/hr_step58_temporal_operator.py` (Git blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`) ont été reconstruits localement, contrôlés par SHA-1 Git des octets, importés et **exécutés réellement avec SymPy**. Un shim minimal remplace **uniquement** l'import de `authenticated_step45` de Step57 ; le module original Step57 complet n'a PAS été exécuté. Aucun moteur original Step55 n'a été exécuté.

La commande `PYTHONPATH=. python -m numerics.hr_step58_temporal_operator` a produit le manifeste original et exécuté `physical_operator()` puis `highest_lapse_certificate()`. Les deux secteurs `N,M` ont les ordres 0,1,2. Sur `Fz=0`, le coefficient de `M''` est exactement nul ; celui de `N''` vaut `(z²-1)*Hg/(Lg*Lf)`, donc il s'annule aussi sur `Hg=0`. **C'est un rejeu du résultat original Step58, pas une découverte de rang Dirac ni une validation des coefficients de premier ordre.**

La transcription rationnelle des seules constantes géométriques Step55 à `R=17/20` donne `-(1-z²)/(Lg*Lf) = -9999884400000000000000000000000000000000/926432894764182404865494596893754186181`, strictement entre -11 et -10. Il s'agit du **facteur** qui multiplie `Hg` dans le coefficient de `N''` sur `Fz=0`, et non de la valeur de `E_N` hors coquille. Le signe ne démontre rien sur les `B_N,B_M` ni sur la positivité des lapses.

## Tests réellement exécutés

`PYTHONPATH=. python -m numerics.hr_b3c3d6_authentic_step58_highjet_replay` : succès, deux SHA authentifiés, identité SymPy et garde rationnelle exactes. `PYTHONPATH=. python -m unittest discover -s tests -v` : **4 cas PASS, 0 FAIL**, non indépendants. Le manifeste original Step58 a été exécuté une fois et les quatre tests réutilisent le cache de la même session Python. Le contrôle Git local réseau échoue toujours par DNS, mais la récupération via connecteur GitHub et la reconstruction SHA ont contourné ce blocage **pour Step45+Step58 uniquement**.

## Limites non négociables

**Le vrai probe original Step58 sur le profil radial exact Step55 à R=17/20 reste NON exécuté** : les six coefficients `A_N,A_M,B_N,B_M,E_N,E_M` et leurs dérivées/zéros/cartes, le raccord centre, les lapses strictement positifs et les conditions aux deux vrais bords restent à certifier. Le profil Step55 complet exige notamment les jets de `pLf` déterminés par l'ODE radiale et les conditions primaires/secondaires ; les seules constantes géométriques ne les remplacent pas. Ne pas transformer le certificat `E_N,E_M` sur coquille en preuve de rang Dirac, de jauge temporelle ou d'existence globale.

Fichiers : `numerics/hr_b3c3d6_authentic_step58_highjet_replay.py`, `tests/test_hr_b3c3d6_authentic_step58_highjet_replay.py`, `research/reports/gate2b-b3c3d6-authentic-step58-highjet-replay.json`, cette note. Priorité inchangée : **probe Step58 original COMPLET sur Step55**, puis Dirac/charges/jauge temporelle/six couples/K=0/J=0/4D/stabilité/observables.
