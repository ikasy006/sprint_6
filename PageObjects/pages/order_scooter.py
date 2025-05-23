import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from url.url import Config

class OrderScooterFormLocators:
    LOCATOR_ORDER_SCOOTER_INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LOCATOR_ORDER_SCOOTER_INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    LOCATOR_ORDER_SCOOTER_INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    LOCATOR_ORDER_SCOOTER_INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    LOCATOR_ORDER_SCOOTER_INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    LOCATOR_ORDER_SCOOTER_NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    LOCATOR_ORDER_SCOOTER_INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    LOCATOR_ORDER_SCOOTER_ARROW = (By.XPATH, "//span[@class='Dropdown-arrow']")
    LOCATOR_ORDER_SCOOTER_BUTTON_CONFIRM = (By.XPATH, "//button[text()='Да']")
    LOCATOR_ORDER_SCOOTER_BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    LOCATOR_ORDER_SCOOTER_PLACED_ORDER = (By.XPATH, "//div[text()='Заказ оформлен']")
    LOCATOR_ORDER_SCOOTER_YANDEX_IMG = (By.XPATH, "//img[@alt='Yandex']")
    LOCATOR_ORDER_SCOOTER_SCOOTER_IMG = (By.XPATH, "//img[@alt='Scooter']")


class OrderScooter(BasePage):
    @allure.step(title='заполнение поля \'Имя\'')
    def fill_name_field(self, name):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_NAME, name)

    @allure.step(title='заполнение поля \'Фамилия\'')
    def fill_surname_field(self, surname):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_SURNAME, surname)

    @allure.step(title='заполнение поля \'Адрес\'')
    def fill_address_field(self, address):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_ADDRESS, address)

    @allure.step(title='заполнение поля \'Станция метро\'')
    def fill_metro_field(self, metro):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_METRO, metro)
        self.find_element((By.XPATH, f"//div[text()='{metro}']")).click()

    @allure.step(title='заполнение поля \'Телефон\'')
    def fill_phone_field(self, phone):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_PHONE, phone)

    @allure.step(title='заполнение поля \'Когда привезти самокат\'')
    def fill_date_field(self, date):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_DATE, date)

    @allure.step(title='заполнение поля \'Срок аренды\'')
    def fill_term_field(self, term):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_ARROW).click()
        self.find_element((By.XPATH, f"//div[text()='{term}']")).click()

    @allure.step(title='нажатие на кнопку \'Далее\'')
    def click_next_button(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_NEXT_BUTTON).click()

    @allure.step(title='нажатие на кнопку \'Заказать\'')
    def click_order_button(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_BUTTON_ORDER).click()

    @allure.step(title='нажатие на кнопку подтверждения')
    def click_confirm_button(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_BUTTON_CONFIRM).click()

    @allure.step(title='проверка появления уведомления об успешном создании заказа')
    def check_placed_order(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_PLACED_ORDER)

    @allure.step(title='открытие страницы оформления заказа')
    def open_page(self):
        self.go_to_page(Config.ORDER_URL)

    @allure.step(title='проверка перемещения на страницу Яндекс Дзен')
    def check_reallocation_yandex(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_YANDEX_IMG).click()
        self.switch_to_new_window()

    @allure.step(title='проверка перемещения на главную страницу')
    def check_reallocation_main_page(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_SCOOTER_IMG).click()
        self.wait(lambda d: Config.BASE_URL == d.current_url)