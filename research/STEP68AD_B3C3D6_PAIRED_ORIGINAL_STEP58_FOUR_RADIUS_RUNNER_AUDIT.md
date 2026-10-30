# JANUS b3c3d6 — comparateur apparié des six coefficients Step58 (30 octobre 2026)

**Avancée instrumentale vérifiée ; PAS de rejeu physique. GATE_2B OPEN ; JANUS_R NOT_VALIDATED.**

## Problème reproductible corrigé

L'ancien probe `hr_b3c3d6_full_original_step58_point_probe.py` et le candidat cubique `hr_b3c3d6_corrected_step58_point_probe_candidate.py` appelaient chacun `u_solution(radius)` : leurs sorties ne pouvaient pas constituer une comparaison *strictement appariée* du même état terminal Step55. Le candidat utilise maintenant des entrées binary64 exactes et un transport d'extrémité d'ordre 2 non certifié, alors que l'ancien probe utilisait une autre convention. La différence de coefficients aurait pu mesurer la différence de solveur/abscisse plutôt que celle des prolongements.

Le nouveau runner `numerics/hr_b3c3d6_paired_original_step58_four_radii.py` résout **une seule fois** l'EDO candidate par rayon et injecte la **même paire** `(U(r²),G(r²,U))` dans les deux probes existants, sans changer les gardes SHA des cinq sources physiques. Quatre cartes sont comparées : affine historique mixte `pLfr=rG` (non holonome hors point), affine réellement holonome (contrôle négatif), quadratique holonome et cubique holonome. Pour les cartes tronquées, les valeurs `pLf''` et `pLf'''` des assertions internes sont recalculées sur le même polynôme ; les anciennes métadonnées de jets ODE qui ne s'appliquent plus sont retirées. Les impressions des probes originaux sont capturées dans les rapports afin que la sortie globale soit du JSON valide. Les monkeypatchs sont restaurés même en cas d'exception.

### Prédiction analytique préalable, non mesure physique

À **même** état, rayon et opérateur, les six coefficients `N0,N1,N2,M0,M1,M2` de l'affine mixte, du quadratique et du cubique doivent coïncider au niveau des jets utilisés par Step58 (audit de dépendances précédent). L'affine strictement holonome peut différer **uniquement en M0**, avec sensibilité physique algébrique `dA_M/dU_ss` déjà obtenue. Cette prédiction n'a PAS été testée numériquement sur les originaux dans cette session. Une différence observée ailleurs signalerait un problème de précision, d'abscisse, de jet ou de substitution ; une égalité flottante ne constituerait pas une enclosure.

### Reproduction requise sur un clone local authentifié

```bash
PYTHONPATH=. python -m unittest tests.test_hr_b3c3d6_paired_original_step58_four_radii -v
PYTHONPATH=. python -m numerics.hr_b3c3d6_paired_original_step58_four_radii > research/reports/b3c3d6_paired_original_step58_four_radii.json
```

Les cinq originaux requis sont les blobs Step45 `66aa43841dccfe4a5d586a49be9c10af3a67a10e`, Step46 `bac025c28dbe1561c0c36c56dbfda46dc326f804`, Step55 normalized `a54a6acf2f7ad2f64c500faecfa1406ecbf7b862`, Step55 barrier `a6e7004120d0a166a3a8973c2fbe1487a8eb70fe`, Step58 `802c23aebd41780d8c462f1aa1711707fe4ee88f`. Le shim Step57 reste minimal et doit être déclaré comme tel.

## Exécution effective et portée

**7 unittest isolés PASS, 0 FAIL final**, `compileall -q numerics tests` PASS, exécutés dans `/mnt/data/janus_paired`. Les tests utilisent des doublures d'opérateurs et vérifient le partage d'état, les quatre modes, les six différences, les jets tronqués, la restauration en exception et les quatre rayons. Un test a initialement échoué par une valeur attendue arithmétiquement incorrecte (51 au lieu de 37,5), corrigée avant le rejeu final. **0** appel physique Step45/46/55/58 ; **0** intégration DOP853 physique ; **0** coefficient A/B/E physique recalculé ; **0** enclosure ; **0** BVP. Le conteneur ne résout pas github.com/raw.githubusercontent.com ; le connecteur GitHub lit et écrit correctement.

Blobs publiés et relus, identiques aux octets testés : runner `bfb428de15d0d093d626f9b0f86fb42fa1f9442f`, tests `9331aca56cd0b845047c13cc3da4546044b2d510`. L'outil d'orchestration n'est **pas** une validation de la théorie JANUS.

## Prochaine étape bloquante

Exécuter le runner avec les cinq originaux SHA authentifiés et conserver les quatre rayons `1/4,1/2,7/10,17/20` ; comparer les six coefficients et la convergence du solveur, puis établir un défaut DOP853 **continu**, une erreur initiale et des enclosures physiques. Ensuite centre et lapses strictement positifs avec **deux vrais bords**, Dirac six couples, dynamique 4D, stabilité et observables. `main` et `research/v2-flrw` ne doivent pas être modifiées, aucun workflow réactivé.
