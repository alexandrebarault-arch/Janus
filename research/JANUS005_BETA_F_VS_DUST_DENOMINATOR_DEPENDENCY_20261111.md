# JANUS-005 — Séparation exacte beta_f / dénominateur f (2026-11-11)

HEAD source: `4008aa9f09af5bdde6051f6c4d6e961ea85de87b`. Audit des sources authentiques `numerics/hr_step46_exact_secondary_ode.py` et `numerics/hr_step55_global_barrier.py`. **Pas de calcul de solution physique, pas de certificat de bord.**

## Identité vérifiée

Dans Step46, `beta= sqrt(1+tfr**2/Lf**2)`, `fac=pLf/(2*mf*Sf*Sfr)`, `denom=beta+fac*tfr`. Sur la carte Step55 `tfr=KF*Lf`, `pLf=s*U`, à s fixé et géométrie f prescrite :

- `beta_f = sqrt(1+KF**2*s)`, donc `partial_U beta_f=0` et `partial_PG beta_f|U=0`.
- `den_f=beta_f+s*U*KF*Lf/(2*mf*Sf*Sfr)` ; `partial_U den_f=s*KF*Lf/(2*mf*Sf*Sfr)` et `partial_PG den_f|U=0`.
- Le long d'une famille PG-only `U(s,lambda)`, `d den_f/dlambda=[s*KF*Lf/(2*mf*Sf*Sfr)]*dU/dlambda`, si les coefficients f prescrits restent constants.

**Contrôle exécuté :** Python/SymPy, différentiation symbolique et deux assertions `simplify(diff(beta,U))==0` et `simplify(diff(den,U)-s*KF*Lf/(2*mf*Sf*Sfr))==0` : **2 PASS**. Ceci précise le rapport précédent : le `beta_f` *nommé* par Step46 est fixe dans cette famille, tandis que le dénominateur de poussière `den_f` varie via U. Ne pas appeler le dénominateur `beta_f`, ni ajouter sa variation deux fois au jacobien déjà différentié en U.

## Contrôle critique et limites

La dérivée totale précédente n'est valable que pour la famille à géométrie f prescrite. Les vraies contraintes et les deux conditions aux bords peuvent exiger une variation de cette géométrie : cette possibilité n'est ni exclue ni établie. L'identité n'établit aucun signe de `dpf/dlambda` ou `dpSf/dlambda`. Les sources Step45/46/55/58 complètes n'ont pas été exécutées ; **0 nouvelle cellule physique évaluée, 0 certifiée**.

**NEXT_ACTION_EXACT :** sur les octets authentiques Step46 et Step55, reconstruire la dérivée de `pf` en U en distinguant `beta_f` et `den_f`, la confronter à `H` dans le jacobien publié, puis vérifier si la famille PG-only satisfait les vraies conditions de bord et Dirac. Pour JANUS-001 : transférer toutes les dépendances et sources historiques authentifiées, vérifier les blobs, lancer la suite ciblée puis le pilote à une cellule.

**GATE_2B = OPEN ; JANUS_R = NOT_VALIDATED.**
