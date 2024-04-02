from page.base_page import BasePage
from base.links import Links
import allure


class HistoryOrderPage(BasePage):

    @allure.step('Проверяем, что открылось окно истории заказа')
    def check_window_history_page(self):
        actual_url = self.get_url_with_wait(Links.HISTORY_ORDER_PAGE)
        expected_url = Links.HISTORY_ORDER_PAGE
        return actual_url == expected_url
