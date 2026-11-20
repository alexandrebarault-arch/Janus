# JANUS-006 — contre-exemple algébrique à la non-annulation automatique du mineur (2026-11-20)

## Provenance et portée
Source Step45 au HEAD dbfe9ee6dab535b13f546274b4e7e9bdf16f6154, blob Git 66aa43841dccfe4a5d586a49be9c10af3a67a10e ; formule de la dérivée extraite du rapport JANUS006_C_EXACT_MOMENT_DERIVATIVE_20261120.md. Le présent test est **un contrôle algébrique indépendant de la non-annulation**, et NON un rejeu octet-à-octet du module Step45, ni une solution des contraintes.

## Hypothèse falsifiée
La positivité de Lg,Lf,Sg,Sf,m2,beta1,beta2,beta3 et la non-nullité de K=m2*Mg2*Lg*Lf*At ne suffisent pas à assurer que le mineur 4×4 précédent est non nul.

Écrire le facteur de la dérivée comme P=2 Lf Sg (Sf beta3+Sg beta2)+Lg sqrt(1-z²)(Sg² beta1-Sf² beta3). Prendre Lg=Lf=Sg=1, z=0, beta1=beta2=beta3=1, et Sf variable positif. Alors P=2(Sf+1)+(1-Sf²)=-(Sf-3)(Sf+1). Pour Sf=3, P=0, tandis que At=beta1*Sg²+2 beta2*Sg Sf+beta3 Sf²=16>0. Avec m2=Mg2=Mf2=1, K=16 et les préfacteurs du mineur sont tous non nuls ; pourtant le mineur est nul.

## Reproduction
```bash
python - <<'PY'
import sympy as s
x=s.symbols('Sf',positive=True)
P=2*(x+1)+(1-x*x)
assert s.factor(P)==-(x-3)*(x+1)
assert P.subs(x,3)==0
assert (1+2*x+x*x).subs(x,3)==16
print('PASS: positive regular parameters, K nonzero, selected minor zero')
PY
```

Contrôle indépendant : 2(3+1)+(1-9)=8-8=0 et At=(1+3)²=16. Ce contrôle ne requiert aucune approximation numérique.

## Limites
La configuration n'a PAS été montrée compatible avec Hg=Hf=Fz=C_exact=0, les contraintes de Dirac, l'holonomie, les deux vrais bords ni les observables. L'annulation d'un seul mineur ne prouve pas que le jacobien complet perd son rang. La formule de dérivée provient du jalon précédent, dont le rejeu authentifié reste à faire. Ne pas transformer ce contre-exemple algébrique en réfutation physique.

**NEXT_ACTION_EXACT** : rejouer la dérivée sur le module Step45 authentifié, calculer les autres mineurs et tester la compatibilité de P=0 avec Hg=Hf=Fz=C_exact=0 ; poursuivre JANUS-001 avec les dépendances authentiques. GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.
