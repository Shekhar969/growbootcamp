import re
import allure
from playwright.sync_api import expect, Page


@allure.title("User login with valid username and password")
@allure.description("Verify that a registered user can successfully log in to the DemoQA application using valid username and password.")
@allure.feature("Login")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_login(page: Page):
    page.goto("https://demoqa.com/login")

    page.get_by_placeholder("UserName").fill("shekhar9999")
    page.get_by_placeholder("Password").fill("Shekhar@9999")

    page.locator("#login").click()
    page.wait_for_timeout(3000)


@allure.title("User login with invalid username and valid password")
@allure.description("Verify that login is rejected when a valid password is provided with an invalid username.")
@allure.feature("Login")
@allure.story("Negative Login Scenarios")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_login_invalid_username(page: Page):
    page.goto("https://demoqa.com/login")

    page.get_by_placeholder("UserName").fill("shekhar99")
    page.get_by_placeholder("Password").fill("Shekhar@9999")

    page.locator("#login").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#name")).to_contain_text("Invalid username")


@allure.title("User login with valid username and invalid password")
@allure.description("Verify that login is rejected when a valid username is provided with an incorrect password.")
@allure.feature("Login")
@allure.story("Negative Login Scenarios")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_login_invalid_password(page: Page):
    page.goto("https://demoqa.com/login")

    page.get_by_placeholder("UserName").fill("shekhar9999")
    page.get_by_placeholder("Password").fill("Shekhar9999")

    page.locator("#login").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#name")).to_contain_text(
        "Invalid username or password!"
    )


@allure.title("User login with empty username and password")
@allure.description("Verify that username and password fields are marked as invalid when the login form is submitted without entering credentials.")
@allure.feature("Login")
@allure.story("Negative Login Scenarios")
@allure.severity(allure.severity_level.NORMAL)
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
