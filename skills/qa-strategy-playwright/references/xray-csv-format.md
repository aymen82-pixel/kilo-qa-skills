# Format CSV Xray — Import Jira Xray

## Structure du CSV (séparateur point-virgule)

### Cas de test manuels (Manual Tests)

```
"Test Type";"Summary";"Description";"Step Action";"Step Data";"Step Result";"Labels";"Priority";"Component"
"Manual";"TC-001 - Connexion valide";"Vérifier la connexion avec identifiants corrects";"Accéder à /login";"URL: http://rec.app.fr/login";"Page de connexion affichée";"smoke;critique";"High";"Auth"
```

### Cas de test Cucumber/BDD

```
"Test Type";"Summary";"Gherkin Type";"Scenario";"Labels";"Priority"
"Cucumber";"TC-001 - Connexion valide";"Scenario";"Given l'utilisateur est sur /login\nWhen il saisit email valide et mot de passe\nThen il est redirigé vers /dashboard";"smoke;critique";"High"
```

## Script Python — Génération CSV Xray (fiable)

```python
import csv
import io

def generate_xray_manual_csv(test_cases: list[dict]) -> str:
    """
    Génère un CSV compatible Xray pour des cas de test manuels.
    
    test_cases: liste de dicts avec les clés:
      - id, summary, description, steps (list of {action, data, result}),
        labels, priority, component
    """
    output = io.StringIO()
    
    fieldnames = [
        "Test Type", "Summary", "Description",
        "Step Action", "Step Data", "Step Result",
        "Labels", "Priority", "Component"
    ]
    
    writer = csv.DictWriter(
        output,
        fieldnames=fieldnames,
        delimiter=';',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n'
    )
    writer.writeheader()
    
    for tc in test_cases:
        steps = tc.get('steps', [])
        for i, step in enumerate(steps):
            row = {
                "Test Type": "Manual" if i == 0 else "",
                "Summary": tc['id'] + " - " + tc['summary'] if i == 0 else "",
                "Description": tc.get('description', '') if i == 0 else "",
                "Step Action": step.get('action', ''),
                "Step Data": step.get('data', ''),
                "Step Result": step.get('result', ''),
                "Labels": ';'.join(tc.get('labels', [])) if i == 0 else "",
                "Priority": tc.get('priority', 'Medium') if i == 0 else "",
                "Component": tc.get('component', '') if i == 0 else "",
            }
            writer.writerow(row)
    
    return output.getvalue()


def generate_xray_cucumber_csv(feature_blocks: list[dict]) -> str:
    """
    Génère un CSV compatible Xray pour des cas de test Cucumber/BDD.
    
    feature_blocks: liste de dicts avec les clés:
      - id, summary, gherkin_type (Scenario|Scenario Outline),
        scenario (texte Gherkin complet), labels, priority
    """
    output = io.StringIO()
    
    fieldnames = [
        "Test Type", "Summary", "Gherkin Type",
        "Scenario", "Labels", "Priority"
    ]
    
    writer = csv.DictWriter(
        output,
        fieldnames=fieldnames,
        delimiter=';',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n'
    )
    writer.writeheader()
    
    for tc in feature_blocks:
        writer.writerow({
            "Test Type": "Cucumber",
            "Summary": tc['id'] + " - " + tc['summary'],
            "Gherkin Type": tc.get('gherkin_type', 'Scenario'),
            "Scenario": tc['scenario'],  # \n dans le texte = OK avec QUOTE_ALL
            "Labels": ';'.join(tc.get('labels', [])),
            "Priority": tc.get('priority', 'Medium'),
        })
    
    return output.getvalue()


# --- Exemple d'utilisation ---

if __name__ == "__main__":
    
    # Cas manuels
    manual_tests = [
        {
            "id": "TC-001",
            "summary": "Connexion valide",
            "description": "Vérifier la connexion avec identifiants valides",
            "labels": ["smoke", "critique"],
            "priority": "High",
            "component": "Auth",
            "steps": [
                {"action": "Accéder à /login", "data": "", "result": "Page de connexion affichée"},
                {"action": "Saisir email", "data": "user@test.fr", "result": "Email saisi dans le champ"},
                {"action": "Saisir mot de passe", "data": "Password123!", "result": "Mot de passe masqué saisi"},
                {"action": "Cliquer sur Connexion", "data": "", "result": "Redirection vers /dashboard"},
            ]
        }
    ]
    
    # Cas BDD
    cucumber_tests = [
        {
            "id": "TC-001",
            "summary": "Connexion valide",
            "gherkin_type": "Scenario",
            "labels": ["smoke", "critique"],
            "priority": "High",
            "scenario": (
                "Given l'utilisateur est sur la page /login\n"
                "When il saisit l'email 'user@test.fr'\n"
                "And il saisit le mot de passe 'Password123!'\n"
                "And il clique sur le bouton Connexion\n"
                "Then il est redirigé vers /dashboard\n"
                "And le message de bienvenue est affiché"
            )
        }
    ]
    
    with open("xray_manual_export.csv", "w", encoding="utf-8-sig") as f:
        f.write(generate_xray_manual_csv(manual_tests))
    
    with open("xray_cucumber_export.csv", "w", encoding="utf-8-sig") as f:
        f.write(generate_xray_cucumber_csv(cucumber_tests))
    
    print("✅ Fichiers CSV générés avec succès")
```

## Notes importantes

- Utiliser **`utf-8-sig`** (BOM) pour l'encodage → évite les problèmes d'accents dans Jira
- Le `QUOTE_ALL` est essentiel pour les contenus multilignes (Gherkin)
- Le séparateur **point-virgule** est le standard Xray (configurable dans Jira)
- Les steps vides entre deux cas sont ignorés par Xray à l'import
- Pour Zephyr Scale : séparateur virgule, format légèrement différent (voir doc officielle)
