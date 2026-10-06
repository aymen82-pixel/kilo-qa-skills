---
name: qa-strategy-playwright
description: >
  Skill QA spécialisé pour produire des livrables de recette complets et professionnels en trois phases :
  (1) rédiger une stratégie de recette / plan de test structuré, (2) générer des cas de test manuels
  en Gherkin/BDD compatibles Xray, Zephyr Scale ou TestRail, (3) automatiser ces cas avec Playwright
  (TypeScript ou JavaScript) en appliquant le Page Object Model.
  
  Déclencher ce skill dès que l'utilisateur mentionne : stratégie de recette, plan de test, cas de test
  manuels, scénarios BDD, Gherkin, automatisation Playwright, test fonctionnel, test de non-régression,
  couverture fonctionnelle, Xray, Zephyr, TestRail, import CSV de tests, ou toute demande de documentation
  QA structurée. Même si l'utilisateur ne demande qu'une seule des trois phases, utiliser ce skill.
---

# QA Strategy & Playwright Skill

## Vue d'ensemble

Ce skill guide l'agent dans la production de trois livrables QA imbriqués :

```
Phase 1 → Stratégie de recette (document de cadrage)
Phase 2 → Cas de test manuels (Gherkin/BDD, prêts à importer)
Phase 3 → Automatisation Playwright (POM, TypeScript)
```

Les phases sont indépendantes mais pensées pour s'enchaîner. Identifier quelle(s) phase(s) l'utilisateur demande avant de commencer.

---

## Phase 1 - Stratégie de recette

### Objectif
Produire un document de stratégie couvrant le contexte projet, le périmètre, les risques, les critères de qualité et l'organisation des tests.

### Structure standard du document

```markdown
# Stratégie de Recette - [Nom du Projet] v[X.Y]

## 1. Contexte & Objectifs
- Application / module testé
- Objectif de la campagne (recette fonctionnelle, TNR, UAT, recette de livraison...)
- Version / sprint / release concerné(e)

## 2. Périmètre de test
### 2.1 Dans le périmètre (in-scope)
### 2.2 Hors périmètre (out-of-scope)

## 3. Approche de test
- Niveaux de test : unitaire / intégration / système / UAT
- Types de test : fonctionnel, TNR, performance, sécurité, accessibilité
- Priorités : critique > haute > moyenne > faible

## 4. Environnements & données
| Environnement | URL | Données | Responsable |
|---|---|---|---|
| Recette (REC) | ... | Jeu de données A | QA Lead |
| Pré-production | ... | Anonymisées | QA Lead |

## 5. Critères d'entrée / sortie
### Critères d'entrée (Definition of Ready for test)
- [ ] Build déployé et stable
- [ ] Données de test disponibles
- [ ] Accès environnement validé
- [ ] User stories avec critères d'acceptation

### Critères de sortie (Definition of Done for test)
- [ ] 100% des cas critiques exécutés
- [ ] Taux de succès ≥ 95% sur les cas critiques
- [ ] 0 anomalie bloquante ouverte
- [ ] Rapport de recette signé

## 6. Gestion des anomalies
- Outil : [Jira / Azure DevOps / ...]
- Sévérités : Bloquant / Majeur / Mineur / Cosmétique
- Workflow : Ouvert → En cours → Corrigé → Vérifié → Fermé

## 7. Livrables QA
| Livrable | Format | Échéance |
|---|---|---|
| Plan de test | Word/Confluence | J-5 |
| Cas de test | Xray/Zephyr/CSV | J-3 |
| Rapport d'exécution | Confluence/PDF | J+2 |

## 8. Planning & ressources
- Charge estimée : X jours/homme
- Ressources : [noms/rôles]
- Jalons : [dates clés]

## 9. Risques & mitigations
| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Environnement instable | Élevée | Fort | Smoke test quotidien |
| Données insuffisantes | Moyenne | Moyen | Jeu de données synthétique |
```

