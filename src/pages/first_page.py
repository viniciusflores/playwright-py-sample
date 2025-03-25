import os

from playwright.sync_api import Page


class FirstPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("URL")
        self.body = page.locator("body")
        self.input_query = page.locator("textarea[name=q], input[name=q]")
        self.btn_search = page.locator("input[type=submit]")

    def make_a_search(self, query: str):
        self.input_query.fill(query)
        # self.btn_search.click()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(self.page.title())
        print(self.input_query.input_value())
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    def open_app_and_make_a_search(self, query: str):
        self.page.goto(self.url)
        self.make_a_search(query)
