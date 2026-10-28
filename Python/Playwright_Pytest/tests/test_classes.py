import os,json
from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, username, password):
        self.page.goto("https://demoqa.com/login")
        self.page.get_by_placeholder("UserName").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.locator("#login").click()


def test_login_qademo(page: Page):
    LoginPage(page).login("shekhar9999", "Shekhar@9999")

BASE_URL = "https://qa-benefit-store-api.corenroll.com/api/v1/get-cart-amount"
AUTH = "Basic 91e8eafdc842cd36769f7537ee0ebca282375302a075f7b2522619030201c5ce"

def test_api_check_plan_detail(page: Page):
    response = page.request.get(BASE_URL,params={"enrollment_id": "eyJpdiI6IkF5eURFTzVvd0xqSXo3SG5SNWRrNUE9PSIsInZhbHVlIjoiQXhkODJMU3pwVXlYQVIxYWJXNGRSUT09IiwibWFjIjoiMGM2YWFmOGU1NGVlYjJhYWUwZjZjNzc5MzA5MDc1NTNkZGE4MjI1ZDhmMjc2YmFhY2RkYjFkNTMwOTVmYzFmZCJ9"},headers={"Authorization": AUTH})

    print("Plan Detail Status:", response.status)
    expect(response).to_be_ok()




def test_api_add_plan_to_the_cart(page: Page):
    payload = {"enrollment_id": "eyJpdiI6InpiYnR3Z0NsRHoxdjVGUlJCNk5CYUE9PSIsInZhbHVlIjoidlhUSXcxclVKVjBTMXdDQ3drT2RrUT09IiwibWFjIjoiZGY2ZDg4NWUxOWRmMDE0NzY2ZGM3MmRlZjk4NmFmZGNiZjg0N2JkODA2YmY0YzJkMGNkOGNkODYyYzcyYzA0NSJ9",
    "plan_id": "eyJpdiI6Ik9IS0htZnRwQUs4VTRUVSswOXhLbWc9PSIsInZhbHVlIjoicDJ4bXk5ZkVrUzFZYjUyUWdTdi9EZz09IiwibWFjIjoiMDM1MDE2MTRmMGIxMGE0NzMwZWVlOTQ3ODI3YTI2NGRlNGJmNjg1OTc5M2ZjOGY3ZjEzYjk5NGNhZWYwZThiMyJ9",
    "plan_pricing_id": "eyJpdiI6InlZZGhXOXFoNGFwUGVXR1dPU1hBQ2c9PSIsInZhbHVlIjoiVEl2WEY2YlBVVFVHWmJTY0FUUlJUQT09IiwibWFjIjoiNTg5ZjQ5YTE5NTkyNTMzYmRhMmVlNDBjMDMwNWVhNzQ3ZGY2Mzc2N2VhNDExNzczZTk2NDA0ODBiMTA3MzhkMiJ9"}

    response =page.request.post(BASE_URL,headers={"Authorization":AUTH}, 
    data=payload)

    print("Plan added to the cart", response.status)

def test_api_check_cart_total(page: Page):
    response = page.request.get(BASE_URL,params={"enrollment_id": "eyJpdiI6InpiYnR3Z0NsRHoxdjVGUlJCNk5CYUE9PSIsInZhbHVlIjoidlhUSXcxclVKVjBTMXdDQ3drT2RrUT09IiwibWFjIjoiZGY2ZDg4NWUxOWRmMDE0NzY2ZGM3MmRlZjk4NmFmZGNiZjg0N2JkODA2YmY0YzJkMGNkOGNkODYyYzcyYzA0NSJ9"},headers={"Authorization": AUTH})

    print("Cart Total Status:", response.status)
    data = response.json()
    print("Cart Total:", data["data"]["result"])