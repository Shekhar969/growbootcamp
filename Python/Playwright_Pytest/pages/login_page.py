from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://demoqa.com/login"

    def __init__(self, page: Page):
        self.page = page

    def login(self, username, password):
        self.page.goto(self.URL)
        self.page.get_by_placeholder("UserName").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.locator("#login").click()

    def verify_login(self):
        expect(self.page).to_have_url("https://demoqa.com/profile")
