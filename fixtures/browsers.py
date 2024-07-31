import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def playwright():
    """ playwright """
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="module")
def browser(playwright):
    """ Браузер """
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="module")
def context(browser):
    """ Контекст со своими куками, сессией и данными """
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="module")
def page(context):
    """ Страница """
    page = context.new_page()
    yield page
    page.close()
