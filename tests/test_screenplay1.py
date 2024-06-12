'''
Basic test
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from config.settings import URL

def _switch_to_another_handler(browser, original_page_handler):
    for window_handle in browser.window_handles:
        if window_handle != original_page_handler:
            browser.switch_to.window(window_handle)
            break

def correct_width_height(image1_width, image2_width, image3_width, image4_width, image1_height, image2_height, image3_height, image4_height):
    if image1_width == image2_width == image3_width == image4_width and image1_height == image2_height == image3_height == image4_height:
        return 'Одинаковая высота и ширина'
    return 'Разные размеры'

def test_banner(browser):
    browser.get(URL)
    original_page_handler = browser.current_window_handle
    contacts = browser.find_element(By.CSS_SELECTOR, 'a[href="/contacts"].sbisru-Header__menu-link')

    assert contacts.text == 'Контакты', 'Unexpected text'

    contacts.click()

    tensor_banner = browser.find_element(By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
    tensor_banner_title = tensor_banner.get_attribute('title')

    assert tensor_banner_title == 'tensor.ru', 'Unexpected title'

    tensor_banner.click()

    _switch_to_another_handler(browser, original_page_handler)

    people_power = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    browser.execute_script("arguments[0].scrollIntoView();", people_power)

    assert people_power.text == 'Сила в людях', 'Unexpected text'

    more = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    browser.execute_script("arguments[0].scrollIntoView();", more)

    assert more.text == 'Подробнее', 'Unexpected link text'

    more.click()

    works = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[1]/h2')
    browser.execute_script("arguments[0].scrollIntoView();", works)

    assert works.text == 'Работаем', 'Unexpected text'

    image1 = works.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img')
    image2 = works.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img')
    image3 = works.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img')
    image4 = works.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img')

    image1_width = image1.get_attribute('width')
    image1_height = image1.get_attribute('height')
    image2_width = image2.get_attribute('width')
    image2_height = image2.get_attribute('height')
    image3_width = image3.get_attribute('width')
    image3_height = image3.get_attribute('height')
    image4_width = image4.get_attribute('width')
    image4_height = image4.get_attribute('height')

    res = correct_width_height(image1_width, image2_width, image3_width, image4_width, image1_height, image2_height, image3_height, image4_height)

    assert res == 'Одинаковая высота и ширина', 'Unexpected image size'
