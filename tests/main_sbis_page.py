from base_page import BasePage
from settings import URL_SBIS

from locators import MainSbisPageLocators

class MainSbisPage(BasePage):
    def find_contacts_sbis_page(self):
        contacts = self.find_element(MainSbisPageLocators.CONTACTS)
        return contacts

    def go_to_contacts_sbis_page(self):
        self.click_on(MainSbisPageLocators.CONTACTS)
