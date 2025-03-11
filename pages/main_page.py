import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):

    @allure.step("Скролл и клик на вопрос")
    def click_question_by_text(self, question_text):
        locator = MainPageLocators.QUESTION(question_text)
        self.scroll_into_view(locator)
        self.click(locator)

    @allure.step("Возврат текста ответа")
    def get_answer_text(self):
        return self.get_text(MainPageLocators.ANSWER_PANEL)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
        self.switch_to_new_tab()
        self.wait.until(lambda d: d.current_url.startswith(Urls.DZEN_URL))

    @allure.step("Клик по верхней кнопке заказа")
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке заказа")
    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)
