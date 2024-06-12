from tests.pages.base_page import BasePage
from config.settings import URL

from tests.utils.locators import MainSbisPageLocators

class MainSbisPage(BasePage):
    def __init__(self, driver, url=URL):
        super(MainSbisPage, self).__init__(driver, url)

    def go_to_contacts_sbis_page(self):
        self.click_on(MainSbisPageLocators.CONTACTS)
