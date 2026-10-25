# JANUS — Étape 68k : famille spatiale exactement contrainte et fixation locale des lapses positifs

**25 octobre 2026 — branche exclusive :** `research/gate2b-nonhomothetic-transfer`. **Gate 2B OPEN ; JANUS-R NOT_VALIDATED.**

## 1. Pourquoi ce calcul est nouveau et ce qu'il ne démontre pas

Les étapes 68h et 68j ont éliminé analytiquement les coefficients `M'` et `N'` du crochet temporel complet sur leurs surfaces de contraintes, sans figer les variations du shift. La difficulté réelle demeure le signe des coefficients `A_N,A_M`, le rapport de lapses et les conditions aux bords.

La présente étape construit un **témoin entièrement EXACT**, portant sur une **famille spatiale homothétique plate**, c'est-à-dire distincte de la véritable famille non homothétique Step55. Elle prouve qu'un rapport de lapses strictement positif et régulier peut apparaître dans le vrai système sphérique original, avec deux poussières positives, pour une famille ouverte de paramètres. Cela n'est **pas** une preuve de l'existence ni du signe de ce rapport sur la branche Step55, ni une solution temporelle 4D.

## 2. Profil canonique paramétrique exact

On fixe `Mg²=Mf²=m²=1` (tous STRICTEMENT positifs), et on conserve les cinq paramètres d'interaction `beta0,...,beta4` entièrement symboliques. Posons :

[
T=eta_1+2eta_2+eta_3,qquad
ho_g=-(eta_0+3eta_1+3eta_2+eta_3),qquad
ho_f=-(eta_1+3eta_2+3eta_3+eta_4).
]

Dans le secteur (oxed{r>0, T>0, ho_g>0, ho_f>0}), les données exactes sont

```text
Lg=Lf=1, Sg=Sf=r,
pLg=pSg=pLf=pSf=0,
theta_g=theta_f=0, theta_g'=theta_f'=0,
p_g=r²*rho_g>0, p_f=r²*rho_f>0,
z=0, z'=z''=z'''=0,
tous les jets radiaux = dérivées analytiques de ce profil.
```

Ces données ont métriques spatiales égales/plates et poussières comobiles **à l'instant initial**. Elles ne sont pas l'ansatz non homothétique à deux courbures de Step55 ; les paramètres utilisés pour construire un témoin ne sont pas ceux du benchmark Step55.

Le Hamiltonien physique ORIGINAL Step45 et son opérateur temporel complet ORIGINAL Step58 donnent exactement, **pour tout (r>0)** :

[
F_z=H_g=H_f=C=0,qquad D_g=D_f=0
]
avec aussi leurs **six premières dérivées radiales** identiquement nulles. Le coefficient de stationnarité original est
[
oxed{K=r^2 T>0quad(r>0)}.
]

Les annulations ont été vérifiées symboliquement en substituant **tous** les jets canoniques jusqu'à l'ordre 4, ainsi que les jets du shift, sans fixer arbitrairement les dérivées absentes.

## 3. Résultat exact : signes stricts et lapses positifs

L'opérateur temporel à six couples sur ce profil donne :

[
egin{aligned}
A_N&=-rac32r^2T(eta_0+eta_1-eta_2-eta_3)
=oxed{rac32r^2T(ho_g+2T)},\\
A_M&=-rac32r^2T(eta_1+eta_2-eta_3-eta_4)
=oxed{-rac32r^2T(ho_f+2T)}.
end{aligned}
]

Ses autres coefficients `B_N,B_M,[Cdot]_{N''},[Cdot]_{M''}` sont exactement nuls sur cette famille. **Ainsi** :
[
oxed{
dot C_{m red}=rac32r^2T
ig[(ho_g+2T)N-(ho_f+2T)Mig].
}
]

Sous les hypothèses de stricte positivité, (A_N>0), (A_M<0), et
[
oxed{rac MN=rac{ho_g+2T}{ho_f+2T}>0.}
]

