import pytest
import allure
import re
from playwright.sync_api import Page, expect

@allure.title("New enrollement user")
@allure.description("I have created new user using")
@allure.severity(allure.severity_level.CRITICAL)
def test_new_enrollement(page: Page):
    page.goto("https://qa-enroll.corenroll.com/")

    page.locator("#zip").fill("12345")
    page.locator("#gender").select_option(value="0")
    page.locator("#tier").select_option(value="IO")

    page.get_by_placeholder("mm/dd/yyyy").fill("01/01/1990")

    page.get_by_role("button", name="Submit").click()
    expect(page).not_to_have_url("/plans")


def test_empty_required_fields(page: Page):
    page.goto("https://qa-enroll.corenroll.com/")

    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#zip")).to_have_class(
        re.compile(r"\bis-invalid\b")
    )


@pytest.mark.parametrize("zip_code", [
    "",
    "123",
    "123456",
    "ABCDE",
    "!@#$%",
])
def test_invalid_zip(page: Page, zip_code):
    page.goto("https://qa-enroll.corenroll.com/")

    page.locator("#zip").fill(zip_code)

    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#zip")).to_have_class(
        re.compile(r"\bis-invalid\b")
    )



@pytest.mark.parametrize("dob", [
    "",
    "99/99/9999",
    "01/01/2030",
    "31/02/1990",
    "abc",
])
def test_invalid_dob(page: Page, dob):
    page.goto("https://qa-enroll.corenroll.com/")

    page.get_by_placeholder("mm/dd/yyyy").fill(dob)
    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_placeholder("mm/dd/yyyy")).to_contain_class("is-invalid")


@pytest.mark.parametrize("gender", [
    "",
    "23"
])
def test_invalid_gender(page: Page, gender):
    page.goto("https://qa-enroll.corenroll.com/")

    page.locator("#gender").select_option(gender)

    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#gender")).to_have_class(
        re.compile(r"\bis-invalid\b")
    )

@pytest.mark.parametrize("tier", [
    "IO",  
    "IS",  
    "IC",  
    "IF",  
])
def test_valid_tier(page: Page, tier):
    page.goto("https://qa-enroll.corenroll.com/")

    page.locator("#tier").select_option(tier)

    expect(page.locator("#tier")).not_to_contain_class("is-invalid")
