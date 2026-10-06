---
name: project-map
description: Générer et maintenir une carte compacte du projet (.kilo/PROJECT_MAP.md) - arborescence utile, rôle des dossiers, points d'entrée, commandes - pour que l'agent la lise au lieu d'explorer le dépôt à chaque tâche. Utiliser au démarrage sur un nouveau projet, quand l'utilisateur veut réduire les tokens, ou après une réorganisation importante.
---

# Carte du projet

## Générer
1. Lancer `py .kilo/skills/project-map/scripts/project_map.py` (ou `python3` hors Windows) depuis la
   racine du projet. Il écrit `.kilo/PROJECT_MAP.md` avec l'arborescence filtrée (profondeur 3 par
   défaut, dossiers lourds exclus) et le nombre de lignes par fichier.
2. Compléter à la main ou avec l'utilisateur la section "Rôle des dossiers" et "Commandes"
   (installation, lancement des tests, environnements), en une ligne par élément.

## Utiliser
- Lire `.kilo/PROJECT_MAP.md` en début de tâche avant toute exploration.
- Ne lister un dossier que si la carte ne suffit pas.

## Maintenir
- Régénérer après ajout ou déplacement de dossiers ; conserver les sections rédigées à la main
  (le script ne remplace que le bloc entre `<!-- AUTO:START -->` et `<!-- AUTO:END -->`).
- Garder le fichier sous 150 lignes : augmenter les exclusions ou réduire la profondeur sinon.
