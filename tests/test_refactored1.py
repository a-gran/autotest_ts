'''
First test
'''
from selenium.webdriver.common.by import By
from main_sbis_page import MainSbisPage
from contacts_sbis_page import ContactsSbisPage
from tensor_main_page import TensorMainPage
from tensor_about_page import TensorAboutPage
from settings import URL_SBIS

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

def test_screenplay1(browser):
    browser.get(URL_SBIS)
    main_sbis_page = MainSbisPage(browser)

    original_page_handler = browser.current_window_handle
    contacts = main_sbis_page.find_contacts_sbis_page()

    assert contacts.text == 'Контакты', 'Unexpected text'

    main_sbis_page.go_to_contacts_sbis_page()

    contacts_sbis_page = ContactsSbisPage(browser)
    tensor_banner = contacts_sbis_page.find_tensor_banner()
    tensor_banner_title = tensor_banner.get_attribute('title')

    assert tensor_banner_title == 'tensor.ru', 'Unexpected title'

    contacts_sbis_page.go_to_tensor_main_page()

    _switch_to_another_handler(browser, original_page_handler)

    tensor_main_page = TensorMainPage(browser)
    people_power = tensor_main_page.get_people_power()
    browser.execute_script("arguments[0].scrollIntoView();", people_power)

    assert people_power.text == 'Сила в людях', 'Unexpected text'

    more = tensor_main_page.get_more()
    browser.execute_script("arguments[0].scrollIntoView();", more)

    assert more.text == 'Подробнее', 'Unexpected link text'

    tensor_main_page.go_to_tensor_about_page()

    tensor_about_page = TensorAboutPage(browser)
    works = tensor_about_page.get_works()
    browser.execute_script("arguments[0].scrollIntoView();", works)

    assert works.text == 'Работаем', 'Unexpected text'

    images_list = browser.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image new_lazy loaded')

    res = _is_correct_width_height(images_list)

    assert res == 'Одинаковая высота и ширина', 'Разные размеры'
