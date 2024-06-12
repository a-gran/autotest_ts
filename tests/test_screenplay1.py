'''
Basic test
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#from config.settings import URL
URL = "https://sbis.ru/"

def _switch_to_another_handler(browser, original_page_handler):
    for window_handle in browser.window_handles:
        if window_handle != original_page_handler:
            browser.switch_to.window(window_handle)
            break

def _is_correct_width_height(images_list):
    widths = 0
    heights = 0
    for image in images_list:
        image_width = image.get_attribute('width')
        if image_width[image + 1] == image_width[image]:
            widths += 1
            image_width[image + 1] = image_width[image]
        image_height = image.get_attribute('height')
        if image_height[image + 1] == image_height[image]:
            heights += 1
            image_height[image + 1] = image_height[image]
    if widths == len(images_list) and heights == len(images_list):
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

    images_list = browser.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image new_lazy loaded')

    res = _is_correct_width_height(images_list)

    assert res == 'Одинаковая высота и ширина', 'Разные размеры'
