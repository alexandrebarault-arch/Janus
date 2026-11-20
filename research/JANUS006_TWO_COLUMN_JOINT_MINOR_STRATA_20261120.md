# JANUS-006 — Mineurs conjoints de la tranche (pLg_r,z), 2026-11-20

Source canonique authentifiée : `numerics/hr_step45_exact_physical_ward.py` blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e` au HEAD `cc9b619a4e3f1ea314458734a8f4b9870b7c585d`. Dans le code : `Hg=Ag-d_r Bg`, `Hf=Af_full-d_r Bf`, `Bg=-2 Mg2 Sg Sgr/Lg+z pLg`, `Bf=-2 Mf2 Sf Sfr/Lf+z Lg pLg/Lf`. D'où les dérivées exactes à jets ambiants fixés `∂plgr Hg=-z`, `∂plgr Hf=-z Lg/Lf`. Les identités Ward vérifiées par la source donnent `∂z Hg=Fz/Lg`, `∂z Hf=Fz/Lf`, et `∂plgr Fz=-Lg`, `∂z Fz=-K/(1-z²)^(3/2)` où `K=m2 Mg2 Lg Lf At`.

Sur la coquille Fz=0, le sous-jacobien exact de (Hg,Hf,Fz) par rapport à (plgr,z) vaut :

```
[ -z       0                        ]
[ -z Lg/Lf 0                        ]
[ -Lg      -K/(1-z²)^(3/2)          ]
```

Le mineur (Hg,Fz) est `z*K/(1-z²)^(3/2)`; le mineur (Hf,Fz) est `z*Lg*K/(Lf*(1-z²)^(3/2))`; celui (Hg,Hf) est zéro. Sous Lg,Lf non nuls, |z|<1 :
- K≠0 ET z≠0 : rang de ce sous-jacobien = 2.
- K=0 OU z=0 : rang = 1 (la ligne Fz garde le coefficient -Lg non nul).

**Contre-audit essentiel :** même sur la branche régulière K≠0, la sous-matrice perd un rang à z=0, malgré ∂zFz≠0. C'est une propriété du choix des deux colonnes (plgr,z), pas une perte de rang de Dirac. Les colonnes d'autres champs, en particulier celles de C_exact et les jets holonomes, peuvent restaurer le rang. Le résultat n'établit aucune solution de Hg=Hf=C_exact=0, ni conditions aux deux vrais bords.

**Calcul exécuté** : Python/SymPy, création de `J=Matrix([[-z,F/Lg],[-z*Lg/Lf,F/Lf],[-Lg,-K/(1-z*z)**Rational(3,2)]])`, substitution `F=0`, déterminants des trois sous-matrices 2x2. Contrôle indépendant : développement manuel du mineur `(-z)*(-K/(1-z²)^(3/2))`. PASS pour la matrice sous les hypothèses ci-dessus ; aucune exécution du moteur physique. Tests b3c3d9 SKIP ; cellules physiques demandées/tentées/évaluées/certifiées/inconclusives = 0/0/0/0/0.

**NEXT_ACTION_EXACT** : calculer les colonnes restantes et la ligne C_exact du jacobien canonique complet au même SHA, puis imposer l'holonomie et les deux vraies traces de bord ; distinguer K=0, z=0 et Kz≠0. Pour JANUS-001, reconstruire octet pour octet les imports Step45/46/55/58 et lancer neuf tests puis pilote. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
