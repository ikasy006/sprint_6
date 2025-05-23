from PageObjects.pages.main_page import MainPageLocators

class TestData:
    MAIN_PAGE_QUESTIONS_AND_ANSWERS_ID = [
        ['accordion__heading-0', 'accordion__panel-0'],
        ['accordion__heading-1', 'accordion__panel-1'],
        ['accordion__heading-2', 'accordion__panel-2'],
        ['accordion__heading-3', 'accordion__panel-3'],
        ['accordion__heading-4', 'accordion__panel-4'],
        ['accordion__heading-5', 'accordion__panel-5'],
        ['accordion__heading-6', 'accordion__panel-6'],
        ['accordion__heading-7', 'accordion__panel-7']
    ]

    ORDER_SCOOTER_DATA_FOR_ORDER = [
        [MainPageLocators.LOCATOR_ENTRANCE_BUTTON_HEADER, 'Рина', 'Кесс', 'москва', 'Аннино', '+79002223311', '23.05.2025', 'сутки'],
        [MainPageLocators.LOCATOR_ENTRANCE_BUTTON_BOTTOM, 'Алия', 'Джесс', 'Москва, Варшавское шоссе', 'Южная', '89997776644', '30.05.2025', 'двое суток']
    ]