Ce rapport est CONSTANT en (r) sur cette famille. Comme `A_N` et `A_M` s'annulent tous deux comme `r²`, la formule du rapport a une extension finie et strictement positive vers `r=0` ; mais la charte servant à éliminer le shift est singulière en `K(0)=0`. Cette extension formelle ne remplace donc PAS l'analyse de régularité canonique au centre.

**Témoin rationnel explicite :**
[
(eta_0,eta_1,eta_2,eta_3,eta_4)=(-5,1,0,0,-5)
Longrightarrow
T=1,quadho_g=2,quadho_f=4.
]
[
oxed{dot C=r^2(6N-9M)},qquad
oxed{N=3, M=2>0},qquad
oxed{M/N=2/3}.
]

Cette construction prouve que la région des paramètres permettant des poussières positives et des lapses positifs n'est pas vide. Une perturbation suffisamment petite conserve ses inégalités strictes par continuité. Le rapport n'est pas universel : il dépend des deux densités et de `T`.

**Contrôle négatif :** si le choix de paramètres viole la positivité de la poussière `f`, un coefficient peut s'annuler et la conclusion de rang local non nul ne suit plus ; les tests conservent cette précondition.

## 4. Provenance, tests et journal machine

Le calcul appelle les originales physiques Step45/58, et la fonction d'authentification des **huit** sources Step45/46/55normal/55barrier/57/58/59/60 SHA-identiques au dépôt. Il ne retape ni l'opérateur `Cdot`, ni ses termes de dérivées de lapses.

- `numerics/hr_step68k_exact_positive_lapse_family.py` — Git blob **`5e8783eec4f342cc29b7208ad6cdeb1d7df9cbd2`** (source exécutée, hash GitHub relu et IDENTIQUE).
- `tests/test_hr_step68k_exact_positive_lapse_family.py` — Git blob **`c9c53a6123c84e2310f3fcb52c4b185d18d92410`** (tests exécutés, hash GitHub relu et IDENTIQUE).
- `research/reports/gate2b-step68k-exact-positive-flat-family.json` — Git blob **`7beda486cd587303df8b376c946b7f8a82f94d8a`**, rapport machine et hypothèses.

Vrai test local :
```bash
cd /mnt/data/janus-step68f
OPENBLAS_NUM_THREADS=1 PYTHONPATH=. pytest -q tests/test_hr_step68k_exact_positive_lapse_family.py
# 18 passed in 11.14s
```

Une première suite comportait **17 succès et un échec de comparaison syntaxique de deux expressions SymPy pourtant identiques**, corrigée en vérifiant la différence factorisée. Les **18 tests définitifs ont ensuite tous réussi**. Aucun workflow GitHub Actions n'a été activé.

## 5. Frontière scientifique et priorité Step68l

L'étape 68k certifie un **témoin analytique de rang local un** pour l'équation de préservation de `C` sur la branche **homothétique plate** considérée : la ligne des coefficients ((A_N,A_M)) n'est pas nulle et a un noyau de lapses positifs.

Elle ne prouve ni que cette famille prolonge une solution dynamique 4D intégrée avec bords, ni le rang complet de la matrice de Dirac, ni une garantie d'absence de fantôme BD. **Surtout**, elle ne certifie toujours pas les signes de `A_N,A_M` sur la solution non homothétique Step55. C'est ce dernier calcul qu'il faut aborder en priorité.

**Step68l :** certifier par intervalles les coefficients `A_N,A_M` sur les 256 cellules rationnelles de la vraie branche non homothétique Step55, obtenir un contrôle régulier au centre et la solution admissible des conditions aux bords, puis un oracle Poisson non-IBP six-couples. Ne pas extrapoler le résultat homothétique à toutes les solutions.

**VERDICT :** résultat paramétrique EXACT d'existence locale des lapses positifs dans un secteur particulier, et deux coefficients de dérivées premières désormais annulés exactement sur les contraintes ; **GATE 2B OPEN — JANUS-R NOT_VALIDATED.**
