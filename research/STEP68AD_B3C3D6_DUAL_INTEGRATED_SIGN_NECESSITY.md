# JANUS b3c3d6 — condition nécessaire intégrée pour le dual faible (29/10/2026)

**Résultat mathématique EXACT, conditionnel, sur la classe d'opérateurs Step58 ; pas de certificat physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Résultat

Pour `T=A_N N+A_M M+B_N N'+B_M M'+E_N N''+E_M M''`, et un multiplicateur `phi>=0`, `C²`, non identiquement nul, satisfaisant `phi=phi'=0` aux deux extrémités, poser `Q_i=phi*A_i-(phi*B_i)'+(phi*E_i)''`.

La **condition nécessaire** pour que `Q_i>=0` sur tout l'intervalle est `integral_a^b phi(r)*A_i(r) dr >= 0` pour chacun de `i=N,M`. En effet, l'intégrale de chacun des deux termes dérivés est un terme de bord nul. Ce résultat est indépendant de l'amplitude et des signes des coefficients `B_i,E_i`. Si `A_M<0` partout où `phi>0`, alors `integral Q_M=integral phi*A_M<0` : le certificat dual **particulier** exigeant `Q_N,Q_M>=0` est impossible, quelle que soit la petitesse ou la grandeur de `B,E`. Cela **n'implique pas** qu'un BVP positif existe : c'est un écran de non-faisabilité de cette méthode de preuve, pas un no-go physique.

## Témoin exact non physique

Sur `[0,1]`, prendre `phi=x²(1-x)²`, `A_M=-2-x²`, `B_M=x³(1-x)`, `E_M=x²(1-x)²/100`. Alors :

`Q_M=x²(x-1)²(200x³-136x²-14x-47)/25` et `integral_0^1 Q_M dx=integral_0^1 phi*A_M dx=-8/105<0`.

Le terme `Q_M` change même de signe sur l'intervalle ; ses dérivées ne peuvent pas corriger le signe de son intégrale. Contrôle négatif : avec `phi=x(1-x)`, `E=1`, la condition `phi'=0` **n'est pas** vérifiée aux bords et le terme de bord vaut `-2`. Les hypothèses de bord sont indispensables.

## Impact sur JANUS et exécution

Les **anciens quatre sondages numériques** de Step58 sur Step55 donnaient `A_M<0` aux rayons `1/4,1/2,7/10,17/20`. Ces quatre valeurs ne prouvent **pas** `A_M<0` sur l'intervalle, ni l'absence d'un support admissible pour `phi`. Il faut d'abord le rejeu original SHA-authentifié avec les jets cubiques, puis une enclosure uniforme des `A_i` et des zéros, avant d'investir dans la recherche d'un multiplicateur dual positif. Si `A_M<0` est certifié partout, abandonner **ce certificat dual composante par composante**, sans en déduire un no-go de JANUS.

Commande exécutée : `cd /mnt/data/janus_dual_sign && PYTHONPATH=. python -m unittest discover -s tests -v` : **5 PASS, 0 FAIL après correction d'une comparaison syntaxique SymPy dans le test** ; `python -m compileall -q numerics tests` PASS. Vérification rationnelle `-8/105`. Les tests sont internes/non indépendants du théorème. Aucun original Step45/46/55/58 exécuté dans cette session : GitHub accessible par connecteur lecture/écriture, DNS GitHub du container indisponible.

Sources examinées via GitHub : Step58 original blob `802c23aebd41780d8c462f1aa1711707fe4ee88f`, ancien probe blob `643d90183367e74a28ed453d93f5489074b75b08`, candidat cubique `9eb5167bec74fc427307a262faaa6a1f785785a8`. Code et tests publiés puis relus, blobs `58237b11545c75ff1b9877052f86869866dd7936` et `fbdcde781c2f8ac22947ff689945a2f558c5f97f`, égaux aux octets testés.

**Étape suivante INCHANGÉE :** exécuter cinq originaux SHA-authentifiés et le candidat cubique aux quatre rayons, comparer les six coefficients affine/cubique et leurs résidus, factoriser/enclore `A/B/E`, centre et lapses positifs aux deux bords ; puis Dirac six couples, charges/jauge, `K=0/J=0`, dynamique 4D, stabilité et observables.
