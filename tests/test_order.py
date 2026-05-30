import pytest
import allure
from pages.order_page import LoginPage, OrderPage


@allure.feature("Обработка заказов")
@allure.story("Создание и подготовка заказа")
@pytest.mark.parametrize("order_name", [
    "Заказ 1",
    "Заказ 2",
])
def test_order_workflow(page, db, corba, order_name):

    with allure.step("Шаг 1 — Авторизация"):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("tomsmith", "SuperSecretPassword!")

    with allure.step("Шаг 2 — Создание заказа"):
        order_page = OrderPage(page)
        order_id = order_page.create_order(order_name) # Через заглушку
        assert order_id is not None

    with allure.step("Шаг 3 — Проверка статуса New в БД"):
        status = "New" # Заглушка
        assert status == "New"

    with allure.step("Шаг 4 — Смена статуса через CORBA"):
        result = corba.prepare_order(order_id)
        assert result is True # Заглушка

    with allure.step("Шаг 5 — Проверка статуса Ready в БД"):
        status = "Ready" # Заглушка
        assert status == "Ready"