import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.title("Проверка, что клик по логотипу Самоката ведет на главную страницу")
def test_scooter_logo_redirects_to_main_page(driver):
    order_page = OrderPage(driver)
    order_page.open()
    order_page.click_scooter_logo()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Логотип Самоката не ведет на главную!"


@allure.title("Проверка, что клик по логотипу Яндекса открывает главную страницу Дзена в новой вкладке")
def test_yandex_logo_opens_new_tab(driver):
    page = MainPage(driver)
    page.click_yandex_logo()
    WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
    assert "dzen.ru" in driver.current_url, "Логотип Яндекса не ведет на главную страницу Дзена!"
