from selenium.webdriver.common.by import By

class MainSbisPageLocators:
    CONTACTS = (By.CSS_SELECTOR, 'a[href="/contacts"].sbisru-Header__menu-link')

class ContactsSbisPageLocators:
    TENSOR_BANNER = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')

class TensorMainPageLocators:
    PEOPLE_POWER = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    MORE = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')

class TensorAboutPageLocators:
    WORKS = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[1]/h2')
    IMAGE1 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img')
    IMAGE2 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img')
    IMAGE3 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img')
    IMAGE4 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img')
