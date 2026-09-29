const { test, expect } = require('@playwright/test')

test("My first Test", async function ({ page }) {
    expect(12).toBe(12)
})

test("My Second Test", async function ({page}) {
    expect("shekhar rawal").toContain("she")
})

test("My Third Test", async function ({page}) {
    expect("shekhar rawal".includes("rawal")).toBeTruthy()
})