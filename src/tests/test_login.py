import os

from playwright.sync_api import Page

from src.pages.first_page import FirstPage


def test_login_page(page: Page):
    search_input = os.getenv("SEARCH_INPUT")
    page_title = os.getenv("SEARCH_PAGE_TITLE")
    first = FirstPage(page)
    first.open_app_and_make_a_search(search_input)
    # title = page.title()
    # expect(title).to_be_equal_to(page_title)
    print("## finish ##")
