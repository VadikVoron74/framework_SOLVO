# Order Processing Test Framework

Прототип мини-фреймворка для тестирования системы обработки заказов.

## Стек

- Python 3.10+
- Pytest
- Playwright
- Allure
- PostgreSQL (psycopg2)
- CORBA (заглушка)
- GitHub Actions

## Структура проекта
```
framework_SOLVO/
├── .github/
│   └── workflows/
│       └── tests.yml      # CI/CD пайплайн
├── corba/
│   └── corba_client.py    # CORBA клиент (заглушка)
├── db/
│   └── db_client.py       # PostgreSQL клиент (заглушка)
├── pages/
│   ├── base_page.py       # Базовый класс POM
│   └── order_page.py      # Страницы авторизации и заказов
├── tests/
│   └── test_order.py      # Тесты
├── .env.example           # Шаблон переменных окружения
├── conftest.py            # Фикстуры pytest
└── requirements.txt       # Зависимости
```
## Установка

```bash
# Клонировать репозиторий
git clone https://github.com/your-username/framework_SOLVO.git
cd framework_SOLVO

# Установить зависимости
pip install -r requirements.txt

# Установить браузер
playwright install chromium

# Создать .env файл
cp .env.example .env
```

## Настройка

Заполните `.env` файл своими данными:
```
BASE_URL=https://your-system-url.com
DB_HOST=your-db-host
DB_PORT=5432
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
CORBA_HOST=your-corba-host
CORBA_PORT=9999
```
## Запуск тестов

```bash
# Запустить все тесты(уже с отчетом Allure и -v, т.к. добавил в pytest.ini)
pytest tests/

```

## CORBA

Поскольку реального стенда нет — используется заглушка.

В реальном проекте использовалась бы библиотека `omniORB`.

Пример фикстуры для подключения к реальному ORB есть в corba/corba_client.py


## Архитектура

Фреймворк разделён на слои:

- **UI слой** — pages/ — Page Object Model
- **DB слой** — db/ — работа с PostgreSQL
- **CORBA слой** — corba/ — взаимодействие с CORBA сервисом
- **Тесты** — tests/ — бизнес-сценарии

## CI/CD

Тесты запускаются автоматически через GitHub Actions:
- При push в ветку main
- При создании Pull Request в main