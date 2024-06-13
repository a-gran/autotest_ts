from base_page import BasePage

from locators import MainSbisPageLocators

class MainSbisPage(BasePage):
    def find_contacts_sbis_page(self):
        contacts = self.find_element(MainSbisPageLocators.CONTACTS)
        return contacts

    def go_to_contacts_sbis_page(self):
        self.click_on(MainSbisPageLocators.CONTACTS)

    def get_local_versions(self):
        local_versions =  self.find_element(MainSbisPageLocators.LOCAL_VERSIONS)
        return local_versions

    def go_to_local_versions(self):
        self.click_on(MainSbisPageLocators.LOCAL_VERSIONS)
