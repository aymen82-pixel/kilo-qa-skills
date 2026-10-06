---
name: kilo-skill-creator
description: Créer ou améliorer un skill Kilo Code (dossier .kilo/skills/<nom>/SKILL.md). Utiliser quand l'utilisateur veut transformer une méthode de travail récurrente (template de livrable, convention de tests, checklist, workflow) en skill réutilisable, ou corriger un skill qui ne se déclenche pas.
---

# Créer un skill Kilo Code

## Structure
```
.kilo/skills/<nom-du-skill>/
├── SKILL.md          # obligatoire
├── scripts/          # optionnel : scripts exécutables
└── references/       # optionnel : docs chargées seulement si besoin
```
- `name` dans le frontmatter = nom exact du dossier (minuscules, chiffres, tirets).
- Skills projet : `.kilo/skills/` à la racine du workspace. Skills globaux : `~/.kilo/skills/`
  (`C:\Users\<user>\.kilo\skills\` sous Windows). Le projet prime en cas de nom identique.
- Recharger VS Code ou l'extension après ajout.

## Méthode
1. Demander : que doit faire le skill, quand doit-il se déclencher, quel livrable produit-il,
   avec un ou deux exemples réels de demande.
2. Rédiger la `description` en premier : c'est le seul texte lu pour décider d'activer le skill.
   Elle dit ce que fait le skill ET les situations/mots qui doivent le déclencher.
3. Corps du SKILL.md : instructions impératives, structure du livrable, règles, un exemple court.
   Viser moins de 300 lignes ; déplacer le détail dans `references/` en indiquant quand le lire.
4. Mettre le code répétitif dans `scripts/` plutôt que de le faire réécrire à chaque fois.
5. Tester avec 2 ou 3 demandes réalistes ; si le skill ne se déclenche pas, enrichir la
   description ; s'il produit un mauvais résultat, préciser les instructions.

## Gabarit
```markdown
---
name: mon-skill
description: <Ce que fait le skill>. Utiliser quand <situations, mots-clés, types de fichiers>.
---

# <Titre>

## Quand l'utiliser
## Méthode
## Format du livrable
## Règles
```
