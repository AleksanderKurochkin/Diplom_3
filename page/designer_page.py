from page.base_page import BasePage
from base.links import Links
import allure


class DesignerPage(BasePage):

    BUTTON_PERSONAL_ACCOUNT = ("xpath", "(//nav//a//p)[3]")
    BUTTON_ORDER_FEED = ('xpath', '//p[contains(text(), "Лента")] | //p[text()="Лента заказов"]')
    BUTTON_INGREDIENT = ('xpath', '//ul//p[text()="Флюоресцентная булка R2-D3"]')
    BUTTON_EXIT_WINDOW_DETAILS = ('xpath', '(//button[@type="button"])[1]')
    BUTTON_CREATE_ORDER = ('xpath', '//button[text() = "Оформить заказ"]')
    WINDOW_DETAILS = ('xpath', '//*[contains(text(), "Детали ингредиента")]')
    SOME_INGREDIENT_BREAD = ('xpath', '//ul//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"] | (//a[@class="burger-ingredient_article__wQtAl"])[2]')
    COUNTER_BREAD = 'xpath', '(//section//div//a//div//p[@class="counter_counter__num__3nue1"])[1]'
    PLACE_INGREDIENT = ('xpath', '//section//ul[@class="BurgerConstructor_basket__list__l9dp_"] | //section[@class="burger-constructor_burger_constructor__jXyGp"]')
    NUMBER_ORDER = ('xpath', '//div[contains(@class, "Modal_modal__contentBox")]/h2')
    NAME_WINDOW_DETAILS = "Детали ингредиента"
    NAME_BUTTON_CREATE_ORDER = "Оформить заказ"

    @allure.step('Открываем страницу конструктора')
    def open_designer_page(self):
        self.open_page(Links.DESIGNER_PAGE)

    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_on_element_visibility(self.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_button_order_feed(self):
        self.click_on_element(self.BUTTON_ORDER_FEED)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_button_create_order(self):
        self.click_on_element(self.BUTTON_CREATE_ORDER)

    @allure.step('Проверяем, что открылось окно конструктора')
    def check_window_designer_page(self):
        actual_url = self.get_url_with_wait(Links.DESIGNER_PAGE)
        expected_url = Links.DESIGNER_PAGE
        return actual_url == expected_url

    @allure.step('Нажимаем на ингредиент')
    def click_ingredient(self):
        self.click_on_element(self.BUTTON_INGREDIENT)

    @allure.step('Ожидаем появления всплывающего окна с описанием ингредиента')
    def check_window_details(self):
        return self.get_text_from_element(self.WINDOW_DETAILS) == self.NAME_WINDOW_DETAILS

    @allure.step('Нажимаем на кнопку крестик окна "Детали ингредиента"')
    def click_button_exit_window_details(self):
        self.click_on_element(self.BUTTON_EXIT_WINDOW_DETAILS)

    @allure.step('Ожидаем что закроется всплывающее окна с описанием ингредиента')
    def check_exit_window_details(self):
        return self.check_element_disappears(self.WINDOW_DETAILS)

    @allure.step('Ожидаем появления кнопки c текстом "Оформить заказ"')
    def check_button_create_order(self):
        return self.get_text_from_element(self.BUTTON_CREATE_ORDER) == "Оформить заказ"

    @allure.step('Добавляем ингредиент "Булка" в состав')
    def add_ingredient_bread(self):
        self.add_ingredient(self.SOME_INGREDIENT_BREAD, self.PLACE_INGREDIENT)

    @allure.step('Получаем счетчик ингредиента "Булка"')
    def get_ingredient_counter(self):
        counter = self.get_text_from_element(self.COUNTER_BREAD)
        return counter

    @allure.step('Получаем номер заказа')
    def get_number_order(self):
        order_number = self.get_text_from_element(self.NUMBER_ORDER)
        return order_number













