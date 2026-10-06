---
name: qa-excel-tracking
description: Créer ou mettre à jour des fichiers Excel de suivi QA - matrice de couverture, suivi d'exécution de campagne, suivi d'anomalies, synthèse OK/KO/skipped par groupe fonctionnel - avec openpyxl. Utiliser pour tout fichier .xlsx ou .csv de suivi de tests, y compris l'analyse de rapports JUnit Playwright.
---

# Suivi QA Excel

## Prérequis
`pip install openpyxl`

## Cas d'usage
- **Synthèse de campagne** : à partir du `results/junit.xml` Playwright, `scripts/junit_to_xlsx.py`
  produit un classeur avec un onglet Détail (un test par ligne) et un onglet Synthèse
  (OK / KO / skipped par groupe, taux de réussite) calculé par formules Excel.
- **Matrice de couverture** : exigences ou endpoints en lignes, cas de test en colonnes ou
  colonne de liens, statut de couverture.
- **Suivi d'anomalies** : ID, titre, sévérité, statut, groupe, date, responsable.

## Règles
- Utiliser des formules Excel (`COUNTIFS`, `SUM`) pour les totaux plutôt que des valeurs calculées
  en Python, afin que le fichier reste juste quand on le modifie.
- En-tête figé (`ws.freeze_panes = "A2"`), filtre automatique, largeurs de colonnes ajustées.
- Mise en forme conditionnelle simple : vert OK, rouge KO, gris skipped.
- Pour modifier un classeur existant, le charger sans perdre les formules
  (`load_workbook(path)` sans `data_only=True`) et ne pas réécrire les onglets non concernés.
- Le groupe fonctionnel se déduit du chemin du test (`tests/api/<groupe>/...`).
