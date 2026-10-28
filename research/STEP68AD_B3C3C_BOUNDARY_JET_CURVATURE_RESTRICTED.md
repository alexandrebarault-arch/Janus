# JANUS — b3c3c : courbure exacte d'une tranche de jets de bord (28 octobre 2026)

## Source et résultat

Les densités originales Step45 post-IBP Fg=N Ag+N' Bg et Ff=M Af+M' Bf ont été lues dans numerics/hr_step45_exact_physical_ward.py, blob Git 66aa43841dccfe4a5d586a49be9c10af3a67a10e. Les termes contenant z' sont Ag ⊃ pLg z' et Af ⊃ pLg Lg z'/Lf. Aucun des quatre termes Ag,Af,Bg,Bf ne dépend de pLg' quand z,z' sont traités comme variables indépendantes. On a donc pour la variation de bord à z indépendant : alpha_z=pLg(N+M Lg/Lf) et alpha_pLg=0.

Sur K>0, poser D=pSg Sg'−Lg pLg'+pg tg', K=m2 mg Lg Lf (b1 Sg²+2 b2 Sg Sf+b3 Sf²), et z*=D/sqrt(D²+K²). Restreindre l'espace des variations de bord à (pLg,pLg') avec tous les autres jets, lapses et leurs dérivées fixés. Alors

    alpha = −pLg Lg (N+M Lg/Lf) K²/(D²+K²)^(3/2) d(pLg')

et sa dérivée extérieure exacte est

    d alpha = −Lg (N+M Lg/Lf) K²/(D²+K²)^(3/2) d(pLg)∧d(pLg').

Le coefficient est strictement négatif si Lg,Lf,N,M,K>0 et D fini. Témoin rationnel NON Step55 : Lg=2/5, Lf=3/5, N=M=1, D=3, K=4, coefficient −32/375.

## Portée critique

Sur cette tranche LIBRE des jets de bord, la 1-forme n'est pas fermée ; aucun contreterme qui soit la variation exacte d'une fonction lisse de ces deux jets ne peut l'annuler sur toute cette tranche. Une variation exacte ajoutée à alpha ne modifie pas d alpha. Ce résultat est CINÉMATIQUE et CONDITIONNEL à l'espace des variations choisi : ni tangence aux contraintes primaires/secondaires, ni admissibilité Dirac des variations, ni conditions physiques aux bords n'ont été démontrées. Fixer pLg ou pLg' réduit la tranche à une dimension et supprime la 2-forme. Des conditions mixtes, des variables de bord supplémentaires, ou un générateur amélioré pourraient changer l'analyse. Ceci n'est PAS le pullback physique de dTheta et ne prouve AUCUN no-go JANUS.

## Reproductibilité

15 assertions symboliques SymPy exactes PASS ; 4 unittest PASS (rejeu des mêmes formules, non indépendant) ; 0 échec final. Les scripts publiés ont été exécutés dans une structure de paquets numerics/tests analogue au dépôt. Une première assertion du témoin avait une substitution incorrecte de D,K dans une expression non développée ; correction avant publication, sans changement de la formule prouvée. Les imports originaux Step45/55/58 et le test b3c2 n'ont PAS été rejoués dans un clone complet (DNS Git indisponible dans le conteneur).

## Suite

b3c3d : rejouer b3c2 sur imports originaux, imposer les contraintes fonctionnelles et les conditions aux limites aux variations de bord, calculer générateurs améliorés et charges, jauge temporelle, puis Dirac six couples/rang/tertiaires, K=0/J=0, 4D, stabilité et observables.

GATE_2B OPEN ; JANUS_R NOT_VALIDATED.
