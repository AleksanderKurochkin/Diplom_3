from page.base_page import BasePage
from locators.locator_personal_account import LocatorPersonalAccount
from base.links import Links
import allure


class PersonalAccount(BasePage):

    @allure.step('Проверяем, что открылось окно личного кабинета')
    def check_window_personal_account(self):
        actual_url = self.get_url_with_wait(Links.PERSONAL_ACCOUNT_PAGE)
        expected_url = Links.PERSONAL_ACCOUNT_PAGE
        return actual_url == expected_url

    @allure.step('Нажимаем на кнопку "История заказов"')
    def click_button_history_order(self):
        self.click_on_element(LocatorPersonalAccount.BUTTON_HISTORY_ORDER)

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_button_exit(self):
        self.click_on_element(LocatorPersonalAccount.BUTTON_EXIT)

    @allure.step('Получаем номер последнего заказа')
    def get_number_last_order(self):
        return self.get_text_from_element(LocatorPersonalAccount.LAST_ORDER)





