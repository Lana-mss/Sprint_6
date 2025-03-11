import allure
from selenium.webdriver import Keys
from locators.order_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(OrderPageLocators.SCOOTER_LOGO)
        self.switch_to_new_tab()

    @allure.step("Заполнение первой формы заказа: {name}, {surname}, {address}, {phone}")
    def fill_first_form(self, name, surname, address, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.click(OrderPageLocators.METRO_DROPDOWN)
        self.click(OrderPageLocators.METRO_OPTION)
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone + Keys.ENTER)

    @allure.step("Нажатие на кнопку 'Далее'")
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение второй формы заказа: дата {date}, цвет {color}, комментарий {comment}")
    def fill_second_form(self, date, color, comment):
        self.send_keys(OrderPageLocators.DATE_PICKER, date + Keys.ENTER)
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.RENT_OPTION_ONE_DAY)

        if "black" in color:
            self.click(OrderPageLocators.COLOR_CHECKBOX_BLACK)
        if "grey" in color:
            self.click(OrderPageLocators.COLOR_CHECKBOX_GREY)

        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment + Keys.ENTER)

    @allure.step("Нажатие на кнопку 'Заказать'")
    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)
        return self.get_text(OrderPageLocators.SUCCESS_MODAL)
