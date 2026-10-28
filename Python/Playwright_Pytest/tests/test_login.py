
from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_login_qademo(page: Page):
    login = LoginPage(page)

    login.login("shekhar9999", "Shekhar@9999")
    login.verify_login()