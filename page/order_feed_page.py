from page.base_page import BasePage
from base.links import Links
import allure


class OrderFeedPage(BasePage):
    BUTTON_DESIGNER = ('xpath', '//p[text() = "Конструктор"]')
    BUTTON_FIRST_ORDER = ('xpath', '(//a[@class="OrderHistory_link__1iNby"] | //a[@class="p-6 mb-4 mr-2 order-card_order__3rqYV"])[1]')
    WINDOW_DETAILS_ORDER = ('xpath', '//p[text() = "Cостав"]')
    NAME_WINDOW_DETAILS_ORDER = "Cостав"
    COUNT_ALL_ORDER = ('xpath', '(//p[contains(@class, "OrderFeed_number")] | //p[@class="text text_type_digits-large feed-info_content__3s65D"])[1]')
    COUNT_TODAY_ORDER = ('xpath', '(//p[contains(@class, "OrderFeed_number")] | //p[@class="text text_type_digits-large feed-info_content__3s65D"])[2]')
    NUMBER_ORDER_IN_WORK = ('xpath', '(//ul[contains(@class, "OrderFeed_orderListReady")]//li | (//ul[@class="pt-6  feed-info_list__1JWvG"])[1])')

    @allure.step('Открываем страницу ленты заказов')
    def open_order_feed_page(self):
        self.open_page(Links.ORDER_FEED_PAGE)

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_button_designer(self):
        self.click_on_element(self.BUTTON_DESIGNER)

    @allure.step('Проверяем, что открылось окно ленты заказов')
    def check_window_order_feed(self):
        actual_url = self.get_url_with_wait(Links.ORDER_FEED_PAGE)
        expected_url = Links.ORDER_FEED_PAGE
        return actual_url == expected_url

    @allure.step('Нажимаем на кнопку первого заказа')
    def click_button_first_order(self):
        self.click_on_element(self.BUTTON_FIRST_ORDER)

    @allure.step('Ожидаем появления всплывающего окна с деталями заказа в котором указан "Состав"')
    def check_window_details_order(self):
        return self.get_text_from_element(self.WINDOW_DETAILS_ORDER) == self.NAME_WINDOW_DETAILS_ORDER

    @allure.step('Получаем счетчик "Выполнено за все время"')
    def get_counter_all_order(self):
        counter = self.get_text_from_element(self.COUNT_ALL_ORDER)
        return counter

    @allure.step('Получаем счетчик "Выполнено за сегодня"')
    def get_counter_today_order(self):
        counter = self.get_text_from_element(self.COUNT_TODAY_ORDER)
        return counter

    @allure.step('Получаем номер заказа "В работе"')
    def get_number_order_in_work(self):
        counter = self.get_text_from_element(self.NUMBER_ORDER_IN_WORK)
        return counter