### Instructions de rédaction
1. Demander à l'utilisateur le contexte si non fourni : nom de l'application, type de livraison, équipe, outil de gestion de tests.
2. Adapter le niveau de détail : livraison critique → exhaustif ; sprint classique → allégé.
3. Toujours inclure une matrice risques/mitigations.
4. Produire en Markdown ; si un export Word est demandé, utiliser le skill `qa-word-deliverables`.

---

## Phase 2 - Cas de test manuels (Gherkin/BDD)

### Objectif
Générer des cas de test structurés en Gherkin, organisés par fonctionnalité, avec les métadonnées nécessaires à l'import dans Xray, Zephyr Scale ou TestRail.

### Structure d'un cas de test Gherkin

```gherkin
# Feature: [Domaine fonctionnel]
# ID: TC-[NNN]
# Priorité: Critique | Haute | Moyenne | Faible
# Type: Fonctionnel | TNR | Régression | Smoke

Feature: [Nom de la fonctionnalité]

  Background:
    Given [précondition commune à tous les scénarios]

  @critique @smoke
  Scenario: [Titre court et explicite - cas nominal]
    Given [état initial]
    When [action de l'utilisateur]
    Then [résultat attendu observable]
    And [assertion complémentaire si nécessaire]

  @haute @regression
  Scenario Outline: [Titre - cas avec données multiples]
    Given [état initial avec <variable>]
    When [action avec <variable>]
    Then [résultat avec <attendu>]

    Examples:
      | variable | attendu |
      | valeur1  | résultat1 |
      | valeur2  | résultat2 |

  @erreur @negative
  Scenario: [Titre - cas d'erreur / limite]
    Given [état initial]
    When [action invalide ou hors limite]
    Then [message d'erreur ou comportement attendu]
```

### Règles de rédaction des cas de test
- **Given** : état du système, données en place, utilisateur connecté
- **When** : UNE seule action utilisateur par step (pas de "et puis")
- **Then** : résultat observable et vérifiable (pas "le système fonctionne")
- **And/But** : pour enchaîner des assertions du même type
- Chaque scénario est **indépendant** (pas de dépendance d'ordre d'exécution)
- Nommer les scénarios avec le format : `[Cas nominal/alternatif/erreur] - [Contexte]`

### Couverture recommandée par fonctionnalité
```
✅ Cas nominal (happy path) - priorité Critique
✅ Cas alternatifs (branches secondaires) - priorité Haute
✅ Cas aux limites (valeurs min/max, vide, null) - priorité Haute
✅ Cas d'erreur (messages, rollback) - priorité Moyenne
✅ Cas de sécurité basique (injection, accès non autorisé) - priorité Haute
```

### Format CSV pour import Xray (Jira)
Voir `references/xray-csv-format.md` pour le détail complet du format et le script Python de génération.

### Format CSV pour import Zephyr Scale
```
Name,Status,Priority,Component,Labels,Description,Steps
"TC-001 - Connexion valide",Active,High,Auth,"smoke,critique","Vérifier la connexion avec identifiants valides","Step 1: Saisir email valide|Step 2: Saisir mot de passe|Step 3: Cliquer Connexion|Expected: Redirection tableau de bord"
```

---

## Phase 3 - Automatisation Playwright (TypeScript)

### Architecture recommandée - Page Object Model

```
project-root/
├── playwright.config.ts
├── package.json
├── tests/
│   ├── [feature].spec.ts        ← fichiers de test (1 par Feature)
│   └── fixtures/
│       └── test-data.ts         ← données de test centralisées
├── pages/
│   ├── BasePage.ts              ← méthodes communes (wait, navigate...)
│   └── [FeaturePage].ts         ← POM par page/fonctionnalité
└── helpers/
    └── api-helpers.ts           ← setup via API si besoin
```

### Template BasePage.ts

```typescript
import { Page, Locator } from '@playwright/test';

export class BasePage {
  readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async navigate(path: string): Promise<void> {
    await this.page.goto(path);
  }

  async waitForPageLoad(): Promise<void> {
    await this.page.waitForLoadState('networkidle');
  }

  async takeScreenshot(name: string): Promise<void> {
    await this.page.screenshot({ path: `screenshots/${name}.png`, fullPage: true });
  }
}
```

