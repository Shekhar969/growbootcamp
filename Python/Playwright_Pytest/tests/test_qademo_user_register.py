import pytest
from playwright.sync_api import Page, expect


def test_new_user_register(page: Page):
    page.goto("https://demoqa.com/login")

    page.get_by_role("button", name="New User").click()
    page.reload()
    page.get_by_role("textbox", name="First Name").fill("test1")
    page.get_by_role("textbox", name="Last Name").fill("test1")
    page.get_by_role("textbox", name="UserName").fill("shekhar9999")
    page.get_by_role("textbox", name="Password").fill("Shekhar@9999")
    page.get_by_role("button", name="Register").click()



def test__user_register(page: Page):
    page.goto("https://demoqa.com/login")

    page.get_by_role("button", name="New User").click()
    page.reload()
    page.wait_for_timeout(3000)
    page.get_by_role("textbox", name="First Name").fill("test1")
    page.get_by_role("textbox", name="Last Name").fill("test1")
    page.get_by_role("textbox", name="UserName").fill("shekhar9999")
    page.get_by_role("textbox", name="Password").fill("Shekhar@9999")
    page.get_by_role("button", name="Register").click()

    expect(page.locator("#name")).to_contain_text("User exists")

def test_register_invalid_password(page: Page):
    page.goto("https://demoqa.com/login")
    page.get_by_role("button", name="New User").click()
    page.reload()
    page.wait_for_timeout(3000)
    page.get_by_role("textbox", name="First Name").fill("test")
    page.get_by_role("textbox", name="Last Name").fill("user")
    page.get_by_role("textbox", name="UserName").fill("uniqueuser123")
    page.get_by_role("textbox", name="Password").fill("test")

    page.get_by_role("button", name="Register").click()

    expect(page.locator("#name")).to_contain_text(
        "Passwords must have"
    )





