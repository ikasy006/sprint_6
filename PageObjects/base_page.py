from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url.url import Config

class BasePage:

    def __init__(self, create_driver):
        self.driver = create_driver
        self.base_url = Config.BASE_URL

    def find_element(self, locator,time=3):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator,time=3):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator))

    def scroll_for_element(self, locator, time=3):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def fill_input(self, locator, value):
        self.find_element(locator).send_keys(value)

    def go_to_site(self):
        return self.driver.get(self.base_url)