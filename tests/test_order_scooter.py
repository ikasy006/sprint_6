import pytest

from PageObjects.pages.main_page import MainPage
from PageObjects.pages.order_scooter import OrderScooter

def test_order_scooter_for_header_button(main_page):
    main_page.go_to_site()
    order_scooter_page = OrderScooter(main_page.click_to_header_button())

    order_scooter_page.fill_name_field('Рина')
    order_scooter_page.fill_surname_field('Кесс')
    order_scooter_page.fill_address_field('москва')
    order_scooter_page.fill_metro_field('Аннино')
    order_scooter_page.fill_phone_field('+79002223311')
    order_scooter_page.click_next_button()

    order_scooter_page.fill_date_field('23.05.2025')
    order_scooter_page.fill_term_field('сутки')
    order_scooter_page.click_order_button()
    order_scooter_page.click_confirm_button()

    order_scooter_page.check_placed_order()

def test_order_scooter_for_bottom_button(main_page):
    main_page.go_to_site()
    order_scooter_page = OrderScooter(main_page.click_to_bottom_button())

    order_scooter_page.fill_name_field('Алия')
    order_scooter_page.fill_surname_field('Джесс')
    order_scooter_page.fill_address_field('Москва, Варшавское шоссе')
    order_scooter_page.fill_metro_field('Южная')
    order_scooter_page.fill_phone_field('89997776644')
    order_scooter_page.click_next_button()

    order_scooter_page.fill_date_field('30.05.2025')
    order_scooter_page.fill_term_field('двое суток')
    order_scooter_page.click_order_button()
    order_scooter_page.click_confirm_button()

    order_scooter_page.check_placed_order()

def test_reallocation_to_yandex(create_driver):
    order_scooter_page = OrderScooter(create_driver)
    order_scooter_page.open_page()

    order_scooter_page.check_reallocation_yandex()


def test_reallocation_to_main_page(create_driver):
    order_scooter_page = OrderScooter(create_driver)
    order_scooter_page.open_page()

    order_scooter_page.check_reallocation_main_page()