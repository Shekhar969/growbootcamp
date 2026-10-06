import re
from playwright.sync_api import expect,Page

def test_user_login(page:Page):
    page.goto("https://demoqa.com/login")

    page.get_by_placeholder("UserName").fill("shekhar9999")
    page.get_by_placeholder("Password").fill("Shekhar@9999")

    page.locator("#login").click()
    page.wait_for_timeout(3000)

def test_user_login_invalid_username(page:Page):
    page.goto("https://demoqa.com/login")

    page.get_by_placeholder("UserName").fill("shekhar99")
    page.get_by_placeholder("Password").fill("Shekhar@9999")

    page.locator("#login").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#name")).to_contain_text("Invalid username")

def test_user_login_invalid_password(page:Page):
    page.goto("https://demoqa.com/login")

    page.get_by_placeholder("UserName").fill("shekhar9999")
    page.get_by_placeholder("Password").fill("Shekhar9999")

    page.locator("#login").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#name")).to_contain_text("Invalid username or password!")

def test_user_login_empty_fields(page: Page):
    page.goto("https://demoqa.com/login")

    page.get_by_placeholder("UserName").fill("")
    page.get_by_placeholder("Password").fill("")

    page.locator("#login").click()

    expect(page.locator("#userName")).to_have_class(
        re.compile(r"\bis-invalid\b")
    )

    expect(page.locator("#password")).to_have_class(
        re.compile(r"\bis-invalid\b")
    )
