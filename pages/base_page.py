import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.order_locators import OrderPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Клик по элементу {locator}
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Получение текста элемента {locator}
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    # Ввод текста в поле {locator}
    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Переключение на новую вкладку
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # Скролл к элементу {locator}
    def scroll_into_view(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Закрытие куки-баннера, если он есть")
    def close_cookie_banner(self):
        try:
            if self.wait.until(EC.presence_of_element_located(OrderPageLocators.COOKIE_BANNER)):
                self.click(OrderPageLocators.CLOSE_BUTTON)
        except:
            pass  # Если баннера нет, ничего не делать
