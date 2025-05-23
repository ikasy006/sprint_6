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
    def fill_name_field(self, name):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_NAME, name)

    def fill_surname_field(self, surname):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_SURNAME, surname)

    def fill_address_field(self, address):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_ADDRESS, address)

    def fill_metro_field(self, metro):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_METRO, metro)
        self.find_element((By.XPATH, f"//div[text()='{metro}']")).click()

    def fill_phone_field(self, phone):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_PHONE, phone)

    def fill_date_field(self, date):
        self.fill_input(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_INPUT_DATE, date)

    def fill_term_field(self, term):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_ARROW).click()
        self.find_element((By.XPATH, f"//div[text()='{term}']")).click()

    def click_next_button(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_NEXT_BUTTON).click()

    def click_order_button(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_BUTTON_ORDER).click()

    def click_confirm_button(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_BUTTON_CONFIRM).click()

    def check_placed_order(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_PLACED_ORDER)

    def open_page(self):
        self.driver.get(Config.ORDER_URL)

    def check_reallocation_yandex(self):
        original_window = self.driver.current_window_handle
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_YANDEX_IMG).click()
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(
            lambda d: Config.YANDEX_URL == d.current_url
        )

    def check_reallocation_main_page(self):
        self.find_element(OrderScooterFormLocators.LOCATOR_ORDER_SCOOTER_SCOOTER_IMG).click()
        WebDriverWait(self.driver, 10).until(
            lambda d: Config.BASE_URL == d.current_url
        )