from page.base_page import BasePage
from base.links import Links
import allure


class LoginPage(BasePage):
    BUTTON_RECOVER_PASSWORD = ("xpath", "//main//div//a[text()='Восстановить пароль']")
    FIELD_LOGIN = ("xpath", '//input[@name="name"]')
    FIELD_PASSWORD = ("xpath", '//input[@name="Пароль"]')
    BUTTON_LOGIN = ("xpath", "//button[text()='Войти']")

    LOGIN = "ivan_0052@test.ru"
    PASSWORD = "qwerrty1234"

    @allure.step('Открываем главную страницу')
    def open_login_page(self):
        self.open_page(Links.LOGIN_PAGE)

    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_button_recover_password(self):
        self.click_on_element(self.BUTTON_RECOVER_PASSWORD)

    @allure.step('Проверяем, что открылось окно восстановления пароля')
    def check_window_recover_password(self):
        actual_url = self.get_current_url()
        expected_url = Links.FORGOT_PASSWORD_PAGE
        return self.check_url(actual_url, expected_url)

    @allure.step('Логинимся в личный кабинет')
    def login_user(self):
        self.open_login_page()
        self.enter_text(self.FIELD_LOGIN, self.LOGIN)
        self.enter_text(self.FIELD_PASSWORD, self.PASSWORD)
        self.click_on_element(self.BUTTON_LOGIN)

    @allure.step('Проверяем, что открылось окно "Вход"')
    def check_window_login(self):
        actual_url = self.get_url_with_wait(Links.LOGIN_PAGE)
        expected_url = Links.LOGIN_PAGE
        return actual_url == expected_url









