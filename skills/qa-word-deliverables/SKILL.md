---
name: qa-word-deliverables
description: Produire ou modifier des livrables QA au format Word (.docx) - stratégie de recette, plan de test, PV de recette, rapport de campagne - avec python-docx. Utiliser quand l'utilisateur demande un fichier Word, un .docx, un document à envoyer ou à signer, ou veut remplir un template Word client.
---

# Livrables QA Word

## Prérequis
`pip install python-docx` (Python 3.10+). Sur Windows, lancer les scripts avec `py`.

## Quand l'utiliser
- Exporter une stratégie ou un plan de test rédigé avec `qa-strategy-playwright`.
- Produire un PV de recette ou un rapport de campagne à partir de résultats (JSON, CSV, JUnit).
- Remplir un template Word fourni par le client sans casser sa mise en forme.

## Méthode
1. Rédiger d'abord le contenu en Markdown et le faire valider.
2. Si un template client existe, partir de lui (`Document("template.docx")`) : réutiliser ses styles
   (`Heading 1`, `Table Grid`...) au lieu d'en créer. Lister les styles disponibles avant d'écrire.
3. Sinon, utiliser `scripts/md_to_docx.py` qui convertit un Markdown simple (titres, paragraphes,
   listes, tableaux, gras) en .docx.
4. Vérifier le résultat : rouvrir le fichier et compter titres et tableaux, ou le convertir en PDF
   (`soffice --headless --convert-to pdf`) si LibreOffice est installé.

## Structures types
**PV de recette** : identification (projet, version, environnement, dates), périmètre testé,
synthèse chiffrée (exécutés / OK / KO / bloqués), anomalies ouvertes par sévérité, réserves,
décision (Go / Go avec réserves / No go), signatures.

**Rapport de campagne** : contexte, périmètre, résultats par groupe fonctionnel, analyse des KO,
tests bloqués et causes (ex. variables manquantes), risques, actions et responsables.

## Règles
- Tableaux : en-tête en gras, une ligne par élément, pas de cellules fusionnées sauf besoin réel.
- Ne pas inclure de token, mot de passe ou donnée client réelle.
- Nommer le fichier `<Projet>_<Livrable>_v<X.Y>_<AAAAMMJJ>.docx`.