### Template Page Object - exemple LoginPage.ts

```typescript
import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class LoginPage extends BasePage {
  // Locators - préférer data-testid, puis aria-label, puis CSS sémantique
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    super(page);
    this.emailInput = page.getByTestId('email-input');
    this.passwordInput = page.getByTestId('password-input');
    this.submitButton = page.getByRole('button', { name: /connexion/i });
    this.errorMessage = page.getByRole('alert');
  }

  async login(email: string, password: string): Promise<void> {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }

  async expectErrorMessage(message: string): Promise<void> {
    await expect(this.errorMessage).toBeVisible();
    await expect(this.errorMessage).toContainText(message);
  }
}
```

### Template Spec - correspondance Gherkin → Playwright

```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { DashboardPage } from '../pages/DashboardPage';
import { TEST_USERS } from './fixtures/test-data';

// Feature: Authentification utilisateur

test.describe('Authentification', () => {

  test.beforeEach(async ({ page }) => {
    // Background: Given l'utilisateur est sur la page de connexion
    await page.goto('/login');
  });

  // TC-001 @critique @smoke
  // Scenario: Connexion avec identifiants valides
  test('TC-001 - Connexion valide - Redirection tableau de bord', async ({ page }) => {
    const loginPage = new LoginPage(page);
    const dashboardPage = new DashboardPage(page);

    // When l'utilisateur saisit des identifiants valides
    await loginPage.login(TEST_USERS.standard.email, TEST_USERS.standard.password);

    // Then il est redirigé vers le tableau de bord
    await expect(page).toHaveURL('/dashboard');
    await expect(dashboardPage.welcomeMessage).toBeVisible();
  });

  // TC-002 @haute @negative
  // Scenario: Connexion avec mot de passe incorrect
  test('TC-002 - Connexion invalide - Message d\'erreur affiché', async ({ page }) => {
    const loginPage = new LoginPage(page);

    // When l'utilisateur saisit un mot de passe incorrect
    await loginPage.login(TEST_USERS.standard.email, 'mauvais_mdp');

    // Then un message d'erreur est affiché
    await loginPage.expectErrorMessage('Identifiants incorrects');
    await expect(page).toHaveURL('/login');
  });

  // TC-003 @haute @parametric
  // Scenario Outline: Validation des champs obligatoires
  const invalidCases = [
    { email: '', password: 'valid123', expectedError: 'Email requis' },
    { email: 'user@test.com', password: '', expectedError: 'Mot de passe requis' },
    { email: 'invalid-email', password: 'valid123', expectedError: 'Email invalide' },
  ];

  for (const { email, password, expectedError } of invalidCases) {
    test(`TC-003 - Validation champ - ${expectedError}`, async ({ page }) => {
      const loginPage = new LoginPage(page);
      await loginPage.login(email, password);
      await loginPage.expectErrorMessage(expectedError);
    });
  }
});
```

### Configuration playwright.config.ts recommandée

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['html', { outputFolder: 'playwright-report' }],
    ['junit', { outputFile: 'results/junit.xml' }],  // pour Xray/Jira
  ],
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
  ],
});
```

---

## Phase 3 bis - Tests API Playwright

Pour une application testée au niveau API (nombreux endpoints répartis en groupes fonctionnels),
appliquer les conventions ci-dessous.

### Conventions à respecter
- Un dossier de specs par groupe fonctionnel : `tests/api/<groupe>/`.
- Chaque test suit la structure Given / When / Then en commentaires, comme les cas Gherkin.
- Les variables d'environnement (URL, tokens, ID de ressources) viennent de
  `.env.uat` (prioritaire) ou `.env.dev`, chargés selon `TEST_ENV`. Ne jamais coder un ID en dur.
- Un test dont une variable obligatoire est absente est marqué `test.skip` avec le nom de la variable
  manquante dans le message, pour que le rapport liste précisément ce qui bloque.
- Ne jamais écrire de secret, token ou donnée de production réelle dans le code, les logs ou les rapports.

### Fixture API
```typescript
// fixtures/api.ts
import { test as base, APIRequestContext, request } from '@playwright/test';
import * as dotenv from 'dotenv';
dotenv.config({ path: `.env.${process.env.TEST_ENV ?? 'uat'}` });

