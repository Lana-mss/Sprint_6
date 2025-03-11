import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA_SETS
import allure


@allure.title("Тест оформления заказа через {order_button} кнопку")
@allure.description("Проверка оформления заказа с разными наборами данных через верхнюю и нижнюю кнопку 'Заказать'.")
@pytest.mark.parametrize("order_button", ["top", "bottom"])
@pytest.mark.parametrize("order_data", ORDER_DATA_SETS)
def test_order_creation(driver, order_button, order_data):
    main_page = MainPage(driver)
    # Кликаем на нужную кнопку "Заказать"
    if order_button == "top":
        main_page.click_order_button_top()
    else:
        main_page.click_order_button_bottom()

    order_page = OrderPage(driver)
    order_page.close_cookie_banner()

    # Заполняем формы заказа
    order_page.fill_first_form(
        order_data["name"], order_data["surname"], order_data["address"], order_data["phone"]
    )
    order_page.click_next_button()

    order_page.fill_second_form(
        order_data["date"], order_data["color"], order_data["comment"]
    )
    order_page.click_order_button()

    # Подтверждаем заказ и проверяем успешное оформление
    success_message = order_page.confirm_order()
    assert "Заказ оформлен" in success_message, "Ошибка: заказ не оформился!"
