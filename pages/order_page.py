from pages.base_page import BasePage
from playwright.sync_api import Page
import allure
import os

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")

    def open(self):
        base_url = os.getenv("BASE_URL")
        with allure.step("Открываем страницу авторизации"):
            self.navigate(f"{base_url}/login")

    def login(self, username: str, password: str):
        with allure.step(f"Авторизуемся как {username}"):
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.login_button.click()

class OrderPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def create_order(self, order_name: str) -> str:
        with allure.step(f"Создаём заказ {order_name}"):
            return "Заказ-0001"