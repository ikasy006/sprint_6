import pytest

from selenium import webdriver
from PageObjects.pages.main_page import MainPage

@pytest.fixture(scope="session")
def create_driver():
    driver = webdriver.Firefox()

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def main_page(create_driver):
    main = MainPage(create_driver)
    main.go_to_site()
    main.click_cookie_button()
    return main