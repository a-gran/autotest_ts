'''
Third test
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from main_sbis_page import MainSbisPage
from download_sbis_page import DownloadSbisPage
from locators import DownloadSbisPageLocators
from selenium.webdriver.chrome.options import Options
from settings import URL_SBIS
from time import sleep
import os

chrome_options = Options()
prefs = {"download.default_directory": f"{os.getcwd()}\downloads"}
chrome_options.add_experimental_option("prefs", prefs)

def _switch_to_another_handler(browser):
    for window_handle in browser.window_handles:
        browser.switch_to.window(window_handle)
        break

def test_screenplay3(browser):
    browser.get(URL_SBIS)
    main_sbis_page = MainSbisPage(browser)

    local_versions = main_sbis_page.get_local_versions()
    browser.execute_script("arguments[0].scrollIntoView();", local_versions)
    main_sbis_page.go_to_local_versions()

    _switch_to_another_handler(browser)

    download_sbis_page = DownloadSbisPage(browser)
    download_sbis_page.find_plugin()
    download_sbis_page.click_to_plugin()

    _switch_to_another_handler(browser)

    download_sbis_page.find_web_installer()
    download_sbis_page.click_to_web_installer()
