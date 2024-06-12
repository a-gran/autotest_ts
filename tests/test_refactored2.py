'''
Basic test
'''
from selenium.webdriver.common.by import By
from main_sbis_page import MainSbisPage
from contacts_sbis_page import ContactsSbisPage
from settings import URL_SBIS
from time import sleep

def _switch_to_another_handler(browser):
    for window_handle in browser.window_handles:
        browser.switch_to.window(window_handle)
        break

def get_url(browser):
    curl = browser.current_url
    return curl

def _is_kamchatskiy_kraj(curl):
    if 'kamch' in curl:
        return True
    return False

def _is_head_title(head_title_text):
    head_title_text = head_title_text.lower()
    if 'камчатск' in head_title_text:
        return True
    return False

def test_screenplay2(browser):
    browser.get(URL_SBIS)
    main_sbis_page = MainSbisPage(browser)

    contacts = main_sbis_page.find_contacts_sbis_page()

    assert contacts.text == 'Контакты', 'Unexpected text'

    main_sbis_page.go_to_contacts_sbis_page()

    contacts_sbis_page = ContactsSbisPage(browser)
    curent_region_field = contacts_sbis_page.find_current_region_field()
    curent_region_field_text = curent_region_field.text
    partners_list_title_1 = contacts_sbis_page.get_title_partners_list_current_region()

    assert curent_region_field_text == 'Краснодарский край', 'Unexpected title'

    _switch_to_another_handler(browser)

    partners_list = contacts_sbis_page.find_partners_list()

    assert partners_list.is_displayed() == True, 'Unexpected text'

    contacts_sbis_page.go_to_modal_window_of_regions()

    _switch_to_another_handler(browser)

    region = contacts_sbis_page.find_region()
    region_text = region.text

    assert region_text == '41 Камчатский край', 'Unexpected title'

    contacts_sbis_page.go_to_region()

    _switch_to_another_handler(browser)

    new_curent_region = contacts_sbis_page.find_current_region_field()
    new_curent_region.click()
    new_curent_region_field = new_curent_region
    new_curent_region_field_text = new_curent_region_field.text
    partners_list_title_2 = contacts_sbis_page.get_title_partners_list_current_region()

    assert new_curent_region_field_text == 'Камчатский край', 'Unexpected title'

    assert partners_list_title_1 != partners_list_title_2, 'Unexpected title'

    curl = get_url(browser)

    res = _is_kamchatskiy_kraj(curl)

    assert res == True, 'Unexpected title'

    head_title = contacts_sbis_page.get_text_head_title()
    print(head_title)

    res = _is_head_title(head_title)
    print(res)

    assert res == True, 'Unexpected title'
