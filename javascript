const { test, expect } = require('@playwright/test');

test('full winning game scenario', async ({ page }) => {
  await page.goto('http://localhost:3000/tris');
  const squares = await page.locator('button');

  // X moves
  await squares.nth(0).click();
  // O moves
  await squares.nth(3).click();
  // X moves
  await squares.nth(1).click();
  // O moves
  await squares.nth(4).click();
  // X moves -> wins
  await squares.nth(2).click();

  await expect(page.locator('text=winner')).toBeVisible();
});