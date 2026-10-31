# JANUS b3c3d6 — correction du débordement binary64 et certificat au rayon exact (31 octobre 2026)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED ; b3c3d6 PARTIELLE.** Audit d'une subtilité du certificat Step55 du 30 octobre : le temps final de l'intégrateur DOP853 est **strictement extérieur** au domaine de la barrière physique Step55.

## Problème vérifié en fractions exactes

Le rayon extérieur physique est `r*=17/20`, donc `s*=289/400`. L'intégrateur antérieur termine à `s_b=6507701461550367/9007199254740992`. La différence positive est exactement `s_b-s*=7/225179981368524800`, environ `3.1086244689504386e-17`. Le certificat original `G_U<0` et la barrière Step55 à 256 cellules ne couvrent **que** `[0,s*]`. Par conséquent, appliquer directement l'inégalité d'erreur **physique** jusqu'à `s_b` sans prolongement rigoureux du tube n'est pas justifié. L'ancienne interprétation de `epsilon` comme borne physique à `s_b` doit être suspendue. Le calcul rationnel du **registre numérique positif** `B=s_b epsilon` (erreur initiale, défauts et sauts) demeure réutilisable.

## Réparation exacte par troncature du registre

Pour chaque morceau dense `P_i`, sur le tube commun certifié, `H_i=2s P_i'-G(s,P_i)+2P_i`, `G_U<=0`, et `e=U-P_i` donnent `d(s|e|)/ds <= |H_i|/2`. Aux interfaces, `s|e|` augmente au plus de `s|J_i|`. Toutes les contributions du registre sont **non négatives**. Leur somme sur le préfixe `[s0,s*]` est donc au plus la somme déjà certifiée sur les polynômes `[s0,s_b]`, soit `B=s_b epsilon`, sans jamais invoquer la solution exacte au-delà de `s*`. Il en résulte la nouvelle borne **au vrai rayon extérieur** :

`|U(s*)-P(s*)| <= (s_b/s*) epsilon < 1/200000`.

`P(s*)` désigne **le polynôme dense correspondant au temps exact s***, pas `P(s_b)`. Le certificat Bernstein corrélé du rejeu physique précédent sur tous les domaines des 28 polynômes inclut le préfixe, donc `P(s*)` reste dans le tube Step55. Cette réparation suppose l'authenticité et l'exactitude des certificats de résidu, de sauts et d'erreur initiale du 30 octobre ; ces moteurs ne sont **pas** réexécutés ici.

Au même `s*`, la borne commune `G_U` du certificat physique précédent donne, par le théorème des accroissements finis et les jets **cohérents avec l'EDO** :

- `|U_s(s*)-F(s*,P(s*))| <= max|G_U-2| epsilon*/(2s*) < 11/1000000` ;
- `|pLf(s*)-s*P(s*)| <= s* epsilon* < 1/200000` ;
- `|pLf'(s*)/(17/20)-G(s*,P(s*))| <= max|G_U| epsilon* < 51/10000000`.

Ici `epsilon*=(s_b/s*)epsilon` est une fraction exacte dans le module. Les valeurs décimales sont environ `4.84954700350249e-6`, `1.0071953468232843e-5`, `3.503797710030549e-6`, `4.854878754591478e-6`. **Ce ne sont toujours pas les six enclosures A/B/E Step58, ni une borne sur P_s.** Les trois autres rayons historiques ne sont pas traités ici. La valeur centrale P(s*) doit être extraite de la partition DOP853 archivée ou reconstruite par rejeu pour produire une enclosure absolue.

## Vérification et limites

Sources physiques originales du certificat antérieur : Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 normalisation `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, barrière `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`. Rapport rationnel déjà publié `research/reports/gate2b-b3c3d6-Step55-physical-correlated-DOP853-7168-cell.json` (blob `e2e210e4ebe5a3b34a2c533e2c1cd705f7deb2dc`). Nouvelle exécution : **7 unittest rationnels PASS, 0 FAIL ; compileall PASS ; module exécuté**. Aucun nouveau rejeu physique original ni Step58.

Prochaine étape : vérifier/rejouer la partition physique DOP853 et évaluer `P(289/400)`, certifier `G_{sU}`, `G_{UU}`, `F` sur le même tube, encloser `U_{ss}`, transférer aux quatre rayons et aux six coefficients Step58, puis BVP lapses positifs aux deux bords et Dirac/4D/stabilité/observables. **Ne pas restaurer la revendication d'une erreur physique à s_b sans extension indépendante du tube.**
