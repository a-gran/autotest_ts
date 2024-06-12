from base_page import BasePage

from locators import ContactsSbisPageLocators

class ContactsSbisPage(BasePage):
    def find_tensor_banner(self):
        tensor_banner = self.find_element(ContactsSbisPageLocators.TENSOR_BANNER)
        return tensor_banner

    def go_to_tensor_main_page(self):
        self.click_on(ContactsSbisPageLocators.TENSOR_BANNER)

    def find_current_region_field(self):
        curent_region_field = self.find_element(ContactsSbisPageLocators.CURENT_REGION_FIELD)
        return curent_region_field

    def get_title_partners_list_current_region(self):
        partners_list_title = self.find_element(ContactsSbisPageLocators.PARTNERS_LIST_TITLE).get_attribute('title')
        return partners_list_title

    def find_partners_list(self):
        partners_list = self.find_element(ContactsSbisPageLocators.PARTNERS_LIST)
        return partners_list

    def find_id(self, partners_list):
        partners_list_id = self.partners_list.find_element(ContactsSbisPageLocators.PARTNERS_LIST)
        return partners_list

    def go_to_modal_window_of_regions(self):
        self.click_on(ContactsSbisPageLocators.CURENT_REGION_FIELD)

    def find_region(self):
        region = self.find_element(ContactsSbisPageLocators.REGION)
        return region

    def get_text_head_title(self):
        head_title = self.find_element(ContactsSbisPageLocators.HEAD_TITLE).get_attribute('outerHTML')
        return head_title

    def go_to_region(self):
        self.click_on(ContactsSbisPageLocators.REGION)
