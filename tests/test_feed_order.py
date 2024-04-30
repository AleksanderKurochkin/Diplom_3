import allure
from base.BaseTest import BaseTest


class TestMainFunction(BaseTest):

    @allure.title('Проверка открытия всплывающего окна с деталями')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями"')
    def test_open_window_details_order(self):
        self.order_feed_page.open_order_feed_page()
        self.order_feed_page.click_button_first_order()
        assert self.order_feed_page.check_window_details_order()

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается на 1')
    @allure.description('Проверяем счетчик до и после выполнения заказа, ожидаем что он увеличивается на 1')
    def test_count_all_order(self):
        self.login_page.login_user()
        self.designer_page.click_button_order_feed()
        initial_counter = self.order_feed_page.get_counter_all_order()
        self.order_feed_page.click_button_designer()
        self.designer_page.add_ingredient_bread()
        self.designer_page.click_button_create_order()
        self.order_feed_page.open_order_feed_page()
        current_counter = self.order_feed_page.get_counter_all_order()
        assert current_counter == f"{int(initial_counter) + 1}"

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается на 1')
    @allure.description('Проверяем счетчик до и после выполнения заказа, ожидаем что он увеличивается на 1')
    def test_count_today_order(self):
        self.login_page.login_user()
        self.designer_page.click_button_order_feed()
        initial_counter = self.order_feed_page.get_counter_today_order()
        self.order_feed_page.click_button_designer()
        self.designer_page.add_ingredient_bread()
        self.designer_page.click_button_create_order()
        self.order_feed_page.open_order_feed_page()
        current_counter = self.order_feed_page.get_counter_today_order()
        assert current_counter == f"{int(initial_counter) + 1}"

    @allure.title('После оформления заказа его номер появляется в разделе В работе.')
    @allure.description('Проверяем раздел "В работе" сразу после создания заказа')
    def test_order_in_work(self):
        self.login_page.login_user()
        self.order_feed_page.click_button_designer()
        self.designer_page.add_ingredient_bread()
        self.designer_page.click_button_create_order()
        number_order = self.designer_page.get_number_order()
        self.order_feed_page.open_order_feed_page()
        number_order_in_work = self.order_feed_page.get_number_order_in_work(number_order)
        assert number_order_in_work

    @allure.title('Проверяем что заказ пользователя из "Истории заказов" отображается на странице "Лента заказов".')
    @allure.description('Делаем заказ, берем из истории номер последнего заказа и проверяем его на странице "Лента '
                        'заказов"')
    def test_order_in_work(self):
        self.login_page.login_user()
        self.order_feed_page.click_button_designer()
        self.designer_page.add_ingredient_bread()
        self.designer_page.click_button_create_order()
        self.designer_page.click_button_exit_window_details()
        self.designer_page.click_button_personal_account()
        self.personal_account.click_button_history_order()
        order = self.personal_account.get_number_last_order()
        self.order_feed_page.open_order_feed_page()
        assert self.order_feed_page.check_number_order_in_feed_order(order[1:])



