import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls


@allure.title("Проверка, что клик по логотипу Самоката ведет на главную страницу")
def test_scooter_logo_redirects_to_main_page(driver):
    order_page = OrderPage(driver)
    order_page.open_url(Urls.ORDER_URL)
    order_page.click_scooter_logo()
    assert driver.current_url == Urls.BASE_URL, "Логотип Самоката не ведет на главную!"


@allure.title("Проверка, что клик по логотипу Яндекса открывает главную страницу Дзена в новой вкладке")
def test_yandex_logo_opens_new_tab(driver):
    page = MainPage(driver)
    page.click_yandex_logo()
    assert driver.current_url.startswith(Urls.DZEN_URL), "Логотип Яндекса не ведет на главную страницу Дзена!"
