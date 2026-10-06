---
name: qa-pptx-comite
description: Générer une présentation PowerPoint (.pptx) de restitution QA - bilan de campagne, avancement de recette, stratégie de test pour un comité ou une équipe - avec python-pptx. Utiliser dès que l'utilisateur veut des slides, une présentation ou un support de réunion sur des résultats de tests.
---

# Présentations QA PowerPoint

## Prérequis
`pip install python-pptx`

## Méthode
1. Partir des chiffres réels (synthèse Excel de `qa-excel-tracking` ou rapport JUnit). Ne jamais
   inventer de chiffres : si une donnée manque, laisser un emplacement explicite `[À compléter]`.
2. Valider le plan des slides avec l'utilisateur avant de générer.
3. Générer avec `scripts/build_deck.py` à partir d'un JSON de contenu, ou en partant du template
   PowerPoint du client s'il est fourni (`Presentation("template.pptx")` et ses layouts).

## Plan type - bilan de campagne
1. Titre (projet, campagne, date)
2. Contexte et périmètre (groupes testés, environnement)
3. Résultats globaux (graphique OK / KO / skipped)
4. Résultats par groupe fonctionnel (tableau)
5. Analyse des KO (principales causes)
6. Tests bloqués et dépendances (variables manquantes, interlocuteurs attendus)
7. Risques
8. Prochaines étapes et demandes à l'équipe

## Règles de forme
- Une idée par slide, 6 lignes maximum, pas de paragraphes.
- Les chiffres clés en gros, le détail en tableau.
- Graphiques natifs PowerPoint (`add_chart`) pour qu'ils restent éditables.

## Format du JSON pour build_deck.py
```json
{
  "title": "Campagne API - Release X.Y",
  "subtitle": "Bilan au JJ/MM/AAAA",
  "slides": [
    {"type": "bullets", "title": "Périmètre", "bullets": ["...", "..."]},
    {"type": "chart", "title": "Résultats globaux", "categories": ["OK","KO","Skipped"], "values": [0,0,0]},
    {"type": "table", "title": "Par groupe", "header": ["Groupe","OK","KO","Skipped"], "rows": [["Groupe A","0","0","0"]]}
  ]
}
```
