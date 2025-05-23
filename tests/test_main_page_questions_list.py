import allure
import pytest
from test_data.test_data import TestData

@allure.title(test_title="Проверка ответов в блоке Вопросы о важном")
@pytest.mark.parametrize("heading, panel", TestData.MAIN_PAGE_QUESTIONS_AND_ANSWERS_ID)
def test_check_answer_for_question(main_page, heading, panel):
    main_page.go_to_site()
    main_page.scroll_for_question(heading)
    main_page.check_open_answer(heading, panel)