from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from url.url import Config


class MainPageLocators:
    LOCATOR_MAIN_PAGE_LIST = (By.XPATH, "//div[@class='accordion']")
    LOCATOR_ENTRANCE_BUTTON_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    LOCATOR_ENTRANCE_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]")
    LOCATOR_MAIN_PAGE_BUTTON_COOKIE = (By.XPATH, "//button[text()='да все привыкли']")
class MainPage(BasePage):

    def scroll_for_question(self, question):
        self.scroll_for_element((By.XPATH, f"//div[@id='{question}']"))

    def click_cookie_button(self):
        self.find_element(MainPageLocators.LOCATOR_MAIN_PAGE_BUTTON_COOKIE).click()

    def click_on_list_element(self, point_id):
        self.find_element((By.ID, point_id)).click()

    def check_open_answer(self, point_id, answer_id):
        self.click_on_list_element(point_id)
        WebDriverWait(self.driver, 3).until(
            lambda d: d.find_element(By.ID, answer_id).get_attribute('hidden') is None
        )

    def click_to_header_button(self):
        self.scroll_for_element(MainPageLocators.LOCATOR_ENTRANCE_BUTTON_HEADER)
        self.find_element(MainPageLocators.LOCATOR_ENTRANCE_BUTTON_HEADER).click()
        WebDriverWait(self.driver, 3).until(
            lambda d: Config.ORDER_URL == d.current_url
        )
        return self.driver

    def click_to_bottom_button(self):
        self.scroll_for_element(MainPageLocators.LOCATOR_ENTRANCE_BUTTON_BOTTOM)
        self.find_element(MainPageLocators.LOCATOR_ENTRANCE_BUTTON_BOTTOM).click()
        WebDriverWait(self.driver, 3).until(
            lambda d: Config.ORDER_URL == d.current_url
        )
        return self.driver