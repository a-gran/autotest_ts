from selenium import webdriver
from time import sleep

def test_browser(browser):
    '''
    Test browser
    '''
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://www.google.com/")
    sleep(2)
    browser.quit()
