from src.pages.base_page import BasePage
from playwright.sync_api import Page


class SearchPage(BasePage):
    URL = 'https://www.mercadolibre.com'

    def __init__(self, page: Page):
        super().__init__(page)

    def load(self) -> None:
        self.page.goto(self.URL)

    # def search(self, phrase: str) -> None:
    #     self.page.locator(self.SEARCH_INPUT).fill(phrase).press('Enter')
