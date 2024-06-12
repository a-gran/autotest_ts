from base_page import BasePage

from locators import TensorAboutPageLocators

class TensorAboutPage(BasePage):
    def get_works(self):
        works = self.find_element(TensorAboutPageLocators.WORKS)
        return works

    def get_images(self):
        images_list = self.find_elements(TensorAboutPageLocators.IMAGES_LIST)
        return images_list
