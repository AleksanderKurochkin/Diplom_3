from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator_order_feed_page import LocatorOrderFeedPage
from page.base_page import BasePage
from base.links import Links
import allure


class OrderFeedPage(BasePage):

    @allure.step('Открываем страницу ленты заказов')
    def open_order_feed_page(self):
        self.open_page(Links.ORDER_FEED_PAGE)

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_button_designer(self):
        self.click_on_element(LocatorOrderFeedPage.BUTTON_DESIGNER)

    @allure.step('Проверяем, что открылось окно ленты заказов')
    def check_window_order_feed(self):
        actual_url = self.get_url_with_wait(Links.ORDER_FEED_PAGE)
        expected_url = Links.ORDER_FEED_PAGE
        return actual_url == expected_url

    @allure.step('Нажимаем на кнопку первого заказа')
    def click_button_first_order(self):
        self.click_on_element(LocatorOrderFeedPage.BUTTON_FIRST_ORDER)

    @allure.step('Ожидаем появления всплывающего окна с деталями заказа в котором указан "Состав"')
    def check_window_details_order(self):
        return self.get_text_from_element(LocatorOrderFeedPage.WINDOW_DETAILS_ORDER) == LocatorOrderFeedPage.NAME_WINDOW_DETAILS_ORDER

    @allure.step('Получаем счетчик "Выполнено за все время"')
    def get_counter_all_order(self):
        counter = self.get_text_from_element(LocatorOrderFeedPage.COUNT_ALL_ORDER)
        return counter

    @allure.step('Получаем счетчик "Выполнено за сегодня"')
    def get_counter_today_order(self):
        counter = self.get_text_from_element(LocatorOrderFeedPage.COUNT_TODAY_ORDER)
        return counter

    @allure.step('Получаем номер заказа "В работе"')
    def get_number_order_in_work(self, number_order):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value(LocatorOrderFeedPage.NUMBER_ORDER_IN_WORK, number_order))

    @allure.step('Проверяем номер заказа в "Ленте заказов"')
    def check_number_order_in_feed_order(self, expected_order):
        order_list_items = self.find_elements(LocatorOrderFeedPage.LIST_ORDERS)
        found = False
        for item in order_list_items:
            if item.text == expected_order:
                found = True
                break
        return found


