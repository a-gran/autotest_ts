from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator")

    def find_elements(self, locator, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator")

    def click_on(self, locator):
        self.find_element(locator).click()

    def get_title(self):
        return self.driver.title

    def enter_txt(self, locator, txt):
        self.find_element(locator).send_keys(txt)

    def find_download(self, locator, timeout = 15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator), message=f"Can't find elements by locator")
