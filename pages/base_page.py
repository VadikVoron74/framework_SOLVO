from playwright.sync_api import Page
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        with allure.step(f"Открываем страницу {url}"):
            self.page.goto(url)

    def take_screenshot(self, name: str):
        allure.attach(
            self.page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )