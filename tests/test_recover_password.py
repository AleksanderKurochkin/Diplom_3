import allure
from base.BaseTest import BaseTest


class TestRecoverPassword(BaseTest):

    @allure.title('Переход на страницу восстановления пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_window_recover_password(self):
        self.login_page.open_login_page()
        self.login_page.click_button_recover_password()
        assert self.login_page.check_window_recover_password()

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить»')
    def test_enter_email_and_click_button_recover(self):
        self.forgot_password_page.open_forgot_password_page()
        self.forgot_password_page.enter_email()
        self.forgot_password_page.click_button_recover()
        assert self.login_page.check_window_recover_password()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Переход на страницу изменения пароля по кнопке «Восстановить»')
    def test_click_button_show_password(self):
        self.forgot_password_page.open_forgot_password_page()
        self.forgot_password_page.enter_email()
        self.forgot_password_page.click_button_recover()
        self.reset_password_page.click_button_show_password()
        assert self.reset_password_page.check_field_active()



