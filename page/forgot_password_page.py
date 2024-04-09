from selenium.webdriver.support import expected_conditions as EC
from base.data import DataTest
from locators.locator_forgot_password_page import LocatorForgotPasswordPage
from page.base_page import BasePage
from base.links import Links
import allure


class ForgotPasswordPage(BasePage):

    @allure.step('Открываем страницу восстановления пароля')
    def open_forgot_password_page(self):
        self.open_page(Links.FORGOT_PASSWORD_PAGE)

    @allure.step('Вводим email')
    def enter_email(self):
        element = self.wait.until(EC.element_to_be_clickable(LocatorForgotPasswordPage.FIELD_EMAIL))
        element.send_keys(DataTest.EMAIL)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_button_recover(self):
        self.click_on_element(LocatorForgotPasswordPage.BUTTON_RESTORE)

    @allure.step('Проверяем, что открылось окно восстановление пароля')
    def check_window_recover_password(self):
        actual_url = self.get_current_url()
        expected_url = Links.RESET_PASSWORD_PAGE
        return self.check_url(actual_url, expected_url)
