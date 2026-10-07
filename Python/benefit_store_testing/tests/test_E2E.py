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

    page.get_by_role("button", name="View More Details").nth(1).click(timeout=20000)

    plan = page.locator(".plan").filter(has_text="MetLife Dental Platinum")
    plan.get_by_role("button", name="Add to Cart").click()

    page.locator("div.order-info a.checkout-btn").click(timeout=30000)

    page.get_by_role("button", name="Continue to Enroll").click(timeout=30000)

    plan = page.locator(".plan").filter(has_text="Personal Information")
    page.locator('[id=":r0:"]').fill("Shekhar")
    page.locator('[id=":r1:"]').fill("Singh")
    page.locator('[id=":r2:"]').fill("Rawal")
    page.locator('[id=":r4:"]').fill("132142521")

    page.get_by_role("button", name="Continue").click(timeout=30000)

    page.locator('input[name="email"]').fill("shekharrawal@gmail.com")
    page.locator('input[name="phoneNumber"]').fill("9742846227")
    page.locator('input[name="address1"]').fill("Bhansi-3")
    page.locator('input[name="zip"]').fill("13214")
    page.locator('input[name="state"]').fill("PA")
    page.locator('input[name="city"]').fill("MNR")

    page.get_by_role("button", name="Continue", exact=True).click(timeout=10000)


    plan = page.locator(".plan").filter(has_text="Add Bank Account")
    page.wait_for_timeout(5000)
    # response = page.request.post(
    #     "https://qa-benefit-store-api.corenroll.com/api/v1/add-plan-to-cart",

    #     headers={
    #         "Authorization": "Basic 91e8eafdc842cd36769f7537ee0ebca282375302a075f7b2522619030201c5ce",
    #         "Content-Type": "application/json"
    #     },

    #     data={
    #         "enrollment_id": "eyJpdiI6InpiYnR3Z0NsRHoxdjVGUlJCNk5CYUE9PSIsInZhbHVlIjoidlhUSXcxclVKVjBTMXdDQ3drT2RrUT09IiwibWFjIjoiZGY2ZDg4NWUxOWRmMDE0NzY2ZGM3MmRlZjk4NmFmZGNiZjg0N2JkODA2YmY0YzJkMGNkOGNkODYyYzcyYzA0NSJ9",

    #         "plan_id": "eyJpdiI6Ik9IS0htZnRwQUs4VTRUVSswOXhLbWc9PSIsInZhbHVlIjoicDJ4bXk5ZkVrUzFZYjUyUWdTdi9EZz09IiwibWFjIjoiMDM1MDE2MTRmMGIxMGE0NzMwZWVlOTQ3ODI3YTI2NGRlNGJmNjg1OTc5M2ZjOGY3ZjEzYjk5NGNhZWYwZThiMyJ9",

    #         "plan_pricing_id": "eyJpdiI6InlZZGhXOXFoNGFwUGVXR1dPU1hBQ2c9PSIsInZhbHVlIjoiVEl2WEY2YlBVVFVHWmJTY0FUUlJUQT09IiwibWFjIjoiNTg5ZjQ5YTE5NTkyNTMzYmRhMmVlNDBjMDMwNWVhNzQ3ZGY2Mzc2N2VhNDExNzczZTk2NDA0ODBiMTA3MzhkMiJ9"
    #     }
    # )

    # # Check API response
    # print("Status:", response.status)
    # print("Response:", response.json())

    # assert response.ok

    # page.get_by_text("Proceed to Enrollment").click()
    # page.get_by_role("button", name="Continue to Enroll").click()

    # page.wait_for_timeout(3999)