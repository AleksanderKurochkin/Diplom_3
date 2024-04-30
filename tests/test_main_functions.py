import allure
from base.BaseTest import BaseTest


class TestMainFunction(BaseTest):

    @allure.title('Переход в ленту заказов')
    @allure.description('Переход по клику на кнопку "Лента заказов"')
    def test_open_window_order_feed(self):
        self.designer_page.open_designer_page()
        self.designer_page.click_button_order_feed()
        assert self.order_feed_page.check_window_order_feed()

    @allure.title('Переход в конструктор')
    @allure.description('Переход по клику на кнопку "Конструктор"')
    def test_open_window_designer(self):
        self.order_feed_page.open_order_feed_page()
        self.order_feed_page.click_button_designer()
        assert self.designer_page.check_window_designer_page()

    @allure.title('Проверка всплывающего окна с деталями')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями,')
    def test_open_window_details(self):
        self.designer_page.open_designer_page()
        self.designer_page.click_ingredient()
        assert self.designer_page.check_window_details()

    @allure.title('Проверка закрытия всплывающего окна с деталями')
    @allure.description('Если кликнуть на крестик, закроется всплывающее окно с деталями,')
    def test_exit_window_details(self):
        self.designer_page.open_designer_page()
        self.designer_page.click_ingredient()
        self.designer_page.click_button_exit_window_details()
        assert self.designer_page.check_exit_window_details()

    @allure.title('Проверка счетчика ингредиента.')
    @allure.description('При добавлении ингредиента "Булка" в заказ, счётчик этого ингредиента увеличивается на 2')
    def test_count_ingredient(self):
        self.designer_page.open_designer_page()
        initial_counter = self.designer_page.get_ingredient_counter()
        self.designer_page.add_ingredient_bread()
        self.designer_page.get_ingredient_counter()
        current_counter = self.designer_page.get_ingredient_counter()
        assert current_counter == f"{int(initial_counter) + 2}"

    @allure.title('Проверка залогиненный пользователь может оформить заказ.')
    @allure.description('Если пользователь залогинен, то на странице конструктора появляется кнопка "Оформить заказ"')
    def test_visible_button_create_order(self):
        self.login_page.login_user()
        assert self.designer_page.check_button_create_order()
