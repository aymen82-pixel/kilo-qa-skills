# Playwright — Bonnes pratiques QA

## Stratégie de sélecteurs (par ordre de préférence)

```typescript
// ✅ 1. data-testid (stable, indépendant du CSS)
page.getByTestId('submit-button')

// ✅ 2. Rôle ARIA (accessible, sémantique)
page.getByRole('button', { name: /connexion/i })
page.getByRole('textbox', { name: /email/i })
page.getByRole('heading', { level: 1 })

// ✅ 3. Label associé (formulaires)
page.getByLabel('Mot de passe')

// ✅ 4. Texte visible
page.getByText('Tableau de bord')

// ⚠️ 5. CSS — dernier recours, fragile
page.locator('.btn-primary')  // à éviter si possible
page.locator('#submit')       // acceptable si ID stable
```

## Assertions robustes (auto-retry intégré)

```typescript
// Visibilité
await expect(locator).toBeVisible();
await expect(locator).toBeHidden();

// URL
await expect(page).toHaveURL('/dashboard');
await expect(page).toHaveURL(/dashboard/);

// Texte
await expect(locator).toHaveText('Message exact');
await expect(locator).toContainText('partiel');

// Valeur de formulaire
await expect(input).toHaveValue('contenu attendu');

// Attribut
await expect(button).toBeDisabled();
await expect(checkbox).toBeChecked();

// Comptage
await expect(page.getByRole('listitem')).toHaveCount(5);
```

## Gestion des attentes — éviter les sleep()

```typescript
// ✅ Attendre un état réseau
await page.waitForLoadState('networkidle');

// ✅ Attendre qu'un élément soit visible
await expect(locator).toBeVisible({ timeout: 10_000 });

// ✅ Attendre une réponse API
const responsePromise = page.waitForResponse('**/api/login');
await loginPage.submit();
const response = await responsePromise;
expect(response.status()).toBe(200);

// ✅ Attendre une navigation
await Promise.all([
  page.waitForURL('/dashboard'),
  loginPage.submit(),
]);

// ❌ À éviter absolument
await page.waitForTimeout(3000);  // flaky, lent
```

## Intercepter les APIs (mocking)

```typescript
// Mocker une réponse API pour tester les cas d'erreur
await page.route('**/api/login', async route => {
  await route.fulfill({
    status: 401,
    contentType: 'application/json',
    body: JSON.stringify({ error: 'Unauthorized' }),
  });
});
```

## Fixtures et données de test

```typescript
// tests/fixtures/test-data.ts
export const TEST_USERS = {
  standard: { email: 'user@test.fr', password: 'Password123!' },
  admin: { email: 'admin@test.fr', password: 'Admin123!' },
  locked: { email: 'locked@test.fr', password: 'Locked123!' },
} as const;

export const TEST_URLS = {
  login: '/login',
  dashboard: '/dashboard',
  profile: '/profile',
} as const;
```

## Organisation des tests — Tags et filtrage

```typescript
// Dans playwright.config.ts — filtrer par tag via CLI
// npx playwright test --grep @smoke
// npx playwright test --grep "@critique|@smoke"
// npx playwright test --grep-invert @wip

test('TC-001 — @smoke @critique — Connexion valide', async ({ page }) => {
  // ...
});
```

## Rapport JUnit pour intégration Xray/Jira CI

```bash
# Exécution + rapport
npx playwright test --reporter=junit

# Puis import dans Xray via CLI ou API REST
curl -X POST \
  -H "Authorization: Bearer $XRAY_TOKEN" \
  -F "file=@results/junit.xml" \
  "https://xray.cloud.getxray.app/api/v2/import/execution/junit"
```

## Checklist avant commit

- [ ] Aucun `waitForTimeout()` dans le code
- [ ] Tous les locators utilisent `getByTestId`, `getByRole` ou `getByLabel`
- [ ] Chaque test est indépendant (pas d'état partagé entre tests)
- [ ] Les données de test sont dans `fixtures/`, pas en dur dans les specs
- [ ] `playwright.config.ts` configuré avec `retries: 2` en CI
- [ ] Rapport JUnit activé pour intégration Jira
