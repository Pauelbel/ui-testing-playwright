import pytest
from playwright.sync_api import sync_playwright
from pages.BaseActions import BaseActionsOnPage
from config import CONFIG_DATA


@pytest.fixture(autouse=True)
def go_to_base_page(page, playwright, browser, context):

    """
    Фикстура для открытия главной страницы сайта
    """

    go_to_base_page = BaseActionsOnPage(page)
    go_to_base_page.go_to_url(CONFIG_DATA["url"])
    yield go_to_base_page
