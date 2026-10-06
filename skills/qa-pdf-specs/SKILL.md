---
name: qa-pdf-specs
description: Lire des spécifications, cahiers des charges ou documentations en PDF (ou Word, Excel, CSV) pour en extraire les exigences, règles de gestion et critères d'acceptation à couvrir par des tests. Utiliser quand l'utilisateur fournit un document source et veut des exigences, une matrice de couverture ou des cas de test à partir de ce document. Sert aussi à exporter un rapport en PDF.
---

# Exploitation de specs PDF pour la QA

## Prérequis
`pip install pdfplumber pypdf python-docx openpyxl`

## Lecture
- **PDF texte** : `scripts/extract_pdf.py doc.pdf` sort le texte page par page (avec numéros de
  page) et les tableaux détectés en CSV. Lire d'abord la table des matières et le nombre de pages,
  puis seulement les sections utiles si le document est long.
- **PDF scanné** (aucun texte extrait) : le signaler à l'utilisateur ; l'OCR nécessite Tesseract
  (`pip install pytesseract pdf2image` + installation de Tesseract et Poppler sous Windows).
- **Word** : `python-docx` (paragraphes et tableaux). **Excel/CSV** : `openpyxl` ou module `csv`.

## Extraction des exigences
Pour chaque exigence trouvée, produire une ligne :
`ID | Source (doc + page/section) | Exigence reformulée | Type (fonctionnelle, règle de gestion, sécurité, perf) | Critère d'acceptation | Priorité proposée`

Règles :
- Citer la page ou la section source de chaque exigence pour la traçabilité.
- Signaler séparément les ambiguïtés, contradictions et informations manquantes sous forme de
  questions à poser aux BA, plutôt que de supposer une réponse.
- Ne pas inventer d'exigence absente du document.
- La sortie alimente ensuite `qa-strategy-playwright` (cas Gherkin) et `qa-excel-tracking` (matrice).

## Export PDF
Pour convertir un .docx ou .pptx en PDF : `soffice --headless --convert-to pdf fichier.docx`
(LibreOffice). Sinon, exporter depuis Word / PowerPoint.
