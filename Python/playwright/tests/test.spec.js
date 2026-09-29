const { test, expect } = require('@playwright/test')

test.skip("My first Test", async function ({ page }) {
    expect(12).toBe(12)
})

test.skip("My Second Test", async function ({page}) {
    expect("shekhar rawal").toContain("she")
})

test.skip("My Third Test", async function ({page}) {
    expect("shekhar rawal".includes("rawal")).toBeTruthy()
})

test.skip("Verify the title of the page", async function ({page}){
    await page.goto("https://www.shekharrawal.com.np/")
    const title= await page.title()
    console.log(title)

    await expect(page).toHaveTitle("Siddhanath Multiple Campus (SNSC) | Smart Attendance Management System")
})

