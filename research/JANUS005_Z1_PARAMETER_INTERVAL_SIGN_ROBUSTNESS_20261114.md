# JANUS-005 — Robustesse algébrique en Z1 (14 novembre 2026)

**Statut : certificat rationnel conditionnel de signe, non certificat physique.** HEAD de base `4e2b4c9812b6b322082b1e8741956e07654e395b`. Source de calcul `research/repro/janus005_continuous_m2_z1_sign_20261114.py`, blob `794400b08c4e88b8a4fbbc83dd2194bb73680844`.

## Question falsifiable
Le signe négatif du déterminant `J=d(Wfbar,Dbar)/d(M2,Z1)` à `Z1=0.004` reste-t-il certifié uniformément pour un intervalle de valeurs de Z1, sans réduire ce paramètre à des points échantillonnés ?

## Protocole effectivement exécuté
Python 3, `fractions.Fraction` et `math.isqrt`. La source originale est conservée inchangée. Commande exacte du second essai :

```bash
python - <<'PY'
s=open('/mnt/data/janus_sign/check.py').read().replace("z=F('.004')","z=I(F('-.01'),F('.01'))")
exec(compile(s,'z_symmetric','exec'))
PY
```

Le remplacement a été appliqué à une copie en mémoire de la source identique au blob publié, et uniquement à l'affectation de `z`. La source utilise une arithmétique rationnelle d'intervalles et des racines carrées encadrées avec `isqrt`. Les 256 cellules radiales couvrent exactement `s=[0,289/400]`; chaque cellule porte simultanément `Z1=[-1/100,1/100]`, sans échantillonnage de Z1. `M2=23.3348939346`, `MG=1` et les autres coefficients Step55 restent prescrits.

Sortie :
```text
T positive all: True Q negative all: True det negative all: True
T global enclosure 0.1060297323982009 0.10822935875319159
Q global enclosure -0.005011816265811553 -0.004453979521719048
det global enclosure -0.0011721318189093274 -0.00102081006034898
```

Les bornes affichées sont décimales indicatives, pas des bornes exactes à réutiliser. L'intervalle de signe strict est certifié par les fractions internes. Un premier contrôle indépendant de domaine `Z1=[0,0.01]` a aussi renvoyé les trois booléens True, avec `det` environ `[-0.0011721289620722703,-0.0010212727426552833]`. Le cas symétrique, plus large, subsume le premier. **Résultat :** pour chaque `s∈[0,0.7225]` et chaque `Z1∈[-0.01,0.01]`, `T>0`, `Q<0` et `J<0` dans la carte algébrique prescrite.

## Limites et contrôle contradictoire restant
Le calcul repose sur la formule de J et les coefficients Step55 déjà audités, pas sur un calcul indépendant de l'opérateur physique. Il ne certifie ni la liberté de Z1 dans les solutions, ni les contraintes de Dirac, ni les deux vrais bords, ni la dynamique 4D. Les 256 cellules sont **algébriques** : cellules physiques b3c3d9 évaluées/certifiées pendant ce jalon = **0/0**. Pour une contre-vérification indépendante supplémentaire, implémenter une seconde arithmétique d'intervalles ou une réduction analytique de Q avec bornes exactes et confronter les extrêmes.

**NEXT_ACTION_EXACT :** vérifier dans Step45/49/55 si la variation de Z1 est physiquement admissible avec M2, PG et les vrais bords ; reconstruire les dépendances authentiques JANUS-001 puis lancer les neuf tests et le pilote une cellule. **GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**
