const {Given,When,Then,Before,After} = require('@cucumber/cucumber');
const { chromium } = require('playwright');
const assert = require('assert');

let browser;
let page;
let downloadPath;
let openedUrl;

// Website URL
const BASE_URL = 'https://shekharrawal.com.np/';

// Update these selectors after inspecting the actual website
const SELECTORS = {
  resume: 'a:has-text("Download Resume")',
  name: 'input[name="name"]',
  email: 'input[name="email"]',
  subject: 'input[name="subject"]',
  message: 'textarea[name="message"]',
  send: 'button:has-text("Send Message")',
  success: '.success-message',
  social: 'a[href*="linkedin.com"]'
};

// Browser setup
Before(async function () {
  browser = await chromium.launch({headless: false});
  page = await browser.newPage({acceptDownloads: true});});

// Scenario 1: Resume Download

Given('the visitor opens the portfolio', async function () {
  await page.goto('https://shekharrawal.com.np/');
  await page.waitForLoadState('domcontentloaded');
});

When('the visitor clicks the Resume link', async function () {
  const resumeLink = page.locator(
    'a[href="/personal/doc/Shekhar_Rawal_Resume.pdf"]'
  );

  await resumeLink.waitFor({ state: 'visible' });

  // Listen for the new tab before clicking
  const newPagePromise = page.context().waitForEvent('page');

  await resumeLink.click();

  this.resumePage = await newPagePromise;

  await this.resumePage.waitForLoadState('domcontentloaded');
});

Then('the resume PDF should open in a new tab', async function () {
  assert.ok(
    this.resumePage,
    'Resume did not open in a new tab'
  );

  assert.ok(
    this.resumePage.url().includes(
      '/personal/doc/Shekhar_Rawal_Resume.pdf'
    ),
    'Incorrect resume URL'
  );
});

Then('the PDF should load successfully', async function () {
  const response = await this.resumePage.request.get(
    this.resumePage.url()
  );

  assert.strictEqual(
    response.status(),
    200,
    'Resume PDF request failed'
  );

  assert.ok(
    response.headers()['content-type']?.includes('application/pdf'),
    'Response is not a PDF'
  );
});


// Scenario 2: Contact Form

Given('the visitor opens the contact section', async function () {
  await page.goto(BASE_URL);

  // Adjust according to the actual contact section
  await page.locator('text=Contact').first().click();
});

When('the visitor enters valid information', async function () {
  await page.locator(SELECTORS.name).fill('QA Test User');

  await page.locator(SELECTORS.email)
    .fill('qa.test@example.com');

  await page.locator(SELECTORS.subject)
    .fill('Portfolio Testing');

  await page.locator(SELECTORS.message)
    .fill('This is a test message from automated BDD testing.');
});

When('clicks Send Message', async function () {
  await page.locator(SELECTORS.send).click();
});


Then('the message should be submitted', async function () {

  const successMessage = page.locator(
    '[role="status"]'
  );

  await successMessage.waitFor({
    state: 'visible',
    timeout: 10000
  });

  assert.ok(
    await successMessage.isVisible(),
    'Message submission was not confirmed'
  );
});

Then('a success message should appear', async function () {

  const successText = page.getByText(
    'Message sent successfully.',
    { exact: true }
  );

  await successText.waitFor({
    state: 'visible',
    timeout: 10000
  });

  assert.ok(
    await successText.isVisible(),
    'Success message is not visible'
  );
});

// Scenario 3: Social Media Links

Given('the visitor is on the portfolio', async function () {await page.goto(BASE_URL);});

When('the visitor clicks a social media link', async function () {
  const socialLink = page.locator(SELECTORS.social).first();
  await socialLink.waitFor({ state: 'visible' });
  openedUrl = await socialLink.getAttribute('href');
  assert.ok(openedUrl, 'Social media URL is missing');});

Then('the correct social profile should open', async function () {
  assert.ok(openedUrl.includes('linkedin.com'),'Incorrect social media URL');});

// Browser cleanup
After(async function () {if (browser) {await browser.close();}});
