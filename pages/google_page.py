import pytest
from playwright.sync_api import Page
from pages.BaseActions import BaseActionsOnPage

FIELD_SERACH = '//*[@id="APjFqb"]'
TEXT_RESULTS = '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3'



class GooglePage(BaseActionsOnPage):

    def search_on_page(self, text: str):
        self.set_text(FIELD_SERACH, text)
        self.push_enter(FIELD_SERACH)


    def check_results(self, text: str):
        self.expect_text(TEXT_RESULTS, text)
