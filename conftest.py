import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from db.db_client import DBClient
from corba.corba_client import CORBAClient

load_dotenv()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def db():
    client = DBClient()
    yield client
    client.close()

@pytest.fixture(scope="session")
def corba():
    client = CORBAClient()
    yield client
# Не закрываем, потому что у нас заглушка, ее не надо закрывать
# Если бы было реально подключение, то закрыли бы
