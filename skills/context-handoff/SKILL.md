---
name: context-handoff
description: Produire un résumé de passation compact pour repartir sur une nouvelle tâche Kilo sans perdre l'essentiel, afin de réduire le contexte et la consommation de tokens. Utiliser quand l'utilisateur dit "nouvelle tâche", "on repart à zéro", "résume pour la suite", quand la conversation est longue ou quand l'objectif change.
---

# Passation de contexte

## But
Remplacer un long historique par un résumé de 30 lignes maximum, réutilisable comme premier
message d'une nouvelle tâche.

## Contenu du résumé (dans cet ordre)
```markdown
# Passation - <sujet> - <date>
## Objectif
<1 à 2 lignes>
## État actuel
- Fait : <livrables, fichiers créés ou modifiés, avec leur chemin>
- En cours : <ce qui reste à terminer>
## Décisions prises
- <décision> : <raison en quelques mots>
## Points bloquants / questions ouvertes
- <...>
## Prochaine étape
<une action précise>
## Fichiers à relire en priorité
- <chemin> (lignes X-Y si pertinent)
```

## Règles
- Ne garder que ce qui sert la suite : pas d'historique des essais ratés, sauf la leçon utile.
- Référencer les fichiers par leur chemin au lieu d'en recopier le contenu.
- Ne jamais inclure de secret, token ou mot de passe.
- Si l'utilisateur le demande, enregistrer le résumé dans `.kilo/handoff/<AAAAMMJJ>-<sujet>.md`.
