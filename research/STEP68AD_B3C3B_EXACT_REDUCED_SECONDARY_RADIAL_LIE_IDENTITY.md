# JANUS — b3c3b : identité de Lie radiale exacte de la secondaire réduite

28 octobre 2026 — **GATE_2B OPEN ; JANUS_R NOT_VALIDATED**.

## Résultat nouveau : l'hypothèse de covariance de b3c3a est levée, dans le cadre local spécifié

Sur la transcription source-fidèle des densités originales Step45, les coefficients du crochet fonctionnel à six couples vérifient exactement :

- `K00 = {E_g^0,E_f^0}` : densité radiale de poids **1** ;
- `K01 = {E_g^0,E_f^1}` : scalaire radial de poids **0** ;
- `C_exact = K00 - ∂r K01` : densité radiale de poids **1**.

Les neuf identités d'annulation des coefficients de `V'`, `V''` et `V'''` ont été vérifiées directement sur `K00`, `K01` et `C_exact`, en tenant compte de tous les jets canoniques jusqu'à l'ordre deux et de `z,z',z''`. Les douze dérivées de `C_exact` par rapport aux seconds jets canoniques s'annulent exactement. De plus, `∂C_exact/∂z' = -(K sqrt(1-z²)+Dg z)/(Lg Lf)`, conformément à Step57.

Sur la branche stationnaire **K>0**, `z_*=Dg/sqrt(Dg²+K²)` est scalaire parce que `Dg` et `K` ont tous deux le poids 2. Le vrai `z_*' = ∂r z_*` est de poids 1, y compris ses contributions des seconds jets canoniques. Trois identités exactes d'homogénéité et de prolongation ont été vérifiées.

Par composition (règle de chaîne exacte, sans jeter les dérivées de `z_*`), la secondaire complète réduite `C_red(q,q',q'')=C_exact(q,q',z_*,∂r z_*)` est de poids 1. Par conséquent, **identité locale exacte** :

```
delta_V C_red = V * (C_red)' + V' * C_red = (V*C_red)'.
```

Elle est valable pour les jets lisses dans la carte positive-K avec métriques régulières. Sur la coquille fonctionnelle `C_red(r)=0`, la contribution cinématique radiale est nulle **dans le volume**. Ce résultat ne nécessite pas d'imposer les équations temporelles Step58 pour l'identité de Lie elle-même.

## Provenance et vérifications

Les sources Step45 (blob `66aa43841dccfe4a5d586a49be9c10af3a67a10e`), Step58 (`802c23aebd41780d8c462f1aa1711707fe4ee88f`), Step55 (`a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`) et Step57 (`bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f`) ont été lus sur GitHub. Le calcul local réutilise le **fichier b3c3a authentifié octet pour octet** (`e7f068a7c4063a27af2456515b58f8732b3b3343`), transcription algébrique source-fidèle de Step45, et reconstruit ses dérivées d'Euler et son crochet à six couples.

**34 assertions exactes SymPy PASS, 1 unittest de rejeu PASS, zéro échec final.** Un premier unittest a échoué sur un comptage erroné (35 au lieu de 34), corrigé avant publication ; aucune identité mathématique n'avait échoué. L'unittest rejoue les mêmes identités, il n'est pas indépendant. Les octets du programme et du test publiés ont été comparés aux fichiers réellement exécutés.

## Limites strictes

Ce certificat prouve la covariance **locale cinématique** de la secondaire réduite dans la carte K>0. Il ne prouve **ni** la différentiabilité du générateur radial sur le domaine à bords, **ni** l'absence de charges de bord, **ni** la covariance des conditions aux frontières, **ni** l'admissibilité d'une jauge temporelle, **ni** la compatibilité globale des lapses. Le rejeu b3c2 avec imports des **moteurs originaux Step45/55/58** reste à faire : les originaux ont été authentifiés mais **non exécutés** dans ce run. Aucun rang Dirac complet, contrainte tertiaire, analyse K=0/J=0, stabilité 4D ou observable cosmologique n'a été établi.

## Prochaine étape b3c3c

(1) Rejouer b3c2 avec les vrais imports originaux, comparer exactement ses coefficients centraux et vérifier indépendamment cette identité sur `exact_physical_ward()['C_exact']` ; (2) calculer le générateur radial/temporel amélioré et ses charges pour des conditions aux frontières explicites ; (3) résoudre le quotient de jauge temporelle et le rang de Dirac à six couples ; (4) seulement ensuite examiner K=0/J=0, 4D, stabilité et observables.

**GATE_2B OPEN — JANUS_R NOT_VALIDATED.**
