---
name: token-saver
description: Règles d'économie de tokens pour l'agent - lecture ciblée des fichiers, recherches avant lecture, éditions par diff, réponses courtes. Utiliser en permanence sur les gros projets, quand l'utilisateur demande de limiter la consommation de tokens, de réduire les coûts, ou quand le contexte devient long.
---

# Économie de tokens

## Lecture
- Chercher avant de lire : `search_files` / grep sur un symbole ou un mot-clé, puis lire seulement
  les lignes utiles (plage de lignes) au lieu du fichier entier.
- Si `.kilo/PROJECT_MAP.md` existe (skill `project-map`), le consulter avant toute exploration.
- Ne jamais lister ou lire `node_modules/`, `dist/`, `build/`, `.git/`, `playwright-report/`,
  `test-results/`, fichiers de lock, logs, rapports HTML, images, fichiers minifiés.
- Ne pas relire un fichier déjà lu dans la tâche s'il n'a pas changé.
- Pour un gros rapport (JUnit, JSON, logs), extraire d'abord les lignes pertinentes
  (échecs, erreurs, `grep -c`) plutôt que de charger tout le fichier.

## Écriture
- Modifier par remplacement ciblé (diff / search-and-replace), jamais en réécrivant un fichier
  entier pour changer quelques lignes.
- Ne pas recopier dans la réponse du code déjà écrit dans un fichier.
- Regrouper les modifications d'un même fichier en une seule opération.

## Commandes
- Limiter la sortie des commandes : `--reporter=line` ou `--reporter=dot` pour Playwright,
  `| tail -n 40`, `--quiet`, filtrage sur les échecs.
- Lancer un seul test ou un seul fichier pour valider un correctif (`npx playwright test fichier -g "TC-001"`)
  avant la suite complète.

## Réponses
- Répondre court : ce qui a été fait, le résultat, et ce qui bloque. Pas de récapitulatif, pas
  de reformulation de la demande, pas d'explication non demandée.
- Poser une question plutôt que d'explorer largement quand une information manque.

## Contexte
- Une tâche = un objectif. Quand l'objectif change ou que la conversation devient longue,
  utiliser le skill `context-handoff` et repartir sur une nouvelle tâche.
