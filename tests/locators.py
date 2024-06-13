from selenium.webdriver.common.by import By

class MainSbisPageLocators:
    CONTACTS = (By.CSS_SELECTOR, 'a[href="/contacts"].sbisru-Header__menu-link')
    LOCAL_VERSIONS = (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')

class ContactsSbisPageLocators:
    TENSOR_BANNER = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
    CURENT_REGION_FIELD = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    PARTNERS_LIST = (By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
    PARTNERS_LIST_TITLE = (By.CLASS_NAME, 'sbisru-Contacts-List__name')
    REGION = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')
    HEAD_TITLE = (By.XPATH, '/html/head/title')

class DownloadSbisPageLocators:
    PLUGIN = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]')
    WEB_INSTALLER = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')

class TensorMainPageLocators:
    PEOPLE_POWER = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    MORE = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')

class TensorAboutPageLocators:
    WORKS = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[1]/h2')
    IMAGES_LIST = (By.CLASS_NAME, 'tensor_ru-About__block3-image new_lazy loaded')
