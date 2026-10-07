# Kilo QA Skills

Skills QA pour [Kilo Code](https://kilo.ai) (format Agent Skills, compatible aussi avec Claude Code) :
stratégie de recette, cas de test Gherkin/BDD, automatisation Playwright (UI et API), livrables Word,
suivi Excel, présentations PowerPoint, extraction d'exigences depuis des specs PDF,
économie de tokens et optimisation de prompts.

| Skill | Rôle |
|---|---|
| `qa-strategy-playwright` | Stratégie de recette, cas Gherkin (Xray / Zephyr / TestRail), automatisation Playwright POM et API |
| `qa-word-deliverables` | Plan de test, PV de recette, rapport de campagne en .docx |
| `qa-pv-recette` | PV de recette Word depuis un modèle générique BPCE et un JSON (US, anomalies, décision, visas) |
| `qa-excel-tracking` | Synthèse de campagne depuis un rapport JUnit Playwright, matrices de couverture, suivi d'anomalies |
| `qa-pptx-comite` | Bilan de campagne en PowerPoint |
| `qa-pdf-specs` | Extraction d'exigences et de critères d'acceptation depuis des PDF / Word / Excel |
| `kilo-skill-creator` | Créer ses propres skills Kilo |
| `token-saver` | Règles de lecture ciblée, éditions par diff et réponses courtes pour réduire les tokens |
| `context-handoff` | Résumé de passation compact pour repartir sur une nouvelle tâche |
| `project-map` | Carte compacte du projet (`.kilo/PROJECT_MAP.md`) à lire au lieu d'explorer le dépôt |
| `galileen-prompt-optimizer` | Galiléen, optimisation stratégique de prompts pour ChatGPT, Claude et Gemini |

## Installation

Pour un projet : copier le dossier `skills/` dans `.kilo/skills/` à la racine du projet.
Pour tous les projets : le copier dans `~/.kilo/skills/` (`C:\Users\<user>\.kilo\skills\` sous Windows).
Pour Claude Code : `.claude/skills/`.

Recharger VS Code ou l'extension Kilo ensuite.

## Prérequis des scripts

```
pip install python-docx python-pptx openpyxl pdfplumber pypdf
```

## Licence

MIT
