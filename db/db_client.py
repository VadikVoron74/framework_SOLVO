# Это через заглушки
import allure

class DBClient:

    def __init__(self):
        print("DB mock: подключение к PostgreSQL")

    def get_order_status(self, order_id: str) -> str:
        with allure.step(f"Проверяем статус заказа {order_id} в БД"):
            print(f"DB mock: получаем статус заказа {order_id}")
            return "New"

    def set_order_status(self, order_id: str, status: str):
        with allure.step(f"Устанавливаем статус {status} для заказа {order_id}"):
            print(f"DB mock: статус заказа {order_id} изменён на {status}")

    def close(self):
        print("DB mock: соединение закрыто")

# Это было бы с реальной БД
"""
import psycopg2
import allure
import os


class DBClient:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", 5432),
            database=os.getenv("DB_NAME", "orders_db"),
            user=os.getenv("DB_USER", "test_user"),
            password=os.getenv("DB_PASSWORD", "test_pass")
        )
        self.cursor = self.connection.cursor()

    def get_order_status(self, order_id: str) -> str:
        with allure.step(f"Проверяем статус заказа {order_id} в БД"):
            self.cursor.execute(
                "SELECT status FROM orders WHERE id = %s",
                (order_id,)
            )
            result = self.cursor.fetchone()
            return result[0] if result else None

    def close(self):
        self.cursor.close()
        self.connection.close()
"""
