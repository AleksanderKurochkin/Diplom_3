from page.base_page import BasePage
from locators.locator_login_page import LocatorLoginPage
from base.data import DataTest
from base.links import Links
import allure


class LoginPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_login_page(self):
        self.open_page(Links.LOGIN_PAGE)

    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_button_recover_password(self):
        self.click_on_element(LocatorLoginPage.BUTTON_RECOVER_PASSWORD)

    @allure.step('Проверяем, что открылось окно восстановления пароля')
    def check_window_recover_password(self):
        actual_url = self.get_current_url()
        expected_url = Links.FORGOT_PASSWORD_PAGE
        return self.check_url(actual_url, expected_url)

    @allure.step('Логинимся в личный кабинет')
    def login_user(self):
        self.open_login_page()
        self.enter_text(LocatorLoginPage.FIELD_LOGIN, DataTest.LOGIN)
        self.enter_text(LocatorLoginPage.FIELD_PASSWORD, DataTest.PASSWORD)
        self.click_on_element(LocatorLoginPage.BUTTON_LOGIN)

    @allure.step('Проверяем, что открылось окно "Вход"')
    def check_window_login(self):
        actual_url = self.get_url_with_wait(Links.LOGIN_PAGE)
        expected_url = Links.LOGIN_PAGE
        return actual_url == expected_url









