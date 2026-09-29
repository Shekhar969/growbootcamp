const {test,expect}= require('@playwright/test')

test("BOID Input at cdsc", async function ({page}){
    await page.goto("https://iporesult.cdsc.com.np/")

    await page.locator("//input[@id='boid']").type("122333132123")
})