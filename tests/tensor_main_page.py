from base_page import BasePage

from locators import TensorMainPageLocators

class TensorMainPage(BasePage):
    def get_people_power(self):
        people_power =  self.find_element(TensorMainPageLocators.PEOPLE_POWER)
        return people_power

    def get_more(self):
        more =  self.find_element(TensorMainPageLocators.MORE)
        return more

    def go_to_tensor_about_page(self):
        self.click_on(TensorMainPageLocators.MORE)
