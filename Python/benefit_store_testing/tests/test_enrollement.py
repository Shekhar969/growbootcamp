import pytest
import allure
import re
from playwright.sync_api import Page, expect


@allure.feature("Enrollment")
@allure.story("New Enrollment")
@allure.title("Create new enrollment user")
@allure.description("Verify that a user can successfully start a new enrollment by providing valid ZIP code, gender, tier, and date of birth.")
@allure.severity(allure.severity_level.CRITICAL)
def test_new_enrollement(page: Page):
    page.goto("https://qa-enroll.corenroll.com/")

    page.locator("#zip").fill("12345")
    page.locator("#gender").select_option(value="0")
    page.locator("#tier").select_option(value="IO")
    page.get_by_placeholder("mm/dd/yyyy").fill("01/01/1990")

    page.get_by_role("button", name="Submit").click()
    expect(page).not_to_have_url("/plans")


@allure.feature("Enrollment")
@allure.story("Required Field Validation")
@allure.title("Validate required fields")
@allure.description("Verify that required fields are marked as invalid when the Submit button is clicked without entering any information.")
@allure.severity(allure.severity_level.CRITICAL)
def test_empty_required_fields(page: Page):
    page.goto("https://qa-enroll.corenroll.com/")

    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#zip")).to_have_class(
        re.compile(r"\bis-invalid\b")
    )


@allure.feature("Enrollment")
@allure.story("ZIP Code Validation")
@allure.title("Validate invalid ZIP code")
@allure.description("Verify that the ZIP code field is marked as invalid when an empty, incomplete, non-numeric, or special-character ZIP code is submitted.")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("zip_code", [
    "",
    "123",
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


@allure.feature("Enrollment")
@allure.story("Gender Validation")
@allure.title("Validate required gender field")
@allure.description("Verify that the gender field is marked as invalid when no gender option is selected.")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("gender", [
    "",
])
def test_invalid_gender(page: Page, gender):
    page.goto("https://qa-enroll.corenroll.com/")

    page.locator("#gender").select_option(gender)

    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#gender")).to_have_class(
        re.compile(r"\bis-invalid\b")
    )


@allure.feature("Enrollment")
@allure.story("Tier Validation")
@allure.title("Validate valid enrollment tier")
@allure.description("Verify that each supported enrollment tier can be selected successfully without displaying a validation error.")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("tier", ["IO","IS","IC","IF",])
def test_valid_tier(page: Page, tier):
    page.goto("https://qa-enroll.corenroll.com/")

    page.locator("#tier").select_option(tier)

    expect(page.locator("#tier")).not_to_contain_class("is-invalid")
