import allure
from base.BaseTest import BaseTest


class TestPersonalAccount(BaseTest):

    @allure.title('Переход в личный кабинет по клику на кнопку «Личный кабинет»')
    @allure.description('Логинимся и переходим в ЛК')
    def test_open_window_personal_account(self):
        self.login_page.login_user()
        self.designer_page.click_button_personal_account()
        assert self.personal_account.check_window_personal_account()

    @allure.title('Переход в раздел «История заказов»')
    @allure.description('Клик на кнопку "История Заказов" в ЛК')
    def test_open_window_history_order(self):
        self.login_page.login_user()
        self.designer_page.click_button_personal_account()
        self.personal_account.click_button_history_order()
        assert self.history_order.check_window_history_page()

    @allure.title('Выход из аккаунта при нажатии на кнопку "Выход".')
    @allure.description('После нажатия на кнопку "Выход" откроется страница "Вход"')
    def test_click_button_exit(self):
        self.login_page.login_user()
        self.designer_page.click_button_personal_account()
        self.personal_account.click_button_exit()
        assert self.login_page.check_window_login()
