# JANUS — 68ad-C2a : douze jets canoniques, formules régulières au centre

Date : 2026-10-26. Branche de recherche exclusive : `research/gate2b-nonhomothetic-transfer`.

**Statut : LEMME CINÉMATIQUE EXACT, NON CERTIFICAT TEMPOREL. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## 1. Nouveauté exacte

Lecture de la source originale `hr_step68o_temporal_interval_annulus.py`, Git blob `c99caebc17f243784450ddff94fb061767e6d8e7`, et des opérateurs temporels `hr_step58_temporal_operator.py` blob `802c23aebd41780d8c462f1aa1711707fe4ee88f` et `hr_step60_full_constraint_prolongation.py` blob `9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509`. L'original 68o évalue encore les jets de U par la récurrence `(G-2U)/(2s)` ; cette division de **larges intervalles** par s est mal conditionnée près du centre, même lorsque la solution est régulière. Le présent résultat supprime la division pour **l'assemblage cinématique** des douze jets, mais pas encore dans la construction des dix profils physiques.

Soit s=r², et F=F(s) de classe C³. Les trois parités exactes de la vraie paramétrisation radiale originale sont :

| Champs canoniques | Forme |
|---|---|
| Lg, Lf | F(s) |
| Sg, Sf, pSg, pSf | r F(s) |
| pLg, pLf, pg, pf | r² F(s) |
| tg, tf | dérivées prescrites t'_g=r KG Lg(s), t'_f=r KF Lf(s) |

Les identités de jets, **sans aucun quotient par r ni s**, sont :

Pour X=F(s) :

    X'=2r F_s
    X''=2F_s+4s F_ss
    X'''=r(12F_ss+8s F_sss)

Pour X=rF(s) :

    X'=F+2s F_s
    X''=r(6F_s+4s F_ss)
    X'''=6F_s+24s F_ss+8s² F_sss

Pour X=r²F(s) :

    X'=2r(F+s F_s)
    X''=2F+10s F_s+4s² F_ss
    X'''=r(24F_s+36s F_ss+8s² F_sss)

Pour les deux horloges poussière t'=r k L(s) :

    t''=k(L+2s L_s)
    t'''=r k(6L_s+4s L_ss)

La valeur locale t(r0)=0 choisie par le code est **un choix de jauge ponctuel** : elle ne signifie pas que t(r)=0 comme fonction sur un intervalle. Le Hamiltonien original dépend de t', pas de t. En particulier les troisième dérivées des champs pairs sont nulles au centre, tandis que celles des champs impairs rF valent 6F_s(0), potentiellement non nulles. Ceci est essentiel pour éviter d'imposer arbitrairement q'''=0.

Le cas X=pLf=r²U(r²) retrouve exactement l'identité de 68ad-C1 : pLf'''/r=24U_s+36sU_ss+8s²U_sss.

## 2. Code, contrôles et portée

Le code `numerics/hr_step68ad_c2a_all_canonical_parity.py` fournit les trois formules génériques et assemble dans l'ordre **les douze vrais champs** q,q',q'',q'''. Il rejette toute absence de profil, profil supplémentaire ou dérivée manquante. Il contient aussi une vérification fail-closed des trois empreintes Git originales à exécuter lorsque les fichiers originaux sont disponibles localement.

Les tests `tests/test_hr_step68ad_c2a_all_canonical_parity.py` utilisent **SymPy** comme oracle de dérivation indépendant pour les trois parités, des polynômes à coefficients rationnels exacts, le cas r=0, les deux horloges et les entrées invalides.

**Commande réellement exécutée** dans `/mnt/data/janus68adC2a` :

    PYTHONPATH=. python -m pytest -q tests/test_hr_step68ad_c2a_all_canonical_parity.py
    15 passed in 0.74s

Ces **15 tests portent sur les identités algébriques**. Les sources originales Step58/60/68o ont été lues sur GitHub, mais **leur moteur physique n'a PAS été exécuté localement** ; le test positif de leurs octets SHA n'a pas été exécuté, seul le rejet d'une source altérée l'a été. L'accès GitHub via connecteur fonctionne, tandis que `git ls-remote` depuis le container a échoué par DNS (`Could not resolve host: github.com`). Ne pas confondre vérification des empreintes retournées par GitHub avec authentification locale octet à octet.

Fichiers publiés, relecture des blobs contre les fichiers effectivement testés :

- `numerics/hr_step68ad_c2a_all_canonical_parity.py` — `bf673187d6b923193c846749b15c3e291ef3ac9f`
- `tests/test_hr_step68ad_c2a_all_canonical_parity.py` — `e465fcb265a76998d6db662836b500e3b8ba9d10`
- `research/reports/gate2b-step68ad-C2a-canonical-parity.json` — `1f0ecef8fa1a8dbf9d8f38c2a9a5609dc0bdf5f7`

## 3. Prochaine étape précise — 68ad-C2b

La condition scientifique non triviale reste de calculer des **tubes certifiés de F,F_s,F_ss,F_sss pour les dix profils**. Pour pLf=U, les tubes Step68v/68ad-B2 existent ; pour les autres, il faut propager les jets par le `Jet` original de Step68n appliqué en variable **s**, et utiliser les expressions physiques originales `jet_geometry`, `jet_G`, `rhof`, `psf`. Ne pas déduire des dérivées d'un simple intervalle F.

Ensuite seulement assembler les 12 jets avec ce module, substituer dans le véritable Step58/60 **non-frozen-shift** et calculer des encadrements rigoureux des coefficients A_N/r² et A_M/r² sur les **sept cellules encore PENDING entre 1/64 et 1/32**, puis plus près du centre. Si les intervalles restent trop larges, rapporter honnêtement une absence de certification et affiner la représentation/corrélation plutôt que d'inventer des signes.

Le rang de Dirac complet, les lapses, les bords, la jauge, les cas J=0/K=0, l'oracle indépendant non-IBP, la stabilité BD et la dynamique cosmologique 4D restent **OUVERTS**.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
