import allure
import os

class CORBAClient:

    def __init__(self):
        self.host = os.getenv("CORBA_HOST", "localhost")
        self.port = os.getenv("CORBA_PORT", "9999")
        print(f"CORBA mock: подключение к {self.host}:{self.port}")

    def prepare_order(self, order_id: str):
        with allure.step(f"CORBA: инициируем подготовку заказа {order_id}"):
            print(f"CORBA mock: подготовка заказа {order_id}")
            return True


# Если бы был доступ к CORBA

'''
import CORBA
import pytest

@pytest.fixture(scope="session")
def corba():
    orb = CORBA.ORB_init()
    obj = orb.string_to_object("corbaloc::localhost:9999/OrderService")
    order_service = obj._narrow(OrderService)
    yield order_service
    orb.destroy()
'''