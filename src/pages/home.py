from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.title_welcome_user = page.get_by_text("Welcome, Automation")
