import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url.url import Config

class BasePage:

    def __init__(self, create_driver):
        self.driver = create_driver
        self.base_url = Config.BASE_URL

    @allure.step(title='поиск элемента')
    def find_element(self, locator,time=3):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator))

    @allure.step(title='поиск элементов')
    def find_elements(self, locator,time=3):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator))

    @allure.step(title='переход к элементу')
    def scroll_for_element(self, locator, time=3):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step(title='заполнение поля')
    def fill_input(self, locator, value):
        self.find_element(locator).send_keys(value)

    @allure.step(title='ожидание')
    def wait(self, predicate, time = 3):
        WebDriverWait(self.driver, time).until(predicate)

    @allure.step(title='переключение на новое окно')
    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        self.wait(lambda d: len(d.window_handles) > 1)
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)
        self.wait(lambda d: Config.YANDEX_URL == d.current_url)

    @allure.step(title='открытие главной страницы')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step(title='переход на станицу')
    def go_to_page(self, url):
        return self.driver.get(url)