from playwright.sync_api import Page, expect


class BaseActionsOnPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_url(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

    def wait_for_selector(self, selector: str):
        self.page.wait_for_selector(selector)

    def click(self, selector: str):
        self.page.click(selector)

    def set_text(self, selector: str, text: str):
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)


    def push_enter(self, selector: str):
        self.page.locator(selector).press("Enter")
        
    def expect_text(self, selector: str, expected_text: str):
        expect(self.page.locator(selector)).to_have_text(expected_text)
