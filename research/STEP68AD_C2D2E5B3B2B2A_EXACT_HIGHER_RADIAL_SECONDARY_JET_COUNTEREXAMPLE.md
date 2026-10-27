# JANUS — 68ad-C2d2e5b3b2b2a : contre-exemple radial exact à la suffisance des jets centraux

27 octobre 2026. **Résultat conditionnel, local, hors coquille secondaire. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources physiques authentifiées
Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step49 `d570948912885d45a625fa2db31c6a5435b6a654`, Step55 `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Sources relues sur GitHub ; **moteurs physiques originaux non réexécutés**.

## Théorème local
Sur la solution analytique centrale Step55/68o, écrire `s=r²`, `pLf=r²U(s)`, `W=pLf'/r=2U+2sU_s`. La secondaire Step46, après résolution algébrique de la primaire f, est affine en W :
`C/r²=A(s,U)[W-G(s,U)]`, où `A(0)=-m2*mg*At/(2*b*mf) !=0`. Step49 prouve `G(0,U)=3U0-U`, donc `G_U(0)=-1`.

Perturber seulement `pLf` par `epsilon*r^6`, soit `delta U=epsilon*s²`, en reconstruisant `pf` et `pSf` avec les formules originales Step46. La géométrie, le secteur g, le shift et les poussières g sont inchangés. Alors `delta W=6epsilon*s²`, `delta G=-epsilon*s²+O(epsilon*s³)`, d'où **`delta C=7A(0)epsilon*r^6+O(epsilon*r^8)+O(epsilon²*r^10)`**. Pour epsilon suffisamment petit et non nul, C n'est pas identiquement nul. Les conditions `Hg=Hf=Fz=Dg+Df=0` restent vraies par construction sur la charte régulière, sous les hypothèses de la reconstruction originale ; la condition centrale `C2=0` est inchangée.

Sur les paramètres rationnels physiques Step55, `At>0`, `A(0)<0` et `7A(0)` est exactement la fraction du certificat JSON (environ **−3225.510376708569**). La non-annulation ne repose pas sur un arrondi.

**Portée :** contre-exemple à l'extrapolation des contraintes centrales tronquées vers `C(r)=0` sur tout r. Ce n'est ni une direction tangentielle aux contraintes fonctionnelles complètes, ni une obstruction de Dirac, ni une réfutation de JANUS. Il ne prouve pas que la famille `Pg` de l'étape précédente échoue ; il prouve seulement que des jets centraux finis ne suffisent pas.

## Tests et suites
V8 : 12 assertions rationnelles du noyau + 9 assertions adversariales du wrapper, zéro échec. Contrôle indépendant Python/SymPy de session : 15 tests unittest réussis et 9 assertions symboliques internes ; code Python scratch non publié. Le script V8 publié est exécuté en mémoire avec les mêmes octets ; pas de test Node dans un clone. Prochaine étape **68ad-C2d2e5b3b2b2b** : construire une famille **tangentielle à C(r)=0 sur tout r** via la variation de l'EDO Step55 et vérifier les bords ; puis oracle original Poisson/Dirac six couples, rang/tertiaires, K=0/J=0, lapses, 4D/stabilité/observables.
