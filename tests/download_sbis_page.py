from base_page import BasePage

from locators import DownloadSbisPageLocators

class DownloadSbisPage(BasePage):
    def find_plugin_(self):
        plugin = self.find_element(DownloadSbisPageLocators.PLUGIN)
        return plugin

    def find_web_installer(self):
        web_installer = self.find_element(DownloadSbisPageLocators.WEB_INSTALLER)
        return web_installer

    def click_to_plugin(self):
        self.click_on(DownloadSbisPageLocators.PLUGIN)

    def click_to_web_installer(self):
        self.click_on(DownloadSbisPageLocators.WEB_INSTALLER)
