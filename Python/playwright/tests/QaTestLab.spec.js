const { test, expect } = require('@playwright/test');

test('Button Click on QA Test Lab', async ({ page }) => {
    await page.goto('https://qatestlab.com/');

    await page.locator('a.qodef-btn.btn-orange.ml20').click();

    await expect(page).toHaveURL(/request-a-quote/);
});