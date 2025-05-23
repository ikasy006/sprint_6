import pytest
from PageObjects.pages.main_page import MainPage

test_data = [
    ['accordion__heading-0', 'accordion__panel-0'],
    ['accordion__heading-1', 'accordion__panel-1'],
    ['accordion__heading-2', 'accordion__panel-2'],
    ['accordion__heading-3', 'accordion__panel-3'],
    ['accordion__heading-4', 'accordion__panel-4'],
    ['accordion__heading-5', 'accordion__panel-5'],
    ['accordion__heading-6', 'accordion__panel-6'],
    ['accordion__heading-7', 'accordion__panel-7']
]

@pytest.mark.parametrize("heading, panel", test_data)
def test_check_answer_for_question(main_page, heading, panel):
    main_page.go_to_site()
    main_page.scroll_for_question(heading)
    main_page.check_open_answer(heading, panel)