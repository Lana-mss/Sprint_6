import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@allure.title("Проверка, что при клике на вопрос появляется правильный ответ")
@pytest.mark.parametrize("question_text", MainPageLocators.EXPECTED_ANSWERS.keys())
def test_questions(driver, question_text):
    page = MainPage(driver)
    page.click_question_by_text(question_text)
    actual_answer = page.get_answer_text()
    expected_answer = MainPageLocators.EXPECTED_ANSWERS[question_text]
    assert actual_answer.strip() == expected_answer.strip(), (
        f"Ожидали: {expected_answer}\n"
        f"Получили: {actual_answer}"
    )
