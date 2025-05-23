import allure
import pytest

from PageObjects.pages.order_scooter import OrderScooter
from test_data.test_data import TestData

class TestOrderScooter:
    @allure.title(test_title="Проверка оформления заказа")
    @pytest.mark.parametrize("locator, name, surname, address, metro, phone, date, term", TestData.ORDER_SCOOTER_DATA_FOR_ORDER)
    def test_order_scooter(self, main_page, locator, name, surname, address, metro, phone, date, term):
        main_page.go_to_site()
        order_scooter_page = OrderScooter(main_page.click_on_button(locator))

        order_scooter_page.fill_name_field(name)
        order_scooter_page.fill_surname_field(surname)
        order_scooter_page.fill_address_field(address)
        order_scooter_page.fill_metro_field(metro)
        order_scooter_page.fill_phone_field(phone)
        order_scooter_page.click_next_button()

        order_scooter_page.fill_date_field(date)
        order_scooter_page.fill_term_field(term)
        order_scooter_page.click_order_button()
        order_scooter_page.click_confirm_button()

        order_scooter_page.check_placed_order()

class TestReallocationFromOrder:
    @allure.title(test_title="Проверка перемещения на станицу Яндекс Дзен")
    def test_reallocation_to_yandex(self, create_driver):
        order_scooter_page = OrderScooter(create_driver)
        order_scooter_page.open_page()

        order_scooter_page.check_reallocation_yandex()

    @allure.title(test_title="Проверка перемещения на главную страницу")
    def test_reallocation_to_main_page(self, create_driver):
        order_scooter_page = OrderScooter(create_driver)
        order_scooter_page.open_page()

        order_scooter_page.check_reallocation_main_page()