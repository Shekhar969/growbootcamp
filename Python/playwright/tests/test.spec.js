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

test("Verify the title of the page", async function ({page}){
    await page.goto("https://www.shekharrawal.com.np/")
    const title= await page.title()
    console.log(title)

    await expect(page).toHaveTitle("Siddhanath Multiple Campus (SNSC) | Smart Attendance Management System")
})

