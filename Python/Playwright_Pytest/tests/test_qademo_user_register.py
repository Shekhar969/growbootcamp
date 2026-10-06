import allure
from playwright.sync_api import Page, expect


@allure.title("Register new user with valid credentials")
@allure.description("Verify that a new user can register successfully using a valid first name, last name, unique username, and valid password.")
@allure.feature("Registration")
@allure.story("Valid User Registration")
@allure.severity(allure.severity_level.CRITICAL)
def test_new_user_register(page: Page):
    page.goto("https://demoqa.com/login")

    page.get_by_role("button", name="New User").click()
    page.reload()
    page.wait_for_timeout(3000)
    page.get_by_role("textbox", name="First Name").fill("test1")
    page.get_by_role("textbox", name="Last Name").fill("test1")
    page.get_by_role("textbox", name="UserName").fill("shekhar9999")
    page.get_by_role("textbox", name="Password").fill("Shekhar@9999")

    page.get_by_role("button", name="Register").click()


@allure.title("Register user with an existing username")
@allure.description("Verify that registration is rejected when a user attempts to register with a username that already exists in the application.")
@allure.feature("Registration")
@allure.story("Negative Registration Scenarios")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_register_existing_username(page: Page):
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


@allure.title("Register user with invalid password")
@allure.description("Verify that registration is rejected when the password does not satisfy the application's password requirements.")
@allure.feature("Registration")
@allure.story("Negative Registration Scenarios")
@allure.severity(allure.severity_level.NORMAL)
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

    expect(page.locator("#name")).to_contain_text("Passwords must have")
