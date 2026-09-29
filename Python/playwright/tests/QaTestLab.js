const { test, expect } = require('@playwright/test')

test("Attendance Button Check", async function ({ page }) {
   await page.goto("https://iporesult.cdsc.com.np/")

   await page.getByPlaceholder("16-digit BOID").type("12231232313")
   console.log("test done successfully")
})