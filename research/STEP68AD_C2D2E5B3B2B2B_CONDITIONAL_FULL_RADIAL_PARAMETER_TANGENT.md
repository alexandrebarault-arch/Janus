# JANUS — 68ad-C2d2e5b3b2b2b : tangente radiale non triviale par variation de P_g (27 octobre 2026)

**Portée : théorème d'existence CONDITIONNEL sur la famille de données spatiales contraintes ; pas un rang de Dirac, pas une famille certifiée aux bords externes. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Sources originales et hypothèses
Les sources authentifiées sont Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step49 `d570948912885d45a625fa2db31c6a5435b6a654`, Step55 normalization `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55 barrier `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step68o `c99caebc17f243784450ddff94fb061767e6d8e7`. Sources relues via connecteur GitHub, moteurs Python historiques **non réexécutés**.

Conserver la géométrie Step55, le shift prescrit `z=r z1`, les coefficients des poussières g `kg,kf`, et remplacer le paramètre d'impulsion g `Pg` par `Pg+lambda` dans **toutes** les formules Step55 de reconstruction g (`Gmom,Gprime,Rhog,Psg`). Les relations algébriques originales imposent `Hg=Fz=Ddiag=0` et gardent `Dg=r³ Dbar` indépendant de `Pg`. Pour chaque `lambda`, reconstruire `pf,pSf` via Step46 et résoudre la vraie EDO réduite `2s U_s=G(s,U;Pg+lambda)-2U`. Cela impose `Hf=C=0` tant que les branches et dénominateurs originaux restent réguliers.

**Hypothèse de continuation** : le graphe exact Step55 à `lambda=0` est compact et contenu dans une charte ouverte de positivité/non-dégénérescence où `G` et les reconstructions sont analytiques en `(s,U,Pg)`. Les certificats historiques Step55/54 apportent les marges sur la solution de base ; leur moteur n'est pas rejoué ici et aucune marge explicite en `lambda` n'est fournie. L'existence d'un voisinage `|lambda|<lambda0` résulte de la dépendance analytique locale au centre et de la continuation/dépendance continue sur l'intervalle compact, sous cette hypothèse. Ce n'est **pas** une nouvelle certification numérique uniforme.

## Théorème tangent exact
Step49 donne, pour la famille de sources paramétrée :
`G(0,U;Pg)=3U0(Pg)-U`, `U0(Pg)=Mf2*b*(Pg/(Mg2*a)-2*z1)`.
En conséquence, `c=dU0/dPg=Mf2*b/(Mg2*a)>0` (valeur rationnelle du benchmark :
`274023815147385251710689588080861/40000000000000000000000000000000000`).

Sur le profil exact `U_*(s)`, la dérivée `v(s)=dU(s;Pg+lambda)/dlambda|0` satisfait sur **tout** `0<s<=289/400` :
`2s v_s=(G_U-2)v+G_Pg`, `v(0)=c>0`.
Écrire `G=3U0(Pg)-U+sR(s,U,Pg)`, `h=v-c`. Alors
`2s h_s=-3h+s[R_U(s,U_*,Pg)(c+h)+R_Pg(s,U_*,Pg)]`.
La formule de Volterra est
`h(s)=s^(-3/2)/2 * integral_0^s t^(3/2) [R_U(t)(c+h(t))+R_Pg(t)] dt`.
Elle sélectionne l'unique solution bornée (mode homogène singulier `s^(-3/2)` exclu). L'existence/continuation régulière suit de l'hypothèse ci-dessus ; `v(0)=c>0` prouve que la direction tangentielle est non nulle. `delta pLf=r² v(r²)` respecte la parité centrale, et les autres variations sont les dérivées des reconstructions originales. **Cette direction est tangentielle aux contraintes spatiales reconstruites sur l'intervalle**, conditionnellement aux identités originales et à la continuation, contrairement au contre-exemple hors secondaire de l'étape précédente.

Cette variation de `Pg` modifie les données initiales du benchmark et peut modifier les traces à `r=17/20`. Aucune condition de bord fixée, raccord 4D, lapse global ou contrainte temporelle de Dirac n'est imposée. Elle ne prouve donc pas l'existence d'une perturbation physique admissible au problème aux limites final.

## Tests réellement exécutés
Le programme BigInt publie **36 assertions exactes PASS**, le wrapper **10 assertions PASS**, et une vérification SymPy indépendante en session a effectué **21 contrôles exacts** (9 coefficients d'EDO, 9 coefficients linéarisés, 3 identités centre/reconstruction). **0 FAIL final**. Les vérifications de séries de `G` utilisent un modèle analytique synthétique respectant la forme Step49, **pas** le véritable `G` Step55 ; le témoin rationnel `Dg=9/10` contrôle l'identité de reconstruction g, non une solution physique. Les 21 contrôles SymPy sont scratch et non publiés comme script.

## Verrous restants
Rejouer le vrai moteur `G(s,U,Pg)` et certifier une marge `lambda0` et des bords admissibles ; construire ensuite les crochets fonctionnels originaux non-IBP à six couples, la matrice Dirac/rang/tertiaires, les chartes `K=0/J=0`, lapses et conditions aux limites, puis dynamique 4D/stabilité/observables. **GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**
