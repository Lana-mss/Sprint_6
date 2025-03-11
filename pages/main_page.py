import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Открытие главной страницы")
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.step("Скролл и клик на вопрос")
    def click_question_by_text(self, question_text):
        locator = MainPageLocators.QUESTION(question_text)
        self.scroll_into_view(locator)
        self.click(locator)

    @allure.step("Возврат текста ответа")
    def get_answer_text(self):
        return self.get_text(MainPageLocators.ANSWER_PANEL)

    @allure.step("Клик по логотипу Яндекса и переключение на другую вкладку")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
        self.switch_to_new_tab()

    @allure.step("Клик по верхней кнопке заказа")
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке заказа")
    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)
