from page.base_page import BasePage
from base.links import Links
import allure


class PersonalAccount(BasePage):
    BUTTON_HISTORY_ORDER = ('xpath', '//a[text() = "История заказов"]')
    BUTTON_EXIT = ('xpath', '//button[text() = "Выход"]')
    LAST_ORDER = ("css selector", "ul[class*='profileList']>li:last-child>a>div>p[class*='digits']")

    @allure.step('Проверяем, что открылось окно личного кабинета')
    def check_window_personal_account(self):
        actual_url = self.get_url_with_wait(Links.PERSONAL_ACCOUNT_PAGE)
        expected_url = Links.PERSONAL_ACCOUNT_PAGE
        return actual_url == expected_url

    @allure.step('Нажимаем на кнопку "История заказов"')
    def click_button_history_order(self):
        self.click_on_element(self.BUTTON_HISTORY_ORDER)

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_button_exit(self):
        self.click_on_element(self.BUTTON_EXIT)

    @allure.step('Получаем номер последнего заказа')
    def get_number_last_order(self):
        return self.get_text_from_element(self.LAST_ORDER)





