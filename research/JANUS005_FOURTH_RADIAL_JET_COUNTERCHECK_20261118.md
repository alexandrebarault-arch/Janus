# JANUS-005 — quatrième jet radial le long de la tangente KG/CF (2026-11-18)

**Statut : résultat algébrique local seulement ; GATE_2B=OPEN ; JANUS_R=NOT_VALIDATED.**

## Provenance et protocole
Baseline GitHub main `5f9e50d4afc9bb6efefb6285889996ec9635435d`. Formule de densité et paramètres repris du fichier authentique `research/repro/janus005_third_radial_jet_replay_20261115.py` (lu via connecteur GitHub à ce HEAD). Reconstitution locale de la même formule dans Python, **pas** un transfert octet-à-octet du script original. Python + mpmath, précision `mp.mp.dps=40`.

Définir `a_n(p) = (1/n!) (d^n rho_g(s,p)/ds^n)|_{s=0}`. Reprendre la tangente à six composantes `d=(1,-(4*A**3*M*C+0.9)/(A**4*C),-Z/A,-CG/A,dKG,dCF)`, avec `dKG,dCF` obtenus par résolution linéaire des deux conditions `D a_1=D a_2=0`, exactement comme dans le script original. Évaluer ensuite `D a_n = sum_i partial_{p_i} a_n * d_i` pour n=0,...,4 avec `mp.diff`.

Commande locale réellement exécutée : `python /mnt/data/janus005_fourth_jet.py`. Le fichier local n'est **pas** durablement conservé dans le dépôt ; reproduction possible en étendant la boucle `for n in (1,2,3)` du script Git original à `for n in (0,1,2,3,4)` et en retirant l'assertion propre à n=3. Pour contrôler n=4, utiliser les différences finies centrées de `jet(4,p)` aux pas `h=1e-3,1e-4`.

## Résultats exécutés
- `D a_0 = +2.60009248497312617729412915704e-39` (zéro numérique).
- `D a_1 = -7.17464813734306340312949546644e-43` (zéro numérique).
- `D a_2 = 0`.
- `D a_3 = +0.0000106859855966529402056407979307` (reproduction du résultat antérieur).
- **`D a_4 = -0.000000123211326921505438740229892665`** (nouveau contrôle local).
- Différences finies centrées du quatrième jet : `h=0.001` → `-0.0000001232164382322273287763863` ; `h=0.0001` → `-0.000000123211378027221480626226`. Convergence compatible avec une erreur d'ordre h².

## Portée contradictoire
La tangente compensant les jets 1 et 2 ne conserve ni le jet 3 ni le jet 4 de cette **famille algébrique prescrite**. Cela ne démontre pas la fixation physique de ces jets, ni l'admissibilité de la tangente sous contraintes de Dirac, ni les deux conditions aux vrais bords, ni un NO-GO du modèle JANUS. Le quatrième jet n'ajoute pas de rang à une matrice déjà de rang 3 dans la sous-famille testée. Ce contrôle ne certifie aucune cellule Step55/58.

Tests numériques locaux : calcul différentiel PASS ; différences finies PASS. Tests moteur b3c3d9 SKIP ; pilote SKIP ; cellules physiques évaluées/certifiées/inconclusives : 0/0/0.

**NEXT_ACTION_EXACT :** confronter la tangente aux équations de contraintes et aux conditions des deux vrais bords (JANUS-005/006), sans multiplier les jets algébriques non contraints. Pour JANUS-001 : transférer les imports Step45/46/55/58 avec vérification des SHA Git locaux, exécuter les neuf tests et le pilote physique à une cellule.
