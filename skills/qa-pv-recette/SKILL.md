---
name: qa-pv-recette
description: Rédiger et générer un PV de recette (PV de tests de sprint ou de release) au format Word à partir d'un modèle générique BPCE - identification, périmètre US/bugs, synthèse, réserves, anomalies résiduelles, US non validées, décision, visas. Utiliser quand l'utilisateur demande un PV de recette, un PV de tests, un procès-verbal de recette ou une décision de passage en livraison.
---

# PV de recette

Génère un .docx à partir de `assets/pv_recette_template.docx` (mise en page, tableaux et cases à cocher
déjà prêts) et d'un fichier JSON. Aucun contenu client réel n'est dans le modèle.

## Prérequis
`pip install python-docx pillow`. Sous Windows, lancer avec `py`.

## Méthode
1. Collecter les données auprès de l'utilisateur ou de ses sources (export Jira/Xray, rapport JUnit,
   résultats de campagne). Ne rien inventer : un champ inconnu reste vide ou `""`.
2. Copier `references/example.json`, le remplir (voir champs ci-dessous).
3. Générer :
   ```
   py scripts/generate_pv.py data.json <Projet>_PV_recette_v1.0_<AAAAMMJJ>.docx
   ```
4. Vérifier : ouvrir le .docx (ou le convertir en PDF) et contrôler titres, tableaux, cases cochées.
   Le script signale les jetons `{{...}}` restés sans valeur.
5. Rappeler à l'utilisateur de remplacer les deux zones « logo » (page de garde et en-tête) par le
   logo officiel, et de relire la décision avant signature.

## Champs du JSON
| Champ | Contenu |
|---|---|
| `projet`, `domaine`, `equipe`, `iteration`, `version`, `date`, `date_modification`, `release` | Cartouche, page de garde et en-tête |
| `directeur_projet`, `product_owner`, `test_lead`, `analystes`, `contributeurs`, `service` | Intervenants |
| `environnement`, `periode` | Ex. `"Recette"`, `"Du 05/01/2026 au 14/01/2026"` |
| `stories`, `bugs` | Listes de `{id, libelle, sprint}` (US puis bugs/MCO) |
| `perimetre_tnr`, `hors_perimetre` | Listes de textes (vide = « Néant ») |
| `graphe` | Chemin d'une image (capture du graphe de couverture) ou `null` pour garder le cadre à remplacer |
| `reserves` | `{id, libelle}` |
| `anomalies` | `{id, libelle, severite, statut, contournement}` (contournement Oui / Non) |
| `non_validees` | `{id, libelle, commentaire, perimetre}` |
| `type_recette` | `"fonctionnels"`, `"tnr"` (les deux par défaut) |
| `decision` | `"accepte"`, `"accepte_reserves"` ou `"refuse"` |
| `reserves_statut` | `"bloquante"`, `"majeure"`, `"mineure"` ou `null` |
| `reserves_decision` | `{date, numero, descriptif}` du tableau de décision |
| `product_owner`, `sponsor_role`, `sponsor` | Bloc visas (PO et responsable métier) |

## Règles de rédaction
- Libellés courts et factuels, identifiants Jira tels quels (`PRJ-123`). Dates en `JJ/MM/AAAA`.
- Décision cohérente avec le contenu : `refuse` s'il reste une anomalie bloquante ouverte ;
  `accepte_reserves` s'il reste des anomalies majeures ou mineures avec réserves listées ;
  `accepte` seulement si aucune anomalie résiduelle ni US non validée.
- Une US non validée doit avoir un commentaire (reconduite au sprint suivant, refusée, etc.).
- Ne jamais mettre de noms, tickets, URL ou logos d'un autre client dans un PV BPCE. Le modèle
  est volontairement générique.
- Les signatures et dates de visa restent vierges : elles sont remplies à la main par les signataires.

## Modifier le modèle
Les jetons du modèle sont de la forme `{{champ}}` (cartouche) et `{{r.champ}}` (lignes clonées par
liste). Éditer le modèle dans Word sans changer ces jetons ni l'ordre des 8 cases à cocher
(fonctionnels, TNR, accepté, accepté avec réserves, refusé, bloquante, majeure, mineure).