export function requireEnv(...names: string[]): string | null {
  const missing = names.filter(n => !process.env[n]);
  return missing.length ? `Variables manquantes : ${missing.join(', ')}` : null;
}

export const test = base.extend<{ api: APIRequestContext }>({
  api: async ({}, use) => {
    const ctx = await request.newContext({
      baseURL: process.env.APP_BASE_URL,
      extraHTTPHeaders: { Authorization: `Bearer ${process.env.APP_TOKEN}` },
    });
    await use(ctx);
    await ctx.dispose();
  },
});
export { expect } from '@playwright/test';
```

### Template de test API
```typescript
// tests/api/projects/projects.spec.ts
import { test, expect, requireEnv } from '../../../fixtures/api';

test.describe('Projets', () => {
  // TC-PRJ-001 @critique @smoke
  test('TC-PRJ-001 - GET projet existant - 200 et schéma attendu', async ({ api }) => {
    const missing = requireEnv('APP_PROJECT_ID');
    test.skip(!!missing, missing ?? '');

    // Given un projet existant
    const id = process.env.APP_PROJECT_ID!;
    // When on récupère le projet
    const res = await api.get(`/projects/${id}`);
    // Then la réponse est 200 et contient l'ID demandé
    expect(res.status()).toBe(200);
    const body = await res.json();
    expect(body).toHaveProperty('id', id);
  });

  // TC-PRJ-002 @haute @negative
  test('TC-PRJ-002 - GET projet inexistant - 404', async ({ api }) => {
    const res = await api.get('/projects/00000000-0000-0000-0000-000000000000');
    expect(res.status()).toBe(404);
  });
});
```

### Couverture minimale par endpoint
Nominal (2xx + contrôle du corps), authentification absente ou invalide (401/403),
ressource inexistante (404), payload invalide (400/422) pour les méthodes d'écriture.

### Reporting
Activer les reporters `html` et `junit` (import Xray). Pour la restitution d'une campagne,
produire un récapitulatif OK / KO / skipped par groupe fonctionnel, avec pour les skipped
la liste des variables manquantes agrégées : c'est l'entrée des skills `qa-excel-tracking`
et `qa-pptx-comite`.

---

## Workflow complet - Comment utiliser ce skill

### Si l'utilisateur fournit un contexte projet
1. **Identifier** quelles phases sont demandées (1, 2, 3 ou les trois)
2. **Interroger** si manquant : nom appli, fonctionnalités à tester, outil de test management, stack technique
3. **Produire** les livrables dans l'ordre : stratégie → cas manuels → specs Playwright
4. **Proposer** exports : `.md` inline, `.docx` (via skill `qa-word-deliverables`), `.feature` (Gherkin), `.spec.ts`

### Si l'utilisateur ne fournit qu'une user story ou une description fonctionnelle
1. Extraire les critères d'acceptation implicites
2. Générer directement les scénarios Gherkin couvrant nominal + alternatifs + erreurs
3. Proposer la transformation en Playwright specs

### Si l'utilisateur veut uniquement automatiser des cas existants
1. Demander les cas de test (Gherkin, tableau, description libre)
2. Mapper chaque scénario en `test()` Playwright
3. Créer les POMs nécessaires
4. Livrer la structure complète prête à exécuter

---

## Références complémentaires

- `references/xray-csv-format.md` - Format CSV détaillé pour import Jira Xray + script Python
- `references/playwright-best-practices.md` - Locators, assertions, gestion des attentes, CI/CD

Lire ces fichiers si l'utilisateur demande des détails spécifiques sur ces sujets.
